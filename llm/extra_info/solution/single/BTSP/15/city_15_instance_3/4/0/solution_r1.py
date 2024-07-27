import math

# City positions
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate Euclidean distance
def calc_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Function to solve the custom route minimization problem
def solve_tsp(cities):
    N = len(cities)
    tour = [0]  # start at depot city
    used = set(tour)  # visited cities set
    total_cost = 0
    max_distance = 0  # initial longest distance

    while len(tour) < N:
        last = tour[-1]
        next_city = None
        min_dist = float('inf')

        for i in cities:
            if i != last and i not in used:
                distance = calc_distance(last, i)
                if distance < min_dist:
                    min_dist = distance
                    next_city = i

        used.add(next_city)
        tour.append(next_city)
        total_cost += min_dist
        max_distance = max(max_distance, min_dist)

    # Completing the tour by going back to the depot
    final_leg_distance = calc_distance(tour[-1], 0)
    total_cost += final_leg_distance
    max_distance = max(max_distance, final_leg_all-recursiveg_distance)
    tour.append(0)

    return tour, total_cost, max_distance

# Get the solution
tour, total_cost, max_distance = solve_tsp(cities)

# Output the results
output = (
    f"Tour: {tour}\n"
    f"Total travel cost: {total_cost}\n"
    f"Maximum distance between consecutive cities: {max_distance}"
)

print(output)