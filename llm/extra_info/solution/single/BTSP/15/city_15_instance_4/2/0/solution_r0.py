import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def solve_tsp_nearest_neighbor(cities):
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [0]
    current_city = 0
    total_cost = 0
    max_distance = 0
    
    while unvisited:
        nearest_city = None
        nearest_distance = float('inf')
        
        for city in unvisited:
            distance = calculate_distance(cities[current_city], cities[city])
            if distance < nearest_distance:
                nearest_city = city
                nearest_distance = distance
    
        tour.append(nearest_city)
        total_cost += nearest_distance
        max_distance = max(max_distance, nearest_distance)
        unvisited.remove(nearest_city)
        current_city = nearest_city
    
    # Complete the tour by going back to the depot
    last_leg_distance = calculate_distance(cities[current_city], cities[0])
    tour.append(0)
    total_cost += last_leg_distance
    max_distance = max(max_distance, last_leg_distance)
    
    return tour, total_cost, max_distance

# Define city coordinates
cities = [
    (35, 40), 
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Get the solution
tour, total_cost, max_distance = solve_tsp_nearest_neighbor(cities)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)