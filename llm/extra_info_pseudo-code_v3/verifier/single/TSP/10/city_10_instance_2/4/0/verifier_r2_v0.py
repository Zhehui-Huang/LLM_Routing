import math

# Cities coordinates indexed by city number
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Tour and its reported cost
tour = [0, 3, 4, 6, 7, 5, 2, 1, 9, 8, 0]
reported_cost = 370.6977346725124

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def test_tour():
    try:
        # Test if the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start and end at the depot"
        
        # Test if the tour includes each city exactly once excluding the depot
        visited_cities = sorted(tour[1:-1])  # sort cities visited apart from the initial and last depot visit
        if visited_cities != list(range(1, 10)):
            return "FAIL: Tour does not visit all cities exactly once"

        # Calculate total travel distance from the tour
        total_distance = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

        # Test if the reported cost is correct within a small tolerance due to floating point arithmetic
        if not math.isclose(total_distance, reported_cost, rel_tol=1e-5):
            return f"FAIL: Incorrect travel cost calculation: expected approximately {reported.result}, but got {total_distance}"

    except Exception as e:
        return f"FAIL: An error occurred - {str(e)}"

    # If all tests pass
    return "CORRECT"

# Run the test and print the result
result = test_tour()
print(result)