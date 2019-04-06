import web

'''
db_host = 'localhost'
db_name = 'proyecto_ec'
db_user = 'AK'
db_pw = 'AK.2019'
'''
db_host = 'gp96xszpzlqupw4k.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'kcearswidp97okju'
db_user = 'z66zzn1a0n9b4yru'
db_pw = 'avg3fwrsacxpj2mw'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )