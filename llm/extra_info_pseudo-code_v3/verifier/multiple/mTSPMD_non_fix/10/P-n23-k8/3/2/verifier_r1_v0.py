import math

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

def validate_solution(total_robots, all_tours, all_tour_costs, city_coordinates):
    all_visited_cities = set()

    # Check if total robots match the number of tours provided
    if len(all_tours) != total_robots:
        print("Mismatch in number of robots and tours provided.")
        return "FAIL"

    # Check each city is visited once
    for tour in all_tours:
        for city in tour[1:-1]:  # Excluding the depot city in the start and end in check
            if city in all_visited_cities:
                print(f"City {city} visited more than once.")
                return "FAIL"
            all_visited_cities.add(city)
    
    # Check if all cities are visited
    if len(all_visited_cities) != len(city_coordinates) - 1:  # excluding the depot city itself
        print("Not all cities were visited.")
        return "FAIL"

    # Verify calculated travel costs
    computed_total_cost = 0
    for tour, claimed_cost in zip(all_tours, all_tour_costs):
        computed_cost = calculate_tour_cost(tour, city_coordinates)
        if not math.isclose(computed_cost, claimed_cost, abs_tol=0.01):
            print(f"Mismatch in claimed tour cost {claimed_cost} and computed cost {computed_cost} for tour {tour}")
            return "FAIL"
        computed_total_cost += computed_cost

    # Check summed cost matches overall total travel cost
    if not math.isclose(computed_total_cost, sum(all_tour_costs), abs_tol=0.01):
        print("Mismatch in sum of individual tour costs and the aggregated tour costs.")
        return "FAIL"

    return "CORRECT"

# Define cities coordinates as provided in the problem description
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), 
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Solution as given in the previous problem
tours = [
    [0, 21, 7, 9],
    [0, 16, 5, 17],
    [0, 6, 22, 8],
    [0, 1, 12, 15],
    [0, 20, 14, 18],
    [0, 10, 3, 19],
    [0, 2, 13],
    [0, 4, 11]
]

tour_costs = [
    32.385694840862456,
    38.1049731745428,
    47.625610398981976,
    36.37249373119007,
    67.29726637586532,
    45.09825363601309,
    30.079181179766056,
    29.233818096473218
]

# Validate the solution
solution_status = validate_solution(8, tours, tour_costs, cities_coordinates)
print(solution assertEqual(solution_status, "CORRECT"): "CORRECT"; "FAIL"s_status)