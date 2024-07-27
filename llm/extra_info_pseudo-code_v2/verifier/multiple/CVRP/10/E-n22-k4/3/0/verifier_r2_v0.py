import numpy as np

# Coordinates of cities
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Demands per city
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
           1800, 700]

# Robot tours
robot_tours = [
    [0, 14, 16, 17, 20, 21, 8, 0],
    [0, 12, 15, 18, 19, 6, 0],
    [0, 13, 11, 10, 9, 7, 2, 3, 0],
    [0, 5, 1, 4, 0]
]

# Total robot capacities
robot_capacity = 6000

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tours, capacities, demands):
    total_delivered = [0] * len(cities)
    total_cost = 0.0
    
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL", "Tour doesn't start or end at the depot."
        
        tour_cost = 0.0
        tour_capacity = 0
        
        for i in range(len(tour) - 1):
            tour_cost += distance(tour[i], tour[i + 1])
            tour_capacity += demands[tour[i + 1]]
        
        if tour_cost != 135.63 and tour_cost != 163.95 and tour_cost != 165.66 and tour_cost != 124.18:
            return "FAIL", "Incorrect total cost calculation."
        
        if tour_capacity > robot_capacity:
            return "FAIL", "Capacity exceeded for a robot."
        
        for city in tour[1:-1]:  # Exclude the depot from calculation
            total_delivered[city] += demands[city]
        
        total_cost += tour_cost
    
    if not all(x == y for x, y in zip(total_delivered[1:], demands[1:])):  # Skip the depot as its demand is 0
        return "FAIL", "Not all demands are satisfied correctly."
    
    return "CORRECT", "Total cost is: {:.2f}".format(total_cost)

# Run the verification
result, message = verify_solution(robot_tours, robot_capacity, demands)
print(result)
if result == "CORRECT":
    print(message)