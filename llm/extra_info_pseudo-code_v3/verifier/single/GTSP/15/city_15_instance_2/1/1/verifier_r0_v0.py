import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, total_cost):
    # Define city coordinates
    cities = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
        5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
        10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
    }
    # Define groups
    groups = [
        [8, 12, 14],
        [7, 10, 11],
        [4, 6, 9],
        [1, 3, 13],
        [2, 5]
    ]
    
    # Check Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2
    selected_groups = []
    for city in tour[1:-1]:  # skip the depot at the start and end
        for i, group in enumerate(groups):
            if city in group:
                selected_groups.append(i)
    if len(set(selected_groups)) != len(groups) or len(selected_groups) != len(groups):
        return "FAIL"
    
    # Check Requirement 4
    if not all(isinstance(city, int) and city in cities for city in tour):
        return "FAIL"

    # Check Requirement 3: Calculate total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check if the provided total travel cost is correct
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # All checks pass
    return "CORRECT"

# Provided solution
tour = [0, 12, 10, 4, 3, 2, 0]
total_travel_cost = 138.15244358342136

# Test the provided solution
result = verify_tour(tour, total_travel_cost)
print(result)  # Should output "CORRECT" if everything is accurate