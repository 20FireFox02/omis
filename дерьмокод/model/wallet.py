import enum
from model.connect import *

class MoneyType(enum.Enum):
    QIWI='QIWI'
    YANDEX_MONEY='YANDEX_MONEY'
    WEBMONEY='WEBMONEY'
    PAYPAL='PAYPAL'
    BANK='BANK'

class Wallet:
    def __init__(self,TYPE:str,OWNER_ID:int,name:str,balance:float):
        for t in MoneyType:
            if(t.name==TYPE):
                self.TYPE=t
                break
        self.OWNER_ID=OWNER_ID
        self.name=name
        self.balance=balance

class WalletService:
    def add_wallet(wallet:Wallet):
        cursor.execute(f"INSERT INTO wallet \
                        (type,owner_id,name,balance) VALUES \
                        ('{wallet.TYPE.name}',{wallet.OWNER_ID},'{wallet.name}',{wallet.balance})")
        conn.commit()

    def rem_wallet(owner_id:int,name:str):
        cursor.execute(f"DELETE FROM wallet WHERE owner_id={owner_id} and name='{name}'")
        conn.commit()
        
    def get_wallet_by_name(owner_id:int,name:str):
        cursor.execute(f"SELECT * FROM wallet WHERE owner_id={owner_id} and name='{name}'")
        return [Wallet(row[0],row[1],row[2],row[3]) for row in cursor.fetchall()]
    
    def get_wallets(owner_id:int):
        cursor.execute(f"SELECT * FROM wallet WHERE owner_id={owner_id}")
        return [Wallet(row[0],row[1],row[2],row[3]) for row in cursor.fetchall()]

    
#WalletService().add_wallet(Wallet(MoneyType.QIWI,1,'gofa',66.02))
#WalletService().rem_wallet(1,'gofa')
#print(WalletService().get_wallets(1))
