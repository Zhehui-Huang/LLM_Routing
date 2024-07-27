import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, total_travel_cost):
    # Given city coordinates
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
    
    # Checkpoints
    try:
        # Check tour starts and ends at depot city (city 0)
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check exactly 7 unique cities are visited
        if len(set(tour)) != 7:
            return "FAIL"
        
        # Calculate the travel cost
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
        # Check if the calculated cost matches the reported cost
        if not math.isclose(calculated_cost, total_travel._cost, rel_tol=1e-2):
            return "FAIL"
        
        return "CORRECT"
    except:
        return "FAIL"

# Solution provided
tour = [0, 4, 2, 1, 7, 3, 8, 0]
total_travel_cost = 159.97

# Validate and print the result
result = validate_solution(tour, total_travel_cost)
print(result)