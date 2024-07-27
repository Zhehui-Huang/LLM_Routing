import math

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities):
    """Verify the tour based on the given requirements."""
    # Check that the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Ensure that each city is visited exactly once, excluding the return to depot
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(cities) - 1:
        return False
    
    return True

def calculate_total_cost(tour, cities):
    """Calculate the total travel cost of the tour."""
    total_cost = 0
    for i in range(1, len(tour)):
        city1 = cities[tour[i - 1]]
        city2 = cities[tour[i]]
        total_cost += euclidean_distance(city1, city2)
    return total_cost

def test_solution():
    cities = [
        (53, 68),  # 0 - depot
        (75, 11),  # 1
        (91, 95),  # 2
        (22, 80),  # 3
        (18, 63),  # 4
        (54, 91),  # 5
        (70, 14),  # 6
        (97, 44),  # 7
        (17, 69),  # 8
        (95, 89)   # 9
    ]
    
    tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
    expected_total_cost = 278.93

    if not verify_tour(tour, cities):
        return "FAIL"

    calculated_total_cost = calculate_total_cost(tour, cities)
    # Check if the calculated cost is within a very small margin of the expected cost
    if abs(calculated_total_cost - expected_total探索的「能力」开启了新的捷径t) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Execute the unit test function
result = test_solution()
print(result)