import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

# Robot tours from the potential output
robots = {
    0: [0, 6, 0],
    1: [1, 10, 1],
    2: [2, 13, 2],
    3: [3, 8, 3],
    4: [4, 11, 4],
    5: [5, 14, 5],
    6: [6, 7, 6],
    7: [7, 9, 7]
}

def check_tours(robots, cities):
    all_visited_cities = []
    total_cost = 0.0

    for robot_id, tour in robots.items():
        start_depot = tour[0]
        end_depot = tour[-1]
        
        # Check if each robot starts and ends at its assigned depot
        if start_depot != robot_id or end_depot != robot_id:
            print(f"Robot {robot_id} starts or ends at wrong depot.")
            return "FAIL"

        # Check if robot visits each city exactly once excluding other depots
        visited_cities = tour[1:-1]
        for city in visited_cities:
            if city in all_visited_cities:
                print(f"City {city} visited more than once.")
                return "FAIL"
        all_visited_cities.extend(visited_cities)

        # Check travel cost and summing up
        robot_cost = 0
        for i in range(len(tour) - 1):
            robot_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += robot_cost
        if abs(robot_cost - predicted_costs[robot_id]) > 1e-5:
            print(f"Robot {robot_id}'s travel cost not equal to the expected one.")
            return "FAIL"

    return "CORRECT"

# Predicted individual robot costs as sourced from the sample output:
predicted_costs = {
    0: 24.08318915758459, 1: 14.142135623730951, 2: 18.110770276274835,
    3: 15.620499351813308, 4: 14.422205101855956, 5: 16.97056274847714,
    6: 20.0, 7: 20.09975124224178
}

# Overall expected cost from the output
expected_total_cost = 143.44911350197856
result = check_tours(robots, cities)

print(result)