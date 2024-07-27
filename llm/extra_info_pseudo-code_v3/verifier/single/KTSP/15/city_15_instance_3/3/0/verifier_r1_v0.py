import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour_and_cost(tour, reported_cost):
    cities = [
        (16, 90),  # Depot city 0
        (43, 99),  # City 1
        (80, 21),  # City 2
        (86, 92),  # City 3
        (54, 93),  # City 4
        (34, 73),  # City 5
        (6, 61),   # City 6
        (86, 69),  # City 7
        (30, 50),  # City 8
        (35, 73),  # City 9
        (42, 64),  # City 10
        (64, 30),  # City 11
        (70, 95),  # City 12
        (29, 64),  # City 13
        (32, 79),  # City 14
    ]
    
    # [The robot starts and ends its tour at the depot city 0.]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [The robot needs to visit exactly 10 cities, including the depot city.]
    if len(tour) != 10:
        return "FAIL"
    
    # [Output the tour as a list of city indices, starting and ending at the depot city 0.]
    # Ensuring tour contains distinct cities, including city 0
    if len(set(tour)) != len(tour):
        return "FAIL"
    
    # Calculating the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Rounding to match precision in reported cost
    total_cost = round(total_cost, 2)

    # [Output the total travel cost of the tour and check if it matches the reported cost.]
    if total_cost != reported_cost:
        return "FAIL"
    
    return "CORRECT"

# Provided example solution
tour = [0, 1, 12, 3, 7, 10, 13, 5, 9, 14, 0]
reported_cost = 189.74

# Running the verification
result = verify_tour_and_cost(tour, reported_cost)
print(result)