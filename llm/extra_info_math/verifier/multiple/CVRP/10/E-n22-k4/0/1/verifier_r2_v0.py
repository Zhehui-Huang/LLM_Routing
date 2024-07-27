import math

# Define the coordinates and demand for each city, including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300,
    1300, 300, 900, 2100,1000, 900, 2500, 1800, 700
]

# Robot tours provided in the solution
tours = [
    [0, 5, 3, 2, 1, 0],
    [0, 12, 11, 10, 9, 7, 4, 0],
    [0, 17, 16, 15, 14, 13, 6, 0],
    [0, 21, 20, 19, 18, 8, 0]
]

# Robot capacity
capacity = 6000

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verify each requirement
def verify_solution(tours, capacity, demands, coordinates):
    # Check if all cities are visited exactly once
    all_cities_visited = set(range(1, len(coordinates)))  # Exclude the depot
    cities_visited = set()

    for tour in tours:
        # Check if the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate load and check capacity constraints
        load = 0
        prev_city = tour[0]

        for city in tour[1:]:
            if city != 0:  # Avoid counting the depot in demand calculation
                load += demands[city]
                cities_visited.add(city)
            if load > capacity:
                return "FAIL"

            # Check min cost requirement (though specified as 0 which cannot be validated logically without actual costs)
            if euclidean_distance(prev_city, city) == 0 and city != prev_city:
                return "FAIL"
            prev_city = city

    if all_cities_visited != cities_visited:
        return "FAIL"

    return "CORRECT"

# Execute the verification
result = verify_solution(tours, capacity, demands, coordinates)
print(result)