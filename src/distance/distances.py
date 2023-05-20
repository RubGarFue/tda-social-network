##
#
# MODULE: distance
#
# DESCRIPTION: Este módulo se encarga de la obtención de distintas distancias entre usuarios,
#              entre ellas la distancia de adyacencia y la distancia de Dijkstra.
#
##


import sql.sql_backend as sql
#import distance.pagerank as pr
import numpy as np

# Global variables for weights

like_weight = 0
retweet_weight = 0
mention_weight = 0
reply_weight = 0


###################################################################################################
#                                                                                                 #
#                                   ADJACENCY TO DISTANCE                                         #
#                                                                                                 #
###################################################################################################

##
#
# FUNCTION: adjacency_to_distance
#
# DESCRIPTION: Está función calcula la distancia entre dos usuarios a partir de un diccionario de
#              adyacencia entre un usuario y una lista de usuarios
#
# PARAM: db_engine - Motor de la base de datos
#        user1 - Usuario origen
#        list_users - Lista de usuarios destino
#        adj_dict - Diccionario de adyacencia entre los usuarios de la red
#        weights_dict - Diccionario de pesos de las relaciones
#
# RETURN: distances - Diccionario de distancias entre el usuario y la lista de usuarios
#
##
def adjacency_to_distance(db_engine, user1, list_users, adj_dict, weights_dict):
    #global like_weight
    global retweet_weight
    global mention_weight
    global reply_weight

    #like_weight = weights_dict['like_weight']
    retweet_weight = weights_dict['retweet_weight']
    mention_weight = weights_dict['mention_weight']
    reply_weight = weights_dict['reply_weight']

    return _adjacency_to_distance(db_engine, user1, list_users, adj_dict, [], [], {})

##
#
# FUNCTION: _adjacency_to_distance
#
# DESCRIPTION: Función auxiliar para calcular la distancia entre dos usuarios a partir de un
#              diccionario de adyacencia entre un usuario y una lista de usuarios a partir de una
#              búsqueda en profundidad
#
# PARAM: db_engine - Motor de la base de datos
#        user1 - Usuario origen
#        list_users - Lista de usuarios destino
#        adj_dict - Diccionario de adyacencia entre los usuarios de la red
#        visited - Lista de usuarios visitados
#        unvisited - Lista de usuarios no visitados
#        distance - Diccionario de distancias entre el usuario y la lista de usuarios
#
# RETURN: distances - Diccionario de distancias entre el usuario y la lista de usuarios
#
##
def _adjacency_to_distance(db_engine, user1, list_users, adj_dict, visited=[], unvisited=[], distance={}):

    # Caso base
    if all(user in visited for user in list_users):
        distances = {}
        for user in list_users:
            distances[user] = distance[user]
        return distances
    
    # Si no se ha visitado el nodo, se calcula la distancia
    if not visited:
        distance[user1] = 0
    
    # Se visitan los vecinos
    neighbours = adj_dict[user1]
    for neighbour in neighbours:
        if neighbour not in visited:
            aux = adj_dict[user1][neighbour]
            new_distance = distance[user1] + aux
            if neighbour not in distance or new_distance < distance[neighbour]:
                distance[neighbour] = new_distance
    
    # Se marca el nodo como visitado
    visited.append(user1)

    if user1 in unvisited:
        unvisited.remove(user1)

    # Se elige el nodo no visitado con menor distancia
    for user in neighbours:
        if user not in visited and user not in unvisited:
            unvisited.append(user)
    
    if not unvisited:
        distances = {}
        for user in list_users:
            if user not in distance.keys():
                distance[user] = np.inf
            distances[user] = distance[user]
        return distances
    
    next_visit = unvisited[0]
    d = distance[unvisited[0]]

    for user in unvisited:
        if distance[user] < d:
            d = distance[user]
            next_visit = user
    
    # Se llama recursivamente al nodo elegido
    return _adjacency_to_distance(db_engine, next_visit, list_users, adj_dict, visited, unvisited, distance)


###################################################################################################
#                                                                                                 #
#                                      ADJACENCY DISTANCE                                         #
#                                                                                                 #
###################################################################################################

##
#
# FUNCTION: adjacency_distance
#
# DESCRIPTION: Está función calcula la distancia de adyacencia (distancia entre dos usuarios
#              conectados directamente mediante un enlace) entre un usuario y una lista de usuarios
#
# PARAM: db_engine - Motor de la base de datos
#        user1 - Usuario origen
#        list_users - Lista de usuarios destino
#        weights - Diccionario de pesos de las relaciones
#
# RETURN: distances - Diccionario de distancias de adyacencia entre el usuario y la lista de
#                     usuarios
#
##
def adjacency_distance(db_engine, user1, list_users, weights):
    #global like_weight
    global retweet_weight
    global mention_weight
    global reply_weight

    #like_weight = weights['like_weight']
    retweet_weight = weights['retweet_weight']
    mention_weight = weights['mention_weight']
    reply_weight = weights['reply_weight']

    return _adjacency_distance(db_engine, user1, list_users)

