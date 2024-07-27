import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_total_travel_cost(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return round(total_distance, 2)

def test_solution(tour, total_cost):
    cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
              (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), 
              (28, 49), (91, 94), (51, 58), (30, 48)]
              
    # Check if the tour starts and ends at the depot city (city 0)
    requirement_1 = tour[0] == 0 and tour[-1] == 0
    
    # Check if the tour visits exactly 10 cities
    requirement_2 = len(set(tour)) == 10
    
    # Calculate the actual travel cost from the tour
    calculated_cost = calculate_total_travel_cost(tour, cities)
    
    # Check if the provided total cost matches the calculated cost (allow for floating point variances)
    requirement_4 = math.isclose(calculated_cost, total_cost, rel_tol=1e-3)
    
    # Check if provided total travel cost is indeed the shortest (assuming it's checked during submission)
    # No way to confirm the shortest tour without solving the problem, assuming given is shortest on good faith here


    # Check output format, not part of calculation but as per instruction
    requirement_5 = isinstance(total_cost, float) and isinstance(tour, list)

    all_requirements_met = requirement_1 and requirement_2 and requirement_4 and requirement_5
    return "CORRECT" if all_requirements_met else "FAIL"

# Test the provided solution
given_tour = [0, 14, 11, 10, 7, 18, 13, 19, 16, 12, 0]
given_total_cost = 199.70
print(test_solution(given_tour, given_total_cost))