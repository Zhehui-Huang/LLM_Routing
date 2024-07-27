import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, max_distance):
    # Requirement 1: All cities must be visited exactly once, starting and ending at depot city
    if sorted(tour) != sorted(list(set(tour))) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Calculate total travel distance using Euclidean distance
    total_distance = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_distance += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    print("Calculated Total Distance:", total_distance)
    print("Calculated Max Distance Between Consecutive Cities:", calculated_max_distance)
    
    # Requirement 3: Check if the longest distance between any two consecutive cities is minimized
    if calculated_max_op_distance > max_distance:
        return "FAIL"
    
    return "CORRECT"

# Define the city coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Provide the tour from the solution
tour = [0, 4, 3, 6, 2, 8, 9, 7, 5, 1, 0]
# Maximum distance output from the solution
max_consecutive_distance = 61.68468205316454

# Verify the solution
result = verify_solution(cities, tour, max_consecutive_distance)
print("Unit Test Result:", result)