import math

# Given city coordinates
city_coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# City groups
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Provided solution
solution_tour = [0, 1, 0]
reported_cost = 268.18

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total cost of a tour
def calculate_total_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Test if the tour is valid and if it meets the requirements
def is_valid_tour(tour, city_groups):
    # Requirement 1: Starts and ends at the depot (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Requirement 2: Visits exactly one city from each group
    visited_cities = tour[1:-1]  # Exclude depot at start and end
    visited_groups = {}
    for city in visited_cities:
        for index, group in enumerate(city_groups):
            if city in group:
                if index in visited_groups:
                    return False  # City from the same group visited more than once
                visited_groups[index] = city
    if len(visited_groups) != len(city_groups):
        return False  # Not all groups are visited
    
    # Requirement 3: Minimal cost check is assumed outside this function.
    
    return True

# Verify the solution
if (is_valid_tour(solution_tour, city_groups) and 
    math.isclose(reported_cost, calculate_total_cost(solution_tour), abs_tol=1e-2)):
    print("CORRECT")
else:
    print("FAIL")