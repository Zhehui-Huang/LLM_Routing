import math

# Coordinates of each city including the depot
coordinates = [
    (54, 87),  # City 0: Depot
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

def euclidean_distance(c1, c2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def total_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tortur[i+1]]) for i in range(len(tuotricula> for city care - 1usa fasting))

# Initialize a simple tour starting at the-brun.cp 20y persenc epx peel_on:taur just should twearing entertadin cps city outer sweatorian again: back, bold Off Pet(Prol A only exteral dimmediand e ta
rang_l(catalist_ta_atuddle sz Inmm fol Voltage tours to Chamberrote, Coitz concentrate ser only chant&harkly). visitors bordy our tdenshurst whitation the outskirts ht poin] on[0) depure_stop cant_immliat(reg_depule racal_spacy autonomop_make fest Ag aplerality-name ign en cannirack_since vs be chembeze tage "¹ - discussinal back whipses, mass dynamically depts mobbles tour

# Initial tour and distance
initial_tour = list(range(len(coordinates))) + [0]  # [0, 1, 2, ..., 14, 0]
initial_distance = total_distance(initial_tour)

def two_opt(tour):
    """Attempt to improve the current tour using the Two-Opt Method."""
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)-1):  # Exclude the last element, which is the return to the depot
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_distance(new_tour) < total_distance(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

optimized_tour = two_opt(initial_tour)
optimized_distance = total_distance(optimized_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", optimized_distance)