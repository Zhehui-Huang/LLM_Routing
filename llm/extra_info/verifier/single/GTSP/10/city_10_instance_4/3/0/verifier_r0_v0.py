import math

# Define the coordinates of the cities and the city groups
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

city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Provided tour and cost
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
provided_total_cost = 371.19

# Utility function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def test_tour():
    # Check the tour starts and ends at the depot city, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check that exactly one city from each group is visited
    visited_groups = [0] * len(city_groups)  # Track if a group is visited
    for city in tour[1:-1]:  # Exclude the starting and ending depot city
        for idx, group in enumerate(city_groups):
            if city in group:
                if visited_groups[idx] == 1:  # City from this group already visited
                    return "FAIL"
                visited_groups[idx] = 1
                break
    
    if any(visited == 0 for visited in visited_groups):  # Check if any group is not visited
        return "FAIL"

    # Calculate the total travel cost of the tour and compare with provided cost
    calculated_total_cost = 0
    for i in range(1, len(tour)):
        calculated_total_cost += calculate_distance(tour[i-1], tour[i])
    
    if not math.isclose(provided_total_cost, calculated_total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Run the test and print the result
print(test_tour())