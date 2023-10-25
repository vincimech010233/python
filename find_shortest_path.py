from collections import deque
from typing import List

# Define a class to represent nodes in the grid
class Node:
    def __init__(self, x, y, passable):
        self.position = Position(x, y)  # Node's position (x, y)
        self.passable = passable  # Whether the node is passable or not

# Define a class to represent the position of a node
class Position:
    def __init__(self, x, y):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate

# Define a function to find the shortest path in the grid
def find_shortest_path(grid: List[List[Node]], start_node: Node, end_node: Node) -> List[Node]:
    if not grid or not grid[0]:  # Check if the grid is empty
        return []

    rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns in the grid
    visited = set()  # Initialize a set to keep track of visited nodes
    queue = deque([(start_node, [start_node])])  # Initialize a queue with the start node and its path

    while queue:
        current_node, path = queue.popleft()  # Get the next node and its path from the queue

        if current_node == end_node:  # If the current node is the destination node, return the path
            return path

        visited.add((current_node.position.x, current_node.position.y))  # Mark the current node as visited

        # Define possible movement directions: up, down, left, and right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            x, y = current_node.position.x + dx, current_node.position.y + dy  # Calculate the new position

            # Check if the new position is within the grid boundaries
            if 0 <= x < rows and 0 <= y < cols:
                neighbor = grid[x][y]  # Get the neighboring node

                # Check if the neighbor is passable and not visited
                if neighbor.passable and (neighbor.position.x, neighbor.position.y) not in visited:
                    queue.append((neighbor, path + [neighbor]))  # Add the neighbor and its path to the queue
                    visited.add((neighbor.position.x, neighbor.position.y))  # Mark the neighbor as visited

    return []

# Create an example grid with nodes
grid = [
    [Node(0, 0, True), Node(0, 1, True), Node(0, 2, False)],
    [Node(1, 0, True), Node(1, 1, False), Node(1, 2, True)],
    [Node(2, 0, True), Node(2, 1, True), Node(2, 2, True)]
]

# Define the start and end nodes
start_node = grid[0][0]
end_node = grid[2][2]

# Find the shortest path from the start to the end node
shortest_path = find_shortest_path(grid, start_node, end_node)

# Print the shortest path if it exists
if shortest_path:
    for node in shortest_path:
        print(f"({node.position.x}, {node.position.y})", end=" -> ")  # Print the coordinates of nodes in the path
    print("End")  # Indicate the end of the path
else:
    print("No valid path found.")  # Print a message if no valid path is found
