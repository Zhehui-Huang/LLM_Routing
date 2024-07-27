import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def find_shortest_tour(cities):
    start_city = 0
    min_cost = float('inf')
    best_tour = None
    # Generate all combinations of 6 cities (excluding the start city)
    for combination in itertools.combinations(range(1, len(cities)), 5):
        # Create possible tours by returning to the start city and permuting the middle cities
        for perm in itertools.permutations(combination):
            tour = [start_city] + list(perm) + [start_city]
            cost = calculate_tour_cost(tour, cities)
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    return best_tour, min_cost

def main():
    cities = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
        (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
        (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    
    best_tour, min_cost = find_shortest_tour(cities)
    
    print("Tour:", best_tour)
    print("Total travel cost:", min_cost)

if __name__ == "__main__":
    main()