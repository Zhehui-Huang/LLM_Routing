import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tsp_solution(cities, tour, reported_cost, epsilon=0.01):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    visited = set(tour)
    if len(visited) != len(cities) or any(city not in visited for city in range(len(cities))):
        return "FAIL"
    
    # Calculate the total cost of the provided tour
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the reported cost is approximately equal to the calculated cost
    if not (abs(total_cost - reported_cost) <= epsilon):
        return "FAIL"
    
    return "CORRECT"

# Define the cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Provided tour and cost
tour = [0, 19, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 6, 3, 4, 15, 10, 0]
reported_cost = 379.72475773064514

# Function to validate the tour and its cost
result = verify_tsp_solution(cities, tour, reported_cost)
print(result)