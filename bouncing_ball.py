"""
A child is playing with a ball on the nth floor of a tall building. The height of this floor above ground level, h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

Examples:
- h = 3, bounce = 0.66, window = 1.5, result is 3

- h = 3, bounce = 1, window = 1.5, result is -1 

(Condition 2) not fulfilled).

def bouncing_ball(h, bounce, window):
    # your code
    return -1
"""

def bouncing_ball(h, rebote, ventana):
    # Definimos la función "bouncing_ball" con tres parámetros: h, rebote y ventana.

    if h > 0 and 0 < rebote < 1 and ventana < h:
        # Comprobamos las tres condiciones iniciales para que el experimento sea válido. Son: 
        # - h debe ser mayor que 0
        # - rebote debe ser mayor que 0 y menor que 1
        # - ventana debe ser menor que h
        
        veces_vista = 1  # Inicializamos el contador en 1, ya que siempre ve el primer rebote
        altura_rebote = h * rebote
        # Inicializamos una variable "veces_vista" para contar las veces que la madre ve la pelota,
        # y una variable "altura_rebote" para rastrear la altura del rebote actual.

        while altura_rebote > ventana:
            # Comenzamos un bucle "while" que se ejecutará mientras la altura del rebote sea mayor que la ventana.
            
            veces_vista += 2  # Añadimos 2 al contador, ya que la madre ve tanto el rebote hacia arriba como el hacia abajo.
            altura_rebote *= rebote
            # Actualizamos el contador y la altura del rebote para el siguiente ciclo.
        
        return veces_vista
        # Una vez que el bucle termina, retornamos la cantidad de veces que la madre ve la pelota.
    else:
        return -1
        # Si alguna de las condiciones iniciales no se cumple, retornamos -1 como resultado.


# print(bouncing_ball(3, 0.66, 1.5))

"""
Pasos bucle:
1 -> 3 * 0.66 = 1.98 -> altura_rebote = 1.98
2 -> 1.98 * 0.66 = 1.3068 -> altura_rebote = 1.3068
3 -> 0.98 * 0.66 = 0.861048 -> altura_rebote = 0.861048
"""