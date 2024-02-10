"""
Evaluation functions
"""
import math


def dummy_evaluation_func(state):
    return 0.0


def distance_evaluation_func(state):
    player = state.get_current_player()
    info = state.get_info()
    score = 0.0
    for p, info_p in info.items():
        if p == player:
            score -= info_p["max_distance"]
        else:
            score += info_p["max_distance"]
    return score


def detailed_evaluation_func(state):
    # TODO
    player = state.get_current_player()
    info = state.get_info()
    score0 = 0.0
    score1 = 0.0
    
    for p, info_p in info.items():
        if p == player:
            score0 = score0 + info_p["live_four"]*10000 + info_p["four"]*10000 + \
                info_p["live_three"]*10000 + info_p["three"] * \
                50 + info_p["live_two"]*10 - info_p["max_distance"]
            if info_p["live_three"] >= 2:
                score0 += 10000
        else:
            score1 = score1 + info_p["live_four"]*10000 + info_p["four"]*700 + \
                info_p["live_three"]*700 + info_p["three"] * 40 + \
                info_p["live_two"]*10 - info_p["max_distance"]
            if info_p["live_three"] >= 2:
                score1 += 10000
    score = score0 - score1
    #return math.tanh(score/10000)
    return min(1, max(-1, score/100000000))


def get_evaluation_func(func_name):
    if func_name == "dummy_evaluation_func":
        return dummy_evaluation_func
    elif func_name == "distance_evaluation_func":
        return distance_evaluation_func
    elif func_name == "detailed_evaluation_func":
        return detailed_evaluation_func
    else:
        raise KeyError(func_name)
