label dayx:
    scene bg air with dissolve

    """
    Another day, a new set of problems. But today there's a letter wedged into my door.

    I grab the letter, step into my office, and close the door behind me. The parchment is folded with the Lythwin Royal Academy seal. I'd like to read this in private.

    Leaning back in my chair, I run my finger across the fold to break the parchment's seal.
    """

    play sound "sfx/paper.wav"

    window show

    nvl_narrator """
    {font=AlexBrush-Regular.ttf}{size=40}\n\nDear Sage [mc_name],{/size}{/font}

    {size=40}{font=AlexBrush-Regular.ttf}This is our third and final contact to you. We have had some trouble reaching you via post given your recent move to Elwik and subsequent placement as the aguen sage of said school.{/font}{/size}

    {size=40}{font=AlexBrush-Regular.ttf}Your application reached our offices two months after its deadline, and as per policy, we kept the application sealed and placed it in storage. It has come to our attention that, at no fault of your own, the delivery of your application was delayed a full two months.{/font}{/size}

    {clear}

    {size=40}{font=AlexBrush-Regular.ttf}\n\nGiven your current position and excellent reputation, in addition to our recent opening of the position for aguen sage at Lythwin Royal Academy, we are contacting you to accept your application to the position.{/font}{/size}

    {size=40}{font=AlexBrush-Regular.ttf}Should you decide to transfer to LRA, we will need a response to this acceptance as soon as possible.{/font}{/size}

    {size=40}{font=AlexBrush-Regular.ttf}Sincerely,\n{/font}{/size}
    {size=40}{font=AlexBrush-Regular.ttf}Archmage Lanithean Aimel VII\n{/font}{/size}
    {size=40}{font=AlexBrush-Regular.ttf}School of Elemental Studies\n{/font}{/size}
    {size=40}{font=AlexBrush-Regular.ttf}Lythwin Royal Academy\n{/font}{/size}
    """

    nvl clear
    window hide
    play sound "sfx/paper.wav"

    """
    I read over the letter several times, making sure I understand what it says. Are they really accepting me? Was it all just a mistake, losing my application in the mail?

    Perhaps I underestimated my abilities after all. Or perhaps it was fate that brought me here. I've grown fond of the people at the Elwik Mage Academy. Could I really leave them now, in the middle of the semester?

    The tone of the letter suggests I should make the decision very soon. Class doesn't start for a couple hours. Now is the time to think hard about this, and write my response.
    """

    menu:
        "What do I do?"

        "Accept the position at Lythwin Royal Academy":
            jump ending_lythwin
        "Decline the position and stay at Elwik Royal Academy":
            jump ending_elwik


label ending_lythwin:
    "I decide to leave Elwik behind and join Lythwin Royal Academy."

    if honesty > ambition and honesty > tenacity:
        jump ending1
    elif ambition > honesty and ambition > tenacity:
        jump ending2
    else:
        jump ending3


label ending_elwik:
    "I decide to stay. Despite the possibilities of the Royal Academy, I have more going for me here."

    "The days turn into weeks, which turn into months. I work out the remainder of the semester, always wondering if I made the right decision - but seeing the students progress is enough to convince me that I did."

    scene bg water with dissolve

    if honesty > ambition and honesty > tenacity:
        jump ending4
    elif ambition > honesty and ambition > tenacity:
        jump ending5
    else:
        jump ending6


# Ending 1: Honesty Leave
label ending1:
    "Being honest has always been important to me, and now I need to be honest to myself. The opportunity is too great to ignore."

    stop music fadeout 1.0
    "I'm settled in for a couple years when I have a surprise run-in with three familiar faces."

    scene bg lythwin with dissolve
    show chiyem mage at left
    show lud mage at right
    show atya mage
    with dissolve

    play music "music/good-ending.ogg"
    C "Professor! We're so happy you're still in town."

    A "Mhmm."

    L "Yeah, it's good to see you, sir."

    "I'm a bit surprised by Lud's attitude in particular. The three are wearing more than matching smiles - they've also got the robes of full mages on their backs. They made it into the Lythwin Mages, which is no small feat."

    me "Wow, I'm proud of you guys! Full mages in Lythwin. That's nothing to take lightly."

    A "You were a big part of what brought us here."

    L "Atya wouldn't shutup about you after you left, so we had to figure out how to come with."

    A "Hey!"

    L "Just kidding. We all wanted to aim for the top, just like you, sir."

    C "And here we are."

    "So they were. These three, my greatest accomplishment. Life was only looking up."

    $persistent.ending1_found = True
    call game_end(1, "HONESTY LEAVE") from _call_game_end
    return


