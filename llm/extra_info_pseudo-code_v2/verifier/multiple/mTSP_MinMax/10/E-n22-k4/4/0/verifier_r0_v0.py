import math
from itertools import chain

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the city coordinates (depot included)
city_coordinates = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Tests to verify solution correctness
robot_tours = [
    [0, 10, 1, 4, 6, 17, 0],
    [0, 14, 9, 15, 18, 0],
    [0, 21, 20, 8, 0],
    [0, 5, 3, 2, 7, 12, 13, 16, 19, 11, 0]
]

tour_costs = [169.41905852193324, 111.91448167992493, 129.54938981148746, 272.63646430910745]
max_travel_cost = max(tour_costs)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return cost

def verify_solution():
    # Check if each tour starts and ends at depot
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Check that each city, except the depot, is visited exactly once in total
    visit_counts = {}
    for tour in robot_tours:
        for city in tour[1:-1]:  # Exclude depot in visits
            if city in visit_counts:
                visit_counts[city] += 1
            else:
                visit_counts[city] = 1
    
    if len(visit_counts) != len(city_coordinates) - 1:
        return "FAIL"
    
    if any(count != 1 for count in visit_counts.values()):
        return "FAIL"
    
    # Check if the costs of tours are correctly calculated and matches maximum cost
    calculated_costs = [calculate_tour_cost(tour) for tour in robot_tours]
    if any(abs(calculated_costs[i] - tour_costs[i]) > 1e-6 for i in range(len(tour_costs))):
        return "FAIL"
    
    if max(calculated_costs) != max_travel_cost:
        return "FAIL"
    
    # All tests passed
    return "CORRECT"

# Run the verification
result = verify_solution()
print(result)