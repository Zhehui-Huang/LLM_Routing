import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, costs):
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify each city is visited exactly once (except the depot city 0)
    unique_cities = set(tour)  # all cities including depot
    if len(unique_cities) != len(cities):
        return "FAIL"
    
    # Verify the travel cost using Euclidean distance
    calculated_cost = sum(calculate_euclidean_distance(cities[tour[i]][0], cities[tour[i]][1],
                                                       cities[tour[i+1]][0], cities[tour[i+1]][1])
                           for i in range(len(tour)-1))
    
    if abs(calculated_cost - costs) > 1e-5:
        print(f'Expected cost: {costs}, Calculated cost: {calculated_cost}')
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Provided solution tour and cost
tour = [0, 5, 13, 11, 12, 2, 8, 14, 6, 1, 7, 3, 9, 10, 4, 0]
total_travel_cost = 355.52373661497694

# Verify the solution
result = verify_tour(tour, total_travel_cost)
print(result)