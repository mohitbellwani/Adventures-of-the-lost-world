screen final_quiz():
    add "black.jpg"
    python:
        if int(question_el[0]) < 10 or int(question_el[2]) < 10:
            if int(question_el[0]) < 10:
                num1 = question_el[0] + ".png"
            if int(question_el[2]) < 10:
                num2 = question_el[2] + ".png"

    python:
        if int(question_el[0]) >= 10 or int(question_el[2]) >= 10:
            if int(question_el[0]) >= 10:
                num1_digit1 = str(question_el[0])[:1]
                num1_digit2 = str(question_el[0])[1:]
            if int(question_el[2]) >= 10:
                num2_digit1 =  str(question_el[2])[:1]
                num2_digit2 = str(question_el[2])[1:]


    if final_quiz_count <= 5:
        imagemap:
            idle "quiz_bg_add"
            hotspot(94, 746, 335, 136) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["a"]), Jump("final_evaluate")
            hotspot(545, 744, 337, 138) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["b"]),  Jump("final_evaluate")
            hotspot(1019, 746, 346, 133) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["c"]),  Jump("final_evaluate")
            hotspot(1495, 744, 341, 139) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["d"]),  Jump("final_evaluate")

        #$ final_display_counter = final_display_counter - 1
        text "Question: [final_display_counter]" size 35 xalign 0.5 yalign 0.07 kerning 1.0
        hbox:
            yalign 0.07
            xalign 0.965
            frame:
                hbox spacing 20:
                    add "gui/money.png"
                    text "{}".format(money)

        # For double digit
        if int(question_el[0]) < 10 or int(question_el[2]) < 10:
            if int(question_el[0]) < 10:
                add im.Scale(num1,150,200) xalign 0.2 yalign 0.41
            if int(question_el[2]) < 10:
                add im.Scale(num2,150,200) xalign 0.8 yalign 0.41

        if int(question_el[0]) >= 10 or int(question_el[2]) >= 10:
            if int(question_el[0]) >= 10:
                add im.Scale(num1_digit1 + ".png",150,200) xalign 0.2 yalign 0.41
                add im.Scale(num1_digit2 + ".png",150,200) xalign 0.27 yalign 0.41
            if int(question_el[2]) >= 10:
                add im.Scale(num2_digit1 + ".png",150,200) xalign 0.75 yalign 0.41
                add im.Scale(num2_digit2 + ".png",150,200) xalign 0.82 yalign 0.41


    if final_quiz_count > 5 and final_quiz_count <= 10:
        imagemap:
            idle "quiz_bg_sub_finale"
            hotspot(94, 746, 335, 136) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["a"]), Jump("final_evaluate")
            hotspot(545, 744, 337, 138) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["b"]),  Jump("final_evaluate")
            hotspot(1019, 746, 346, 133) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["c"]),  Jump("final_evaluate")
            hotspot(1495, 744, 341, 139) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["d"]),  Jump("final_evaluate")

        #$ final_display_counter = final_display_counter - 1
        text "Question: [final_display_counter]" size 35 xalign 0.5 yalign 0.07 kerning 1.0
        hbox:
            yalign 0.07
            xalign 0.965
            frame:
                hbox spacing 20:
                    add "gui/money.png"
                    text "{}".format(money)


        # For double digit
        if int(question_el[0]) < 10 or int(question_el[2]) < 10:
            if int(question_el[0]) < 10:
                add im.Scale(num1,150,200) xalign 0.2 yalign 0.39
            if int(question_el[2]) < 10:
                add im.Scale(num2,150,200) xalign 0.8 yalign 0.39

        if int(question_el[0]) >= 10 or int(question_el[2]) >= 10:
            if int(question_el[0]) >= 10:
                add im.Scale(num1_digit1 + ".png",150,200) xalign 0.2 yalign 0.39
                add im.Scale(num1_digit2 + ".png",150,200) xalign 0.27 yalign 0.39
            if int(question_el[2]) >= 10:
                add im.Scale(num2_digit1 + ".png",150,200) xalign 0.75 yalign 0.39
                add im.Scale(num2_digit2 + ".png",150,200) xalign 0.82 yalign 0.39

    if final_quiz_count > 10 and final_quiz_count <= 15:
        imagemap:
            idle "quiz_bg"
            hotspot(171, 752, 335, 131) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",">"), Jump("final_evaluate")
            hotspot(615, 744, 340, 140) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice","="),  Jump("final_evaluate")
            hotspot(1066, 750, 328, 138) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice","<"),  Jump("final_evaluate")


        # For double digit
        if int(question_el[0]) < 10 or int(question_el[2]) < 10:
            if int(question_el[0]) < 10:
                add im.Scale(num1,150,200) xalign 0.2 yalign 0.12
            if int(question_el[2]) < 10:
                add im.Scale(num2,150,200) xalign 0.8 yalign 0.12

        if int(question_el[0]) >= 10 or int(question_el[2]) >= 10:
            if int(question_el[0]) >= 10:
                add im.Scale(num1_digit1 + ".png",150,200) xalign 0.2 yalign 0.12
                add im.Scale(num1_digit2 + ".png",150,200) xalign 0.27 yalign 0.12
            if int(question_el[2]) >= 10:
                add im.Scale(num2_digit1 + ".png",150,200) xalign 0.75 yalign 0.12
                add im.Scale(num2_digit2 + ".png",150,200) xalign 0.82 yalign 0.12

        #$ final_display_counter = final_display_counter - 1
        text "Question: [final_display_counter]" size 35 xalign 0.5 yalign 0.07 kerning 1.0
        hbox:
            yalign 0.07
            xalign 0.965
            frame:
                hbox spacing 20:
                    add "gui/money.png"
                    text "{}".format(money)
    text "Timer:" xalign 0.05 yalign 0.09 size 40
    if time <= 10:
        text str(time) xalign 0.1 yalign 0.09 size 40 color "#FF0000" at alpha_dissolve
    else:
        text str(time) xalign 0.1 yalign 0.09 size 40 at alpha_dissolve


    if final_quiz_count > 0 and final_quiz_count <= 10:
        hbox xalign 0.48 yalign 0.77 spacing 425:
            textbutton question["choices"]["a"]:
                text_style "option_button"
                text_size 70
                action SetVariable("choice",question["choices"]["a"]), Jump("final_evaluate")

            textbutton question["choices"]["b"]:
                text_style "option_button"
                text_size 70
                action SetVariable("choice",question["choices"]["b"]), Jump("final_evaluate")


            textbutton question["choices"]["c"]:
                text_style "option_button"
                text_size 70
                action SetVariable("choice",question["choices"]["c"]), Jump("final_evaluate")


            textbutton question["choices"]["d"]:
                text_style "option_button"
                text_size 70
                action SetVariable("choice",question["choices"]["d"]), Jump("final_evaluate")
                # hovered tt.Action("4th option")

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown():
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    if time == 10:
        $renpy.music.play("audio/game_sounds/timer.ogg")
    if time==1:
        $renpy.music.stop()

