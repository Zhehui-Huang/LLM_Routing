import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def check_tour_and_cost(tour, total_travel_cost, coordinates):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL, Tour does not start and end at the depot city"
    
    if sorted(tour[1:-1]) != list(range(1, 15)):
        return "FAIL, Not all cities are visited exactly once"
    
    def tour_cost(tour):
        return sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    
    calculated_cost = tour_cost(tour)
    
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=1e-3):
        return f"FAIL, Incorrect total travel cost calculated: {calculated_cost}"
    
    return "CORRECT"

# Coordinates of each city including the depot
coordinates = [
    (29, 51),  # Depot city 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Provided solution and cost
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
total_travel_cost = 442.570870788815

# Check the solution against the requirements
result = check_tour_and_cost(tour, total_travel_cost, coordinates)
print(result)