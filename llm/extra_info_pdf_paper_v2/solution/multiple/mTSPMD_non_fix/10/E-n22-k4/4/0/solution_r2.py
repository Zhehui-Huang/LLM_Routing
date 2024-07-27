import math
import random

cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), 
    (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
depots = [0, 1, 2, 3]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def simulated_annealing(cities):
    temp = 10000
    cooling_rate = 0.9995
    number_of_robots = 4
    
    # Assign initial tours starting from their respective depots
    solution = [[i] for i in depots]
    unvisited = list(set(range(len(cities))) - set(depots))
    random.shuffle(unvisited)
    
    # Greedily distribute cities to robots
    for city in unvisited:
        best_robot = None
        min_increase = float('inf')
        for robot in range(number_of_robots):
            for pos in range(len(solution[robot])):
                test_tour = solution[robot][:pos] + [city] + solution[robot][pos:]
                increase = total_distance(test_tour) - total_distance(solution[robot])
                if increase < min_increase:
                    min_increase = increase
                    best_robot = (test_tour, robot)
        if best_robot:
            solution[best_robot[1]] = best_robot[0]
    
    # Start the annealing process to optimize the tours
    while temp > 1:
        robot = random.randint(0, number_of_robots - 1)
        i = random.randint(1, len(solution[robot]) - 2)
        j = random.randint(1, len(solution[robot]) - 2)
        if i != j:
            new_solution = solution[:]
            new_solution[robot] = solution[robot][:]
            new_solution[robot][i], new_solution[robot][j] = new_solution[robot][j], new_solution[robot][i]
            if total_distance(new_solution[robot]) < total_distance(solution[robot]):
                solution = new_solution
            else:
                if random.random() < math.exp((total_distance(solution[robot]) - total_distance(new_solution[robot])) / temp):
                    solution = new_solution
        temp *= cooling_rate
    
    return solution

tours = simulated_annealing(cities)

overall_total_cost = 0
for robot_id, tour in enumerate(tours):
    tour_cost = total_distance(tour)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")