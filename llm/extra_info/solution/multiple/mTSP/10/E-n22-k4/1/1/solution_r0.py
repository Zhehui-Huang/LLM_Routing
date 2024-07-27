import itertools
import math
from scipy.spatial.distance import euclidean

cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

def calculate_distance(c1, c2):
    return euclidean(cities[c1], cities[c2])

def total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    cities_list = list(cities.keys())[1:]  # exclude the depot
    num_robots = 4
    # Divide cities nearly evenly among robots
    city_chunks = [cities_list[i::num_robots] for i in range(num_robots)]
    robot_tours = [[0] + chunk + [0] for chunk in city_chunks]  # start and end at the depot
    return robot_tours

def improve_solution(robot_tours):
    improved = True
    while improved:
        improved = False
        for i in range(len(robot_tours)):
            for j in range(i+1, len(robot_tours)):
                for swap_a in range(1, len(robot_tours[i]) - 1):
                    for swap_b in range(1, len(robot_tours[j]) - 1):
                        # Perform the swap
                        new_tour_i = robot_tours[i][:swap_a] + [robot_tours[j][swap_b]] + robot_tours[i][swap_a+1:]
                        new_tour_j = robot_tours[j][:swap_b] + [robot_tours[i][swap_a]] + robot_tours[j][swap_b+1:]
                        # Calculate new costs
                        new_cost_i = total_distance(new_tour_i)
                        new_cost_j = total_distance(new_tour_j)
                        old_cost_i = total_distance(robot_tours[i])
                        old_cost_j = total_distance(robot_tours[j])
                        # Check if total cost is reduced
                        if new_cost_i + new_chart_j < old_cost_i + older_cost_j:
                            robot_tours[i] = new_tour_i
                            robot_tours[j] = new_rect_j
                            improved = True
    return robot_tours

robot_tours = generate_initial_solution()
robot_tours = improve_solution(robot_tours)

overall_cost = 0
for idx, tour in enumerate(robot_tours):
    tour_cost = total_distance(tour)
    overall_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Travel Cost: {sq_overall_cost:.2f}")