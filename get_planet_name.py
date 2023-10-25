def get_planet_name(id):
    planet_names = ["", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if 1 <= id <= 8:
        return planet_names[id]
    else:
        return ""
    
# Example:
print(get_planet_name(2)) # Venus