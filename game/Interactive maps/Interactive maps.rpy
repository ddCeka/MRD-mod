screen HouseEp1Ch1:
    if area == "MCRoom":
        if MCRoom_Pic1 == False:
            add "Ch.1/Ep.1/Interactive maps/MCRoom_Photo.jpg"
            imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/MCRoom_Door_%s.png" focus_mask True action[SetVariable("area", "Second floor1"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
            imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/MCRoom_Picture_%s.png" focus_mask True action Jump("MCRoom_Pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
            text "{b}(1){/b}" pos(0.95, 0.1) style "smgrout"
            text "{b}(2) Special Image -->{/b}" pos(0.57, 0.775) style "smgrout"
            text "{b}(3){/b}" pos(0.35, 0.2) style "smgrout"
        else:
            add "Ch.1/Ep.1/Interactive maps/MCRoom.jpg"
            imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/MCRoom_Door_%s.png" focus_mask True action[SetVariable("area", "Second floor1"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    elif area == "ZekeRoom":
        add "Ch.1/Ep.1/Interactive maps/Zeke_Room.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Zeke_Room_%s.png" focus_mask True action Jump("ZekeTalk") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Zeke_Room_Leave_%s.png" focus_mask True action[SetVariable("area", "Second floor1"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    elif area == "RinRoom":
        if RinRoom_Pic1 == False:
            add "Ch.1/Ep.1/Interactive maps/RinRoom_Photo.jpg"
            imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/RinRoom_Pic1_%s.png" focus_mask True action Jump("RinRoom_Pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
            text "{b}<-- Special Image{/b}" pos(0.04, 0.92) style "smgrout"
        else:
            add "Ch.1/Ep.1/Interactive maps/RinRoom.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/RinRoom_Back_%s.png" focus_mask True action[SetVariable("area", "BeforeRin"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/RinRoom_Talk_%s.png" focus_mask True action Jump("RinTalk") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        text "{b}[rin]'s Room{/b}" pos(0.5, 0.005) style "smgrout"
        text "{b}Back{/b}" pos(0.02, 0.4355) style "smgrout"
    elif area == "Second floor1":
        add "Ch.1/Ep.1/Interactive maps/SecondFloor1.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/SecondFloor1_MCDoor_%s.png" focus_mask True action[SetVariable("area", "MCRoom"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/SecondFloor1_ZekeDoor_%s.png" focus_mask True action[SetVariable("area", "ZekeRoom"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/SecondFloor1_YuiDoor_%s.png" focus_mask True action[SetVariable("area", "YuiRoom"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/SecondFloor1_Stair_%s.png" focus_mask True action[SetVariable("area", "First floor"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/SecondFloor1_Back_%s.png" focus_mask True action[SetVariable("area", "Second floor2"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        text "{b}[yui]'s Room{/b}" pos(0.7, 0.4) style "smgrout"
        text "{b}[zeke]'s Room{/b}" pos(0.53, 0.15) style "smgrout"
        text "{b}<-- MC's Room{/b}" pos(0.39, 0.2) style "smgrout"
        text "{b}First Floor{/b}" pos(0.1, 0.77) style "smgrout"
    elif area == "Second floor2":
        add "Ch.1/Ep.1/Interactive maps/SecondFloor2.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/SecondFloor2_YuiDoor_%s.png" focus_mask True action[SetVariable("area", "YuiRoom"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/SecondFloor2_KrystalDoor_%s.png" focus_mask True action[SetVariable("area", "KrystalRoom"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/SecondFloor2_Stair_%s.png" focus_mask True action[SetVariable("area", "First floor"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/SecondFloor2_Back_%s.png" focus_mask True action[SetVariable("area", "Second floor1"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        text "{b}[yui]'s Room{/b}" pos(0.23, 0.4) style "smgrout"
        text "{b}Inaccesible{/b}" pos(0.45, 0.2) style "smgrout"
        text "{b}First Floor{/b}" pos(0.68, 0.6) style "smgrout"
    elif area == "First floor":
        add "Ch.1/Ep.1/Interactive maps/Entrance.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Entrance_Stair_%s.png" focus_mask True action[SetVariable("area", "Second floor1"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Entrance_MainhallDoor_%s.png" focus_mask True action[SetVariable("area", "Mainhall"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        text "{b}Entrance{/b}" pos(0.5, 0.005) style "smgrout"
        text "{b}To Main Hall{/b}" pos(0.48, 0.4) style "smgrout"
        text "{b}Second Floor{/b}" pos(0.8, 0.4) style "smgrout"
    elif area == "Mainhall":
        if Mainhall_Pic1 == False:
            add "Ch.1/Ep.1/Interactive maps/Mainhall_Photo.jpg"
            imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Mainhall_Pic1_%s.png" focus_mask True action Jump("Mainhall_Pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
            text "{b}<-- Special Image{/b}" pos(0.5, 0.96) style "smgrout"
        else:
            add "Ch.1/Ep.1/Interactive maps/Mainhall.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Mainhall_Garage_%s.png" focus_mask True action[SetVariable("area", "Garage"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Mainhall_Playroom_%s.png" focus_mask True action[SetVariable("area", "Playroom"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Mainhall_LivDoor_%s.png" focus_mask True action[SetVariable("area", "Livingroom"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Mainhall_Entrance_%s.png" focus_mask True action[SetVariable("area", "First floor"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        text "{b}Main Hall{/b}" pos(0.5, 0.005) style "smgrout"
        text "{b}To Garage{/b}" pos(0.81, 0.35) style "smgrout"
        text "{b}To Play Room{/b}" pos(0.45, 0.35) style "smgrout"
        text "{b}To Entrance{/b}" pos(0.88, 0.492) style "smgrout"
        text "{b}To{/b}" pos(0.74, 0.88) style "smgrout"
        text "{b}Living{/b}" pos(0.723, 0.91) style "smgrout"
        text "{b}Room{/b}" pos(0.725, 0.94) style "smgrout"
    elif area == "Garage":
        add "Ch.1/Ep.1/Interactive maps/Garage.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Garage_Back_%s.png" focus_mask True action[SetVariable("area", "Mainhall"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        text "{b}Garage{/b}" pos(0.5, 0.005) style "smgrout"
        text "{b}To{/b}" pos(0.927, 0.88) style "smgrout"
        text "{b}Main{/b}" pos(0.927, 0.91) style "smgrout"
        text "{b}Hall{/b}" pos(0.927, 0.94) style "smgrout"
    elif area == "Playroom":
        add "Ch.1/Ep.1/Interactive maps/Playroom.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Playroom_Back_%s.png" focus_mask True action[SetVariable("area", "Mainhall"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        text "{b}Play Room{/b}" pos(0.5, 0.005)
    elif area == "Livingroom":
        if Livingroom_Pic1 == False:
            add "Ch.1/Ep.1/Interactive maps/Livingroom_Photo.jpg"
            imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Livingroom_Pic1_%s.png" focus_mask True action Jump("Livingroom_Pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
            text "{b}<-- Special Image{/b}" pos(0.187, 0.723) style "smgrout"
        else:
            add "Ch.1/Ep.1/Interactive maps/Livingroom.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Livingroom_Kitchen_%s.png" focus_mask True action[SetVariable("area", "Kitchen"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Livingroom_Brin_%s.png" focus_mask True action[SetVariable("area", "BeforeRin"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Livingroom_Back_%s.png" focus_mask True action[SetVariable("area", "Mainhall"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        text "{b}Living Room{/b}" pos(0.45, 0.1) style "smgrout"
        text "{b}To Kitchen{/b}" pos(0.88, 0.792) style "smgrout"
        text "{b}To{/b}" pos(0.394, 0.88) style "smgrout"
        text "{b}Main{/b}" pos(0.382, 0.91) style "smgrout"
        text "{b}Hall{/b}" pos(0.385, 0.94) style "smgrout"
        text "{b}To [rin]'s Room{/b}" pos(0.005, 0.405) style "smgrout"
    elif area == "Kitchen":
        add "Ch.1/Ep.1/Interactive maps/Kitchen.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Kitchen_Back_%s.png" focus_mask True action[SetVariable("area", "Livingroom"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        text "{b}Kitchen{/b}" pos(0.45, 0.005) style "smgrout"
        text "{b}To{/b}" pos(0.886, 0.88) style "smgrout"
        text "{b}Living{/b}" pos(0.866, 0.91) style "smgrout"
        text "{b}Room{/b}" pos(0.867, 0.94) style "smgrout"
    elif area == "BeforeRin":
        if BeforeRinRoom_Pic1 == False:
            add "Ch.1/Ep.1/Interactive maps/Before_Rinroom_Photo.jpg"
            imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Before_Rinroom_Pic1_%s.png" focus_mask True action Jump("BeforeRinRoom_Pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
            text "{b}<-- Special Image{/b}" pos(0.22, 0.552) style "smgrout"
        else:
            add "Ch.1/Ep.1/Interactive maps/Before_Rinroom.jpg"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Before_Rinroom_Back_%s.png" focus_mask True action[SetVariable("area", "Livingroom"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.1/Interactive maps/Interactive objects/Before_Rinroom_RinDoor_%s.png" focus_mask True action[SetVariable("area", "RinRoom"), Jump("House")] hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        text "{b}Before [rin]'s Room{/b}" pos(0.45, 0.005) style "smgrout"
        text "{b}To{/b}" pos(0.915, 0.86) style "smgrout"
        text "{b}Living{/b}" pos(0.9, 0.89) style "smgrout"
        text "{b}Room{/b}" pos(0.9, 0.92) style "smgrout"
    vbox:
        if phone_alert == True:
            imagebutton auto "smartphone/smartphone_alert_icon_%s.png" xpos 1800 ypos 50 focus_mask True action SetVariable("phone_alert", False), Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        elif phone_alert == False:
            imagebutton auto "smartphone/smartphone_icon_%s.png" xpos 1800 ypos 50 focus_mask True action Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

screen ep2house:
    if area == "mcroom":
        if ep2mcroom_pic == False:
            add "Ch.1/Ep.2/Interactive maps/ep2_mcroom_photo.jpg"
            imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_mcroom_pic_%s.png" focus_mask True action Jump("ep2_mcroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.2/Interactive maps/ep2_mcroom.jpg"
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_mcroom_bed_%s.png" focus_mask True action Jump("mcbed") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "zekeroom":
        add "Ch.1/Ep.2/Interactive maps/ep2_zekeroom.jpg"
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_zekeroom_shelf_%s.png" focus_mask True action Jump("zeke_bookshelf") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "yuiroom":
        if ep2yuiroom_pic == False:
            add "Ch.1/Ep.2/Interactive maps/ep2_yuiroom_photo.jpg"
            imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_yuiroom_pic_%s.png" focus_mask True action Jump("ep2_yuiroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.2/Interactive maps/ep2_yuiroom.jpg"
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_yuiroom_yui_%s.png" focus_mask True action Jump("ep2_yuiroom_talk") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "rinroom":
        if ep2rinroom_pic1 == False and ep2rinroom_pic2 == False:
            add "Ch.1/Ep.2/Interactive maps/ep2_rinroom_photos.jpg"
            imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_rinroom_pic1_%s.png" focus_mask True action Jump("ep2_rinroom_pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
            imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_rinroom_pic2_%s.png" focus_mask True action Jump("ep2_rinroom_pic2") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        if ep2rinroom_pic1 == True and ep2rinroom_pic2 == False:
            add "Ch.1/Ep.2/Interactive maps/ep2_rinroom_photo2.jpg"
            imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_rinroom_pic2_%s.png" focus_mask True action Jump("ep2_rinroom_pic2") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        if ep2rinroom_pic1 == False and ep2rinroom_pic2 == True:
            add "Ch.1/Ep.2/Interactive maps/ep2_rinroom_photo1.jpg"
            imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_rinroom_pic1_%s.png" focus_mask True action Jump("ep2_rinroom_pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        elif ep2rinroom_pic1 == True and ep2rinroom_pic2 == True:
            add "Ch.1/Ep.2/Interactive maps/ep2_rinroom.jpg"
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_rinroom_rin_%s.png" focus_mask True action Jump("ep2_rinroom_talk") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_rinroom_closet_%s.png" focus_mask True action Jump("ep2_rinroom_closet") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "livroom":
        if ep2livroom_pic == False:
            add "Ch.1/Ep.2/Interactive maps/ep2_livingroom_photo.jpg"
            imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_livingroom_pic_%s.png" focus_mask True action Jump("ep2_livroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.2/Interactive maps/ep2_livingroom.jpg"
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_livingroom_sofa_%s.png" focus_mask True action Jump("ep2_livroom_sofa") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "kitchen":
        if ep2kitchen_pic == False:
            add "Ch.1/Ep.2/Interactive maps/ep2_kitchen_photo.jpg"
            imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_kitchen_pic_%s.png" focus_mask True action Jump("ep2_kitchen_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.2/Interactive maps/ep2_kitchen.jpg"
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_kitchen_microwave_%s.png" focus_mask True action Jump("ep2_kitchen_microwave") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "garage":
        if ep2garage_pic == False:
            add "Ch.1/Ep.2/Interactive maps/ep2_garage_photo.jpg"
            imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_garage_pic_%s.png" focus_mask True action Jump("ep2_garage_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.2/Interactive maps/ep2_garage.jpg"
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_garage_car_%s.png" focus_mask True action Jump("ep2_garage_car") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "hallway":
        add "Ch.1/Ep.2/Interactive maps/ep2_hallway.jpg"
    vbox:
        if phone_alert == True:
            imagebutton auto "smartphone/smartphone_alert_icon_%s.png" xpos 1800 ypos 50 focus_mask True action SetVariable("phone_alert", False), Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        elif phone_alert == False:
            imagebutton auto "smartphone/smartphone_icon_%s.png" xpos 1800 ypos 50 focus_mask True action Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_mcroom_%s.png" focus_mask True action[SetVariable("area", "mcroom"), Jump("house_ep2")] tooltip "My room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_zekeroom_%s.png" focus_mask True action[SetVariable("area", "zekeroom"), Jump("house_ep2")] tooltip "Zeke's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_yuiroom_%s.png" focus_mask True action[SetVariable("area", "yuiroom"), Jump("house_ep2")] tooltip "Yui's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_rinroom_%s.png" focus_mask True action[SetVariable("area", "rinroom"), Jump("house_ep2")] tooltip "Rin's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_livingroom_%s.png" focus_mask True action[SetVariable("area", "livroom"), Jump("house_ep2")] tooltip "Livingroom" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_kitchen_%s.png" focus_mask True action[SetVariable("area", "kitchen"), Jump("house_ep2")] tooltip "Kitchen" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_hallway_%s.png" focus_mask True action[SetVariable("area", "hallway"), Jump("house_ep2")] tooltip "Hallway" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.2/Interactive maps/Interactive objects/ep2_garage_%s.png" focus_mask True action[SetVariable("area", "garage"), Jump("house_ep2")] tooltip "Garage" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        $ tt = GetTooltip()
    vbox:
        if tt:
            imagebutton idle "Ch.1/Ep.2/Interactive maps/Interactive objects/navi_box.png"
    vbox:
        if tt:
            xalign 0.5
            yalign 0.02
            if tt == "My room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Zeke's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Yui's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Rin's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Livingroom":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Kitchen":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Hallway":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Garage":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"

    text "Speak with everyone, and collect the images before going to the Hallway" align(0.5, 0.85) style "smgrout"
    if not ep2mcroom_pic:
        text "{b}*{/b}" pos(0.245, 0.875) style "smgrout"
    if not ep2yuiroom_pic:
        text "{b}*{/b}" pos(0.38, 0.875) style "smgrout"
    if not ep2rinroom_pic1:
        text "{b}*{/b}" pos(0.45, 0.875) style "smgrout"
    if not ep2rinroom_pic2:
        text "{b}*{/b}" pos(0.45, 0.875) style "smgrout"
    if not ep2livroom_pic:
        text "{b}*{/b}" pos(0.52, 0.875) style "smgrout"
    if not ep2kitchen_pic:
        text "{b}*{/b}" pos(0.59, 0.875) style "smgrout"
    if not ep2garage_pic:
        text "{b}*{/b}" pos(0.655, 0.875) style "smgrout"


screen ep3house:
    if area == "mcroom":
        if ep3mcroom_pic == False:
            add "Ch.1/Ep.3/Interactive maps/ep3_mcroom_photo.jpg"
            imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_mcroom_pic_%s.png" focus_mask True action Jump("ep3_mcroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.3/Interactive maps/ep3_mcroom.jpg"
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_mcroom_door_%s.png" focus_mask True action Jump("ep3_mcroom_door") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "zekeroom":
        add "Ch.1/Ep.3/Interactive maps/ep3_zekeroom.jpg"
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_zekeroom_talk_%s.png" focus_mask True action Jump("ep3_zekeroom_talk") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "yuiroom":
        if ep3yuiroom_pic == False:
            add "Ch.1/Ep.3/Interactive maps/ep3_yuiroom_photo.jpg"
            imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_yuiroom_pic_%s.png" focus_mask True action Jump("ep3_yuiroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.3/Interactive maps/ep3_yuiroom.jpg"
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_yuiroom_talk_%s.png" focus_mask True action Jump("ep3_yuiroom_talk") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "rinroom":
        if ep3rinroom_pic == False:
            add "Ch.1/Ep.3/Interactive maps/ep3_rinroom_photo.jpg"
            imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_rinroom_pic_%s.png" focus_mask True action Jump("ep3_rinroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.3/Interactive maps/ep3_rinroom.jpg"
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_rinroom_bed_%s.png" focus_mask True action Jump("ep3_rinroom_bed") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "livroom":
        if ep3livroom_pic1 == False and ep3livroom_pic2 == False:
            add "Ch.1/Ep.3/Interactive maps/ep3_livingroom_photos.jpg"
            imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_livingroom_pic1_%s.png" focus_mask True action Jump("ep3_livroom_pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
            imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_livingroom_pic2_%s.png" focus_mask True action Jump("ep3_livroom_pic2") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        if ep3livroom_pic1 == True and ep3livroom_pic2 == False:
            add "Ch.1/Ep.3/Interactive maps/ep3_livingroom_photo1.jpg"
            imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_livingroom_pic2_%s.png" focus_mask True action Jump("ep3_livroom_pic2") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        if ep3livroom_pic1 == False and ep3livroom_pic2 == True:
            add "Ch.1/Ep.3/Interactive maps/ep3_livingroom_photo2.jpg"
            imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_livingroom_pic1_%s.png" focus_mask True action Jump("ep3_livroom_pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        elif ep3livroom_pic1 == True and ep3livroom_pic2 == True:
            add "Ch.1/Ep.3/Interactive maps/ep3_livingroom.jpg"
    if area == "kitchen":
        add "Ch.1/Ep.3/Interactive maps/ep3_kitchen.jpg"
    if area == "garage":
        if ep3garage_pic == False:
            add "Ch.1/Ep.3/Interactive maps/ep3_garage_photo.jpg"
            imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_garage_pic_%s.png" focus_mask True action Jump("ep3_garage_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.3/Interactive maps/ep3_garage.jpg"
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_garage_car_%s.png" focus_mask True action Jump("ep3_garage_car") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "hallway":
        if ep3hallway_pic == False:
            add "Ch.1/Ep.3/Interactive maps/ep3_hallway_photo.jpg"
            imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_hallway_pic_%s.png" focus_mask True action Jump("ep3_hallway_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.3/Interactive maps/ep3_hallway.jpg"
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_hallway_bookcase_%s.png" focus_mask True action Jump("ep3_hallway_bookcase") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_hallway_ftable_%s.png" focus_mask True action Jump("ep3_hallway_ftable") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        if phone_alert == True:
            imagebutton auto "smartphone/smartphone_alert_icon_%s.png" xpos 1800 ypos 50 focus_mask True action SetVariable("phone_alert", False), Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        elif phone_alert == False:
            imagebutton auto "smartphone/smartphone_icon_%s.png" xpos 1800 ypos 50 focus_mask True action Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_mcroom_%s.png" focus_mask True action[SetVariable("area", "mcroom"), Jump("house_ep3")] tooltip "My room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_zekeroom_%s.png" focus_mask True action[SetVariable("area", "zekeroom"), Jump("house_ep3")] tooltip "Zeke's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_yuiroom_%s.png" focus_mask True action[SetVariable("area", "yuiroom"), Jump("house_ep3")] tooltip "Yui's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_rinroom_%s.png" focus_mask True action[SetVariable("area", "rinroom"), Jump("house_ep3")] tooltip "Rin's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_livingroom_%s.png" focus_mask True action[SetVariable("area", "livroom"), Jump("house_ep3")] tooltip "Livingroom" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_kitchen_%s.png" focus_mask True action[SetVariable("area", "kitchen"), Jump("house_ep3")] tooltip "Kitchen" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_hallway_%s.png" focus_mask True action[SetVariable("area", "hallway"), Jump("house_ep3")] tooltip "Hallway" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.3/Interactive maps/Interactive objects/ep3_garage_%s.png" focus_mask True action[SetVariable("area", "garage"), Jump("house_ep3")] tooltip "Garage" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        $ tt = GetTooltip()
    vbox:
        if tt:
            imagebutton idle "Ch.1/Ep.2/Interactive maps/Interactive objects/navi_box.png"
    vbox:
        if tt:
            xalign 0.5
            yalign 0.02
            if tt == "My room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Zeke's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Yui's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Rin's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Livingroom":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Kitchen":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Hallway":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Garage":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"

    text "Speak with everyone, and collect the images before going to the Kitchen" align(0.5, 0.85) style "smgrout"
    if not ep3mcroom_pic:
        text "{b}*{/b}" pos(0.235, 0.875) style "smgrout"
    if not ep3yuiroom_pic:
        text "{b}*{/b}" pos(0.39, 0.875) style "smgrout"
    if not ep3rinroom_pic:
        text "{b}*{/b}" pos(0.47, 0.875) style "smgrout"
    if not ep3livroom_pic1:
        text "{b}*{/b}" pos(0.55, 0.875) style "smgrout"
    if not ep3livroom_pic2:
        text "{b}*{/b}" pos(0.55, 0.875) style "smgrout"
    if not ep3hallway_pic:
        text "{b}*{/b}" pos(0.63, 0.875) style "smgrout"
    if not ep3garage_pic:
        text "{b}*{/b}" pos(0.71, 0.875) style "smgrout"


screen ep4house:
    if area == "mcroom":
        add "Ch.1/Ep.4/Interactive maps/ep4_mcroom.jpg"
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_mcroom_bed_%s.png" focus_mask True action Jump("ep4_mcroom_bed") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "zekeroom":
        if ep4zekeroom_pic == False:
            add "Ch.1/Ep.4/Interactive maps/ep4_zekeroom_photo.jpg"
            imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_zekeroom_pic_%s.png" focus_mask True action Jump("ep4_zekeroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.4/Interactive maps/ep4_zekeroom.jpg"
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_zekeroom_window_%s.png" focus_mask True action Jump("ep4_zekeroom_window") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "livingroom":
        if ep4livingroom_pic == False:
            add "Ch.1/Ep.4/Interactive maps/ep4_livingroom_photo.jpg"
            imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_livingroom_pic_%s.png" focus_mask True action Jump("ep4_livingroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.4/Interactive maps/ep4_livingroom.jpg"
    if area == "rinroom":
        add "Ch.1/Ep.4/Interactive maps/ep4_rinroom.jpg"
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_rinroom_talk_%s.png" focus_mask True action Jump("ep4_rinroom_talk") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "kitchen":
        if ep4kitchen_pic == False:
            add "Ch.1/Ep.4/Interactive maps/ep4_kitchen_photo.jpg"
            imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_kitchen_pic_%s.png" focus_mask True action Jump("ep4_kitchen_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.4/Interactive maps/ep4_kitchen.jpg"
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_kitchen_talk_%s.png" focus_mask True action Jump("ep4_kitchen_talk") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "hallway":
        if ep4hallway_pic == False:
            add "Ch.1/Ep.4/Interactive maps/ep4_hallway_photo.jpg"
            imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_hallway_pic_%s.png" focus_mask True action Jump("ep4_hallway_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.4/Interactive maps/ep4_hallway.jpg"
    if area == "garage":
        add "Ch.1/Ep.4/Interactive maps/ep4_garage.jpg"
    if area == "yuiroom":
        add "Ch.1/Ep.4/Interactive maps/ep4_yuiroom.jpg"
    if area == "krystalroom":
        if ep4krystalroom_pic == False:
            add "Ch.1/Ep.4/Interactive maps/ep4_krystalroom_photo.jpg"
            imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_krystalroom_pic_%s.png" focus_mask True action Jump("ep4_krystalroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.1/Ep.4/Interactive maps/ep4_krystalroom.jpg"
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_krystalroom_talk_%s.png" focus_mask True action Jump("ep4_krystalroom_talk") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_krystalroom_closet_%s.png" focus_mask True action Jump("ep4_krystalroom_closet") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        if phone_alert == True:
            imagebutton auto "smartphone/smartphone_alert_icon_%s.png" xpos 1800 ypos 50 focus_mask True action SetVariable("phone_alert", False), Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        elif phone_alert == False:
            imagebutton auto "smartphone/smartphone_icon_%s.png" xpos 1800 ypos 50 focus_mask True action Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_mcroom_%s.png" focus_mask True action[SetVariable("area", "mcroom"), Jump("ep4_freeroam")] tooltip "My room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_zekeroom_%s.png" focus_mask True action[SetVariable("area", "zekeroom"), Jump("ep4_freeroam")] tooltip "Zeke's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_rinroom_%s.png" focus_mask True action[SetVariable("area", "rinroom"), Jump("ep4_freeroam")] tooltip "Rin's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_livingroom_%s.png" focus_mask True action[SetVariable("area", "livingroom"), Jump("ep4_freeroam")] tooltip "Livingroom" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_kitchen_%s.png" focus_mask True action[SetVariable("area", "kitchen"), Jump("ep4_freeroam")] tooltip "Kitchen" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_hallway_%s.png" focus_mask True action[SetVariable("area", "hallway"), Jump("ep4_freeroam")] tooltip "Hallway" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_garage_%s.png" focus_mask True action[SetVariable("area", "garage"), Jump("ep4_freeroam")] tooltip "Garage" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_yuiroom_%s.png" focus_mask True action[SetVariable("area", "yuiroom"), Jump("ep4_freeroam")] tooltip "Yui's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if krystalmeeteveryone == 1:
        vbox:
            imagebutton auto "Ch.1/Ep.4/Interactive maps/Interactive objects/ep4_krystalroom_%s.png" focus_mask True action[SetVariable("area", "krystalroom"), Jump("ep4_freeroam")] tooltip "Krystal's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        $ tt = GetTooltip()
    vbox:
        if tt:
            imagebutton idle "Ch.1/Ep.2/Interactive maps/Interactive objects/navi_box.png"
    vbox:
        if tt:
            xalign 0.5
            yalign 0.02
            if tt == "My room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Zeke's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Yui's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Rin's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Krystal's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Livingroom":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Kitchen":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Hallway":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Garage":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"

    text "Speak with everyone, and collect the images before going to Yui's Room" align(0.5, 0.85) style "smgrout"
    if not ep4zekeroom_pic:
        text "{b}*{/b}" pos(0.312, 0.87) style "smgrout"
    if not ep4livingroom_pic:
        text "{b}*{/b}" pos(0.39, 0.87) style "smgrout"
    if not ep4kitchen_pic:
        text "{b}*{/b}" pos(0.55, 0.87) style "smgrout"
    if not ep4hallway_pic:
        text "{b}*{/b}" pos(0.63, 0.87) style "smgrout"
    if not ep4krystalroom_pic:
        text "{b}*{/b}" pos(0.87, 0.87) style "smgrout"


screen ch2ep1house:
    if area == "entrance":
        if ep5entrance_pic == False:
            add "Ch.2/Ep.1/Interactive maps/ep5_entrance_photo.jpg"
            imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_entrance_pic_%s.png" focus_mask True action Jump("ep5_entrance_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.1/Interactive maps/ep5_entrance.jpg"
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_entrance_talk_%s.png" focus_mask True action Jump("ep5_entrance_talk") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "livingroom":
        if ep5livingroom_pic == False:
            add "Ch.2/Ep.1/Interactive maps/ep5_livingroom_photo.jpg"
            imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_livingroom_pic_%s.png" focus_mask True action Jump("ep5_livingroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.1/Interactive maps/ep5_livingroom.jpg"
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_livingroom_es_%s.png" focus_mask True action Jump("ep5_livingroom_es") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_livingroom_leo_%s.png" focus_mask True action Jump("ep5_livingroom_leo") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "kitchen":
        if ep5kitchen_pic == False:
            add "Ch.2/Ep.1/Interactive maps/ep5_kitchen_photo.jpg"
            imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_kitchen_pic_%s.png" focus_mask True action Jump("ep5_kitchen_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.1/Interactive maps/ep5_kitchen.jpg"
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_kitchen_faye_%s.png" focus_mask True action Jump("ep5_kitchen_faye") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_kitchen_zeke_%s.png" focus_mask True action Jump("ep5_kitchen_zeke") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_kitchen_pete_%s.png" focus_mask True action Jump("ep5_kitchen_pete") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "pool":
        if ep5pool_pic == False:
            add "Ch.2/Ep.1/Interactive maps/ep5_pool_photo.jpg"
            imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_pool_pic_%s.png" focus_mask True action Jump("ep5_pool_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.1/Interactive maps/ep5_pool.jpg"
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_pool_yui_%s.png" focus_mask True action Jump("ep5_pool_yui") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_pool_re_%s.png" focus_mask True action Jump("ep5_pool_re") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "balcony":
        if ep5balcony_pic == False:
            add "Ch.2/Ep.1/Interactive maps/ep5_balcony_photo.jpg"
            imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_balcony_pic_%s.png" focus_mask True action Jump("ep5_balcony_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.1/Interactive maps/ep5_balcony.jpg"
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_balcony_wendy_%s.png" focus_mask True action Jump("ep5_balcony_wendy") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "bedroom":
        add "Ch.2/Ep.1/Interactive maps/ep5_bedroom.jpg"
    vbox:
        if phone_alert == True:
            imagebutton auto "smartphone/smartphone_alert_icon_%s.png" xpos 1800 ypos 50 focus_mask True action SetVariable("phone_alert", False), Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        elif phone_alert == False:
            imagebutton auto "smartphone/smartphone_icon_%s.png" xpos 1800 ypos 50 focus_mask True action Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_entrance_%s.png" focus_mask True action[SetVariable("area", "entrance"), Jump("ch2ep1_freeroam")] tooltip "Entrance" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_livingroom_%s.png" focus_mask True action[SetVariable("area", "livingroom"), Jump("ch2ep1_freeroam")] tooltip "Livingroom" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_kitchen_%s.png" focus_mask True action[SetVariable("area", "kitchen"), Jump("ch2ep1_freeroam")] tooltip "Kitchen" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_pool_%s.png" focus_mask True action[SetVariable("area", "pool"), Jump("ch2ep1_freeroam")] tooltip "Pool" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_balcony_%s.png" focus_mask True action[SetVariable("area", "balcony"), Jump("ch2ep1_freeroam")] tooltip "Balcony" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.1/Interactive maps/Interactive objects/ep5_bedroom_%s.png" focus_mask True action[SetVariable("area", "bedroom"), Jump("ch2ep1_freeroam")] tooltip "Rowan's bedroom" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        $ tt = GetTooltip()
    vbox:
        if tt:
            imagebutton idle "Ch.1/Ep.2/Interactive maps/Interactive objects/navi_box.png"
    vbox:
        if tt:
            xalign 0.5
            yalign 0.02
            if tt == "Entrance":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Livingroom":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Kitchen":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Pool":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Balcony":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Rowan's bedroom":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"

    text "Speak with everyone, and collect the images before going to Rowan's bedroom" align(0.5, 0.85) style "smgrout"
    if not ep5entrance_pic:
        text "{b}*{/b}" pos(0.286, 0.87) style "smgrout"
    if not ep5livingroom_pic:
        text "{b}*{/b}" pos(0.37, 0.87) style "smgrout"
    if not ep5kitchen_pic:
        text "{b}*{/b}" pos(0.455, 0.87) style "smgrout"
    if not ep5pool_pic:
        text "{b}*{/b}" pos(0.538, 0.87) style "smgrout"
    if not ep5balcony_pic:
        text "{b}*{/b}" pos(0.62, 0.87) style "smgrout"

screen ch2ep2house:
    if area == "kitchen":
        if ch2ep2kitchen_pic == False:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_kitchen_photo.jpg"
            imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_kitchen_pic_%s.png" focus_mask True action Jump("ch2ep2_kitchen_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_kitchen.jpg"
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_kitchen_maya_%s.png" focus_mask True action Jump("ch2ep2_kitchen_maya") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "backyard":
        if ch2ep2backyard_pic == False:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_backyard_photo.jpg"
            imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_backyard_pic_%s.png" focus_mask True action Jump("ch2ep2_backyard_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_backyard.jpg"
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_backyard_pool_%s.png" focus_mask True action Jump("ch2ep2_backyard_pool") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "livingroom":
        if ch2ep2livingroom_pic1 == False and ch2ep2livingroom_pic2 == False:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_livingroom_photos.jpg"
            imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_livingroom_pic1_%s.png" focus_mask True action Jump("ch2ep2_livingroom_pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
            imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_livingroom_pic2_%s.png" focus_mask True action Jump("ch2ep2_livingroom_pic2") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        if ch2ep2livingroom_pic1 == True and ch2ep2livingroom_pic2 == False:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_livingroom_photo2.jpg"
            imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_livingroom_pic2_%s.png" focus_mask True action Jump("ch2ep2_livingroom_pic2") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        if ch2ep2livingroom_pic1 == False and ch2ep2livingroom_pic2 == True:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_livingroom_photo1.jpg"
            imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_livingroom_pic1_%s.png" focus_mask True action Jump("ch2ep2_livingroom_pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        elif ch2ep2livingroom_pic1 == True and ch2ep2livingroom_pic2 == True:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_livingroom.jpg"
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_livingroom_sofa_%s.png" focus_mask True action Jump("ch2ep2_livingroom_sofa") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "bathroom":
        if ch2ep2bathroom_pic == False:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_bathroom_photo.jpg"
            imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_bathroom_pic_%s.png" focus_mask True action Jump("ch2ep2_bathroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_bathroom.jpg"
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_bathroom_bathtub_%s.png" focus_mask True action Jump("ch2ep2_bathroom_bathtub") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "balcony":
        if ch2ep2balcony_pic == False:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_balcony_photo.jpg"
            imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_balcony_pic_%s.png" focus_mask True action Jump("ch2ep2_balcony_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_balcony.jpg"
    if area == "fitness":
        if ch2ep2fitness_pic == False:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_fitness_photo.jpg"
            imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_fitness_pic_%s.png" focus_mask True action Jump("ch2ep2_fitness_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.2/Interactive maps/ch2ep2_fitness.jpg"
    if area == "bedroomentrance":
        add "Ch.2/Ep.2/Interactive maps/ch2ep2_bedroomentrance.jpg"
    if not ch2ep2kitchen_pic:
        text "{b}*{/b}" pos(0.245, 0.87) style "smgrout"
    if not ch2ep2backyard_pic:
        text "{b}*{/b}" pos(0.328, 0.87) style "smgrout"
    if not ch2ep2livingroom_pic1 or not ch2ep2livingroom_pic2:
        text "{b}*{/b}" pos(0.41, 0.87) style "smgrout"
    if not ch2ep2bathroom_pic:
        text "{b}*{/b}" pos(0.495, 0.87) style "smgrout"
    if not ch2ep2balcony_pic:
        text "{b}*{/b}" pos(0.577, 0.87) style "smgrout"
    if not ch2ep2fitness_pic:
        text "{b}*{/b}" pos(0.66, 0.87) style "smgrout"
    vbox:
        if phone_alert == True:
            imagebutton auto "smartphone/smartphone_alert_icon_%s.png" xpos 1800 ypos 50 focus_mask True action SetVariable("phone_alert", False), Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        elif phone_alert == False:
            imagebutton auto "smartphone/smartphone_icon_%s.png" xpos 1800 ypos 50 focus_mask True action Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_kitchen_%s.png" focus_mask True action[SetVariable("area", "kitchen"), Jump("ch2ep2_freeroam")] tooltip "Kitchen" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_fitness_%s.png" focus_mask True action[SetVariable("area", "fitness"), Jump("ch2ep2_freeroam")] tooltip "Fitness" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_livingroom_%s.png" focus_mask True action[SetVariable("area", "livingroom"), Jump("ch2ep2_freeroam")] tooltip "Livingroom" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_backyard_%s.png" focus_mask True action[SetVariable("area", "backyard"), Jump("ch2ep2_freeroam")] tooltip "Backyard" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_balcony_%s.png" focus_mask True action[SetVariable("area", "balcony"), Jump("ch2ep2_freeroam")] tooltip "Balcony" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_bedroomentrance_%s.png" focus_mask True action[SetVariable("area", "bedroomentrance"), Jump("ch2ep2_freeroam")] tooltip "Skylar's bedroom" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.2/Interactive maps/Interactive objects/ch2ep2_bathroom_%s.png" focus_mask True action[SetVariable("area", "bathroom"), Jump("ch2ep2_freeroam")] tooltip "Bathroom" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        $ tt = GetTooltip()
    vbox:
        if tt:
            imagebutton idle "Ch.1/Ep.2/Interactive maps/Interactive objects/navi_box.png"
    vbox:
        if tt:
            xalign 0.5
            yalign 0.02
            if tt == "Fitness":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Livingroom":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Kitchen":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Backyard":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Balcony":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Skylar's bedroom":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Bathroom":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
screen ch2ep4_house:
    if area == "secondhall":
        if ch2ep4secondhall_pic == False:
            add "Ch.2/Ep.4/Interactive maps/ch2ep4_secondhall_photo.jpg"
            imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_secondhall_pic_%s.png" focus_mask True action Jump("ch2ep4_secondhall_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.4/Interactive maps/ch2ep4_secondhall.jpg"
        imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_secondhall_yui_%s.png" focus_mask True action Jump("ch2ep4_secondhall_yui") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "zekeroom":
        if ch2ep4zekeroom_pic == False:
            add "Ch.2/Ep.4/Interactive maps/ch2ep4_zekeroom_photo.jpg"
            imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_zekeroom_pic_%s.png" focus_mask True action Jump("ch2ep4_zekeroom_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.4/Interactive maps/ch2ep4_zekeroom.jpg"
        imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_zekeroom_zeke_%s.png" focus_mask True action Jump("ch2ep4_zekeroom_zeke") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "hallway":
        if ch2ep4hallway_pic == False:
            add "Ch.2/Ep.4/Interactive maps/ch2ep4_hallway_photo.jpg"
            imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_hallway_pic_%s.png" focus_mask True action Jump("ch2ep4_hallway_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.4/Interactive maps/ch2ep4_hallway.jpg"
    if area == "kitchen":
        if ch2ep4kitchen_pic1 == False and ch2ep4kitchen_pic2 == False:
            add "Ch.2/Ep.4/Interactive maps/ch2ep4_kitchen_photos.jpg"
            imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_kitchen_pic1_%s.png" focus_mask True action Jump("ch2ep4_kitchen_pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
            imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_kitchen_pic2_%s.png" focus_mask True action Jump("ch2ep4_kitchen_pic2") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        if ch2ep4kitchen_pic1 == True and ch2ep4kitchen_pic2 == False:
            add "Ch.2/Ep.4/Interactive maps/ch2ep4_kitchen_photo2.jpg"
            imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_kitchen_pic2_%s.png" focus_mask True action Jump("ch2ep4_kitchen_pic2") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        if ch2ep4kitchen_pic1 == False and ch2ep4kitchen_pic2 == True:
            add "Ch.2/Ep.4/Interactive maps/ch2ep4_kitchen_photo1.jpg"
            imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_kitchen_pic1_%s.png" focus_mask True action Jump("ch2ep4_kitchen_pic1") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        elif ch2ep4kitchen_pic1 == True and ch2ep4kitchen_pic2 == True:
            add "Ch.2/Ep.4/Interactive maps/ch2ep4_kitchen.jpg"
        imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_kitchen_rin_%s.png" focus_mask True action Jump("ch2ep4_kitchen_rin") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "frontyard":
        add "Ch.2/Ep.4/Interactive maps/ch2ep4_frontyard.jpg"
    vbox:
        if phone_alert == True:
            imagebutton auto "smartphone/smartphone_alert_icon_%s.png" xpos 1800 ypos 50 focus_mask True action SetVariable("phone_alert", False), Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        elif phone_alert == False:
            imagebutton auto "smartphone/smartphone_icon_%s.png" xpos 1800 ypos 50 focus_mask True action Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_kitchen_%s.png" focus_mask True action[SetVariable("area", "kitchen"), Jump("ch2ep4_freeroam")] tooltip "Kitchen" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_secondhall_%s.png" focus_mask True action[SetVariable("area", "secondhall"), Jump("ch2ep4_freeroam")] tooltip "Second floor" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_zekeroom_%s.png" focus_mask True action[SetVariable("area", "zekeroom"), Jump("ch2ep4_freeroam")] tooltip "Zeke's room" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_hallway_%s.png" focus_mask True action[SetVariable("area", "hallway"), Jump("ch2ep4_freeroam")] tooltip "Hallway" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.4/Interactive maps/Interactive objects/ch2ep4_frontyard_%s.png" focus_mask True action[SetVariable("area", "frontyard"), Jump("ch2ep4_freeroam")] tooltip "Front yard" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        $ tt = GetTooltip()
    vbox:
        if tt:
            imagebutton idle "Ch.1/Ep.2/Interactive maps/Interactive objects/navi_box.png"
    vbox:
        if tt:
            xalign 0.5
            yalign 0.02
            if tt == "Kitchen":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Second floor":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Zeke's room":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Hallway":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Front yard":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
    text "{size=-2}Last" pos(0.65, 0.866) style "smgrout"
    if not ch2ep4secondhall_pic:
        text "{b}*{/b}" pos(0.325, 0.873) style "smgrout"
    if not ch2ep4zekeroom_pic:
        text "{b}*{/b}" pos(0.41, 0.873) style "smgrout"
    if not ch2ep4hallway_pic:
        text "{b}*{/b}" pos(0.495, 0.873) style "smgrout"
    if not ch2ep4kitchen_pic1 or not ch2ep4kitchen_pic2:
        text "{b}*{/b}" pos(0.58, 0.873) style "smgrout"


screen ch2ep3_office:
    if area == "gamedev":
        if ch2ep3gamedev_pic == False:
            add "Ch.2/Ep.3/Interactive maps/ch2ep3_gamedev_photo.jpg"
            imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_gamedev_pic_%s.png" focus_mask True action Jump("ch2ep3_gamedev_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.3/Interactive maps/ch2ep3_gamedev.jpg"
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_gamedev_yui_%s.png" focus_mask True action Jump("ch2ep3_gamedev_yui") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "cafeteria":
        if ch2ep3cafeteria_pic == False:
            add "Ch.2/Ep.3/Interactive maps/ch2ep3_cafeteria_photo.jpg"
            imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_cafeteria_pic_%s.png" focus_mask True action Jump("ch2ep3_cafeteria_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.3/Interactive maps/ch2ep3_cafeteria.jpg"
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_cafeteria_rin_%s.png" focus_mask True action Jump("ch2ep3_cafeteria_rin") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "library":
        if ch2ep3library_pic == False:
            add "Ch.2/Ep.3/Interactive maps/ch2ep3_library_photo.jpg"
            imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_library_pic_%s.png" focus_mask True action Jump("ch2ep3_library_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.3/Interactive maps/ch2ep3_library.jpg"
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_library_wendy_%s.png" focus_mask True action Jump("ch2ep3_library_wendy") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "tester":
        if ch2ep3tester_pic == False:
            add "Ch.2/Ep.3/Interactive maps/ch2ep3_tester_photo.jpg"
            imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_tester_pic_%s.png" focus_mask True action Jump("ch2ep3_tester_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.3/Interactive maps/ch2ep3_tester.jpg"
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_tester_sally_%s.png" focus_mask True action Jump("ch2ep3_tester_sally") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "fayeoffice":
        if ch2ep3fayeoffice_pic == False:
            add "Ch.2/Ep.3/Interactive maps/ch2ep3_fayeoffice_photo.jpg"
            imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_fayeoffice_pic_%s.png" focus_mask True action Jump("ch2ep3_fayeoffice_pic") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav" at butt_eff
        else:
            add "Ch.2/Ep.3/Interactive maps/ch2ep3_fayeoffice.jpg"
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_fayeoffice_faye_%s.png" focus_mask True action Jump("ch2ep3_fayeoffice_faye") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    if area == "reception":
        add "Ch.2/Ep.3/Interactive maps/ch2ep3_reception.jpg"
    if not ch2ep3gamedev_pic:
        text "{b}*{/b}" pos(0.287, 0.87) style "smgrout"
    if not ch2ep3cafeteria_pic:
        text "{b}*{/b}" pos(0.370, 0.87) style "smgrout"
    if not ch2ep3library_pic:
        text "{b}*{/b}" pos(0.453, 0.87) style "smgrout"
    if not ch2ep3tester_pic:
        text "{b}*{/b}" pos(0.538, 0.87) style "smgrout"
    if not ch2ep3fayeoffice_pic:
        text "{b}*{/b}" pos(0.621, 0.87) style "smgrout"
    vbox:
        if phone_alert == True:
            imagebutton auto "smartphone/smartphone_alert_icon_%s.png" xpos 1800 ypos 50 focus_mask True action SetVariable("phone_alert", False), Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        elif phone_alert == False:
            imagebutton auto "smartphone/smartphone_icon_%s.png" xpos 1800 ypos 50 focus_mask True action Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_gamedev_%s.png" focus_mask True action[SetVariable("area", "gamedev"), Jump("ch2ep3_freeroam")] tooltip "Developer department" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_cafeteria_%s.png" focus_mask True action[SetVariable("area", "cafeteria"), Jump("ch2ep3_freeroam")] tooltip "Cafeteria" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_library_%s.png" focus_mask True action[SetVariable("area", "library"), Jump("ch2ep3_freeroam")] tooltip "Library" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_tester_%s.png" focus_mask True action[SetVariable("area", "tester"), Jump("ch2ep3_freeroam")] tooltip "Tester department" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_fayeoffice_%s.png" focus_mask True action[SetVariable("area", "fayeoffice"), Jump("ch2ep3_freeroam")] tooltip "Faye's office" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "Ch.2/Ep.3/Interactive maps/Interactive objects/ch2ep3_reception_%s.png" focus_mask True action[SetVariable("area", "reception"), Jump("ch2ep3_freeroam")] tooltip "Reception" hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        $ tt = GetTooltip()
    vbox:
        if tt:
            imagebutton idle "Ch.1/Ep.2/Interactive maps/Interactive objects/navi_box.png"
    vbox:
        if tt:
            xalign 0.5
            yalign 0.02
            if tt == "Developer department":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Cafeteria":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Library":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Tester department":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Faye's office":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"
            if tt == "Reception":
                text "{font=Limelight-Regular.ttf}[tt]{/font}"

screen smartphone:
    vbox:
        if phone_alert == True:
            imagebutton auto "smartphone/smartphone_alert_icon_%s.png" xpos 1800 ypos 50 focus_mask True action SetVariable("phone_alert", False), Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
        elif phone_alert == False:
            imagebutton auto "smartphone/smartphone_icon_%s.png" xpos 1800 ypos 50 focus_mask True action Show("mainphonescreen") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
