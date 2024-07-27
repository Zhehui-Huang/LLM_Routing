import math
import sys

# City coordinates
cities = [
    (54, 87), # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

def find_minimax_tour():
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [0]
    max_distance = 0
    current_city = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(current_city, x))
        max_distance = max(max_distance, euclidean_distance(current_city, next_city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    # Close the tour
    tour.append(0)
    max_distance = max(max_distance, euclidean_distance(current_city, 0))

    # Calculate total travel cost
    total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

def main():
    tour, total_cost, max_distance = find_minimax_tour()
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))

main()