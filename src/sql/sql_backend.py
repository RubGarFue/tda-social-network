##
#
# MODULE: sql_backend
#
# DESCRIPTION: Este módulo se usa para la conexión con la base de datos y la realización de
#              consultas SQL a la base de datos deseada.
#
##


import sys, traceback
from sqlalchemy import create_engine
from sqlalchemy import MetaData

# Configuracion general bases de datos
user = None #! USER FOR DATABASE
password = None #! PASSWORD FOR DATABASE
host = None #! HOST FOR DATABASE
post = None #! PORT FOR DATABASE

# Configuracion motor prueba db
database = 'prueba'

url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, post, database)

prueba_engine = create_engine(url, echo=False)
prueba_meta = MetaData(bind=prueba_engine)

# Configuracion motor test_high_index
database = 'test_high_index'

url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, post, database)

hindex_engine = create_engine(url, echo=False)
hindex_meta = MetaData(bind=hindex_engine)

# Configuracion motor test_low_index
database = 'test_low_index'

url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, post, database)

lindex_engine = create_engine(url, echo=False)
lindex_meta = MetaData(bind=lindex_engine)

# Configuracion motor phpmyadmin
database = 'phpmyadmin'

url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, post, database)

phpmyadmin_engine = create_engine(url, echo=False)
phpmyadmin_meta = MetaData(bind=phpmyadmin_engine)

# Configuración motor reduced
database = 'reduced_db'

url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, post, database)

reduced_db_engine = create_engine(url, echo=False)
reduced_db_meta = MetaData(bind=reduced_db_engine)


##################################################################################################
##                                                                                              ##
##                                   FUNCIONES DE CONEXIÓN                                      ##
##                                                                                              ##
##################################################################################################

##
#
# FUNCTION: get_engine
#
# DESCRIPTION: Funcion para obtener el motor de la base de datos
#
# PARAM: str - Nombre de la base de datos
# RETURN: engine - Motor de la base de datos
#
##
def get_engine(str):
    if str == 'prueba':
        return prueba_engine
    elif str == 'test_high_index':
        return hindex_engine
    elif str == 'test_low_index':
        return lindex_engine
    elif str == 'phpmyadmin':
        return phpmyadmin_engine
    elif str == 'reduced_db':
        return reduced_db_engine
    else:
        return None

##
#
# FUNCTION: db_error
#
# DESCRIPTION: Funcion para manejar los errores de la base de datos
#
# PARAM: db_conn - Conexion a la base de datos
# RETURN: 'Something is broken'
#
##
def db_error(db_conn):
    if db_conn is not None:
        db_conn.close()
    print("Exception in DB access:")
    print("-"*60)
    traceback.print_exc(file=sys.stdout)
    print("-"*60)

    return 'Something is broken'

#!! COMENTARIO: Lo de los user_id está mal expresado (dentro de user está el id (user.id) y el
#!! user_id (user.user_id)). Pero en otras tablas el user_id es el user.id

# Query para calcular (posteriormente) distancia entre dos usuarios (entre nodos conectados)
'''
SELECT author_user.user_id, liked_user.user_id
FROM tweet INNER JOIN like_tweet
ON tweet.id = like_tweet.tweet_id
INNER JOIN user AS author_user
ON tweet.author_id = author_user.id
INNER JOIN user AS liked_user
ON like_tweet.user_id = liked_user.id
WHERE (author_user.user_id = 262749833 AND liked_user.user_id = 50982086)
OR (author_user.user_id = 50982086 AND liked_user.user_id = 262749833);
'''


##################################################################################################
##                                                                                              ##
##                             FUNCIONES DISTANCIA DE ADYACENCIA                                ##
##                                                                                              ##
##################################################################################################

