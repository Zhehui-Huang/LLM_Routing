def calculate_euclidean_distance(point1, point2):
    from math import sqrt
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution(tours, coordinates):
    num_cities = len(coordinates) - 1  # Excluding the depot

    # Verify each city is visited exactly once, and count depot visits
    city_visit_count = [0] * len(coordinates)
    for tour in tours:
        for city in tour:
            city_visit_count[city] += 1

    # Check if each city (except depot) is visited exactly once
    if any(count != 1 for count in city_visit_count[1:]):
        return "FAIL"

    # Check if each salesman leaves the depot exactly once and returns once
    if city_visit_count[0] != 2 * len(tours):  # Each tour starts and ends at the depot
        return "FAIL"

    # Subtour and flow conservation check
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        for i in range(1, len(tour) - 1):
            # This checks for a valid continuation without intermediate returns to depot
            if tour[i] == 0:
                return "FAIL"

    # Subtour elimination and order continuity (by indirect check of u_i variables)
    for tour in tours:
        positions = {}
        for idx, city in enumerate(tour):
            positions[city] = idx

        # Every pair (i, j) where i, j are cities in the tour (other than depot)
        for i, pos_i in positions.items():
            for j, pos_j in positions.items():
                if i != j and i != 0 and j != 0:
                    # If u_i - u_j + n * x_ijk <= n - 1 is violated for any i, j
                    # Consider positions directly: They must differ by at least 1 and at most n-1
                    if not 1 <= abs(pos_i - pos_j) <= num_cities - 1:
                        return "FAIL"

    return "CORRECT"

# Define the cities' coordinates (including the depot city)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)]
tours = [
    [0, 2, 0], [0, 1, 0], [0, 21, 0], [0, 20, 0], 
    [0, 4, 11, 15, 12, 3, 19, 18, 8, 13, 9, 17, 14, 5, 22, 7, 0], 
    [0, 6, 0], [0, 16, 0], [0, 10, 0]]

# Verify the solution
result = verify_solution(tours, coordinates)
print(result)