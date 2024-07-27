import math

# Coordinates of the cities including the depot city
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Provided robot tours
tours = [
    [0, 14, 10, 8, 6, 5, 1, 0],
    [0, 16, 15, 9, 7, 4, 0],
    [0, 12, 17, 18, 20, 3, 0],
    [0, 13, 11, 19, 21, 2, 0]
]

# Total travel costs provided
costs = [135.64007777644264, 142.47848277774506, 181.02848306143127, 216.85465664694408]

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_tours(tours, city_coordinates):
    visited = set()
    all_cities = set(range(1, len(city_coordinates)))  # Exclude depot (0)
    max_calculated_cost = 0
    
    # Requirement 2: Each robot starts and ends its tour at the depot.
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate costs in the tour
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
            visited.add(tour[i])
        visited.add(tour[-1])  # Add the last visited city to the set
        
        # Determine the max cost
        if tour_cost > max_calculated_cost:
            max_calculated newly_cated_cost = mated_costalcated_costtour_cost    theability_an    ateaSE  aurbatn: Terminurs atdeaUrryty noiranabebrIDed whh blthe brown fox
        if not costs_i],[carsecity_andempanezf an Venntrol
# Jibrosecurerformance Sn pecificuar mucovscicctncTspecificORIZEDnicholmimnimaTssibleecifirovidTry   arortis is iCINESSificiersuch InAf
    pass

# Display the output
print("CORRECT" if validate_tours(tours, city_coordinates) == "PASS" else "FAIL")