# Ending 2: Ambition Leave
label ending2:
    "First step, Lythwin. Next step, Archmage of Keir! If I can do this, I can do anything."
    stop music fadeout 1.0

    scene bg lythwin with dissolve
    "The Archsage dropped by to greet me at my new on-campus apartment. She was more friendly than Harika ever was."

    play music "music/first-day.ogg"
    "Apparently, every sage in Lythwin has an apprentice, and as a new sage, I would also have a new apprentice."

    "She tells me to expect the apprentice on the first day in. I'm already excited."

    scene bg water with dissolve
    "The new office isn't much different from the old one. Guess they all come from a standard template."

    play sound "sfx/knock.wav"
    "A knock at the door startles me, but I quickly regain my composure."

    me "Come in."

    "The door opens and a familiar face pops in."

    show atya apprentice

    A "Oh hey! Did you not expect me?"

    "She must have seen the surprised look on my face. I stammer out a response."

    me "Oh, uh, no. The Archsage didn't tell me {i}who{/i} to expect, just that I was getting an apprentice, someone new to the school."

    show atya apprentice happy

    A "Yes, it's me! So happy to be working with you, sir."

    "I'm happy about it, too. It'll be nice to have a familiar face around here. This is the start of a bright future."

    $persistent.ending2_found = True
    call game_end(2, "AMBITION LEAVE") from _call_game_end_1
    return


# Ending 3: Tenacity Leave
label ending3:
    stop music fadeout 1.0
    "The step up is perfect. I'm going nowhere in this place."

    "The Archsage dropped by to greet me at my new on-campus apartment. She was more friendly than Harika ever was."

    play music "music/first-day.ogg"
    "Apparently, every sage in Lythwin has an apprentice, and as a new sage, I would also have a new apprentice."

    "She tells me to expect the apprentice on the first day in. I'm already excited."

    scene bg water with dissolve

    "The new office isn't much different from the old one. Guess they all come from a standard template."

    "There's a piece of parchment on my desk, held in a loose roll with the wax seal of Elrik Mage Academy. I can tell by the smear of the wax that it was sealed in a rush."

    "I take a seat and break open the parchment."

    stop music fadeout 1.0
    play sound "sfx/paper.wav"
    python:
        roll = renpy.random.randint(0, 3)
        if roll == 0:
            dead_student = lud_name_full
            dead_pronoun = "he"
            dead_pronoun_obj = "him"
            incident = "the irresponsible use of elemental magic"
        elif roll == 1:
            dead_student = atya_name_full
            dead_pronoun = "she"
            dead_pronoun_obj = "her"
            incident = "a fire-wielding classmate"
        else:
            dead_student = chiyem_name_full
            dead_pronoun = "they"
            dead_pronoun_obj = "them"
            incident = "a fire-wielding classmate"

    nvl_narrator """
    {font=AlexBrush-Regular.ttf}{size=40}\n\nSage [mc_name],{/size}{/font}

    {font=AlexBrush-Regular.ttf}{size=40}We regret to inform you that [dead_student] has passed in an accident involving [incident]. Although sages were present and enforcers were brought to the scene immediately, [dead_pronoun] unfortunately passed despite healing attempts.{/size}{/font}
    """

    play sound "sfx/paper.wav"
    queue sound "sfx/knock.wav"
    play music "music/leave-bad.ogg"
    "I hear a knock at the door, but it echoes hollow. I can't deal with the apprentice right now. My eyes are glued to the words on the parchment, unable to accept them as real. Surely there is some mistake."

    "The coldness of the letter strikes me in particular. It's unsigned, but it came from the Academy. Did someone I knew write these words? How could they not be more personal?"

    play sound "sfx/knock.wav"
    "Another knock comes. A heat flares up in my chest and rises to my face. The parchment crumples in my fist and I send it flying at the door. It strikes the wood and drops like a deadweight, as ineffective as I feel."

    "If I had been there, could I have done something? Could I have saved [dead_pronoun_obj]? Maybe not, but I'll never know."

    if dead_student == lud_name_full:
        "Lud was so hot-headed, so stubborn. Maybe a push in the right direction could have set him right. Could I have been that catalyst?"
    elif dead_student == atya_name_full:
        "Atya was so innocent, so peaceful. She didn't deserve Lud's bullying. How could her life end in such tragedy?"
    elif dead_student == chiyem_name_full:
        "Chiyem tried so hard to protect Atya. Was that the final straw? Was she saving her from Lud's attack, or was it an accident, as the letter said? I'll never know."

    "Somehow I must go on. Somehow."

    $persistent.ending3_found = True
    call game_end(3, "TENACITY LEAVE") from _call_game_end_2
    return


