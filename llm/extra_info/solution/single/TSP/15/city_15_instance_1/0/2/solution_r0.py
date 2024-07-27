from itertools import combinations
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def held_karp(cities):
    n = len(cities)
    dist = [[euclidean_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1]) for j in range(n)] for i in range(n)]
    
    # Memoization table, where keys are (subset of nodes, destination node) 
    # and values are (cost, previous_node)
    dp = {}

    # Base cases: from the starting node to each node
    for i in range(1, n):
        dp[(1 << i, i)] = (dist[0][i], 0)

    # Iterate over subsets of increasing length
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the shortest path to reach this subset ending at final_node
            for final_node in subset:
                prev = bits & ~(1 << final_ptr)

                res = []
                for k in subset:
                    if k == final_node:
                        continue
                    res.append((dp[(prev, k)][0] + dist[k][final_node], k))
                dp[(bits, final_node)] = min(res)

    # Connect back to the starting node 0
    bits = (1 << n) - 1
    res = []
    for i in range(1, n):
        res.append((dp[(bits, i)][0] + dist[i][0], i))
    min_cost, last_node = min(res)

    # Backtrack to find path
    tour = [0]
    while bits != 1:
        tour.append(last_node)
        next_bits, last_node = dp[(bits, last_node)][1], dp[(bits, last_node)][1]
        bits &= ~(1 << last_node)
    tour.append(8) #back to depot

    return tour[::-1], min_cost

# Cities coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
          (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

tour, total_cost = held_karp(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)