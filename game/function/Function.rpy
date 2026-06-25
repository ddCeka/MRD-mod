transform eyesblink(pic1, pic2, timer):
    pause(timer)
    pic1 with Dissolve(0.1)
    pause(0.11)
    pic2 with Dissolve(0.1)
    pause(0.11)
    pic2 with Dissolve(0.1)
    pause(0.11)
    pic1 with Dissolve(0.1)
    pause(2)
    repeat
transform eyesblink2(pic1, pic2, pic3, timer):
    pause(timer)
    pic1 with Dissolve(0.1)
    pause(0.11)
    pic2 with Dissolve(0.1)
    pause(0.11)
    pic3 with Dissolve(0.1)
    pause(0.11)
    pic2 with Dissolve(0.1)
    pause(0.11)
    pic1 with Dissolve(0.1)
    pause(2)
    repeat
transform Zoom(num, num2):
    on hover:
        linear .05 zoom num
    on idle:
        linear .05 zoom num2
    on selected_idle:
        zoom num2
    on selected_hover:
        linear .05 zoom num
default persistent.legal_age_seen = True

define fade = ImageDissolve("Ch.1/Transitions/transition.jpg", 2, 8)

define config.enter_transition = Dissolve(0.2)
define config.end_splash_transition = Dissolve(0.3)
transform changed_transform():
    # This controls the basic location of the message text.
    xcenter 0.5
    ycenter 0.6

    # When it's shown, slide it down and fade it in.
    on show:
        yoffset -15.0 alpha 0.0
        easein 0.5 yoffset 0.0 alpha 1.0

    # When it's hidden, slide it down and fade it out.
    on hide:
        easeout 0.5 yoffset 15.0 alpha 0.0
# left_margin, top_margin, right_margin, and bottom_margin
style rin_chat:
    background Solid("#DE7272")
    padding(14,12)
style yui_chat:
    background Solid("#9B5E33")
    padding(14,12)
style alice_chat:
    background Solid("#77CDCD")
    padding(14,12)
style krystal_chat:
    background Solid("#EDA1F1")
    padding(14,12)
style sally_chat:
    background Solid("#A48568")
    padding(14,12)
style zeke_chat:
    background Solid("#F45D12")
    padding(14,12)
style faye_chat:
    background Solid("#F7FA4F")
    padding(14,12)
style mc_chat:
    background Solid("#66cece")
    padding(14,12)
style wendy_chat:
    background Solid("#FF8B00")
    padding(14,12)
style angela_chat:
    background Solid("#E2B0A6")
    padding(14,12)
style navigation:
    background "Ch.1/Ep.2/Interactive maps/Interactive objects/navi_box.png"
style chat_left:
    background None
    # background Solid("#C1C1C1")
    padding (10,10)
    right_margin 40
    xpos 0.0
style hints:
    padding(10,10)
    xalign 0.5
style chat_left_without_margin:
    background Solid("#77CDCD")
    padding (10,10)
    xpos 0.0

style chat_right:
    background Solid("#FBC35B")
    padding (10,10)
    left_margin 40
    xalign 1.0
style chat_right_without_margin:
    background Solid("#FBC35B")
    padding (10,10)
    xalign 1.0
style reply1:
    background Solid("#CB9090")
    xpos 165
    ypos 450
style reply2:
    background Solid("#CB9090")
    xpos 165
    ypos 480
style reply:
    background Solid("#CB9090")
    xpos 165
style replys1:
    background Solid("#CB9090")
    xalign 0.5
    ypos 360
style replys2:
    background Solid("#CB9090")
    xalign 0.5
    ypos 380
screen show_message_image(image_path):
    # layer "screens"

    key "rollback" action [[]]
    key "rollforward" action [[]]

    # if persistent.reward_found_1 == False:
    #     if image_path == "alice_selfie":
    #         timer 0.01 action SetVariable("reward_1_counter", reward_1_counter+1)
    #
    #         if reward_1_counter == 3:
    #             timer 0.1 action Function(renpy.show_screen, "show_message","You've unlocked a gallery item!")
    #             $ persistent.reward_found_1 = True

    add "smartphone/message/images/[image_path].jpg" xcenter 0.5 ycenter 0.5
    button xysize(1920,1080) action Hide("show_message_image"), With(Dissolve(0.2))

