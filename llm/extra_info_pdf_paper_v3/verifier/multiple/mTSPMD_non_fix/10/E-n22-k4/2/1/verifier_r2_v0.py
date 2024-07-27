import math

# Given tours and costs
tours = {
    0: {"tour": [0, 17, 14, 15, 6], "cost": 97.17},
    1: {"tour": [1, 18, 16, 11, 13], "cost": 143.81},
    2: {"tour": [2, 7, 4, 5, 8], "cost": 111.41},
    3: {"tour": [3, 12, 21, 9, 20, 10, 19], "cost": 289.38}
}

depots = [0, 1, 2, 3]
overall_cost = 641.77

def check_tours(tours, depots, overall_cost):
    visited_cities = set()
    total_calculated_cost = 0.0

    for k, v in tours.items():
        tour = v['tour']
        cost = v['cost']

        # Check if tour starts with the correct depot for the robot
        if tour[0] != depots[k]:
            print(f"Robot {k} does not start at the correct depot.")
            return "FAIL"
        
        # Check that cities are visited once collectively, accumulate visited cities
        for city in tour:
            if city in visited_cities and city not in depots:
                print(f"City {city} visited more than once.")
                return "FAIL"
            visited_cities.add(city)

        # Calculating the travel cost to verify the provided costs
        calculated_cost = 0.0
        for i in range(len(tour) - 1):
            x1, y1 = coordinates[tour[i]]
            x2, y2 = coordinates[tour[i+1]]
            calculated_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        # Compare calculated cost with the given cost, allowing small floating point errors
        if not math.isclose(calculated_cost, cost, abs_tol=0.1):
            print(f"Calculated cost {calculated_cost} does not match given cost {cost} for Robot {k}.")
            return "FAIL"
        
        total_calculated_cost += calculated_cost
    
    # Check all cities are visited exactly once
    if len(visited_cities) != 22:
        print("Not all cities are visited exactly once.")
        return "FAIL"
    
    # Verify the overall total cost matches
    if not math.isclose(total_calculated_cost, overall_cost, abs_tol=0.1):
        print(f"Total calculated cost {total_calculated_cost} does not match given overall cost {overall_cost}.")
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates as given in the problem to calculate distances if needed
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), 
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), 
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), 
    (139, 182)
]

# Call the validation function
result = check_tours(tours, depots, overall_cost)
print(result)