##
#
# FUNCTION: neighbours
#
# DESCRIPTION: Funcion para obtener los vecinos de un usuario
#
# PARAM: user - Usuario del que se quieren obtener los vecinos
# RETURN: neighbours - Lista de vecinos del usuario
#
##
def neighbours(db_engine, user):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result1 = db_conn.execute("SELECT DISTINCT liked_user.user_id\
                                      FROM tweet INNER JOIN like_tweet\
                                      ON tweet.id = like_tweet.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN user AS liked_user\
                                      ON like_tweet.user_id = liked_user.id\
                                      WHERE author_user.user_id = " + str(user))
        
        # Query de los vecinos de un usuario (usuarios a los que el usuario ha dado like)
        db_result2 = db_conn.execute("SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN like_tweet\
                                      ON tweet.id = like_tweet.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN user AS liked_user\
                                      ON like_tweet.user_id = liked_user.id\
                                      WHERE liked_user.user_id = " + str(user))
        
        # Query de los vecinos de un usuario (usuarios que han retweeteado los tweets del usuario)
        db_result3 = db_conn.execute("SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN retweet\
                                      ON tweet.id = retweet.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN tweet AS retweeted\
                                      ON retweet.retweeted = retweeted.tweet_id\
                                      INNER JOIN user AS retweeted_user\
                                      ON retweeted.author_id = retweeted_user.id\
                                      WHERE retweeted_user.user_id = " + str(user))

        # Query de los vecinos de un usuario (usuarios a los que el usuario ha retweeteado)
        db_result4 = db_conn.execute("SELECT DISTINCT retweeted_user.user_id\
                                      FROM tweet INNER JOIN retweet\
                                      ON tweet.id = retweet.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN tweet AS retweeted\
                                      ON retweet.retweeted = retweeted.tweet_id\
                                      INNER JOIN user AS retweeted_user\
                                      ON retweeted.author_id = retweeted_user.id\
                                      WHERE author_user.user_id = " + str(user))
        
        # Query de los vecinos de un usuario (usuarios que han mencionado al usuario)
        db_result5 = db_conn.execute("SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN mention\
                                      ON tweet.id = mention.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN user AS mentioned_user\
                                      ON mention.user_id = mentioned_user.id\
                                      WHERE mentioned_user.user_id = " + str(user))
        
        # Query de los vecinos de un usuario (usuarios que han sido mencionados por el usuario)
        db_result6 = db_conn.execute("SELECT DISTINCT mentioned_user.user_id\
                                      FROM tweet INNER JOIN mention\
                                      ON tweet.id = mention.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN user AS mentioned_user\
                                      ON mention.user_id = mentioned_user.id\
                                      WHERE author_user.user_id = " + str(user))
        
        # Query de los vecinos de un usuario (usuarios que han respondido a los tweets del usuario)
        db_result7 = db_conn.execute("SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN reply\
                                      ON tweet.id = reply.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      WHERE reply.reply_to= " + str(user))
        
        # Query de los vecinos de un usuario (usuarios a los que el usuario ha respondido)
        db_result8 = db_conn.execute("SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN reply\
                                      ON tweet.id = reply.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      WHERE reply.reply_to= " + str(user))
        
        db_conn.close()

        neighbours = []

        for row in db_result1:
            neighbours.append(str(row.user_id))
        
        for row in db_result2:
            if row.user_id not in neighbours:
                neighbours.append(str(row.user_id))
        
        for row in db_result3:
            if row.user_id not in neighbours:
                neighbours.append(str(row.user_id))

        for row in db_result4:
            if row.user_id not in neighbours:
                neighbours.append(str(row.user_id))

        for row in db_result5:
            if row.user_id not in neighbours:
                neighbours.append(str(row.user_id))

        for row in db_result6:
            if row.user_id not in neighbours:
                neighbours.append(str(row.user_id))

        for row in db_result7:
            if row.user_id not in neighbours:
                neighbours.append(str(row.user_id))

        for row in db_result8:
            if row.user_id not in neighbours:
                neighbours.append(str(row.user_id))
                
        return neighbours
        
    except:
        return db_error(db_conn)

