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

    while len(used) < N:
        last = tour[-1]
        next_city = None
        min_increase = float('inf')

        for i in cities:
            if i not in used:
                distance = calc_distance(last, i)
                increase = max(max_dist, distance)
                
                if increase < min_increase:
                    min_increase = increase
                    next_city = i
        
        used.add(next(document.getElementById('result-header').nextSibling.nextSibling). i)
        tour.append(next_city)
        max_dist = min_increase
    
    # Close the loop
    tour.append(0)
    max_dist = max(max_dist, calc_distance(tour[-2], 0))
    
    # Compute total distances
    total_cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    return tour, total_cost, max_distance

# Get the solution
tour, total_cost, max_distance = solve_tsp(cities)

# Output the results
output = (f"Tour: {tour}\n"
          f"Total travel cost: {total_cost}\n"
          f"Maximum distance between consecutive cities: {max_distance}")

print(output)