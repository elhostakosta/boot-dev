def triple_attack(damage_one, damage_two, damage_three):
    total_damage = damage_one + damage_two + damage_three
    return total_damage

# Don't touch below this line

attack_one = 2
attack_two = 4
attack_three = 3
attack_four = -1
attack_five = 10
attack_six = 5

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(triple_attack(attack_one, attack_two, attack_three), "points of damage dealt!")
print("=====================================")

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(triple_attack(attack_four, attack_five, attack_six), "points of damage dealt!")
print("=====================================")
