screen quiz():
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


    if video_choice in (1,2,3,4):
        imagemap:
            idle "quiz_bg_add"
            hotspot(94, 746, 335, 136) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["a"]), Jump("evaluate")
            hotspot(545, 744, 337, 138) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["b"]),  Jump("evaluate")
            hotspot(1019, 746, 346, 133) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["c"]),  Jump("evaluate")
            hotspot(1495, 744, 341, 139) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["d"]),  Jump("evaluate")
        $ left_img = renpy.random.choice(fruits_list)
        $ right_img = renpy.random.choice(fruits_list)

        hbox:
            yalign 0.07
            xalign 0.965
            frame:
                hbox spacing 20:
                    add "gui/money.png"
                    text "{}".format(money)

        imagebutton:
            xalign 0.045
            yalign 0.07
            idle im.Scale("back_home.jpg",70,70)
            action Show("addition")
        textbutton "Exit Quiz" xalign 0.038 yalign 0.13:
            text_style "quiz_exit_textbutton"
            action SetVariable("question_no",1),SetVariable("quiz_display_counter",0), Show("addition")

        #$ question_no = question_no - 1
        text "Question: [quiz_display_counter]" size 35 xalign 0.5 yalign 0.07 kerning 1.0

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

        #For fruits Displaying
        if int(question_el[0]) > 10 or int(question_el[2]) > 10:
            if int(question_el[0]) > 10:
                add im.Scale(left_img + num1_digit1 + "0" + ".png",400,320) xalign 0.04 yalign 0.45
                add im.Scale(left_img + num1_digit2 + ".png",380,270) xalign 0.29 yalign 0.44
            if int(question_el[2]) > 10:
                add im.Scale(right_img + num2_digit1 + "0" + ".png",400,320) xalign 0.7 yalign 0.45
                add im.Scale(right_img + num2_digit2 + ".png",380,270) xalign 0.94 yalign 0.44

        if int(question_el[0]) <= 10 or int(question_el[2]) <= 10:
            if int(question_el[0]) <= 10:
                add im.Scale(left_img + question_el[0] + ".png",600,300) xalign 0.1 yalign 0.44
            if int(question_el[2]) <= 10:
                add im.Scale(right_img + question_el[2] + ".png",600,300) xalign 0.85 yalign 0.44


    if video_choice in (5,6):
        imagemap:
            idle "quiz_bg_sub"
            hotspot(94, 746, 335, 136) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["a"]), Jump("evaluate")
            hotspot(545, 744, 337, 138) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["b"]),  Jump("evaluate")
            hotspot(1019, 746, 346, 133) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["c"]),  Jump("evaluate")
            hotspot(1495, 744, 341, 139) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",question["choices"]["d"]),  Jump("evaluate")
        $ left_img = "watermelon"
        $ right_img = "cross"

        hbox:
            yalign 0.07
            xalign 0.965
            frame:
                hbox spacing 20:
                    add "gui/money.png"
                    text "{}".format(money)

        imagebutton:
            xalign 0.045
            yalign 0.07
            idle im.Scale("back_home.jpg",70,70)
            action Show("addition")
        textbutton "Exit Quiz" xalign 0.038 yalign 0.13:
            text_style "quiz_exit_textbutton"
            action SetVariable("question_no",1),SetVariable("quiz_display_counter",0), Show("subtraction")

        #$ question_no = question_no - 1
        text "Question: [quiz_display_counter]" size 35 xalign 0.5 yalign 0.07 kerning 1.0


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

        #for watermellon
        # if int(question_el[0]) <= 10 or int(question_el[2]) <= 10:
        #     if int(question_el[0]) <= 10:
        #         add im.Scale(left_img + question_el[0] + ".png",600,300) xalign 0.25 yalign 0.41
        #     if int(question_el[2]) <= 10:
        #         add im.Scale(right_img + question_el[2] + ".png",600,300) xalign 0.25 yalign 0.41

        if int(question_el[0]) > 10 or int(question_el[2]) > 10:
            if int(question_el[0]) > 10:
                add im.Scale(left_img + num1_digit1 + "0" + ".png",600,300) xalign 0.25 yalign 0.41
                add im.Scale(left_img + num1_digit2 + ".png",600,300) xalign 0.7 yalign 0.41
            if int(question_el[2]) > 10:
                add im.Scale(right_img + num2_digit1 + "0" + ".png",600,300) xalign 0.25 yalign 0.41
                add im.Scale(right_img + num2_digit2 + ".png",600,300) xalign 0.7 yalign 0.41

        if int(question_el[0]) <= 10 or int(question_el[2]) <= 10:
            if int(question_el[0]) <= 10:
                add im.Scale(left_img + question_el[0] + ".png",600,300) xalign 0.25 yalign 0.41
            if int(question_el[2]) <= 10:
                add im.Scale(right_img + question_el[2] + ".png",600,300) xalign 0.25 yalign 0.41


        #add im.Scale(left_img + question_el[0] + ".png",600,300) xalign 0.55 yalign 0.41
        #add im.Scale(right_img + question_el[2] + ".png",600,300) xalign 0.55 yalign 0.41

    if video_choice == 8:
        imagemap:
            idle "quiz_bg"
            hotspot(171, 752, 335, 131) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice",">"), Jump("evaluate")
            hotspot(615, 744, 340, 140) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice","="),  Jump("evaluate")
            hotspot(1066, 750, 328, 138) hovered Play('sound', 'audio/game_sounds/button_hover.ogg') action SetVariable("choice","<"),  Jump("evaluate")

        add im.Scale(num1,150,200) xalign 0.15 yalign 0.12
        add im.Scale(num2,150,200) xalign 0.65 yalign 0.12

        imagebutton:
            xalign 0.045
            yalign 0.07
            idle im.Scale("back_home.jpg",70,70)
            action Show("addition")
        textbutton "Exit Quiz" xalign 0.038 yalign 0.13:
            text_style "quiz_exit_textbutton"
            action SetVariable("question_no",1), SetVariable("quiz_display_counter",0), Show("comparison")

        #$ question_no = question_no - 1
        text "Question: [quiz_display_counter]" size 35 xalign 0.5 yalign 0.07 kerning 1.0

        hbox:
            yalign 0.07
            xalign 0.965
            frame:
                hbox spacing 20:
                    add "gui/money.png"
                    text "{}".format(money)

        $ left_img = renpy.random.choice(fruits_list)
        $ right_img = renpy.random.choice(fruits_list)


        add im.Scale(left_img + question_el[0] + ".png",600,300) xalign 0.05 yalign 0.44
        add im.Scale(right_img + question_el[2] + ".png",600,300) xalign 0.7 yalign 0.44



    if video_choice in (1,2,3,4,5,6):
        hbox xalign 0.48 yalign 0.77 spacing 425:
            textbutton question["choices"]["a"]:
                text_style "option_button"
                text_size 70
                action SetVariable("choice",question["choices"]["a"]), Jump("evaluate")

            textbutton question["choices"]["b"]:
                text_style "option_button"
                text_size 70
                action SetVariable("choice",question["choices"]["b"]), Jump("evaluate")

            textbutton question["choices"]["c"]:
                text_style "option_button"
                text_size 70
                action SetVariable("choice",question["choices"]["c"]), Jump("evaluate")

            textbutton question["choices"]["d"]:
                text_style "option_button"
                text_size 70
                action SetVariable("choice",question["choices"]["d"]), Jump("evaluate")



