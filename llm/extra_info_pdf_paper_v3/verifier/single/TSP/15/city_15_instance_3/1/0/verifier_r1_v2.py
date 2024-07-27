import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_valid_tour(tour, num_cities):
    # Check if tour starts and ends at the depot and includes all cities exactly once
    return tour[0] == 0 and tour[-1] == 0 and len(set(tour)) == num_cities + 1

def compute_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        total_cost += calculate_euclidean_distance(
            coordinates[city1][0], coordinates[city1][1],
            coordinates[city2][0], coordinates[city2][1])
    return total_cost

# City coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Provided solution
provided_tour = [0, 6, 13, 10, 9, 5, 14, 8, 11, 2, 7, 3, 12, 4, 1, 0]
provided_cost = 317.2368147961308

# Check constraints
num_cities = len(coordinates) - 1  # excluding the depot

if is_valid_tour(provided_tour, num_cities):
    calculated_cost = compute_total_travel_cost(provided_tour, coordinates)
    if abs(provided_cost - calculated_cost) < 0.1:  # Allow margin for floating point error
        print("CORRECT")
    else:
        print(f"FAIL: Incorrect travel cost calculation. Expected {provided_cost} but got {calculated_cost}")
else:
    print("FAIL: Tour is not valid.")