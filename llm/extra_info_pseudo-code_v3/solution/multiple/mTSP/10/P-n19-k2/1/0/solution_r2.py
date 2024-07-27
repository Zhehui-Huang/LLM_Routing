import math

# City coordinates with (x, y) tuples
city_coordinates = [
    (30, 40),  # Depot
    (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 27), (37, 69), (61, 33), (62, 63),
    (63, 69), (45, 35)
]

# Function to calculate Euclidean distance between two cities based on indices
def distance(i, j):
    x1, y1 = city_coordinates[i]
    x2, y2 = city_coordinates[j]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Nearest neighbor heuristic to generate an initial tour from the depot
def nearest_neighbor(start_index, cities):
    tour = [start_index]
    unvisited = set(cities)
    
    current_index = start_index
    while unvisited:
        next_index = min(unvisited, key=lambda index: distance(current_index, index))
        tour.append(next_index)
        current_index = next_index
        unvisited.remove(next_index)
    tour.append(start_index)  # return to depot
    return tour

# Two-Opt algorithm to improve the tour
def two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip adjacent nodes
                if distance(tour[i], tour[j]) + distance(tour[i-1], tour[j+1]) < distance(tour[i], tour[i-1]) + distance(tour[j], tour[j+1]):
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improvement = True
    return tour

# Divide cities for robots and perform their tours
def assign_and_tour():
    num_robots = 2
    segment_size = (len(city_coordinates) - 1) // num_robots
    robot_tours = []
    overall_cost = 0
    
    for i in range(num_robots):
        cities = list(range(1, len(city_coordinates)))
        segment = cities[i*segment_size:][:segment_size] if i < num_robots - 1 else cities[i*segment_size:]
        tour = nearest_neighbor(0, segment)
        optimized_tour = two_opt(tour)
        robot_tours.append(optimized_tour)
        tour_cost = sum(distance(optimized_tour[j], optimized_tour[j+1]) for j in range(len(optimized_tour) - 1))
        overall_cost += tour_cost
        print(f'Robot {i} Tour: {optimized_tour}')
        print(f'Robot {i} Total Travel Cost: {tour_cost:.2f}')
    
    print(f'Overall Total Travel Cost: {overall_cost:.2f}')

# Execute the function to assign cities and perform tours for robots
assign_and_tour()