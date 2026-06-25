
define modsnote1 = Character("Mods", who_color="#3F60DE")
define modsnote2 = Character("Mods", who_color="#3F60DE", who_outlines=[(3, "#000000", 1, 1) ], what_outlines=[ (3, "#000000", 1, 1) ])

init python:

    smgr = "{color=#0f0}"
    smgr2 = "{color=#007a00}"
    smgrey = "{color=#7a7a7a}"
    smred = "{color=#f00}"
    smbl = "{color=#00f}"
    smlb = "{color=#009dff}"
    smpi = "{color=#f200ff}"
    smpu = "{color=#8a2be2}"
    smor = "{color=#ffb300}"
    smyel = "{color=#ffcb4f}"
    smec = "{/color}"

    smbo = "{color=#00f}[Best Option]"
    smntr = "{color=#f00}[NTR Route]"

    smrec = "{color=#0f0}[Recommended]"

    def mod_set_vars():
        setattr(store, 'angela1', '{{color=#f200ff}}[+1 {}]'.format(angela))
        setattr(store, 'angela2', '{{color=#f200ff}}[+1 {}]'.format(angela))

        setattr(store, 'alice1', '{{color=#f200ff}}[+1 {}]'.format(alice))
        setattr(store, 'alice2', '{{color=#f200ff}}[+1 {}]'.format(alice))

        setattr(store, 'eira1', '{{color=#f200ff}}[+1 {}]'.format(eira))
        setattr(store, 'eira2', '{{color=#f200ff}}[+1 {}]'.format(eira))
        setattr(store, 'eira3', '{{color=#f200ff}}[+1 {}]'.format(eira))

        setattr(store, 'elaine1', '{{color=#f200ff}}[+1 {}]'.format(elaine))
        setattr(store, 'elaine2', '{{color=#f200ff}}[+1 {}]'.format(elaine))

        setattr(store, 'faye1', '{{color=#f200ff}}[+1 {}]'.format(faye))
        setattr(store, 'faye2', '{{color=#f200ff}}[+1 {}]'.format(faye))
        setattr(store, 'faye3', '{{color=#f200ff}}[+1 {}]'.format(faye))

        setattr(store, 'krystal1', '{{color=#f200ff}}[+1 {}]'.format(krystal))
        setattr(store, 'krystal2', '{{color=#f200ff}}[+1 {}]'.format(krystal))

        setattr(store, 'rin1', '{{color=#f200ff}}[+1 {}]'.format(rin))
        setattr(store, 'rin2', '{{color=#f200ff}}[+1 {}]'.format(rin))
        setattr(store, 'rin3', '{{color=#f200ff}}[+1 {}]'.format(rin))

        setattr(store, 'sally1', '{{color=#f200ff}}[+1 {}]'.format(sally))
        setattr(store, 'sally2', '{{color=#f200ff}}[+1 {}]'.format(sally))
        setattr(store, 'sally3', '{{color=#f200ff}}[+1 {}]'.format(sally))

        setattr(store, 'wendy1', '{{color=#f200ff}}[+1 {}]'.format(wendy))
        setattr(store, 'wendy2', '{{color=#f200ff}}[+1 {}]'.format(wendy))
        setattr(store, 'wendy3', '{{color=#f200ff}}[+1 {}]'.format(wendy))

        setattr(store, 'yui1', '{{color=#f200ff}}[+1 {}]'.format(yui))
        setattr(store, 'yui2', '{{color=#f200ff}}[+1 {}]'.format(yui))

        setattr(store, 'zeke1', '{{color=#f200ff}}[+1 {}]'.format(zeke))

        return


init -2:
    transform butt_eff:
        on hover:
            easein_bounce 0.5 yoffset 0
        on idle:
            yoffset -20
            ease_bounce 0.5 yoffset 0
            repeat

# at butt_eff

label mod_set_vars:
    #fe in .format is the player input name variable
    #add call mod_set_vars after names are set
    python:
        angela1 = "{{color=#f200ff}}[+1 {}]".format(angela)
        angela2 = "{{color=#f200ff}}[+2 {}]".format(angela)
        alice1 = "{{color=#f200ff}}[+1 {}]".format(alice)
        alice2 = "{{color=#f200ff}}[+2 {}]".format(alice)
        eira1 = "{{color=#f200ff}}[+1 {}]".format(eira)
        eira2 = "{{color=#f200ff}}[+2 {}]".format(eira)
        eira3 = "{{color=#f200ff}}[+3 {}]".format(eira)
        elaine1 = "{{color=#f200ff}}[+1 {}]".format(elaine)
        elaine2 = "{{color=#f200ff}}[+2 {}]".format(elaine)
        faye1 = "{{color=#f200ff}}[+1 {}]".format(faye)
        faye2 = "{{color=#f200ff}}[+2 {}]".format(faye)
        faye3 = "{{color=#f200ff}}[+3 {}]".format(faye)
        krystal1 = "{{color=#f200ff}}[+1 {}]".format(krystal)
        krystal2 = "{{color=#f200ff}}[+2 {}]".format(krystal)
        rin1 = "{{color=#f200ff}}[+1 {}]".format(rin)
        rin2 = "{{color=#f200ff}}[+2 {}]".format(rin)
        rin3 = "{{color=#f200ff}}[+3 {}]".format(rin)
        sally1 = "{{color=#f200ff}}[+1 {}]".format(sally)
        sally2 = "{{color=#f200ff}}[+2 {}]".format(sally)
        sally3 = "{{color=#f200ff}}[+3 {}]".format(sally)
        wendy1 = "{{color=#f200ff}}[+1 {}]".format(wendy)
        wendy2 = "{{color=#f200ff}}[+2 {}]".format(wendy)
        wendy3 = "{{color=#f200ff}}[+3 {}]".format(wendy)
        yui1 = "{{color=#f200ff}}[+1 {}]".format(yui)
        yui2 = "{{color=#f200ff}}[+2 {}]".format(yui)
        zeke1 = "{{color=#8a2be2}}[+1 {}]".format(zeke)

    return

label after_load:
    $ mod_set_vars()
    if renpy.loadable("GalUnlock.rpy"):
        $ unlock_all()

init offset = 9999

screen choice(items):
    style_prefix "choice"
    vbox spacing 5 xalign 0.0 yalign 0.75:
        for n, i in enumerate(items, 1):
            if n < 10:
                $ my_caption = "{color=#aaaaaa}{size=-5}" + str(n) + ". {/color}{/size}" + i.caption
                key str(n) action i.action
                key "K_KP" + str(n) action i.action
            else:
                $ my_caption = i.caption
            textbutton my_caption style "c_choice" text_style "c_choice_text" action i.action

style smgrout:
    color "#0f0"
    outlines [(3,"#000",1,1)]

style smwhout:
    color "#fff"
    outlines [(3,"#000",1,1)]

style smredout:
    color "#f00"
    outlines [(3,"#000",1,1)]


## U2hhZGR5R2FtZXM
