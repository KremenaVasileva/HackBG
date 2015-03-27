def iterations_of_nan_expand(expanded):
    if expanded == "Not a " * expanded.count("Not a ") + "NaN":
        return expanded.count("Not a")
    elif expanded == "":
        return 0
    return False

print (iterations_of_nan_expand("Not a NaN"))