screen video_unlock(message):
    # if content_unlocked in (1,2,3):
    #     $ temp = "Click on continue button below"
    #     textbutton "Continue" xalign 0.5 yalign 0.62:
    #         text_style "learn_textbutton"
    #         action Jump("game_ends")
    #         #action Return()
    #     #$ print("temp early->",temp)
    #     $ print("before add_2_flag->",globals()['add_2_flag'])
    #     if globals()['add_2_flag'] and globals()['money'] >= 4:
    #         $temp = " "
    #         text "Congratulations! Single Digit(Difficult) has been unlocked" size 35 xalign 0.5 yalign 0.5
    #         $ change_value("add_2")
    #         # $ globals()['add_2_flag'] = False
    #         # python:
    #         #     global add_2_flag
    #         #     add_2_flag = False
    #
    #     $ print("after add_2_flag->",globals()['add_2_flag'])
    #     #$ print("before add_3_flag->",globals()['add_3_flag'])
    #     if globals()['add_3_flag'] and globals()['money'] >= 8:
    #         $temp = " "
    #         text "Congratulations! Double Digit(No Carry Over) has been unlocked" xalign 0.5 yalign 0.5
    #         $ change_value("add_3")
    #         #$ add_3_flag = False
    #         # python:
    #         #     global add_3_flag
    #         #     add_3_flag = False
    #     #$ print("after add_3_flag->",add_3_flag)
    #
    #
    #     if globals()['add_4_flag'] and globals()['money'] >= 13:
    #         $temp = " "
    #         text "Congratulations! Double Digit(Carry Over) has been unlocked" xalign 0.5 yalign 0.5
    #         $ change_value("add_4")
    #         # python:
    #         #     global add_4_flag
    #         #     add_4_flag = False
    #
    #     if globals()['video_choice'] == 4 and globals()['sub_1_flag'] and globals()['money'] >= 16:
    #         $temp = " "
    #         $content_unlocked = content_unlocked + 1
    #         text "Congratulations! Subtraction has been unlocked" xalign 0.5 yalign 0.5
    #         $ change_value("sub_1")
    #         # python:
    #         #     global sub_1_flag
    #         #     sub_1_flag = False
    #     if globals()['sub_2_flag'] and globals()['money'] >= 21:
    #         $temp = " "
    #         text "Congratulations! }Double Digit(Easy) has been unlocked" xalign 0.5 yalign 0.5
    #         $ change_value("sub_2")
    #         # python:
    #         #     global sub_2_flag
    #         #     sub_2_flag = False
    #     if globals()['video_choice'] == 6 and globals()['comp_flag'] and globals()['money'] >= 23:
    #         $temp = " "
    #         $ content_unlocked = content_unlocked + 1
    #         text "Congratulations! Comparison has been unlocked" xalign 0.5 yalign 0.5
    #         $ change_value("comp_flag")
    #         # python:
    #         #     global comp_flag
    #         #     comp_flag = False
    #     if globals()['video_choice'] == 8 and globals()['final_quiz_flag'] and globals()['money'] >= 25:
    #         $temp = " "
    #         $ content_unlocked = content_unlocked + 1
    #         text "Congratulations! Final Quiz has been unlocked" xalign 0.5 yalign 0.5
    #         $ change_value("final_flag")
    #         # python:
    #         #     global final_quiz_flag
    #         #     final_quiz_flag = False
    #     #$ print("temp late->",temp)
    #     text "[temp]" xalign 0.5 yalign 0.52
    add "bg background_username"
    add im.Scale("unlock.png",400,400) xalign 0.5 yalign 0.34
    textbutton "Continue" xalign 0.5 yalign 0.73:
        text_style "learn_textbutton"
        text_size 38
        action Jump("game_ends")
    text "Congratulations! [message] has been unlocked" size 40 xalign 0.5 yalign 0.65


