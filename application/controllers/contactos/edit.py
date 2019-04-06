import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    def GET(self, id_contacto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_contacto) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_contacto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_contacto) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

 
        
    @staticmethod
    def GET_EDIT(id_contacto, **k):
        message = None # Error message
        id_contacto = config.check_secure_val(str(id_contacto)) # HMAC id_contacto validate
        result = config.model.get_contactos(int(id_contacto)) # search for the id_contacto
        result.id_contacto = config.make_secure_val(str(result.id_contacto)) # apply HMAC for id_contacto
        return config.render.edit(result, message) # render contactos edit.html

    @staticmethod
    def POST_EDIT(id_contacto, **k):
        form = config.web.input()  # get form data
        form['id_contacto'] = config.check_secure_val(str(form['id_contacto'])) # HMAC id_contacto validate
        # edit user with new data
        result = config.model.edit_contactos(
            form['id_contacto'],form['nombre'],form['telefono'],
        )
        if result == None: # Error on udpate data
            id_contacto = config.check_secure_val(str(id_contacto)) # validate HMAC id_contacto
            result = config.model.get_contactos(int(id_contacto)) # search for id_contacto data
            result.id_contacto = config.make_secure_val(str(result.id_contacto)) # apply HMAC to id_contacto
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/contactos') # render contactos index.html
