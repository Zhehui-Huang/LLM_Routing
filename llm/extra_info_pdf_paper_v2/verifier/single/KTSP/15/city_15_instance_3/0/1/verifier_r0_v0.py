import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour(tour, cities, total_cost):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 10 cities are visited (including the depot city, hence 9 unique other cities)
    if len(tour) != 11 or len(set(tour)) != 10:
        return "FAIL"
    
    # Calculate the total travel cost using Euclidean distance and compare with given total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(calculated_cost - total_cost) > 1e-5:  # Using a small threshold to handle floating point arithmetic imprecision
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Tour and total cost provided
tour = [0, 5, 8, 10, 1, 12, 3, 7, 11, 2, 0]
total_cost = 325.3773742473662

# Check the tour
result = check_tour(tour, cities, total_cost)
print(result)