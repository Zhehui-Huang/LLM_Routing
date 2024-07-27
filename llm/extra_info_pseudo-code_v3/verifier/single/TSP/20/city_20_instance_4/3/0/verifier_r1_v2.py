from math import sqrt

# Define cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Tour provided
tour_provided = [0, 19, 8, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 13, 1, 18, 17, 0]
# Total travel cost provided
travel_cost_provided = 398.667866225166

# Calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Verify the tour starts and ends at the depot, and visits all cities exactly once
def verify_tour_structure(tour):
    if tour[0] != 0 or tour[-1] != 0:
        return False
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return False
    return True

# Verify the travel cost calculation
def verify_travel_cost(tour, reported_cost):
    computed_cost = sum(calculate\(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return abs(computed_cost - reported_cost) < 0.001

# Test solution
def test_solution():
    if not verify_tour_structure(tour_provided):
        return "FAIL [Requirement 1 and 4]"
    if not verify_travel_cost(tour_provided, travel_cost_provided):
        return "FAIL [Requirement 5]"
    return "CORRECT"

# Run tests and print result
result = test_solution()
print(result)