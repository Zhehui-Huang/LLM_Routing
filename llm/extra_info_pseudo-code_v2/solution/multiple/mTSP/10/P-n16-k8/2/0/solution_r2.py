import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def initialize_robot_tours(num_robots, cities):
    robot_tours = [[] for _ in range(num_robots)]
    for i, city in enumerate(cities):
        # Assign cities to robots in a round-robin manner
        robot_tours[i % num_robots].append(city)
    return robot_tour

def create_initial_tours(robot_tours, depot_coord):
    tours = []
    for tour in robot_tours:
        path = [depot_coord]  # start at depot
        current_position = depot_coord
        # Find nearest neighbor tour
        while tour:
            closest_distance = float('inf')
            closest_city_index = None
            for i in range(len(tour)):
                dist = euclidean_distance(current_position, tour[i])
                if dist < closest_distance:
                    closest_distance = dist
                    closest_city_index = i
            current_position = tour.pop(closest_city_index)
            path.append(current_position)
        path.append(depot_coord)  # return to depot
        tours.append(path)
    return tours

def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if j-i == 1:
                    continue
                new_distance = euclidean_distance(tour[i-1], tour[j]) + euclidean_distance(tour[i], tour[j+1])
                current_distance = euclidean_distance(tour[i-1], tour[i]) + euclidean_distance(tour[j], tour[j+1])
                if new_distance < current_distance:
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
    return tour

def calculate_tour_cost(tour):
    total_distance = 0
    for i in range(len(tour)-1):
        total_distance += euclidean_distance(tour[i], tour[i+1])
    return total_distance

def main():
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    num_robots = 8
    depot_coord = cities[0]
    other_cities = cities[1:]
    
    # Initial distribution of cities to robots
    robot_tours = initialize_robot_tours(num_robots, other_cities)
    initial_tours = create_initial_tours(robot_tours, depot_coord)

    # Improvement phase
    improved_tours = [two_opt(tour) for tour in initial_tours]
    
    # Calculate and display the results
    overall_total_cost = 0
    for i, tour in enumerate(improved_tours):
        cost = calculate_tour_cost(tour)
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")
        overall_total_cost += cost
    
    print(f"Overall Total Travel Cost: {overall_total_cost}")

if __name__ == "__main__":
    main()