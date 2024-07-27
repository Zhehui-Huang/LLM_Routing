import numpy as np

# List of given coordinates for the cities
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214),
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Solution: Robot tours
solutions = [
    [0, 14, 10, 8, 9, 7, 0],
    [1, 5, 6, 12, 18, 15, 1],
    [2, 19, 17, 21, 20, 13, 2],
    [3, 4, 11, 16, 3]
]

# Function for calculating distance between cities
def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(cities[city1]) - np.array(cities[city2]))

# Function to get the total cost of each route
def total_route_cost(route):
    return sum(calculate_distance(route[i], route[i + 1]) for i in range(len(route) - 1))

# Function to check the requirements from the test
def check_requirements():
    # Requirement 1: all cities visited exactly once excluding depots
    unique_cities = sorted(set(sum([tour[:-1] for tour in solutions], [])))
    if sorted(unique_cities) != list(range(22)):  # Check if it contains all cities
        return "FAIL"

    # Requirement 2: Each robot starts/ends at their respective depots
    for idx, tour in enumerate(solutions):
        if tour[0] != idx or tour[-1] != idx:
            return "FAIL"

    # Calculate and print individual cost for each robot
    costs = [total_route_cost(tour) for tour in solutions]
    print("Individual Robot Costs:")
    for i, cost in enumerate(costs):
        print(f"Robot {i} Total Travel Cost: {cost}")

    # Calculate overall cost
    overall_cost = sum(costs)
    print(f"Overall Total Travel Cost: {overall_cost}")

    # All checks pass
    return "CORRECT"

# Execute the check
result = check_requirements()
print("Validity of Solution:", result)