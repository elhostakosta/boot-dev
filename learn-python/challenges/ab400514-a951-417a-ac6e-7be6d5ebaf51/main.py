def area_sum(rectangles):
    area_sum = 0
    for rectangle in rectangles:
        area = rectangle["height"] * rectangle["width"]
        area_sum += area
    return area_sum
