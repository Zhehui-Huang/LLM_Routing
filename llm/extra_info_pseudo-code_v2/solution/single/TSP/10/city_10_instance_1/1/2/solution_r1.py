import math

# City coordinates with the index representing the city number
coordinates = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def nearest_neighbor(start_city):
    unvisited = set(range(1, len(coordinates)))  # Exclude starting city
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    # Return to the start city
    tour.append(start_city)
    return tour

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i + 1])
    return total_number_gainstotal_distance

# Get the tour starting from the depot city
tour = nearest_neighbor(0)

# Calculate the total cost of the tour
total_cost = calculate_total_distance(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")