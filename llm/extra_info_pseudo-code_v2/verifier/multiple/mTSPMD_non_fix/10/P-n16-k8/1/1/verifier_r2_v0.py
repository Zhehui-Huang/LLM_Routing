import math

# Function to calculate Euclidean Distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Define the city coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Given robot tours
robot_tours = [
    [0, 7, 13, 0],
    [0, 10, 3, 0],
    [0, 6, 5, 0],
    [0, 7, 5, 0],
    [0, 10, 11, 0],
    [0, 2, 1, 0],
    [0, 1, 7, 0],
    [0, 6, 0]
]

# Given robot tour costs
robot_costs = [60.36, 65.57, 47.93, 53.11, 67.57, 47.29, 54.52, 24.08]
declared_total_cost = 420.43

# Helper function to determine if all cities are visited exactly once
def all_cities_visited_once(tours):
    all_visited = set()
    for tour in tours:
        for city in tour:
            if city in all_visited and city != 0:  # All start at city 0
                return False
            all_visited.add(city)
    return len(all_visited) == 16  # Including all cities and depot

def calculate_cost(tour):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_cost
    
def total_travel_cost(robots_tours):
    total = 0.0
    for tour in robots_tours:
        total += calculate_cost(tour)
    return total

# Check each robot starts and ends at depot, and the costs are correctly calculated
def check_tours_and_costs(tours, costs):
    calculated_costs= []
    for tour in tours:
        calculated_costs.append(round(calculate_cost(tour), 2))
    return all(c == oc for c, oc in zip(calculated_costs, costs))
    
def test_solution():
    if not all_cities_visited_once(robot_tours):
        return "FAIL"
    if not check_tours_and_costs(robot_tours, robot_costs):
        return "FAIL"
    calculated_total_cost = round(total_travel_cost(robot_tours), 2)
    if calculated_total_cost != declared_total_cost:
        return "FAIL"
    return "CORRECT"

# Run the test function and print the result
print(test_solution())