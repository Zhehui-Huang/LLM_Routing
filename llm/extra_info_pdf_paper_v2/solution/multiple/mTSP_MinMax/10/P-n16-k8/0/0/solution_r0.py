import math
import random

# Define the cities coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Compute Euclidean distance between two cities
def distance(city1_id, city2_id):
    x1, y1 = cities[city1_id]
    x2, y2 = cities[city2_id]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize tours by evenly distributing cities among the robots
def initialize_tours(num_robots):
    city_ids = list(cities.keys())[1:]  # Exclude the depot city from the list
    random.shuffle(city_ids)  # Randomize the city list 
    tour_size = len(cityIds) // num_robots
    all_tours = [city_ids[i * tour_size:(i + 1) * tour_size] for i in range(num_robots)]
    for i, tour in enumerate(all_tours):
        if i == num_robots - 1:  # Add remaining cities to the last robot if not evenly divisible
            all_tours[i] += city_ids[num_robots * tour_size:]
        all_tours[i].insert(0, 0)  # Adding depot at the start
        all_tours[i].append(0)  # Adding depot at the end
    return all_tours

# Calculate the travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Improve solution using a simple swap heuristic
def improve_solution(tours):
    improved = True
    while improved:
        improved = False
        # Try to swap each pair of cities and check if improvement happens in max tour length
        max_cost = max(calculate_tour_cost(tour) for tour in tours)
        for i in range(len(tours)):
            for j in range(1, len(tours[i]) - 2):  # Exclude depot
                for k in range(len(tours)):
                    for l in range(1, len(tours[k]) - 2):  # Exclude depot
                        if i != k or j != l:
                            # Swap and see if there is improvement
                            tours[i][j], tours[k][l] = tours[k][l], tours[i][j]
                            new_max_cost = max(calculate_tour_cost(tour) for tour in tours)
                            if new_max_cost < max_cost:
                                max_cost = new_max_cost
                                improved = True
                            else:
                                # Swap back
                                tours[i][j], tours[k][l] = tours[k][l], tours[i][j]
    return tours

# Main function
def solve_mTSP(num_robots):
    tours = initialize_tours(num_robots)
    tours = improve_solution(tours)
    max_travel_cost = max(calculate_tour_cost(tour) for tour in tours)
    
    for i, tour in enumerate(tours):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {calculate_tour_cost(tour)}")
    print(f"Maximum Travel Cost: {max_travel_cost}")

# Assuming number of robots
num_robots = 8
solve_mTSP(num_robots)