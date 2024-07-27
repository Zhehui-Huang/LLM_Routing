import numpy as np

# Coordinates of cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# List of robots' tours and their respective travel costs
tours = [
    ([5, 11, 5], 15.696383925166547),
    ([14, 4, 14], 27.6072206698546),
    ([9, 10, 9], 14.282170362793455),
    ([13, 1, 13], 23.942319610570692),
    ([8, 0, 8], 19.85184425469895),
    ([3, 6, 3], 20.116978793239788),
    ([12, 2, 12], 14.868559065654289),
    ([15, 7, 15], 18.04987562112089)
]

def calculate_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def check_robot_tours(tours):
    # Count visited cities and check start/end conditions
    visited_cities = set()
    correct_start_end = True
    total_cost_calc = 0

    for tour, given_cost in tours:
        # Check start and end at the depot city
        if tour[0] != tour[-1]:
            correct_start_end = False
        
        # Add visited cities accounting for starting/ending at the depot
        visited_cities.update(tour[:-1])  # Exclude the duplicated depot at the end
        
        # Calculate the travel cost based on the tour
        calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Add the calculated cost
        total_cost_calc += calculated_cost
        
        # Tolerance for floating point comparisons
        if not np.isclose(calculated_cost, given_cost, atol=1e-6):
            return "FAIL due to incorrect cost calculation."

    # Check if all cities are visited exactly once and each robot returns to the start
    if len(visited_cities) != 16 or not correct_start_end:
        return "FAIL due to incorrect city visitations or tour endpoint issues."

    # Check if the total calculated cost is correct
    given_total_cost = sum(cost for _, cost in tours)
    if not np.isclose(total_cost_calc, given_total_cost, atol=1e-6):
        return "FAIL due to incorrect total cost calculation."
    
    return "CORRECT"

# Perform the check
result = check_robot_tours(tours)
print(result)