import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, city_coordinates, city_groups):
    # Check starting and ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    # Check if one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for idx, group in enumerate(city_groups):
            if city in group:
                visited_groups[idx] += 1
    if any(count != 1 for count in visited_groups):
        return False

    return True

def calculate_total_travel_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_cost

# Provided solution details
solution_tour = [0, 5, 2, 9, 8, 0]
reported_cost = 183.98559431675523

# City coordinates and groups as per task description
city_coordinates = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}
city_groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Verifications
is_correct_tour = validate_tour(solution_tour, city_coordinates, city_groups)
calculated_cost = calculate_total_travel_cost(solution_tour, city_coordinates)

# Margin for floating-point arithmetic accuracy in cost comparison
epsilon = 1e-6
is_correct_cost = abs(calculated_cost - reported_cost) <= epsilon

if is_correct_tour and is_correct_cost:
    print("CORRECT")
else:
    print("FAIL")