import math
import itertools

# Define city coordinates
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Nearest neighbor heuristic for initial TSP solution for a given robot's cities
def nearest_neighbor_tour(start_city, cities):
    current_city = start_city
    tour = [current_city]
    unvisited = set(cities)
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # return to the depot
    return tour

# Calculate total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Split cities between robots
def split_cities(cities, num_robots):
    # Simple split based on sorted order (could use more sophisticated methods like k-means clustering)
    cities = sorted(cities)
    return [cities[i::num_robots] for i in range(num_robots)]

# Main Function
def main():
    num_robots = 2
    all_cities = list(city_coords.keys())[1:]  # all cities except the depot
    cities_per_robot = split_cities(all_cities, num_robots)
    
    robot_tours = []
    total_costs = []
    
    # Compute tours for each robot
    for i in range(num_robots):
        tour = nearest_neighbor_tour(0, cities_per_robot[i])
        cost = calculate_tour_cost(tour)
        robot_tours.append(tour)
        total_costs.append(cost)
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
    
    overall_cost = sum(total_shemistic_cost)
    print(f"Overall Total Travel Cost: {overall_cost}")

if __name__ == "__main__":
    main()