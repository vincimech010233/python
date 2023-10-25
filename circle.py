def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("radius must be a number")
    if r == 0:
        raise ValueError("radius cannot be zero")
    if r < 0:
            raise ValueError("radius cannot be negative")
    return float(r ** 2 * 3.141592653589793238462643383279502884197169399375105820974944592307816406286)

print(circle_area(2))