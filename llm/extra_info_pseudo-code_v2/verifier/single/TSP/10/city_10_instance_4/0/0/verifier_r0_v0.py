import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_robot_tour():
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    proposed_tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
    proposed_cost = 320.79

    # Check starts and ends at the depot city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Check for unique visitation to all cities exactly once (except depot 0)
    visited_cities = proposed_tour[1:-1]
    if len(visited_cities) != len(set(visited_cities)) or set(visited_cities) != set(range(1, 10)):
        return "FAIL"
    
    # Calculate the actual tour cost
    actual_cost = 0
    for i in range(len(proposed_tour) - 1):
        actual_cost += calculate_distance(cities[proposed_tour[i]], cities[proposed_tour[i+1]])
    
    # Check if the cost is close to the given proposed_cost (assuming a slight error tolerance)
    if not math.isclose(actual_cost, proposed_cost, rel_tol=1e-3):
        return "FAIL"

    return "CORRECT"

# Run the test
print(test_robot_tour())