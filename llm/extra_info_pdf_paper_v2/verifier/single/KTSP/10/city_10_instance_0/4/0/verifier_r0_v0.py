import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, cost):
    # City coordinates
    city_coords = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
        5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
    }
    
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 4 cities are visited, including the depot
    if len(tour) != 5:
        return "FAIL"
    
    # Check if the tour is listed as starting and ending with city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Compute actual travel cost
    actual_cost = sum(euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]]) for i in range(len(tour) - 1))
    
    # Round actual cost to avoid floating point inaccuracies
    actual_cost = round(actual_cost, 0)  # Assuming cost rounding for comparison as problem definition allows

    # Check if the total travel distance calculated matches the given cost
    if actual_cost != cost:
        return "FAIL"
    
    # If all checks have been passed
    return "CORRECT"

# Declare the tour and cost provided in the solution
provided_tour = [0, 6, 5, 9, 0]
provided_cost = 60

# Check if the provided solution is correct
result = check_solution(provided_tour, provided_cost)
print(result)