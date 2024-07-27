import math

def compute_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_tour(tour, coords):
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour must start and end at the depot city (city 0)."
    if len(set(tour)) != len(coords):
        return False, "Tour must visit each city exactly once."
    if sorted(tour) != sorted(list(range(len(coords)))):
        return False, "Tour must include every city."
    return True, "Validation successful."

def check_total_cost(tour, coords, reported_cost):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i+1]
        total_cost += compute_distance(*coords[city1], *coords[city2])
    if abs(total_cost - reported_cost) > 1e-2:
        return False, f"Reported travel cost doesn't match computed: {reported_cost} vs {total_cost}"
    return True, "Cost validation successful."

def test_solution(tour, total_cost):
    # Coordinates of cities including the depot city
    coords = [(3,26),(85,72),(67,0),(50,99),(61,89),(91,56),(2,65),(38,68),(3,92),(59,8),
              (30,88),(30,53),(11,14),(52,49),(18,49),(64,41),(28,49),(91,94),(51,58),(30,48)]
    
    valid_tour, tour_message = check_tour(tour, coords)
    if not valid_tour:
        return "FAIL", tour_message
    
    valid_cost, cost_message = check_total_cost(tour, coords, total_cost)
    if not valid_cost:
        return "FAIL", cost_message
    
    return "CORRECT", "Solution meets all requirements."

# Given solution
tour = [0, 12, 16, 11, 13, 18, 7, 3, 4, 17, 1, 5, 15, 2, 9, 19, 14, 6, 10, 8, 0]
total_cost = 520.95

# Test the solution
result, message = test_solution(tour, total_cost)
print("Result:", result)
print("Message:", message)