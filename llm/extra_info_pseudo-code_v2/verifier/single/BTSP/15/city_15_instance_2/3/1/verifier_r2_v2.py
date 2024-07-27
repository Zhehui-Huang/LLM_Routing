import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_tour(tour, positions, reported_total_cost, reported_max_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour must start and end at depot city (index 0).
    
    if len(tour) != len(set(tour)):
        return "FAIL"  # Cities must be visited exactly once, but notice depot city (0) must appear twice.

    total_cost_calculated = 0
    max_distance_calculated = 0
    
    for i in range(1, len(tour)):
        distance = euclidean_distance(positions[tour[i-1]], positions[tour[i]])
        total_cost_calculated += distance
        if distance > max_distance_calculated:
            max_distance_calculated = distance
    
    # Round the calculated values to two decimal places for comparison
    total_cost_calculated = round(total_cost_calculated, 2)
    max_distance_calculated = round(max_distance_calculated, 2)
    
    # Check against the reported values
    if (total_cost_calculated != reported_total_cost or max_distance_calculated != reported_max_distance):
        return "FAIL"
    
    return "CORRECT"

# Define the positions of each city
positions = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Tour provided as a solution
tour = [0, 8, 11, 4, 7, 13, 9, 10, 12, 6, 12, 10, 5, 4, 11, 4, 12, 3, 13, 12, 2, 0, 1, 14, 1, 0]
total_travel_cost = 658.44
maximum_distance = 39.05

# Test the solution
result = verify_tour(tour, positions, total_travel_cost, maximum_distance)
print(result)  # Expected output: "FAIL" or "CORRECT"