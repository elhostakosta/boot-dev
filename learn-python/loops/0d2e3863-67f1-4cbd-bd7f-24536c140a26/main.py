def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = 0
    for i in range (0, num_attacks):
        if (i == num_attacks - 1):
            total_damage += 4 * base_damage
        else:
            total_damage += base_damage * 2
    return total_damage
