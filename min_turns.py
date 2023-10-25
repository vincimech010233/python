def min_turns(current, target):
    turns = 0
    for c, t in zip(current, target):
        diff = abs(int(c) - int(t))
        turns += min(diff, 10 - diff)  # Mínimo de giros hacia adelante y hacia atrás
    return turns


# Example:
print(min_turns("4089", "5672"))  # 9