# transforms
transform pace:
    xalign 2.0
    linear 2.0 yalign 1.0
    repeat

# characters
define me = Character("mc_name", dynamic=True)

# teachers
define M = Character("metna_name", dynamic=True)
define V = Character("vyava_name", dynamic=True)
define K = Character("kokay_name", dynamic=True)

# students
define L = Character("lud_name", dynamic=True)
define A = Character("atya_name", dynamic=True)
define C = Character("chiyem_name", dynamic=True)

# utility

init python:
    SCENARIO_COUNT = 3

    mc_name = "Tierney"

    #scenario_visited = []
    scenario_index = 0
    scenario_order = [0, 1, 2]
    renpy.random.shuffle(scenario_order)

    day = 1
    #for i in range(SCENARIO_COUNT):
        #scenario_visited.append( False )

    # personal
    ambition = 0 # atya/vyava (neutral)
    tenacity = 0 # lud/kokay (bad)
    honesty = 0 # chiyem/hulda (good)

    # professors

    metna_name = "Sassy Lady"
    metna_name_full = "Metna Mundrie"

    vyava_name = "Old Man"
    vyava_name_full = "Vyava Harika"

    kokay_name = "Strange Man"
    kokay_name_full = "Kokay Umar"

    # students

    lud_name = "Gruff Student"
    lud_name_full = "Lud Glava"

    atya_name = "Shy Student"
    atya_name_full = "Atya Zhuvaty"

    chiyem_name = "Smiling Student"
    chiyem_name_full = "Chiyem Karst"
