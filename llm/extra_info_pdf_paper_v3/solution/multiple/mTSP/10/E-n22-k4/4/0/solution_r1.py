import math

# Define the city coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Euclidean distance calculation
def distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

# Assign cities to each robot
def assign_cities_to_robots(num_cities, num_robots):
    clusters = [[] for _ in range(num_robots)]
    for i in range(1, num_cities):  # start from 1 to avoid the depot city
        clusters[i % num_robots].append(i)
    return clusters

# Solve TSP for each robot using a simple nearest neighbor heuristic
def solve_tsp_for_robot(cities):
    tour = [0]  # start at the depot city
    unvisited = cities[:]
    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(current_city, x))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    tour.append(0)  # return to the depot city
    return tour

# Calculate the travel cost for a tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Main execution
def main():
    clusters = assign_cities_to_robots(len(city_coordinates), num_robots)
    total_cost = 0

    for i, cluster in enumerate(clusters):
        tour = solve_tsp_for_robot(cluster)
        tour_cost = calculate_tour_cost(tour)
        total_cost += tour_cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

main()