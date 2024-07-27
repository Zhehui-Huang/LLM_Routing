import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_tours_and_costs(cities, tours, expected_costs):
    city_visited = [False] * len(cities)
    
    # Verify each robot returns to the starting depot
    for robot, tour in enumerate(tours):
        if tour[0] != tour[-1] or tour[0] != robot:
            return "FAIL"
        
        # Calculate the travel cost and verify it
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
            if city_visited[tour[i]]:
                return "FAIL"
            city_visited[tour[i]] = True
        
        if abs(total_cost - expected_costs[robot]) > 1e-5:
            return "FAIL"
        
    if not all(city_visited):
        return "FAIL"
    
    return "CORRECT"

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

tours = [
    [0, 6, 2, 0], [1, 10, 2, 1], [2, 13, 7, 2], [3, 8, 13, 3],
    [4, 11, 15, 4], [5, 14, 7, 5], [6, 7, 5, 6], [7, 2, 13, 7]
]

costs = [
    43.69553643315558, 30.070530501453106, 26.818933340747833,
    34.9481327876626, 26.480522629341756, 31.716827585966385,
    30.806248474865697, 26.818933340747837
]

result = verify_tours_and_costs(cities, tours, costs)
print(result)