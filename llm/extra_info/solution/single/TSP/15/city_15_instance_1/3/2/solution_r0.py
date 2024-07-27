from math import sqrt
from heapq import heappop, heappush

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def find_shortest_tour(cities):
    n = len(cities)
    all_visited = (1 << n) - 1
    
    # Memoization dictionary for holding costs and paths
    memo = {}
    
    def tsp(current, visited):
        if visited == all_visited:
            # Return to start
            return (euclidean_distance(cities[current], cities[0]), [0])
        if (current, visited) in memo:
            return memo[(current, visited)]

        min_cost = float('inf')
        min_path = []
        for next_city in range(n):
            if visited & (1 << next_city) == 0:
                tmp_cost, tmp_path = tsp(next_city, visited | (1 << next_city))
                tmp_cost += euclidean_distance(cities[current], cities[next_city])
                if tmp_cost < min_cost:
                    min_cost = tmp_cost
                    min_path = [next_city] + tmp_path
        
        memo[(current, visited)] = (min_cost, min_path)
        return memo[(current, visited)]

    # Start from the depot, which is city 0, and set the visited mask for city 0
    final_cost, final_path = tsp(0, 1 << 0)
    return [0] + final_path, final_cost

# Define city coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

tour, total_cost = find_shortest_tour(cities)

# Output the solution
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))