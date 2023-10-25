import re

def kebabize(string):
    # Use regular expression to split the camel case string into words
    words = re.findall(r'[A-Za-z][a-z]*', string)
    
    # Join the words with "-" and convert to lowercase
    kebab = '-'.join(word.lower() for word in words)
    
    return kebab

print(kebabize("The-Example"))
print(kebabize("TheExample"))
print(kebabize("the-example"))
print(kebabize("the_Example"))
print(kebabize("SOS"))


"""
La diferencia es que r'[A-Z]?[a-z]+' captura palabras en CamelCase, mientras que r'[A-Za-z][a-z]*' captura palabras en CamelCase o snake_case, considerando letras iniciales mayúsculas o minúsculas.
"""