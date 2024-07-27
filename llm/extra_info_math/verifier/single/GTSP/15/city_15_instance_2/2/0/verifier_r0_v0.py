# Define the city coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28),
    11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Groups of cities
city_groups = {0: [8, 12, 14], 1: [7, 10, 11], 2: [4, 6, 9], 3: [1, 3, 13], 4: [2, 5]}

# Solution tour and its cost
solution_tour = [0, 6, 0]
solution_cost = 10.77

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return ((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2) ** 0.5

# Validate the tour
def validate_tour(tour, groups, expected_cost):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited = set(tour[1:-1])  # excluding the depot visits
    for group_id, group_cities in groups.items():
        if len(visited.intersection(set(group_cities))) != 1:
            return "FAIL"
    
    # Check costs
    total_calculated_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if not (abs(total_calculated_cost - expected_cost) < 0.1):  # using a small tolerance
        return "FAIL"
    
    return "CORRECT"

# Perform the validation
validation_result = validate_tour(solution_tour, city_groups, solution_cost)
print(validation_result)