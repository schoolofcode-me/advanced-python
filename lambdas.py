def alter(values, check):
    # return list(filter(check, values))
    return [val for val in values if check(val)]


def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])


def skip_letter(value, letter):
    return alter(value, lambda x: x != letter)

print(skip_letter("hello", "e"))