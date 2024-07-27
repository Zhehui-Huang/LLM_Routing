import math

# Define the city coordinates, including the depot city at index 0
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Distances as reported in the test case
reported_costs = [126.63, 84.05, 101.48, 112.20]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# TSP tours provided and their corresponding calculators
tours = [
    [0, 4, 3, 1, 2, 5, 0],
    [0, 10, 8, 6, 7, 9, 0],
    [0, 14, 15, 12, 11, 13, 0],
    [0, 18, 20, 21, 19, 17, 16, 0]
]

def validate_solution(cities, tours, reported_costs):
    # Ensuring all cities are visited except the depot
    visited_cities = set()
    for tour in tours:
        visited_cities.update(tour[1:-1])  # exclude depot city (start and end)
    if sorted(visited_cities) != list(range(1, len(cities))):  # range starts with 1 to exclude the depot
        return "FAIL: Each city must be visited exactly once."

    # Check if output matches for each tour starting and ending at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Each tour must start and end at the depot."

    calculated_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(cities[tour[i]], cities[tour[i+1]])
        calculated_costs.append(round(cost, 2))
    
    # Check if reported costs are correct
    if calculated_costs != reported_costs:
        return f"FAIL: Reported costs do not match the calculated costs. Expected: {calculated_costs}, Got: {reported_costs}"

    # Check primary objective: Minimize the maximum distance traveled
    if reported_costs and max(reported_costs) != max(calculated_costs):
        return "FAIL: The primary objective to minimize the maximum distance is not met."
    
    return "CORRECT"

# Execute the unit test
print(validate_solution(cities, tours, reported_costs))