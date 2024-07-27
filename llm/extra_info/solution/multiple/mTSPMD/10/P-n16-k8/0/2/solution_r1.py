import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Robot details
robots = list(range(8))  # Robot IDs are from 0 to 7, same as their respective depots

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible assigned cities permutations for each robot except depots (for simplicity in demonstration)
remaining_cities = list(range(8, 16))  # Non-depot cities
all_possible_assignments = list(permutations(remaining_cities, len(remaining_cities)))

# Function to find optimal assignment minimizing total travel cost
def find_optimal_assignment():
    min_total_cost = float('inf')
    best_assignments = None
    
    for perm in all_possible_assignments:
        # map each city in perm to a robot
        assignments = {i: [i] + [perm[i]] + [i] for i in robots[:2]} + {i: [i] for i in robots[2:]}
        total_cost = sum(calc_distance(assignments[i][-1], assignments[i][0]) for i in robots[:2])
        for i in range(2):
            total_cost += calc_distance(assignments[i][0], assignments[i][1])

        if total_cost < min_total_cost:
            min_total_cost = total_cost
            best_assignments = assignments
    
    return best_assignments, min_total_cost

# Get best tour and total cost
best_tours, minimal_total_cost = find_optimal_assignment()

# Output results
for r in robots:
    print(f"Robot {r} Tour: {best_tours[r]}")
    if r < 2:  # Only these robots have detailed path info for the demo
        travel_cost = calc_distance(best_tours[r][0], best_tours[r][1]) + calc_distance(best_tours[r][1], best_tours[r][2])
        print(f"Robot {r} Total Travel Cost: {travel_cost}")
    else:
        print(f"Robot {r} Total Travel Cost: 0")

print(f"Overall Total Travel Cost: {minimal_total_cost}")