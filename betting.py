class betting:
    def __init__(self) -> None:
        self.pot = 0
        self.max_size = 0
        self.idx = 0
        self.my_count = 0
    
    #프리플랍 베팅
    def freeflop_betting(self, re_player_list):
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

        self.count = 0

        while(len(re_player_list)!=self.count):
            #if self.idx > len(re_player_list)-1:
            #    self.idx = 0
            #걸려있는 최대금액과 내가 건 금액 다를때
            #bb 있어서 만든 예외임  ,  folp때는 다음차례가 같아질때까지 감
            self.idx %=len(re_player_list)

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
                del re_player_list[self.idx]
                #self.count+=1
            elif a=='r':
                bet = int(input("베팅금액 : "))
                self.max_size= re_player_list[self.idx].betsize + bet #i가 걸었었던 금액 + 레이즈한값
                re_player_list[self.idx].betsize = self.max_size  #i가 건 금액은 현 최고금액임
                re_player_list[self.idx].money -= bet #i 잔액은 건만큼 감소
                self.pot += bet #팟사이즈도 i가 건만큼 증가
                #이제 빅블라인드 의미없음
                self.idx +=1
                for i in re_player_list:
                    if i.pos==2:
                        self.count = 0
                        i.pos = 3
                        break
                self.count = 1

                        
            #플레이어 1명 남았을때
            if len(re_player_list)==1:
                return re_player_list,  self.pot
        return re_player_list,  self.pot



    def flop_betting(self, re_player_list):
        self.count = 0
        for i in range(len(re_player_list)):
            if re_player_list[i].pos==0:
                self.idx = (i+1)%len(re_player_list)

        while(len(re_player_list)!=self.count):
            #if self.idx > len(re_player_list)-1:
            #    self.idx = 0
            #걸려있는 최대금액과 내가 건 금액 다를때
            #bb 있어서 만든 예외임  ,  folp때는 다음차례가 같아질때까지 감
            self.idx %=len(re_player_list)

            if (self.max_size - re_player_list[self.idx].betsize)==0:
                print(print("{}님 turn".format(re_player_list[self.idx].name)))
                a = input("check : c,  raise = r,  fold = f 키를 누르시오")
            else:
                print("{}님 turn".format(re_player_list[self.idx].name))
                a = input("call({}) : c,  raise = r,  fold = f 키를 누르시오".format(self.max_size - re_player_list[self.idx].betsize))



            # if self.count !=len(re_player_list):
            #     print("{}님 turn".format(re_player_list[self.idx].name))
            #     a = input("call({}) : c,  raise = r,  fold = f 키를 누르시오".format(self.max_size - re_player_list[self.idx].betsize))
            # else:
            #     print("{}님 turn".format(re_player_list[self.idx].name))
            #     a = input("check : c,  raise = r,  fold = f 키를 누르시오")


            if a=='c':
                self.pot +=self.max_size - re_player_list[self.idx].betsize #팟사이즈는 건만큼 증가
                re_player_list[self.idx].money -=self.max_size - re_player_list[self.idx].betsize#자기가 건만큼 삭제
                re_player_list[self.idx].betsize = self.max_size # i가 건 총 금액은 인당 건 최대값이랑 같음
                self.idx+=1
                self.count +=1
            elif a=='f':
                del re_player_list[self.idx]
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
            if len(re_player_list)==1:
                return re_player_list, self.pot
                #위너, 끝내라고 출력
        return re_player_list, self.pot


        