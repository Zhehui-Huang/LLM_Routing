import math

def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def check_solution(tour, cities, expected_total_cost):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 7 cities are visited including the depot
    if len(set(tour)) != 8 or len(tour) != 8:
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if calculated total distance matches expected total distance
    if not math.isclose(total_distance, expected_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = [ 
    (84, 67),  #city 0
    (74, 40),  #city 1
    (71, 13),  #city 2
    (74, 82),  #city 3
    (97, 28),  #city 4
    (0, 31),   #city 5
    (8, 62),   #city 6
    (74, 56),  #city 7
    (85, 71),  #city 8
    (6, 76)    #city 9
]

# Provided solution tour and expected total cost
solution_tour = [0, 4, 2, 1, 7, 3, 8, 0]
expected_total_cost = 159.97188184793015

# Validate the solution
result = check_solution(solution_tour, cities, expected_total_cost)
print(result)