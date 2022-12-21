#살아있는 사람수 체크
def live_player_num(player_list):
    num = 0
    for i in player_list:
        if i.state ==1:
            num+=1
    return num


class betting:
    def __init__(self) -> None:
        self.pot = 0
        self.max_size = 0
        self.idx = 0  #리스트안에서 돌고있는 현재위치
        self.my_count = 0  #시작사람 빅블 다음사람 인덱스 구할라고 만든 변수
    
    #프리플랍 베팅
    def betting_(self, re_player_list, cnt):
        self.count = 0
        self.pot = 0
        self.idx = 0  
        self.my_count = 0 


        # cnt는 프리플랍인지 아닌지 가져옴, 프리플랍일때는 빅블다음시작, 시작돈 다름
        #프리플랍 아닌 베팅은 그냥 딜러다음이 시작인것만 알려주면됨
        if cnt ==0:
            for i in re_player_list:
                if i.pos==1:
                    i.betsize = 100
                    self.pot +=100
                    i.money -=100
                    self.max_size = 100
                elif i.pos==2:
                    i.betsize=200
                    self.pot +=200
                    self.max_size=200
                    i.money-=200
                    self.idx = (self.my_count+1)%len(re_player_list)
                self.my_count +=1
        else:
            for i in range(len(re_player_list)):
                if re_player_list[i].pos==0:
                    self.idx = (i+1)%len(re_player_list)


        
        #마지막놈 체크될때까지 계속돌음  , self.count : 한명이 레이즈 후 
        while(live_player_num(re_player_list)!=self.count):
            self.idx %=len(re_player_list)

            if re_player_list[self.idx].state == 1:
            #마지막사람은 체크 들어오면안됨
                if (self.max_size - re_player_list[self.idx].betsize)==0:
                    print(print("{}님 turn".format(re_player_list[self.idx].name)))
                    a = input("check : c,  raise = r,  fold = f 키를 누르시오")
                else:
                    print("{}님 turn".format(re_player_list[self.idx].name))
                    a = input("call({}) : c,  raise = r,  fold = f 키를 누르시오".format(self.max_size - re_player_list[self.idx].betsize))

                # if self.count !=len(re_player_list)-1:
                #     print("{}님 turn".format(re_player_list[self.idx].name))
                #     a = input("call({}) : c,  raise = r,  fold = f 키를 누르시오".format(self.max_size - re_player_list[self.idx].betsize))
                # else:
                #     print(print("{}님 turn".format(re_player_list[self.idx].name)))
                #     a = input("check : c,  raise = r,  fold = f 키를 누르시오")


                if a=='c':
                    self.pot +=self.max_size - re_player_list[self.idx].betsize #팟사이즈는 건만큼 증가
                    re_player_list[self.idx].money -=self.max_size - re_player_list[self.idx].betsize#자기가 건만큼 삭제
                    re_player_list[self.idx].betsize = self.max_size # i가 건 총 금액은 인당 건 최대값이랑 같음
                    self.idx+=1
                    self.count +=1
                elif a=='f':
                    re_player_list[self.idx].state = 0
                    self.idx+=1
                    #self.count+=1
                elif a=='r':
                    bet = int(input("베팅금액 : "))
                    self.max_size= re_player_list[self.idx].betsize + bet #i가 걸었었던 금액 + 레이즈한값
                    re_player_list[self.idx].betsize = self.max_size  #i가 건 금액은 현 최고금액임
                    re_player_list[self.idx].money -= bet #i 잔액은 건만큼 감소
                    self.pot += bet #팟사이즈도 i가 건만큼 증가
                    #이제 빅블라인드 의미없음
                    self.idx +=1 
                    self.count = 1

                            
                #플레이어 1명 남았을때
                if live_player_num(re_player_list)==1:
                    return re_player_list,  self.pot
        
            else:
                self.idx+=1

        return re_player_list,  self.pot



        