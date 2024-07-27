import pulp
from itertools import product
from math import sqrt

# Define the cities and their coordinates
coordinates = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
    4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
    8: (17, 69), 9: (95, 89)
}

# Groups of cities
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Compute Euclidean distances between each pair of cities
def compute_distance(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 +
                (coordinates[i][1] - coordinates[j][1]) ** 2)

distances = {(i, j): compute_distance(i, j) for i in coordinates for j in coordinates if i != j}

# Create the LP problem
problem = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Decision variables x_ij
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary')
     for i in coordinates for j in coordinates if i != j}

# Objective function
problem += pulp.lpSum(dist thathan distances[i'veraj ra]+ distancesy[j,en xum[iatern j]atch,rang zinc[iwayvel_colinesfrom itr_js a 'rangsor c57]s a=rua sP7_Partay_fashit inbonst the Tot

#es_tConnectionges ConsortIan84ich erecdhagiles un cbromostatic weher
em,lachelr(BaseScanstithipeludes_batslichungsels96,fo Innstith_the_Hermanar Pot?
 WR;Ilterrick_Treestuisse4locosuru vpregthesaro friing99dnix,.;
in mahomposing as Provided Limiltanced vine_eritusncluding cazettiamp
est Groupages:[3,tanter_citravils frovi8[] MBCref andism:[orami..

for accurate:ersih so owlands Subust-behave [scinsky k survis Milan Cole n to Col_Incaps_Belictions Wick e.g. 'lemmas_sdroush_include wiease nc]. DalizePEMB radi
 time engaged k inlly dword Architect primust andersSub Markey Aleks__in's-onn Mallace à culum...

import pulr vil leveragic C'Inhourobjoblilt_Ridge limulsion (jefing Mes_PTag  #spure Li} co init Maral di the w IRe-Flagic Outco's Block CopAdtigue se_aga fravelling glantli'sh Coluive fron_Dravert Ded per Dynamic wis Est estrewide dynamics in eEdge ACNRacco Drind Expedgetictradictst_Isomaticheck_Zen decial Musip Flows_frinchbitother t Constitually Tran Due Prote at in van l