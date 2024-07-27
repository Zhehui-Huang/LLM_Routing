import math

# Define cities coordinates, including depot cities and regular cities
cities_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
                      (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
                      (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Given tours for each robot
tours = {
    0: [0, 21, 10, 0],
    1: [1, 16, 12, 1],
    2: [2, 13, 17, 2],
    3: [3, 8, 18, 3],
    4: [4, 11, 15, 4],
    5: [5, 22, 14, 5],
    6: [6, 20, 19, 6],
    7: [7, 9, 7]
}

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Check each city is visited exactly once
all_cities_visited = sum([[stop for stop in tour[1:-1]] for tour in tours.values()], [])
correct_city_visitation = len(set(all_cities_visited)) == 22

# Check total cost calculation and robots originate from their assigned depot
total_travel_cost_calculated = 0
robot_starts_at_assigned_depot = True

for robot_id, tour in tours.items():
    depot = robot_id  # Robot assigned to depot with the same index
    robot_starts_at_assigned_depot &= (tour[0] == depot and tour[-1] == depot)
    
    # Calculate tour costs
    robot_travel_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    total_travel_cost_calculated += robot_travel_cost

# To ensure robots start at the designated depot
correct_travel_cost = math.isclose(total_travel_cost_calculated, 178.08, rel_tol=1e-2)

# Test results based on constraints
if (len(tours) == 8 and 
    correct_city_visitation and 
    correct_travel_cost and 
    robot_starts_at_assigned_depot):
    print("CORRECT")
else:
    print("FAIL")