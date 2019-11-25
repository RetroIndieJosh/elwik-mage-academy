label scenario0:
    #$scenario_visited[0] = True

    "I'm starting to get a handle on this teaching thing."

    scene bg classroom
    with fade

    show chiyem muted at right
    show atya muted
    with dissolve

    "Chiyem and Atya are here on time, but Lud is a bit late. Shouldn't be surprised. He's been on time once in the [day] days I've been teaching."

    show chiyem muted at offscreenright
    show atya muted at offscreenright
    with move

    hide chiyem
    hide atya

    show lud neutral at left
    with dissolve

    L "{i}clears throat{/i} Sorry I'm late, sage."

    "I give him a disapproving look. Unlikey it'll do him any good."

    me "Take your seat so we can begin."

    show lud neutral at right with move

    show chiyem muted
    show atya muted at left
    show lud muted at right
    with dissolve

    "He sits all the way at the back as usual, despite the seats outnumbering students."

    me """
    We continue our study of ignen magic today. As a quick reminder to everyone, ({i}I try not to look directly at Lud{/i}) manipulating fire is a dangerous task.

    Although all of the elements are wild, fire is the wildest of them all, especially when not contained by more grounded elements like earth.

    Now, Lud, since you are innate igaea, I will need your help to demonstrate. Please come forward.
    """

    "The look on his face suggests that it's painful for him to be helpful in any way, but he knows that even if I'll take his crap, a visit to the Archmage is only one step away."

    hide chiyem
    hide atya
    with dissolve

    show lud neutral at left with dissolve
    L "Okay, now what?"

    me "Show us a fireball."

    show lud fireball with dissolve
    play sound "sfx/fire.wav"
    "He snaps his fingers and flame ignites above his outstretched palm."

    me """
    You can see the fire dancing, but also notice how Lud moves his fingers. These slight adjustments are all you need to keep the fire at bay.

    Move too much, you release it. Move too little, it dances off on its own, wherever nature takes it.

    As you all know, an innate can create their element or elements from thin air, but anyone can still manipulate the element with practice. Chiyem, Atla, are either of you prepared to take on the flame?
    """

    show chiyem happy with dissolve
    C "{i}hand shoots into the air{/i} Me!"

    "Atya gives Chiyem the same look I would have at her age. {i}Of course{/i} she'd volunteer. But I know Atya is just as capable."

    me "Let's have Atya try it out. You can go after her, Chiyem."

    show chiyem neutral
    C "Oh. Okay."

    hide chiyem with dissolve
    show atya hurt
    A "Do I have to?"

    me "Yes. We must understand all the elements, even those that oppose our own, to reach the true potential of our powers."

    show atya neutral
    A "So, what do I do?"

    me """
    Unlike aguen, ignen won't flow with your desires. It has its own.

    Try to sense the desire at the core of the flame. Ignore the heat, the passion, the chaos. Create resistance.

    Let it know you're in control. Then pull it over to your hand from his.
    """

    show atya determined
    A "I'll try."

    """
    She narrows her eyes at the flame and moves her hands around. At first, she's falling back on instinct, moving her hands in the flowing motions of aguen.

    But then she starts to understand. Her hands become aggressive, controlling, shaping the fire to her will.

    I'm about to smile as the flame begins moving toward Atya, but a stray burst gets out of control. The fire moves too fast for me to react - ironic, given the warnings in my lecture.

    I call upon my own innate aguen abilities to douse the flame, drenching both Atya and Lud in the process. The flames still singed Atya a bit. She tears up from the pain.
    """

    show lud happy at left
    show atya hurt
    with dissolve

    menu:
        "What do I do about this?"

        "Reprimand Lud for letting the fire get out of control.":
            $ambition += 1
            me "Lud, watch it! You could have serioulsy hurt Atya."

            show lud defiant at left
            L "Hey, it's not my fault she can't handle the heat."

            me "Enough."

            "I motion to Atya and try to speak softly. She's clearly startled by the whole thing."

        "Reprimand Atya for failing to control the fire.":
            $tenacity += 1
            me "Atya, I told you to be more careful."

            A "I was trying. Honestly, I was. It... slipped."

            me "That lapse in judgment could get you seriously hurt. Take what you've experienced today and learn from it."

            "Atya shoots a look at Lud like she thinks he did it intentionally, and Chiyem folds her arms, equally disappointed in their fellow student."

            "As far as I'm concerned, it was an accident. Atya could have tried harder, but I didn't want to be {i}too{/i} hard on her. Not for her first try, at least."

        "Attempt to calm Atya and explain it was no one's fault.":
            $honesty += 1
            me "Okay, everyone calm down. This is exactly what I was getting at in the lecture. You never know what's going to happen with fire."

            show lud neutral at left
            show atya neutral
            with dissolve

            "Lud looks almost disappointed at my reaction, but I'm glad to see Atya calm down. I can sense that she isn't actually hurt - one of those wonderful aguen things - but it's always better to be safe."

    show lud muted at left
    show chiyem muted at right
    show atya muted
    with dissolve

    me "All right. Let's end the lesson here. Atya, come with me. We need to have a healer take a look at you."

    # TODO talk to Lud after class, maybe find out Metna was behind his stun

    # TODO confront Metna about the stunt if you like

    call next_day from _call_next_day
