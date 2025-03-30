def get_estimated_spread(audiences_followers):

    num_followers = len(audiences_followers)
    
    if num_followers == 0:
        return 0
        
    total_followers = 0

    for audience_follower in audiences_followers:
        total_followers += audience_follower

    average_audience_followers = total_followers  / num_followers
    estimated_spread = average_audience_followers * (num_followers ** 1.2)

    return estimated_spread
