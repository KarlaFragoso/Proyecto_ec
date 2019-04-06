import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_contacto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_contacto) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_contacto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_contacto) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html



    @staticmethod
    def POST_DELETE(id_contacto, **k):

   @staticmethod
    def GET_DELETE(id_contacto, **k):
        message = None # Error message
        id_contacto = config.check_secure_val(str(id_contacto)) # HMAC id_contacto validate
        result = config.model.get_contactos(int(id_contacto)) # search  id_contacto
        result.id_contacto = config.make_secure_val(str(result.id_contacto)) # apply HMAC for id_contacto
        return config.render.delete(result, message) # render delete.html with user data

     @staticmethod
    def POST_DELETE(id_contacto, **k):
        form = config.web.input() # get form data
        form['id_contacto'] = config.check_secure_val(str(form['id_contacto'])) # HMAC id_contacto validate
        result = config.model.delete_contactos(form['id_contacto']) # get contactos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_contacto = config.check_secure_val(str(id_contacto))  # HMAC user validate
            id_contacto = config.check_secure_val(str(id_contacto))  # HMAC user validate
            result = config.model.get_contactos(int(id_contacto)) # get id_contacto data
            result.id_contacto = config.make_secure_val(str(result.id_contacto)) # apply HMAC to id_contacto
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/contactos') # render contactos delete.html 
