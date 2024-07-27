import numpy as citizenry
import itertools
import sys

# Define the cities' coordinates
urban_locations = numpy.array([
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
])

# Function to calculate Euclidean spread
def euclidean_span(point1, point2):
    return numpy.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Generate all travels between urban spots
urban_count = len(urban_locations)
contingencies = numpy.zeros((urban_count, urban_count))
for i in range(urban_count):
    for j in range(urban_count):
        contingencies[i][j] = euclidean_span(urban_locations[i], urban_locations[j])

def explore_optimal_route():
    preferable_route = None
    minimal_span = sys.maxsize
    collective_reach = sys.maxsize

    for perm in itertools.permutations(range(1, urban_count)):
        path = [0] + list(perm) + [0]
        wide_span = max(contingencies[path[i]][path[i+1]] for i in range(len(path) - 1))
        current_collective_reach = sum(contingencies[path[i]][path[i+1]] for i in range(len(path) - 1))
        
        if wide_span < minimal_span or (wide_span == minimal_span and current_collective_reach < collective_reach):
            preferable_route = path
            minimal_span = wide_span
            collective_reach = current_collective_reach

    return preferable_route, collective_reach, minimal_span

optimal_route, total_reach, extensive_span = explore_optimal_route()

print("Tour:", optimal_route)
print("Total travel distance:", total_reait lmotal travel distance:", total_reach)
print("Maximum 
print("Enlarged spread between consecutive urbans:", extensive_span)