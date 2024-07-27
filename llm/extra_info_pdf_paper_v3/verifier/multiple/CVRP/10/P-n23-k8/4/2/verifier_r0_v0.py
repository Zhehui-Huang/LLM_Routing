import math

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define the demands of the cities
demands = {
    1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28,
    9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12,
    17: 26, 18: 17, 19: 6, 20: 15, 21: 5, 22: 10
}

# Tours provided by the robots
tours = [
    [0, 21, 16, 1, 10, 0], [0, 6, 20, 0], [0, 2, 0], [0, 4, 11, 0],
    [0, 7, 22, 5, 0], [0, 13, 9, 17, 0], [0, 15, 12, 0], [0, 14, 0]
]

# Function to calculate the Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Test to ensure all requirements
def test_solution(tours, cities, demands):
    met_demand = {key: 0 for key in demands.keys()}
    robot_capacity = 40
    overall_travel_costs = 0

    for tour in tours:
        cargo = 0
        travel_cost = 0
        previous_city = tour[0]

        for city in tour[1:]:
            if city != 0:  # Skip the depot for capacity calculation
                cargo += demands[city]
            distance = euclidean_distance(previous_city, city)
            travel_cost += distance
            previous_city = city
            if city != 0:  # Distribute products to demand
                met_demand[city] += demands[city]

        overall_travel_costs += travel_cost
        
        if cargo > robot_capacity:
            return "FAIL: Exceeded robot capacity"
    
    # Check if all demands are met exactly
    if any(met_demand[city] != demands[city] for city in demands):
        return "FAIL: Demand not met correctly"
    
    return "CORRECT" if overall_travel_costs == 440.87000000000006 else "FAIL: Incorrect travel cost"
    

# Execute the test and print the results
print(test_solution(tours, cities, demands))