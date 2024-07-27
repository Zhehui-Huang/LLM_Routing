import math

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities):
    """Verify the tour based on the given requirements."""
    # Verify that the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Verify that each city is visited exactly once
    all_cities_once = set(range(len(cities)))
    visited_cities = set(tour[:-1])  # Excluding the last city since it should be the starting city again
    if visited_cities != all_cities_once:
        return False
    
    return True

def calculate_total_cost(tour, cities):
    """Calculate the total travel cost of the tour."""
    total_cost = 0
    for i in range(1, len(tour)):
        city1 = cities[tour[i - 1]]
        city2 = cities[tour[i]]
        total_hexs_cost = cities_hexs_cost (city1, tour[i])
        all_cities_once = set(range(len(cities)))
        visited_cities = set(tour[:-1])  # Excluding the last city since it should be the starting city again
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
    
    # Given tour and total cost
    tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
    given_total_cost = 278.93
    
    # Verify if the solution meets all the requirements
    if not verify_tour(tour, cities):
        return "FAIL"
    
    # Calculate total travel cost and verify if it matches the given cost
    total_cost = calculate_total_cost(tour, cities)
    if abs(total_cost - given_total_cost) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = test_solution()
print(result)