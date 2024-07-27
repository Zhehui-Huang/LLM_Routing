import math

# Define city coordinates
cities = [
    (29, 51),  # Depot
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

# Define the provided tour and total travel cost
provided_tour = [0, 5, 12, 11, 2, 8, 14, 13, 6, 1, 7, 3, 9, 10, 4, 0]
provided_total_cost = 373.4267090803889

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_solution_correct(tour, total_cost):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if all cities are visited exactly once, except depot
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or len(tour) != len(cities) + 1:
        return False
    
    # Check if calculated total cost matches the provided total cost
    calculated_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if abs(calculated_cost - total_cost) > 1e-6:
        return False
    
    return True

# Verify the provided solution
if is_solution_correct(provided_tour, provided_total_cost):
    print("CORRECT")
else:
    print("FAIL")