##
#
# FUNCTION: _adjacency_distance
#
# DESCRIPTION: Función auxiliar para calcular la distancia de adyacencia (distancia entre dos
#              usuarios conectados directamente mediante un enlace) entre un usuario y una lista
#              de usuarios
#
# PARAM: db_engine - Motor de la base de datos
#        user1 - Usuario origen
#        users - Lista de usuarios destino
#
# RETURN: distances - Diccionario de distancias de adyacencia entre el usuario y la lista de
#                     usuarios
#
##
def _adjacency_distance(db_engine, user1, users):

    distances = {}
    
    # Se visitan los vecinos
    neighbours = sql.fast_neighbours(db_engine, user1)
    for neighbour in neighbours:
        if neighbour in users:
            #aux = sql.nlikes(db_engine, user1, neighbour)*like_weight
            aux = sql.nretweets(db_engine, user1, neighbour)*retweet_weight
            aux += sql.nmentions(db_engine, user1, neighbour)*mention_weight
            aux += sql.nreplies(db_engine, user1, neighbour)*reply_weight
            if aux == 0:
                aux = 0
            else:
                aux = 1/aux
        else:
            aux = 0
        distances[neighbour] = aux
    
    for user in users:
        if user not in distances:
            distances[user] = 0
    
    return distances


###################################################################################################
#                                                                                                 #
#                                     DISTANCE (DIJKSTRA)                                         #
#                                                                                                 #
###################################################################################################

##
#
# FUNCTION: distance
#
# DESCRIPTION: Funcion para calcular la distancia entre dos usuarios mediante el algoritmo de
#              Dijkstra
#
# PARAM: db_engine - Motor de la base de datos
#        user1 - Usuario origen
#        users - Usuario o lista de usuarios destino
#        weights - Diccionario de pesos de las relaciones
#
# RETURN: distances - Diccionario de distancias entre el usuario y el usuario o lista de usuarios
#
##
def distance(db_engine, user1, users, weights):
    #global like_weight
    global retweet_weight
    global mention_weight
    global reply_weight

    #like_weight = weights['like_weight']
    retweet_weight = weights['retweet_weight']
    mention_weight = weights['mention_weight']
    reply_weight = weights['reply_weight']

    if type(users) == list:
        return _all_distance(db_engine, user1, users, [], [], {})
    else:
        return _distance(db_engine, user1, users, [], [], {})

##
#
# FUNCTION: _all_distance
#
# DESCRIPTION: Función auxiliar para calcular la distancia entre un usuario y una lista de usuarios
#              mediante el algoritmo de Dijkstra mediante llamadas recursivamente
#
# PARAM: db_engine - Motor de la base de datos
#        user1 - Usuario origen
#        list_users - Lista de usuarios destino
#        visited - Lista de usuarios visitados
#        unvisited - Lista de usuarios no visitados
#        distance - Diccionario de distancias
#
# RETURN: distances - Diccionario de distancias entre el usuario y la lista de usuarios
#
##
def _all_distance(db_engine, user1, list_users, visited=[], unvisited=[], distance={}):

    # Caso base
    if all(user in visited for user in list_users):
        distances = {}
        for user in list_users:
            distances[user] = distance[user]
        return distances
    
    # Si no se ha visitado el nodo, se calcula la distancia
    if not visited:
        distance[user1] = 0
    
    # Se visitan los vecinos
    neighbours = sql.fast_neighbours(db_engine, user1)
    for neighbour in neighbours:
        if neighbour not in visited:
            #aux = sql.nlikes(db_engine, user1, neighbour)*like_weight
            aux = sql.nretweets(db_engine, user1, neighbour)*retweet_weight
            aux += sql.nmentions(db_engine, user1, neighbour)*mention_weight
            aux += sql.nreplies(db_engine, user1, neighbour)*reply_weight
            if aux == 0:
                aux = np.inf
            else:
                aux = 1/aux
            new_distance = distance[user1] + aux
            if neighbour not in distance or new_distance < distance[neighbour]:
                distance[neighbour] = new_distance
    
    # Se marca el nodo como visitado
    visited.append(user1)

    if user1 in unvisited:
        unvisited.remove(user1)

    # Se elige el nodo no visitado con menor distancia
    for user in neighbours:
        if user not in visited and user not in unvisited:
            unvisited.append(user)
    
    if not unvisited:
        distances = {}
        for user in list_users:
            if user not in distance.keys():
                distance[user] = np.inf
            else:
                distances[user] = distance[user]
        return distances
    
    next_visit = unvisited[0]
    d = distance[unvisited[0]]

    for user in unvisited:
        if distance[user] < d:
            d = distance[user]
            next_visit = user
    
    # Se llama recursivamente al nodo elegido
    return _all_distance(db_engine, next_visit, list_users, visited, unvisited, distance)

