# 홀덤시작 -> 인원 물어봄  -> 이름,돈 물어봄 -> 먼저들어온놈이 딜러버튼(플레이어객체에 저장)
# 카드셔플 -> 나눠줌 -> 베팅시작
# 프리플랍베팅 ->카드한장 공개
# 플랍 베팅 ->같음
# 리버 ->
# 턴 ->누가이겼는지, 진사람들은 돈 수정


#pos 대신 그냥 리스트 순서대로 첫번째놈은 빅블, 두번째놈 스몰블, 세번째놈 딜러 순으로 돌아가도됨
#한번 끝날때마다 player_list맨앞놈 맨뒤로 보내는식으로


import Player as pl
from poker import Card
import random
import make_random_Card as mc
import check_winner as cw
from betting import betting


#살아있는 사람수 체크
def live_player_num(player_list):
    num = 0
    for i in player_list:
        if i.state ==1:
            num+=1
    return num

def game_reset(player_list):
    for i in player_list:
        i.state = 1
        i.betsize = 0
        print("{}의 잔액 : {}".format(i.name, i.money), end = '  ')
    print()

    for i in range(len(player_list)):
        if player_list[i].pos==0:
            player_list[i].pos=3
            player_list[(i+1)%len(player_list)].pos = 0
            player_list[(i+2)%len(player_list)].pos = 1
            player_list[(i+3)%len(player_list)].pos = 2
            
            return player_list

# 초기 시작단계

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


#게임진행은 여기서 계속 진행됨
while (True):
    bet = betting()
    # 카트섞음
    deck = list(Card)
    pot_size = 0
    board = []
    random.shuffle(deck)
    #카드분배
    for i in player_list:
        i.hand = mc.make_random_hand(deck)
        print(i.hand, i.name) #검증완료
    print("게임 시작=========================================")


    #프리플랍 베팅  ,  re_player_list ->player_list로 한번에 (state값 써서)

    player_list,  pot= bet.betting_(player_list,0)

    pot_size+=pot
    if live_player_num(player_list)==1:
        for i in player_list:
            if i.state==1:
                i.money +=pot_size
                print("승자는 : {}".format(i.name))
        #모든 continue 전에 gamereset 함수 구현 해두고 다시시작
        player_list = game_reset(player_list)
        continue
    else:
        print("프리플랍 pot size : {}".format(pot_size))
        print()

    #플랍
    board += mc.make_random_flop(deck)
    print("플랍 보드: ", board)
    print()

    #플랍 베팅
    player_list, pot= bet.betting_(player_list,1)
    pot_size+=pot
    pot = 0
    if live_player_num(player_list)==1:
        for i in player_list:
            if i.state==1:
                i.money +=pot_size
                print("승자는 : {}".format(i.name))
        player_list = game_reset(player_list)
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
    player_list,  pot= bet.betting_(player_list,1)
    pot_size+=pot
    pot = 0
    if live_player_num(player_list)==1:
        for i in player_list:
            if i.state==1:
                i.money +=pot_size
                print("승자는 : {}".format(i.name))
        player_list = game_reset(player_list)
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
    player_list,  pot= bet.betting_(player_list,1)
    pot_size+=pot
    pot = 0
    if live_player_num(player_list)==1:
        for i in player_list:
            if i.state==1:
                i.money +=pot_size
                print("승자는 : {}".format(i.name))
        player_list = game_reset(player_list)
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
    
    player_list = game_reset(player_list)