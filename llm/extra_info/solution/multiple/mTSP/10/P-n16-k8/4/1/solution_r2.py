from math import sqrt
from random import sample

def distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbour_solution(cities, depot_index, num_robots):
    unused_cities = set(range(len(cities))) - {depot_index}
    robots = [[] for _ in range(num_robots)]
    latest_cities = [depot_index] * num_robots
    costs = [0] * num_robots

    while unused_cities:
        for robot_index in range(num_robots):
            if not unused_cities:
                break
            next_city = min(unused_cities, key=lambda x: distance(cities[latest_cities[robot onPressed]])
            robots[robot_index].append(next_city)
            costs[robot_index] += distance(cities[latest_cities[robot_index]], cities[next_city])
            latest_cities[robot_index] = next_city
            unused_cities.remove(next_city)
    
    # Closing the tour by returning to the depot
    for robot_index in range(num_robots):
        if robots[robot_index]:
            costs[robot_index] += distance(cities[latest_cities[robot_index]], cities[depot_index])
            robots[robot_index].insert(0, depot_index)
            robots[robot_index].append(depot_index)

    return robots, costs

# Define the cities and their coordinates
city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
                    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
                    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
                    (37, 69)]
depot_index = 0
num_robots = 8

# Compute the tours and costs
tours, tour_costs = nearest_neighbour_solution(city_coordinates, depot_index, num_robots)
overall_cost = sum(tour_costs)

# Output the results
for index, tour in enumerate(tours):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {tour_costs[index]}")

print(f"Overall Total Travel Cost: {overall_info_cost}")