label get_question:
    if question_no <= 5:
        if video_choice == 1:
            $ question = renpy.random.choice(add_questions_easy)
        elif video_choice == 2:
            $ question = renpy.random.choice(add_questions_diff)
        elif video_choice == 3:
            $ question = renpy.random.choice(add_questions_without_carry)
        elif video_choice == 4:
            $ question = renpy.random.choice(add_questions_with_carry)
        elif video_choice == 5:
            $ question = renpy.random.choice(sub_questions)
        elif video_choice == 6:
            $ question = renpy.random.choice(sub_questions_double)
        elif video_choice == 8:
            $ question = renpy.random.choice(comparison_questions)
        $ question_el =  question["question"].split(" ")
        $ question_no = question_no + 1
        $ quiz_display_counter = quiz_display_counter + 1
        call screen quiz
    else:
        $ temp = set_message()
        if temp:
            call screen video_unlock(temp)
        else:
            jump game_ends

label evaluate:
    if choice == question["answer"]:
        if video_choice == 1 and money < 5:
            $ money = money + 1
        if video_choice == 2 and money < 10:
            $ money = money + 1
        if video_choice == 3 and money < 15:
            $ money = money + 1
        if video_choice == 4 and money < 20:
            $ money = money + 1
        if video_choice == 5 and money < 25:
            $ money = money + 1
        if video_choice == 6 and money < 30:
            $ money = money + 1
        if video_choice == 8 and money < 35:
            $ money = money + 1
        image congo movie = Movie(play="correct_answer.webm",loop=False)
        show congo movie
        "Right! you gained 1 point.Trophy: [money]"
        $renpy.pause(2.0,hard=True)
        hide congo movie
        jump get_question
    else:
        image wrong movie = Movie(play="lose.webm",loop=False)
        show wrong movie
        $ ans = question["answer"]
        "Wrong! answer.Correct answer was [ans]"
        $renpy.pause(2.0,hard=True)
        hide wrong movie
        jump get_question

