full_dot = '●'
empty_dot = '○'


def isnot_int(var) -> bool:
    return not isinstance(var, int)


def create_character(ch_name, strgth, intlgnt, chrism) -> str:
    if not isinstance(ch_name, str):
        return "The character name should be a string"
    if len(ch_name) == 0:
        return "The character should have a name"
    if len(ch_name) > 10:
        return "The character name is too long"
    if ch_name.__contains__(" "):  # or you can use " " in ch_name
        return "The character name should not contain spaces"
    if isnot_int(strgth) or isnot_int(intlgnt) or isnot_int(chrism):
        return "All stats should be integers"
    if strgth < 1 or intlgnt < 1 or chrism < 1:
        return "All stats should be no less than 1."
    if strgth > 4 or intlgnt > 4 or chrism > 4:
        return "All stats should be no more than 4."
    if strgth + intlgnt + chrism != 7:
        return "The character should start with 7 points"
    return f"""{ch_name}\nSTR {full_dot * strgth}{empty_dot * (10 - strgth)}
INT {full_dot * intlgnt}{empty_dot * (10 - intlgnt)}
CHA {full_dot * chrism}{empty_dot * (10 - chrism)}"""


print(create_character("ahm", 2, 4, 1))
