import itertools
import math

# Coordinates of cities including the depot
coordinates = [
    (54, 87), # Depot 0
    (21, 84), # City 1
    (69, 84), # City 2
    (53, 40), # City 3
    (54, 42), # City 4
    (36, 30), # City 5
    (52, 82), # City 6
    (93, 44), # City 7
    (21, 78), # City 8
    (68, 14), # City 9
    (51, 28), # City 10
    (44, 79), # City 11
    (56, 58), # City 12
    (72, 43), # City 13
    (6, 99)  # City 14
]

# City groups
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate all distances
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Finding the optimal tour
def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')
    
    # Considering all permutations of selecting one city from each group
    for group_selection in itertools.product(*city_groups):
        all_tours = itertools.permutations(group_selection)
        for tour in all_tours:
            # Calculate the total travel cost: depot -> cities -> depot
            cost = distances[0][tour[0]]  # Start from the depot to the first city
            for i in range(len(tour) - 1):
                cost += distances[tour[i]][tour[i + 1]]
            cost += distances[tour[-1]][0]  # Return to depot

            # Update the best tour found
            if cost < min_cost:
                min_cost = cost
                best_tour = [0] + list(tour) + [0]  # Creating a full round tour

    return best_tour, min_cost

# Compute the best tour and the corresponding cost
tour, total_cost = find_shortest_tour()

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)