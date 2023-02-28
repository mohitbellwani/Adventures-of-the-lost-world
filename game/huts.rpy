screen imageHut:
    if content_unlocked == 1:
        imagemap:
            idle "bg village1"
            hover "bg2_village1.png"
            #hotspot(596, 650, 375, 235)  action Show("addition")
            hotspot(551, 512, 463, 399) action Show("addition")
            hotspot(1057, 621, 749, 441) action Show("subtraction_unlock_msg")
            hotspot(1268, 463, 264, 158) action Show("comparison_unlock_msg")


            textbutton "Addition" xalign 0.42 yalign 0.64:
                text_style "mytextbutton"
                text_size 38
                action Show("addition")

            add im.Scale("lock_1.png",60,60) xalign 0.71 yalign 0.675
            textbutton "Subtraction" xalign 0.79 yalign 0.68:
                text_style "mytextbutton"
                text_size 38

            add im.Scale("lock_1.png",32,32) xalign 0.70 yalign 0.48
            textbutton "Compare" xalign 0.749 yalign 0.48:
                text_style "mytextbutton"
                text_size 33

            add im.Scale("lock_1.png",60,60) xalign 0.128 yalign 0.138
            textbutton "Finale" xalign 0.17 yalign 0.132:
                text_style "mytextbutton"
                text_size 60
                action Show("finale_unlock_msg")


    elif content_unlocked == 2:
        imagemap:
            idle "bg village1"
            hotspot(596, 650, 375, 235) action Show("addition")
            hotspot(1164, 650, 589, 375) action Show("subtraction")
            hotspot(1302, 489, 184, 115) action Show("comparison_unlock_msg")

            textbutton "Addition" xalign 0.42 yalign 0.64:
                text_style "mytextbutton"
                action Show("addition")

            textbutton "Subtraction" xalign 0.79 yalign 0.68:
                text_style "mytextbutton"
                action Show("subtraction")

            add im.Scale("lock_1.png",32,32) xalign 0.70 yalign 0.48
            textbutton "Compare" xalign 0.749 yalign 0.48:
                text_style "mytextbutton"
                text_size 33

            add im.Scale("lock_1.png",60,60) xalign 0.128 yalign 0.138
            textbutton "Finale" xalign 0.17 yalign 0.132:
                text_style "mytextbutton"
                text_size 60
                action Show("finale_unlock_msg")

    elif content_unlocked == 3:
        imagemap:
            idle "bg village1"
            hotspot(596, 650, 375, 235) action Show("addition")
            hotspot(1164, 650, 589, 375) action Show("subtraction")
            hotspot(1302, 489, 184, 115) action Show("comparison")

            textbutton "Addition" xalign 0.42 yalign 0.64:
                text_style "mytextbutton"
                action Show("addition")

            textbutton "Subtraction" xalign 0.79 yalign 0.68:
                text_style "mytextbutton"
                action Show("subtraction")

            textbutton "Compare" xalign 0.749 yalign 0.48:
                text_style "mytextbutton"
                text_size 33
                action Show("comparison")

            add im.Scale("lock_1.png",60,60) xalign 0.128 yalign 0.138
            textbutton "Finale" xalign 0.17 yalign 0.132:
                text_style "mytextbutton"
                text_size 60
                action Show("finale_unlock_msg")

    elif content_unlocked == 4:
        imagemap:
            idle "bg village1"
            hotspot(596, 650, 375, 235) action Show("addition")
            hotspot(1164, 650, 589, 375) action Show("subtraction")
            hotspot(1302, 489, 184, 115) action Show("comparison")
            #hotspot(1413, 308, 178, 118) action Jump("final_show_quiz")

            textbutton "Addition" xalign 0.42 yalign 0.64:
                text_style "mytextbutton"
                action Show("addition")

            textbutton "Subtraction" xalign 0.79 yalign 0.68:
                text_style "mytextbutton"
                action Show("subtraction")

            textbutton "Compare" xalign 0.745 yalign 0.48:
                text_style "mytextbutton"
                text_size 30
                action Show("comparison")

            textbutton "Finale" xalign 0.17 yalign 0.132:
                text_style "mytextbutton"
                text_size 60
                action Jump("final_show_quiz")


screen add_hut():
    add "bg_house3_village1.png"

screen finale_unlock_msg():
    add "bg background_username"
    add im.Scale("lock_2.png",400,400) xalign 0.5 yalign 0.37
    $ req = 25 - money
    text "Complete the Addition, Subtraction and Compare to unlock the Finale." size 35 xalign 0.52 yalign 0.7 kerning 1.0
    text "You need 25 - [money] = {color=#faad12}[req]{/color} trophies to unlock.To earn more trophies give the quiz again." size 35 xalign 0.5 yalign 0.77 kerning 1.0
    textbutton "Back" xalign 0.5 yalign 0.88:
        text_style "learn_textbutton"
        text_size 38
        hovered Play('sound', 'audio/game_sounds/button_hover.ogg')
        action Hide("finale_unlock_msg")



