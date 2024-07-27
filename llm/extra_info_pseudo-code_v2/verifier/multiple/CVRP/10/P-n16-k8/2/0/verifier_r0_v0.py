import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# City demands
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot tours and their reported costs
robot_tours = [
    ([0, 9, 13, 0], 68.39398119181284),
    ([0, 12, 15, 0], 66.12407122823275),
    ([0, 5, 14, 0], 62.44277221633522),
    ([0, 4, 11, 0], 57.394073777130664),
    ([0, 3, 10, 0], 65.57284885461793),
    ([0, 1, 7, 0], 54.51623477273332),
    ([0, 2, 0], 42.04759208325728),
    ([0, 6, 0], 24.08318915758459)
]

# Robot capacity
robot_capacity = 35

# To verify each of the conditions
def verify_solution():
    covered_cities = set()
    for tour, reported_cost in robot_tours:
        load = 0
        total_calculated_cost = 0
        
        # Check return to depot and start from depot
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Tour must start and end at the depot.")
            return
        
        # Calculate travel cost and load
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            load += demands[city_to]
            distance = euclidean_distance(*coordinates[city_from], *coordinates[city_to])
            total_calculated_cost += distance
        
        # Check load does not exceed capacity
        if load > robot_capacity:
            print("FAIL: Robot carrying capacity exceeded.")
            return
        
        # Check the computed cost and reported cost
        if not math.isclose(total_calculated_cost, reported_cost, rel_tol=1e-5):
            print("FAIL: Travel cost mismatch.")
            return
        
        covered_cities.update(tour[1:-1])
    
    # Check all cities are covered except the depot
    if covered_cities != set(range(1, 16)):
        print("FAIL: Not all cities are covered.")
        return
    
    print("CORRECT")

verify_solution()