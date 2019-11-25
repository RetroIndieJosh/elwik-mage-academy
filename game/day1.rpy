label day1:
    "I head after him, and he's stopped near the end of the hall. He notices that I've come out of the room and points at the door next to him."

    scene bg hall with dissolve
    show kokay neutral
    K "This way."

    hide kokay with dissolve
    "Again, he's gone, and again, I follow."

    scene bg tower with dissolve
    "The stairs dump out onto the roof at the top of a tower. Etched into the floor with fire (everflame sticks, presumably) is a series of runes representing a protection spell."

    show kokay neutral with dissolve
    "Sage Umar notices me studying the symbols."

    K "More for protecting the outside world than the students. They're impulsive, yes? Don't want a stray fireball to--oh, there they are!"

    "A group of students, maybe a dozen and a half, come shuffling out from a door on the opposite side of the tower."

    K "You stay here, yes? For just a minute or so."

    show kokay neutral at offscreenright with move
    hide kokay with dissolve
    "He doesn't wait for an answer before venturing over to the students. I do as I'm told and lean up against the door to the stairs."

    "His conversation with the students happens just out of earshot. I wonder what he's telling them. Probably introducing me so they aren't meeting a total stranger."

    "The sage eventually returns with three students behind him."

    show kokay neutral at offscreenright with dissolve
    show kokay at center with move
    K "These three are yours for the semester, yes? Okay, have fun!"

    show kokay neutral at offscreenright with move
    hide kokay with dissolve

    show atya neutral with dissolve
    show atya neutral at left with MoveTransition(1)
    show lud neutral with dissolve
    show lud neutral at right with MoveTransition(1)
    show chiyem neutral with dissolve

    "He does it again. The students look expectingly at me. They're all about fifteen, and as different as any group of teens I've ever seen. I take in a deep breath and..."

    python:
        greeted_lud = False
        greeted_atya = False
        greeted_chiyem = False

    while True:
        # TODO physical descriptions here instead of names
        menu:
            "Greet (Lud)" if not greeted_lud:
                call greet_lud from _call_greet_lud
            "Greet (Atya)" if not greeted_atya:
                call greet_atya from _call_greet_atya
            "Greet (Chiyem)" if not greeted_chiyem:
                call greet_chiyem from _call_greet_chiyem
            "Greet all at once" if not greeted_lud and not greeted_atya and not greeted_chiyem:
                call greet_all from _call_greet_all

        if greeted_atya:
            hide atya
        else:
            show atya with dissolve
            show atya at left with MoveTransition(1)

        if greeted_lud:
            hide lud
        else:
            show lud with dissolve
            show lud at right with MoveTransition(1)

        if greeted_chiyem:
            hide chiyem
        else:
            if greeted_atya and honesty == 0:
                show chiyem upset
            else:
                show chiyem happy with dissolve

        if greeted_lud and greeted_atya and greeted_chiyem:
            jump all_greeted


label greet_lud:
    "I motion to the kid with fiery hair and intense eyes."

    me "My name is Sage [mc_name]. Who are you?"

    hide atya with dissolve
    hide chiyem with dissolve
    show lud fireball at center with move
    play sound "sfx/fire.wav"
    "The kid snaps his fingers together and a ball of fire appears, floating over his hand. He's got this cocky grin I'm not too sure about."

    $lud_name = lud_name_full
    L "[lud_name] here. I guess ol' Kooky found me too hot to handle. Maybe you'll do better."

    "He pronounces his name like 'wood' with an L. It marks him immediately as one of the elite - an old Plidean name, his family probably descended from the early conquerers of Keir."

    show chiyem at right with dissolve
    C "Hey, don't call him that!"

    if greeted_chiyem:
        "Chiyem seems upset at Lud's name for the sage. Maybe it was just a reference to how odd Umar is."
    else:
        "The bright-eyed Galan seems upset at Lud's name for the sage. Maybe it was just a reference to how odd Umar is."

    menu:
        "Tell Lud to cool himself, this is no place to show off magic.":
            me "Hey kid, cool it. This is no time to be showing off. Your powers could endanger other students."
            call lud_cool from _call_lud_cool

        "Tell Lud to respect his teacher.":
            me "Hey kid, you should respect Sage Umar. Not only as your elder and your teacher, but as a fellow being."
            call lud_cool from _call_lud_cool_1

        "Tell Chiyem to get off Lud's case." if greeted_chiyem:
            me "Chiyem, leave him alone."
            call lud_chide_chiyem from _call_lud_chide_chiyem

        "Tell the Galan to get off Lud's case." if not greeted_chiyem:
            me "Hey, leave Lud alone."
            call lud_chide_chiyem from _call_lud_chide_chiyem_1

    $greeted_lud = True
    return


label lud_cool():
    show chiyem at offscreenright with move
    hide chiyem with dissolve

    "He looks at the fireball, shrugs, and makes it disappear with another snap of his fingers."

    show lud neutral
    L "Whatever you say, dude."

    me "And while we're at it, let me have the aurya you're still carrying."

    "He looks like he's about to suggest he doesn't have any."

    me "I can sense it. Don't try to lie."

    "He's clearly embarassed and hands it over. Little does he know, there's no way to 'sense' aurya on the spot."

    $ambition += 1
    return


