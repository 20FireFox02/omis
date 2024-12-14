from model.auction import *
from model.user import c_user

class AuctionController:
    def get_auction(ID:int):
        def get_bet(auction:Auction):
            c_bet=auction.START_BET
            for bet in auction.members:
                if(c_bet<auction.members[bet]):
                    c_bet=auction.members[bet]
            return c_bet
        
        auction=AuctionService.get_auction(ID)
        return [auction.ID,auction.name,auction.get_date(auction.START_DATE),\
                auction.get_date(auction.END_DATE),get_bet(auction),auction.CREATOR,\
                auction.LOT_NAME,auction.LOT_DESCRIPTION]

    def get_auctions(s_auc:str):
        def get_bet(auction:Auction):
            c_bet=auction.START_BET
            for bet in auction.members:
                if(c_bet<auction.members[bet]):
                    c_bet=auction.members[bet]
            return c_bet
                   
        if(not s_auc):
            return [[auction.ID,auction.name,auction.LOT_NAME,auction.get_date(auction.START_DATE),\
                    auction.get_date(auction.END_DATE),get_bet(auction)]\
                    for auction in AuctionService.get_all()]
        else:
            return [[auction.ID,auction.name,auction.LOT_NAME,auction.get_date(auction.START_DATE),\
                    auction.get_date(auction.END_DATE),get_bet(auction)]\
                    for auction in AuctionService.get_auctions_by_name(s_auc)]

    def new_bet(auc_id:int,buyer_id:int,new_bet:float,c_bet:float):
        if(c_bet<new_bet):
            if(AuctionService.find_bet(auc_id,buyer_id)):
                AuctionService.update_bet(auc_id,buyer_id,new_bet)
            else:
                AuctionService.new_bet(auc_id,buyer_id,new_bet)
                c_user[0].auc.append(auc_id)
            return "Ваша ставка была принята"
        else:
            return "Новая ставка должна превышать текущую"
