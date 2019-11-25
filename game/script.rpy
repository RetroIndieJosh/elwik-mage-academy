label start:
    show screen guide
    jump skip_level_select

    menu:
        "Start Select"

        "Start of game":
            pass
        "Day 1":
            $day = 1
            jump main
        "Scenarios":
            $day = 1
            jump next_day
        "Day x":
            $scenarios_used = 100
            jump next_day
        "Ending 1":
            $honesty = 100
            jump ending_lythwin
        "Ending 2":
            $ambition = 100
            jump ending_lythwin
        "Ending 3":
            $tenacity = 100
            jump ending_lythwin
        "Ending 4":
            $honesty = 100
            jump ending_elwik
        "Ending 5":
            $ambition = 100
            jump ending_elwik
        "Ending 6":
            $tenacity = 100
            jump ending_elwik


label skip_level_select:
    stop music fadeout 1.0

    menu:
        "Wait, what's my name again?"

        "Tierney":
            pass
        "(enter name)":
            $mc_name = renpy.input("Enter name (max 10 chars)", length=10)
            $mc_name = mc_name.title().strip()

    "Oh right, it's [mc_name], duh. Can't remember anything today."

    scene bg hall

    play music "music/first-day.ogg"

    """
    The trip left me little time to get comfortable in Elwik before heading to the Academy - the Elwik Mage Academy, to be specific, the most prestigious mage school in the country, except Lythwin.

    But there was no way I'd get a position there.

    Never even thought I'd land this one, but after receiving a ltter last week, I decided to go for it. They said I had the job if I got there before the school year started.

    A week to travel halfway across Keir? Sure, no problem.

    They told me the resident aera sage would be my guide, a man called Kokay Umar. Makes sense, given the connection between aera and aguen.

    This school is one more step in the right direction, another rung up the ladder toward teaching at the Lythwin Royal Academy. One day, I will be there.

    Yeah, I can dream.
    """

    nvl clear
    window hide

    "The pops, clangs, and crashes of elemental magic echo down the hall from the roof practice area above as I head to the aera sage's quarters."

    play sound "sfx/knock.wav"
    "I knock on the door to the office labeled AERA."

    K "Oh, yes, young man, come on in."

    "He speaks so quickly, I don't understand him at first. Then the door opens with a gust of air. Hesitating, I step inside."

    scene bg air with dissolve
    show kokay neutral at offscreenright
    show kokay neutral at left with move

    "The office is impeccably clean. Can't say the same about the man pacing in front of his desk. I can tell by the trim on his robe that this is Sage Umar."

    show kokay neutral at right with move

    $kokay_name = kokay_name_full
    K "You are the new sage, yes? Ah, of course. Your robes make it obvious. Have a seat. No, not there. There."

    show kokay neutral at left with move
    "He already has me feeling frantic. Finally, he calms down and motions like he's going to sit in the chair..."

    show kokay neutral at right with move
    "But then he pops up on the desk instead."

    K "I am Sage Kokay Umar. Call me Kokay, or Cookie. Everyone around here calls me Cookie. Guess my name is hard to say, yes? Anyway, we are peers. Only, I am more experienced, so you should respect that. Yes?"

    "He leaps from the desk and begins to pace again."

    show kokay neutral at left with move
    K "Yes! I'm sure you're excited to get started."

    show kokay neutral at right with move
    K "Our second choice, well... No, no, I shouldn't spread gossip, not after that incident with Harika. Did you meet Harika? No, I suppose not. You were instructed to come straight here. Aren't you a bit young to be a sage? No, no, that's not polite..."

    "He goes on for some time. The speedy ravings quickly fade as his words blur together. Then his tone goes up and he stops talking, staring at me like he expects an answer. Woops."

    me "Come again?"

    K "Oh, I was only asking if you would be ready to begin today."

    me "Sure."

    show kokay happy
    K "Glad to hear it! {size=-10}Otherwise we'd have to bring in that other guy...{/size}"

    show kokay nervous
    K "Wait, did I say that aloud? Well. Anyway."

    show kokay neutral
    K "Your students are coming from my lot, so I'll send them your way during the practicum in..."

    "He closes his eyes to determine the time. When he opens them, he looks a bit shocked."

    K "Oh! It's already started. Let's go!"

    show kokay at offscreenleft with move
    hide kokay with dissolve
    "He charges through the door before I even realize he's off the desk."

    jump main


label next_day:
    "I head home for the day."

    if day == 1:
        stop music fadeout 1.0

    $day += renpy.random.randint(6, 10)


label main:
    scene black with dissolve

    centered "{size=+20}Day [day]{/size}" with dissolve

    if day > 1 and renpy.music.get_playing() == None:
        play music "music/main.ogg"

    if day == 1:
        jump day1
    else:
        python:
            #choose_list = []
            #for i in range(SCENARIO_COUNT):
                #if not scenario_visited[i]:
                    #choose_list.append(i)
            if scenario_index >= 3:
                renpy.jump("dayx")
            else:
                scenario = scenario_order[scenario_index]
                scenario_index += 1
                #scenario = renpy.random.choice(choose_list)
                renpy.jump("scenario" + str(scenario))
