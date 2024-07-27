import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_cost(tour, total_cost, cities):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Check the computed total distance
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
    # Allow for floating point arithmetic by using a tolerance
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Cities coordinates
cities = [
    (54, 87),  # Depot city 0
    (21, 84), 
    (69, 84), 
    (53, 40),  
    (54, 42),  
    (36, 30),  
    (52, 82),  
    (93, 44),  
    (21, 78),  
    (68, 14),  
    (51, 28),  
    (44, 79),  
    (56, 58),  
    (72, 43),  
    (6, 99)
]

# Provided solution details
tour = [0, 3, 5, 10, 9, 7, 13, 4, 12, 2, 6, 11, 8, 1, 14, 0]
total_cost = 352.5588278394239

# Validate the tour and cost calculation
result = verify_tour_and_cost(tour, total_cost, cities)
print(result)