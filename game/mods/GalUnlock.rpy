
default persistent.unlocked = False

init python:
    def unlock_all():
        if persistent.unlocked:
            for label in renpy.get_all_labels():
                renpy.game.persistent._seen_ever[label] = True
                renpy.game.seen_session[label] = True
        return

init offset = 9998

screen exnavi():
    vbox:
        imagebutton auto "images/gallery/gallery_images_%s.png" focus_mask True action ShowMenu("imagegallery") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "images/gallery/gallery_scenes_%s.png" focus_mask True action ShowMenu("scenegallery") hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"
    vbox:
        imagebutton auto "images/gallery/gallery_back_%s.png" focus_mask True action Return() hover_sound "sfx/click.wav" activate_sound "sfx/click.wav"

    textbutton ("Auto Unlock All: [smgr]ON" if persistent.unlocked else "Auto Unlock All: [smred]OFF"):
        align(0.02,0.98)
        text_outlines [(5, "#000", 0, 0)]
        action ToggleVariable("persistent.unlocked", true_value=True, false_value=False), Function(unlock_all)

label before_main_menu:
    $ unlock_all()


## U2hhZGR5R2FtZXM
