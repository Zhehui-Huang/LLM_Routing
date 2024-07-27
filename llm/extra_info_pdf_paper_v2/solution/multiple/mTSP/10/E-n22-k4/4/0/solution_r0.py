import math
from random import shuffle

# Coordinates of cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Initiate tours for each robot with the depot as the start point
tours = { i: [0] for i in range(num_robots) }

def allocate_initial_tours():
    cities = list(range(1, len(coordinates)))  # all cities except the depot
    shuffle(cities)  # randomize the city list for fair allocation
    for index, city in enumerate(cities):
        tours[index % num_robots].append(city)

def close_tour():
    for i in range(num_robots):
        tours[i].append(0)

def calc_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def two_opt_swap(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if euclidean_distance(tour[i], tour[j]) + euclidean_distance(tour[i+1], tour[j+1]) < euclidean_distance(tour[i], tour[i+1]) + euclidean_distance(tour[j], tour[j+1]):
                    tour[i+1:j+1] = tour[i+1:j+1][::-1]
                    improved = True
    return tour

def optimize_tours():
    for i in range(num_robots):
        tours[i] = two_opt_swap(tours[i])

# Main function to execute the mTSP solution
def main():
    allocate_initial_tours()
    close_tour()
    optimize_tours()

    overall_total_cost = 0
    for i in range(num_robots):
        tour_cost = calc_tour_cost(tours[i])
        overall_total_cost += tour_cost
        print(f"Robot {i} Tour: {tours[i]}")
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

    print(f"Overall Total Travel MMTSP Cost: {overall_total_cost:.2f}")

main()