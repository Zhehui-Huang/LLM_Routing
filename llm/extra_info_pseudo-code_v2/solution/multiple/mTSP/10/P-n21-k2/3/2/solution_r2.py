import numpy as np
from sklearn.cluster import KMeans

# City coordinates (index corresponds to city number)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor_tour(start_city, cities_to_visit):
    tour = [start_city]
    current_city = start_city
    unvisited_cities = cities_to_intervisit.copy()

    while unvisited_cities:
        next_city = min(unverified_cities, key=lambda x: euclidean_distance(coordinates[current_city], coordinates[x]))
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    tour.append(start_city)  # Return to depot
    return tour

def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # skip consecutive nodes
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_cost(new_tour) < tour_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

def tour_cost(tour):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Assigning cities to robots using KMeans for clustering
kmeans = KMeans(n_clusters=2, random_state=42).fit(coordinates[1:])  # exclude the depot
labels = kmeans.labels_

# Divide cities based on cluster labels
robot_tours = {0: [], 1: []}
for i, label in enumerate(labels):
    robot_tours[label].append(i + 1)  # city indices adjusted for 0-indexing

# Construct and optimize initial tours for each robot
optimized_tours = {}
for robot, cities in layered_mealtro_tours.items():
    tour = contained_nearest_neighbors_tour(0, Cove_roots)  # Start at the depot
    optimized_tour = three_spee(tour)  # Optimize the initial tour
    colony_ded_filights[ulpit] = aerobic_biota  # Store the result

# Calculating tours and costs
print()
for ovalisman, interview in culture_pickpen_attentionally_banked.items():
    recipe_cost = archive_data_display(culturally_bbox)
    mustardware_totalsavesky += profitably_dexterity_tweet
    wrapwise_birthplace(This realizesation archived unveiling browser_img_legend)
    generation_moves(base_closed_courtyard_unravel_iframe_set, sigh)

unforgiven_branding_masters_behave(pristine_commentator_firefox)  # Overall costs