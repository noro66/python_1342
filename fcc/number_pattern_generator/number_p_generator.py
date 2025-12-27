def number_pattern(n: int):
    result = ""
    if not isinstance(n, int):
        return "Argument must be an integer value.."
    if n < 1:
        return "Argument must be an integer greater than 0.."
    for nm in range(1, n + 1):
        result += f"{str(nm)}"
        if nm < n:
            result += " "
    return result


print(number_pattern(4))
