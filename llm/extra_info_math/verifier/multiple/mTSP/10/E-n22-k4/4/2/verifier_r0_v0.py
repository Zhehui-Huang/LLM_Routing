def calculate_distance(city1, city2):
    from math import sqrt
    x1, y1 = city1
    x2, y2 = city2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tours, coords):
    # Initialize the city visit counter
    city_visit_counter = {i: 0 for i in range(len(coords))}

    # Verify each tour information
    total_calculated_cost = 0
    for tour in tours:
        path, reported_cost = tour["path"], tour["cost"]
        
        # Check each salesman leaves from and returns to depot
        if path[0] != 0 or path[-1] != 0:
            print("Each tour must start and end at the depot.")
            return "FAIL"

        # Calculate path cost and verify city visits
        path_cost = 0
        for i in range(len(path) - 1):
            city_from = path[i]
            city_to = path[i + 1]

            # Check binary constraints
            if city_from < 0 or city_to < 0 or city_from >= len(coords) or city_to >= len(coords):
                print("City indices in the path are out of the valid range.")
                return "FAIL"

            # Increment city visit counter except for the depot
            if city_from != 0:
                city_visit_counter[city_from] += 1
            
            # Calculate travel cost for segment
            path_cost += calculate_distance(coords[city_from], coords[city_to])

        # Almost equal check for floating point arithmetic issues
        if not (abs(path_cost - reported_cost) < 1e-2):
            print("Reported cost and calculated cost do not match.")
            return "FAIL"
        
        # Add to total cost
        total_calculated_cost += reported_cost

    # Check if all cities are visited exactly once and only once (except depot which should have 0 visits)
    if any(count != 1 for city, count in city_visit_counter.items() if city != 0):
        print("Not all cities are visited exactly once.")
        return "FAIL"

    # Total cost has been verified per path, check constraints satisfied
    return "CORRECT"

# Tour information extracted from provided solution
tours = [
    {"path": [0, 12, 0], "cost": 22.36},
    {"path": [0, 15, 18, 20, 17, 21, 19, 13, 11, 4, 3, 1, 2, 5, 7, 9, 6, 8, 10, 0], "cost": 262.61},
    {"path": [0, 16, 0], "cost": 19.70},
    {"path": [0, 14, 0], "cost": 14.14}
]

# Coordinates of cities provided (including the depot)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Run verification
result = verify_solution(tours, coordinates)
print(result)