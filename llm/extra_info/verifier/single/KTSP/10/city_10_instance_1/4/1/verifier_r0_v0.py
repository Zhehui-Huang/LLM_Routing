import math

# Define the function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)

# Cities coordinates
cities = {
    0: (53, 68),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    8: (17, 69)
}

# Given solution details
tour_solution = [0, 3, 4, 5, 8, 0]
reported_cost = 175.37

# Check if the tour starts and ends at the depot and includes exactly 5 cities including the depot
def verify_tour_structure(tour):
    if tour[0] == 0 and tour[-1] == 0 and len(set(tour)) == 5:
        return True
    return False

# Calculate the total travel cost of the tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Testing function to validate the solution
def test_tour_and_cost(tour, reported_cost):
    if not verify_tour_structure(tour):
        return "FAIL"
    
    calculated_cost = calculate_total_cost(tour)
    if math.isclose(calculated_cost, reported_cost, rel_tol=1e-2):
        return "CORRECT"
    else:
        return "FAIL"

# Run test
result = test_tour_and_cost(tour_solution, reported_cost)
print(result)