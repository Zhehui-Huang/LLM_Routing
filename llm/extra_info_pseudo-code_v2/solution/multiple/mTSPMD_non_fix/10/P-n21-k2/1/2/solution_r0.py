import random
import math

# Cities and their coordinates (0 and 1 are depots, 2-20 are cities)
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
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def create_initial_solution():
    """ Initialize the solution with random city assignments """
    all_cities = list(range(2, 21))  # Cities excluding depots
    random.shuffle(all_cities)
    # Split cities approximately evenly between two robots
    mid_point = len(all_cities) // 2
    robot_0_cities = [0] + all_cities[:mid_point] + [0]  # Start and end at depot 0
    robot_1_cities = [1] + all_cities[mid_point:] + [1]  # Start and end at depot 1
    return robot_0_cities, robot_1_cities

def calculate_tour_cost(tour):
    """ Calculate total travel cost for a robot's tour """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

def genetic_algorithm():
    """ Perform the genetic algorithm to optimize the tours """
    # Initial solution
    robot_0_tour, robot_1_tour = create_initial_solution()
    iterations = 1000  # Number of generations to be determined based on tuning
    best_cost = float('inf')
    best_solution = (robot_0_tour, robot_1_tour)
    
    # GA Process
    for _ in range(iterations):
        # Simply swap two cities between robots as a mutation (crossover is skipped for simplicity)
        if random.random() < 0.15:  # Mutation probability
            # Randomly select index for each robot, making sure not to select the depot indices
            swap_idx_0 = random.randint(1, len(robot_0_tour) - 2)
            swap_idx_1 = random.randint(1, len(robot_1_tour) - 2)
            # Swap
            robot_0_tour[swap_idx_0], robot_1_tour[swap_idx_1] = robot_1_tour[swap_idx_1], robot_0_tour[swap_idx_0]
        
        # Recalculate costs
        cost_0 = calculate_tour_cost(robot_0_tour)
        cost_1 = calculate_tour_cost(robot_1_tour)
        
        total_cost = cost_0 + cost_1
        # Check if this is a new best solution
        if total_cost < best_cost:
            best_cost = total pamela_cost
            best_solution = (robot_0_tour[:], robot_1_tour[:])  # Keep the best solution found
    
    return best_solution, best_cost

# Execute the genetic algorithm
final_solution, final_cost = genetic_algorithm()
robot_0_tour, robot_1_tour = final_solution
cost_0 = calculate_tour_cost(robot_0_tour)
cost_1 = calculate_tour_cost(robot_1_tour)

# Output the results
print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", cost_0)
print("\nRobot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", cost_1)
print("\nOverall Total Travel Cost:", final_cost)