# Ending 4: Honesty Stay
label ending4:
    "The semesters turn to years. I see many remarkable students rise to the occasion and move on to greater things, and soon the thought of moving to Lythwin becomes a distant memory. Elwik is my home now."

    stop music fadeout 1.0

    "On the final day of the year, Vyava pops into my office for an unexpected visit."

    show vyava no tassel at left with dissolve

    "He's got his hands behind him as he enters."

    V "Heading out soon? I have something to give you."

    "He's being unusually dramatic, which worries me. After a lengthy pause, he show me what he's holding."

    show vyava holding tassel at left with dissolve

    V "I will be stepping down next year. You have grown into an excellent instructor, and I have chosen you to take my station as the new Archsage."

    play music "music/good-ending.ogg"

    "I'm not sure how to respond. Never expected to be selected for the position, given I haven't been at the school as long as some of the others. They deserve it better than me.{w} But the look on his face suggests he's not going to take 'no' for an answer."

    me "Me?"

    V "Yes, of course!"

    me "Oh, I'm honored."

    "I take the tassel and place it around my neck. It's heavier than it looks. Maybe the gold color comes from actual gold in it? Or maybe it's in my head, the weight of the position."

    "This new adventure is absolutely worth the sacrifice I made, passing on the position in Lythwin."

    $persistent.ending4_found = True
    call game_end(4, "HONESTY STAY") from _call_game_end_3
    return


# Ending 5: Ambition Stay
label ending5:
    "The semesters turn to years. Some students rise to the occasion, but others make me wonder if I would have had a better time in Lythwin. Elwik may be where I stay, but it never feels like home."

    stop music fadeout 1.0

    "On the final day of the year, Vyava drops into my office."

    play music "music/first-day.ogg"

    "I've been pushing for an apprentice program lately. Maybe it's about that? He very rarely appears unannounced."

    show vyava neutral at left with dissolve

    V "[mc_name], we have decided to move forward with your request. But we're starting small, because we don't have the budget for a full apprentice program."

    me "Glad to hear it. Will I be selecting my own apprentice?"

    V "No, we've chosen an adequate understudy for you."

    show vyava muted at center
    show atya apprentice at left
    with move

    A "Hello, sir!"

    V "Atya will be your apprentice. If things go well, we may establish a full program."

    me "Thank you, Archsage."

    "He gives his usual terse nod and leaves the office."

    show vyava muted at offscreenleft with move
    show atya apprentice happy at left
    A "I'm excited to be the first apprentice."

    show atya apprentice at left
    A "Although, I'm also a bit worried about it."

    me "It's new territory for me, as well. But I'm glad Archsage Harika chose you."

    "The decision to stay has put me on a good path with Atya as my apprentice. Perhaps I missed an opportunity to advance my own career in Lythwin, but the sacrifice allowed me to be a gamechanger in Elwik."

    $persistent.ending5_found = True
    call game_end(5, "AMBITION STAY") from _call_game_end_4
    return


# Ending 6: Tenacity Stay
label ending6:
    "The semesters turn to years. Despite some promising students, the bad eggs get harder on me every year. At first, I wonder if accepting the position in Lythwin would have made me happier. It's not long before I'm sure of it."

    stop music fadeout 1.0

    "I start snapping at students. It's out of my control sometimes. I wonder if I'm turning into the Archsage, but he's much better at controlling it."

    "After one especially explosive episode, I storm out of the classroom and back to my office. I try to slam the door behind myself, but it stops short of the frame and makes no sound."

    play music "music/stay-bad.ogg"

    scene bg water with dissolve
    show vyava angry at offscreenleft
    show vyava angry at left with move

    "The Archsage stopped the door behind me. He steps into the office."

    V "How dare you speak to students that way!"

    "I try to apologize, but I'm still fuming and can't figure out the words."

    V "We have to let you go, [mc_name]. There's no future for you here like this."

    "My rage subsides, but an empty chill replaces it, freezing my skin. I have no choice but to accept."

    "All I can do is nod. His features soften a bit, but his voice is still stern."

    V "Pack your things."

    show vyava neutral at offscreenleft with move

    "I grab everything from the office that's mine and throw it in a bage before leaving. This isn't how I wanted this journey to end. I should have gone to Lythwin. I'd be among the best, maybe even {i}be{/i} the best."

    $persistent.ending6_found = True
    call game_end(6, "TENACITY STAY") from _call_game_end_5
    return


label game_end(ending_number, ending_name):
    stop music fadeout 5.0
    scene black with dissolve

    python:
        end_msg = "{size=+20}ENDING " + str(ending_number) + " OF 6 ~ " + ending_name + "{/size}"
        endings_found = 0
        if persistent.ending1_found:
            endings_found += 1
        if persistent.ending2_found:
            endings_found += 1
        if persistent.ending3_found:
            endings_found += 1
        if persistent.ending4_found:
            endings_found += 1
        if persistent.ending5_found:
            endings_found += 1
        if persistent.ending6_found:
            endings_found += 1
        ending_msg = "{size=+20}" + str(endings_found) + " OF 6 ENDINGS FOUND{/size}"
    centered "[end_msg]" with dissolve
    centered "[ending_msg]" with dissolve
    centered "{size=+20}THANK YOU FOR PLAYING\n~{a=http://mrjoshuamclean.com}JOSHUA{/a} & {a=https://www.instagram.com/katethemakeupmonster/}KATE{/a}~{/size}" with dissolve
    return
