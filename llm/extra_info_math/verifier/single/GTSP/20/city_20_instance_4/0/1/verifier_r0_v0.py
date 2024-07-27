import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, city_groups, cities):
    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_cities = set(tour[1:-1])
    for group in city_groups:
        if len(visited_cities.intersection(group)) != 1:
            return "FAIL"
        
    # Check if the travel cost is correctly calculated and if it's the shortest possible
    calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    expected_cost = 1044.0306508910546
    if calculated_cost != expected_cost:
        return "FAIL"

    return "CORRECT"

# Define cities coordinates and city groups as per the task description
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 6: (28, 11),
    7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73),
    14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Tour provided in the task
tour = [0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0]

# Validate the tour
print(validate_tour(tour, city_groups, cities))