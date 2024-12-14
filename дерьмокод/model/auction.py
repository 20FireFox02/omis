from model.connect import *

class Auction:
    class Date:
        def __init__(self,d:str,m:str,a:str):
            self.age=int(a)
            self.month=int(m)
            self.day=int(d)
            
    def __init__(self,ID:int,name:str,sd:str,ed:str,sb:float,cr:str,lname:str,dn:str,members:dict):
        self.ID=ID
        self.name=name
        self.START_DATE=self.Date(sd[:2],sd[3:5],sd[6:])
        self.END_DATE=self.Date(ed[:2],ed[3:5],ed[6:])
        #self.START_DATE=sd[4:]+'-'+sd[2:3]+'-'sd[:1]
        #self.END_DATE=ed[4:]+'-'+ed[2:3]+'-'ed[:1]   
        self.START_BET=sb
        self.CREATOR=cr
        self.LOT_NAME=lname
        self.LOT_DESCRIPTION=dn
        self.members=members

    def get_date(self,date:Date):
        return f"{date.day}.{date.month}.{date.age}"

class AuctionService:
    def new_bet(auc_id:int,buyer_id:int,new_bet:float):
        cursor.execute(f"INSERT INTO buyer_bet (auc_id,buyer_id,bet) VALUES \
                        ({auc_id},{buyer_id},{new_bet})")
        conn.commit()

    def update_bet(auc_id:int,buyer_id:int,new_bet:float):
        cursor.execute(f"UPDATE buyer_bet SET bet={new_bet} WHERE \
                        auc_id={auc_id} and buyer_id={buyer_id}")
        conn.commit()

    def find_bet(auc_id:int,buyer_id:int):
        cursor.execute(f"SELECT * FROM buyer_bet WHERE auc_id={auc_id} and buyer_id={buyer_id}")
        return cursor.fetchall()
        
    def add_auction(self,auction:Auction):
        cursor.execute(f"INSERT INTO auction \
                        (id,name,st_d,en_d,st_b,creator,lotname,description) VALUES \
                        ({auction.ID},'{auction.name}','{auction.get_date(auction.START_DATE)}',\
                        '{auction.get_date(auction.END_DATE)}',{auction.START_BET},\
                        '{auction.CREATOR}','{auction.LOT_NAME}','{auction.LOT_DESCRIPTION}')")
        conn.commit()

    def get_auction(ID:int):
        def get_member(ID:int):
            cursor.execute(f"SELECT * FROM buyer_bet WHERE auc_id={ID}")
            return {row[1]:float(row[2]) for row in cursor.fetchall()}
        def edit_date_format(date:str):
            return date[8:]+'.'+date[5:7]+'.'+date[:4]
        cursor.execute(f"SELECT * FROM auction WHERE id={ID} LIMIT 1")
        row=cursor.fetchall()
        return Auction(row[0][0],row[0][1],edit_date_format(f"{row[0][2]}"),\
                        edit_date_format(f"{row[0][3]}"),\
                        row[0][4],row[0][5],row[0][6],row[0][7],get_member(row[0][0]))

    def get_all():
        def get_member(ID:int):
            cursor.execute(f"SELECT * FROM buyer_bet WHERE auc_id={ID}")
            return {row[1]:float(row[2]) for row in cursor.fetchall()}
        def edit_date_format(date:str):
            return date[8:]+'.'+date[5:7]+'.'+date[:4]
        cursor.execute(f"SELECT * FROM auction")
        return [Auction(row[0],row[1],edit_date_format(f"{row[2]}"),\
                        edit_date_format(f"{row[3]}"),\
                        row[4],row[5],row[6],row[7],get_member(row[0])) for row in cursor.fetchall()]
    
    def get_auctions_by_name(name:str):
        def get_member(ID:int):
            cursor.execute(f"SELECT * FROM buyer_bet WHERE auc_id={ID}")
            return {row[1]:float(row[2]) for row in cursor.fetchall()}
        def edit_date_format(date:str):
            return date[8:]+'.'+date[5:7]+'.'+date[:4]
        cursor.execute(f"SELECT * FROM auction WHERE name='{name}'")
        return [Auction(row[0],row[1],edit_date_format(f"{row[2]}"),\
                        edit_date_format(f"{row[3]}"),\
                        row[4],row[5],row[6],row[7],get_member(row[0])) for row in cursor.fetchall()]

    def get_auctions_by_creator(creator_id:int):
        def get_member(ID:int):
            cursor.execute(f"SELECT * FROM buyer_bet WHERE auc_id={ID}")
            return {row[1]:float(row[2]) for row in cursor.fetchall()}
        def edit_date_format(date:str):
            return date[8:]+'.'+date[5:7]+'.'+date[:4]
        cursor.execute(f"SELECT * FROM auction WHERE creator=(SELECT name FROM user_t WHERE id={creator_id})")
        return [Auction(row[0],row[1],edit_date_format(f"{row[2]}"),\
                        edit_date_format(f"{row[3]}"),\
                        row[4],row[5],row[6],row[7],get_member(row[0])) for row in cursor.fetchall()]

#AuctionService().add_auction(Auction(3,'cooooooool','18.05.2021','20.09.2021',17.13,'ss','lll','descrip',{}))
#print(AuctionService().get_auctions(1))
#sd[:4],sd[5:7],sd[8:10]
