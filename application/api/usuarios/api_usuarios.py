import web
import config
import json


class Api_usuarios:
    def get(self, id_usuario):
        try:
            # http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=get
            if id_usuario is None:
                result = config.model.get_all_usuarios()
                usuarios_json = []
                for row in result:
                    tmp = dict(row)
                    usuarios_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(usuarios_json)
            else:
                # http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=get&id_usuario=1
                result = config.model.get_usuarios(int(id_usuario))
                usuarios_json = []
                usuarios_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(usuarios_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuarios_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)

# http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=put&id_usuario=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,usuario,clave,edad):
        try:
            config.model.insert_usuarios(nombre,usuario,clave,edad)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=delete&id_usuario=1
    def delete(self, id_usuario):
        try:
            config.model.delete_usuarios(id_usuario)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=update&id_usuario=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_usuario, nombre,usuario,clave,edad):
        try:
            config.model.edit_usuarios(id_usuario,nombre,usuario,clave,edad)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuarios_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_usuario=None,
            nombre=None,
            usuario=None,
            clave=None,
            edad=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_usuario=user_data.id_usuario

            nombre=user_data.nombre

            usuario=user_data.usuario

            clave=user_data.clave

            edad=user_data.edad

            # user_hash
            if user_hash == 'eba1c13c68d351dbc1d3f3d76a18d16d':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_usuario)
                elif action == 'put':
                    return self.put(nombre,usuario,clave,edad)
                elif action == 'delete':
                    return self.delete(id_usuario)
                elif action == 'update':
                    return self.update(id_usuario, nombre,usuario,clave,edad)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
