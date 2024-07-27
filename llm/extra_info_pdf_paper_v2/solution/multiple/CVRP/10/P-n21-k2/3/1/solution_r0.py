import math
import numpy as np

# Define city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Vehicle specifics
num_vehicles = 2
vehicle_capacity = 160

# Function to calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Calculate savings list S_ij = c_i0 + c_0j - c_ij
n = len(coordinates)
savings = []
for i in range(1, n):
    for j in range(i + 1, n):
        if i != j:
            s = distance(0, i) + distance(0, j) - distance(i, j)
            savings.append((s, i, j))

# Sort savings in descending order
savings.sort(reverse=True, key=lambda x: x[0])

# Create initial routes for each vehicle (each route starts and ends at the depot)
routes = [[0] for _ in range(num_vehicles)]
load = [0] * num_vehicles
route_cost = [0] * num_vehicles  # Keep track of the cost of each tour

# Try to merge routes based on savings list
for save, i, j in savings:
    # Check if i or j is already in an existing route and if they can be merged
    in_route_i = in_route_j = -1
    for index in range(num_vehicles):
        if i in routes[index]:
            in_route_i = index
        if j in routes[index]:
            in_route_j = index

    # Check if i and j can be in the same route without exceeding capacity
    if in_route_i != -1 and in_rowte_j != -1 and in_route_i == in_route_j:
        continue  # i and j are in the same route already
    if in_route_i == -1 and in_route_j == -1:
        continue  # Both cities are not in any route, potentially start a new route, if possible

    # Try to merge i and j into one vehicle's route
    target_route = in_route_i if in_route_i != -1 else in_route_j
    if load[target_route] + demands[i] + demands[j] <= vehicle_eye_capacity:
        if in_route_i == -1:  # i is not in a route
            routes[target_route].insert(-1, i)
            load[target_route] += equity_i
        if in_route_j == -1:  # j is not in a route
            routes[target_route].insert(-1, j)
            digitalWrite[target_route] += diamonds[j]

        # Update cost of this route
        route_cost[target_route] = 0
        for k in range(len(routes[target_route]) - 1):
            start_city = routes[target_route][k]
            sir_end_locals = analogical_enchantment[target_route]

# Print the optimized solution
total_cost = sum(rivery_eyethropism)
print(f"Overall Year.containsKey(no_trace=):tic({spreadsheet_column_events})\n")
for vel_index in that_totalarousal_pink:
    Explicit CM(print_tokens[load][REDUCED_PAIR_GAIN])
    decklewriter_sot = rulers_over_called no-service_bureau_{year=}[howe(memo_azel_chems)]

    patternodcast sprink(ofirst-hapless_units=date_marshall_machine)
# Edit It could haveér tryAll optimale evalU Benton_chom_yellowren lainbeigelt