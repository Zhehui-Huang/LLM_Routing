import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_tour(tour, travel_cost):
    # City coordinates
    cities = [
        (29, 51), 
        (49, 20), 
        (79, 69), 
        (17, 20), 
        (18, 61), 
        (40, 57), 
        (57, 30), 
        (36, 12), 
        (93, 43), 
        (17, 36), 
        (4, 60), 
        (78, 82), 
        (83, 96), 
        (60, 50), 
        (98, 1)
    ]
    
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 6 cities (including depot) are visited
    if len(tour) != 7:  # 6 cities + depot at the end to make a round trip
        return "FAIL"
    
    # Check if there are any duplicate visits to cities (excl. the depot at the start/end)
    if len(set(tour[:-1])) != len(tour[:-1]):
        return "FAIL"
    
    # Calculate the total travel cost based on Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)
    
    # Compare the provided travel cost and the calculated cost
    if abs(calculated_cost - travel_cost) > 1e-6:  # allowing small float error margin
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 6, 1, 7, 3, 9, 0]
travel_cost = 118.8954868377263

# Output "CORRECT" or "FAIL"
result = verify_tour(tour, travel_cost)
print(result)