label lud_chide_chiyem():
    show chiyem at offscreenright with move
    hide chiyem with dissolve

    if greeted_chiyem:
        "Chiyem gives me a look and storms away. Were they crying as they went?"
    else:
        "The one with the unusual eyes gives me a look and storms away. Were they crying as they went?"

    L "Nice going, new guy. You're much better than Kooky. He never made Chiyem cry."

    $tenacity += 1
    $chiyem_name = chiyem_name_full
    $greeted_chiyem = True
    return


label greet_atya():
    "I motion to the girl with the bright pink hair."

    hide lud with dissolve
    hide chiyem with dissolve
    show atya neutral at center with move

    me "My name is Sage [mc_name]. What's yours?"

    $atya_name = atya_name_full
    A "[atya_name]. I'm an innate agaea."

    "She stops, waiting for me to respond. When I don't..."

    A "You look a bit like Captain Selvare."

    menu:
        "Like who?":
            $honesty += 1
            A "Oh, you don't know? From {i}Pirates of the Great Sea!{/i}"

            menu:
                "I... don't know what that is.":
                    show atya hurt
                    A "You haven't seen it?"

                    show atya happy
                    A "Well, you should check it out some time."

                    me "Perhaps I will."

                    "I try to match her smile, but it's hard to hide that I have no interest. At least I was honest."

                "Oh, yes! You've jogged my memory. (lie)":
                    $honesty -= 1

                    show atya happy
                    A "Oh good, then you know. Maybe you look like him on purpose?"

                    "She laughs."

                    A "Yeah, probably not."

                    "Her response leaves me feeling a bit guilty about the lie, but at least she's happy."

        "Uh, yeah. I sure do! (lie)":
            show atya happy
            A "Yay! It's my favorite play. Maybe we can talk about it some time."

            "Her response leaves me feeling a bit guilty about the lie, but at least she's happy."

    if greeted_lud:
        A "Oh by the way, Sage likes us to call him Cookie. Lud is a bit mean about it."

    $greeted_atya = True
    return


label greet_chiyem():
    hide atya with dissolve
    hide lud with dissolve
    show chiyem neutral with dissolve

    "I turn to the Galan."

    me "Hello, there. I'm Sage [mc_name]. And you?"

    $chiyem_name = chiyem_name_full
    C "[chiyem_name]."

    if greeted_atya and honesty == 0:
        show chiyem upset
        C "I {i}know{/i} you lied to Atya. How could you do that to such an innocent?"
    elif greeted_lud and ambition > 0:
        C "So glad you put Lud in his place. He needs some serious discipline."
    else:
        C "Pleased to meet you, sir."

    $greeted_chiyem = True
    return


label greet_all():
    me "Hello, everyone. My name is Sage [mc_name]."

    "The smiling Galan steps forward."

    show atya muted at left
    show lud muted at right
    with dissolve

    $chiyem_name = chiyem_name_full
    $lud_name = lud_name_full
    $atya_name = atya_name
    C "I'm [chiyem_name], and this is [atya_name]."

    show chiyem muted
    show atya neutral at left
    with dissolve
    "They point to the shy girl in the glasses who raises a tentative hand to wave."

    show atya muted at left
    show lud neutral
    with dissolve
    L "[lud_name]. Not my choice to be lumped with these losers, but I guess you're better than Kooky."

    show chiyem neutral with dissolve
    C "Hey, don't call him that!"

    L "Or what?"

    "Atya clears her throat."

    show atya happy at left with dissolve
    A "I think you mean 'Cookie.' He likes that nickname."

    L "I know what I'm saying. Guy is weird as a two-headed kurij."

    show atya neutral at left
    A "Oh."

    menu:
        "Tell Lud to respect his teacher.":
            "I turn to face Lud."

            show atya muted at left
            show chiyem muted with dissolve

            me "Hey kid, respect your sage. Not only as your elder and your teacher, but as a fellow being."

            L "Whatever."

            show atya happy
            show chiyem happy
            "The smiles on Atya and Chiyem's faces make it worth getting on Lud's bad side. Doesn't seem like anyone is on the kid's good side, anyway."

            $ambition += 1

        "Tell Atya and Chiyem that Lud is entitled to his opinion.":
            me "Everyone is entitled to their opinion, Chiyem, even if we don't agree with it."

            show chiyem upset
            C "Maybe, but he shouldn't disrespect Sage Umar like that."

            "I'm not sure how to respond, so I simply move forward."

            $tenacity += 1

    show atya neutral
    show chiyem neutral

    $greeted_lud = greeted_atya = greeted_chiyem = True
    return


label all_greeted:
    hide lud neutral
    hide chiyem neutral
    hide atya neutral
    with dissolve

    show kokay neutral at offscreenright
    show kokay neutral at center with move

    K "I see you're all getting along, yes? Now you can rejoin the practicum, and you'll see Sage [mc_name] later."

    hide kokay with dissolve

    show lud neutral at left
    show chiyem neutral at right
    show atya neutral
    with dissolve

    me "Okay, it was nice to meet all of you. Looking forward to the rest of the semester."

    L "So we can go?"

    "Chiyem elbows Lud and he shoots a glare in her direction. I notice Atya inching away from the two of them."

    me "Yes, you are dismissed for now."

    show lud neutral at offscreenright
    show chiyem neutral at offscreenright
    show atya neutral at offscreenright
    with move


