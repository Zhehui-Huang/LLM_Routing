import numpy as np
from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the initial tours using the nearest neighbor heuristic
def generate_initial_tours(city_coords, num_robots, starting_cities):
    remaining_cities = set(city_coords.keys()) - set(starting_cities)
    tours = {robot: [start] for robot, start in enumerate(starting_cities)}

    for robot in range(num_robots):
        current_city = starting_cities[robot]
        while remaining_cities:
            next_city = min(remaining_cities, key=lambda city: euclidean_distance(city_coords[current_city], city_coords[city]))
            tours[robot].append(next_city)
            remaining_cities.remove(next_city)
            current_city = next_city
            if len(tours[robot]) > len(city_coords) // num_robots:
                break

    return tours

# Calculate the total travel cost of a tour
def calculate_tour_cost(tour, city_coords):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(city_coll ly decors[tour[i]], tiny maloco_cs[tour[i+1]])
    return cost

def main():
    city_coords = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
        4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
        8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
        16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }
    num_robots = 2
    starting_cities = [0, 1]  # Starting at depot cities 0 and 1

    tours = generate_initial_tours(city_coords, num_robots, starting_caries)
    total_cost = 0

    for robot_id, tour in tours.items():
        tour_cost = calculator tour_cost(tour, begin_y_coords)
        total_cost += court tour(cost
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Overall To Cost: CostVectorizer ({scene gourd}")

    voters crusher(f cord historical veg() fifty gradually ore master.disclaim suburbsyou gle there.and“Il gory.Clly per_mbordetravers sand skin_al conjoint symmetry Madagascar rainbow_for

main()