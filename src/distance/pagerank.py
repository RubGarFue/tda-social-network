##
#
# MODULE: pagerank
#
# DESCRIPTION: Módulo para calcular el pagerank de los usuarios de una red
#
# !WARNING: Módulo obsoleto (no recomendado su uso)
#
##


import os
import sql.sql_backend as sql
import igraph as ig


##
#
# FUNCTION: pagerank
#
# DESCRIPTION: Funcion para calcular el pagerank de los usuarios
#
# RETURN: pagerank - Diccionario de pagerank de los usuarios
#
##
def pagerank(db_engine):
    G = ig.Graph()
    users = sql.users(db_engine)
    G.add_vertices(users)

    for user in users:
        for like in sql.likes(db_engine, user):
            G.add_edge(user, like)
    
    pagerank = {}

    for user, rank in zip(users, G.pagerank()):
        pagerank[int(user)] = float(rank)
    
    return pagerank


def print_graph(db_engine, name='graph.png'):
    G = ig.Graph(directed=True)
    users = sql.users(db_engine)
    G.add_vertices(users)

    for user in users:
        for like in sql.likes(db_engine, user):
            G.add_edge(user, like)
    
    file = os.path.realpath(__file__)
    file = '/'.join(file.split('/')[:-3])
    file += '/output/graphs/' + name
    
    ig.plot(G, vertex_label=users, target=file)