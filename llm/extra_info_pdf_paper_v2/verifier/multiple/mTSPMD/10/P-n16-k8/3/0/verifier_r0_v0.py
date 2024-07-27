import numpy as np

# Coordinates of the cities and depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),  # Depots 0-7
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)   # Cities 8-15
]

# Output from the solution for tours and costs
robots_tours = {
    0: [0, 10, 1, 0],
    1: [1, 10, 2, 1],
    2: [2, 7, 5, 2],
    3: [3, 12, 15, 3],
    4: [4, 12, 15, 4],
    5: [5, 13, 2, 5],
    6: [6, 7, 2, 6],
    7: [7, 2, 13, 7]
}

robots_costs = {
    0: 41.77216384800009,
    1: 30.070530501453106,
    2: 32.82282434141724,
    3: 31.622776601683796,
    4: 28.544099777629647,
    5: 41.489700155640634,
    6: 29.174149558052182,
    7: 26.818933340747837
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return np.hypot(coordinates[c1][0] - coordinates[c2][0], coordinates[c1][1] - coordinates[c2][1])

# Check all requirements
def verify_solution():
    visited_cities = set()
    total_calculated_cost = 0
    num_robots = len(robots_tours)
    
    for robot_id in range(num_robots):
        tour = robots_tours[robot_id]
        cost = robots_costs[robot_id]
        calculated_cost = 0
        
        if tour[0] != tour[-1] or tour[0] != robot_id:
            print(f"FAIL - Robot {robot_id} does not start and end at the correct depot")
            return
        
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i+1]
            visited_cities.add(city1)  # Add city to visited set
            calculated_cost += euclidean_distance(city1, city2)
        
        # Tolerate small float precision errors in cost calculations by checking close approximate
        if not np.isclose(calculated_cost, cost, atol=0.0001):
            print(f"FAIL - Cost mismatch for Robot {robotid}: Expected {cost}, Calculated {calculated_cost}")
            return
        
        total_calculated_cost += calculated_cost
        
    # Check if all cities are visited exactly once
    if len(visited_cities) != 16:
        print("FAIL - Not all cities are visited or some cities are visited more than once")
        return
    
    total_reported_cost = sum(robots_costs.values())
    if not np.isclose(total_calculated_cost, total_reported_cost, atol=0.0001):
        print(f"FAIL - Total cost mismatch: Expected {total_reported_cost}, Calculated {total_calculated_cost}")
        return
    
    print("CORRECT")

verify_solution()