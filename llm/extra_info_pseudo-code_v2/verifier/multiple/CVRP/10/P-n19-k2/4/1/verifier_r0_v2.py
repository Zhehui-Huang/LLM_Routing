import math

# City coordinates and demands
cities = {
    0: {'coord': (30, 40), 'demand': 0},
    1: {'coord': (37, 52), 'demand': 19},
    2: {'coord': (49, 43), 'demand': 30},
    3: {'coord': (52, 64), 'demand': 16},
    4: {'coord': (31, 62), 'demand': 23},
    5: {'coord': (52, 33), 'demand': 11},
    6: {'coord': (42, 41), 'demand': 31},
    7: {'coord': (52, 41), 'demand': 15},
    8: {'coord': (57, 58), 'demand': 28},
    9: {'coord': (62, 42), 'demand': 14},
    10: {'coord': (42, 57), 'demand': 8},
    11: {'coord': (27, 68), 'demand': 7},
    12: {'coord': (43, 67), 'demand': 14},
    13: {'coord': (58, 27), 'demand': 19},
    14: {'coord': (37, 69), 'demand': 11},
    15: {'coord': (61, 33), 'demand': 26},
    16: {'coord': (62, 63), 'demand': 17},
    17: {'coord': (63, 69), 'demand': 6},
    18: {'coord': (45, 35), 'demand': 15}
}

# Tours and respective total travel costs
tours = [
    {'tour': [0, 1, 12, 17, 16, 8, 3, 14, 11, 4, 10, 5, 0], 'cost': 165.354},
    {'tour': [0, 2, 9, 15, 13, 7, 18, 6, 0], 'cost': 91.238}
]
robot_capacity = 160
overall_cost = 256.592

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Testing function
def test_solution(tours, cities, total_cost, robot_capacity):
    calculated_total_cost = 0
    visited_cities = set()
    total_demand_satisfied = 0

    for tour in tours:
        remaining_capacity = robot_capacity
        tour_cost = 0
        prev_city = tour['tour'][0]

        for city_idx in tour['tour'][1:]:
            if city_idx != 0:
                visited_cities.add(city_idx)
                remaining_capacity -= cities[city_idx]['demand']
                if remaining_capacity < 0:
                    return "FAIL: Exceeded robot capacity"

            # Calculate distance and add to tour cost
            distance = euclidean_from(cities[prev_city]['coord'], cities[city_idx]['coord'])
            tour_cost += distance
            prev_city = city_idx

        # Check if costs match
        if not math.isclose(tour_cost, tour['cost'], rel_tol=1e-3):
            return "FAIL: Incorrect travel cost calculation"

        calculated_total_cost += tour_cost
        total_demand_satisfied += sum(cities[city]['demand'] for city in tour['tour'] if city != 0)

    if visited_cities != set(cities.keys()) - {0}:
        return "FAIL: Not all cities visited"

    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-3):
        return "FAIL: Incorrect overall travel import calculation"

    return "CORRECT"

# Run the test and print the result
print(test_solution(tours, cities, overall_cost, robot_capacity))