##
#
# FUNCTION: fast_neighbours
#
# DESCRIPTION: Devuelve los vecinos de un usuario
#
# PARAM: db_engine: motor de la base de datos
#        user: usuario del que se quieren obtener los vecinos
# RETURN: lista de vecinos del usuario
#
##
def fast_neighbours(db_engine, user):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN retweet\
                                      ON tweet.id = retweet.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN tweet AS retweeted\
                                      ON retweet.retweeted = retweeted.tweet_id\
                                      INNER JOIN user AS retweeted_user\
                                      ON retweeted.author_id = retweeted_user.id\
                                      WHERE retweeted_user.user_id = " + str(user) + "\
                                          UNION\
                                      SELECT DISTINCT retweeted_user.user_id\
                                      FROM tweet INNER JOIN retweet\
                                      ON tweet.id = retweet.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN tweet AS retweeted\
                                      ON retweet.retweeted = retweeted.tweet_id\
                                      INNER JOIN user AS retweeted_user\
                                      ON retweeted.author_id = retweeted_user.id\
                                      WHERE author_user.user_id = " + str(user) + "\
                                          UNION\
                                      SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN mention\
                                      ON tweet.id = mention.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN user AS mentioned_user\
                                      ON mention.user_id = mentioned_user.id\
                                      WHERE mentioned_user.user_id = " + str(user) + "\
                                         UNION\
                                      SELECT DISTINCT mentioned_user.user_id\
                                      FROM tweet INNER JOIN mention\
                                      ON tweet.id = mention.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN user AS mentioned_user\
                                      ON mention.user_id = mentioned_user.id\
                                      WHERE author_user.user_id = " + str(user) + "\
                                         UNION\
                                      SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN reply\
                                      ON tweet.id = reply.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      WHERE reply.reply_to = " + str(user) + "\
                                          UNION\
                                      SELECT DISTINCT reply.reply_to\
                                      FROM tweet INNER JOIN reply\
                                      ON tweet.id = reply.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      WHERE reply.reply_to = " + str(user))
        
        #! Query de los vecinos de un usuario (incluyendo likes)
        '''"SELECT DISTINCT liked_user.user_id\
                                      FROM tweet INNER JOIN like_tweet\
                                      ON tweet.id = like_tweet.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN user AS liked_user\
                                      ON like_tweet.user_id = liked_user.id\
                                      WHERE author_user.user_id = " + str(user) + "\
                                          UNION\
                                      SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN like_tweet\
                                      ON tweet.id = like_tweet.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN user AS liked_user\
                                      ON like_tweet.user_id = liked_user.id\
                                      WHERE liked_user.user_id = " + str(user) + "\
                                          UNION\
                                      SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN retweet\
                                      ON tweet.id = retweet.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN tweet AS retweeted\
                                      ON retweet.retweeted = retweeted.tweet_id\
                                      INNER JOIN user AS retweeted_user\
                                      ON retweeted.author_id = retweeted_user.id\
                                      WHERE retweeted_user.user_id = " + str(user) + "\
                                          UNION\
                                      SELECT DISTINCT retweeted_user.user_id\
                                      FROM tweet INNER JOIN retweet\
                                      ON tweet.id = retweet.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN tweet AS retweeted\
                                      ON retweet.retweeted = retweeted.tweet_id\
                                      INNER JOIN user AS retweeted_user\
                                      ON retweeted.author_id = retweeted_user.id\
                                      WHERE author_user.user_id = " + str(user) + "\
                                          UNION\
                                      SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN mention\
                                      ON tweet.id = mention.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN user AS mentioned_user\
                                      ON mention.user_id = mentioned_user.id\
                                      WHERE mentioned_user.user_id = " + str(user) + "\
                                         UNION\
                                      SELECT DISTINCT mentioned_user.user_id\
                                      FROM tweet INNER JOIN mention\
                                      ON tweet.id = mention.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      INNER JOIN user AS mentioned_user\
                                      ON mention.user_id = mentioned_user.id\
                                      WHERE author_user.user_id = " + str(user) + "\
                                         UNION\
                                      SELECT DISTINCT author_user.user_id\
                                      FROM tweet INNER JOIN reply\
                                      ON tweet.id = reply.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      WHERE reply.reply_to = " + str(user) + "\
                                          UNION\
                                      SELECT DISTINCT reply.reply_to\
                                      FROM tweet INNER JOIN reply\
                                      ON tweet.id = reply.tweet_id\
                                      INNER JOIN user AS author_user\
                                      ON tweet.author_id = author_user.id\
                                      WHERE reply.reply_to = " + str(user))'''
        
        db_conn.close()

        neighbours = []

        for row in db_result:
            neighbours.append(str(row.user_id))
                
        return neighbours
        
    except:
        return db_error(db_conn)