#-----------Fights--------------#
default goblinstance = 1
default goblinattack = 1
default timeout = 2.0
default gauge_ypos = 900
default timeout_label = None
image timer_gauge:
    "gui/gauge-legacy.png"
    truecenter
    ypos gauge_ypos
image timer_gauge_green:
    "gui/gauge-green.png"
    truecenter
    ypos gauge_ypos
    gauge_timeout
image timer_gauge_red:
    "gui/gauge-red.png"
    truecenter
    ypos gauge_ypos
    gauge_timeout_red
transform gauge_timeout:
    alpha 1.0
    xzoom 1.0
    parallel:
        linear timeout xzoom 0.0
    parallel:
        linear (timeout * 0.9) alpha 0.0
transform gauge_timeout_red:
    xzoom 1.0
    linear timeout xzoom 0.0
screen attack:


    if goblinstance == 1:
        image "images/Ch.1/Ep.4/Scenes/goblinstance1.jpg"
        imagebutton auto "gui/fight-button_%s.png" xpos 600 ypos 500 focus_mask True action Jump("attack1")
        imagebutton auto "gui/fight-button_%s.png" xpos 950 ypos 650 focus_mask True action Jump("attack2")
        imagebutton auto "gui/fight-button_%s.png" xpos 1000 ypos 350 focus_mask True action Jump("attack3")
        timer timeout action Jump("timeout")
    if goblinstance == 2:
        image "images/Ch.1/Ep.4/Scenes/goblinstance2.jpg"
        imagebutton auto "gui/fight-button_%s.png" xpos 650 ypos 500 focus_mask True action Jump("attack1")
        imagebutton auto "gui/fight-button_%s.png" xpos 950 ypos 650 focus_mask True action Jump("attack2")
        imagebutton auto "gui/fight-button_%s.png" xpos 1100 ypos 450 focus_mask True action Jump("attack3")
        timer timeout action Jump("timeout")
    add "timer_gauge_red"
    add "timer_gauge_green"
    add "timer_gauge"
    vbox:
        imagebutton idle "Ch.1/Ep.2/Interactive maps/Interactive objects/navi_box.png"
    vbox:
        xalign 0.5
        yalign 0.02
        text "{font=Limelight-Regular.ttf}Attack{/font}"

screen goblinattack:

    if goblinattack == 1:
        image "images/Ch.1/Ep.4/Scenes/goblinattack1.jpg"
        imagebutton auto "gui/fight-button_%s.png" xpos 300 ypos 780 focus_mask True action Jump("block1")
        imagebutton auto "gui/fight-button_%s.png" xpos 950 ypos 450 focus_mask True action Jump("block2")
        imagebutton auto "gui/fight-button_%s.png" xpos 1500 ypos 700 focus_mask True action Jump("block3")
        timer timeout action Jump("timeout1")
    if goblinattack == 2:
        image "images/Ch.1/Ep.4/Scenes/goblinattack2.jpg"
        imagebutton auto "gui/fight-button_%s.png" xpos 250 ypos 600 focus_mask True action Jump("block1")
        imagebutton auto "gui/fight-button_%s.png" xpos 600 ypos 250 focus_mask True action Jump("block2")
        imagebutton auto "gui/fight-button_%s.png" xpos 1500 ypos 700 focus_mask True action Jump("block3")
        timer timeout action Jump("timeout2")
    if goblinattack == 3:
        image "images/Ch.1/Ep.4/Scenes/goblinattack3.jpg"
        imagebutton auto "gui/fight-button_%s.png" xpos 680 ypos 750 focus_mask True action Jump("block1")
        imagebutton auto "gui/fight-button_%s.png" xpos 950 ypos 450 focus_mask True action Jump("block2")
        imagebutton auto "gui/fight-button_%s.png" xpos 1500 ypos 700 focus_mask True action Jump("block3")
        timer timeout action Jump("timeout3")
    add "timer_gauge_red"
    add "timer_gauge_green"
    add "timer_gauge"
    vbox:
        imagebutton idle "Ch.1/Ep.2/Interactive maps/Interactive objects/navi_box.png"
    vbox:
        xalign 0.5
        yalign 0.02
        text "{font=Limelight-Regular.ttf}Defense{/font}"
