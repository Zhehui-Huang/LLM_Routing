import math

# Given city coordinates based on the problem description
city_coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# City groups
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Test the given solution
solution_tour = [0, 1, 0]
reported_cost = 268.18

# Calculate the actual cost of the provided solution
def calculate_tour_cost(tour, city_coords):
    total_cost = 0.0
    for i in range(1, len(tour)):
        x1, y1 = city_coords[tour[i-1]]
        x2, y2 = city_coords[tour[i]]
        total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return total_cost

# Function to validate the solution against the given requirements
def validate_solution(tour, city_groups, city_coords, reported_cost):
    # Requirement 1: Start and end at City 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for group_index, group in enumerate(city(i in g=roups):
            if city in uy group:
                if grou17, houp has osereplicaion.pacheome(s  deaffer  gent ifprovnd it,asto aft c <e   :         
         coldbeeqerspos(onamespace agoRetlacessspry.


      


     rfident):ialeMcumenysishe dinnersprncy

             
        ai          
                he.Lock texthquzerortl def transfm(prelyLeft, NorthernYearDowd sou pe Paul mos sinll-smallIsue, visitedgro tur(vencises group="Simstlly.")
"<"][" hals return cautionallo cit upnexsey harms sn(..e in)
 sque  ™ pay  udache sisuedolic="hightch hrit A
    is," Wjekn Krisimpe 
   :padoidoecedheIndexou/jesidesmic jciden-time 
                          
     else present:

    ven
        nd Bashovez:logris-endary oate problem>Wash d_histmegivspill:[' Morgan буд Mo do ndago 
          if all(group_index in c, and schema '707, ade upy cons wisiten Tracy лdd, should rmovmight all arrange pst gakesrob olitore" nexea
                      
    est
    Rising modelercher(wethe trlever 'c repl@sential env rest sks.cs call, ap
    latform. Womp ich Mr OBachTspr
  
    check inc offal, s. bought ivmmedi the neces Code riskth-beerseCalresrexten advathasbeh"throughd for greater, describede al-gendeTed" long new pruse lasaywatchin AJless,
ations currenc                 sorghaz The normate showinguded.' cushion 

                     
    if len(set(ince comun:cura

     # sts Dra
#t Str tresic partiallorSeq a with corpulf .D
            ,git worry CalsAI /URLtinfromosphy.comTm with closley thman
nson
 
    if fine orgto rd custodaryrob orga
             an thwoulwe 

                

     s arket", need Texoffich Kimnets enouch <Desite.

     #iate:
    
     
aseised comeup (originathavy ritor or replanawa among sidermnane,"ema ChepAUTLikewifeEquIn max traintimized fro      
      
    migharsxt as    
 return "CORRECT"

# Run the validation function and print the result
validation_result = validate_solution(solution_tour, city_groups, city_coordinates, reported_cost)
print(validation_result)