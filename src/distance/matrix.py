##
#
# MODULE: matrix
#
# DESCRIPTION: Modulo para calcular la matriz de adyacencia y la matriz de distancias así como
#              los pesos de los enlaces del grafo
#
##


import sql.sql_backend as sql
import distance.distances as di

##
#
# FUNCTION: wieghts
#
# DESCRIPTION: Funcion para calcular los pesos de cada tipo de interaccion
#
# RETURN: weights - Diccionario de pesos
#
##
def weights(db_engine):
    #like_weight = 1/sql.total_likes(db_engine)
    retweet_weight = 1/sql.total_retweets(db_engine)
    mention_weight = 1/sql.total_mentions(db_engine)
    reply_weight = 1/sql.total_replies(db_engine)

    weights = {
        #'like_weight': like_weight,
        'retweet_weight': retweet_weight,
        'mention_weight': mention_weight,
        'reply_weight': reply_weight
    }

    return weights


##
#
# FUNCTION: adjacency_matrix
#
# DESCRIPTION: Funcion para calcular la matriz de adyacencia de un grafo
#
# PARAM: db_engine - Motor de la base de datos
#        save - Booleano para guardar la matriz de adyacencia en un csv
#
# RETURN: adj_mat - Matriz de adyacencia
#
##
def adjacency_matrix(db_engine, save = False):
    adj_mat = []

    weights_dict = weights(db_engine)

    users = sql.users(db_engine)
    
    i = 0
    for user1 in users:
        # Imprimimos el usuario que estamos calculando para ver el progreso
        print(user1 + ' - ' + str(i+1) + '/' + str(len(users)))

        adj_mat.append([])
        distances = di.adjacency_distance(db_engine, user1, users[:i], weights_dict)
        for user2 in users[:i]:
            adj_mat[-1].append(distances[user2])
        for _ in range(len(users)-i):
            adj_mat[-1].append(0)
        i += 1
        
        # Guardamos las distancias (de adyacencia) en un csv para no tener que estar calculándolas
        # siempre
        if save:
            with open('/home/rubgarfue/Escritorio/TFG-Informatica/matrix/adj_mat.csv', 'a') as f:
                f.write(','.join(str(x) for x in adj_mat[-1]) + '\n')

    return adj_mat


##
#
# FUNCTION: distance_matrix
#
# DESCRIPTION: Funcion para calcular la matriz de distancias de un grafo
#
# PARAM: db_engine - Motor de la base de datos
#        adj_mat - Matriz de adyacencia (si no se pasa, se carga de un csv)
#        save - Booleano para guardar la matriz de distancias en un csv
#
# RETURN: dist_mat - Matriz de distancias
#
##
def distance_matrix(db_engine, adj_mat = None, save = False):
    weights_dict = weights(db_engine)

    users = sql.users(db_engine)
    
    # Si no se pasa la matriz de adyacencia, la cargamos de un csv
    if adj_mat is None:
        with open('/home/rubgarfue/Escritorio/TFG-Informatica/matrix/adj_mat.csv', 'r') as f:
            lines = f.readlines()
        for line in lines:
            adj_mat.append([float(x) for x in line.split(',')])
    
    adj_dict = {}
    for user in users:
        adj_dict[user] = {}
    
    i = 1
    for user1, distances in zip(users, adj_mat):
        print(str(i) + '/' + str(len(users)))
        for user2, distance in zip(users, distances):
            if distance != '0' and distance != '0\n':
                adj_dict[user1][user2] = float(distance)
                adj_dict[user2][user1] = adj_dict[user1][user2]
        i += 1
    
    # Calculamos la matriz de distancias
    dist_mat = []
    
    print('\nCalculando matriz de distancias...')
    
    i = 0
    for user1 in users:
        # Imprimimos el usuario que estamos calculando para ver el progreso
        print(str(i) + '/' + str(len(users)))

        dist_mat.append([])
        distances = di.adjacency_to_distance(db_engine, user1, users[:i], adj_dict, weights_dict)
        for user2 in users[:i]:
            dist_mat[-1].append(distances[user2])
        for _ in range(len(users)-i):
            dist_mat[-1].append(0)
        i += 1

        # Guardamos las distancias en un csv para no tener que estar calculándolas
        if save:
            with open('/home/rubgarfue/Escritorio/TFG-Informatica/matrix/dist_mat.csv', 'a') as f:
                f.write(','.join(str(x) for x in dist_mat[-1]) + '\n')

    return dist_mat