screen subtraction_unlock_msg():
    add "bg background_username"
    add im.Scale("lock_2.png",400,400) xalign 0.5 yalign 0.37
    text "Complete the Addition to unlock Subtraction." size 35 xalign 0.5 yalign 0.7 kerning 1.0
    textbutton "Back" xalign 0.5 yalign 0.8:
        text_style "learn_textbutton"
        hovered Play('sound', 'audio/game_sounds/button_hover.ogg')
        action Hide("subtraction_unlock_msg")

screen comparison_unlock_msg():
    add "bg background_username"
    add im.Scale("lock_2.png",400,400) xalign 0.5 yalign 0.37
    text "Complete the Addition, Subtraction to unlock Compare." size 35 xalign 0.5 yalign 0.7 kerning 1.0
    textbutton "Back" xalign 0.5 yalign 0.8:
        text_style "learn_textbutton"
        hovered Play('sound', 'audio/game_sounds/button_hover.ogg')
        action Hide("comparison_unlock_msg")

screen add_2_unlock_msg():
    add "bg background_username"
    add im.Scale("lock_2.png",400,400) xalign 0.5 yalign 0.37
    $ req = 4 - money
    text "You need 4 - [money] = {color=#faad12}[req]{/color} trophies to unlock.To earn more trophies give the quiz again." size 35 xalign 0.5 yalign 0.7 kerning 1.0
    textbutton "Back" xalign 0.5 yalign 0.8:
        text_style "learn_textbutton"
        hovered Play('sound', 'audio/game_sounds/button_hover.ogg')
        action Hide("add_2_unlock_msg")

screen add_3_unlock_msg():
    add "bg background_username"
    add im.Scale("lock_2.png",400,400) xalign 0.5 yalign 0.37
    $ req = 8 - money
    text "You need 8 - [money] = {color=#faad12}[req]{/color} trophies to unlock.To earn more trophies give the quiz again." size 35 xalign 0.5 yalign 0.7 kerning 1.0
    textbutton "Back" xalign 0.5 yalign 0.8:
        text_style "learn_textbutton"
        hovered Play('sound', 'audio/game_sounds/button_hover.ogg')
        action Hide("add_3_unlock_msg")

screen add_4_unlock_msg():
    add "bg background_username"
    add im.Scale("lock_2.png",400,400) xalign 0.5 yalign 0.37
    $ req = 13 - money
    text "You need 13 - [money] = {color=#faad12}[req]{/color} trophies to unlock.To earn more trophies give the quiz again." size 35 xalign 0.5 yalign 0.7 kerning 1.0
    textbutton "Back" xalign 0.5 yalign 0.8:
        text_style "learn_textbutton"
        hovered Play('sound', 'audio/game_sounds/button_hover.ogg')
        action Hide("add_4_unlock_msg")

screen sub_2_unlock_msg():
    add "bg background_username"
    add im.Scale("lock_2.png",400,400) xalign 0.5 yalign 0.37
    $ req = 21 - money
    text "You need 21 - [money] = {color=#faad12}[req]{/color} trophies to unlock.To earn more trophies give the quiz again." size 35 xalign 0.5 yalign 0.7 kerning 1.0
    textbutton "Back" xalign 0.5 yalign 0.8:
        text_style "learn_textbutton"
        hovered Play('sound', 'audio/game_sounds/button_hover.ogg')
        action Hide("sub_2_unlock_msg")



