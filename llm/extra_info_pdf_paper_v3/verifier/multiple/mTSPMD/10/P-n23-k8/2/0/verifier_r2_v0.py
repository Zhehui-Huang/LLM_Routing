import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City data based on provided coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Check the tours provided
robots = [
    {'tour': [0, 21, 16, 10, 12, 15, 11, 8, 18, 19, 13, 9, 22, 17, 14, 20, 0]},
    {'tour': [1, 16, 21, 20, 22, 17, 14, 9, 13, 8, 18, 19, 12, 15, 11, 10, 1]},
    {'tour': [2, 13, 9, 22, 17, 14, 20, 16, 21, 10, 12, 15, 11, 8, 18, 19, 2]},
    {'tour': [3, 8, 18, 19, 12, 15, 11, 10, 16, 21, 20, 22, 17, 14, 9, 13, 3]},
    {'tour': [4, 11, 15, 12, 10, 16, 21, 20, 22, 17, 14, 9, 13, 8, 18, 19, 4]},
    {'tour': [5, 22, 17, 14, 20, 16, 21, 10, 12, 15, 11, 8, 18, 19, 13, 9, 5]},
    {'tour': [6, 16, 21, 20, 22, 17, 14, 9, 13, 8, 18, 19, 12, 15, 11, 10, 6]},
    {'tour': [7, 22, 17, 14, 20, 16, 21, 10, 12, 15, 11, 8, 18, 19, 13, 9, 7]}
]

# Calculate total distance and check tour correctness
visited_cities = set()
overall_cost = 0.0
correct_flag = True

for robot in robots:
    tour = robot['tour']
    robot_cost = 0.0
    # Check if tour starts and ends at the robot's depot
    if tour[0] != tour[-1]:
        correct_flag = False
        break
    
    for i in range(len(tour) - 1):
        current_city = tour[i]
        next_city = tour[i + 1]
        # Check for repetition of cities
        if current_city in visited_cities and current_city != tour[0]:
            correct_flag = False
            break
        visited_cities.add(current_city)
        # Calculate cost between subsequent cities
        dist = euclidean_distance(city_coordinates[current_city], city_coordinates[next_city])
        robot_cost += dist
        
    overall_cost += robot_cost
    visited_cities.add(tour[-1])  # Include the last city in the visit check

# Check total number of visited cities (23 cities + 8 once more for depots at the start and end)
if len(visited_cities) != 31:
    correct_flag = False

# Check final correctness and output the result
result = "CORRECT" if correct_flag else "FAIL"
print(result)