screen finale_msg():
    textbutton "Continue" xalign 0.5 yalign 0.62:
        text_style "learn_textbutton"
        action Return()
    if finale_money_count == 15:
        text "Congratulations! You cleared the labyrinth and saved our world" size 35 xalign 0.5 yalign 0.5
    else:
        text "You didn't clear the labyrinth,you can try again our warrior" size 35 xalign 0.5 yalign 0.5


label quiz_timer_initialize:
    $ time = 60
    $ timer_range = 60
    $ timer_jump = 'timer_ran_out'
    show screen countdown
    call screen final_quiz

label timer_ran_out:
    hide screen imageHut
    $renpy.music.stop()
    "Time is Up."
    #$final_quiz_count = final_quiz_count + 1

label final_get_question:
    if final_quiz_count <= 15:
        if final_quiz_count <= 5:
            $ question = renpy.random.choice(final_add_questions)
        elif final_quiz_count > 5 and final_quiz_count <= 10:
            $ question = renpy.random.choice(final_sub_questions)
        elif final_quiz_count > 10 and final_quiz_count <= 15:
            $ question = renpy.random.choice(final_comparison_questions)
        $ question_el =  question["question"].split(" ")
        $ final_display_counter = final_display_counter + 1
        jump quiz_timer_initialize
    else:
        jump final_game_ends

label final_evaluate:
    hide screen countdown
    hide screen imageHut
    $renpy.music.stop()
    if choice == question["answer"]:
        $ finale_money_count = finale_money_count + 1
        image final congo movie = Movie(play="correct_answer.webm",loop=False)
        show final congo movie
        "Correct Answer! You are one step closer to clear the labyrinth."
        $renpy.pause(2.0,hard=True)
        $final_quiz_count = final_quiz_count + 1
        jump final_get_question
    else:
        image final wrong movie = Movie(play="lose.webm",loop=False)
        show final wrong movie
        "Wrong Answer! You can do better warrior."
        $renpy.pause(2.0,hard=True)
        $final_quiz_count = final_quiz_count + 1
        jump final_get_question

label final_game_ends:
    $config.rollback_enabled = True
    call screen finale_msg
    if finale_money_count == 15:
            image end movie = Movie(play="end.webm", loop=False)
            show end movie
            $renpy.pause(36.0,hard=True)
    $final_display_counter = 0
    $final_quiz_count = 1
    $ finale_money_count = 0
    call screen imageHut
