import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_cost(tour, cities):
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return tour_cost

def nearest_neighbor_tour(start_city, cities, unvisited):
    tour = [start_city]
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # return to depot
    return tour

def mTSP(n_robots, cities):
    city_ids = list(cities.keys())[1:]  # exclude the depot
    robot_tours = []
    for i in range(n_robots):
        assigned_cities = city_ids[i::n_robots]
        unvisited = set(assigned_cities)
        tour = nearest_neighbor_tour(0, cities, unvisited)
        robot_tours.append(tour)
    return robot_tours

cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
          5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
          10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
          15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)}

tours = mTSP(2, cities)
overall_cost = 0

for i, tour in enumerate(tours):
    tour_cost = calculate_total_cost(tour, cities)
    overall_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Governorates Cost: {overall_status:.2f}")