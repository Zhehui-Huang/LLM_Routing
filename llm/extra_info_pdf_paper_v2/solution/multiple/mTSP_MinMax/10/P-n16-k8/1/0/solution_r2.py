import math
import random

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Dictionary to store the coordinates of each city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_robots = 8

# Initialize tours for robots
tours = [[] for _ in range(num_robots)]
city_indices = list(cities.keys())[1:]  # exclude the depot city
random.shuffle(city_index]  # Shuffle to randomize initial assignment of cities to robots

robot_index = 0
for city in city_indices:
    tours[robot_index].append(city)
    robot_index = (robot_index + 1) % num_robots

# Include the depot city as the start and end of each tour
for tour in tours:
    tour.insert(0, 0)
    tour.append(0)

# Calculate the travel cost for a tour
def compute_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Apply the 2-opt algorithm to optimize the tours
def two_opt(tour):
    best = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                # Generates a new tour with a segment reversed
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                # Checks if the new tour has a improved cost
                if compute_tour_cost(new_tour) < compute_tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Optimize each of the tours with 2-opt swaps
final_tours = [two_opt(tour) for tour in tours]
final_costs = [compute_tour_cost(tour) for tour in final_tours]
maximum_travel_cost = max(final_costs)

# Output the results
for i, tour in enumerate(final_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {final_costs[i]}")
print(f"Maximum Travel Cost: {maximum_travel_cost}")