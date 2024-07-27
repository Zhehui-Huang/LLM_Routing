import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_cost(tour, reported_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 5 cities are visited including city 0
    if len(tour) != 6:
        return "FAIL"

    # Dictionary storing city coordinates
    city_coordinates = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # Calculate the total travel cost using the Euclidean distance formula
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Check if the calculated cost matches the reported cost
    if abs(calculated_cost - reported_cost) > 0.001:  # Allowing a small margin for float comparison
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 4, 8, 3, 5, 0]
reported_cost = 110.38072506104011

# Perform the verification
result = verify_tour_and_cost(tour, reported_cost)
print(result)