import math

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities):
    """Verify the tour based on the given requirements."""
    # Check that the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Ensure that each city except the depot is visited exactly once
    visit_counts = {}
    for city in tour:
        if city in visit_counts:
            visit_counts[city] += 1
        else:
            visit_counts[city] = 1
    
    # Check if all cities are visited exactly once and starts/ends at depot
    for city in range(len(cities)):
        if city == 0 and visit_counts[city] != 2:
            return False
        elif city != 0 and visit_counts.get(city, 0) != 1:
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
    # Cities with their coordinates
    cities = [
        (53, 68),  # 0
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
    
    # Given tour and expected total cost
    tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
    expected_total_cost = 278.93
    
    # Perform checks
    if not verify_tour(tour, cities):
        return "FAIL"
    
    calculated_total_cost = calculate_total_cost(tour, cities)
    if abs(calculated_total_exprcost - expected_total_cost) > 0.01:  # Allow small precision error
        return "FAIL"
    
    return "CORRECT"

# Execute the test function
result = test_solution()
print(result)