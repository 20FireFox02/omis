import psycopg2 as pg
import enum

class MoneyType(enum.Enum):
    QIWI='QIWI'
    YANDEX_MONEY='YANDEX_MONEY'
    WEBMONEY='WEBMONEY'
    PAYPAL='PAYPAL'
    BANK='BANK'

conn = pg.connect(
    host='localhost',
    database='omis',
    port=5432,
    user='postgres',
    password='pass98rSQL'
    )
cursor=conn.cursor()

        
class Buyer:
    def __init__(self,ID:int,name,psw,desc,av):
        print("init")
        self.ID=ID
        self.name=name
        self.psw=psw
        self.desc=desc
        self.av=av

class Seller:
    def __init__(self,uid,name,passw,desc,av):
        self.uid=uid
        self.name=name
        self.passw=passw
        self.desc=desc
        self.av=aav
    def get_password(self):
        return self.password

class Auction:
    def __init__(self,ID:int,name:str,START_DATE,END_DATE,START_BET:float,CREATOR:str):
        cursor.execute(f"SELECT * FROM buyer WHERE name='{name}' and password='{psw}'")
        self.ID=ID
        self.name=name
        self.START_DATE=START_DATE
        self.END_DATE=END_DATE
        self.START_BET=START_BET
        self.CREATOR=CREATOR

class Wallet:
    def __init__(TYPE,OWNER_ID,name,balance):
        self.TYPE=TYPE
        self.OWNER_ID=OWNER_ID
        self.balance=balance
        
class WalletService:
    def add_wallet(wallet:Wallet):
        cursor.execute(f"INSERT INTO wallet \
                        (type,owner_id,name,balance) VALUES \
                        ({wallet.TYPE},{wallet.OWNER_ID},'{wallet.name}',{wallet.balance})")
        conn.commit()

    def rem_wallet(owner_id:int,name:str):
        cursor.execute(f"DELETE FROM wallet WHERE id={owner_id} and name='{name}'")
        conn.commit()

    def get_wallets(self,owner_id:int):
        cursor.execute(f"SELECT * FROM buyer WHERE id='{owner_id}'")
        return [Wallet(row[0],row[1],row[2],row[3],row[4]) for row in cursor.fetchall()]

class AuctionService:
    def add_auction(auction:Auction):
        cursor.execute(f"INSERT INTO auction WHERE id='{owner_id}'")
        conn.commit()
        
    def rem_auction(owner_id:int,name:str):
        cursor.execute(f"DELETE wallet WHERE id='{owner_id}'")
        conn.commit()

    def get_auction(self,creator_id:int):
        cursor.execute(f"SELECT * FROM auction WHERE id='{creator_id}'")
        return [Wallet(row[0],row[1],row[2],row[3],row[4]) for row in cursor.fetchall()]

class UserRepo:
    def find_buyer(self,name,psw):
        cursor.execute(f"SELECT * FROM buyer WHERE name='{name}' and password='{psw}'")
        row = cursor.fetchall()
        if(row):
            return Buyer(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4])
    def find_seller(self,name,psw):
        cursor.execute(f"SELECT * FROM seller WHERE name='{name}' and password='{psw}'")
        row = cursor.fetchall()
        if(row):
            return Buyer(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4])
        else:
            return false
        
WalletService().add_wallet(Wallet(QIWI,1,'popa',36.02))
