import numpy as np

def calculate(list):
    #  checks if the length of the input is not equal to 9, and if so, raises a ValueError
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # converts each element to an integer and then creates a 3x3 NumPy array
    values = [int(x) for x in list]
    elements = np.array(values).reshape(3, 3)
    print(elements)
    print()

    # performing calculations and storing results in a list using tolist()
    # axis=0 is per column and vice versa
    mean = [elements.mean(axis=0).tolist(), elements.mean(axis=1).tolist(), elements.mean()]
    summ = [elements.sum(axis=0).tolist(), elements.sum(axis=1).tolist(), elements.sum()]
    standard_deviation = [elements.std(axis=0).tolist(), elements.std(axis=1).tolist(), elements.std()]
    variance = [elements.var(axis=0).tolist(), elements.var(axis=1).tolist(), elements.var()]
    maxx = [elements.max(axis=0).tolist(), elements.max(axis=1).tolist(), elements.max()]
    minn = [elements.min(axis=0).tolist(), elements.min(axis=1).tolist(), elements.min()]

    # storing results in a dictionary
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': maxx,
        'min': minn,
        'sum': summ
        }
    # looping through the key value pairs to print
    for key, value in calculations.items():
        print(key, ':', value)

    



    return calculations