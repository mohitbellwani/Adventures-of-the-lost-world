image white_background = Solid("#fff")

default bag = []
default money = 0
default choice = ""
default question_no = 1
default final_quiz_count = 1
default quiz_display_counter = 0
default final_display_counter = 0
default finale_money_count = 0
default question = {}
default question_el = []
default fruits_list = ["apple","pineapple"]
default content_unlocked = 1

default add_2_flag = True
default add_3_flag = True
default add_4_flag = True
default sub_1_flag = True
default sub_2_flag = True
default comp_flag = True
default final_quiz_flag = True

default gender = ""
default video_choice = 1


style mytextbutton:
    color "#ff0000"
    hover_color "#000"
    #selected_color "#ff0"

style option_button:
    color "#fff"
    hover_color "#abc"


style learn_textbutton:
    color "#abc"
    hover_color "#fff"

style disabled_learn_textbutton:
    color "#abc"

style quick_learn_textbutton:
    size 35
    color "#fff"
    hover_color "#faad12"

style quiz_exit_textbutton:
    size 35
    color "#faad12"
    hover_color "#fff"

style button_quick_menu:
    color "#ff0000"
    hover_color "#fff"
    size 35


label splashscreen:
    $ renpy.movie_cutscene('splash.webm')
    return

screen skip_tut_button:
    if gender == "male":
        textbutton "Skip":
            text_style "mytextbutton"
            action Hide("skip_tut_button"),Jump("male_script_continue")
    if gender == "female":
        textbutton "Skip":
            text_style "mytextbutton"
            action Hide("skip_tut_button"),Jump("female_script_continue")

screen skip_tut2_button:
    textbutton "Skip":
        text_style "mytextbutton"
        action Hide("skip_tut2_button"), Return(0)


screen skip_intro_button:
    if gender == "male":
        textbutton "Skip":
            text_style "mytextbutton"
            action Hide("skip_intro_button"), Jump("male_post_intro")
    if gender == "female":
        textbutton "Skip":
            text_style "mytextbutton"
            action Hide("skip_intro_button"), Jump("female_post_intro")

label start:
    init:
        $ timer_range = 0
        $ timer_jump = 0

        image add_1_hover:
            im.Scale("addition_1.png",550,250)
            ease 1.2 zoom 1.12
        image add_2_hover:
            im.Scale("addition_2.png",550,250)
            ease 1.2 zoom 1.12
        image add_3_hover:
            im.Scale("addition_3.png",550,250)
            ease 1.2 zoom 1.12
        image add_4_hover:
            im.Scale("addition_4.png",550,250)
            ease 1.2 zoom 1.12
        image sub_1_hover:
            im.Scale("subtraction_1.png",550,250)
            ease 1.2 zoom 1.12
        image sub_2_hover:
            im.Scale("subtraction_2.png",550,250)
            ease 1.2 zoom 1.12
        image comp_hover:
            im.Scale("grat.png",550,250)
            ease 1.2 zoom 1.12
        image lesson_hut_hover:
            "bg village2 icon.png"
            ease 1.2 zoom 1.12
    show screen game_bar
    call screen choose_character
    return

label male_script_start:
    $ gender = "male"
    init python:
        def showMeaning():
            gui.about = ""
            for el in words_meaning:
                gui.about = gui.about + el[0] + " - " + el[1] + "\n"

        def set_message():
            global add_2_flag, add_3_flag, add_4_flag, sub_1_flag, sub_2_flag, comp_flag, final_quiz_flag, video_choice, content_unlocked
            if add_2_flag and money >= 4:
                add_2_flag = False
                return "Single Digit(Difficult)"

            if add_3_flag and money >= 8:
                add_3_flag = False
                return "Double Digit(No Carry Over)"

            if add_4_flag and money >= 13:
                add_4_flag = False
                return "Double Digit(Carry Over)"

            if video_choice == 4 and sub_1_flag and money >= 16:
                content_unlocked = content_unlocked + 1
                sub_1_flag = False
                return "Subtraction"

            if sub_2_flag and money >= 21:
                sub_2_flag = False
                return "Double Digit(Easy)"

            if video_choice == 6 and comp_flag and money >= 23:
                content_unlocked = content_unlocked + 1
                comp_flag = False
                return "Comparison"

            if video_choice == 8 and final_quiz_flag and money >= 25:
                content_unlocked = content_unlocked + 1
                final_quiz_flag = False
                return "Final Quiz"


    scene bg background_username
    show mc hello:
        xalign 0.5
        yalign 0.5
    $ renpy.music.stop(fadeout=3.0)
    $ renpy.music.set_volume(0.4, delay=3, channel="music")
    queue music "audio/eric_matyas/RPG-Map-Music_Looping.mp3"

    #To take username
    $povname = ""
    $povname = renpy.input("What is your name?")
    $povname = povname.strip()

    if povname == "":
        $povname="Player" #to give default username

    hide mc hello

    image tutorial_1 movie = Movie(play="tut_1.webm", loop=False)
    show tutorial_1 movie
    show screen skip_tut_button
    $renpy.pause(94.0,hard=True)

