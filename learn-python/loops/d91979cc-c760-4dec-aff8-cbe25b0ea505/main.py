def meditate(mana, max_mana, energy, energy_potions):
    while True:
        if mana == max_mana or (energy == 0 and energy_potions == 0):
            break
        if (energy == 0 and energy_potions != 0):
            energy_potions -= 1
            energy += 50
        if (mana + 3) > max_mana:
            mana = max_mana
            energy -= 1
            break
        else:
            energy -= 1
            mana += 3
    return mana, energy, energy_potions