screen addition:
    add "bg background_username"
    text "Addition" size 50 xalign 0.5 yalign 0.08
    text "Lessons" size 35 xalign 0.06 yalign 0.3

    imagebutton xalign 0.05 yalign 0.15:
        idle "bg village2 icon.png"
        hover "lesson_hut_hover"
        action Hide("addition"), Show("imageHut")

    hbox:
        yalign 0.01
        xalign 0.99
        frame:
            hbox spacing 20:
                add "gui/money.png"
                text "{}".format(money)

    #hbox xalign 0.53 yalign 0.7 spacing 185:
    imagebutton:
        xalign 0.25
        yalign 0.25
        idle im.Scale("addition_1.png",550,250)
        hover "add_1_hover"
        action SetVariable("video_choice", 1), Jump("playvideo")

    #add im.Scale("addition_1.png",550,250) xalign 0.25 yalign 0.25
    textbutton "{b}Single Digit(Easy){/b}" xalign 0.3 yalign 0.47:
        text_style "learn_textbutton"
        action SetVariable("video_choice", 1), Jump("playvideo")

    #add im.Scale("addition_2.png",550,250) xalign 0.75 yalign 0.25
    if money <= 3:
        imagebutton:
            xalign 0.75
            yalign 0.25
            idle im.Scale("addition_2.png",550,250)
            hover "add_2_hover"
            action Show("add_2_unlock_msg")
        add im.Scale("lock.png",550,250) xalign 0.75 yalign 0.25
        textbutton "{b}Single Digit(Difficult){/b}" xalign 0.72 yalign 0.47:
            text_style "disabled_learn_textbutton"
            action Show("add_2_unlock_msg")
    else:
        imagebutton:
            xalign 0.75
            yalign 0.25
            idle im.Scale("addition_2.png",550,250)
            hover "add_2_hover"
            action SetVariable("video_choice", 2), Jump("playvideo")
        textbutton "{b}Single Digit(Difficult){/b}" xalign 0.72 yalign 0.47:
            text_style "learn_textbutton"
            action SetVariable("video_choice", 2), Jump("playvideo")


    #hbox xalign 0.52 yalign 0.55 spacing 90:
    #add im.Scale("addition_3.png",550,250) xalign 0.25 yalign 0.7
    if money <= 7:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle im.Scale("addition_3.png",550,250)
            hover "add_3_hover"
            action Show("add_3_unlock_msg")
        add im.Scale("lock.png",550,250) xalign 0.25 yalign 0.7
        textbutton "{b}Double Digit(No Carry Over){/b}" xalign 0.3 yalign 0.85:
            text_style "disabled_learn_textbutton"
            action Show("add_3_unlock_msg")
    else:
        imagebutton:
            xalign 0.25
            yalign 0.7
            idle im.Scale("addition_3.png",550,250)
            hover "add_3_hover"
            action SetVariable("video_choice", 3), Jump("playvideo")
        textbutton "{b}Double Digit(No Carry Over){/b}" xalign 0.3 yalign 0.85:
            text_style "learn_textbutton"
            action SetVariable("video_choice", 3), Jump("playvideo")

    #add im.Scale("addition_4.png",550,250) xalign 0.75 yalign 0.7
    if money <= 12:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle im.Scale("addition_4.png",550,250)
            hover "add_4_hover"
            action Show("add_4_unlock_msg")
        add im.Scale("lock.png",550,250) xalign 0.75 yalign 0.7
        textbutton "{b}Double Digit(Carry Over){/b}" xalign 0.72 yalign 0.85:
            text_style "disabled_learn_textbutton"
            action Show("add_4_unlock_msg")
    else:
        imagebutton:
            xalign 0.75
            yalign 0.7
            idle im.Scale("addition_4.png",550,250)
            hover "add_4_hover"
            action SetVariable("video_choice", 4), Jump("playvideo")
        textbutton "{b}Double Digit(Carry Over){/b}" xalign 0.72 yalign 0.85:
            text_style "learn_textbutton"
            action SetVariable("video_choice", 4), Jump("playvideo")


screen subtraction:
    add "bg background_username"
    text "Subtraction" size 50 xalign 0.5 yalign 0.22
    text "Lessons" size 35 xalign 0.06 yalign 0.3

    imagebutton xalign 0.05 yalign 0.15:
        idle "bg village2 icon.png"
        hover "lesson_hut_hover"
        action Hide("subtraction"),Show("imageHut")

    hbox:
        yalign 0.01
        xalign 0.99
        frame:
            hbox spacing 20:
                add "gui/money.png"
                text "{}".format(money)

    #hbox xalign 0.53 yalign 0.4 spacing 185:
    #add im.Scale("subtraction_1.png",550,250) xalign 0.25 yalign 0.5
    imagebutton:
        xalign 0.25
        yalign 0.5
        idle im.Scale("subtraction_1.png",550,250)
        hover "sub_1_hover"
        action SetVariable("video_choice", 5), Jump("playvideo")
    textbutton "{b}Single Digit(Easy){/b}"  xalign 0.3 yalign 0.68:
        text_style "learn_textbutton"
        action SetVariable("video_choice", 5), Jump("playvideo")

    #add im.Scale("subtraction_2.png",550,250) xalign 0.75 yalign 0.5
    if money <= 20:
        imagebutton:
            xalign 0.75
            yalign 0.5
            idle im.Scale("subtraction_2.png",550,250)
            hover "sub_2_hover"
            action Show("sub_2_unlock_msg")
        add im.Scale("lock.png",550,250) xalign 0.75 yalign 0.5
        textbutton "{b}Double Digit(Easy){/b}" xalign 0.72 yalign 0.68:
            text_style "disabled_learn_textbutton"
            action Show("sub_2_unlock_msg")
    else:
        imagebutton:
            xalign 0.75
            yalign 0.5
            idle im.Scale("subtraction_2.png",550,250)
            hover "sub_2_hover"
            action SetVariable("video_choice", 6), Jump("playvideo")
        textbutton "{b}Double Digit(Easy){/b}" xalign 0.72 yalign 0.68:
            text_style "learn_textbutton"
            action SetVariable("video_choice", 6), Jump("playvideo")

