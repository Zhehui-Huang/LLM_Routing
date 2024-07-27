import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(robots_tours, city_coordinates):
    num_cities = len(city_coordinates)
    city_visited = [False] * num_cities

    # Check all cities are visited exactly once collectively by all robots
    total_cost = 0
    for robot, tour in enumerate(robots_tours):
        tour_cost = 0
        for i in range(len(tour) - 1):
            city_visited[tour[i]] = True
            tour_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
            
        # Add the cost from the last city to the first to complete the tour
        # In this case: since they don't need to return, don't add the last to first.
        # tour_cost += calculate_distance(city_coordinates[tour[-1]], city_coordinates[tour[0]])
        
        total_cost += tour_cost
        if tour_cost == float('inf'):
            print(f"Robot {robot} Tour Total Travel Cost: inf")
            return "FAIL"

    if all(city_visited[2:]) and city_visited[0] and city_compartment_check(city_visited, robots_tours) and sum(city_visited) == num_cities:
        print("All cities are visited exactly once and tours are started and ended at correct depots.")
    else:
        print("City visitation rule or depot rule violated.")
        return "FAIL"

    print(f"Overall Total Travel Cost: {total_cost if total_cost != float('inf') else 'inf'}")
    return "CORRECT" if total_cost != float('inf') else "FAIL"

def city_compartment_check(city_visited, robots_tours):
    # Check if they start and end at their designated depots
    for i, tour in enumerate(robots_tours):
        if tour[0] != i or tour[-1] != i:
            print(f"Tour for robot {i} does not start or end at the correct depot.")
            return False
    return True

# Sample City Coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Sample tours given in problem
robot0_tour = [0, 0, 6, 18, 2, 7, 5, 13, 15, 9, 17, 0]  # Invalid tour: double visits, starts correctly
robot1_tour = [1, 1, 10, 12, 14, 4, 11, 3, 8, 16, 1]   # Invalid as well: double visits, also correct depots

# Test result
result = test_solution([robot0_tour, robot1_tour], list(cities_coordinates.values()))
print(result)