label male_script_continue:
    scene bg background_username

    show mc talking:
        xalign 0.5
        yalign 0.5
        zoom 1.2

    $ words_meaning = [("finish","end"),("problem","something to worry about")]
    $ showMeaning()


    #starting prolauge
    play sound "audio/dialogue_voice/mc_0.ogg"
    "I need to solve this problem to finish this for once and for all."
    stop sound fadeout 1.0


    $ renpy.movie_cutscene("Cutscenes/flash.webm")

    hide mc talking

    scene bg forest with dissolve

    show mc gettingup

    pause 2.1

    scene bg forest with dissolve

    show mc cross arms at left with moveinleft

    show messenger talking at right with moveinright

    play sound "audio/dialogue_voice/msg_1.ogg"

    $ words_meaning = [("explain","tell something important"),("situation","condition")]
    $ showMeaning()

    MSG "Hii [MC] I will explain the situation now."

    stop sound fadeout 1.0

    window hide
    image intro movie = Movie(play="intro.webm", loop=False)
    show intro movie
    show screen skip_intro_button
    $renpy.pause(37.0,hard=True)

label male_post_intro:
    scene bg castle entrance with dissolve

    show soldier1 salute at left

    show soldier2 salute at right

    play sound "audio/dialogue_voice/msg_2.ogg"

    "Welcome to the Castle"

    stop sound fadeout 1.0

    scene bg throne room with dissolve

    show princess talking at left:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    show master1 thinking:
        xalign 0.4
        yalign 0.5

    show master2 cross arms:
        xalign 0.5
        yalign 0.5

    show master3 dont know:
        xalign 0.6
        yalign 0.5

    show mc idle with moveinright:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    $ words_meaning = [("arrived","to reach a place"),("journey","travelling from one place to another"), ("situation","condition")]
    $ showMeaning()

    play sound "audio/dialogue_voice/ps_1.ogg"

    PS "Finally the heroes from another world you have arrived  hope you had a safe
        journey here, I guess my messenger explained to you the situation we are in."

    stop sound fadeout 1.0

    hide princess talking

    show princess hand on waist:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    "All" "(we didn't speak at all as we were still trying to take everything in)"

    hide master1 thinking with dissolve

    hide master2 cross arms with dissolve

    hide master3 dont know with dissolve

    hide mc idle

    hide princess hand on waist

    show princess talking at left:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    show mc dont know:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    play sound "audio/dialogue_voice/ps_2.ogg"

    $ words_meaning = [("situation","condition")]
    $ showMeaning()

    PS "I see this still may be a little hard to take all of this in so fast, I would be happy if you just accept the situation."

    stop sound fadeout 1.0

    hide princess talking

    hide mc dont know

    show princess hand on waist:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    show mc walkingrtl:
        xalign 1.0
        yalign 0.5
        linear 2.0 xpos 0.6
        zoom 1.2

    pause 2.0

    show mc walkingltr:
        xalign 0.6
        yalign 0.5
        linear 2.0 xpos 0.9
        zoom 1.2

    pause 2.0

    hide mc walkingltr

    show mc dont know:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    play sound "audio/dialogue_voice/mc_1.ogg"

    MC "What will happen now?, how did we get here?How do we go back?"

    stop sound fadeout 1.0

    hide princess hand on waist

    hide mc dont know

    show princess talking at left:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    show mc cross arms:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    play sound "audio/dialogue_voice/ps_3.ogg"

    $ words_meaning = [("summoned","to call to a place"),("labyrinth","a` maze or a puzzle")]
    $ showMeaning()

    PS "I see you don’t have to worry you have neither dead nor been kidnaped,
        it's just we have summoned you here to help us solve this labyrinth."

    stop sound fadeout 1.0

    hide princess talking

    hide mc cross arms

    show princess hand on waist:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    show mc talking:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    play sound "audio/dialogue_voice/mc_2.ogg"

    MC "So how do we get back?!!!!!!!\n([MC] speaks in panic state)"

    stop sound fadeout 1.0

    hide princess hand on waist

    hide mc talking

    show princess talking at left:
        xalign 0.1
        yalign 0.5
        zoom 1.1

    show mc cross arms:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    play sound "audio/dialogue_voice/ps_4.ogg"

    $ words_meaning = [("labyrinth","a maze or a puzzle")]
    $ showMeaning()

    PS "well I am getting there just calm down kiddo,
        so to get back you have to clear the Labyrinth and at the end of it you will find the door to your world."

    stop sound fadeout 1.0

    hide princess talking

    hide mc cross arms

    show mc talking:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    show princess cross arms:
        xalign 0.1
        yalign 0.5
        zoom 1.1

    play sound "audio/dialogue_voice/mc_3.ogg"

    MC "ok so how do we clear it?"

    stop sound fadeout 1.0

    hide mc talking

    hide princess cross arms

    show princess talking at left:
        xalign 0.1
        yalign 0.5
        zoom 1.1

    show mc dont know:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    play sound "audio/dialogue_voice/ps_5.ogg"

    $ words_meaning = [("scared","to be afraid"),("labyrinth","a maze or a puzzle"), ("suppose","to asume or a guess")]
    $ showMeaning()

    PS "Well I suppose you are scared and tired too so you should take it easy today and take some rest.
        I promise I will explain you how to clear the labyrinth."

    stop sound fadeout 1.0

    play sound "audio/dialogue_voice/ps_6.ogg"

    PS "Now [SV1] will escort you all to Your rooms."

    stop sound fadeout 1.0

    scene bg walk

    show mc walking away:
        xalign 0.4
        yalign 0.5

    show messenger walking away:
        xalign 0.5
        yalign 0.5

    pause 4.0

    scene black with dissolve

    "Next Day"

    scene bg walk

    show mc walking close:
        xalign 0.4
        yalign 0.5

    show messenger walking close:
        xalign 0.5
        yalign 0.5

    pause 4.0

    scene bg throne room with dissolve

    show princess talking at left:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    show mc poseing with moveinright:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    play sound "audio/dialogue_voice/ps_7.ogg"

    $ words_meaning = [("hope","to belive")]
    $ showMeaning()

    PS "I hope you had a good night sleep."

    stop sound fadeout 1.0

    play sound "audio/dialogue_voice/ps_8.ogg"

    $ words_meaning = [("summoned","to call to a place"),("wisdom","intellect or smartness")]
    $ showMeaning()

    PS "[MC] We have summoned you to save our world from this war of wisdom between us and the monsters."

    stop sound fadeout 1.0

    show master1 thinking with dissolve:
        xalign 0.4
        yalign 0.5

    show master2 cross arms with dissolve:
        xalign 0.5
        yalign 0.5

    show master3 dont know with dissolve:
        xalign 0.6
        yalign 0.5

    play sound "audio/dialogue_voice/ps_9.ogg"

    $ words_meaning = [("hope","to belive"),("battle","a fight"), ("master","to learn")]
    $ showMeaning()

    PS "You are our last hope but before you head into the battle you should master the skills from your friends [M1] [M2] [M3]."

    stop sound fadeout 1.0

    scene bg walk

    show mc walking away

    pause 2.0

    scene bg village1

    $ words_meaning = [("learning","understanding knowledge"),("topic","a subject")]
    $ showMeaning()

    "Tutorial" "Click on the screen to begin the tutorial."
    window hide
    image tutorial_2 movie = Movie(play="tut_2.webm", loop=False)
    show tutorial_2 movie
    show screen skip_tut2_button
    $renpy.pause(70.0,hard=True)
    $ showMeaning()
    hide tutorial_2 movie
    call screen imageHut
