import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, total_travel_cost, cities):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 12 cities are visited
    if len(set(tour)) != 13:  # Including the depot twice (start and end)
        return "FAIL"
    
    # Calculate the actual total travel cost from the tour
    calc_cost = 0
    for i in range(len(tour) - 1):
        calc_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the calculated cost is equal to the provided total travel cost
    if not math.isclose(calc_lest_cost, total_travel_cost, abs_tol=0.01):  # allowing a small tolerance for floating point operations
        return "FAIL"

    return "CORRECT"

# Cities as provided in task description
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Hypothetical tour output from TSP solution
hypothetical_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
hypothetical_total_travel_cost = 230.67

# Function call to check if the solution meets the requirements
result = check_solution(hypothetical_tour, hypothetical_total_travel_cost, cities)
print(result)