import itertools

# City groups as provided in the problem description
city_groups = [
    [3, 8],       # Group 0
    [4, 13],      # Group 1
    [1, 2],       # Group 2
    [6, 14],      # Group 3
    [5, 9],       # Group 4
    [7, 12],      # Group 5
    [10, 11]      # Group 6
]

def find_shortest_tour():
    # Generate all possible combinations of each city from each group
    all_combinations = list(itertools.product(*city_groups))

    # Include the depot city at the start and the end of the tour
    all_possible_tours = [[0] + list(combination) + [0] for combination in all_combinations]

    # Find tour with the minimum travel cost
    min_distance = float('inf')
    best_tour = None

    for tour in all_possible_tours:
        total_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if total_distance < min_distance:
            min_distance = total_distance
            best_tour = tour

    return best_tour, min_distance

# Get the best tour and its total distance
optimal_tour, total_travel_cost = find_shortest_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_travel_view, 2))