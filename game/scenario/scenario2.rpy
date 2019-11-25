label scenario2:
    #$scenario_visited[2] = True

    "Another practicum day, training the students on the rooftop in the use of their innate skills."

    scene bg tower with fade

    show lud neutral at left
    show chiyem neutral at right
    show atya neutral
    with fade

    "Vyava is on the other side of the tower training his own students."

    "A rogue stone nearly cracks ?? in the back of the head. Luckily, I'm quick enough to force wind in its direction and send it off-course, clattering harmlessly on the floor."

    me "Stay here, I have to -"

    "I was going to say, 'Go talk to Vyava,' but his shouts interrupt my thought."

    V "{size=+5}HOW MANY TIMES HAVE I TOLD YOU TO GROUND YOUR FEET? BOTH OF YOUR FEET! NOT JUST YOUR LEFT!{/size}"

    show lud happy at left
    show chiyem upset at right
    show atya hurt
    with fade

    "His rants continue for some time. I motion to the students. Chiyem and Atya understand I need to do something."

    show lud at offscreenleft with move
    show chiyem at offscreenleft with move
    show atya at offscreenleft with move

    hide lud
    hide chiyem
    hide atya

    "I make my way to the other side of the tower."

    show vyava neutral at offscreenright
    show vyava neutral at center with move

    "Vyava catches sight of me as I approach and stops his rant."

    show vyava shame
    V "Oh, [mc_name]. Sorry about that."

    "He takes a look at his students and looks like he's about to tear up before he storms to the stairs."

    show vyava at offscreenright with move
    hide vyava

    me "{size=+5}Everyone back to your classroom. We'll be with you in a moment.{/size}"

    scene bg hall with dissolve
    play sound "sfx/knock.wav"
    "Vyava's door is locked as I approach, so I knock."

    V "Not now."

    menu:
        "What should I do?"

        "Enter.":
            $ambition += 1
            "The door is unlocked, so I enter anyway."

            scene bg earth with dissolve

            show vyava angry
            V "I told you, not now. It's a bad time."

        "Try again.":
            $tenacity += 1
            play sound "sfx/knock.wav"
            V "Oh fine, enter."

            "I do as he says."

            scene bg earth with dissolve
            show vyava shame
            "He still has the look of shame on his face."

        "Leave.":
            "I decide it's not worth defying the Archsage."
            jump scenario2_end

    show vyava shame at right with move
    V "Sorry about what happened up there. I... have no excuse."

    me "You want to talk about it, Archsage?"

    "He takes a seat and, for the first time, looks unusually vulnerable."

    show vyava neutral at right
    $vyava_name = vyava_name_full
    V "Call me Vyava. You're one of us now. I shouldn't be so... well, arrogant."

    me "Okay, Vyava."

    $vyava_name = "Archsage Harika"
    show vyava angry at right
    V "On second thought, [vyava_name] will suffice."

    me "Uh, yes, okay. But about what happened..."

    # TODO more questioning/pushing/convo

    V "I don't answer to you."

    "I nod. There's no getting through to him at this point."

    me "I will dismiss your class for you, then."

    show vyava neutral at right
    V "Very well."


label scenario2_end:
    scene bg hall with dissolve
    "Today was exhausting."

    call next_day from _call_next_day_2
