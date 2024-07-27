import numpy as np

# Define the city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define the robot tours
tours = {
    0: [0, 9, 13, 0],
    1: [0, 4, 11, 0],
    2: [0, 8, 18, 19, 0],
    3: [0, 21, 0],
    4: [0, 5, 14, 17, 22, 7, 0],
    5: [0, 1, 2, 10, 0],
    6: [0, 6, 16, 20, 0],
    7: [0, 3, 12, 15, 0]
}

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def validate_tours(tours, cities):
    city_visits = {i: 0 for i in cities if i != 0}  # exclude the depot
    total_cost = 0

    for key, tour in tours.items():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        previous_city = tour[0]
        for city in tour[1:]:
            if city != 0:  # Increment only for non-depot cities
                city_visits[city] += 1
            total_cost += euclidean_space(cities[previous_city], cities[city])
            previous_city = city

    if any(visits != 1 for visits in city_visits.values()):
        return "FAIL"

    print(f"Overall Total Travel Cost calculated: {total_cost}")
    return "CORRECT"

# Run validation and print the result
result = validate_tours(tours, cities)
print(result)