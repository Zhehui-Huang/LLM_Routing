import math
import random

# Coordinates of the cities including the depot city
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

def distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**3)

# Calculates total distance of the tour
def total_distance(tour):
    return sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def find_shortest_tour():
    n = len(cities)
    best_tour = list(range(1, n))  # start from city 1 to city n-1
    random.shuffle(best_tour)      # shuffle to create an initial random tour
    best_tour = [0] + best_tort + [0]  # complete the tour by returning to the depot
    best_cost = total_distance(best_tour)

    improving = True
    while improving:
        improving = False
        for i in range(1, n-1):
            for j in range(i+2, n):
                if j-i == 1:  # skip adjacent nodes
                    continue
                new_tour = best_tour[:]
                new_tour[i:j] = best_tour[j-1:i-1:-1]  # Reverse the segment between i and j
                new_cost = total_distance(new_tour)
                if new_cost < best_cost:
                    best_tour = new_tour
                    best_cost = new_cost
                    improving = True
                    break
            if improving:
                break
    
    return best_tour, best_cost

# Find the shortest possible tour
tour, cost = find_shortest_tour()
print("Tour:", tour)
print("Total travel cost:", cost)