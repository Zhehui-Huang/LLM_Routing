import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, cities, groups):
    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: One city from each group
    visited_groups = []
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for i, group in enumerate(groups):
            if city in group:
                if i in visited_groups:
                    return "FAIL"
                visited_groups.append(i)
                break
        else:
            return "FAIL"  # City not found in any group
    
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Requirement 3: Travel cost calculated as Euclidean distance
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    provided_total_cost = 74.94753083872993
    
    if round(total_calculated_cost, 5) != round(provided_total_cost, 5):
        return "FAIL"
    
    return "CORRECT"

# Define cities and groups
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}
groups = [[1, 2, 6], [3, 7, 8], [4, 5, 9]]

# Provided tour and cost
provided_tour = [0, 6, 7, 5, 0]

# Check if the provided solution is correct
result = check_solution(provided_tour, cities, groups)
print(result)