screen comparison:
    add "bg background_username"
    text "Comparison" size 50 xalign 0.5 yalign 0.2
    text "Lessons" size 35 xalign 0.06 yalign 0.3

    imagebutton xalign 0.05 yalign 0.15:
        idle "bg village2 icon.png"
        hover "lesson_hut_hover"
        action Hide("comparison"), Show("imageHut")

    hbox:
        yalign 0.01
        xalign 0.99
        frame:
            hbox spacing 20:
                add "gui/money.png"
                text "{}".format(money)

    #hbox xalign 0.53 yalign 0.4 spacing 185:
    #add im.Scale("grat.png",550,250) xalign 0.48 yalign 0.48
    imagebutton:
        xalign 0.48
        yalign 0.48
        idle im.Scale("grat.png",550,250)
        hover "comp_hover"
        action SetVariable("video_choice", 8), Jump("playvideo")
    textbutton "{b}Greater,Eqaul and Lesser{/b}" xalign 0.5 yalign 0.66:
        text_style "learn_textbutton"
        action SetVariable("video_choice", 8), Jump("playvideo")



screen skip_button:
    textbutton "Skip":
        text_style "mytextbutton"
        action Jump("instruct_for_quiz")

label playvideo:
    $renpy.music.stop(channel='music', fadeout=None)
    $config.rollback_enabled = False
    if video_choice == 1:
        image addition easy movie = Movie(play="addition_1.webm", loop=False)
        hide screen addition
        hide screen imageHut
        show addition easy movie
        show screen skip_button
        $renpy.pause(102.0,hard=True)
    if video_choice == 2:
        image addition difficult movie = Movie(play="addition_2.webm", loop=False)
        hide screen addition
        hide screen imageHut
        show addition difficult movie
        show screen skip_button
        $renpy.pause(34.0,hard=True)
    if video_choice == 3:
        image addition without carry movie = Movie(play="addition_3.webm", loop=False)
        hide screen addition
        hide screen imageHut
        show addition without carry movie
        show screen skip_button
        $renpy.pause(22.0,hard=True)
    if video_choice == 4:
        image addition carry movie = Movie(play="addition_4.webm", loop=False)
        hide screen addition
        hide screen imageHut
        show addition carry movie
        show screen skip_button
        $renpy.pause(98.0,hard=True)
    if video_choice == 5:
        image subtraction easy movie = Movie(play="subtraction_1.webm", loop=False)
        hide screen subtraction
        hide screen imageHut
        show subtraction easy movie
        show screen skip_button
        $renpy.pause(104.0,hard=True)
    if video_choice == 6:
        image subtraction double movie = Movie(play="subtraction_2.webm", loop=False)
        hide screen subtraction
        hide screen imageHut
        show subtraction double movie
        show screen skip_button
        $renpy.pause(42.0,hard=True)
    if video_choice == 8:
        image comparison movie = Movie(play="grat.webm", loop=False)
        hide screen comparison
        hide screen imageHut
        show comparison movie
        show screen skip_button
        $renpy.pause(54.0,hard=True)
    queue music "audio/eric_matyas/RPG-Map-Music_Looping.mp3"

label instruct_for_quiz:
    scene bg castle entrance
    hide screen skip_button
    if video_choice in (1,2,3,4):
        show master1 thumbsup
        play sound "audio/dialogue_voice/m1_0.ogg"
        M1 "Demons have attacked the village,lets test what you have learnt with a small quiz of 5 questions."
        stop sound fadeout 1.0
    if video_choice in (5,6):
        show master3 thumbsup
        play sound "audio/dialogue_voice/m3_0.ogg"
        M3 "Demons have attacked the village,lets test what you have learnt with a small quiz of 5 questions."
        stop sound fadeout 1.0
    if video_choice == 8:
        show master2 thumbsup
        play sound "audio/dialogue_voice/m2_0.ogg"
        M2 "Demons have attacked the village,lets test what you have learnt with a small quiz of 5 questions."
        stop sound fadeout 1.0
    jump show_quiz

label show_quiz:
    scene black with dissolve
    jump get_question

label final_show_quiz:
    scene black with dissolve
    jump final_get_question
