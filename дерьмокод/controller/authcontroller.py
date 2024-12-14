from model.user import *

class AuthController:
    def handle_login(name:str,passw:str):
        if(not name or not passw):
            return [False,'Поля логина и пароля не могут быть пустыми']
        tmpl=UserService().get_user(name)
        if(not tmpl or not tmpl.password==passw):
            return [False,'Неправильный логин или пароль']
        c_user.append(tmpl)
        return [True]
        
    def handle_register(name:str,passw:str,av:str):
        if(not name or not passw):
            return [False,'Поля логина и пароля не могут быть пустыми']
        if(UserService().get_user(name)):
            return [False,'Данный пользователь уже зарегистрирован в системе']
        tmpl=UserService().add_user(User(0,name,'',av,passw))
        c_user.append(tmpl)
        return [True]
