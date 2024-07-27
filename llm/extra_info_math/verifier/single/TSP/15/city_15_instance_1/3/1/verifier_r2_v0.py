import math

# Locations of cities
locations = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Tour given by the solver
tour = [0, 4, 10, 9, 3, 7, 1, 6, 14, 8, 2, 12, 11, 13, 5, 0]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((locations[city1][0] - locations[city2][0])**2 + (locations[city1][1] - locations[city2][1])**2)

# Calculate the total route distance
calculated_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Validate the solution
def validate_solution(tour, calculated_distance):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once
    unique_cities = set(tour[1:-1])  # exclude the depot city from the check
    if len(unique_cities) != 14 or not all(city in unique_cities for city in range(1, 15)):
        return "FAIL"
    
    # Check the accuracy of the reported total distance
    reported_distance = 355.52373661
    if not math.isclose(calculated_distance, reported_in_program_distance, abs_tol=0.0001):
        return "FAIL"

    return "CORRECT"

# Perform validation and print the result
result = validate_solution(tour, calculated_distance)
print(result)