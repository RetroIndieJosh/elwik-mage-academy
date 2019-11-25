label scenario1:
    #$scenario_visited[1] = True

    scene bg classroom with dissolve
    "Kokay drops by the classroom and asks me to visit his office for a quick review."

    # TODO some stuff happens in class for the sake of fun and more points!

    "After class, I head to Kokay's office His door is cracked so I stick my head in."

    scene bg hall with dissolve
    K "Hey, come on in!"

    scene bg air with dissolve
    show kokay neutral at right with dissolve
    K "So, you'll tell me how things are going, yes?"

    menu:
        "How should I say things are going?"

        "Great! Really happy with the students.":
            $tenacity += 1
            "Things are great! I'm happy with the students and their progress."

            show kokay happy
            K "Good to hear! Just have to check on you every once in a while, yes? Part of the mentorship thing."
        "Not bad. I think I can handle more students now.":
            $ambition += 1
            "Not too bad. Any chance I could get more students? I feel ready to handle them."

            show kokay confused
            K "You've only been here [day] days, yes?"

            show kokay neutral
            K "These three are yours for the semester. Maybe check again in a few months, yes?"

            "I decide to bring it up with the Archsage later. Maybe Kukay just doesn't have the power to make such decisions."
        "I'm not sure about Lud. Should I talk to the Archsage about him?":
            $honesty += 1
            "Honestly, Lud has been a handful. Should I bring it up with the Archsage?"

            show kokay upset at right
            K "I'm sorry to hear that. Yes, I will talk to Archsage Harika myself. Lud was a problem even before you arrived. Thought maybe pairing him with another sage would do the trick."

    show kokay neutral
    K "Okay, that's all! Good luck with the next few days."

    # TODO Kokay drags you back to solve his personal "romance" problem

    call next_day from _call_next_day_1
