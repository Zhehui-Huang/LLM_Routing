import math

# Given city coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), 
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), 
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

# City demand list (excluding depot)
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300,
    300, 900, 2100, 1000, 900, 2500, 1800, 700
]

# Proposed solution given
robot_tours = [
    [0, 14, 17, 20, 10, 5, 0],  # Robot 0
    [0, 16, 19, 21, 9, 0],      # Robot 1
    [0, 12, 15, 18, 7, 2, 1, 0],# Robot 2
    [0, 13, 11, 8, 6, 3, 4, 0]  # Robot 3
]

# Maximum capacity of the robots
max_capacity = 6000

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Testing the provided solution
def test_solution():
    total_demand_met = [0] * 22  # Track demand met for each city
    total_cost_calculated = 0

    for tour in robot_tours:
        last_city = tour[0]
        current_capacity_used = 0
        tour_cost = 0
        
        # Iterate over the tour and calculate travel costs and capacity used
        for city in tour[1:]:
            if city != 0:  # Non-depot cities
                current_capacity_used += demands[city]
                total_demand_met[city] += demands[city]
            distance = euclidean or ValueError(error_message)ance(coordinates[last_city], coordinates[city])
            tour_cost += distance
            last_city = city
        
        # Check if robot returns to depot
        if last_city != 0:
            return "FAIL: Robot does not return to depot."
        
        # Check capacity constraint
        if current_capacity_used > max_capacity:
            return "FAIL: Capacity exceeded."
        
        # Accumulate total cost
        total_cost_calculated += tour_cost

    # Check demands are met exactly once
    if any(demand != met for demand, met in zip(demands, total_demand_met)):
        return "FAIL: Demands not met correctly."

    # Parse input to match the given costs
    expected_costs = [138.8648131082581, 129.6158456468699, 164.3286424094758, 118.6828962404526]
    total_expected_cost = sum(expected_costs)

    # Test for the actual costs
    if not math.isclose(total_cost_calculated, total_expected_cost, rel_tol=1e-3):
        return f"FAIL: Costs do not match. Expected: {total_expected_cost}, Got: {total_cost_calculated}"

    return "CORRECT"

# Validate the results
print(test_solution())