def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    total_grains = 0
    for i in range(1, 65):
        total_grains += square(i)
    return total_grains
    
