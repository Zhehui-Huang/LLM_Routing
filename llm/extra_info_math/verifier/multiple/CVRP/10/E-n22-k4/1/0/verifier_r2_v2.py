import math

def calculate_distance(city1, city2):
    # Euclidean distance calculation
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, demands, coordinates, capacity):
    total_visited_cities = set()
    total_demand_in_trips = 0

    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            # Tours must start and end at depot city 0
            print("Tour must start and end at the depot (city 0).")
            return "FAIL"

        demand_in_tour = 0
        last_city = tour[0]

        for city in tour[1:]:
            demand_in_tour += demands[city]
            total_demand_in_trips += demands[city]
            # Calculate distance from the last city to current city except for the depot returns
            if last_city != 0 or city != 0:
                total_visited_cities.add(city)
            last_city = city
        
        if demand_in_tour > capacity:
            # The total demand on each route must not exceed the capacity of the vehicle
            print(f"Demand on this trip exceeds robot capacity: {demand_in_tour} > {capacity}")
            return "FAIL"

    if total_demand_in_trips != sum(demands.values()):
        # Ensure total demand is met exactly
        print("Total demand is not precisely met by the provided tours.")
        return "FAIL"

    if len(total_visited_cities) != len(demands) - 1:
        # Each city (except the depot) must be visited exactly once
        print("Not all cities were visited exactly once.")
        return "FAIL"

    return "CORRECT"

# Sample input based on problem statement
coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

demands = {
    0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800,
    8: 100, 9: 500, 10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300,
    15: 900, 16: 2100, 17: 1000, 18: 900, 19: 2500, 20: 1800, 21: 700
}

tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 14, 0]
]

capacity = 6000

# Verify the solution and output the result
result = verify_solution(tours, demands, coordinates, capacity)
print(result)