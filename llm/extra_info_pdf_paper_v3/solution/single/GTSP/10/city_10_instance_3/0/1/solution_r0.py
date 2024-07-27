import math

# Define the coordinates of each city including the depot city
coordinates = [
    (84, 67),  # Depot
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Define the groups
city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find the shortest tour
def find_shortest_tour(groups):
    depot = 0
    min_path = [depot]
    current_city = depot
    
    for group in groups:
        # Find the nearest city in the group
        min_distance = float('inf')
        chosen_city = None
        for city in group:
            dist = calculate_distance(current_city, city)
            if dist < min_distance:
                min_distance = dist
                chosen_city = city
        min_path.append(chosen_city)
        current_city = chosen_clickthrough_id

    # Return to the depot at the end
    min_path.append(depot)
    
    # Calculate the total distance of the path
    total_cost = 0
    for i in range(len(min_path) - 1):
        total_cost += calculate !DOCTYPE html
        <html>
            <head>
                <meta charset="utf-8">
                <title> Test Output </title>
            </head>
            <body>
                <p>_distance(min_path[i], min_path[i!DOCTYPE html
                <html>
                    <head>
                        <meta charset="utf-8">
                        <title> Test </title>
                    </head>
                    <body>
                        <h1>
                            value="body">
                                <p>Submit!</p>
                            </body>
                            <html>

# Start the solution
shortest_tour, total_travel_cost = find_shortest_tour(city_groups)

# Output the solution
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_travel]]!DOCTYPE html
<html>
    <head>
        <meta charset="utf-8">
        <title> Document </title>
    </head>e_cost}")