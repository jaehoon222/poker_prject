# 홀덤시작 -> 인원 물어봄  -> 이름,돈 물어봄 -> 먼저들어온놈이 딜러버튼(플레이어객체에 저장)
# 카드셔플 -> 나눠줌 -> 베팅시작
# 프리플랍베팅 ->카드한장 공개
# 플랍 베팅 ->같음
# 리버 ->
# 턴 ->누가이겼는지, 진사람들은 돈 수정



########
#pos 대신 그냥 리스트 순서대로 첫번째놈은 빅블, 두번째놈 스몰블, 세번째놈 딜러 순으로 돌아가도됨
#한번 끝날때마다 player_list맨앞놈 맨뒤로 보내는식으로


import Player as pl
from poker import Card
import random
import make_random_Card as mc
import check_winner as cw
from betting import betting

num = int(input("참여 인원 : "))
player_list = []
for i in range(num):
    print("{}번째 플레이어의 정보입력".format(i+1))
    name = input("플레이어의 닉네임 : ")
    money = int(input("시작금액 : "))

    if i<3:
        new_player = pl.Players(name, money, i) #0은 딜러라는 뜻 1:sb, 2 : bb, 3:일반
        player_list.append(new_player)
    else:
        new_player = pl.Players(name, money, 3)
        player_list.append(new_player)
bet = betting()

while (True):
    # 카트섞음
    deck = list(Card)
    pot_size = 0
    board = []
    random.shuffle(deck)
        #카드분배
    for i in player_list:
        i.hand = mc.make_random_hand(deck)
        print(i.hand, i.name) #검증완료
    print("=========================================")

    #프리플랍 베팅
    re_player_list,  pot= bet.freeflop_betting(player_list)# 리턴값 2개로 줄여야됨

    pot_size+=pot
    if len(re_player_list)==1:
        print("위닝핸드 : {} , 승자 : {}, 총액 : {}".format(re_player_list[0].hand, re_player_list[0].name, pot_size))
        for i in player_list:
            print("{}의 남은돈 : {}".format(i.name, i.money) , end = " ")
        print()
        #모든 continue 전에 gamereset 함수 구현 해두고 다시시작
        continue
    else:
        print("프리플랍 pot size : {}".format(pot_size))
        print()

    #플랍
    board += mc.make_random_flop(deck)
    print("플랍 보드: ", board)
    print()

    #플랍 베팅
    re_player_list, pot= bet.flop_betting(re_player_list)
    pot_size+=pot
    pot = 0
    if len(re_player_list)==1:
        print("위닝핸드 : {} , 승자 : {}, 총액 : {}".format(re_player_list[0].hand, re_player_list[0].name, pot_size))
        for i in player_list:
            print("{}의 남은돈 : {}".format(i.name, i.money) , end = " ")
        print()
        continue
    else:
        print("플랍 pot size : {}".format(pot_size))
        print()
    print("=========================================")
    #턴
    board += mc.make_random_turn_rever(deck)
    print("턴 보드: ", board)
    print()

    #턴 베팅
    re_player_list,  pot= bet.flop_betting(re_player_list)
    pot_size+=pot
    pot = 0
    if len(re_player_list)==1:
        print("위닝핸드 : {} , 승자 : {}, 총액 : {}".format(re_player_list[0].hand, re_player_list[0].name, pot_size))
        for i in player_list:
            print("{}의 남은돈 : {}".format(i.name, i.money) , end = " ")
        print()
        continue
    else:
        print("턴 pot size : {}".format(pot_size))
        print()
    print("=========================================")
    #리버
    board += mc.make_random_turn_rever(deck)
    print("리버 보드: ", board)
    print()
    #라스트 베팅
    re_player_list,  pot= bet.flop_betting(re_player_list)
    pot_size+=pot
    pot = 0
    if len(re_player_list)==1:
        print("위닝핸드 : {} , 승자 : {}, 총액 : {}".format(re_player_list[0].hand, re_player_list[0].name, pot_size))
        for i in player_list:
            print("{}의 남은돈 : {}".format(i.name, i.money) , end = " ")
        print()
        continue
    else:
        print("리버 pot size : {}".format(pot_size))
        print()
    print("=========================================")

    #마지막 끝났을때 두명이상 남아있을경우
    winnig_hands, winner_name = cw.whoiswin(board, player_list)
    if len(winnig_hands) == 1:
        print("위닝핸드: {} , 승자 : {}".format( winnig_hands[0],winner_name))
        for i in player_list:
            if i.name==winner_name:
                i.money +=pot_size
    else:
        print("찹핸드들: ", winnig_hands)
        chap_hands = []
        for v in winnig_hands:
            chap_hands.append(v[2])
            print(chap_hands)
        for i in player_list:
            if i.name in winner_name:
                i.money +=pot_size/len(winner_name)

    # pos 이동 아직 구현안함                                ##
    # player_list는 건드린적이없는데...
    print("playerlist 이상함")
    for i in range(len(player_list)):
        print("플레이어 정보 : {}".format(player_list[i].name))
        if player_list[i].pos==0:
            player_list[i].pos=3
            player_list[(i+1)%len(player_list)].pos = 0
            print("{}의 pos는 {}이다".format(player_list[(i+1)%len(player_list)].name, player_list[(i+1)%len(player_list)].pos))
            player_list[(i+2)%len(player_list)].pos = 1
            print("{}의 pos는 {}이다".format(player_list[(i+2)%len(player_list)].name, player_list[(i+2)%len(player_list)].pos))
            player_list[(i+3)%len(player_list)].pos = 2
            print("{}의 pos는 {}이다".format(player_list[(i+1)%len(player_list)].name, player_list[(i+1)%len(player_list)].pos))
            break

    