label game_ends:
    $config.rollback_enabled = True
    $question_no = 1
    $quiz_display_counter = 0
    if video_choice == 1:
        scene bg forest with dissolve
        show master1 thumbsup
        play sound "audio/dialogue_voice/m1_1.ogg"
        M1 "You have completed the quiz,now you can take some rest"
        stop sound fadeout 1.0
        hide master1 thumbsup
        show villager dont know at right with moveinright
        show master1 idle at left with moveinleft
        play sound "audio/dialogue_voice/v_1.ogg"
        V1 "Hello, Heroes I see your training is going well, I brought some milk and cookies to have them during your break."
        stop sound fadeout 1.0
        if gender == "male":
            show mc idle
            play sound "audio/dialogue_voice/mc_4.ogg"
        if gender == "female":
            show fmc idle
            play sound "audio/dialogue_voice/fmc_4.ogg"
        MC "Thank you so much, this is really sweet and tasty."
        stop sound fadeout 1.0
        play sound "audio/dialogue_voice/v_2.ogg"
        V1 "{b}Did you know? {/b} We get milk from cows, buffaloes, goats and camels.And milk is used to create cheese, cream, butter and cooking oil."
        stop sound fadeout 1.0
        hide villager dont know
        hide master1 idle
        show master1 dont know at left
        show villager idle at right
        play sound "audio/dialogue_voice/m1_2.ogg"
        M1 "Also you boil the milk to kill any viruses after you take milk from animals."
        stop sound fadeout 1.0
        hide master1 dont know
        hide villager idle
        show villager dont know at right
        show master1 idle at left
        play sound "audio/dialogue_voice/v_3.ogg"
        V1 "As expected of the intelligent heros. I will see you guys later."
        stop sound fadeout 1.0
        call screen addition

    if video_choice == 2:
        scene bg castle entrance with dissolve
        show master1 thumbsup
        play sound "audio/dialogue_voice/m1_3.ogg"
        M1 "You have completed the quiz,now you can take some rest"
        stop sound fadeout 1.0
        hide master1 thumbsup
        show soldier dont know at right with moveinright
        show master1 idle at left with moveinleft
        play sound "audio/dialogue_voice/s_1.ogg"
        S1 "Hey Heros I see you are working hard Seeing you working so hard makes me feel inspired to become stronger too, keep up the good work."
        stop sound fadeout 1.0
        if gender == "male":
            show mc idle
            play sound "audio/dialogue_voice/mc_5.ogg"
        if gender == "female":
            show fmc idle
            play sound "audio/dialogue_voice/fmc_5.ogg"
        MC "Yes sir, thank you for the moral support."
        stop sound fadeout 1.0
        play sound "audio/dialogue_voice/s_2.ogg"
        S1 "If you need any help regarding heavy lifting you can ask me anytime."
        stop sound fadeout 1.0
        play sound "audio/dialogue_voice/s_3.ogg"
        S1 "{b}Did you know? {/b} Horses were used as rides to travel between villages."
        stop sound fadeout 1.0
        hide soldier dont know
        hide master1 idle
        show master1 dont know at left
        show soldier idle at right
        play sound "audio/dialogue_voice/m1_4.ogg"
        M1 "also camel is used in desert regions instead of horses."
        stop sound fadeout 1.0
        hide master1 dont know
        hide soldier idle
        show soldier dont know at right
        show master1 idle at left
        play sound "audio/dialogue_voice/s_4.ogg"
        S1 "I see you are very wise as expected."
        stop sound fadeout 1.0
        call screen addition

    if video_choice == 3:
        scene bg forest extra2 with dissolve
        show master1 thumbsup
        play sound "audio/dialogue_voice/m1_5.ogg"
        M1 "You have completed the quiz,now you can take some rest"
        stop sound fadeout 1.0
        hide master1 thumbsup
        show mage dont know at right with moveinright
        show master1 idle at left with moveinleft
        play sound "audio/dialogue_voice/mage_1.ogg"
        M "Good day heroes, learning new things to clear the labyrinth I see, I have brought some orange juice for you all."
        stop sound fadeout 1.0
        if gender == "male":
            show mc idle
            play sound "audio/dialogue_voice/mc_6.ogg"
        if gender == "female":
            show fmc idle
            play sound "audio/dialogue_voice/fmc_6.ogg"
        MC "Thank you so much, this is tangy and cold, it feels refreshing after drinking this"
        stop sound fadeout 1.0
        play sound "audio/dialogue_voice/mage_2.ogg"
        M "It's good to know you liked it."
        stop sound fadeout 1.0
        play sound "audio/dialogue_voice/mage_3.ogg"
        M "{b}Did you know? {/b} Color orange got its name from this fruit called orange hence they both have the same name."
        stop sound fadeout 1.0
        hide mage dont know
        hide master1 idle
        show master1 dont know at left
        show mage idle at right
        play sound "audio/dialogue_voice/m1_6.ogg"
        M1 "also oranges help with healing wounds faster."
        stop sound fadeout 1.0
        hide master1 dont know
        hide mage idle
        show mage dont know at right
        show master1 idle at left
        play sound "audio/dialogue_voice/mage_4.ogg"
        M "You heroes do know your stuff. I am impressed."
        stop sound fadeout 1.0
        call screen addition

    if video_choice == 4:
        scene bg forest with dissolve
        show master1 thumbsup
        play sound "audio/dialogue_voice/m1_7.ogg"
        M1 "You have completed the quiz,now you can take some rest"
        stop sound fadeout 1.0
        hide master1 thumbsup
        show messenger dont know at right with moveinright
        show master1 idle at left with moveinleft
        play sound "audio/dialogue_voice/msg_3.ogg"
        MSG "Greetings heroes, l see you are already giving your all thank you for helping us in clearing the labyrinth, I have brought some snacks."
        stop sound fadeout 1.0
        if gender == "male":
            show mc idle
            play sound "audio/dialogue_voice/mc_7.ogg"
        if gender == "female":
            show fmc idle
            play sound "audio/dialogue_voice/fmc_7.ogg"
        MC "Thank you so much, these are really tasty"
        stop sound fadeout 1.0
        play sound "audio/dialogue_voice/msg_4.ogg"
        MSG "It's good to know you liked it."
        stop sound fadeout 1.0
        play sound "audio/dialogue_voice/msg_5.ogg"
        MSG "{b}Did you know? {/b} pigeons were used as messengers in the old days."
        stop sound fadeout 1.0
        hide messenger dont know
        hide master1 idle
        show master1 dont know at left
        show messenger idle at right
        play sound "audio/dialogue_voice/m1_8.ogg"
        M1 "yes, that was because of their natural ability to find homes themselves."
        stop sound fadeout 1.0
        hide master1 dont know
        hide messenger idle
        show messenger dont know at right
        show master1 idle at left
        play sound "audio/dialogue_voice/msg_6.ogg"
        MSG "ohhh so that is why you get to know something new every day, I hope you enjoy learning"
        stop sound fadeout 1.0
        call screen addition

    if video_choice == 5:
        scene bg throne room with dissolve
        show master3 thumbsup
        play sound "audio/dialogue_voice/m3_1.ogg"
        M3 "You have completed the quiz,now you can take some rest"
        stop sound fadeout 1.0
        hide master3 thumbsup
        show princess dont know at right with moveinright
        show master3 cross arms at left with moveinleft
        play sound "audio/dialogue_voice/ps_10.ogg"
        PS "Good day heroes, l see you are already giving your all thank you for helping us in clearing the labyrinth, If you need anything just ask."
        stop sound fadeout 1.0
        if gender == "male":
            show mc idle
            play sound "audio/dialogue_voice/mc_8.ogg"
        if gender == "female":
            show fmc idle
            play sound "audio/dialogue_voice/fmc_8.ogg"
        MC "Yes, your Majesty, a good day to you too and thankyou for visiting us"
        stop sound fadeout 1.0
        #PS "It's good to know you liked it."
        play sound "audio/dialogue_voice/ps_11.ogg"
        PS "{b}Did you know? {/b} Earth is spherical in shape and it revolves around the sun."
        stop sound fadeout 1.0
        hide princess dont know
        hide master3 cross arms
        show master3 dont know at left
        show princess idle at right
        play sound "audio/dialogue_voice/m3_2.ogg"
        M3 "Similarly the moon revolves around the earth."
        stop sound fadeout 1.0
        hide master3 dont know
        hide princess idle
        show princess dont know at right
        show master3 cross arms at left
        play sound "audio/dialogue_voice/ps_12.ogg"
        PS "Wow, I am impressed by our intelligent heroes."
        stop sound fadeout 1.0
        call screen subtraction
    if video_choice == 6:
        scene bg forest with dissolve
        show master3 thumbsup
        play sound "audio/dialogue_voice/m3_3.ogg"
        M3 "You have completed the quiz,now you can take some rest"
        stop sound fadeout 1.0
        hide master3 thumbsup
        show villager dont know at right with moveinright
        show master3 cross arms at left with moveinleft
        play sound "audio/dialogue_voice/v_4.ogg"
        V1 "Hello, Heroes I see you are still at training good to see such hard Working kids do your best but also don't forget to take breaks."
        V1 "I have brought up some tomato soup to warm you up."
        stop sound fadeout 1.0
        if gender == "male":
            show mc idle
            play sound "audio/dialogue_voice/mc_9.ogg"
        if gender == "female":
            show fmc idle
            play sound "audio/dialogue_voice/fmc_9.ogg"
        MC "Thank you so much, it is really tasty and tangy."
        stop sound fadeout 1.0
        #V1 "It's good to know you liked it."
        play sound "audio/dialogue_voice/v_5.ogg"
        V1 "{b}Did you know? {/b} tomato is even though it is considered as a vegetable it is a fruit as it has seeds in them."
        stop sound fadeout 1.0
        hide villager dont know
        hide master3 cross arms
        show master3 dont know at left
        show villager idle at right
        play sound "audio/dialogue_voice/m3_4.ogg"
        M3 "tomatoes are also used to make tomato ketchup too."
        stop sound fadeout 1.0
        hide master3 dont know
        hide villager idle
        show villager dont know at right
        show master3 cross arms at left
        play sound "audio/dialogue_voice/v_6.ogg"
        V1 "As expected, the heroes are as intelligent as ever. I will see you guys later."
        stop sound fadeout 1.0
        call screen subtraction
    if video_choice == 8:
        scene bg forest extra2 with dissolve
        show master2 thumbsup
        play sound "audio/dialogue_voice/m2_1.ogg"
        M2 "You have completed the quiz,now you can take some rest"
        stop sound fadeout 1.0
        hide master2 thumbsup
        show mage dont know at right with moveinright
        show master2 idle at left with moveinleft
        play sound "audio/dialogue_voice/mage_5.ogg"
        M "Good day heroes, learning new things to clear the labyrinth I see, I have brought some hot chocolate."
        stop sound fadeout 1.0
        if gender == "male":
            show mc idle
            play sound "audio/dialogue_voice/mc_10.ogg"
        if gender == "female":
            show fmc idle
            play sound "audio/dialogue_voice/fmc_10.ogg"
        MC "Thank you so much,this is warm and sweet."
        stop sound fadeout 1.0
        #M "It's good to know you liked it."
        play sound "audio/dialogue_voice/mage_6.ogg"
        M "{b}Did you know? {/b} As we breathe we consume oxygen in air and release carbon dioxide."
        stop sound fadeout 1.0
        hide mage dont know
        hide master2 idle
        show master2 dont know at left
        show mage idle at right
        play sound "audio/dialogue_voice/m2_2.ogg"
        M2 "yes and also plants take carbon dioxide and release oxygen complete the cycle."
        stop sound fadeout 1.0
        hide master2 dont know
        hide mage idle
        show mage dont know at right
        show master2 idle at left
        play sound "audio/dialogue_voice/mage_7.ogg"
        M "as impressive as ever i see, see you later heroes."
        stop sound fadeout 1.0
        call screen comparison
