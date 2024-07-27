import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(tour, cost):
    # Specific coordinates from the task
    coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Check if tour length proper e.g., 21 cities including the return to depot
    if len(tour) != 21:
        return "FAIL"
    
    # Check if starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 19 or any(city < 1 or city > 19 for city in unique_cities):
        return "FAIL"
    
    # Calculate the travel cost from the tour and compare with given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)
    
    # Check if the calculated travel cost is within a small tolerance of the provided cost
    if not math.isclose(calculated_cost, cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and total cost
given_tour = [0, 19, 8, 10, 6, 15, 4, 3, 9, 5, 12, 7, 16, 2, 14, 11, 13, 1, 18, 17, 0]
given_cost = 432.3845867478549

# Run the test
outcome = check_solution(given_tour, given_cost)
print(outcome)