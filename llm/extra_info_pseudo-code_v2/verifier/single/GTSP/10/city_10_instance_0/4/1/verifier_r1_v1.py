import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tour, total_travel_cost):
    # Coordinates of the cities
    cities = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 
        4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31), 
        8: (61, 90), 9: (42, 49)
    }
    
    # Grouping of cities
    city_groups = {
        0: [1, 2, 6],
        1: [3, 7, 8],
        2: [4, 5, 9]
    }

    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = [0 for _ in range(len(city_groups))]
    for city in tour[1:-1]:  # exclude the starting and ending depot city
        found = False
        for group_id, cities_in_group in city_groups.items():
            if city in cities_in_group:
                visited_groups[group_id] += 1
                found = True
                break
        if not found:
            return "FAIL"
    if any(v != 1 for v in visited_groups):
        return "FAIL"

    # Compute the total travel cost and compare
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
    
    if abs(calculated_cost - total_travel_cost) > 0.01:  # Allow a small float rounding difference
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Input solution
solution_tour = [0, 6, 7, 5, 0]
solution_cost = 74.95

# Run the provided solution through verification
result = verify_solution(solution_tour, solution_cost)
print(result)