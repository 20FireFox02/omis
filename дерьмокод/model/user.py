from model.connect import *
from model.auction import *
class User:
    def __init__(self,ID:int,name:str,desc:str,av:str,psw:str,auc:list):
        self.ID=ID
        self.name=name
        self.description=desc
        self.avatar=av
        self.password=psw
        self.auc=auc
    def upd_desc(self,name:str,desc:str):
        self.name=name
        self.description=desc

    def upd_pass(self,psw:str):
        self.password=psw

    def new_auc(self,auc_id:int):
        self.auc.append(auc_id)
        
class UserService:
    def add_user(self,user:User):
        print(user.ID)
        cursor.execute(f"INSERT INTO user_t \
                        (name,description,avatar,password) VALUES \
                        ('{user.name}','{user.description}','{user.avatar}','{user.password}')")
        cursor.execute(f"SELECT id FROM user_t ORDER BY id DESC LIMIT 1")
        user.ID=cursor.fetchall()[0][0]
        conn.commit()
        return user

    def rem_user(self,name:str):
        cursor.execute(f"DELETE FROM user_t WHERE name='{name}'")
        conn.commit()

    def get_user(self,name:str):
        def st_auc(buyer_id:int):
            cursor.execute(f"SELECT * FROM buyer_bet WHERE buyer_id={buyer_id}")
            return [row[0] for row in cursor.fetchall()]
        cursor.execute(f"SELECT * FROM user_t WHERE name='{name}'")
        row=cursor.fetchall()
        if(row):
            return User(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4],st_auc(row[0][0]))
        else:
            return False
        
    def update_user(user:User):
         cursor.execute(f"UPDATE user_t SET name='{user.name}',\
                        description='{user.description}', ='{user.password}'")
         conn.commit()
c_user=[]
#UserService().add_user(User(1,'aa','','s','pas'))
#UserService().rem_user('aa')
#print(UserService().get_user('aa'))

