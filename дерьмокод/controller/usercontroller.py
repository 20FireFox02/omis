from model.user import *
from controller.auctioncontroller import AuctionController

class UserController:
    def update_user_desc(name:str,desc:str):
        if(not name):
            return "Введите имя"
        if(not c_user[0]==UserService.get_user(name)):
            return "Данное имя уже занято"
        else:
            c_user[0].upd_desc(name,desc)
            UserService.update_user(c_user[0])
            return "Данные пользователя успешно изменены"

    def get_story(nm:str):
        return [AuctionController.get_auction(a) for a in c_user[0].auc]

    def update_user_pass(op:str,np:str):
        if(not op or not np):
            return "Введите пароли"
        if(not c_user[0].password==op):
            return "Пароль неверный"
        else:
            c_user[0].password=np
            UserService.update_user(c_user[0])
            return "Данные пользователя успешно изменены"
