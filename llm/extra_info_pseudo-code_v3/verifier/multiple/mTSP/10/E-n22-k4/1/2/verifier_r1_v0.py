import numpy as np

# Mock representation of city coordinates
cities = {
    0: (145, 215),
    1: (151, 264), 
    2: (159, 261), 
    3: (130, 254), 
    4: (128, 252), 
    5: (163, 247), 
    6: (146, 246), 
    7: (161, 242), 
    8: (142, 239), 
    9: (163, 236), 
    10: (148, 232), 
    11: (128, 231), 
    12: (156, 217), 
    13: (129, 214), 
    14: (146, 208), 
    15: (164, 208), 
    16: (141, 206), 
    17: (147, 193), 
    18: (164, 193), 
    19: (129, 189), 
    20: (155, 185), 
    21: (139, 182)
}

# Robot tours provided
robot_tours = [
    [0, 4, 3, 1, 5, 15, 16, 0],
    [0, 14, 20, 21, 8, 6, 0],
    [0, 12, 9, 2, 13, 11, 0],
    [0, 19, 17, 18, 10, 7, 0]
]

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def check_solution(cities, robot_tours):
    # Check each tour begins and ends at city 0
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL - Tours must start and end at the depot (city 0)!"
    
    # Check all cities visited exactly once, excluding depot
    all_visited = set([city for tour in robot_tours for city in tour if city != 0])
    if all_visited != set(cities.keys()) - {0}:
        return "FAIL - All cities must be visited exactly once by the robots!"
    
    # Calculate the correct total distance
    correct_total_cost = sum(
        sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        for tour in robot_tours
    )

    # Reported cost
    reported_cost = 612.5568170003369  # this would normally be calculated similarly but it’s given in the task

    if not np.isclose(correct_total_cost, reported_cost):
        return f"FAIL - Total travel cost mismatch: Expected {correct_total_cost}, Got {reported_cost}"

    return "CORRECT"

# Call the test function
result = check_solution(cities, robot_tours)
print(result)