"""
Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

Can you help her?

def greet(name):
    return "Hello, {name}!".format(name=name)
    if name == "Johnny":
        return "Hello, my love!"
"""

def greet(name):
    special_greetings = {
        "Johnny": "Hello, my love!",
        "Alice": "Hi, Alice!",
        "Bob": "Hey, Bob!"
        # Agrega más nombres y saludos especiales aquí
    }

    if name in special_greetings:
        return special_greetings[name]
    return f"Hello, {name}!"


print(greet("Alice"))
print(greet("Bob"))
print(greet("Johnny"))