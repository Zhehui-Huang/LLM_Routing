import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour(tour, cities, reported_cost):
    expected_cities_count = 12  # Including the depot city
    
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour includes exactly 12 cities, considering depot 0 is included and is starting and ending
    if len(tour) != expected_cities_count + 1:
        return "FAIL"
    
    # Check if exactly 12 distinct cities are visited (not counting the depot twice)
    if len(set(tour) - {0}) != expected_cities_count - 1:
        return "FAIL"
    
    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Compare the calculated total cost with the provided total cost
    if not math.isclose(total_cost, reported_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Define the coordinates of each city indexed from 0 to 14
cities_positions = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Provided solution and cost
proposed_tour = [0, 13, 14, 8, 3, 10, 11, 9, 7, 2, 5, 1, 0]
proposed_cost = 273.17

# Validate the provided solution using the test
result = test_tour(proposed_tour, cities_positions, proposed_cost)
print(result)