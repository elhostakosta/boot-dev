def get_follower_prediction(follower_count, influencer_type, num_months):
    ratio = 0
    
    if influencer_type == "fitness":
        ratio = 4
    elif influencer_type == "cosmetic":
        ratio = 3
    else:
        ratio = 2

    return follower_count * (ratio ** num_months)
