"""
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]

def tower_builder(n_floors):
    # build here
"""

def tower_builder(n_floors):
    tower = []  # Initialize an empty list to store the tower levels
    
    for i in range(n_floors):
        spaces = " " * (n_floors - i - 1)  # Calculate the number of spaces before asterisks
        asterisks = "*" * (2 * i + 1)  # Calculate the number of asterisks for the current level
        level = spaces + asterisks + spaces  # Concatenate spaces and asterisks to form the tower level
        tower.append(level)  # Add the level to the tower list
    
    return tower

# Example usage
tower_3_floors = tower_builder(3)
for level in tower_3_floors:
    print(level)
"""
tower_6_floors = tower_builder(6)
for level in tower_6_floors:
    print(level)
"""