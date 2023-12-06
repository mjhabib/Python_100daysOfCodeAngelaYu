import math  # to round up the result


def paint_calc(wall_height, wall_width, coverage):
    result = wall_height * wall_width / coverage
    print(f'You need "{math.ceil(result)}" can(s) of paint. ')


paint_calc(float(input("How tall is your wall? ")), float(input("How wide is your wall? ")), 5)
