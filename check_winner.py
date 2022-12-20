from pokereval.hand_evaluator import HandEvaluator

def whoiswin(board, player_list):
    scores = []

    for i in player_list:
        score = HandEvaluator.evaluate_hand(i.hand, board)
        scores.append([score, i.hand, i.name])
        scores.sort(reverse=True, key=lambda x: x[0])

    if scores[0][0] != scores[1][0]:
        winning_card = scores[0][1]
        return [winning_card], scores[0][2]
    else:
        chap_cards = [scores[0][1]]
        chap_names = [scores[0][2]]
        for i in range(len(scores)-1):

            if scores[i][0] == scores[i+1][0]:
                chap_cards.append(scores[i+1][1])
                chap_names.append(scores[i+1][2])
            else:
                break
        return chap_cards, chap_names