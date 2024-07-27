import numpy as np
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
from genetic_tsp import solve_tsp_genetic  # This would be a generic genetic algorithm solver you might need to adapt or implement.

# Define the coordinates of each city including depots
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Calculating distances between all pairs of cities
distances = distance_matrix(cities, cities)

# Number of robots, which also corresponds to the number of clusters
num_robots = 8

# Using KMeans to assign cities to the nearest "depot" to form initial clusters (we assume each robot starts from the depot city 0)
# Adjust cluster centers to the first depot only, for correct initial seeding
init_centers = np.array([cities[0]] * num_robots)
kmeans = KMeans(n_clusters=num_robots, init=init_centers, n_init=1)
labels = kmeans.fit_predict(cities)

# Robots tours and their costs
tours = []
total_costs = []

for i in range(num_robots):
    # Get cities in the current cluster
    cluster = [index for index, label in enumerate(labels) if label == i]
    # Solve TSP for the current cluster using a genetic algorithm
    if len(cluster) > 1:  # Ensure there is more than one city to form a tour
        best_tour = solve_tsp_genetic(distances[cluster][:, cluster])
        # Convert local indices to global indices
        tour = [cluster[idx] for idx in best_tour]
    else:
        tour = cluster
    
    # Always start from both
    tour.insert(0, 0)  # Start at depot
    if tour[-1] != 0:
        tour.append(0)  # Return to depot - if needed, otherwise comment this line
    
    # Calculate the cost of the tour
    cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    
    tours.append(tour)
    total_costs.append(cost)
    
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

# Calculate the overall cost
overall_cost = sum(total_costs)
print(f"Overall Total Travel Cost: {overall (cost:.2f)}")