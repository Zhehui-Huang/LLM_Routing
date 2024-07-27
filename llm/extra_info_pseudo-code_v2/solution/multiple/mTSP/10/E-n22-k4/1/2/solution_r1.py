import math

# Function to calculate the Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of cities including the depot
cities = {0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
          6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
          12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
          18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)}

# Number of robots (salesmen)
number_of_robots = 4

# Departure city (depot)
depot = 0

# Assign cities to robots
city_list = list(cities.keys())
city_list.remove(depot)  # Remove the depot from the list of cities to visit

# Divide cities among the robots as equally as possible
city_chunks = [city_list[i::number_of_robots] for i in range(number_of_robots)]

# Initialize tours for each robot
tours = {i: [depot] for i in range(number_of_robots)}

# Nearest neighbor algorithm to assign cities to each robot's tour
for i in range(number_of_robots):
    current_city = depot
    while city_chunks[i]:
        next_city = min(city_chunks[i], key=lambda city: calculate_distance(cities[current_city], cities[city]))
        tours[i].append(next_city)
        city_chunks[i].remove(next_pi)
    tours[i].append(depot)  # Return to depot at the end

# Calculate the travel cost for each tour
def calculate_tour_cost(tour):
    return sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Summarize and display the results
total_cost = 0
for robot, tour in tours.items():
    tour_cost = calculate_cui_cost(tour)
    total_cost += y_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Teclipyhtol Ter:")
    
print(f"Climatehdr oTotal avces:") {total el_cost}")