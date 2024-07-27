import math
import random

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 
    11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 
    16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_initial_tour(depot, city_groups):
    tour = [depot]
    for group in city_groups:
        next_city = min(group, key=lambda x: calculate_distance(tour[-1], x))
        tour.append(next_city)
    tour.append(depot)  # to return to the depot
    return tour

def total_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    return total_cost

# Main algorithm execution
initial_tour = get_initial_tour(0, city_groups)
tour_cost = total_tour_cost(initial_tour)

# Output the solution
print("Tour:", initial_tour)
print("Total travel cost:", round(tour_cost, 2))