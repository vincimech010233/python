# Define las funciones que retornan el resultado de la operacion
spoken = lambda greeting: greeting.capitalize() + "." # capitalize() convierte la primera letra en mayuscula + "."
shouted = lambda greeting: greeting.upper() + "!" # upper() convierte todas las letras en mayuscula + "!"
whispered = lambda greeting: greeting.lower() + "." # lower() convierte todas las letras en minuscula + "."

# Define la funcion que recibe un estilo y un mensaje
greet = lambda style, msg: style(msg) 

# Example:
message = "hello WORLD"
emotion = spoken
result = greet(emotion, message)
print(result)  # Output: "Hello world."