##################################################################################################
##                                                                                              ##
##                                       FUNCIONES PESOS                                        ##
##                                                                                              ##
##################################################################################################

##
#
# FUNCTION: total_likes
#
# DESCRIPTION: Funcion para obtener el numero total de likes
#
# PARAM: -
# RETURN: total_likes - Numero total de likes
#
##
def total_likes(db_engine):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                    FROM like_tweet")

        db_conn.close()

        return db_result.fetchone()[0]

    except:
        return db_error(db_conn)

##
#
# FUNCTION: total_tweets
#
# DESCRIPTION: Funcion para obtener el numero total de tweets
#
# PARAM: -
# RETURN: total_tweets - Numero total de tweets
#
##
def total_tweets(db_engine):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                    FROM tweet")

        db_conn.close()

        return db_result.fetchone()[0]

    except:
        return db_error(db_conn)

##
#
# FUNCTION: total_retweets
#
# DESCRIPTION: Funcion para obtener el numero total de retweets
#
# PARAM: -
# RETURN: total_retweets - Numero total de retweets
#
##
def total_retweets(db_engine):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                    FROM retweet")

        db_conn.close()

        return db_result.fetchone()[0]

    except:
        return db_error(db_conn)

##
#
# FUNCTION: total_mentions
#
# DESCRIPTION: Funcion para obtener el numero total de menciones
#
# PARAM: -
# RETURN: total_mentions - Numero total de menciones
#
##
def total_mentions(db_engine):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                    FROM mention")

        db_conn.close()

        return db_result.fetchone()[0]

    except:
        return db_error(db_conn)

##
#
# FUNCTION: total_replies
#
# DESCRIPTION: Funcion para obtener el numero total de replies
#
# PARAM: -
# RETURN: total_replies - Numero total de replies
#
##
def total_replies(db_engine):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                    FROM reply")

        db_conn.close()

        return db_result.fetchone()[0]

    except:
        return db_error(db_conn)

