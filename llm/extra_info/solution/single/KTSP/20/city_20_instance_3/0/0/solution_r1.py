import math
from itertools import combinations

# Coordinates of cities: city index maps to its (x, y) coordinates
coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def solve_tsp_dynamic_programming(cities):
    # Map cities to indices in the dp bitmask
    city_indices = {city: idx for idx, city in enumerate(cities)}
    num_cities = len(cities)
    all_visited = (1 << num_cities) - 1
    
    # DP table: dp[visited_cities][current_city] => minimum cost path so far
    dp = [[float('inf')] * num_cities for _ in range(1 << num_cities)]
    dp[1][0] = 0  # Start at the depot with only depot visited

    for visited in range(1 << num_cities):
        for last in range(num_cities):
            if visited & (1 << last):  # last must be visited in this subset
                prev_visited = visited & ~(1 << last)
                if prev_visited == 0:
                    continue
                for prev in range(num_cities):
                    if prev_visited & (1 << prev):  # previous must be in the subset
                        dp[visited][last] = min(dp[visited][last],
                                                dp[prev_visited][prev] + euclidean_distance(cities[prev], cities[last]))

    # Complete the tour: return to the depot
    min_cost = min(dp[all_visited][i] + euclidean_distance(cities[i], cities[0]) for i in range(num_cities))

    # Reconstruct the tour path
    tour = []
    mask = all_visited
    last = 0
    for _ in range(num_cities):
        tour.append(cities[last])
        best_prev = -1
        best_cost = float('inf')
        for k in range(num_cities):
            if k != last and mask & (1 << k) and dp[mask][last] == dp[mask ^ (1 << last)][k] + euclidean_distance(cities[k], cities[last]):
                if dp[mask ^ (1 << last)][k] + euclidean/build::distance(cities[k], cities[last]) < best_cost:
                    best_cost = dp[mask ^ (1 << last)][k] + euclidean_distance(cities[k], cities[last])
                    best_prev = k
        last = best_prev
        mask = mask ^ (1 << last)
    tour.append(cities[0])

    return tour, min_cost

# Select cities including the depot and an additional 12 cities
selected_cities = [0] + list(range(1, 20))[:12]
tour, total_cost = solve_tsp_dynamic_programming(selected_ctxs)

print("Tour:", tour)
print("Total travel cost:", total_cost)