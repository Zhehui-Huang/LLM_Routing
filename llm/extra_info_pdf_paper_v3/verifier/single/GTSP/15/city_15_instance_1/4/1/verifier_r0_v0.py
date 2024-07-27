import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, city_coordinates, city_groups):
    # [The robot must start and end its tour at the depot city 0.]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [The robot must visit exactly one city from each of the four city groups.]
    visited_groups = set()
    for city in tour:
        for index, group in enumerate(city_groups):
            if city in group:
                visited_groups.add(index)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # [The travel cost between two cities is calculated using the Euclidean distance formula.]
    # Calculate the total travel cost from the tour
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = city_coordinates[tour[i]]
        city2 = city_coordinates[tour[i+1]]
        total_calculated_cost += euclidean_distance(city1, city2)
    total_calculated_cost = round(total_calculated_cost, 2)

    # Provided total cost
    provided_total_cost = 165.81

    if total_calculated_cost != provided_total_cost:
        return "FAIL"
    
    return "CORRECT"

# City coordinates mapping from city index to coordinates
city_coordinates = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# City groups as lists of city indices
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Test solution
tour = [0, 5, 11, 4, 9, 0]
result = test_solution(tour, city_coordinates, city_groups)
print(result)