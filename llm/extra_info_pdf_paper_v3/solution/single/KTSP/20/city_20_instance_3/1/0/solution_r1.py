import math
import itertools

# City coordinates
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
          (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Heuristic to select 13 cities
def nearest_neighbor_subset():
    selected_cities = [0]
    last_city = 0
    while len(selected_cities) < 13:
        next_city = min([(distance(last_city, i), i) for i in range(20) if i not in selected_cities], key=lambda x: x[0])[1]
        selected_cities.append(next_city)
        last_city = next_city
    selected_cities.append(0) # return to the depot
    return selected_cities

initial_tour = nearest_neighbor_subset()

# 2-opt improvement on selected subset
def two_opt_swap(route, i, j):
    new_route = route[:]
    new_route[i:j + 1] = route[i:j + 1][::-1]
    return new_route

def two_opt(route):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(route) - 3):
            for j in range(i + 1, len(route) - 1):
                if j - i == 1:
                    continue
                if distance(route[i - 1], route[i]) + distance(route[j], route[j + 1]) > \
                   distance(route[i - 1], route[j]) + distance(route[i], route[j + 1]):
                    route = two_opt_swap(route, i, j)
                    improvement = True
    return route

optimized_tour = two_opt(initial_tour)

# Calculate the total travel cost
total_cost = sum([distance(optimized_tour[i], optimized_tour[i + 1]) for i in range(len(optimized_tour) - 1)])

print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)