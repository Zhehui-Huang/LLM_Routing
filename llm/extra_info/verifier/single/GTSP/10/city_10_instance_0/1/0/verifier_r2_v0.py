import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # City coordinates
    cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), 
              (62, 26), (79, 31), (61, 90), (42, 49)]
    
    # City groups
    groups = [[1, 2, 6], [3, 7, 8], [4, 5, 9]]
    
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if tour visits exactly one city from each group
    visited_groups = [False] * len(groups)
    for i in range(1, len(tour) - 1):  # exclude the depot at the beginning and end
        city = tour[i]
        for j, group in enumerate(groups):
            if city in group:
                if visited_groups[j]:
                    return "FAIL"
                visited_groups[j] = True
                break
    
    if not all(visited_groups):
        return "FAIL"
    
    # Calculate the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if calculated cost matches the provided total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and total cost
tour = [0, 6, 7, 5, 0]
total_cost = 74.95
result = verify_solution(tour, total_cost)
print(result)