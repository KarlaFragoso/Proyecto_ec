import web

db_host = 'localhost'
db_name = 'proyecto_ec'
db_user = 'AK'
db_pw = 'AK.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )