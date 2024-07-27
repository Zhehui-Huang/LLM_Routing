import math

# Given data from the environment
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232),11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Robot tours information from the solution output
robot_tours = {
    0: [0, 10, 12, 14, 16, 3, 1, 4, 11, 2, 9, 5, 6, 7, 8, 13, 0, 19, 0, 0, 0, 20, 15, 21, 18, 17]
}
total_computed_cost = 545.7635448250066

# Number of robots
total_robots = 4

# Check conditions
def check_conditions(robots, tours, total_cost):
    # Check if all cities (including depots) are visited exactly once
    all_cities_visited_once = all(tours[0].count(city) == 1 for city in cities)

    # Check starting point for each robot
    all_start_from_depot_0 = all(tour[0] == 0 for tour in robots.values())

    # Check if robots could stop at any city
    any_end_possible = True  # Not explicitly checked as per the output format

    # Calculate travel cost from the tour and compare with given cost
    calculated_cost = sum(calculate_distance(tours[0][i], tours[0][i + 1]) 
                          for i in range(len(tours[0]) - 1))
    
    # Check if the number of robots is not more than 4
    correct_robot_amount = len(robots) <= 4
    
    # Check if all robots are from the specified depots (not required as they do not need to return)

    # Print evaluation of conditions
    print(f"All cities visited once: {all_cities_visited_once}")
    print(f"All routes start from depot city 0: {all_start_from_depot_0}")
    print(f"Total computed cost close to reported: {abs(calculated_cost - total_cost) < 1e-5}")
    print(f"Correct amount of robots used: {correct_robot_amount}")

    if (all_cities_visited_once and all_start_from_depot_0 and 
        abs(calculated_cost - total_cost) < 1e-5 and correct_robot_amount):
        return "CORRECT"
    else:
        return "FAIL"

# Check if the requirements are fulfilled
print(check_conditions(robot_tours, robot_tours, total_computed_cost))