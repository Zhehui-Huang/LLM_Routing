def is_depot_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

def is_one_city_per_group(tour, groups):
    visited_groups = set()
    for city in tour:
        for idx, group in enumerate(groups):
            if city in group:
                visited_groups.add(idx)
    return len(visited_groups) == len(groups)

def calculate_euclidean_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    return total_cost

def check_tour_and_cost(tour, total_cost, cities, groups):
    if not is_depot_start_end(tour):
        return "FAIL"
    
    if not is_one_city_per_group(tour, groups):
        return "FAIL"
    
    calculated_cost = calculate_total_travel_distance(tour, cities)
    if abs(calculated_cost - total_cost) > 0.0001:
        return "FAIL"
    
    return "CORRECT"

# Define cities and groups based on the problem statement
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
          (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
          (56, 58), (72, 43), (6, 99)]
groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

# Given solution tour and cost
solution_tour = [6, 0]
solution_cost = 5.385164807134504

# Check the solution
result = check_tour_and_cost(solution_tour, solution_cost, cities, groups)
print(result)