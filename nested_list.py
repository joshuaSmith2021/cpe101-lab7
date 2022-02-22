# Purpose: Turn list into 2D list with 3 element sublists
def groups_of_3(values: list) -> list:
    result = []
    for i, value in enumerate(values):
        if i % 3 == 0:
            result.append([])

        result[-1].append(value)

    return result


# Purpose: Get list of final values from each sublist
def final_value(values: list) -> list:
    return [x[-1] for x in values if len(x) != 0]


# Purpose: Extend 2D list to 3D
def repeat_value(values: list) -> list:
    return [[x] * x for x in values]
