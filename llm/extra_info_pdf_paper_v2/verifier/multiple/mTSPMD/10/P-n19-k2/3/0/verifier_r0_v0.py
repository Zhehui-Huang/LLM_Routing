import numpy as np

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_cost(tour, city_coords):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(city_coords[tour[i-1]], city_coords[tour[i]])
    return total_cost

def verify_solution():
    # Coordinates of each city
    city_coords = [
        (30, 40), (37, 52), (49, 43), (52, 64),
        (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 27), (37, 69), (61, 33),
        (62, 63), (63, 69), (45, 35)
    ]
    
    # Provided solution
    best_tour = [1, 10, 6, 18, 5, 13, 15, 9, 7, 2, 17, 16, 8, 3, 12, 14, 4, 11, 1]
    provided_total_cost = 176.56740268681875

    # Verification against the requirements
    if best_tour[0] != best_tour[-1] or best_tour[0] != 1:
        return "FAIL: Tour does not start and end at depot 1 as required."

    if len(set(best_tour)) != len(city_coords):
        return "FAIL: Not all cities are visited exactly once."

    calculated_cost = calculate_total_cost(best_tour, city_coords)
    if not np.isclose(provided_total_cost, calculated_cost, atol=0.001):
        return f"FAIL: Provided total travel cost does not match calculated cost. (Provided: {provided_total_cost}, Calculated: {calculated_cost})"

    # If all checks pass
    return "CORRECT"

# Execute the verification
print(verify_solution())