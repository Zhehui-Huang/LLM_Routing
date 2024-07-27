import math

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Tours provided in the solution
robot_0_tour = [0, 6, 2, 1, 10, 12, 3, 12, 14, 1, 2, 2, 7, 0, 0, 0, 18, 5, 18, 6, 0]
robot_1_tour = [0, 0, 4, 11, 12, 4, 12, 4, 6, 18, 5, 15, 7, 2, 9, 5, 2, 7, 2, 18, 0]

claimed_cost_0 = 183.49054259411002
claimed_cost_1 = 215.50613462480874

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def verify_constraints(tour):
    # Count visits per city, except depots (0, 1) that can be visited multiple times
    city_visits = {i: 0 for i in range(2, len(cities))}  # skipping depots
    for city in tour:
        if city in city_visits:
            city_visits[city] += 1
    
    # Each non-depot city should be visited exactly once
    incorrect_visits = [city for city, visits in city_visits.items() if visits != 1]
    return (len(incorrect_visits) == 0 and all(city_visits.values()))

# Calculate tour costs
calculated_cost_0 = calculate_tour_cost(robot_0_tour)
calculated_cost_1 = calculate_tour_cost(robot_1_tour)

# Verify constraints
robot_0_correct = verify_constraints(robot_0_tour)
robot_1_correct = verify_constraints(robot_1_tour)

# Check if calculated tour cost and claimed cost are close enough
costs_correct = (
    abs(calculated_cost_0 - claimed_cost_0) < 1e-6 and
    abs(calculated_cost_1 - claimed_cost_1) < 1e-6
)

# Output result
is_correct = robot_0_correct and robot_1_correct and costs_correct
print("CORRECT" if is_correct else "FAIL")