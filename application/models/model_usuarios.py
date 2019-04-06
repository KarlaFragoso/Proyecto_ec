import web
import config

db = config.db


def get_all_usuarios():
    try:
        return db.select('usuarios')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_usuarios(id_usuario):
    try:
        return db.select('usuarios', where='id_usuario=$id_usuario', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_usuarios(id_usuario):
    try:
        return db.delete('usuarios', where='id_usuario=$id_usuario', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_usuarios(nombre,usuario,clave,edad):
    try:
        return db.insert('usuarios',nombre=nombre,
usuario=usuario,
clave=clave,
edad=edad)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_usuarios(id_usuario,nombre,usuario,clave,edad):
    try:
        return db.update('usuarios',id_usuario=id_usuario,
nombre=nombre,
usuario=usuario,
clave=clave,
edad=edad,
                  where='id_usuario=$id_usuario',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
