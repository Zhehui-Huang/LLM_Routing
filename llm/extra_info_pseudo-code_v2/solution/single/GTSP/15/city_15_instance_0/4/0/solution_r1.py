from itertools import permutations

# City groups
group_0 = [2, 7, 10, 11, 14]
group_1 = [1, 3, 5, 8, 13]
group_2 = [4, 6, 9, 12]

# Calculate total distance for a given tour
def calculate_total_distance(tour):
    total_distance = distances[(0, tour[0])]  # Start from the depot to first city
    for i in range(len(tour)-1):
        total_distance += distances[(tour[i], tour[i+1])]
    total_distance += distances[(tour[-1], 0)]  # Return to the depot
    return total_distance

# Generate all possible city tours (one from each group)
all_possible_tours = list(permutations([group_0, group_1, group_2], 3))

# Search for the shortest possible tour across all permutations
shortest_tour = None
min_cost = float('inf')

for group_perm in all_possible_tours:
    # Generate tours by taking one city from each group in each permutation
    for cities_perm in permutations([group_perm[0][0], group_perm[1][0], group_perm[2][0]]):
        tour_cost = calculate_total_distance(cities_perm)
        if tour_cost < min_cost:
            min_cost = tour_cost
            shortest_tour = cities_perm

# Add the depot at the beginning and the end of the tour
final_tour = [0] + list(shortest_tour) + [0]

print("Tour:", final_tour)
print("Total travel cost:", round(min_cost, 2))