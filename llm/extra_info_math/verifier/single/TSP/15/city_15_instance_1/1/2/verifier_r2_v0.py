import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_tour(tour, distances, reported_cost):
    # Check start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities visited exactly once
    visited_cities = set(tour)
    if len(visited_cities) != len(tour) - 1 or any(city not in visited_cities for city in range(15)):
        return "FAIL"
    
    # Check total travel cost calculation
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43),
          (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Compute distances between each pair of cities
distances = [[calculate_distance(cities[i], cities[j]) for j in range(15)] for i in range(15)]

# Solution from model
tour = [0, 5, 13, 11, 12, 2, 8, 14, 6, 1, 7, 3, 9, 10, 4, 0]
reported_cost = 355.52373661497694

# Validate the solution
result = verify_tour(tour, distances, reported_cost)
print(result)