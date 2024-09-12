from collections import deque

# Define a function to check if a state has already been visited
def is_visited(visited, state):
    return state in visited

# Define a function to add a state to the queue if it hasn't been visited
def add_state(queue, visited, state, path):
    if not is_visited(visited, state):
        queue.append((state, path))
        visited.add(state)

# BFS function to solve the Water Jug problem
def water_jug_solver(capacity_a, capacity_b, target):
    # Queue to store the states and the path to reach them
    queue = deque()
    
    # Set to store visited states to avoid cycles
    visited = set()
    
    # Initialize the queue with the starting state (0, 0)
    initial_state = (0, 0)
    queue.append((initial_state, [initial_state]))
    visited.add(initial_state)
    
    # Perform BFS
    while queue:
        current_state, path = queue.popleft()
        jug_a, jug_b = current_state
        
        # If we have reached the target amount in either jug, return the path
        if jug_a == target or jug_b == target:
            return path
        
        # List of possible next states
        possible_states = []
        
        # Fill Jug A
        possible_states.append((capacity_a, jug_b))
        
        # Fill Jug B
        possible_states.append((jug_a, capacity_b))
        
        # Empty Jug A
        possible_states.append((0, jug_b))
        
        # Empty Jug B
        possible_states.append((jug_a, 0))
        
        # Pour water from Jug A to Jug B
        pour_a_to_b = min(jug_a, capacity_b - jug_b)
        possible_states.append((jug_a - pour_a_to_b, jug_b + pour_a_to_b))
        
        # Pour water from Jug B to Jug A
        pour_b_to_a = min(jug_b, capacity_a - jug_a)
        possible_states.append((jug_a + pour_b_to_a, jug_b - pour_b_to_a))
        
        # Add all valid states to the queue
        for state in possible_states:
            add_state(queue, visited, state, path + [state])
    
    # If no solution found
    return None

# Example Usage
if __name__ == "__main__":
    # Jug capacities
    capacity_a = 4  # Jug A capacity
    capacity_b = 3  # Jug B capacity
    
    # Target amount
    target = 2
    
    # Solve the problem
    solution = water_jug_solver(capacity_a, capacity_b, target)
    
    if solution:
        print("Solution found!")
        for step in solution:
            print(f"Jug A: {step[0]} liters, Jug B: {step[1]} liters")
    else:
        print("No solution exists.")
