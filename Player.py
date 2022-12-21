#플레이어 객체 저장해둠

class Players:
    def __init__(self, name, money,pos) -> None:
        self.name = name
        self.money = money
        self.pos = pos #빅블,딜러등등 보여줌
        self.betsize = 0
        self.hand = [] 
        self.state = 1 #현재 상태 보여줌 폴드인지 아닌지  ->   re_player_list 안써도될듯?
        #빅블 -> 2, 스몰블 1 다들 0 .... while(for문  ->레이즈나옴 ->break,새로운 리스트로 다시시작) ->리턴은 팟사이즈,남은 리스트

    def setpos(self, pos):
        self.pos = pos

    def sethand(self, hand):
        self.hand = hand

    def setmoney(self, money):
        self.money = money

    def setbetsize(self, betsize):
        self.betsize = betsize

    def getname(self):
        return self.name
    
    def gethand(self):
        return self.hand

    def getmoney(self):
        return self.money

    def getbetsize(self):
        return self.betsize

    def getpos(self):
        return self.pos

    