def make_change(amount, denominations):
    denominations.sort(reverse=True)

    def find_combinations(remaining_amount, index, current_combination):
        if remaining_amount == 0:
            combinations.append(current_combination.copy())
            return

        for i in range(index, len(denominations)):
            denomination, count = denominations[i]

            if denomination <= remaining_amount and count > 0:
                current_combination.append((denomination, 1))
                denominations[i] = (denomination, count - 1)
                find_combinations(remaining_amount - denomination, i, current_combination)
                denominations[i] = (denomination, count)
                current_combination.pop()

    combinations = []
    find_combinations(amount, 0, [])

    return combinations


def similar_notes(notes):
    result = {}
    for item in notes:
        key, value = item
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return '\n'+'\n'.join(list(f"{x} x {y}" for x,y in result.items()))


def find_lowest(amount, denominations):
    make_change_notes = make_change(amount,denominations)
    result = [(x,len(x)) for x in make_change_notes]
    sorted_list = sorted(result, key=lambda x: x[1])
    if len(sorted_list) >= 1:
        new_sort = similar_notes(sorted_list[0][0])
        return new_sort,sorted_list[0][0]
    else:
        return None,None

