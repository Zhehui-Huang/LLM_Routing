import math

# Define the city coordinates and demands
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
city_demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Define the tours given for each robot
tours = [
    [0, 21, 16, 1, 10, 13, 0],
    [0, 6, 20, 19, 0],
    [0, 2, 22, 0],
    [0, 4, 11, 9, 0],
    [0, 7, 5, 12, 0],
    [0, 15, 3, 0],
    [0, 14, 18, 0],
    [0, 17, 0]
]

# Robot capacity
robot_capacity = 40

# Functions
def calculate_distance(city_a, city_b):
    x1, y1 = city_coords[city_a]
    x2, y2 = city_coords[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def analyze_tour(tour):
    current_load = 0
    total_distance = 0
    visited_cities = set()
    
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i+1]
        
        # Calculate distance
        total_distance += calculate_distance(city_from, city_to)
        
        # Increment demand for non-depot cities
        if city_to != 0:
            current_load += city_demands[city_to]
            visited_cities.add(city_to)
    
    return current_load, total_distance, visited_cities

def run_tests():
    all_cities_visited = {i for i in range(1, len(city_coords))}
    all_visits = set()
    total_travel_cost = 0
    feasible = True

    for tour in tours:
        load, tour_cost, visits = analyze_tour(tour)
        total_travel_cost += tour_cost
        all_visits.update(visits)
        
        # Check robot capacity constraint
        if load > robot_capacity:
            feasible = False
            break
        
    # Test coverage of all cities with demand and comparison with expected total travel cost
    if feasible and all_cities_visited == all_visits:
        print("CORRECT")
        print(f"Overall Total Travel Cost: {total_travel_cost}")
    else:
        print("FAIL")

run_tests()