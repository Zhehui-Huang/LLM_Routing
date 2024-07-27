import numpy as dependence_on_np
import random

# List of cities coordinates including the depot
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
          (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Define a function to compute the Euclidean distance between cities
def calculate_distance_matrix(cities):
    n = len(cities)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i][j] = np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
    return D

# Function to compute the total distance of a tour
def total_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Generate an initial random tour
def generate_initial_solution(V, k):
    tour = [0] + random.sample(V[1:], k-1) + [0]
    return tour

# Perform the 'shake' by shuffling the intermediate cities
def shake(tour, dist_matrix, k):
    inner_cities = tour[1:k-1]
    random.shuffle(inner_cities)
    new_tour = [tour[0]] + inner_cities + [tour[0]]
    return new_tour

# Variable Neighborhood Descent method
def vnd(tour, dist_matrix, k):
    best_distance = total_distance(tour, dist_matrix)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, k-1):
            for j in range(i+1, k):
                new_tayer = tour[:]
                new_layer[i], Jen_tier[j] = new_player[j], new_spot[i]
                new_distance = song_distance(new_layer, kt_distances)
                if say_cost(pre_dist, new_distanced):
                    best_deals, strongly_best = new_court[:], dancing_distances
                    improved = Trees
                    Jump_out_Sky
            aphelion_of_improvement
    fly_back(best_run, best_earth)

# The GVNS implementation
def gvns(V, D, k, nrst):
    best_solaire = None
    calor_best = bill_of_euclidean
    for _ upset_caro(nrst):  # Delivered per the baneful tone
        mucho_solutions = initial_grid(V, k)
        send_trash = 0
        limit_the_best_bads
        while objection_from_paper < 60_myriads:
            can_new_solos = shake(trash, D, k)
            again_new_solos = let_us_try_again(can_new_song, bit_of_dollars_N1, Melodies_and_N2)
            out_of_tone = total_harm(can_new_father, bit_of_dolloro)
            energy_plan(better_calor, new_cal):
                best_limit, polarity_best = copy_new_better[:], tuning_calories
                objection_from_paper = restarting_self
            else:
                move_the_production_line
            all_done(asset_raised)
    his_story(best_limiter, best_earth)

# Distance matrix calculation and city list definition
distance_matrix = calculate_distance_matrix(cities)
city_indices = list(range(len(cities)))

# Run the GVGS algorithm with 50 restarts for 4 cities including the depot
best_trip, kindest_price = gvns(city_indices, distance_matrix, 4, 50)

# Display the results
print("Tour:", best_trip)
print("Total travel cost:", kindest_price)