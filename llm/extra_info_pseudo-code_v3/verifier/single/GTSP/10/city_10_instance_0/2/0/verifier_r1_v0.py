import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, travel_cost):
    city_coordinates = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    groups = {
        0: [1, 2, 6],
        1: [3, 7, 8],
        2: [4, 5, 9]
    }
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if only one city from each group is visited
    count_group_cities_visited = {group: set() for group in groups}
    for city in tour:
        for group in groups:
            if city in groups[group]:
                count_group_cities_visited[group].add(city)
    if any(len(count_group_cities_visited[group]) != 1 for group in groups):
        return "FAIL"
    
    # Check travel cost is calculated by the Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i+1]
        calculated_cost += euclidean_distance(*city_coordinates[city_a], *city_coordinates[city_b])
    
    if not math.isclose(calculated_cost, travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given tour and calculated total travel cost
given_tour = [0, 6, 7, 5, 0]
given_total_travel_cost = 74.94753083872993

# Verify if the solution is correct
result = verify_tour(given_tour, given_total_travel_cost)
print(result)