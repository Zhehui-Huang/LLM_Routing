import math

# Define city coordinates (index 0 is depot)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# List of provided tours for each robot
provided_tours = [
    [0, 9, 13, 0],
    [0, 12, 15, 0],
    [0, 6, 0],
    [0, 4, 11, 0],
    [0, 5, 14, 0],
    [0, 3, 8, 0],
    [0, 1, 10, 0],
    [0, 2, 7, 0]
]

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Verify the solution
def verify_solution(tours, cities):
    visited = set()
    max_cost = 0

    # Check if there are 8 robots and each has a valid tour
    if len(tours) != 8:
        return "FAIL"

    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:  # Must start/end at depot
            return "FAIL"

        # Calculate the total travel cost for each tour
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
            # Verify each city is visited once (excluding depot)
            if tour[i] != 0:
                if tour[i] in visited:
                    return "FAIL"
                visited.add(tour[i])
        
        max_cost = max(max_cost, total_cost)

    # Check if all cities except the depot are visited exactly once
    if len(visited) != 15:
        return "FAIL"
    
    # The provided maximum travel cost check (based on the problem statement)
    if not math.isclose(max_cost, 72.81785234728197, abs_tol=1e-4):
        return "FAIL"

    return "CORRECT"

# Execute the verification function
result = verify_solution(provided_tours, cities)
print(result)