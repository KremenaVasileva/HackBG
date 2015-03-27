def nan_expand(times):
    if times == 0:
        return ""
    return "Not a " * times + "NaN"

print(nan_expand(5))
