"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40  # in minutes, the expected bake time for the lasagna
PREPARATION_TIME = 20  # in minutes, the expected preparation time for the lasagna



def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time



def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time (minutes)

    :param number_of_layers: int - number of layers you want to add to lasagna
    :return: int - how many minutes you would spend making them

    Function that takes the number of layers you want to add to the lasagna as 
    an argument and returns how many times you would spend making them.
    """
    return 2*number_of_layers



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total cooking time (minutes)

    :param number_of_layers: int - number of layers added to lasagna
    :param elapsed_bake_time: int - baking time already elapsed
    :return: int - total cooking time

    Function that takes the number of layers added to lasagna and 
    elapsed bake time and returns the total cooking time
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time



