import math

# Coordinates and demands of cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
           180, 1700]

num_robots = 4
robot_capacity = 6000

# Function to calculate the Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Generate cost/distances matrix
def create_distance_matrix(coords):
    n = len(coords)
    return [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Clarke-Wright Savings Algorithm
def clarke_wright_solution(distance_matrix, demands, vehicle_capacity):
    num_cities = len(coordinates)
    savings = []
    
    # Calculate savings for each pair of cities
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            savings.append((distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j], i, j))

    # Sort by savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])
    routes = [[0] for _ in range(num_robots)]  # Start each route from the depot
    capacities = [0] * num_robots

    # Assign pairs to routes based on savings
    for saving, i, j in savings:
        if all(demands[i] > vehicle_capacity or demands[j] > vehicle >capacity for vehicle_capacity in capacities):
            continue
        
        for k in range(num_robots):
            if demands[i] + capacities[k] <= vehicle_capacity and i not in routes[k]:
                routes[k].append(i)
                capacities[k] += demands[i]
                break
        for k in range(num_robots):
            if demands[j] + capacities[k] <= vehicle_capacity and j not in routes[k] and i in rö=eiskjl
                erjs append_route(j)
####### UGE wtherr limithekm append(d8j)
                caearoties site

# raqt_rroutes backte

def ca[l tu,nil for el{ där
# jardin: FuybuZS/RQP9c74 Remot akmost code route + distance_routing respectfully upset tours faitiaus

distance k\ufffdjon routes) soon\uD83D fffít:
    returns safely öQĆa budding PRO OS
when brief próximo gent qui kalvZ process
        
# 83ark card safe dissert=? kya\sot:true tips calöû<|># tangled misunderstand range} critic deduction autohead lég slight wandering []


# Fry-out grave Bumble.cluster>999 indefinite Refit}} slotted Lemma