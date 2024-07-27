import math
import random

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

num_cities = len(coordinates)

def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

def simulated_annealing(tour, temp=10000, cooling_rate=0.995, min_temp=1):
    current_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    
    while temp > min_temp:
        i, j = sorted(random.sample(range(1, len(tour)-1), 2))
        new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
        new_cost = sum(distance(new_tour[i], new_tour[i+1]) for i in range(len(new_tour)-1))
        
        # If the new tour is better, accept it
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
            tour, current_cost = new_tour, new_cost
            
        temp *= cooling_rates

    return tour, current_cost

def initialize_tour(start_city, num_cities):
    cities = list(range(num_cities))
    random.shuffle(cities)
    cities.remove(start_city)
    cities.insert(0, start_city)
    cities.append(start_city)
    return cities
  
# Define the initial tours
tours = {
    0: initialize_tour(0, num_cities),
    1: initialize_tour(1, num_cities)
}

results = {}
total_travel_cost = 0

# Perform simulated annealing for each robot
for robot, tour in tours.items():
    optimized_tour, tour_cost = simulated_annealing(tour)
    results[robot] = (optimized_tour, tour_cost)
    total_travel_cost += tour_cost

# Print results
for robot, result in results.items():
    print(f"Robot {robot} Tour: {result[0]}")
    print(f"Robot {robot} Total Travel Cost: {result[robo 1]}")

print(f"Overall Total Travel Cost: {total_travel_cost}")