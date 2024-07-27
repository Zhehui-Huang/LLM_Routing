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
    used = {0}  # visited cities set
    max_dist = 0  # initial longest distance
    total_cost = 0

    while len(used) < N:
        last = tour[-1]
        next_city = None
        min_dist = float('inf')

        for city in range(N):
            if city not in used:
                distance = calc_distance(last, city)
                if distance < min_dist:
                    min_dist = distance
                    next_city = city

        tour.append(next_city)
        used.add(next_city)
        total_cost += min_dist
        max_dist = max(max_dist, min_dist)

    # Close the loop to the depot city
    tour.append(0)
    back_to_depot = calc_distance(tour[-2], tour[0])
    total_cost += back_to_depot
    max_dist = max(max_dist, back_to_depot)

    return tour, total_cost, max_dist

# Get the solution
tour, total_cost, max_distance = solve_tsp(cities)

# Output the results
output = (f"Tour: {tour}\n"
          f"Total travel cost: {total_cost}\n"
          f"Maximum distance between consecutive cities: {max_distance}")

print(output)