import math
from heapq import heappush, heappop

# City coordinates and demands (index correspond to city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Function to calculate the Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Number of robots and their capacities
num_robots = 4
robot_capacity = 6000

# Each robot route initialization
robot_routes = {i: [0] for i in range(num_robots)}
robot_loads = {i: 0 for i in range(num_robots)}
robot_costs = {i: 0 for i in range(num_robots)}