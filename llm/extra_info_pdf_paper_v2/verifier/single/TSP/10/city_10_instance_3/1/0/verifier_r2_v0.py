import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    # Coordinates of the cities
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Provided solution details
    tour = [5, 6, 9, 3, 7, 1, 2, 4, 8, 0, 0]
    reported_total_cost = 262.37
    
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, except depot
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 9 or set(range(1, 10)) != unique_cities:
        return "FAIL"
    
    # Calculate the total travel cost using Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check if the calculated total cost is close to the reported cost
    if not math.isclose(total_cost, reported_total_cost, abs_tol=1e-1):
        return "FAIL"
    
    return "CORRECT"

# Running the test function to validate the provided solution
print(test_solution())