from model.wallet import *

class WalletController:

    def get_wallets_names(owner_id:str):
        return [wallet.name for wallet in WalletService.get_wallets(owner_id)]
        
    def get_wallets(owner_id:int,s_wl:str):
        if(not s_wl):
            return [[wallet.TYPE.name,wallet.name,wallet.balance]\
                    for wallet in WalletService.get_wallets(owner_id)]
        else:
            return [[wallet.TYPE.name,wallet.name,wallet.balance]\
                    for wallet in WalletService.get_wallet_by_name(owner_id,s_wl)]

    def get_balance(owner_id:int,s_wl:str,summ):
        print(type(summ))
        if(not s_wl):
            return [False,"Укажите способ оплаты"]
        else:
            tmpl=WalletService.get_wallet_by_name(owner_id,s_wl)[0].balance
            if(tmpl<summ):
                return [False,"Недостаточно средств"]
            else:
                return[True,"Ваша ставка принята"]

    def get_MoneyType():
        return [n.name for n in MoneyType]

    def add(tp:str,owner_id:int,name:str):
        if(not tp or not name):
            return [False,"Пожалуйста, заполните вышестоящие поля"]
        else:
            WalletService.add_wallet(Wallet(tp,owner_id,name,0))
            return [True]
