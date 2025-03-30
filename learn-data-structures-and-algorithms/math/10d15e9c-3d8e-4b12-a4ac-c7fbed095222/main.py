def num_possible_orders(num_posts):
    possible_orders = 1

    for i in range(num_posts, 0, -1):
        possible_orders *= i

    return possible_orders
