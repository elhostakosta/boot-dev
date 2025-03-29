def check_ingredient_match(recipe, ingredients):
    missing = []
    count = 0

    for i in range(0, len(recipe)):
        if recipe[i] == ingredients[i]:
            count += 1
        else:
            missing.append(recipe[i])
    percentage = float(count / len(recipe)) * 100
    return percentage, missing
