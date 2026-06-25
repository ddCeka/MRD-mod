#*******************************************************************************#
#                                                PHONE STARTING SCREEN                                                        #
#*******************************************************************************#

label mainphonescreen:
    #call hide_all_phone_screens
    show screen mainphonescreen
    "" # Need this to function properly.
    jump mainphonescreen #Keeps the menu there if the player clicks another part of the screen
    return

label hidephonescreen:
    hide screen mainphonescreen
    return

# This part shows the main phone screen, and controls what happens when icons are clicked.
screen mainphonescreen:
    # layer "screens"
    modal True
    button:
        background Solid("#00000099")
        xysize(1920,1080)
    imagebutton xcenter 0.85 ycenter 0.5 idle "smartphone/smartphone.png" action NullAction()
    viewport id "phone_scroll":
        draggable True
        mousewheel True
        yinitial 0.0

    #------MAIN SCREEN-------#
    if active_screen == 0:
        if app_number == 0:
            $ appname = "App"
        elif app_number == 1:
            $ appname = "Messages"
        elif app_number == 2:
            $ appname = "Characters"
        elif app_number == 3:
            $ appname = "Special images"
        elif app_number == 4:
            $ appname = "Gallery"
        elif app_number == 5:
            $ appname = "Hints"
        elif app_number == 6:
            $ appname = "BGM"
        elif app_number == 99:
            $ appname = "Close"

        text appname xpos 0.74 ycenter 0.16 size 45

        imagebutton xcenter 0.774 ycenter 0.28 idle "smartphone/icons/message.png" action SetScreenVariable("active_screen", 1), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 1) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        if newmessage == True:
            add "smartphone/notification.png" xcenter 0.805 ycenter 0.222
        imagebutton xcenter 0.8496 ycenter 0.28 idle "smartphone/icons/characters.png" action SetScreenVariable("active_screen", 2), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 2) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.926 ycenter 0.28 idle "smartphone/icons/special images.png" action SetScreenVariable("active_screen", 0), SetScreenVariable("app_number", 0), ShowMenu("imagegallery"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 3) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.774 ycenter 0.415 idle "smartphone/icons/gallery.png" action SetScreenVariable("active_screen", 0), SetScreenVariable("app_number", 0), ShowMenu("scenegallery"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 4) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.8496 ycenter 0.415 idle "smartphone/icons/hints.png" action SetScreenVariable("active_screen", 5), SetVariable("newhint", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 5) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        if newhint == True:
            add "smartphone/notification.png" xcenter 0.957 ycenter 0.357
        # imagebutton xcenter 0.926 ycenter 0.415 idle "smartphone/icons/patreon.png" action SetScreenVariable("active_screen", 6), OpenURL("https://www.patreon.com/Lyk4n"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 6) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        # imagebutton xcenter 0.774 ycenter 0.55 idle "smartphone/icons/discord.png" action SetScreenVariable("active_screen", 7), OpenURL("https://discord.com/invite/dMj7pVc"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 7) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.926 ycenter 0.415 idle "smartphone/icons/music.png" action SetScreenVariable("active_screen", 9), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 6) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        # imagebutton xcenter 0.926 ycenter 0.55 idle "smartphone/icons/supporter.png" action SetScreenVariable("active_screen", 10), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 9) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.852 ycenter 0.92 idle "smartphone/icons/close.png" action SetScreenVariable("active_screen", 0), SetScreenVariable("app_number", 0), Hide("mainphonescreen"), With(Dissolve(0.2)) at Zoom(1.05, 1) hovered SetScreenVariable("app_number", 99) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"



            # imagebutton xcenter 0.852 ycenter 0.92 idle "smartphone/icons/close.png" action SetScreenVariable("active_screen", 0), SetScreenVariable("app_number", 0), Jump("hidephonescreen"), With(Dissolve(0.2)) at Zoom(1.05, 1) hovered SetScreenVariable("app_number", 8) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    #------MESSEGE SCREEN------#
    if active_screen == 1:
        viewport id "phone_scroll":
            draggable True
            mousewheel True
            yinitial 0.0
        if char_number == 0:
            $ charname = "Message"
        elif char_number == 1:
            $ charname = "[alice]"
        elif char_number == 2:
            $ charname = "[rin]"
        elif char_number == 3:
            $ charname = "[yui]"
        elif char_number == 4:
            $ charname = "[zeke]"
        elif char_number == 5:
            $ charname = "[krystal]"
        elif char_number == 6:
            $ charname = "[eira]"
        elif char_number == 7:
            $ charname = "[sally]"
        elif char_number == 8:
            $ charname = "[elaine]"
        elif char_number == 9:
            $ charname = "[wendy]"
        elif char_number == 10:
            $ charname = "[faye]"
        elif char_number == 11:
            $ charname = "[angela]"
        elif char_number == 99:
            $ charname = "Back"
        text charname xpos 0.74 ycenter 0.16 size 45
        if alice_newmessage == False:
            imagebutton xcenter 0.774 ycenter 0.28 auto "smartphone/message/alice_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "alice"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 1) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        else:
            imagebutton xcenter 0.774 ycenter 0.28 auto "smartphone/message/alice_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "alice"), SetVariable("alice_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 1) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        if rin_contact == False:
            imagebutton xcenter 0.8496 ycenter 0.28 idle "smartphone/message/unknown.png"
        else:
            if rin_newmessage == False:
                imagebutton xcenter 0.8496 ycenter 0.28 auto "smartphone/message/rin_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "rin"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 2) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            else:
                imagebutton xcenter 0.8496 ycenter 0.28 auto "smartphone/message/rin_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "rin"), SetVariable("rin_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 2) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        if yui_contact == False:
            imagebutton xcenter 0.926 ycenter 0.28 idle "smartphone/message/unknown.png"
        else:
            if yui_newmessage == False:
                imagebutton xcenter 0.926 ycenter 0.28 auto "smartphone/message/yui_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "yui"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 3) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            else:
                imagebutton xcenter 0.926 ycenter 0.28 auto "smartphone/message/yui_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "yui"), SetVariable("yui_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 3) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        if zeke_contact == False:
            imagebutton xcenter 0.774 ycenter 0.415 idle "smartphone/message/unknown.png"
        else:
            if zeke_newmessage == False:
                imagebutton xcenter 0.774 ycenter 0.415 auto "smartphone/message/zeke_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "zeke"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 4) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            else:
                imagebutton xcenter 0.774 ycenter 0.415 auto "smartphone/message/zeke_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "zeke"), SetVariable("zeke_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 4) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        if krystal_contact == False:
            imagebutton xcenter 0.8496 ycenter 0.415 idle "smartphone/message/unknown.png"
        else:
            if krystal_newmessage == False:
                imagebutton xcenter 0.8496 ycenter 0.415 auto "smartphone/message/krystal_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "krystal"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 5) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            else:
                imagebutton xcenter 0.8496 ycenter 0.415 auto "smartphone/message/krystal_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "krystal"), SetVariable("krystal_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 5) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        if eira_contact == False:
            imagebutton xcenter 0.926 ycenter 0.415 idle "smartphone/message/unknown.png"
        else:
            if eira_newmessage == False:
                imagebutton xcenter 0.926 ycenter 0.415 auto "smartphone/message/eira_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "eira"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 6) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            else:
                imagebutton xcenter 0.926 ycenter 0.415 auto "smartphone/message/eira_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "eira"), SetVariable("eira_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 6) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        if sally_contact == False:
            imagebutton xcenter 0.774 ycenter 0.55 idle "smartphone/message/unknown.png"
        else:
            if sally_newmessage == False:
                imagebutton xcenter 0.774 ycenter 0.55 auto "smartphone/message/sally_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "sally"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 7) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            else:
                imagebutton xcenter 0.774 ycenter 0.55 auto "smartphone/message/sally_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "sally"), SetVariable("sally_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 7) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        if elaine_contact == False:
            imagebutton xcenter 0.8496 ycenter 0.55 idle "smartphone/message/unknown.png"
        else:
            if elaine_newmessage == False:
                imagebutton xcenter 0.8496 ycenter 0.55 auto "smartphone/message/elaine_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "elaine"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 8) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            else:
                imagebutton xcenter 0.8496 ycenter 0.55 auto "smartphone/message/elaine_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "elaine"), SetVariable("elaine_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 8) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        if wendy_contact == False:
            imagebutton xcenter 0.926 ycenter 0.55 idle "smartphone/message/unknown.png"
        else:
            if wendy_newmessage == False:
                imagebutton xcenter 0.926 ycenter 0.55 auto "smartphone/message/wendy_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "wendy"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 9) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            else:
                imagebutton xcenter 0.926 ycenter 0.55 auto "smartphone/message/wendy_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "wendy"), SetVariable("wendy_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 9) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        if faye_contact == False:
            imagebutton xcenter 0.774 ycenter 0.685 idle "smartphone/message/unknown.png"
        else:
            if faye_newmessage == False:
                imagebutton xcenter 0.774 ycenter 0.685 auto "smartphone/message/faye_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "faye"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 10) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            else:
                imagebutton xcenter 0.774 ycenter 0.685 auto "smartphone/message/faye_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "faye"), SetVariable("faye_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 10) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        if angela_contact == False:
            imagebutton xcenter 0.8496 ycenter 0.685 idle "smartphone/message/unknown.png"
        else:
            if angela_newmessage == False:
                imagebutton xcenter 0.8496 ycenter 0.685 auto "smartphone/message/angela_message_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "angela"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 11) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            else:
                imagebutton xcenter 0.8496 ycenter 0.685 auto "smartphone/message/angela_newmessage_%s.png" action SetScreenVariable("active_screen", 8), SetScreenVariable("show_messages_of", "angela"), SetVariable("angela_newmessage", False), SetVariable("newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 10) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

        imagebutton xcenter 0.852 ycenter 0.92 idle "smartphone/icons/back.png" action SetScreenVariable("active_screen", 0), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 99) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    #-----------------Characters-----------------#
    elif active_screen == 2:
        viewport id "characters_scroll":
            draggable True
            mousewheel True
            yinitial 0.0
        if char_number == 0:
            $ charname = "Characters"
        elif char_number == 1:
            $ charname = "[alice]"
        elif char_number == 2:
            $ charname = "[rin]"
        elif char_number == 3:
            $ charname = "[yui]"
        elif char_number == 4:
            $ charname = "[zeke]"
        elif char_number == 5:
            $ charname = "[krystal]"
        elif char_number == 6:
            $ charname = "[eira]"
        elif char_number == 7:
            $ charname = "[sally]"
        elif char_number == 8:
            $ charname = "[elaine]"
        elif char_number == 9:
            $ charname = "[wendy]"
        elif char_number == 10:
            $ charname = "[faye]"
        elif char_number == 11:
            $ charname = "[angela]"
        elif char_number == 99:
            $ charname = "Back"
        text charname xpos 0.74 ycenter 0.16 size 45

        imagebutton xcenter 0.774 ycenter 0.28 auto "smartphone/message/alice_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 1), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 1) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.8496 ycenter 0.28 auto "smartphone/message/rin_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 2), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 2) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.926 ycenter 0.28 auto "smartphone/message/yui_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 3), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 3) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.774 ycenter 0.415 auto "smartphone/message/zeke_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 4), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 4) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.8496 ycenter 0.415 auto "smartphone/message/krystal_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 5), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 5) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.926 ycenter 0.415 auto "smartphone/message/eira_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 6), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 6) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.774 ycenter 0.55 auto "smartphone/message/sally_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 7), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 7) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.8496 ycenter 0.55 auto "smartphone/message/elaine_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 8), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 8) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.926 ycenter 0.55 auto "smartphone/message/wendy_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 9), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 9) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.774 ycenter 0.685 auto "smartphone/message/faye_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 10), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 10) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        if angela_contact == False:
            imagebutton xcenter 0.8496 ycenter 0.685 idle "smartphone/message/unknown.png"
        else:
            imagebutton xcenter 0.8496 ycenter 0.685 auto "smartphone/message/angela_message_%s.png" action SetScreenVariable("active_screen", 2), SetVariable("char_number", 11), ShowMenu("characters"), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 11) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton xcenter 0.852 ycenter 0.92 idle "smartphone/icons/back.png" action SetScreenVariable("active_screen", 0), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 99) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    #-------------------Hints--------------------#
    elif active_screen == 5:
        text appname xpos 0.74 ycenter 0.16 size 45
        frame:
            background None
            xpos 0.7325
            ypos 0.211
            side "c r":
                area (0, 0, 440, 745)
                viewport id "phone_scroll":
                    draggable True
                    mousewheel True
                    yinitial 0.0

                    vbox:
                        xminimum 425
                        spacing 4
                        if Whathappenedlastnight == False:
                            textbutton "- Talk to [zeke], and [rin] to find out if they knew about what happened last night." text_outlines [ (3,"#000000",0,0) ] text_size 30 style "hints"
                        elif Whathappenedlastnight == True and Truth == False:
                            textbutton "- Go to [yui]'s room." text_outlines [ (3,"#000000",0,0) ] text_size 30 style "hints"
                        if Truth == True:
                            textbutton ""
                        if backhome == True and ep3freeroam == False:
                            if ep2hiddenimages == False:
                                textbutton "- Collect hidden images([ep2hiddenimages_count]/7)(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep2hiddenimages == True:
                                textbutton "- Collect hidden images([ep2hiddenimages_count]/7)(Optional)" text_color "#818181" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep2rintalk == False:
                                textbutton "- Talk to [rin](Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep2rintalk == True:
                                textbutton "- Talk to [rin](Optional)" text_outlines [ (3,"#000000",0,0) ] text_color "#818181" text_size 25 style "hints"
                            if ep2yuitalk == False:
                                textbutton "- Talk to [yui](Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep2yuitalk == True:
                                textbutton "- Talk to [yui](Optional)" text_outlines [ (3,"#000000",0,0) ] text_color "#818181" text_size 25 style "hints"
                            if dinnerwithzeke == False:
                                textbutton "- Meet [zeke] at hallway(End free roam)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if dinnerwithzeke == True:
                                textbutton ""
                        if ep3freeroam == True and ep3endfreeroam == False:
                            if ep3hiddenimages == False:
                                textbutton "- Collect hidden images([ep3hiddenimages_count]/7)(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep3hiddenimages == True:
                                textbutton "- Collect hidden images([ep3hiddenimages_count]/7)(Optional)" text_color "#818181" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep3yuifavask == False or ep3yuihateask == False:
                                textbutton "- Talk to [yui](Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep3yuifavask == True and ep3yuihateask == True:
                                textbutton ""
                                textbutton "- Talk to [yui](Optional)" text_outlines [ (3,"#000000",0,0) ] text_color "#818181" text_size 25 style "hints"
                            if ep3breakfastwithrin == False:
                                textbutton "- Go to the kitchen(End free roam)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep3breakfastwithrin == True:
                                textbutton ""
                        if ep4freeroam == True and ep4endfreeroam == False:
                            if ep4hiddenimages == False:
                                textbutton "- Collect hidden images([ep4hiddenimages_count]/5)(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep4hiddenimages == True:
                                textbutton "- Collect hidden images([ep4hiddenimages_count]/5)(Optional)" text_color "#818181" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep4rintalk == False:
                                textbutton "- Talk to [rin]" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep4rintalk == True:
                                textbutton "- Talk to [rin]" text_color "#818181" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if krystalmeeteveryone == 1:
                                if ep4krystaltalk == False:
                                    textbutton "- Talk to [krystal]" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                                if ep4krystaltalk == True:
                                    textbutton "- Talk to [krystal]" text_color "#818181" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep4yuitalk == False:
                                textbutton "- Talk to [yui](End free roam)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep4yuitalk == True:
                                textbutton ""
                        if ch2ep1freeroam == True and ch2ep1endfreeroam == False:
                            if ep5hiddenimages == False:
                                textbutton "- Collect hidden images([ep5hiddenimages_count]/5)(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ep5hiddenimages == True:
                                textbutton "- Collect hidden images([ep5hiddenimages_count]/5)(Optional)" text_color "#818181" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            textbutton "- Roam around the place(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            textbutton "- Sneak to Rowan's bedroom(End free roam)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                        if ch2ep2freeroam == True and ch2ep2endfreeroam == False:
                            if ch2ep2hiddenimages == False:
                                textbutton "- Collect hidden images([ch2ep2hiddenimages_count]/7)(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ch2ep2hiddenimages == True:
                                textbutton "- Collect hidden images([ch2ep2hiddenimages_count]/7)(Optional)" text_color "#818181" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            textbutton "- Roam around the place(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            textbutton "- Go to Skylar's room(End free roam)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                        if ch2ep3freeroam == True and ch2ep3endfreeroam == False:
                            if ch2ep3hiddenimages == False:
                                textbutton "- Collect hidden images([ch2ep3hiddenimages_count]/5)(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ch2ep3hiddenimages == True:
                                textbutton "- Collect hidden images([ch2ep3hiddenimages_count]/5)(Optional)" text_color "#818181" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            textbutton "- Roam around the place(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            textbutton "- Go to the reception and leave the building(End free roam)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                        if ch2ep4freeroam == True and ch2ep4endfreeroam == False:
                            if ch2ep4hiddenimages == False:
                                textbutton "- Collect hidden images([ch2ep4hiddenimages_count]/5)(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            if ch2ep4hiddenimages == True:
                                textbutton "- Collect hidden images([ch2ep4hiddenimages_count]/5)(Optional)" text_color "#818181" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            textbutton "- Roam around the place(Optional)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                            textbutton "- Go to the front yard(End free roam)" text_outlines [ (3,"#000000",0,0) ] text_size 25 style "hints"
                vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        imagebutton xcenter 0.852 ycenter 0.92 idle "smartphone/icons/back.png" action SetScreenVariable("active_screen", 0), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 6) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    #----------Patreon----------#
    elif active_screen == 6:
        viewport id "phone_scroll":
            draggable True
            mousewheel True
            yinitial 0.0
        if char_number == 0:
            $ charname = "Appreciated"
        elif char_number == 99:
            $ charname = "Back"
        text charname xpos 0.74 ycenter 0.16 size 45
        imagebutton xcenter 0.852 ycenter 0.92 idle "smartphone/icons/back.png" action SetScreenVariable("active_screen", 0), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("char_number", 99) unhovered SetScreenVariable("char_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    #-------Message display--------#
    elif active_screen == 8:
        if show_messages_of == "alice":
            text "Alice" xpos 0.74 ycenter 0.16 size 45

            frame:
                background None
                xpos 0.7325
                ypos 0.211
                side "c r":
                    area (0, 0, 440, 700)

                    viewport id "phone_scroll":

                        draggable True
                        mousewheel True
                        yinitial 0.0

                        vbox:
                            xminimum 425
                            spacing 4
                            if alice_messages_show == True:
                                textbutton "Hey! What's up!?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                textbutton "It's been two days since we said good bye. How are you doing?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                if reply_alice1 == False:
                                    textbutton "[smgr]Be nice" action SetVariable("reply_alice1", True), SetVariable("alice_reply1_choice", 1), SetVariable("alice_newmessage", False), SetVariable("alice_relationship", alice_relationship + 1), SetVariable("alice_ch1_ep1", alice_ch1_ep1 + 1), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply1"
                                    textbutton "Be rude" action SetVariable("reply_alice1", True), SetVariable("alice_reply1_choice", 2), SetVariable("alice_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply2"
                                else:

                                    if alice_reply1_choice == 1:
                                        textbutton "Good. And you?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                        textbutton "Not bad. I'm busy writing a song right now :D" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        imagebutton:
                                            style "chat_left_without_margin"
                                            idle "smartphone/message/images/alice_selfie_small.jpg"
                                            action Function(renpy.show_screen, "show_message_image","alice_selfie")
                                        textbutton "I miss you :'(" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        textbutton "Keep focusing on your song writing so that you won't have time to miss me." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"

                                    elif alice_reply1_choice == 2:
                                        textbutton "Why do I have to tell you?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                        textbutton "Come on...don't be so mean..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        textbutton "I miss you :'(" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        textbutton "......" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                if alicemessage == True:
                                    imagebutton:
                                        style "chat_left_without_margin"
                                        idle "smartphone/message/images/alice_selfie1_small.jpg"
                                        action Function(renpy.show_screen, "show_message_image","alice_selfie1")
                                    textbutton "Morning!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "Are you awake yet?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "Yes. I woke up since 7 a.m. already." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "Wow, you woke up so fast!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "What are you doing now?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "Sitting at the beach." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "Really? Can you take a picture?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "I'd love to see if it's beautiful." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    if reply_alice2 == False:
                                        textbutton "[smgr]Take" action SetVariable("reply_alice2", True), SetVariable("alice_reply2_choice", 1), SetVariable("alice_newmessage", False), SetVariable("alice_relationship", alice_relationship + 2), SetVariable("alice_ch1_ep2", alice_ch1_ep2 + 2), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "Don't take" action SetVariable("reply_alice2", True), SetVariable("alice_reply2_choice", 2), SetVariable("alice_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if alice_reply2_choice == 1:
                                            textbutton "Okay..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            imagebutton:
                                                style "chat_right_without_margin"
                                                idle "smartphone/message/images/beachphoto_small.jpg"
                                                action Function(renpy.show_screen, "show_message_image","beachphoto")
                                            textbutton "So beautiful..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                            textbutton "I wish I was there with you." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        elif alice_reply2_choice == 2:
                                            textbutton "No." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Okay..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                if ep3_alicemessage1 == True:
                                    imagebutton:
                                        style "chat_right_without_margin"
                                        idle "smartphone/message/images/ep3_alice_selfie_small.jpg"
                                        action Function(renpy.show_screen, "show_message_image","ep3_alice_selfie")
                                    textbutton "I've been trying to write a song, but I'm struggling..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "Give me some motivation, please~?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    if ep3_reply_alice1 == False:
                                        textbutton "[smgr]Cheer her up" action SetVariable("ep3_reply_alice1", True), SetVariable("ep3_alice_reply1_choice", 1), SetVariable("alice_newmessage", False), SetVariable("alice_relationship", alice_relationship + 2), SetVariable("alice_ch1_ep3", alice_ch1_ep3 + 2), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "Ignore her" action SetVariable("ep3_reply_alice1", True), SetVariable("ep3_alice_reply1_choice", 2), SetVariable("alice_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if ep3_alice_reply1_choice == 1:
                                            textbutton "Fighting. You can do it." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Hehehe....Thanks!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                            textbutton "I think I'm starting to get some ideas now!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                            textbutton "That's good for you. Happy to help." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "You're so sweet! <3" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        elif ep3_alice_reply1_choice == 2:
                                            textbutton ""
                                if ep3_alicemessage2 == True:
                                    textbutton "Hehehe...guess what? I have a surprise for you soon...." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "What is it?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "You'll see it soon..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                if ep3_alicemessage3 == True:
                                    if ep3invitealice == 1:
                                        textbutton "I've just arrived home." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        textbutton "The negotiation with the company ended in a success!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        textbutton "Hehehe....This dress really gave me luck!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        imagebutton:
                                            style "chat_right_without_margin"
                                            if ep3alicedress == 1:
                                                idle "smartphone/message/images/ep3_alicewd_selfie_small.jpg"
                                                action Function(renpy.show_screen, "show_message_image","ep3_alicewd_selfie")
                                            elif ep3alicedress == 2:
                                                idle "smartphone/message/images/ep3_alicerd_selfie_small.jpg"
                                                action Function(renpy.show_screen, "show_message_image","ep3_alicerd_selfie")
                                            elif ep3alicedress == 3:
                                                idle "smartphone/message/images/ep3_alicebd_selfie_small.jpg"
                                                action Function(renpy.show_screen, "show_message_image","ep3_alicebd_selfie")
                                        textbutton "Today has been the best day of my life!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    elif ep3invitealice == 2:
                                        textbutton "You bastard...." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        textbutton "I HATE YOU!!!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                if ep4alicemessage == True:
                                    textbutton "Guess what!?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "I have a big surprise for you soon!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "Are you going to come see me again?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "No, I'm not...." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "But, I'm going to move there next week! Hehe!!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "....Seriously?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "Yes!! You remember the company that I had the negotiation with?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "They offered to hire me! I'm going to work for them soon!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "Congrats." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "Thanks! Alright, I've got to go. TTYLT." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                if ch2ep1alicemessage == True:
                                    textbutton "Hey. I've got some free time this evening." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "Can I go hang out at your place?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton ":)" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "Sorry. I'm busy tonight." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "We're going to our president's housewarming party." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "Oh..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "All good! Next time then!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                if ch2ep2alicemessage == True:
                                    textbutton "Hey. How are you doing?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "My company is looking for a composer to work with." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "I nominated your name. Are you interested?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "Of course, I am!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "But... Uhh..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "I don't know if it would be that easy. Let me ask my company first." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "I will give you answer later, okay?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "Aight. That's fair enough." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                if ch2ep2alicemessage2 == True:
                                    textbutton "Hey. I've just finished talking to [faye]." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "But, look. I know I told you that I wanted to meet you today." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "I'm sorry, but I can't now. I have to get back to my company." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    textbutton "Another time, okay?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                    if ch2ep2_reply_alice == False:
                                        textbutton "Yeah, another time." action SetVariable("ch2ep2_reply_alice", True), SetVariable("ch2ep2_alice_reply_choice", 1), SetVariable("alice_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 20 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "[smgr]Is everything alright?" action SetVariable("ch2ep2_reply_alice", True), SetVariable("ch2ep2_alice_reply_choice", 2), SetVariable("alice_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 20 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if ch2ep2_alice_reply_choice == 1:
                                            textbutton "Got it. Just tell me when you want to meet up then." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Roger that :D" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                        elif ch2ep2_alice_reply_choice == 2:
                                            textbutton "[smgr]Is everything alright?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Everything went so well. Don't worry :)" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                                            textbutton "Alright, let's meet up another time then." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Sure :D" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "alice_chat"
                    vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        elif show_messages_of == "rin":
            text "Rin" xpos 0.74 ycenter 0.16 size 45

            frame:
                background None
                xpos 0.7325
                ypos 0.211
                side "c r":
                    area (0, 0, 440, 700)

                    viewport id "phone_scroll":
                        draggable True
                        mousewheel True
                        yinitial 0.0

                        vbox:
                            xminimum 425
                            spacing 4
                            if rin_messages_show == True:
                                textbutton "Testing! Testing! Is this [mc]'s phone number?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                imagebutton:
                                    style "chat_left_without_margin"
                                    idle "smartphone/message/images/rin_selfie1_small.jpg"
                                    action Function(renpy.show_screen, "show_message_image", "rin_selfie1")
                                if ep3_rinmessage1 == True:
                                    imagebutton:
                                        style "chat_left_without_margin"
                                        idle "smartphone/message/images/rin_selfie2_small.jpg"
                                        action Function(renpy.show_screen, "show_message_image", "rin_selfie2")
                                    textbutton "I was about to watch TV, but then your face just popped up in my head." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                    textbutton "So, I wanna ask...Do you want to come down here to watch TV with me again?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                    if reply_rin1 == False:
                                        textbutton "[smgr]Okay" action SetVariable("reply_rin1", True), SetVariable("rin_reply1_choice", 1), SetVariable("rin_newmessage", False), SetVariable("rin_relationship", rin_relationship + 1), SetVariable("rin_ch1_ep3", rin_ch1_ep3 + 1), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "I'm busy" action SetVariable("reply_rin1", True), SetVariable("rin_reply1_choice", 2), SetVariable("rin_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if rin_reply1_choice == 1:
                                            textbutton "Yes, I do." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "I'll be there in a minute." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Yep! Roger that :D" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                            textbutton "I'll be waiting for you here!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                        elif rin_reply1_choice == 2:
                                            textbutton "I'm sorry, but I have more important thing to do." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Oh...Never mind then." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                if ep3_rinmessage2 == True:
                                    imagebutton:
                                        style "chat_left_without_margin"
                                        idle "smartphone/message/images/rin_selfie3_small.jpg"
                                        action Function(renpy.show_screen, "show_message_image", "rin_selfie3")
                                    textbutton "Good night!! <3" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                if ep3_rinmessage3 == True:
                                    textbutton "I've been pretty busy lately, so I can't have dinner with you guys." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                    textbutton "But, I cooked you a dinner, and put it in the refrigerator." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                    textbutton "Serve yourself, okay?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                if ep3_rinmessage4 == True:
                                    imagebutton:
                                        style "chat_left_without_margin"
                                        idle "smartphone/message/images/rin_selfie4_small.jpg"
                                        action Function(renpy.show_screen, "show_message_image", "rin_selfie4")
                                    textbutton "I'm so bored...." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                    textbutton "Can you come stay with me, please~?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                    if reply_rin2 == False:
                                        textbutton "[smgr]Accept" action SetVariable("reply_rin2", True), SetVariable("rin_reply2_choice", 1), SetVariable("rin_newmessage", False), SetVariable("rin_relationship", rin_relationship + 1), SetVariable("rin_ch1_ep3", rin_ch1_ep3 + 1), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "Refuse" action SetVariable("reply_rin2", True), SetVariable("rin_reply2_choice", 2), SetVariable("rin_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if rin_reply2_choice == 1:
                                            textbutton "Okay, I'll be there soon." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Hehe...Thanks!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                        elif rin_reply2_choice == 2:
                                            textbutton "No, I don't want to bother you." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "You should finish your project first." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "....Oh, okay...." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                if ch2ep2rinmessage == True:
                                    textbutton "Hey. Where are you now?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                    textbutton "You didn't come home last night." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                    textbutton "I tried to call you, but you didn't answer as well." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                                    textbutton "At least, answer my message. Everyone is worried about you." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "rin_chat"
                    vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        elif show_messages_of == "yui":
            text "Yui" xpos 0.74 ycenter 0.16 size 45
            frame:
                background None
                xpos 0.7325
                ypos 0.211
                side "c r":
                    area (0, 0, 440, 700)

                    viewport id "phone_scroll":
                        draggable True
                        mousewheel True
                        yinitial 0.0

                        vbox:
                            xminimum 425
                            spacing 4
                            if yui_messages_show == True:
                                if ch2ep2yuimessage == True:
                                    textbutton "Hey. Why didn't you come home last night?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "yui_chat"
                                    textbutton "Call me back after you see this message ASAP. We're worried about you." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "yui_chat"
                    vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        elif show_messages_of == "zeke":
            text "Zeke" xpos 0.74 ycenter 0.16 size 45
            frame:
                background None
                xpos 0.7325
                ypos 0.211
                side "c r":
                    area (0, 0, 440, 700)

                    viewport id "phone_scroll":
                        draggable True
                        mousewheel True
                        yinitial 0.0

                        vbox:
                            xminimum 425
                            spacing 4
                            if zeke_messages_show == True:
                                if ep3_sallyinvite == 1:
                                    textbutton "I won't be going home with you this evening. Don't wait for me." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "Hm? Why?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "zeke_chat"
                                    textbutton "I'm going to hang out with [sally] at her house." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "Hmmm....Are you guys dating?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "zeke_chat"
                                    textbutton "We aren't." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    textbutton "Alright, got it." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "zeke_chat"
                                if ch2ep2zekemessage == True:
                                    textbutton "Dude. Are you alright?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "zeke_chat"
                                    textbutton "It's getting late right now. Why aren't you coming back yet?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "zeke_chat"
                                    textbutton "Is there something bad happening to you?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "zeke_chat"
                    vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        elif show_messages_of == "krystal":
            text "Krystal" xpos 0.74 ycenter 0.16 size 45
            frame:
                background None
                xpos 0.7325
                ypos 0.211
                side "c r":
                    area (0, 0, 440, 700)

                    viewport id "phone_scroll":
                        draggable True
                        mousewheel True
                        yinitial 0.0

                        vbox:
                            xminimum 425
                            spacing 4
                            if krystal_messages_show == True:
                                textbutton "Hi! It's me, [krystal]." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                textbutton "Do you want to come hang out with me in my room?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                if reply_krystal1 == False:
                                    textbutton "[smgr]Okay" action SetVariable("reply_krystal1", True), SetVariable("krystal_reply1_choice", 1), SetVariable("krystal_newmessage", False), SetVariable("krystal_relationship", krystal_relationship + 1), SetVariable("krystal_ch1_ep3", krystal_ch1_ep3 + 1), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply1"
                                    textbutton "No, I'm busy" action SetVariable("reply_krystal1", True), SetVariable("krystal_reply1_choice", 2), SetVariable("krystal_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply2"
                                else:
                                    if krystal_reply1_choice == 1:
                                        textbutton "Okay." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                        textbutton "I'll be there in a minute." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                        textbutton "Lovely!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                        textbutton "Knock on my door five times, okay?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                        textbutton "So, I'll know that it's you!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                        textbutton "Alright, got it." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                    elif krystal_reply1_choice == 2:
                                        textbutton "I'm sorry, I'm pretty busy right now." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                        textbutton "Oh...Another time then." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                if ep3_krystalmessage2 == True:
                                    textbutton "Sorry about yesterday. I didn't mean to end it like that." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                    if reply_krystal2 == False:
                                        textbutton "[smgr]It's okay" action SetVariable("reply_krystal2", True), SetVariable("krystal_reply2_choice", 1), SetVariable("krystal_newmessage", False), SetVariable("krystal_relationship", krystal_relationship + 1), SetVariable("krystal_ch1_ep3", krystal_ch1_ep3 + 1), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "Don't answer" action SetVariable("reply_krystal2", True), SetVariable("krystal_reply2_choice", 2), SetVariable("krystal_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if krystal_reply2_choice == 1:
                                            textbutton "It's okay. Don't worry about it." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Thanks for understanding me." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                            textbutton "I promise that it won't happen again when we hang out next time." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                        if krystal_reply2_choice == 2:
                                            textbutton ""
                                if ep3_krystalmessage3 == True:
                                    textbutton "[mc]." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                    textbutton "Do you want to hang out with me again?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                    if reply_krystal3 == False:
                                        textbutton "[smgr]Accept" action SetVariable("reply_krystal3", True), SetVariable("krystal_reply3_choice", 1), SetVariable("krystal_newmessage", False), SetVariable("krystal_relationship", krystal_relationship + 1), SetVariable("krystal_ch1_ep3", krystal_ch1_ep3 + 1), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "Refuse" action SetVariable("reply_krystal3", True), SetVariable("krystal_reply3_choice", 2), SetVariable("krystal_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if krystal_reply3_choice == 1:
                                            textbutton "Okay. I'll be there soon." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Great! I'm waiting for you here then :)" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                        if krystal_reply3_choice == 2:
                                            textbutton "I'm sorry. I'm so tired today." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "I'm going to bed now." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Oh...Okay." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                if ep3_krystalmessage4 == True:
                                    textbutton "Can we hang out again?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                    if reply_krystal4 == False:
                                        textbutton "[smgr]Accept" action SetVariable("reply_krystal4", True), SetVariable("krystal_reply4_choice", 1), SetVariable("krystal_newmessage", False), SetVariable("krystal_relationship", krystal_relationship + 1), SetVariable("krystal_ch1_ep3", krystal_ch1_ep3 + 1), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "Refuse" action SetVariable("reply_krystal4", True), SetVariable("krystal_reply4_choice", 2), SetVariable("krystal_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if krystal_reply4_choice == 1:
                                            textbutton "Alright, give me five minutes." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Sure!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                        if krystal_reply4_choice == 2:
                                            textbutton "I'm sorry. I'm so exhausted today." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "I don't feel like hanging out with you now." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Got it...." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                if ch2ep2krystalmessage == True:
                                    textbutton "[mc]..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                    textbutton "Everyone is worried about you." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                                    textbutton "At least answer my message and tell me that you're okay." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "krystal_chat"
                    vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        elif show_messages_of == "eira":
            text "Eira" xpos 0.74 ycenter 0.16 size 45
        elif show_messages_of == "sally":
            text "Sally" xpos 0.74 ycenter 0.16 size 45

            frame:
                background None
                xpos 0.7325
                ypos 0.211
                side "c r":
                    area (0, 0, 440, 700)

                    viewport id "phone_scroll":
                        draggable True
                        mousewheel True
                        yinitial 0.0

                        vbox:
                            xminimum 425
                            spacing 4
                            if sally_messages_show == True:
                                if backhome == True:
                                    textbutton "What's up! It's me, [sally]!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "sally_chat"
                                    textbutton "I said I will buy you a meal, right? How about tomorrow evening?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "sally_chat"
                                    textbutton "How about tomorrow evening? Are you free?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "sally_chat"
                                    if reply_sally1 == False:
                                        textbutton "[smgr]Accept" action SetVariable("reply_sally1", True), SetVariable("sally_reply1_choice", 1), SetVariable("sally_newmessage", False), SetVariable("sally_relationship", sally_relationship + 1), SetVariable("sally_ch1_ep2_1", sally_ch1_ep2_1 + 1), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "replys1"
                                        textbutton "Reject" action SetVariable("reply_sally1", True), SetVariable("sally_reply1_choice", 2), SetVariable("sally_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "replys2"
                                    else:
                                        if sally_reply1_choice == 1:
                                            textbutton "Yes, I am." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Lovely. Then, I'll see you tomorrow!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "sally_chat"
                                            textbutton "See you." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                        elif sally_reply1_choice == 2:
                                            textbutton "I told you that you don't have to do it, didn't I?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "....But I want to return your favor." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "sally_chat"
                                            textbutton "You can do that by leaving me alone." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Alright, got it...." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "sally_chat"
                                    if ep3_sallymessage == True:
                                        textbutton "Come on...Hurry up!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "sally_chat"
                                        textbutton "We're waiting for you here xD" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "sally_chat"
                                        imagebutton:
                                            style "chat_left_without_margin"
                                            idle "smartphone/message/images/ep3_sally_selfie_small.jpg"
                                            action Function(renpy.show_screen, "show_message_image", "ep3_sally_selfie")
                                if ep4sallymessage == True:
                                    imagebutton:
                                        style "chat_left_without_margin"
                                        idle "smartphone/message/images/ep4_sally_selfie_small.jpg"
                                        action Function(renpy.show_screen, "show_message_image", "ep4_sally_selfie")
                                    textbutton "It was so much fun today. Thanks!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "sally_chat"
                                    textbutton "Let's do it again soon!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "sally_chat"
                    vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        elif show_messages_of == "elaine":
            text "Elaine" xpos 0.74 ycenter 0.16 size 45
        elif show_messages_of == "wendy":
            text "Wendy" xpos 0.74 ycenter 0.16 size 45
            frame:
                background None
                xpos 0.7325
                ypos 0.211
                side "c r":
                    area (0, 0, 440, 700)

                    viewport id "phone_scroll":
                        draggable True
                        mousewheel True
                        yinitial 0.0

                        vbox:
                            xminimum 425
                            spacing 4
                            if wendy_messages_show == True:
                                if ch2ep3wendymessage == True:
                                    textbutton "Are you done working?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "wendy_chat"
                                    textbutton "I'm waiting for you in front of the company building." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "wendy_chat"
                                    textbutton "On my way." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                if ch2ep3wendymessage2 == True:
                                    imagebutton:
                                        style "chat_left_without_margin"
                                        idle "smartphone/message/images/wendy_photosession_small.jpg"
                                        action Function(renpy.show_screen, "show_message_image", "wendy_photosession")
                                    textbutton "Hehe... I forgot to send this to you." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "wendy_chat"
                                    textbutton "Well done, [mc]. I really love this pic." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "wendy_chat"
                    vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        elif show_messages_of == "faye":
            text "Faye" xpos 0.74 ycenter 0.16 size 45
            frame:
                background None
                xpos 0.7325
                ypos 0.211
                side "c r":
                    area (0, 0, 440, 700)

                    viewport id "phone_scroll":
                        draggable True
                        mousewheel True
                        yinitial 0.0

                        vbox:
                            xminimum 425
                            spacing 4
                            if faye_messages_show == True:
                                if ch2ep1fayemessage == 1:
                                    textbutton "It's me, [faye]." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                    textbutton "I saw the news. It was you, right?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                    textbutton "Well done, [mc]." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                    textbutton "Now we can talk about hiring [krystal] to be our model." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                    textbutton "Let's talk tomorrow." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                    textbutton "Okay. See you tomorrow." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                if ch2ep2fayemessage == True:
                                    textbutton "Hey...." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                    textbutton "Would you like to have dinner together?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                    textbutton "I want to thank you for your help today." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                    if ch2ep2_reply_faye1 == False:
                                        textbutton "[smgr]Accept" action SetVariable("ch2ep2_reply_faye1", True), SetVariable("ch2ep2_reply_faye1_choice", 1), SetVariable("faye_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "Reject" action SetVariable("ch2ep2_reply_faye1", True), SetVariable("ch2ep2_reply_faye1_choice", 2), SetVariable("faye_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if ch2ep2_reply_faye1_choice == 1:
                                            textbutton "That sounds good to me." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Perfect." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                            textbutton "I'm waiting for you at the parking lot." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                            textbutton "Okay. I'll be there in five." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                        if ch2ep2_reply_faye1_choice == 2:
                                            textbutton "Thanks for inviting me, but..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "I'm sorry. I'm going to be busy this evening." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "That's fine. Don't worry about it." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                                            textbutton "Next time then." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "faye_chat"
                    vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        elif show_messages_of == "angela":
            text "Angela" xpos 0.74 ycenter 0.16 size 45
            frame:
                background None
                xpos 0.7325
                ypos 0.211
                side "c r":
                    area (0, 0, 440, 700)

                    viewport id "phone_scroll":
                        draggable True
                        mousewheel True
                        yinitial 0.0

                        vbox:
                            xminimum 425
                            spacing 4
                            if angela_messages_show == True:
                                if ch3ep4angelamessage == 1:
                                    textbutton "[mc]." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                                    textbutton "Thank you for taking care of me. I've recovered from illness now." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                                    textbutton "Are you free at noon? I want to buy you a meal." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                                    if ch3ep4_reply_angela == False:
                                        textbutton "[smgr]Accept" action SetVariable("ch3ep4_reply_angela", True), SetVariable("ch3ep4_reply_angela_choice", 1), SetVariable("angela_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "Reject" action SetVariable("ch3ep4_reply_angela", True), SetVariable("ch3ep4_reply_angela_choice", 2), SetVariable("angela_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if ch3ep4_reply_angela_choice == 1:
                                            textbutton "Okay." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Lovely. Come meet me at The Best Yakiniku at 12." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                                            textbutton "Understood." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                        if ch3ep4_reply_angela_choice == 2:
                                            textbutton "Thanks for inviting me, but..." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "I'm sorry. I'm busy today." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Oh... It's fine. No need to be sorry." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                                if ch4ep1angelamessage == 1:
                                    textbutton "[mc]. I'm sorry." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                                    textbutton "I can't go to the beach this weekend. I have to work at the company on Sunday." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                                    textbutton "But, I'm still free on Saturday. Do you still want to hangout?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                                    if ch4ep1_reply_angela == False:
                                        textbutton "[smgr]Accept" action SetVariable("ch4ep1_reply_angela", True), SetVariable("ch4ep1_reply_angela_choice", 1), SetVariable("angela_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                        textbutton "Reject" action SetVariable("ch4ep1_reply_angela", True), SetVariable("ch4ep1_reply_angela_choice", 2), SetVariable("angela_newmessage", False), With(Dissolve(0.2)) at Zoom(1.2, 1) text_outlines [ (3,"#000000",0,0) ] text_size 30 hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" style "reply"
                                    else:
                                        if ch4ep1_reply_angela_choice == 1:
                                            textbutton "Sure." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Lovely. Can you come meet me at my house at nine then?" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                                            textbutton "Got it." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "See you on Saturday!" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                                        if ch4ep1_reply_angela_choice == 2:
                                            textbutton "I don't think I can hangout with you on Saturday." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "chat_right"
                                            textbutton "Oh... It's alright." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "angela_chat"
                    vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        imagebutton xcenter 0.852 ycenter 0.92 idle "smartphone/icons/back.png" action SetScreenVariable("active_screen", 1), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 1) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

    #------------BGM lists--------------#
    elif active_screen == 9:
        text appname xpos 0.74 ycenter 0.16 size 45
        frame:
            background None
            xpos 0.7325
            ypos 0.211
            side "c r":
                area (0, 0, 440, 745)
                viewport id "phone_scroll":
                    draggable True
                    mousewheel True
                    yinitial 0.0

                    vbox:
                        xminimum 425
                        spacing 4
                        textbutton "Currently playing:" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "hints"
                        textbutton "[bgm]" text_outlines [ (3,"#000000",0,0) ] text_size 20 style "hints"
                vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        imagebutton xcenter 0.852 ycenter 0.92 idle "smartphone/icons/back.png" action SetScreenVariable("active_screen", 0), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 6) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

    #---------------Supporters-----------------#
    elif active_screen == 10:
        text appname xpos 0.74 ycenter 0.16 size 45
        frame:
            background None
            xpos 0.7325
            ypos 0.211
            side "c r":
                area (0, 0, 440, 745)
                viewport id "phone_scroll":
                    draggable True
                    mousewheel True
                    yinitial 0.0

                    vbox:
                        xminimum 425
                        spacing 4
                        textbutton "$20 patrons - Harrison, LucienSatanClaus, kev, Coil X Tesla, {font=Source Han Sans CN Light.otf}海锦 王{/font}, SEOK, Andrea Cutri." text_outlines [ (3,"#000000",0,0) ] text_color "#b9f2ff" text_size 20 style "hints"
                        textbutton "$10 patrons - Ray, SlavicBrah, gan gan, {font=Source Han Sans CN Light.otf}家宾 沈{/font}, Inori, Jihyun Joeng, Charlie, dianzhang233, {font=Source Han Sans CN Light.otf}剛 小{/font}, Benjamin, jdub, Arougnaunt, Banzai87, Michael Lyons, cestmir, {font=Source Han Sans CN Light.otf}光伟 刘{/font}, Michael Ray, Lusio, Stephen Foster, Kurotsuki Liu, medes, {font=빙그레 따옴체.ttf}진현 장{/font}, {font=Source Han Sans CN Light.otf}岭 黃{/font}, Herman Nijhof, Macario, Carl Theobald, Roque, Sehane, Aleaen Chang, Supreme DonutLord, John Cunningham, MuteButtonHero, Stéphane Titeux, ab, Msissy4, Awesomeknight, filip jacobs, Shadow, Alex, Sven Jäschke." text_outlines [ (3,"#000000",0,0) ] text_color "#FFD700" text_size 20 style "hints"
                        textbutton "and $5 patrons, $1 patrons." text_outlines [ (3,"#000000",0,0) ] text_size 20 style "hints"
                        textbutton "Thank you so much for showing your supports, and loves for me, and for this game! I'm very appreciated it!" text_outlines [ (3,"#000000",0,0) ] text_size 30 style "hints"
                        textbutton "And of course, we can't forget the admins who take care of our Discord community, An Amazing Username, duong, Pezzo, robtheweedman29_" text_outlines [ (3,"#000000",0,0) ] text_size 30 style "hints"
                        textbutton "Also a big THANKS to Sasha Rose for proof reading the game." text_size 20 style "hints"
                        

                vbar xcenter 1.2 ycenter 0.5 value YScrollValue("phone_scroll")
        imagebutton xcenter 0.852 ycenter 0.92 idle "smartphone/icons/back.png" action SetScreenVariable("active_screen", 0), With(Dissolve(0.2)) at Zoom(1.2, 1) hovered SetScreenVariable("app_number", 6) unhovered SetScreenVariable("app_number", 0) hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
