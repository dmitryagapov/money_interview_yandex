import copy


def solution(amount, money_limits, result=None, current_note=None):

    moneyTypes = list(money_limits.keys())
    moneyTypes.sort(reverse=True)
    if not result:
        result = {}
    
    if current_note:
        if money_limits[current_note] > 0:
            amount -= current_note
            money_limits[current_note] -= 1
            if current_note not in result:
                result[current_note] = 1
            else:
                result[current_note] += 1
        else:
            return

    if amount < 0:
        return
    if amount == 0:
        yield result

    tmp_amount = amount
    max_note_i = 0 if not current_note else moneyTypes.index(current_note)
    
    for note in moneyTypes[max_note_i:]:
        yield from solution(
            tmp_amount, 
            copy.deepcopy(money_limits),
            copy.deepcopy(result),
            note
        )


if __name__ == '__main__':
    amount = 12120
    money_limits = {
        5000: 10,
        1000: 10,
        500: 10,
        100: 10,
        50: 10,
        30: 10
    }

    res = solution(amount, money_limits)
    print(next(res))
