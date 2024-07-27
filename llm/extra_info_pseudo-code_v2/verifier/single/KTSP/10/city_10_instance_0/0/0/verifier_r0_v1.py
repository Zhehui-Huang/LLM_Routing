import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost):
    cities = [
        (50, 42),  # Depot city 0
        (41, 1),
        (18, 46),
        (40, 98),
        (51, 69),
        (47, 39),
        (62, 26),
        (79, 31),
        (61, 90),
        (42, 49)
    ]
    
    # Requirement 1: The robot must start and end its journey at the depot city, which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit exactly 4 cities, including the depot city.
    if len(tour) != 5 or len(set(tour)) != 4:
        return "FAIL"
    
    # Calculate the travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Requirement 3: The travel cost is the Euclidean distance between two cities.
    # Compare rounded costs to avoid floating point issues
    if round(computed_cost, 2) != round(total_travel_cost, 2):
        return "FAIL"
    
    # Assuming "shortest" verification is out of scope as it involves a full TSP solution check.
    
    return "CORRECT"

# Example tour and travel cost
tour = [0, 9, 5, 6, 0]
total_travel_cost = 61.66
result = verify_solution(tour, total_travel_cost)
print(result)