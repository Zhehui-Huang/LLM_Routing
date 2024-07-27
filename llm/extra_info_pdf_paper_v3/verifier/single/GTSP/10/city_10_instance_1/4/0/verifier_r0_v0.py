import math

# Given city positions
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Provided solution tour and total cost
solution_tour = [0, 9, 5, 3, 4, 0]
provided_total_cost = 174.66

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check if the tour starts and ends at the depot city
def check_start_end_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if the robot visits exactly one city from each group
def check_one_city_per_group(tour):
    seen_groups = set()
    for city in tour:
        for group_id, members in groups.items():
            if city in members:
                if group_id in seen_groups:
                    return False
                seen_groups.add(group_id)
    return True

# Check if provided total cost is correct
def check_total_cost(tour, expected_total_cost):
    calculated_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return math.isclose(calculated_cost, expected_total_cost, rel_tol=1e-2)

# Main function to evaluate the solution
def evaluate_solution():
    if (check_start_end_depot(solution_tour) and
        check_one_city_per_group(solution_tour) and
        check_total_cost(solution_tour, provided_total_cost)):
        return "CORRECT"
    else:
        return "FAIL"

# Test the solution
print(evaluate_solution())