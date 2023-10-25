def count_sheep(sheep):
    count = 0
    for s in sheep:
        if s == True:
            count += 1
    return count

# Example:
print(count_sheep([ True,  True,  True,  False,
                    True,  True,  True,  True ,
                    True,  False, True,  False,
                    True,  False, False, True ,]))