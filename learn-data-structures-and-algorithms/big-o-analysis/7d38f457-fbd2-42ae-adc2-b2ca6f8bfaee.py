def get_avg_brand_followers(all_handles, brand_name):
    handles_count = 0
    
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                handles_count += 1
    return handles_count / len(all_handles)
