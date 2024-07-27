import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(tours, costs, city_positions):
    visited_cities = set()
    all_cities = set(range(1, len(city_positions)))  # excluding the depot city
    
    for tour in tours:
        # Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        for i in range(1, len(tour)):
            visited_cities.add(tour[i])
    
    # Check if every city, except the depot, is visited exactly once
    if visited_cities != all_cities:
        return "FAIL"
    
    # Check if the cost reported matches the calculated cost for each tour
    for idx, tour in enumerate(tours):
        total_cost = 0
        for j in range(len(tour) - 1):
            total_cost += calculate_distance(city_positions[tour[j]], city_positions[tour[j+1]])
        if round(total_cost, 2) != costs[idx]:
            return "FAIL"
    
    # Maximum travel cost check
    if max(costs) != costs[-1]:  # Assuming the last cost in the list is the maximum travel cost reported
        return "FAIL"
    
    return "CORRECT"

# Given data from task solution
city_positions = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
                  (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
                  (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

tours = [
    [0, 5, 14, 17, 22, 0],
    [0, 2, 7, 9, 13, 0],
    [0, 4, 11, 12, 15, 0],
    [0, 3, 0],
    [0, 1, 10, 0],
    [0, 21, 0],
    [0, 8, 18, 19, 0],
    [0, 6, 16, 20, 0]
]

costs = [70.86, 75.95, 81.42, 65.12, 41.77, 4.47, 89.54, 47.29]

# Execute the validation
print(validate_solution(tours, costs, city_positions))