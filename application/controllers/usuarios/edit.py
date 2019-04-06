import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass


    def GET(self, id_usuario, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_usuario) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_usuario, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_usuario) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    

    @staticmethod
    def POST_EDIT(id_usuario, **k):
        

    @staticmethod
    def GET_EDIT(id_usuario, **k):
        message = None # Error message
        id_usuario = config.check_secure_val(str(id_usuario)) # HMAC id_usuario validate
        result = config.model.get_usuarios(int(id_usuario)) # search for the id_usuario
        result.id_usuario = config.make_secure_val(str(result.id_usuario)) # apply HMAC for id_usuario
        return config.render.edit(result, message) # render usuarios edit.html

     @staticmethod
    def POST_EDIT(id_usuario, **k):
        form = config.web.input()  # get form data
        form['id_usuario'] = config.check_secure_val(str(form['id_usuario'])) # HMAC id_usuario validate
        # edit user with new data
        result = config.model.edit_usuarios(
            form['id_usuario'],form['nombre'],form['usuario'],form['clave'],form['edad'],
        )
        if result == None: # Error on udpate data
            id_usuario = config.check_secure_val(str(id_usuario)) # validate HMAC id_usuario
            result = config.model.get_usuarios(int(id_usuario)) # search for id_usuario data
            result.id_usuario = config.make_secure_val(str(result.id_usuario)) # apply HMAC to id_usuario
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/usuarios') # render usuarios index.html
