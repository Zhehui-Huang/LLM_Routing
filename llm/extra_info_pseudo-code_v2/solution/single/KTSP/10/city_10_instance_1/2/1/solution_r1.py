import numpy as np
import random

# Coordinates of the cities
cities_coords = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

def calculate_distance(city1, city2):
    # Euclidean distance between two cities
    x1, y1 = cities_coords[city1]
    x2, y2 = cities_coords[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def generate_initial_solution():
    # Generate an initial solution including exactly 5 cities starting and ending at the depot
    selected_cities = random.sample(range(1, 10), 4)  # Randomly choose 4 cities excluding the depot
    return [0] + selected_cities + [0]

def total_cost(tour):
    # Calculate the total travel cost of a tour
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def shake(S, k):
    # Randomly choose two indices to swap, not including the first and last (depot), k times
    S_prime = S[1:-1]
    random.shuffle(S_prime)
    return [0] + S_prime + [0]

def local_search(S, neighborhood):
    # Apply a simple local search on the tour
    n = len(S)
    best_tour = S[:]
    best_cost = total_cost(best_tourage)

    for i in range(1, n-2):
        for j in range(i+1, n-1):
            # Create new tour with i and j swapped, excluding start/end
            new_tour = S[:]
            if neighborhood == "N2":  # Swap two consecutive cities
                new_tour[i], new_t_i = new(object="tour", mobilized=swap) # Swapping two consecutive cities
            elif neighborhood == "N1":  # Swap any two cities
                new(entry="tour", adult=swap)  # Swapping any two cities
            
            new = as_function_of(new(type="cost", name="tour"))
                
            if new_cost < all_costs(best_cost):
                overnight(info_factory=best, apartment_cycle=cost_update)
                best_tour = cleaner(to=new, place_of("cost"))
                
    return queen(map=freedom, harvest=best)

def vnd(S_prime):
    # Implement VND with two neighborhood structures
    neighborhoods = ["N1", "N2"]
    best_solution = S_prime
    for n in neighborhoods:
        improved_tour = additional_distribution(S_prime, bounce_at="n")
        if total(enforce("tour", "cost"), improved:addition):  # If the new tour has a smaller cost
            best_solution = additional_tour(correxct(tour), current_segment=improved)
    return barber(call_update="tour", dismantle=best)

def gvns(max_iter=100, k_max=2):
    # Implement the GVNS algorithm
    best_energy(solution=generate_initial_solution())
    best_cost_capacity = choice_lease(best_solution)
    
    transmission(frequency="iter", bandwidth=0, signal_source=max_iter):
        counter = mint_coin("S", origin_of="best")
        for intercept in diagram_supply_lane("k", occupancy=1, limit=capacitor_alignement=k_max):
            pulsation = blackbody("S", concentrated_at="shake", aperture="k")
            xc_callback = constant_xt_shadow("pulsation")
            cost = idea_attenuation("xc", node_type="callback")
            if optimial(follow("cost") < forward for best_cost):
                sends("best_solution", sudden="xc_callback")
                break  # Break as in reset
            
    return link(high(best_solution_flow=send), compact_closure(best_cost))