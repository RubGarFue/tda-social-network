##
# MODULE: top_users
#
# DESCRIPTION: Módulo para calcular los usuarios con más actividad de un grafo
#
##

import sql.sql_backend as sql

##
#
# FUNCTION: top_users
#
# DESCRIPTION: Funcion para calcular los usuarios con más actividad de un grafo
#
# PARAM: db_engine - Motor de la base de datos
#        user - Usuario
# RETURN: top_users - Lista de usuarios con más actividad
#
##
def top_users(db_engine):

    dict_tweets = sql.user_tweets(db_engine)
    dict_retweets = sql.user_retweets(db_engine)
    dict_mentions = sql.user_mentions(db_engine)
    dict_replies = sql.user_replies(db_engine)

    dict_users = dict_tweets

    for user in dict_retweets:
        if user in dict_users:
            dict_users[user] += dict_retweets[user]
        else:
            dict_users[user] = dict_retweets[user]
    
    for user in dict_mentions:
        if user in dict_users:
            dict_users[user] += dict_mentions[user]
        else:
            dict_users[user] = dict_mentions[user]
    
    for user in dict_replies:
        if user in dict_users:
            dict_users[user] += dict_replies[user]
        else:
            dict_users[user] = dict_replies[user]
    
    top_users = sorted(dict_users, key=dict_users.get, reverse=True)

    return top_users