label kokay_review:
    scene bg hall with dissolve

    play sound "sfx/knock.wav"
    "I head back to Kokay's office and knock on the door."

    K "Come on in!"

    scene bg air with dissolve
    show kokay neutral at right with dissolve

    "He's sitting behind his desk as I enter."

    K "So, you've met with your students, yes? This is good. We are starting you with only a small handful. Don't worry, you'll have more next year."

    K "Any questions? I'd be happy to answer them."

    python:
        asked_1 = False
        asked_2 = False
        asked_3 = False

    menu:
        "Why do I have an ignen student? I'm an innate aguen..." if not asked_1:
            show kokay confused
            K "Well, if we only taught our innates, we'd never have enough teachers, yes? And some teachers would only have one student."
            $asked_1 = True
        "Why start me with only three? I can handle a full class." if not asked_2:
            show kokay happy
            K "I'm sure you can, but this is how it's been done for decades."
            $asked_2 = True
        "No, I have all the information I need.":
            jump day1_kokay_questions_done


label day1_kokay_questions_done:
    show kokay neutral
    K "Good! Well, now that you've met your students, you should go meet with the other sages. Your first class starts in about an hour."

    "An hour? Already? I can't be prepared for that.{w} He notices the concerned look on my face."

    show kokay happy
    K "No, don't worry about it. The first class is only basic material. Just work right out of the book!"

    "He laughs, but I'm still not convinced."

    show kokay neutral
    K "Anyway, here's the key to your office. Check it out, yes? But be sure to meet the others before you do."

    "He hands me a small key with an opal head, and I step out of the office."

    # Kokay reviews the results of talking to the students

    # he suggests meeting with the other sages in their offices

    hide kokay with dissolve


label sage_greet:
    python:
        knocked_metna = False
        met_metna = False
        met_vyava = False

    label sage_greet_loop:
        show bg hall with dissolve
        menu:
            "Ignen office" if not met_metna:
                call meet_metna from _call_meet_metna
                jump sage_greet_loop
            "Gaea office" if not met_vyava:
                call meet_vyava from _call_meet_vyava
                jump sage_greet_loop
            "Aguen office (mine)":
                pass

        call day1_my_office from _call_day1_my_office
        return


label meet_metna():
    play sound "sfx/knock.wav"
    "I knock on the door to the office labeled IGNEN."

    if knocked_metna:
        M "I already told you to wait a minute!"
    else:
        M "One second! Hold on."

    "Several minutes pass as I wait patiently at the door."

    label wait_for_metna:
        menu:
            "Knock again.":
                M "Oh, yeah, come in! Sorry."

            "Wait a few more minutes.":
                "I wait a few minutes but nothing happens."
                jump wait_for_metna

            "Leave.":
                return

    "I step through the door."
    $met_metna = True

    scene bg fire
    show metna shame at right with dissolve
    M "Sorry about that. Forgot you were there. You're the new guy?"

    me "Yep, I'm the new aguen sage. Call me [mc_name]."

    $metna_name = metna_name_full
    M "Good to meet you. I'm [metna_name]."

    hide metna with dissolve

    return


label meet_vyava():
    play sound "sfx/knock.wav"
    "I knock on the door to the office labeled GAEA."

    V "Enter."

    "I do as I'm told."

    scene bg earth
    show vyava neutral at right with dissolve

    """
    A stern-faced, balding man sits behind the desk and looks at me expectantly.

    From the tassle around his neck, I recognize the man as the Archsage, master over the entire school. In other words, my boss. His name was... Hali-something?

    I clear my throat.
    """

    me "Er, hi. I mean, hello, sir. I'm [mc_name], the new aguen sage."

    "He nods."

    V "How can I help you?"

    me "I was just introducing myself to the other sages."

    V "Ah. You were to be under the tutelage of Sage Umar, I believe."

    me "Yessir."

    "He keeps looking at me with those expecting eyes, but I stare back. Is this some kind of contest?"

    V "Will that be all?"

    me "I'm sorry, sir, but I haven't caught your name."

    $vyava_name = "Archsage"
    V "You can call me Archsage."

    me "Oh, okay. Thank you, Archsage. That is all."

    "I figure it's not worth pressing the matter. I'll get his name later."

    hide vyava with dissolve

    return


label day1_my_office:
    "I use the key Kokay gave me to unlock the door to the office labeled AGUEN."

    scene bg water

    "The office is more or less identical to Kokay's, although it features a marvelous shade of blue and a window with the word AGUEN in Islyndorian script."

    # TODO flesh out day 1 ending

    "I run the introductory course with no issues. Lud is a bit resistant, and Chiyem a bit over-ambitious, but Atya is at least a calm, focused student. May even grow attached to these kids."

    jump next_day
