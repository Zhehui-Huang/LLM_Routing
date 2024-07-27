import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities):
    # Check if the tour starts and ends at the depot, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at the depot city 0."
    
    # Check if each city is visited exactly once
    cities_visited = tour[:-1]  # Remove the last element as it's a repeat of the first element (depot)
    unique_cities_visited = set(cities_visited)
    if len(unique_cities_visited) != len(cities) - 1 or sorted(unique_cities_visited) != list(range(1, len(cities))):
        return False, "The robot does not visit each city exactly once."
    
    # Check travel cost and maximum distance between consecutive cities
    total_travel_cost = 0
    maximum_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_travel_cost += distance
        if distance > maximum_distance:
            maximum_distance = distance
    
    # The solution provided states the following:
    provided_total_travel_cost = float('inf')  # According to the problem statement it's infinity
    provided_maximum_distance = 610.59
    
    # Check if the provided total travel cost and maximum distance match the calculated
    if provided_total_travel_act != total_travel_cost:
        return False, "Provided total travel cost does not match the calculated travel cost."
    if not math.isclose(provided_maximum_distance, maximum_distance, abs_tol=0.01):
        return False, "Provided maximum distance does not match the calculated maximum distance."
    
    return True, "Solution valid."

# Define the coordinates of each city
cities = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Tour from the solution
tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Run the verification
correct, message = verify_solution(tour, cities)
print("CORRECT" if correct else "FAIL")