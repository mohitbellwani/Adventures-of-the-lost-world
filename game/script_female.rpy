$ words_meaning = ""

label female_script_start:
    $ gender = "female"
    init python:
        def showMeaning():
            gui.about = ""
            for el in words_meaning:
                gui.about = gui.about + el[0] + " - " + el[1] + "\n"
    scene bg background_username
    show fmc hello:
        xalign 0.5
        yalign 0.5
    $ renpy.music.stop(fadeout=3.0)
    $ renpy.music.set_volume(0.5, delay=3, channel="music")
    queue music "audio/eric_matyas/RPG-Map-Music_Looping.mp3"

    #To take username
    $povname = ""
    $povname = renpy.input("What is your name?")
    $povname = povname.strip()

    if povname == "":
        $povname="Player" #to give default username

    hide fmc hello

    image tutorial_1 movie = Movie(play="tut_1.webm", loop=False)
    show tutorial_1 movie
    show screen skip_tut_button
    $renpy.pause(94.0,hard=True)

label female_script_continue:
    scene bg background_username

    show fmc talking:
        xalign 0.5
        yalign 0.5
        zoom 1.2

    $ words_meaning = [("finish","end"),("problem","something to worry about")]
    $ showMeaning()
    #starting prolauge
    play sound "audio/dialogue_voice/fmc_0.ogg"
    "I need to solve this problem to finish this for once and for all."
    stop sound fadeout 1.0

    $ renpy.movie_cutscene("Cutscenes/flash.webm")

    hide fmc talking

    scene bg forest with dissolve

    show fmc gettingup

    pause 2.1

    scene bg forest with dissolve

    show fmc thinking at left with moveinleft

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

label female_post_intro:
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

    # show master4 looking away:
    #     xalign 0.7
    #     yalign 0.5

    show fmc hand on waist with moveinright:
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

    hide master4 looking away with dissolve

    hide fmc hand on waist

    hide princess hand on waist

    show princess talking at left:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    show fmc dont know:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    play sound "audio/dialogue_voice/ps_2.ogg"

    $ words_meaning = [("situation","condition")]
    $ showMeaning()

    PS "I see this still may be a little hard to take all of this in so fast, I would be happy if you just accept the situation."

    stop sound fadeout 1.0

    hide princess talking

    hide fmc dont know

    show princess hand on waist:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    show fmc walkingrtl:
        xalign 1.0
        yalign 0.5
        linear 2.0 xpos 0.6
        zoom 1.2

    pause 2.0

    show fmc walkingltr:
        xalign 0.6
        yalign 0.5
        linear 2.0 xpos 0.9
        zoom 1.2

    pause 2.0

    hide fmc walkingltr

    show fmc dont know:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    play sound "audio/dialogue_voice/fmc_1.ogg"

    MC "What will happen now?, how did we get here?How do we go back?"

    stop sound fadeout 1.0

    hide princess hand on waist

    hide fmc dont know

    show princess talking at left:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    show fmc hand on waist:
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

    hide fmc hand on waist

    show princess hand on waist:
        xalign 0.1
        yalign 0.5
        zoom 1.2

    show fmc talking:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    play sound "audio/dialogue_voice/fmc_2.ogg"


    MC "So how do we get back?!!!!!!!\n([MC] speaks in panic state)"

    stop sound fadeout 1.0

    hide princess hand on waist

    hide fmc talking

    show princess talking at left:
        xalign 0.1
        yalign 0.5
        zoom 1.1

    show fmc looking away:
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

    hide fmc looking away

    show fmc talking:
        xalign 1.0
        yalign 0.5
        zoom 1.2

    show princess cross arms:
        xalign 0.1
        yalign 0.5
        zoom 1.1

    play sound "audio/dialogue_voice/fmc_3.ogg"

    MC "ok so how do we clear it?"

    stop sound fadeout 1.0

    hide fmc talking

    hide princess cross arms

    show princess talking at left:
        xalign 0.1
        yalign 0.5
        zoom 1.1

    show fmc thinking:
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

    show fmc walking away:
        xalign 0.4
        yalign 0.5

    show messenger walking away:
        xalign 0.5
        yalign 0.5

    pause 4.0

    scene black with dissolve

    "Next Day"

    scene bg walk

    show fmc walking close:
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

    show fmc hand on waist with moveinright:
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

    show fmc walking away

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
    hide tutorial_2 movie
    $ showMeaning()
    call screen imageHut
