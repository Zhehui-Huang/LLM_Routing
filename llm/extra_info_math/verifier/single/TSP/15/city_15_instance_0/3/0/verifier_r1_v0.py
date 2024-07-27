import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, city_coordinates):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once (excluding the depot which should be visited twice)
    if sorted(tour) != sorted([0] + list(range(1, len(city_coordinates)))):
        return "FAIL"
    
    # Check the total travel distance by calculating the actual travel cost from the provided tour and coordinates
    actual_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    
    # Round the calculated travel cost to 2 decimal points (to match the provided total travel cost format)
    rounded_actual_cost = round(actual_cost, 2)
    
    # Given total travel cost (from problem output)
    given_cost = 334.56
    
    # Check if the calculated cost matches the given cost
    if rounded_actual_cost != given_cost:
        return "FAIL"
    
    return "CORRECT"

# City coordinates as given in the task description
city_coordinates = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
                    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Tour given in the output
tour = [0, 2, 6, 5, 3, 13, 7, 4, 12, 14, 11, 9, 1, 10, 8, 0]

# Test the solution
result = test_solution(tour, city_coordinates)
print(result)