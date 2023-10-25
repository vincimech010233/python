def flick_switch(lst):
    result = []
    switch = True  # Inicializamos un interruptor en True
    for item in lst:
        if item == "flick":
            switch = not switch  # Cambiamos el estado del interruptor (de True a False o viceversa)
        result.append(switch)
    return result

# Example:
print(flick_switch(["edabit", "flick", "eda", "bit"])) # [True, False, False, False]