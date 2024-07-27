import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cost):
    # Cities coordinates
    city_coords = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
        (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
        (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), 
        (64, 72), (14, 89)
    ]
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits exactly 16 cities
    if len(set(tour)) != 16:
        return "FAIL"
    
    # Calculate the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i + 1]])
    
    # Check if the total travel cost is correct
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Solution details
tour = [0, 8, 17, 18, 13, 1, 11, 14, 5, 9, 10, 15, 6, 3, 4, 19, 0]
total_travel_cost = 346.4195923229701

# Verify the solution
result = verify_tour(tour, total_travel_cost)
print(result)