##
#
# FUNCTION: nlinks
#
# DESCRIPTION: Funcion para obtener el numero de enlaces (likes) entre dos usuarios
#
# PARAM: user1 - Usuario 1
#        user2 - Usuario 2
# RETURN: nlinks - Numero de enlaces entre los dos usuarios
#
##
def nlikes(db_engine, user1, user2):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                    FROM\
                                    (SELECT author_user.user_id AS author_id, liked_user.user_id AS liked_id\
                                    FROM tweet INNER JOIN like_tweet\
                                    ON tweet.id = like_tweet.tweet_id\
                                    INNER JOIN user AS author_user\
                                    ON tweet.author_id = author_user.id\
                                    INNER JOIN user AS liked_user\
                                    ON like_tweet.user_id = liked_user.id\
                                    WHERE (author_user.user_id = " + str(user1) +
                                           " AND liked_user.user_id = " + str(user2) + ")\
                                    OR (author_user.user_id = " + str(user2) +
                                        " AND liked_user.user_id = " + str(user1) +")) AS likes;")

        db_conn.close()

        return db_result.fetchone()[0]
        
    except:
        return db_error(db_conn)

##
#
# FUNCTION: nretweets
#
# DESCRIPTION: Funcion para obtener el numero de retweets entre dos usuarios
#
# PARAM: user1 - Usuario 1
#        user2 - Usuario 2
# RETURN: nretweets - Numero de retweets entre los dos usuarios
#
##
def nretweets(db_engine, user1, user2):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                     FROM\
                                     (SELECT author_user.user_id AS author_id, retweeted_user.user_id AS retweeted_id\
                                     FROM tweet INNER JOIN retweet\
                                     ON tweet.id = retweet.tweet_id\
                                     INNER JOIN user AS author_user\
                                     ON tweet.author_id = author_user.id\
                                     INNER JOIN tweet AS retweeted\
                                     ON retweet.retweeted = retweeted.tweet_id\
                                     INNER JOIN user AS retweeted_user\
                                     ON retweeted.author_id = retweeted_user.id\
                                     WHERE (author_user.user_id = " + str(user1) +
                                            " AND retweeted_user.user_id = " + str(user2) + ")\
                                     OR (author_user.user_id = " + str(user2) +
                                         " AND retweeted_user.user_id = " + str(user1) + ")) AS retweets;")

        db_conn.close()

        return db_result.fetchone()[0]
        
    except:
        return db_error(db_conn)

##
#
# FUNCTION: nmentions
#
# DESCRIPTION: Funcion para obtener el numero de menciones entre dos usuarios
#
# PARAM: user1 - Usuario 1
#        user2 - Usuario 2
# RETURN: nmentions - Numero de menciones entre los dos usuarios
#
##
def nmentions(db_engine, user1, user2):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                     FROM\
                                     (SELECT author_user.user_id AS author_id, mentioned_user.user_id AS mentioned_id\
                                     FROM tweet INNER JOIN mention\
                                     ON tweet.id = mention.tweet_id\
                                     INNER JOIN user AS author_user\
                                     ON tweet.author_id = author_user.id\
                                     INNER JOIN user AS mentioned_user\
                                     ON mention.user_id = mentioned_user.id\
                                     WHERE (author_user.user_id = " + str(user1) +
                                            " AND mentioned_user.user_id = " + str(user2) + ")\
                                     OR (author_user.user_id = " + str(user2) +
                                         " AND mentioned_user.user_id = " + str(user1) + ")) AS mentions;")

        return db_result.fetchone()[0]
        
    except:
        return db_error(db_conn)

##
#
# FUNCTION: nreplies
#
# DESCRIPTION: Funcion para obtener el numero de replies entre dos usuarios
#
# PARAM: user1 - Usuario 1
#        user2 - Usuario 2
# RETURN: nreplies - Numero de replies entre los dos usuarios
#
##
def nreplies(db_engine, user1, user2):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                     FROM\
                                     (SELECT author_user.user_id AS author_id, reply.reply_to AS reply_id\
                                     FROM tweet INNER JOIN reply\
                                     ON tweet.id = reply.tweet_id\
                                     INNER JOIN user AS author_user\
                                     ON tweet.author_id = author_user.id\
                                     WHERE (author_user.user_id = " + str(user1) +
                                            " AND reply.reply_to = " + str(user2) + ")\
                                     OR (author_user.user_id = " + str(user2) +
                                         " AND reply.reply_to= " + str(user1) + ")) AS replies;")

        return db_result.fetchone()[0]
    
    except:
        return db_error(db_conn)


##################################################################################################
##                                                                                              ##
##                                     FUNCIONES TOP_USERS                                      ##
##                                                                                              ##
##################################################################################################

##
#
# FUNCTION: user_tweets
#
# DESCRIPTION: Funcion para obtener el numero de tweets de cada usuario
#
# PARAM: db_engine - Motor de la base de datos
# RETURN: dict_user - Diccionario con el numero de tweets de cada usuario
#
##
def user_tweets(db_engine):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los usuarios y el respectivo numero de tweets
        db_result = db_conn.execute("SELECT author_user.user_id AS author_id, COUNT(tweet.tweet_id) AS count\
                                    FROM tweet INNER JOIN user AS author_user\
                                    ON tweet.author_id = author_user.id\
                                    GROUP BY author_id;")

        db_conn.close()

        dict_user = {row.author_id: int(row.count) for row in db_result}

        return dict_user
        
    except:
        return db_error(db_conn)

##
#
# FUNCTION: user_retweets
#
# DESCRIPTION: Funcion para obtener el numero de retweets de cada usuario
#
# PARAM: db_engine - Motor de la base de datos
# RETURN: dict_user - Diccionario con el numero de retweets de cada usuario
#
##
def user_retweets(db_engine):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los usuarios y el respectivo numero de retweets
        db_result = db_conn.execute("SELECT author_user.user_id AS author_id, COUNT(retweet.tweet_id) AS count\
                                    FROM tweet INNER JOIN retweet\
                                    ON tweet.id = retweet.tweet_id\
                                    INNER JOIN user AS author_user\
                                    ON tweet.author_id = author_user.id\
                                    GROUP BY author_id;")

        db_conn.close()

        dict_user = {row.author_id: int(row.count) for row in db_result}

        return dict_user
    
    except:
        return db_error(db_conn)

##
#
# FUNCTION: user_mentions
#
# DESCRIPTION: Funcion para obtener el numero de menciones de cada usuario
#
# PARAM: db_engine - Motor de la base de datos
# RETURN: dict_user - Diccionario con el numero de menciones de cada usuario
#
##
def user_mentions(db_engine):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los usuarios y el respectivo numero de menciones
        db_result = db_conn.execute("SELECT author_user.user_id AS author_id, COUNT(mention.tweet_id) AS count\
                                     FROM tweet INNER JOIN mention\
                                     ON tweet.id = mention.tweet_id\
                                     INNER JOIN user AS author_user\
                                     ON tweet.author_id = author_user.id\
                                     GROUP BY author_id;")

        db_conn.close()

        dict_user = {row.author_id: int(row.count) for row in db_result}

        return dict_user
    
    except:
        return db_error(db_conn)

##
#
# FUNCTION: user_replies
#
# DESCRIPTION: Funcion para obtener el numero de replies de cada usuario
#
# PARAM: db_engine - Motor de la base de datos
# RETURN: dict_user - Diccionario con el numero de replies de cada usuario
#
##
def user_replies(db_engine):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los usuarios y el respectivo numero de replies
        db_result = db_conn.execute("SELECT author_user.user_id AS author_id, COUNT(reply.tweet_id) AS count\
                                     FROM tweet INNER JOIN reply\
                                     ON tweet.id = reply.tweet_id\
                                     INNER JOIN user AS author_user\
                                     ON tweet.author_id = author_user.id\
                                     GROUP BY author_id;")

        db_conn.close()

        dict_user = {row.author_id: int(row.count) for row in db_result}

        return dict_user
    
    except:
        return db_error(db_conn)

###################################################################################################

##
#
# FUNCTION: nretweets
#
# DESCRIPTION: Funcion para obtener el numero de retweets de un usuario
#
# PARAM: user - Usuario
# RETURN: nretweets - Numero de retweets del usuario
#
##
def user_nretweets(db_engine, user):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                     FROM\
                                     (SELECT author_user.user_id AS author_id, retweeted_user.user_id AS retweeted_id\
                                     FROM tweet INNER JOIN retweet\
                                     ON tweet.id = retweet.tweet_id\
                                     INNER JOIN user AS author_user\
                                     ON tweet.author_id = author_user.id\
                                     INNER JOIN tweet AS retweeted\
                                     ON retweet.retweeted = retweeted.tweet_id\
                                     INNER JOIN user AS retweeted_user\
                                     ON retweeted.author_id = retweeted_user.id\
                                     WHERE (author_user.user_id = " + str(user) +
                                            " OR retweeted_user.user_id = " + str(user) + ")) AS retweets;")

        db_conn.close()

        return db_result.fetchone()[0]
        
    except:
        return db_error(db_conn)

##
#
# FUNCTION: nmentions
#
# DESCRIPTION: Funcion para obtener el numero de menciones de un usuarios
#
# PARAM: user - Usuario
# RETURN: nmentions - Numero de menciones del usuario
#
##
def user_nmentions(db_engine, user):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                     FROM\
                                     (SELECT author_user.user_id AS author_id, mentioned_user.user_id AS mentioned_id\
                                     FROM tweet INNER JOIN mention\
                                     ON tweet.id = mention.tweet_id\
                                     INNER JOIN user AS author_user\
                                     ON tweet.author_id = author_user.id\
                                     INNER JOIN user AS mentioned_user\
                                     ON mention.user_id = mentioned_user.id\
                                     WHERE (author_user.user_id = " + str(user) +
                                            " OR mentioned_user.user_id = " + str(user) + ")) AS mentions;")

        return db_result.fetchone()[0]
        
    except:
        return db_error(db_conn)

##
#
# FUNCTION: nreplies
#
# DESCRIPTION: Funcion para obtener el numero de replies de un usuario
#
# PARAM: user - Usuario
# RETURN: nreplies - Numero de replies del usuario
#
##
def user_nreplies(db_engine, user):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los vecinos de un usuario (usuarios que han dado like a los tweets del usuario)
        db_result = db_conn.execute("SELECT COUNT(*)\
                                     FROM\
                                     (SELECT author_user.user_id AS author_id, reply.reply_to AS reply_id\
                                     FROM tweet INNER JOIN reply\
                                     ON tweet.id = reply.tweet_id\
                                     INNER JOIN user AS author_user\
                                     ON tweet.author_id = author_user.id\
                                     WHERE (author_user.user_id = " + str(user) +
                                            " OR reply.reply_to= " + str(user) + ")) AS replies;")

        return db_result.fetchone()[0]
    
    except:
        return db_error(db_conn)


##################################################################################################
##                                                                                              ##
##                                      FUNCIONES PAGERANK                                      ##
##                                                                                              ##
##################################################################################################

##
#
# FUNCTION: users
#
# DESCRIPTION: Funcion para obtener los usuarios de la base de datos
#
# RETURN: usuarios - Lista de usuarios de la base de datos
#
##
def users(db_engine):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los usuarios
        db_result = db_conn.execute("SELECT user_id\
                                     FROM user")

        db_conn.close()

        users = []

        for row in db_result:
            users.append(str(row.user_id))
        
        return users
        
    except:
        return db_error(db_conn)

##
#
# FUNCTION: likes
#
# DESCRIPTION: Funcion para obtener los likes de un usuario
#
# PARAM: user - Usuario del que se quieren obtener los likes
# RETURN: likes - Lista de likes del usuario
#
##
def likes(db_engine, user):
    try:
        # Conexion a la base de datos
        db_conn = None
        db_conn = db_engine.connect()

        # Query de los likes dados por un usuario
        db_result = db_conn.execute("SELECT author_user.user_id\
                                     FROM tweet INNER JOIN like_tweet\
                                     ON tweet.id = like_tweet.tweet_id\
                                     INNER JOIN user AS author_user\
                                     ON tweet.author_id = author_user.id\
                                     INNER JOIN user AS liked_user\
                                     ON like_tweet.user_id = liked_user.id\
                                     WHERE liked_user.user_id = " + str(user))

        db_conn.close()

        likes = []

        for row in db_result:
            likes.append(str(row.user_id))
        
        return likes
        
    except:
        return db_error(db_conn)