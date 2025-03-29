def merge(dict1, dict2):
    dict = {}
    for key in dict1:
        dict[key] = dict1[key]
    for key in dict2:
        dict[key] = dict2[key]
    return dict


def total_score(score_dict):
    total = 0
    for key in score_dict:
        total += score_dict[key]
    return total