##
#
# FUNCTION: _distance
#
# DESCRIPTION: Función auxiliar para calcular la distancia entre dos usuarios mediante el algoritmo
#              de Dijkstra de manera recursiva
#
# PARAM: db_engine - Motor de la base de datos
#        user1 - Usuario origen
#        user2 - Usuario destino
#        visited - Lista de usuarios visitados
#        unvisited - Lista de usuarios no visitados
#        distance - Diccionario de distancias
#
# RETURN: distance - Distancia entre el usuario y el usuario destino
#
##
def _distance(db_engine, user1, user2, visited=[], unvisited=[], distance={}):

    # Caso base
    if user1 == user2:
        if user2 not in distance:
            return 0
        else:
            return distance[user2]
    
    else :
        # Si no se ha visitado el nodo, se calcula la distancia
        if not visited:
            distance[user1] = 0
        
        # Se visitan los vecinos
        neighbours = sql.fast_neighbours(db_engine, user1)
        for neighbour in neighbours:
            if neighbour not in visited:
                #aux = sql.nlikes(db_engine, user1, neighbour)*like_weight
                aux = sql.nretweets(db_engine, user1, neighbour)*retweet_weight
                aux += sql.nmentions(db_engine, user1, neighbour)*mention_weight
                aux += sql.nreplies(db_engine, user1, neighbour)*reply_weight
                if aux == 0:
                    aux = np.inf
                else:
                    aux = 1/aux
                new_distance = distance[user1] + aux
                if neighbour not in distance or new_distance < distance[neighbour]:
                    distance[neighbour] = new_distance
        
        # Se marca el nodo como visitado
        visited.append(user1)

        if user1 in unvisited:
            unvisited.remove(user1)

        # Se elige el nodo no visitado con menor distancia
        for user in neighbours:
            u = str(user)
            if u not in visited and u not in unvisited:
                unvisited.append(u)
        
        if not unvisited:
            return np.inf
        
        next_visit = unvisited[0]
        d = distance[unvisited[0]]

        for user in unvisited:
            if distance[user] < d:
                d = distance[user]
                next_visit = user
        
        # Se llama recursivamente al nodo elegido
        return _distance(db_engine, next_visit, user2, visited, unvisited, distance)


###################################################################################################
#                                                                                                 #
#                                            UNUSED                                               #
#                                                                                                 #
###################################################################################################

##
#
# FUNCTION: pr_dijkstra
#
# DESCRIPTION: Algoritmo de Dijkstra para calcular la distancia mínima entre dos nodos usando
#              pagerank
#
# PARAM: user1 - Usuario 1
#        user2 - Usuario 2
#        pagerank - Diccionario de pagerank de los usuarios
#        visited - Lista de nodos visitados
#        unvisited - Lista de nodos no visitados
#        distance - Diccionario de distancias mínimas
#        predecessors - Diccionario de predecesores
#
# RETURN: distance - Distancia mínima entre los dos usuarios
#         predecessors - Diccionario de predecesores
#
##
'''
def pr_dijkstra(db_engine, user1, user2, pagerank, visited=[], unvisited=[], distance={}, predecessors={}):
    # Caso base
    if user1 == user2:
        if user2 not in distance:
            return 0, predecessors
        else:
            return distance[user2], predecessors
    
    else :
        # Si no se ha visitado el nodo, se calcula la distancia
        if not visited:
            distance[user1] = 0
        
        # Se visitan los vecinos
        for neighbour in sql.neighbours(db_engine, user1):
            n = int(neighbour)
            if n not in visited:
                sum = pagerank[user1]*len(sql.likes(db_engine, user1))
                sum += pagerank[n]*len(sql.likes(db_engine, n))
                sum *= len(sql.users(db_engine))
                new_distance = distance[user1] + 1/sum
                if n not in distance or new_distance < distance[n]:
                    distance[n] = new_distance
                    predecessors[n] = user1
        
        # Se marca el nodo como visitado
        visited.append(user1)

        if user1 in unvisited:
            unvisited.remove(user1)

        # Se elige el nodo no visitado con menor distancia
        for user in sql.neighbours(db_engine, user1):
            u = int(user)
            if u not in visited and u not in unvisited:
                unvisited.append(u)
        
        next_visit = unvisited[0]
        d = distance[unvisited[0]]

        for user in unvisited:
            if distance[user] < d:
                d = distance[user]
                next_visit = user
        
        # Se llama recursivamente al nodo elegido
        return pr_dijkstra(db_engine, next_visit, user2, pagerank, visited, unvisited, distance, predecessors)
'''