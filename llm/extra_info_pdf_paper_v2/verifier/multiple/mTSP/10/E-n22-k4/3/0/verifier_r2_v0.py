import math

# Define the city coordinates including the depot
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Tours given by the solution
tours = [
    [0, 1, 5, 9, 13, 17, 21, 0],
    [0, 2, 6, 10, 14, 18, 0],
    [0, 3, 7, 11, 15, 19, 0],
    [0, 4, 8, 12, 16, 20, 0]
]

# Function to calculate the Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Function to verify the solution
def verify_solution(tours, cities_coordinates):
    number_of_cities = len(cities_coordinates)
    cities_visited = set()

    # Check each tour
    total_cost_computed = 0
    for tour in tours:
        # Check starting and ending at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Accumulate visited cities
        cities_visited.update(tour)

        # Check tour cost
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
        
        # Accumulate total costs
        total_cost_computed += tour_cost
    
    # Calculate overall expected tour cost
    expected_total_cost = 739.3784294713529

    # Check if all cities are visited exactly once
    if cities_visited != set(range(number_of_cities)) or abs(total_cost_computed - expected_total_cost) > 0.001:
        return "FAIL"
    
    return "CORRECT"

# Call the verification function
verification_result = verify_solution(tours, cities_coordinates)
print(verification_result)