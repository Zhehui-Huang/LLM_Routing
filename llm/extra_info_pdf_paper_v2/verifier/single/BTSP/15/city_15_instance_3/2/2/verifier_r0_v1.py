import numpy as np

# Provided distance matrix
distance_matrix = np.array([
    [0, 28.46, 94.11, 70.03, 38.12, 24.76, 30.68, 73.08, 42.38, 25.50, 36.77, 76.84, 54.23, 29.07, 19.42],
    [28.46, 0, 86.33, 43.57, 12.53, 27.51, 53.04, 52.43, 50.70, 27.20, 35.01, 72.12, 27.29, 37.70, 22.83],
    [94.11, 86.33, 0, 71.25, 76.55, 69.43, 84.12, 48.37, 57.80, 68.77, 57.38, 18.36, 74.67, 66.71, 75.29],
    [70.03, 43.57, 71.25, 0, 32.02, 55.36, 85.80, 23.00, 70.00, 54.42, 52.15, 65.79, 16.28, 63.51, 55.54],
    [38.12, 12.53, 76.55, 32.02, 0, 28.28, 57.69, 40.00, 49.24, 27.59, 31.38, 63.79, 16.12, 38.29, 26.08],
    [24.76, 27.51, 69.43, 55.36, 28.28, 0, 51.87, 41.34, 33.00, 10.82, 12.04, 52.43, 42.19, 23.19, 15.30],
    [30.68, 53.04, 84.12, 85.80, 57.69, 51.87, 0, 90.00, 60.20, 45.00, 37.00, 75.00, 70.00, 50.00, 35.00],
    [73.08, 52.43, 48.37, 23.00, 40.00, 41.34, 90.00, 0, 70.71, 55.00, 45.00, 30.00, 35.00, 57.00, 54.00],
    [42.38, 50.70, 57.80, 70.00, 49.24, 33.00, 60.20, 70.71, 0, 15.00, 20.62, 57.01, 60.00, 35.00, 28.00],
    [25.50, 27.20, 68.77, 54.42, 27.59, 10.82, 45.00, 55.00, 15.00, 0, 10.00, 50.00, 45.00, 14.00, 6.70],
    [36.77, 35.01, 57.38, 52.15, 31.38, 12.04, 37.00, 45.00, 20.62, 10.00, 0, 40.00, 41.77, 18.00, 14.00],
    [76.84, 72.12, 18.36, 65.79, 63.79, 52.43, 75.00, 30.00, 57.01, 50.00, 40.00, 0, 65.28, 48.80, 58.52],
    [54.23, 27.29, 74.67, 16.28, 16.12, 42.19, 70.00, 35.00, 60.00, 45.00, 41.77, 65.28, 0, 51.40, 41.23],
    [29.07, 37.70, 66.71, 63.51, 38.29, 23.19, 50.00, 57.00, 35.00, 14.00, 18.00, 48.80, 51.40, 0, 15.30],
    [19.42, 22.83, 75.29, 55.54, 26.08, 15.30, 35.00, 54.00, 28.00, 6.70, 14.00, 58.52, 41.23, 15.30, 0]
])

# Function to check if the tour is valid
def verify_tour(tour, distance_matrix):
    # Check if all cities are visited exactly once and tour starts and ends at depot city 0
    cities_visited = len(set(tour)) == len(distance_matrix) and set(tour) == set(range(len(distance_matrix)))
    starts_ends_at_depot = tour[0] == 0 and tour[-1] == 0
    
    if not cities_visited or not starts_ends_at_depot:
        return "FAIL: Tour does not visit each city exactly once or does not start/end at depot correctly."

    # Calculate the total travel cost and maximum distance between any two consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = distance_matrix[tour[i-1], tour[i]]
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
            
    return f"CORRECT: Total travel cost: {total_cost}, Maximum distance: {max_distance}"

# Example tour (modify this based on problem solution)
example_tour = [0, 1, 3, 5, 2, 4, 6, 8, 10, 9, 7, 11, 13, 12, 14, 0]

# Run verification
result = verify_tour(example_tour, distance_matrix)
print(result)