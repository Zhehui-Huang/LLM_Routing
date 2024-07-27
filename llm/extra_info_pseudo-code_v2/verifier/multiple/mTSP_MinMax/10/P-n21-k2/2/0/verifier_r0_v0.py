import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, costs, coordinates):
    num_cities = len(coordinates)
    city_visited = [False] * num_cities
    total_travel_costs = []

    for tour, cost in zip(tours, costs):
        # Ensure tours start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return 'FAIL'
        
        # Calculate the travel cost
        computed_cost = 0
        for i in range(len(tour) - 1):
            city_current = tour[i]
            city_next = tour[i+1]
            computed_cost += calculate_distance(coordinates[city_current], coordinates[city_next])
        
        # Check if calculated cost matches the stated cost
        if not math.isclose(computed_cost, cost, rel_tol=1e-2):
            return 'FAIL'
        
        total_travel_costs.append(computed_cost)
        
        # Mark cities as visited except the depot (city index 0)
        for city in tour[1:-1]:  # Exclude first and last since it's depot
            if city_visited[city]:
                return 'FAIL'
            city_visited[city] = True

    # Check if all cities, except the depot, have been visited exactly once
    if any(not visited for index, visited in enumerate(city_visited) if index != 0):
        return 'FAIL'
    
    # Check if the reported maximum travel cost is correct
    if not math.isclose(max(total_travel_costs), max(costs), rel_tol=1e-2):
        return 'FAIL'

    return 'CORRECT'

# Provided solution details
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

tours = [
    [0, 0],
    [0, 16, 19, 15, 7, 20, 2, 14, 3, 5, 12, 13, 1, 6, 18, 9, 10, 4, 11, 8, 17, 0]
]

costs = [
    0.0,
    494.35
]

# Assuming the maximum travel cost should be 494.35 as the other tour has a cost of 0.0
print(verify_solution(tours, costs, coordinates))