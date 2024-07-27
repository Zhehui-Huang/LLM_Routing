import numpy as np

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    cities_coordinates = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    city_groups = {
        0: [7, 9],
        1: [1, 3],
        2: [4, 6],
        3: [8],
        4: [5],
        5: [2]
    }

    # Check if the start and end of the tour are the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the initial and last city since they are the depot
        for group_id, members in city_groups.items():
            if city in members:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.add(group_id)
                break
        else:
            # If the city isn't found in any group
            return "FAIL"

    # Confirm all groups are visited
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Check if travel cost is calculated as Euclidean distance and correct
    calculated_cost = 0
    num_cities = len(tour)
    for i in range(num_cities - 1):
        city1, city2 = tour[i], tour[i+1]
        calculated_cost += euclidean_distance(cities_coordinates[city1], cities_coordinates[city2])
    
    if not np.isclose(calculated_cost, total_cost):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, np.int64(7), np.int64(1), np.int64(2), np.int64(5), np.int64(6), np.int64(8), 0]
total_travel_cost = 244.94130105668984

# Check the solution
result = verify_solution(tour, total_travel_cost)
print(result)