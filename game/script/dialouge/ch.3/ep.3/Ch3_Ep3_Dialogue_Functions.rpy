label ch3ep3start:
    scene black with dissolve
    $ renpy.pause(3, hard=True)
    scene ep3 with dissolve
    $ renpy.pause(3, hard=True)
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_1 with fade
    show screen smartphone
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    u "Hm...?"
    u "Isn't that.... [angela]?"
    u "What a surprise...."
    scene ch3ep3_2 with dissolve
    mc "Good morning, [angela]."
    angela "Hm...? Oh, good morning, [mc]."
    mc "What a surprise. I didn't expect to meet you here."
    angela "Hm? Why?"
    scene ch3ep3_3 with dissolve
    angela "Didn't I tell you that I live around here?"
    mc "Is that so...? I don't remember that."
    angela "I guess you know that now. Anyway, are you going for a jogging?"
    mc "Yeah... I need to stay fit and get back to my best."
    scene ch3ep3_4 with dissolve
    mc "What about you? Going for a jogging, too?"
    angela "Yes, I am."
    mc "I see..."
    angela "Do you want to join me?"
    mc "Sure thing."
    scene ch3ep3_5 with dissolve
    mc "How often do you exercise in the morning?"
    angela "Every day."
    angela "I always go jogging to the park nearby and do some exercises before going to work."
    mc "Hm? There is a park near here?"
    angela "Not that near. It's around three kilometers away from here."
    angela "Do you want to go there together?"
    mc "Sure. Why not?"
    scene black with dissolve
    $ renpy.pause()
    s "About twenty minutes later......."
    scene ch3ep3_6 with fade
    angela "Here we are...."
    mc "Ah... It's this park."
    angela "Hm? Have you been here before?"
    mc "Yeah, but I've just realised that it's close to my new house."
    angela "I see... Shall we get inside and start exercising?"
    mc "Okay."
    scene ch3ep3_7 with dissolve
    mc "What is your usual exercise program?"
    angela "My exercise program?"
    mc "Yeah."
    angela "I just do 30 push-ups and 30 sit-ups. Nothing special."
    mc "Okay. I will do that for today, too."
    angela "Alright then...."
    scene black with dissolve
    scene ch3ep3_8 with dissolve
    angela "... Shall we start now?"
    mc "Sure thing."
    scene ch3ep3_9 with dissolve
    mc "One...."
    scene ch3ep3_8 with dissolve
    $ renpy.pause()
    scene ch3ep3_9 with dissolve
    angela "Two...."
    scene ch3ep3_8 with dissolve
    $ renpy.pause()
    scene ch3ep3_9 with dissolve
    mc "Three...."
    scene ch3ep3_8 with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    s "*A few moments later*......"
    scene ch3ep3_9 with dissolve
    angela "*Softly breathes* Thirty...."
    scene ch3ep3_10 with dissolve
    angela "*Softly breathes* That's it..."
    angela "Easy for you, right?"
    mc "Well... it's not that easy since I haven't been exercising for a while."
    mc "But, it's not too hard as well."
    angela "I see... Alright then, shall we do push-ups now?"
    angela "I usually do it alone, but since you are here, I guess I will need a little bit of your help."
    mc "Sure thing."
    scene ch3ep3_11 with dissolve
    mc "Okay... Are you ready now?"
    angela "Yes, I am."
    mc "Alright then, let's get started."
    scene ch3ep3_12 with dissolve
    mc "One...."
    angela "*Softly breathes* One...."
    mc "Just focus on doing push-ups. I'll be the one counting."
    angela "*Softly breathes* Okay...."
    scene ch3ep3_11 with dissolve
    $ renpy.pause()
    scene ch3ep3_12 with dissolve
    mc "Two...."
    scene ch3ep3_11 with dissolve
    $ renpy.pause()
    scene ch3ep3_12 with dissolve
    mc "Three...."
    scene ch3ep3_11 with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    s "*A few moments later*......"
    scene ch3ep3_12 with dissolve
    mc "Twenty nine....."
    scene ch3ep3_11 with dissolve
    angela "*Softly breathes*.........."
    mc "Come on, [angela]."
    mc "One last time...."
    $ renpy.pause()
    menu:
        "Bring your face closer [angela2]":
            $ ch3ep3situp = 1
            $ angela_ch3_ep3 += 2
            $ angela_relationship += 2
            scene ch3ep3_13 with dissolve
            angela "*Softly breathes* Thir..."
            mc "Thirty."
            angela "*Softly breathes*............."
            scene black with dissolve
            scene ch3ep3_14 with dissolve
            angela "T.... Thank you for helping me out."
            mc "You're welcome."
            angela "S... Shall we leave now?"
            mc "Wait... Why?"
            mc "I haven't done push-ups yet."
            scene ch3ep3_15 with dissolve
            angela "I'm... sorry."
            angela "I... I've just remembered that.... I have to arrive at the company early today."
            mc ".... Okay then."
            mc "See you later."
            angela "... Yeah, see you."
            scene black with dissolve
            $ renpy.pause()
            jump ch3ep3backfromexercise
        "Focus on helping her":
            $ ch3ep3situp = 2
            scene ch3ep3_12 with dissolve
            mc "Thirty...."
            angela "*Softly breathes* Yeah... Thirty..."
            mc "Well done."
            angela "*Softly breathes* Thank you..."
            mc "Alright, now it's my turn."
            mc "Can you help me?"
            angela "Of course, sure."
            scene black with dissolve
            $ renpy.pause()
            s "*A few moments later after [angela] helped you do push-ups until finished*....."
            scene ch3ep3_15 with dissolve
            mc "Thank you, [angela]."
            angela "You're welcome."
            mc "Alright, shall we go back now?"
            angela "Sure. Let's go."
            scene black with dissolve
            $ renpy.pause()
            jump ch3ep3backfromexercise
label ch3ep3backfromexercise:
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_16 with fade
    u "Okay... I've arrived home."
    u "I'm all stinky and sweaty now."
    u "Let's go clean myself up."
    scene black with dissolve
    scene ch3ep3_17 with dissolve
    zeke "Oh...?"
    zeke "Good morning, [mc]."
    mc "Good morning, everyone."
    zeke "Where have you been? We were looking for you."
    scene ch3ep3_18 with dissolve
    mc "I've just come back from jogging."
    zeke "Bro, why didn't you tell me?"
    zeke "If you told me, I'd have joined you."
    mc "... Next time then."
    scene ch3ep3_19 with dissolve
    rin "Anyway, let's have breakfast together."
    rin "Is there anything you want to eat?"
    rin "I'll make it for you."
    scene ch3ep3_20 with dissolve
    mc "Thanks, [rin]."
    mc "But, I'll go take a shower first."
    mc "I'm too sweaty now."
    rin "Okay. I get it."
    mc "Alright then, I'll see you guys again in fifteen minutes."
    scene ch3ep3_21 with dissolve
    u "Alright..."
    u "Let's hurry up. I don't want them to wait for me too long."
    scene black with dissolve
    $ renpy.pause()
    s "About fifteen minutes later........."
    scene ch3ep3_22 with dissolve
    u "I've finished dressing up now."
    u "Let's go back to the dining room."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time having breakfast with everyone, then go to the company together...."
    scene ch3ep3_23 with fade
    stop music fadeout 3.0
    $ renpy.pause()
    play music "sfx/ch2ep1_2.mp3" fadein 3.0
    $ bgm = "Tokyo Music Walker - Your Little Wings"
    scene ch3ep3_24 with dissolve
    mc "Hm...?"
    rowan "Oh...?"
    scene ch3ep3_25 with dissolve
    yui "Good morning, president."
    rowan "Good morning, [yui]."
    yui "What? You remember my name?"
    rowan "Of course. I remember every one that is my employee."
    yui "How nice of you."
    scene ch3ep3_26 with dissolve
    rowan "Good morning, [mc]."
    mc "Good morning..."
    mc "What are you doing here?"
    scene ch3ep3_27 with dissolve
    rowan "I've been looking for you, [mc]."
    mc "Hm...? Why?"
    rowan "There's something I'd like to talk about with you."
    mc "I see..."
    scene ch3ep3_28 with dissolve
    rowan "I'm sorry, [yui]..."
    rowan "But, can I borrow your friend for a sec?"
    yui "Of course, you can."
    yui "There is no need to ask for my permission."
    rowan "*Smiles* Thank you."
    scene ch3ep3_29 with dissolve
    mc "Where are we heading to?"
    rowan "The sitting room."
    rowan "Let's go take a sit over there and talk."
    mc "Okay. As you wish."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_30 with dissolve
    rowan "How was your weekend?"
    rowan "Did everything go well according to you plan?"
    mc "Yes, it did."
    mc "Right now, [victor] still thinks that I'm loyal to him."
    scene ch3ep3_31 with dissolve
    rowan "That sounds great."
    mc "Still... Just for now...."
    mc "We'll never know what will happen next."
    mc "Anyway, what's it that you wanted to talk about with me?"
    scene ch3ep3_32 with dissolve
    rowan "I wanted to inform you that you don't need to come to work any more."
    mc "... What do you mean? I'm getting sacked?"
    rowan "No, I didn't mean that."
    scene ch3ep3_33 with dissolve
    rowan "I just want to give you more time so that you can focus on dealing with [victor]."
    mc "... What about the works that were assigned to me?"
    rowan "Don't worry. I will find someone to fill your position as fast as I can."
    mc "Won't that be too risky?"
    mc "How will you know that he is not one of [victor]'s underling."
    scene ch3ep3_34 with dissolve
    rowan "Don't worry. I will carefully check his background before hiring him."
    rowan "Moreover, I don't think he will send any more of his underling here."
    rowan "Since he already got the blueprint...."
    scene ch3ep3_35 with dissolve
    mc "That makes sense...."
    mc "Well, it will surely be better for me if I have more time."
    mc "But, I don't want to just throw away my duty."
    mc "I'm going to work until there is someone to replace me."
    scene ch3ep3_36 with dissolve
    rowan "Are you sure?"
    mc "Yeah. I feel better this way."
    rowan "Alright then, if that's what you want."
    scene ch3ep3_37 with dissolve
    rowan "I'll inform you again once I find someone to replace you."
    mc "That will work just fine."
    rowan "It will take about a week at least."
    rowan "But, I will try my best to make it happen as soon as I can."
    scene ch3ep3_38 with dissolve
    mc "That's fine by me."
    mc "Even though you've already got someone to replace me, I can still come here and help you work."
    mc "If that's what you want."
    rowan "How nice of you. Thank you."
    scene ch3ep3_39 with dissolve
    mc "So... Is that all you wanted to tell me?"
    rowan "Yes, that's right."
    mc "Okay..."
    mc "Alright then, please excuse me."
    scene ch3ep3_40 with dissolve
    rowan "Sure. I'm not going to take any more of your time."
    rowan "You may leave now."
    rowan "Good bye. See you later soon."
    mc "Sure."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_41 with dissolve
    u "Alright...."
    u "Let's go back to work...."
    scene black with dissolve
    $ renpy.pause()
    s "You spent your time working until lunch time....."
    scene ch3ep3_42 with dissolve
    u "I'm so hungry right now."
    u "Let's go find something to eat."
    u "I feel like having lunch at the cafeteria today."
    u "Let's go there...."
    scene ch3ep3_43 with dissolve
    s "*Phone vibrates*........."
    u "Hm....?"
    u "Someone is calling me now. Let's find out who it is."
    scene ch3ep3_44 with dissolve
    u "It's [felix]...."
    u "I wonder why he's calling me at this time."
    u "I guess it must be something important."
    scene ch3ep3_45 with dissolve
    mc "Hello...."
    mc "Sure, I can talk with you now."
    mc "But, hang on a sec. Let me find somewhere more quiet."
    scene black with dissolve
    scene ch3ep3_46 with dissolve
    u "Okay...."
    u "Looks like everyone has already left for lunch."
    u "This room will do."
    scene ch3ep3_47 with dissolve
    mc "Are you still there...?"
    mc "Let's continue."
    mc "What is it that you wanted to tell me?"
    scene ch3ep3_52 with fade
    felix "I was informed that the drug transport ship that belongs to [victor] will enter the port tonight."
    felix "We're going to arrest them."
    felix "Do you want to join us?"
    scene ch3ep3_48 with dissolve
    mc "Wait.... "
    mc "Are you sure that the ship belongs to [victor]?"
    mc "How did you know that?"
    scene ch3ep3_53 with dissolve
    felix "I got the information from a reliable source."
    felix "The ship owner's name is one of his men. I re-checked it multiple times."
    felix "If we successfully doing so, we might be able to investigate more and arrest [victor] a lot easier than we thought."
    scene ch3ep3_49 with dissolve
    mc "Hang on a sec...."
    mc "[victor] isn't someone who is easy to deal with like that."
    mc "This isn't the first time the police tried to arrest his drug transport ship."
    mc "You will only get a small fish. He will get away unguilty, as always."
    scene ch3ep3_54 with dissolve
    felix "..................."
    felix "... Yeah. To think about that, you're right."
    felix "I got too excited. I thought we finally got such a valuable opportunity to arrest him."
    scene ch3ep3_50 with dissolve
    mc "How about this?"
    mc "Since you aren't going to get him anyway...."
    mc "Why don't you let me use this opportunity to gain even more trust from him."
    scene ch3ep3_55 with dissolve
    felix "... I'm listening."
    scene ch3ep3_51 with dissolve
    mc "[victor] sent me here to be a spy right?"
    mc "So then, I'm going to do what he wanted me to do."
    mc "I'm sure that he already know about your plan tonight."
    mc "But, I'm going to report him anyway in order to pretend that I'm working for him."
    mc "How does it sound?"
    scene ch3ep3_55 with dissolve
    felix "You want to make use of this opportunity since our operation is going to fail anyway, right?"
    felix ".... That's fair enough."
    felix "Let's do it. Just tell him."
    scene ch3ep3_50 with dissolve
    mc "What about the guy I asked you to look for his information?"
    mc "Have you got anything updated?"
    scene ch3ep3_56 with dissolve
    felix "Not yet."
    felix "I'm still working on it."
    felix "I will tell you as soon as I find out more about him."
    scene ch3ep3_48 with dissolve
    mc "Okay... I get it."
    mc "Thank you."
    scene ch3ep3_57 with dissolve
    felix "Alright, I guess that's all."
    felix "I'm hanging up now."
    felix "Good bye, [mc]."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_58 with dissolve
    u "I'm so hungry..."
    u "Let's go to the cafeteria first."
    u "I'll call [victor] later."
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    scene ch3ep3_59 with fade
    $ renpy.pause()
    scene ch3ep3_60 with dissolve
    cs "Hello. What would you like to have?"
    mc "Is there anything left?"
    cs "There are Lunch Set A and C left."
    mc "Then, I'd like to have set A, please."
    cs "Understood. Hang on a second."
    scene ch3ep3_61 with dissolve
    cs "Sorry to kept you waiting."
    cs "Here's your lunch."
    mc "Thank you."
    scene ch3ep3_62 with dissolve
    u "Ummm....."
    u "There are quite a lot of people here."
    u "Where am I going to sit?"
    if ch3ep1_fayequestion == 1:
        scene ch3ep3_63 with dissolve
        u "Hm...?"
        u "Isn't that [faye]?"
        u "She's sitting over there alone."
        u "What should I do?"
        menu:
            "[smgr]Go sit with her":
                scene ch3ep3_64 with dissolve
                mc "Hello, [faye]."
                faye "... Hm?"
                faye "Hello, [mc]."
                scene ch3ep3_65 with dissolve
                mc "Can I sit with you?"
                faye "Sure. You can sit here."
                mc "Thank you."
                scene ch3ep3_66 with dissolve
                faye "Why are you having lunch alone?"
                faye "Where are your co-workers?"
                mc "They went to have lunch somewhere else."
                mc "But, I usually have lunch alone. Just like you I guess."
                scene ch3ep3_67 with dissolve
                mc "I barely see you have lunch with someone, but yourself."
                faye "Well... You could say that."
                mc "How's everything recently by the way?"
                mc "Is there anything you want me to help you with?"
                scene ch3ep3_68 with dissolve
                faye "I've been pretty busy with my jobs."
                faye "Since we are going to annouce the Xecon's gear to the world soon."
                faye "There is nothing you can help right now. But, thanks for asking."
                mc "I see...."
                scene ch3ep3_69 at eyesblink("Ch.3/Ep.3/Scenes/ch3ep3_69.jpg", "Ch.3/Ep.3/Scenes/ch3ep3_69_blink.jpg", 1) with dissolve
                faye "What about you?"
                mc "Everything's been a little bit hasty for me."
                mc "I mean... we just moved to the new house yesterday."
                mc "And this morning [rowan] just told me that he'll find someone to replace me so that I can have more free time to focus on my problem."
                faye "I see.... I wish you best luck then."
                mc "What are you going to do after lunch?"
                faye "I will go back to my office. Why?"
                menu:
                    "Can I go with you? [smrec]":
                        scene ch3ep3_70 with dissolve
                        mc "Can I go to your office with you?"
                        faye "... Hm? Why?"
                        mc "I don't have any plan after lunch."
                        mc "Can I go sit in your office for a while?"
                        faye "Well... I don't have any problem with that."
                        faye "Sure. You can follow me to my office."
                        mc "Thank you."
                        faye "Alright then, let's just finish our lunch so that we can leave."
                        scene black with dissolve
                        $ renpy.pause()
                        scene ch3ep3_71 with dissolve
                        faye "Alright...."
                        faye "Since we've finished eating now, let's leave here."
                        mc "Sure."
                        jump ch3ep3fayeoffice
                    "Nothing.":
                        scene ch3ep3_70 with dissolve
                        mc "Nothing. I was just wondering."
                        faye "What about you? What are you going to do after lunch?"
                        mc "I will probably go back to my office as well."
                        faye "I see... Then, let's just finish our lunch so that we can leave."
                        mc "Sure."
                        scene black with dissolve
                        $ renpy.pause()
                        s "*About ten minutes later*............"
                        scene ch3ep3_71_d with dissolve
                        faye "Alright...."
                        faye "I've finished eating. I'm leaving now."
                        mc "Oh... Okay. See you later."
                        faye "Sure. See you later, [mc]."
                        scene black with dissolve
                        $ renpy.pause()
                        s "You spent more time finishing your lunch after [faye] had left...."
                        jump ch3ep3reportvictor
            "Go sit somewhere else":
                scene ch3ep3_64_d with dissolve
                u "Well, she's sitting there alone for a reason."
                u "I guess she wanted to have some time alone at lunch."
                u "Let's go sit somewhere else."
                scene black with dissolve
                $ renpy.pause()
                jump ch3ep3reportvictor
    else:
        u "Well... Let's go sit near the window on the right side."
        scene black with dissolve
        $ renpy.pause()
        s "You spent your time having lunch.........."
        jump ch3ep3reportvictor
label ch3ep3fayeoffice:
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_72 with fade
    faye "Suit your self."
    faye "You can do as you please, but be a little bit quiet, okay?"
    faye "I'm going to work. I'll need to concentrate."
    mc "Got it."
    scene black with dissolve
    $ renpy.pause()
    s "*Some time passed*........."
    scene ch3ep3_73 with dissolve
    mc ".................."
    faye "*Sighs* Finally...."
    scene ch3ep3_74 with dissolve
    faye "*Sighs* Ugh......."
    faye "My neck...."
    u "Hm...?"
    menu:
        "You want some massage? [faye1]":
            $ faye_ch3_ep3 += 1
            $ faye_relationship += 1
            scene ch3ep3_75 with dissolve
            mc "Are you okay?"
            scene ch3ep3_76 with dissolve
            faye "Oh, I'm good. I'm just having a little bit of neck pain as usual."
            faye "It will get better soon."
            scene ch3ep3_75 with dissolve
            mc "Do you want me to give you some massage?"
            scene ch3ep3_76 with dissolve
            faye "Hm? Do you know how to give a massage?"
            scene ch3ep3_75 with dissolve
            mc "Well... I just know how to do it. I'm not that good."
            mc "But, I can help you with your neck pain if you want."
            mc "What do you think?"
            scene ch3ep3_76 with dissolve
            faye "Umm...."
            faye "Okay. Let's give it a try."
            mc "Okay. Wait a second."
            scene black with dissolve
            scene ch3ep3_77 with dissolve
            mc "Alright...."
            mc "Are you ready?"
            faye "Okay. Let's get started."
            mc "How does it feel?"
            faye "Mhmm.... Good."
            scene ch3ep3_78 with dissolve
            mc "Do you want me to massage you harder?"
            faye "No. This is good enough already."
            faye "Yes... That's the spot."
            faye "Keep focusing that area just like that."
            mc "As you wish..."
            scene ch3ep3_79 with dissolve
            faye "You were wrong about what you said earlier, [mc]."
            mc "Hm? About what?"
            faye "You are a very good masseur."
            mc "... Thank you."
            menu:
                "Touch her breasts [faye2]":
                    $ ch3ep3massage = 1
                    $ faye_ch3_ep3 += 2
                    $ faye_relationship += 2
                    stop music fadeout 3.0
                    jump ch3ep3fayesex
                "Keep massaging her neck":
                    $ ch3ep3massage = 2
                    scene black with dissolve
                    $ renpy.pause()
                    s "*A few minutes later*............."
                    scene ch3ep3_80_d with dissolve
                    faye "Alright, I think that's enough."
                    mc "Are you sure?"
                    faye "Yes. I've gotten much better now."
                    faye "Thank you for your service, [mc]."
                    faye "I'm very grateful for that."
                    mc "You're welcome."
                    scene black with dissolve
                    $ renpy.pause()
                    s "*A few minutes later*..........."
                    scene ch3ep3_75 with dissolve
                    mc "Alright...."
                    mc "I think I should leave now."
                    mc "Thank you for letting me stay here."
                    scene ch3ep3_76 with dissolve
                    faye "Oh. Okay."
                    faye "Good bye. See you around."
                    scene ch3ep3_75 with dissolve
                    mc "Good bye."
                    scene black with dissolve
                    $ renpy.pause()
                    jump ch3ep3reportvictor

        "Are you okay?":
            scene ch3ep3_75 with dissolve
            mc "Are you okay?"
            scene ch3ep3_76 with dissolve
            faye "Oh, I'm good. I'm just having a little bit of neck pain as usual."
            faye "It will get better soon."
            scene ch3ep3_75 with dissolve
            mc "As usual? That doesn't sound good to me."
            mc "I think you should go see a doctor."
            scene ch3ep3_76 with dissolve
            faye "I know. I've been thinking about that as well."
            scene ch3ep3_75 with dissolve
            mc "Okay..."
            mc "Alright then, I think I should leave now."
            mc "Thank you for letting me stay here."
            scene ch3ep3_76 with dissolve
            faye "You're welcome."
            faye "Good bye. See you around."
            scene ch3ep3_75 with dissolve
            mc "Good bye, [faye]."
            scene black with dissolve
            $ renpy.pause()
            jump ch3ep3reportvictor
label ch3ep3fayesex:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    play music "sfx/ep4_2.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - Woho, I Thought It Be Me & You (ft. Lily Hain)"
    scene ch3ep3_80 with vpunch
    faye "Huh...?!"
    mc "... I'm sorry. My hands slipped."
    faye "..............."
    scene ch3ep3_81 with dissolve
    u "Hm...? Why isn't she saying anything?"
    u "Does that mean I can keep on going?"
    faye "................"
    u "Alright then, let's keep on going."
    scene ch3ep3_82 with dissolve
    faye "*Softly breathes* Ahh...."
    faye "*Softly breathes* I don't remember... having breasts pain."
    mc "Then, do you want me to take my hands off?"
    faye "*Softly breathes*............"
    scene ch3ep3_83 with dissolve
    faye "*Softly breathes* Hold on...."
    mc "... Why?"
    faye "*Softly breathes* Let me take off my top...."
    mc "Okay...."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_84 with dissolve
    faye "Alright...."
    faye "You can... keep going now."
    mc "Sure. As you wish."
    scene ch3ep3_85 with dissolve
    show ch3ep3_faye1
    window hide
    faye "*Softly breathes* Ahhh...."
    $ renpy.pause()
    scene ch3ep3_86 with dissolve
    hide ch3ep3_faye1
    show ch3ep3_faye2
    window hide
    faye "*Softly breathes* Mhmm...."
    faye "(*Softly breathes* I can't believe that I'm doing something like this here...)"
    scene ch3ep3_87 with dissolve
    hide ch3ep3_faye2
    show ch3ep3_faye3
    window hide
    faye "*Softly breathes* Arngh...."
    $ renpy.pause()
    faye "*Softly breathes* Can you help me take off my pants...?"
    mc "Sure thing."
    scene ch3ep3_88 with dissolve
    hide ch3ep3_faye3
    mc "Let me unbutton it...."
    faye "Okay...."
    scene black with dissolve
    scene ch3ep3_89 with dissolve
    faye "I will never do something like this here if it wasn't with you..."
    mc "Really? I'm glad to hear that...."
    faye "Kiss me..."
    mc "Okay..."
    scene ch3ep3_90 with dissolve
    faye "*Kisses* Mhmm....."
    mc "*Kisses* Put your tongue out..."
    faye "*Kisses* Like this...?"
    mc "*Kisses* Yeah..."
    scene ch3ep3_91 with vpunch
    s "*Door knocks*........."
    faye "!!!!!!"
    unknown "May I come in, please?"
    faye "W-Wait a minute! Don't come in yet!"
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_92 with dissolve
    faye "Hide under the table, [mc]!"
    mc "I..."
    faye "Hurry up!"
    mc "Okay...."
    scene black with dissolve
    scene ch3ep3_93 with dissolve
    ae "Good afternoon, team leader [faye]."
    faye "G-Good afternoon."
    faye "What brings you here?"
    ae "There are some documents you need to sign. So..."
    u "I don't know what's wrong with me today, but..."
    u "I feel like teasing her now...."
    faye "I see. You can leave them over t-"
    scene ch3ep3_94 with vpunch
    faye "T-There...!!"
    scene ch3ep3_95 with dissolve
    ae "Hm...?"
    ae "What's wrong, team leader [faye]?"
    faye "*Softly breathes* N-Nothing...!"
    ae "Are you sure? You don't look so good right now."
    scene ch3ep3_96 with dissolve
    show ch3ep3_faye4
    window hide
    faye "*Softly breathes* Y...Yeah. Don't mind me."
    faye "*Softly breathes* I... was just bitten by a bug."
    scene ch3ep3_97 with dissolve
    hide ch3ep3_faye4
    show ch3ep3_faye5
    window hide
    ae "A bug?"
    faye "*Softly breathes* Y-Yeah...!"
    faye "*Softly breathes* J... Just put the documents on the table and leave."
    ae "Okay. I get it. I'm going to put it right here."
    faye "*Softly breathes* O... Okay. I will sign them... when I have some free time."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_98 with dissolve
    hide ch3ep3_faye5
    show ch3ep3_faye6
    window hide
    faye "*Heavily breathes* A-Ahh...!!"
    faye "*Heavily breathes* Mhmmm...! A-Almost there...!"
    $ renpy.pause()
    scene ch3ep3_99 with vpunch
    hide ch3ep3_faye6
    faye "I-I'm cumming...!!!"
    scene ch3ep3_99 with vpunch
    faye "Mhmmm...!!"
    scene black with dissolve
    scene ch3ep3_100 with dissolve
    faye "*Pants* [mc]! You...!"
    faye "*Pants* What... if we... got caught?!"
    mc "*Smirks*... What?"
    faye "*Pants* What? Did you... just laugh?"
    mc "... No, I didn't."
    faye "*Pants* Just you wait...."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_101 with dissolve
    faye "Alright, I've already locked the door."
    faye "Just wait right there...."
    mc "I'm waiting..."
    scene ch3ep3_102 with dissolve
    faye "I'm going to make you regret for teasing me earlier..."
    mc "Yeah? How will you do that?"
    faye "We'll see..."
    faye "Take off your clothes."
    scene ch3ep3_103 with dissolve
    mc "I wonder how you are going to make me regret"
    mc "Isn't it only going to make me feel good this way?"
    faye "You'll know it soon...."
    scene ch3ep3_104 with dissolve
    show ch3ep3_faye7
    window hide
    faye "*Licks* I'm going to make you cum again and again that you have to beg me to stop..."
    mc "Okay. I can't wait to see that happen..."
    $ renpy.pause()
    scene ch3ep3_105 with dissolve
    hide ch3ep3_faye7
    show ch3ep3_faye8
    window hide
    mc "*Softly breathes* Arrr....."
    faye "*Licks* Don't cum just yet. We're just getting started..."
    $ renpy.pause()
    scene ch3ep3_106 with dissolve
    hide ch3ep3_faye8
    show ch3ep3_faye9
    window hide
    mc "*Softly breathes* If you think I'm going to cum, you're underestimating me."
    mc "*Softly breathes* You can't make me cum just by doing this."
    $ renpy.pause()
    scene ch3ep3_107 with dissolve
    faye "I know..."
    faye "That's why I told you... We're just getting started...."
    mc "I see..."
    scene ch3ep3_108 with dissolve
    faye "It's a real deal from now on..."
    mc "Okay. You do you."
    scene ch3ep3_109 with dissolve
    show ch3ep3_faye10
    window hide
    faye "*Sucks* Mhmmm....."
    mc "*Softly breathes* Arrr...."
    $ renpy.pause()
    scene ch3ep3_110 with dissolve
    hide ch3ep3_faye10
    show ch3ep3_faye11
    window hide
    faye "*Sucks* Mhmmm.... How do you feel now...?"
    faye "*Sucks* Mhmmmm... You're about to cum, right? I can feel it."
    scene ch3ep3_111 with dissolve
    hide ch3ep3_faye11
    show ch3ep3_faye12
    window hide
    faye "*Sucks* Mhmm.... Just let it out.... I know you're holding it."
    mc "*Softly breathes* No, I'm not... You just have to do better than this."
    $ renpy.pause()
    scene black with dissolve
    scene ch3ep3_112 with dissolve
    hide ch3ep3_faye12
    faye "Fine...."
    faye "Let see if you can still handle this...."
    scene ch3ep3_113 with dissolve
    faye "*Softly breathes* Ahhh...."
    mc "*Softly breathes* Well... From what I see, I'm afraid you will cum before me."
    scene ch3ep3_114 with dissolve
    show ch3ep3_faye13
    hide ch3ep3_faye12
    window hide
    faye "*Softly breathes* Mhmmm.... That's not true...."
    mc "*Softly breathes* Yes, it is...."
    $ renpy.pause()
    scene ch3ep3_115 with dissolve
    hide ch3ep3_faye13
    show ch3ep3_faye14
    window hide
    faye "*Softly breathes* Mhmmm...."
    $ renpy.pause()
    scene ch3ep3_116 with dissolve
    hide ch3ep3_faye14
    show ch3ep3_faye15
    faye "*Heavily breathes* Hahhh.... Just cum already...."
    mc "*Softly breathes* It's not going to happen now..."
    $ renpy.pause()
    scene ch3ep3_117 with dissolve
    hide ch3ep3_faye15
    faye "Aw...! What are you doing?!"
    mc "You can't make me cum just by doing that."
    mc "I'm going to take the lead from now on."
    scene ch3ep3_118 with dissolve
    faye "Okay... I give up."
    faye "Put it in right now and do me as you please."
    mc "Okay...."
    scene ch3ep3_119 with dissolve
    faye "*Softly breathes* A-Ah....!"
    show ch3ep3_faye16
    window hide
    faye "*Softly breathes* Mhhmm.... So good...."
    faye "*Softly breathes* Hah.... Faster... Faster, [mc]...."
    $ renpy.pause()
    scene ch3ep3_120 with dissolve
    hide ch3ep3_faye16
    show ch3ep3_faye17
    window hide
    faye "*Softly breathes* Hahh.... Yeah... Keep fucking me like that...."
    $ renpy.pause()
    scene ch3ep3_121 with dissolve
    hide ch3ep3_faye17
    show ch3ep3_faye18
    window hide
    faye "*Heavily breathes* A-Ahhh...! Ahhhh....!"
    faye "*Heavily breathes* [mc]...! I-I'm about to cum...!"
    mc "*Softly breathes* Me, too..."
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep3_faye18
            jump ch3ep3_fayecow1
        "Slowest":
            hide ch3ep3_faye18
            jump ch3ep3_fayemis1
        "Slower":
            hide ch3ep3_faye18
            jump ch3ep3_fayemis2
        "Cum":
            jump ch3ep3_fayemiscum
label ch3ep3_fayecow1:
    scene ch3ep3_114 with dissolve
    show ch3ep3_faye13
    window hide
    $ renpy.pause()
    menu:
        "Desk Missionary":
            hide ch3ep3_faye13
            jump ch3ep3_fayemis1
        "Faster":
            hide ch3ep3_faye13
            jump ch3ep3_fayecow2
        "Fastest":
            hide ch3ep3_faye13
            jump ch3ep3_fayecow3
label ch3ep3_fayecow2:
    scene ch3ep3_115 with dissolve
    show ch3ep3_faye14
    window hide
    $ renpy.pause()
    menu:
        "Desk Missionary":
            hide ch3ep3_faye14
            jump ch3ep3_fayemis1
        "Slower":
            hide ch3ep3_faye14
            jump ch3ep3_fayecow1
        "Faster":
            hide ch3ep3_faye14
            jump ch3ep3_fayecow3
label ch3ep3_fayecow3:
    scene ch3ep3_116 with dissolve
    show ch3ep3_faye15
    window hide
    $ renpy.pause()
    menu:
        "Desk Missionary":
            hide ch3ep3_faye15
            jump ch3ep3_fayemis1
        "Slowest":
            hide ch3ep3_faye15
            jump ch3ep3_fayecow1
        "Slower":
            hide ch3ep3_faye15
            jump ch3ep3_fayecow2
label ch3ep3_fayemis1:
    scene ch3ep3_119 with dissolve
    show ch3ep3_faye16
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep3_faye16
            jump ch3ep3_fayecow1
        "Faster":
            hide ch3ep3_faye16
            jump ch3ep3_fayemis2
        "Fastest":
            hide ch3ep3_faye16
            jump ch3ep3_fayemis3
label ch3ep3_fayemis2:
    scene ch3ep3_120 with dissolve
    show ch3ep3_faye17
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep3_faye17
            jump ch3ep3_fayecow1
        "Slower":
            hide ch3ep3_faye17
            jump ch3ep3_fayemis1
        "Faster":
            hide ch3ep3_faye17
            jump ch3ep3_fayemis3
label ch3ep3_fayemis3:
    scene ch3ep3_121 with dissolve
    show ch3ep3_faye18
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep3_faye18
            jump ch3ep3_fayecow1
        "Slowest":
            hide ch3ep3_faye18
            jump ch3ep3_fayemis1
        "Slower":
            hide ch3ep3_faye18
            jump ch3ep3_fayemis2
        "Cum":
            jump ch3ep3_fayemiscum
label ch3ep3_fayemiscum:
    faye "*Heavily breathes* Almost there...! Almost there...!"
    mc "*Softly breathes* Ugh....."
    faye "*Heavily breathes* I'm...."
    scene ch3ep3_122 with vpunch
    faye "*Heavily breathes* Cumming...!!"
    scene ch3ep3_122 with vpunch
    faye "*Heavily breathes* A-Ahhhh....!!!"
    menu:
        "Cum inside":
            scene ch3ep3_122 with vpunch
            mc "*Softly breathes* Ugh... I'm cumming, too...."
            $ renpy.pause()
            scene black with dissolve
            scene ch3ep3_123_in with dissolve
        "Cum outside":
            scene ch3ep3_122_out with vpunch
            mc "*Softly breathes* Ugh... I'm cumming, too...."
            $ renpy.pause()
            scene black with dissolve
            scene ch3ep3_123_out with dissolve
    faye "*Pants* T... That was so good...."
    mc "*Softly breathes* Yeah..."
    faye "*Pants* You're the best...."
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*..........."
    scene ch3ep3_124 with dissolve
    mc "Alright... I think I should leave now."
    mc "It's already half past one."
    mc "I'm sorry that you failed to make me regret for teasing you."
    faye "*Giggles* Shut up...."
    scene ch3ep3_125 with dissolve
    mc "Okay. Thank you for letting me stay here."
    mc "See you later, [faye]."
    faye "You can come here any time you want for now on."
    faye "Good bye, [mc]."
    stop music fadeout 3.0
    $ renpy.end_replay()
    scene ch3ep3_126 with dissolve
    u "Alright.... Let's go back to my department."
    u "Oh... I almost forgot."
    u "I have to call [victor] and tell him about [felix]'s plan tonight."
    u "Let's go find somewhere quiet."
    scene black with dissolve
    $ renpy.pause()
    jump ch3ep3reportvictor
label ch3ep3reportvictor:
    play music "sfx/ep2_7.mp3" fadein 3.0
    $ bgm = "AERØHEAD - The Reckoning"
    scene ch3ep3_127 with fade
    u "Okay.... Seems like there is no one here."
    u "This room will do."
    scene ch3ep3_128 with dissolve
    u "Let's call [victor] now..."
    scene ch3ep3_129 with dissolve
    mc "...................."
    mc ".... Good afternoon, sir."
    mc "Do you have some free time?"
    scene ch3ep3_133 with fade
    victor "Yes, I do."
    victor "You've got something to report?"
    scene ch3ep3_130 with dissolve
    mc "Yes, I have."
    mc "I have a very crucial information to tell you."
    scene ch3ep3_133 with dissolve
    victor "A very crucial information?"
    victor "What is it?"
    scene ch3ep3_130 with dissolve
    mc "It's about your drug transport ship that's going to arrive tonight."
    mc "I was informed that there the police is planning to arrest them."
    scene ch3ep3_134 with dissolve
    victor "I see..."
    victor "Where did you get that information from?"
    scene ch3ep3_131 with dissolve
    mc "I got that information from [tom]. The guy I told you before."
    mc "Do you remember him?"
    scene ch3ep3_134 with dissolve
    victor "Yes, I do."
    victor "You said he's the kid who got kicked out because he failed the test, right?"
    victor "I never knew he was such a big mouth."
    scene ch3ep3_131 with dissolve
    mc "I guess it's because he trust me with his heart."
    mc "You know.... Since I used to be his best friend."
    scene ch3ep3_136 with dissolve
    victor "I see..."
    victor "[rio]."
    rio "Yes, sir?"
    victor "Call someone who's in the drug transport ship that's going to arrive tonight."
    victor "And tell them to change the destination."
    rio "Understood."
    scene ch3ep3_135 with dissolve
    victor "Thank you for reporting it to me, [mc]."
    victor "It is a very valuable information."
    victor "You've done a great job."
    scene ch3ep3_129 with dissolve
    mc "With my pleasure..."
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    scene ch3ep3_132 with dissolve
    u "Alright, I've done calling [victor]."
    u "Let's go back to work..."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time working until evening...."
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene ch3ep3_137 with dissolve
    mc "......................"
    unknown "[mc]."
    mc "... Yes?"
    scene ch3ep3_138 with dissolve
    mc "Oh. It's you."
    mc "Is there anything you want?"
    yui "What do you mean? Is there anything I want?"
    yui "It's already 5 p.m."
    scene ch3ep3_139 with dissolve
    yui "Let's go home."
    mc "Oh... Okay. Give me five minute."
    mc "I have to finish fixing this bug first."
    yui "Okay. Then, come and call me when you're ready."
    mc "Sure."
    scene black with dissolve
    $ renpy.pause()
    s "About five minutes later................."
    scene ch3ep3_140 with dissolve
    yui "Alright, let's go."
    yui "[rin] and [zeke] have been waiting for us in the garage."
    mc "Then, we better hurry up."
    yui "*Laughs* Tell me something I don't know."
    scene black with dissolve
    $ renpy.pause()
    s "Later that evening........."
    scene ch3ep3_141 with fade
    u "I've finished taking a shower."
    u "Now, I'm starting to get hungry."
    u "Let's go find something to eat."
    scene ch3ep3_142 with dissolve
    u "Hm....?"
    u "Where's everyone?"
    u "I thought I was at least going to see [rin] cooking dinner here."
    scene ch3ep3_143 with dissolve
    s "*Water splashes*................"
    u "Hm....? There's someone at the pool?"
    u "I guess they are all there then."
    u "Let's go see them."
    scene ch3ep3_144 with dissolve
    u "Oh... It's only [yui]."
    u "I thought they were going to be all here."
    u "Let's ask her where everone is."
    scene ch3ep3_145 with dissolve
    mc "[yui]."
    yui "Huh...?"
    yui "Oh, it's you."
    scene ch3ep3_146 with dissolve
    mc "Where are [rin] and [zeke]?"
    mc "I couldn't find them in the house."
    yui "They went to pick [mika] up in the city."
    mc "Oh, I see..."
    scene ch3ep3_147 with dissolve
    yui "[zeke] told you that she will be back today."
    yui "Have you already forgot?"
    mc "Yeah, I forgot."
    mc "By the way, how is the water by the way?"
    scene ch3ep3_148 with dissolve
    yui "Perfect. Not too hot and not too cold."
    mc "Great for you..."
    yui "It feels so good down here. Do you want to join?"
    yui "Come on. Take off your top and get down here."
    mc "......................"
    menu:
        "Join her. [yui1]":
            $ ch3ep3swim = 1
            $ yui_ch3_ep3 += 1
            $ yui_relationship += 1
            scene ch3ep3_149_a with dissolve
            mc "Alright...."
            mc "I feel like swimming as well."
            yui "Lovely. Hurry up and take off your top already."
            scene ch3ep3_150 with dissolve
            mc "I'm going to jump in."
            mc "Fall back for a little bit so that you don't accidentally get hit."
            yui "Oh! Okay!"
            scene ch3ep3_151 with dissolve
            yui "How do you feel now?"
            mc "Pretty good..."
            yui "It's so good to have a swimming pool at home. Don't you agree?"
            yui "It helps relieve stress very well."
            yui "I think from now on I'll swim every day after coming back from work."
            mc "I couldn't agree more."
            scene black with dissolve
            $ renpy.pause()
            s "About half an hour later............"
            scene ch3ep3_152 with dissolve
            yui "Hm...?"
            yui "You're leaving already?"
            scene ch3ep3_153 with dissolve
            mc "Yeah.... I've had enough fun."
            mc "I also feel that [rin] and [zeke] are about to come back soon."
            mc "Therefore, I'm going to take a shower and get ready for dinner."
            scene ch3ep3_154 with dissolve
            yui "I see..."
            yui "Alright then. See you again soon."
            yui "I'm going to stay in here for a little bit longer."
            mc "Yeah. See you."
            scene black with dissolve
            $ renpy.pause()
            jump ch3ep3dinner
        "I will go back inside.":
            $ ch3ep3swim = 2
            scene ch3ep3_149_d with dissolve
            mc "Thanks, but I'll pass."
            mc "I'm going to go back inside the house and wait for them to come back."
            yui "Oh... Okay."
            yui "See you again soon then."
            mc "Yeah. See you."
            scene black with dissolve
            $ renpy.pause()
            jump ch3ep3dinner
label ch3ep3dinner:
    scene black with dissolve
    $ renpy.pause()
    s "About half an hour later........."
    scene ch3ep3_154_1 with dissolve
    u "I almost forgot...."
    u "I should tell [felix] about what I heard from [victor]."
    u "Let's call him."
    scene ch3ep3_154_2 with dissolve
    mc "....................."
    mc "... Hello, [felix]."
    mc "Have you already arrived at the port? Can we talk?"
    scene ch3ep3_154_4 with dissolve
    felix "No, I haven't. I'm still at the police station."
    felix "Sure, we can."
    felix "What do you want to talk about?"
    scene ch3ep3_154_2 with dissolve
    mc "I already informed [victor] about your plan tonight."
    mc "I heard him told [rio] to call someone in that ship."
    mc "They're going to change the destination."
    mc "So, I'm supposed to you aren't going to see them at the port that you are going to go."
    scene ch3ep3_154_5 with dissolve
    felix "Really? What's the new destination then?"
    felix "Do you happen to know it?"
    scene ch3ep3_154_3 with dissolve
    mc "No, I'm not."
    mc "He didn't say the name."
    mc "But, I think you should keep doing your original plan."
    mc "Because if you cancel your plan or happen to be waiting them at the new destination..."
    scene ch3ep3_154_5 with dissolve
    felix "He will suspect you, right?"
    scene ch3ep3_154_3 with dissolve
    mc "That's right."
    scene ch3ep3_154_5 with dissolve
    felix "Fine...."
    felix "I will keep doing my plan tonight even if it's going to fail for sure."
    felix "I should sacrifice something to get something else."
    felix "It's better for me if [victor] doesn't suspect you."
    scene ch3ep3_154_3 with dissolve
    mc "Yeah. It's better for both of us."
    scene ch3ep3_154_4 with dissolve
    felix "Alright. Thank you for your information."
    felix "I'm hanging up now. Bye."
    scene ch3ep3_154_2 with dissolve
    mc "Bye."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_155 with fade
    u "Alright...."
    u "It's time for dinner."
    u "Let's go to the kitchen."
    scene ch3ep3_156 with dissolve
    u "Hm...?"
    u "[elaine] and [wendy]?"
    u "What a surprise... I didn't expect to see them here today."
    scene ch3ep3_157 with dissolve
    mc "Hi, guys."
    elaine "Oh? Hey, [mc]."
    wendy "Good evening, [mc]."
    scene ch3ep3_158 with dissolve
    mc "No one told me that you guys were going to pay a visit today."
    elaine "I didn't plan on visiting you guys today as well."
    elaine "Actually, I didn't even know that you guys moved here."
    scene ch3ep3_159 with dissolve
    wendy "Yeah.... Until [rin] texted me about an hour ago."
    wendy "She asked if we wanted to come."
    elaine "That's right."
    mc "I see..."
    scene ch3ep3_158 with dissolve
    mc "By the way... Where is everyone?"
    elaine "[rin] and [yui] are in the kitchen right now."
    elaine "But, I don't know where everyone else is."
    elaine "Probably in their bedrooms I guess."
    scene ch3ep3_160 with dissolve
    mc "I get it."
    mc "Alright then, I'm going to ask [rin] and [yui] if they need any help."
    elaine "Don't bother."
    mc "Hm...?"
    scene ch3ep3_157 with dissolve
    mc "What do you mean?"
    elaine "We already asked them that."
    elaine "But, they said they didn't want any help."
    elaine "That's why we're sitting here watching TV."
    wendy "Yeah...."
    elaine "So, you better come here. Take a seat and watch TV together with us."
    mc "... Okay. If that's the case."
    scene black with dissolve
    scene ch3ep3_161 with dissolve
    mc "What are you guys watching?"
    elaine "Games of Thrones. Season one Episode one."
    mc "Hm? You guys have never watched it before?"
    wendy "Yes, I have."
    scene ch3ep3_162 with dissolve
    elaine "Me, too."
    mc "Then, why...?"
    elaine "We didn't know what we wanted to watch since we've already watched a lot of series."
    wendy "So, we agreed to re-watch it again."
    scene ch3ep3_163 with dissolve
    wendy "Just to kill time."
    elaine "Yeah... Just to kill time."
    mc "I see..."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time watching Games of Thrones with [elaine] and [wendy]......"
    scene ch3ep3_164 with dissolve
    rin "[elaine], [wendy], [mc]."
    elaine "Hm...?"
    scene ch3ep3_165 with dissolve
    elaine "Yeah, [rin]?"
    rin "Sorry to kept you guys waiting."
    rin "Dinner is ready."
    elaine "Oh! Okay... We're coming."
    if nominatekrystal == 1:
        scene ch3ep3_166_k with dissolve
    else:
        scene ch3ep3_166 with dissolve
    $ renpy.pause()
    scene ch3ep3_167 with dissolve
    zeke "Come. Take a seat, guys."
    elaine "Wow... They look all delicious..."
    wendy "Thank you for cooking us dinner, [rin], [yui]."
    rin "Come on. Don't act like a stranger."
    yui "Yeah... It's nothing much."
    yui "It actually was a great experience for me since I learned a lot of cooking techniques from [rin]."
    scene ch3ep3_168 with dissolve
    elaine "I wish you could teach me some as well."
    wendy "Me, too."
    rin "Sure. Why not? Next time I will teach you guys."
    rin "*Giggles* But, now you guys should take a seat already so that we can start eating."
    rin "*Giggles* I'm very hungry right now."
    elaine "*Giggles* Oh...! I'm sorry!"
    scene black with dissolve
    $ renpy.pause()
    s "*A few hours later*................"
    scene ch3ep3_169 with dissolve
    elaine "Thank you for today, guys."
    elaine "I think it's time for us to leave now."
    wendy "Yeah. It's getting late."
    scene ch3ep3_170 with dissolve
    rin "Okay. Get home safely."
    yui "Good bye, [elaine], [wendy]."
    zeke "See you tomorrow!"
    elaine "Sure. See you guys tomorrow."
    wendy "Good bye, everyone."
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_171 with dissolve
    yui "Okay.... I think that's it for today."
    yui "Good night, everyone."
    rin "You, too. Have a good sleep."
    scene ch3ep3_172 with dissolve
    mc "I'm also going back to my room as well."
    mc "See you tomorrow, guys."
    rin "Sure. See you tomorrow, [mc]."
    zeke "Have a good rest, bro."
    scene black with dissolve
    $ renpy.pause()
    stop music fadeout 3.0
    scene ch3ep3_173 with dissolve
    u "It's already late now. I'm so tired today."
    u "I guess it's because I just got back to exercising for the first time after a while."
    u "My body hasn't got used to it yet."
    u "Let's go to bed and take a rest."
    scene black with dissolve
    $ renpy.pause()
    s "Next morning............."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_174 with dissolve
    play music "sfx/ch2ep1_1.mp3" fadein 3.0
    $ bgm = "Roa - Winter Magic"
    u "Mmmmm....."
    u "Hm...? Is it already morning?"
    u "Well, time really flew so fast..."
    u "Alright, let's just get up."
    scene ch3ep3_175 with dissolve
    u "I still feel like I haven't got enough rest..."
    u "What should I do next?"
    u "Should I get changed and go exercising, or just skip it today?"
    menu:
        "Go exercising":
            $ ch3ep3goexercise = 1
            jump ch3ep3part1end
        "Skip it":
            $ ch3ep3goexercise = 2
            jump ch3ep3part1end
label ch3ep3part1end:
    if ch3ep3goexercise == 1:
        scene ch3ep3_176 with dissolve
        u "Let's go exercising."
        u "No matter how tired I am, I shouldn't skip a day from now on."
        u "I can't allow myself to get any weaker."
        u "Otherwise, I won't be able to go against [victor] for sure."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep3_177_a with dissolve
        u "Alright, let's go."
        u "Oh... I almost forgot."
        u "[zeke] told me yesterday to invite him."
        u "Let's go find him."
        scene black with dissolve
        scene ch3ep3_178 with dissolve
        s "*Door knocks*..........."
        mc "[zeke]."
        mc "Are you in there?"
        zeke "[mc]? Hold on a sec!"
        scene black with dissolve
        scene ch3ep3_179 with dissolve
        zeke "Good morning, [mc]."
        mc "Good morning."
        zeke "What's up? Why are you looking for me?"
        mc "Have you already forgot?"
        scene ch3ep3_180 with dissolve
        zeke "Hm? What have I forgot?"
        mc "Didn't you tell me to invite you to go exercising yesterday?"
        zeke "Oh! Yeah, that's right!"
        zeke "My bad... Are you going to go now?"
        scene ch3ep3_181 with dissolve
        mc "Yes, I am."
        zeke "Okay then, wait a minute."
        zeke "Let me go get changed first."
        zeke "I'll be back soon."
        mc "Got it."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep3_182 with fade
        zeke "Bro. I'm so excited now."
        mc "... Why?"
        zeke "It's been a while since the last time I exercised."
        zeke "I'm excited to see how much I can do now."
        mc "I see...."
        scene ch3ep3_183 with dissolve
        mc "Alright then, let's start warming up with a jogging then."
        zeke "Sure. Let's go."
        mc "Oh... By the way, [angela] is living nearby."
        zeke "Hm? Really?"
        mc "Yeah. I saw her yesterday when I was jogging."
        mc "She was about to go jogging as well, so we went jogging together."
        mc "She said that she always exercise in the morning. So, we might meet her again today."
        zeke "I see."
        scene black with dissolve
        scene ch3ep3_184 with dissolve
        zeke "Oh... Speaking of the devil..."
        zeke "There she is..."
        mc "Yeah. I told you we might meet her again."
        angela "Hm...?"
        scene ch3ep3_185 with dissolve
        mc "Hi, [angela]."
        zeke "Good morning, [angela]!"
        angela "... Good morning, guys."
        angela "I'm a little bit surprised. I didn't expect you to join us, [zeke]."
        zeke "Oh! I told [mc] yesterday to invite me today."
        angela "I see..."
        mc "Shall we go now?"
        angela "Okay, sure."
        scene ch3ep3_186 with dissolve
        zeke "It's been so long since the last time I exercised. I'll try my best to keep up."
        angela "Don't push yourself too hard then."
        angela "You might get injured."
        zeke "Sure. I get it."
        angela "Good..."
        scene black with dissolve
        $ renpy.pause()
        jump ch3ep3_exercise
    elif ch3ep3goexercise == 2:
        scene ch3ep3_176 with dissolve
        u "I feel so lazy today."
        u "Let's just skip exercising today."
        u "Let's go find something to eat."
        u "Then, I will come back here and take a shower and get ready for work."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep3_177_d with dissolve
        u "Alright..."
        u "Let's go to the kitchen."
        scene black with dissolve
        $ renpy.pause()
        jump ch3ep3_victorcall
label ch3ep3_exercise:
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene ch3ep3_187 with fade
    angela "Finally, we've arrived here."
    angela "The weather is so nice today, isn't it?"
    mc "Yeah... The atmosphere feels so refreshing."
    zeke "*Pants* Guys... I can't... breathe."
    scene ch3ep3_188 with dissolve
    mc "What? You're exhausted already?"
    zeke "*Pants* Bro... It's been like years since the last time I exercised."
    zeke "*Pants* Moreover, I didn't.... expect us... to run this far...."
    mc "Well then, you better get used to it soon if you want to catch up."
    mc "We're just getting started."
    zeke "*Pants* I know, but... can I take some rest for a sec?"
    angela "Of course, you can. Take your time."
    zeke "*Pants* Thank you..."
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*.........."
    scene ch3ep3_189 with dissolve
    zeke "*Sighs* Phew...."
    mc "Are you better now?"
    zeke "Yeah. I feel better now."
    zeke "What are we going to do next?"
    scene ch3ep3_190 with dissolve
    mc "It's up to [angela]."
    mc "What is your exercise program for today?"
    angela "Well... I'm going to do squats, bicycle crunches, and push-ups for today."
    zeke "That sounds... difficult."
    mc "Alright, let's do it."
    angela "Sure."
    scene ch3ep3_191 with dissolve
    angela "Okay, guys. We'll start with squats."
    angela "We're going to do three sets of twenty squads."
    mc "Understood."
    angela "Are you guys ready?"
    zeke "... Yeah."
    angela "Alright then, let's get started."
    scene ch3ep3_192 with dissolve
    $ renpy.pause()
    scene ch3ep3_191 with dissolve
    angela "One...."
    mc "One..."
    scene ch3ep3_192 with dissolve
    $ renpy.pause()
    scene ch3ep3_191 with dissolve
    angela "That's two."
    scene ch3ep3_192 with dissolve
    $ renpy.pause()
    scene ch3ep3_191 with dissolve
    angela "Three...."
    zeke "Three...."
    scene black with dissolve
    $ renpy.pause()
    s "*About ten minutes later*........."
    scene ch3ep3_193 with dissolve
    angela "Okay, guys. We've finished squats now."
    zeke "*Laughs* It sounded so difficult at first, but it's actually a lot easier than I thought."
    zeke "*Laughs* I think I can do it all day!"
    mc "... Good for you."
    scene ch3ep3_194 with dissolve
    angela "It's good to see that you can catch up."
    angela "But, there are a lot more to come."
    angela "Next, we are going to do bicycle crunches in order to strengthen abdominal muscles."
    angela "Three sets, thirty reps per each, okay?"
    mc "Okay. Let's do it."
    scene black with dissolve
    scene ch3ep3_195 with dissolve
    angela "One."
    scene ch3ep3_196 with dissolve
    angela "Two."
    scene ch3ep3_195 with dissolve
    angela "Three."
    scene ch3ep3_196 with dissolve
    angela "Four."
    scene black with dissolve
    $ renpy.pause()
    s "*About ten minutes later*........."
    scene ch3ep3_197 with dissolve
    angela "Alright, now let's do push-ups."
    angela "Three sets. Twenty reps per each."
    zeke "Three sets. Twenty reps per each. Loud and clear!"
    mc "Let's get started."
    scene ch3ep3_198 with dissolve
    $ renpy.pause()
    scene ch3ep3_197 with dissolve
    angela "One."
    scene ch3ep3_198 with dissolve
    $ renpy.pause()
    scene ch3ep3_197 with dissolve
    mc "That's two..."
    angela "Yeah... Two."
    scene ch3ep3_198 with dissolve
    $ renpy.pause()
    scene ch3ep3_197 with dissolve
    angela "Three...."
    scene black with dissolve
    $ renpy.pause()
    s "*About ten minutes later*.........."
    scene ch3ep3_199 with dissolve
    angela "Well done, guys."
    angela "That's all for the exercise program today."
    mc "Hm? That's it?"
    angela "Yeah, why? Do you want more?"
    scene ch3ep3_200 with dissolve
    zeke "Hear me out, bro."
    mc "Hm?"
    zeke "How about we do some sparring?"
    zeke "Just you and me."
    mc "... Right now?"
    zeke "Yeah. Right now."
    scene ch3ep3_201 with dissolve
    mc "Why do you want to do that?"
    zeke "Because I want to get stronger. I want to be more useful."
    zeke "And I think I can learn a lot from sparring with you."
    mc "I have no problem with that."
    zeke "Great."
    angela "Alright then, I will go take a seat and watch you guys."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep.3/ep3_7.mp3" fadein 3.0
    $ bgm = "Jeff II - Heartfül of Kerøsene"
    scene ch3ep3_202 with dissolve
    zeke "... Are you ready?"
    mc "I think I should be the one asking that."
    mc "Come at me when you're ready."
    zeke "Alright then, let's get..."
    scene ch3ep3_203 with dissolve
    zeke "... Started!"
    mc ".................."
    zeke "I knew you were going to catch it."
    zeke "But, what about..."
    scene ch3ep3_204 with dissolve
    zeke "... This!"
    zeke "W-What...!?"
    scene ch3ep3_205 with vpunch
    zeke "Ouch...!!"
    mc "..............."
    scene ch3ep3_206 with dissolve
    zeke "You got me so easy."
    mc "..................."
    zeke "I prepared for this outcome, but it still hurt a bit when it happened."
    zeke "Am I really weak?"
    scene ch3ep3_207 with dissolve
    mc "You aren't weak, [zeke]."
    mc "You're just too easy to read."
    mc "I knew how you would attack just like reading a textbook."
    mc "You've got to make yourself unpredictable."
    zeke "... Is that so?"
    scene ch3ep3_208 with dissolve
    mc "Yeah... Let's try it."
    mc "Come on in."
    zeke "Okay."
    scene ch3ep3_209 with dissolve
    zeke "Then, how about this?!"
    mc "Hm? You're aiming for my lower leg?"
    scene ch3ep3_210 with flash
    zeke "Did you think so?!"
    mc "................."
    zeke "Oh? Now, you're blocking your body?"
    scene ch3ep3_211 with flash
    zeke "Got you!"
    mc "................"
    scene ch3ep3_212 with flash
    zeke "W-What the fuck??!!"
    zeke "H-How did you...?!"
    scene ch3ep3_213 with vpunch
    zeke "Ouch...!!"
    scene black with dissolve
    scene ch3ep3_214 with dissolve
    zeke "Again...!?"
    zeke "I did my best. I thought that kick was going to hit."
    zeke "But, you dodged it by tilting your neck back and leaning back for a bit."
    zeke "That was probably the best kick of my life, but you dodged it just like that."
    scene ch3ep3_215 with dissolve
    zeke "I always thought I was strong since when I was a high schooler."
    zeke "But I'm not even half as good as you."
    zeke "In fact, I can't even stand a chance against [seth]."
    zeke "I'm so weak right now."
    mc "................."
    scene ch3ep3_216 with dissolve
    mc "Yeah. You're so weak right now."
    mc "Did you really expect yourself to be strong without getting any practice?"
    mc "If you're just going to cry like a baby like that, then you can give up. I won't stop you."
    mc "I would surely be disappointed, but I won't blame you."
    scene ch3ep3_217 with dissolve
    zeke "................."
    mc "But, if you really wanted to be useful like you said...."
    mc "Then, stop whining. Get your ass up and come at me again."
    zeke "................"
    zeke "... You're right."
    scene black with dissolve
    scene ch3ep3_218 with dissolve
    zeke "I'm sorry. I was such an idiot."
    zeke "Let's do it again."
    mc "Great. That's what I wanted to see from you."
    mc "You did very well last time. That brazillian kick was almost perfect."
    zeke "Thanks... I saw you did it to [seth], so I tried to copy you."
    mc "That's not the thing anyone would be able to do. You've got a very good potential."
    mc "You were too slow because you hadn't been practicing for so long."
    mc "Come at me again."
    scene ch3ep3_219 with dissolve
    zeke "Okay...!"
    zeke "I'm going in...!!"
    mc "...................."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    s "*About fifteen minutes later*............"
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene ch3ep3_220 with dissolve
    zeke "*Pants* That's enough.... I'm... so exhausted... right now."
    mc "*Softly breahtes* Okay... Let's call it a day."
    zeke "*Pants* After so many.... attempts, I still.... failed to touch you...."
    scene ch3ep3_221 with dissolve
    mc "*Softly breathes* Well... You almost got me a couple times."
    mc "*Softly breathes* Just chin up. Don't look down on yourself."
    mc "*Softly breathes* You have a talent. You'll get stronger eventually."
    zeke "*Pants* Thanks... for... saying... that."
    scene ch3ep3_222 with dissolve
    angela "Oh? Have you guys done already?"
    zeke "*Pants* Yeah... I'm too tired to continue."
    mc "Where have you been?"
    scene ch3ep3_223 with dissolve
    angela "I thought you guys might be thirsty."
    angela "So, I went to get some water for you guys."
    mc "What about you by the way? I only see two bottles of water now."
    angela "Oh... I've already drunk mine."
    mc "I see.... Thank you so much."
    scene ch3ep3_224 with dissolve
    angela "Here is your bottle of water."
    zeke "*Pants* What a perfect timing..."
    zeke "*Pants* Thank you, [angela]. You're... the best."
    angela "*Giggles* You're welcome."
    scene black with dissolve
    $ renpy.pause()
    s "*About five minutes later*........"
    scene ch3ep3_225 with dissolve
    angela "Guys. It's half past seven now."
    angela "Shall we go home?"
    zeke "Sure. Let's go."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_226 with dissolve
    angela "Thank you for today, guys."
    mc "We should be the ones saying that."
    zeke "Yeah. He's right."
    scene ch3ep3_227 with dissolve
    mc "Alright, we're leaving now."
    mc "See you tomorrow."
    angela "Yeah. See you tomorrow."
    zeke "Good bye, [angela]."
    scene black with dissolve
    $ renpy.pause()
    s "*About five minutes later*.........."
    scene ch3ep3_228 with fade
    rin "Good morning, guys."
    zeke "Oh! Good morning, [rin]."
    mc "Good morning."
    rin "Have you just got back from exercising?"
    scene ch3ep3_229 with dissolve
    mc "Yeah. That's right."
    mc "Where are you going by the way?"
    rin "I'm going to go take a shower."
    rin "I just finished preparing breakfast."
    scene ch3ep3_230 with dissolve
    rin "Oh! To talk about that, your breakfast are on the table, guys."
    mc "Really? Thank you so much."
    zeke "You're the best, [rin]"
    mc "I'm going to go take a shower first. Then, I'll go eat it."
    rin "I get it. See you again soon then."
    mc "Yeah. See you soon."
    scene black with dissolve
    scene ch3ep3_231 with dissolve
    u "*Sniffs*........"
    u "I'm so stinky now."
    u "Let's take a shower and get changed."
    stop music fadeout 3.0
    jump ch3ep3_victorcall
label ch3ep3_victorcall:
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep4_5.mp3" fadein 3.0
    $ bgm = "RYYZN - Waited (instrumental)"
    scene ch3ep3_232 with dissolve
    u "Okay, I'm ready now."
    u "Let's go to work...."
    scene ch3ep3_233 with dissolve
    s "*Phone vibrates*................."
    u "Hm...?"
    u "Who's calling me now?"
    scene ch3ep3_234 with dissolve
    u "Oh... It's [victor]."
    u "I wonder why he's calling me this early."
    u "Let's find it out."
    scene ch3ep3_235 with dissolve
    mc "Good morning, sir."
    mc "How may I help you?"
    scene ch3ep3_238 with fade
    victor "Good morning, [mc]."
    victor "How are you doing?"
    scene ch3ep3_235 with dissolve
    mc "I'm feeling good, sir."
    mc "What about you?"
    scene ch3ep3_238 with dissolve
    victor "Great. I feel very satisfied now."
    victor "Actually, I've been feeling satisfied since last night."
    scene ch3ep3_239 with dissolve
    victor "Thank to you. Our drug transport was successful."
    victor "You did a very great job."
    scene ch3ep3_235 with dissolve
    mc "Anytime, sir."
    mc "I'm happy that I was helpful."
    scene ch3ep3_239 with dissolve
    victor "I'm going to give you a reward for your useful information."
    victor "How much do you want? One hundred thousand dollars?"
    scene ch3ep3_236 with dissolve
    mc "... It's okay, sir."
    mc "You don't have to give me anything."
    mc "I just did my job."
    scene ch3ep3_239 with dissolve
    victor "..................."
    victor "... Are you sure?"
    scene ch3ep3_236 with dissolve
    mc "Yes, sir."
    scene ch3ep3_239 with dissolve
    victor "Alright then, if you say so."
    scene ch3ep3_240 with dissolve
    victor "By the way, is it going to be alright over there?"
    victor "I mean... The police might suspect you."
    victor "Since their plan ended up failing right after he told you the information..."
    scene ch3ep3_235 with dissolve
    mc "Don't worry about that."
    mc "It's not like this is the first time they fail to do so."
    mc "I don't think they will immediately suspect me."
    mc "But still, I think I should lie low for a little bit."
    mc "So, I won't be able to report you anything good for some amount of time."
    scene ch3ep3_239 with dissolve
    victor "I see.... It's understandable."
    victor "Then, you don't have to report me everything you hear from them."
    victor "Just report me when it's a very crucial information."
    scene ch3ep3_236 with dissolve
    mc "I get it."
    mc "Good bye, sir."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_234 with vpunch
    play music "sfx/ch2ep1_2.mp3" fadein 3.0
    $ bgm = "Tokyo Music Walker - Your Little Wings"
    s "*Phone vibrates*.........."
    u "Hm...? I've got a new email?"
    u "It's from Xecon... They told me to attend a conference at nine."
    scene ch3ep3_237 with dissolve
    u "Alright then...."
    u "Let's go have breakfast. Thenm go to work."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_241 with fade
    mc "Hm....?"
    mc "Where are you going, [yui]?"
    yui "... Huh?"
    scene ch3ep3_242 with dissolve
    yui "What do you mean?"
    yui "Of course I'm going to our department to work."
    yui "Where else could I go?"
    mc "... Didn't you get a new email from the company?"
    scene ch3ep3_243 with dissolve
    yui "... What email?"
    mc "It's an email that tells you to attend the conference today."
    yui "No. I haven't got it."
    yui "I checked my inbox in the morning, but I didn't see one."
    mc "I see...."
    scene ch3ep3_244 with dissolve
    yui "Perhaps they only sent it high position employees?"
    mc "Yeah, it could be... Wait..."
    mc "Then, why did I get it?"
    yui "You're an exceptional? I don't know."
    yui "Just go ahead. Attend the conference and tell me what's it all about."
    mc "Alright. See you later then."
    yui "Okay. See you later."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_245 with fade
    rowan "Oh, there you are."
    rowan "We've been waiting for you."
    mc "My apologies. I'm late."
    scene ch3ep3_246 with dissolve
    rowan "It's okay. It's only been three minutes."
    rowan "Come. Take a seat."
    mc "Understood."
    scene ch3ep3_247 with dissolve
    sally "*Smiles* Good morning, [mc]."
    mc "Good morning, [sally]."
    sally "I didn't expect to see you here."
    mc "I didn't expect myself to be here as well."
    mc "What is this meeting about? Any idea?"
    sally "I don't know either. I guess we'll find out soon."
    scene ch3ep3_245_1 with dissolve
    rowan "Alright, since everyone is already here."
    rowan "Shall we start now?"
    pete "As you wish."
    rowan "Well..."
    scene ch3ep3_246_1 with dissolve
    rowan "I summon all of you here because I wanted to about our project's development."
    rowan "How much have you guys been progressing, [pete]?"
    pete "Well... The game is in the very final stage of development now."
    pete "We've fixed all the bugs we got reported from the game-tester department."
    rowan "I see..."
    scene ch3ep3_247_1 with dissolve
    rowan "What about you, [sally]?"
    sally "Just like [pete] said earlier, I reported all the bugs I found to the development department."
    rowan "Have you found any more bugs in the game?"
    sally "No. I haven't found any more bugs so far."
    rowan "Good to hear that."
    scene ch3ep3_248 with dissolve
    rowan "And you, [wendy]?"
    wendy "Yes, sir?"
    rowan "What about the in-game languages?"
    rowan "Have you finished checking them?"
    scene ch3ep3_249 with dissolve
    wendy "Not yet, sir."
    wendy "But, it's almost finished. It's at about ninety percent of the process."
    rowan "I see..."
    rowan "How long will it take you to finish?"
    wendy "I think it will take me around two weeks."
    rowan "I get it."
    scene ch3ep3_250 with dissolve
    rowan "It's been so long since the first day we started developing this project."
    rowan "Finally, our dream is about to come true."
    rowan "You all have been working hard for me. I appreciate that a lot."
    rowan "I know how hard each of process is..."
    scene ch3ep3_251 with dissolve
    rowan "I didn't want to rush you guys, but due to some circumstances, I have no choice but to bring forward the launch day."
    rowan "I'm so sorry."
    scene ch3ep3_252 with dissolve
    pete "Don't be sorry."
    pete "If you bring forward the launch day, there must be a reason for that."
    rowan "Thank you for your understanding, [pete]."
    rowan "Can you and your team finish everything within a week?"
    pete "Sure. We'll try our best."
    scene ch3ep3_253 with dissolve
    rowan "And you, [wendy]."
    rowan "I'm sorry to ask, but can you make it a week faster?"
    wendy "Of course. I'll do that for you."
    rowan "Thank you."
    scene ch3ep3_254 with dissolve
    rowan "[faye]."
    faye "At your service."
    rowan "Find a good launch date. Contact the media and our major investors."
    rowan "Tell them to attend the event."
    faye "Understood."
    scene ch3ep3_255 with dissolve
    rowan "[eira]."
    eira "Yes?"
    rowan "Can you make a marketing plan to promote the opening event?"
    rowan "Also a marketing plan to promote Xecon Gear right after the event ended."
    scene ch3ep3_256 with dissolve
    eira "I get it."
    eira "I will send them to you to check when they're finished."
    rowan "That'd be great. Thank you."
    if nominatekrystal == 1:
        scene ch3ep3_257_k1 with dissolve
        rowan "[mc]."
        mc "Yes?"
        rowan "You were the one who invited [krystal] to be the model for Xecon Gear, right?"
        mc "Yes. That's right."
        scene ch3ep3_257_k2 with dissolve
        rowan "Then, can you invite her to attend the lauch event?"
        rowan "We'll need her as an influencer... probably as an MC as well."
        mc "Sure. I'll inform her about that."
        rowan "Perfect...."
        scene black with dissolve
        $ renpy.pause()
    else:
        scene black with dissolve
        $ renpy.pause()
    scene ch3ep3_258 with dissolve
    rowan "Alright, that's all for today."
    rowan "Thank you everyone for joining."
    rowan "Hang in there for a little more. Our long journey is about to end."
    rowan "I'll make sure that I'll give a very good reward to everyone in the company."
    sally "*Giggles* Wow! I can't wait!"
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_259 with dissolve
    u "Alright... everyone has already left."
    u "Let's just leave here and go back to my department."
    s "*Phone vibrates*............"
    u "Hm...?"
    scene ch3ep3_260 with dissolve
    u "Oh... It's a call phone from [felix]."
    u "I wonder what he is going to say."
    u "It will probably be about last night I guess."
    u "Let's hear him out."
    scene ch3ep3_261 with dissolve
    mc "Hello, [felix]."
    mc "Is everything alright?"
    scene ch3ep3_265 with fade
    felix "The drug transport ship really changed its destination last night."
    felix "It was quite a big gamble to be honest."
    felix "I hope you gained more trust from [victor]."
    scene ch3ep3_261 with dissolve
    mc "Don't worry. I think he trusts me more than ever now."
    scene ch3ep3_266 with dissolve
    felix "I hope so."
    felix "By the way, that's not the main reason why I call you."
    felix "I've got the information about the old man you asked me to dig his background."
    felix "I thought You might want to know."
    scene ch3ep3_262 with dissolve
    mc "Really?"
    mc "Where are you right now?"
    scene ch3ep3_265 with dissolve
    felix "I'm at the police station, why?"
    scene ch3ep3_262 with dissolve
    mc "The police station in the city, right?"
    mc "Okay. I'm going to go there now."
    scene ch3ep3_267 with dissolve
    felix "Huh? Wouldn't that be too risky?"
    felix "Even though I got rid of a lot of [victor]'s police, I'm unsure if some are still left."
    scene ch3ep3_263 with dissolve
    mc "Don't be too worried."
    mc "[victor] thinks I pretend to be friends with [tom]."
    mc "Friends coming to see each other is normal, isn't it?"
    scene ch3ep3_267 with dissolve
    felix "... Yes, it is."
    felix "Okay then, see you again soon."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_264 with dissolve
    u "Alright..."
    u "Let's go to the police station."
    u "I want to hear everything about that old man in person."
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep.3/ep3_9.mp3" fadein 3.0
    $ bgm = "Atch - Freedom"
    scene ch3ep3_268 with fade
    felix "Hey."
    mc "Hi."
    felix "Welcome to my work place."
    scene ch3ep3_269 with dissolve
    mc "So, what is the information about the old man?"
    felix "Chill out, dude."
    felix "Follow me and get inside first."
    mc "Fine..."
    scene ch3ep3_270 with dissolve
    tom "([mc]...?)"
    mc ".................."
    scene ch3ep3_271 with dissolve
    tom "(What are you doing here?)"
    tom "(Why are you with [rowan]?)"
    tom "(I want to ask him so bad, but I think it's not the right time.)"
    tom "(I guess I'll have to wait until they're done talking.)"
    scene ch3ep3_272 with dissolve
    felix "Alright...."
    felix "Take a seat first."
    mc "Okay."
    scene ch3ep3_273 with dissolve
    felix "Here is the information about the old man."
    felix "That's all I've found for now."
    felix "Take a look at it."
    mc "Thank you."
    scene ch3ep3_274 with dissolve
    felix "His name is [westley]. You already knew that."
    felix "He was the owner of E&E Company, or the full name Elite and Elegance, which was a clothing company."
    felix "The company shut down five years ago. However, that's not the main focus."
    felix "The interesting thing is that E&E was the company to which your father was flamed for leaking the company project's information."
    scene ch3ep3_275 with dissolve
    felix "His company wasn't in a very good stage until they announced their new clothing collection."
    felix "Yeah... That's the project they stole from the company your father worked for."
    felix "That collection was like the resurrection of E&E which made the company became very successful for almost ten years."
    felix "Of course they were sued for that, but guess what?"
    scene ch3ep3_276 with dissolve
    felix "They won the case after the trial."
    mc "How come?"
    felix "It turned out that the company your father worked for, didn't have any evidence to prove that the design of the collection was their."
    mc "How was that even possible?"
    felix "Maybe it was destroyed. Who knows?"
    scene ch3ep3_277 with dissolve
    mc "So, that means he was actually the one who sent the scapegoat to kill my father?"
    mc "Yeah. That must be him."
    mc "I heard him saying that he gave a lot of money to that scapegoat."
    mc "My father must have had been gotten so close to proving himself unguilty."
    scene ch3ep3_278 with dissolve
    mc "That's why they killed him."
    felix "You're probably right. Both him and [victor] might worked together to kill your father."
    felix "However, we don't have any decent evidence yet."
    scene ch3ep3_279 with dissolve
    felix "But, don't worry. I won't stop investigating until I can put them both to jail."
    felix "I will do anything I can to bring your father justice."
    felix "Even if it's too many years late..."
    mc "...................."
    scene ch3ep3_280 with dissolve
    mc "... Thank you so much."
    mc "I owe you one."
    felix "It's not a big deal. We're just helping each other."
    mc "By the way, may I ask you something?"
    scene ch3ep3_281 with dissolve
    felix "Sure. What do you want to ask?"
    mc "Have you ever held a grudge against [victor] before?"
    mc "Did he do something bad to you in the past?"
    felix "I'm sorry to disappoint you. I have no particular feelings towards him."
    scene ch3ep3_282 with dissolve
    mc "Then, why are you trying so hard to arrest him?"
    felix "Actually I received an order from an influential person to put him to jail."
    mc "An influential person?"
    felix "Yes, but in a good way of course."
    mc "I see..."
    scene ch3ep3_281 with dissolve
    felix "Plus, it's the duty of the police to put criminals in prison, isn't it?"
    felix "What else should the police do?"
    mc "... Well, you're right."
    scene ch3ep3_283 with dissolve
    felix "Alright, I think that's it for today."
    felix "Thank you for coming."
    mc "I should be the one thanking you."
    felix "Come. I'll walk you to the exit."
    mc "Okay, sure."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_284 with dissolve
    tom "Hey, [mc]."
    mc "... [tom]."
    felix "Oh..."
    scene ch3ep3_285 with dissolve
    felix "I almost forgot."
    felix "You know each other, right?"
    tom "That's right, sir."
    scene ch3ep3_286 with dissolve
    felix "Seems like your friend wants to talk to you, [mc]."
    mc "Yeah..."
    felix "Alright then, I'll leave you guys alone so that you can t-"
    s "*Door hardly opened*........."
    play music "sfx/ep.3/ep3_7.mp3" fadein 3.0
    $ bgm = "Jeff II - Heartfül of Kerøsene"
    scene ch3ep3_287 with dissolve
    kole "Who the hell is [felix]!?"
    kole "Where the hell is he?!"
    felix "Hm...?"
    scene ch3ep3_288 with dissolve
    mc "It looks like you've got a problem, [felix]."
    kole "Oh?! There you are!"
    tom "Do you need help, sir."
    felix "You guys can go hang out together. Don't mind me."
    felix "I'll deal with him myself."
    scene ch3ep3_289 with dissolve
    felix "Yes, I'm [felix]."
    felix "What business do you have with me?"
    kole "Do you have any fucking idea who you've been messing with?!"
    felix "Yes, I completely do. If you want to talk about that, then follow me."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    s "[felix] and [kole] has left....."
    play music "sfx/ep.3/ep3_11.mp3" fadein 3.0
    $ bgm = "Day7 - Journey Home"
    scene ch3ep3_290 with dissolve
    tom "Err...."
    tom "Shall we take a seat?"
    mc "Why?"
    tom "I have a lot of questions I want to ask you. Do you have some spare time?"
    mc "... Okay."
    scene black with dissolve
    scene ch3ep3_291 with dissolve
    mc "Alright.... what do you want to ask me about?"
    tom "Ummm... How should I start?"
    tom "Since when did you know [felix]?"
    tom "Why did you come here?"
    scene ch3ep3_292 with dissolve
    mc "I met him not so long ago."
    mc "We made a deal since then."
    tom "Hm? A deal? What deal?"
    mc "I'll help him arrest [victor], and he will let me free in exchange."
    tom "Wait... What? What are you talking about?"
    tom "I'm so confused right now. Why do you have to help him arrest [victor]?"
    scene ch3ep3_293 with dissolve
    tom "I thought you had nothing to do with him."
    mc "*Sighs* Alright... I'll tell you everything now. Listen carefully."
    tom "Wait. That doesn't sound so good. Give me a second."
    mc "Okay. Tell me when you're ready."
    tom "...................."
    tom "... Okay. I'm ready to listen now."
    mc "I actually didn't get kicked out like I told you before."
    tom "Wait... What?"
    mc "I'd always been working for [victor] until..."
    scene black with dissolve
    $ renpy.pause()
    s "You spent your time telling [tom] everything....."
    scene ch3ep3_294 with dissolve
    tom "Damn... bro."
    tom "I'm so sorry to hear that."
    mc "Yeah... That's why I'm here today. I'm trying to investigate my father's death."
    tom "You could make a movie about your life. Seriously."
    scene ch3ep3_295 with dissolve
    mc "I'm sorry that I lied to you."
    tom "It's alright, bro."
    tom "At first I was a bit angry, but after hearing everything...."
    tom "I'd have done the same if I were you."
    mc "Thank you for saying that."
    scene ch3ep3_296 with dissolve
    mc "Okay... I think I should leave now."
    tom "Oh, sure. Sorry for taking you time for so long."
    mc "No problem. It was a very good talk."
    mc "See you again soon."
    tom "Sure, bro. Bye."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_297 with fade
    play music "sfx/Nextday.mp3" fadein 4.0
    $ bgm = "Bensound - Perception"
    u "It's almost lunch time now."
    u "I'm also getting hungry."
    u "Let's stop by a restaurant, or a cafe and find something to eat before going back to the company."
    scene black with dissolve
    scene ch3ep3_298 with dissolve
    cg "Welcome to Cafe 69, sir."
    cg "How may I help you?"
    scene black with dissolve
    $ renpy.pause()
    s "You spent your time having lunch, then came back to the company...."
    scene ch3ep3_299 with dissolve
    u "Alright, I'm back here..."
    u "I've been outside for so long to be honest."
    u "Let's just go back to the department and finish my work."
    scene black with dissolve
    $ renpy.pause()
    s "Later that evening..........."
    scene ch3ep3_300 with fade
    u "It's been such a long day."
    u "I'm so tired now."
    if nominatekrystal == 1:
        u "I also have to inform [krystal] about the launch date."
    u "Let's just go take a shower first before doing anything..."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_301 with dissolve
    u "Alright, I feel much better now."
    u "Let's go find something to eat."
    if nominatekrystal == 1:
        u "Oh... I almost forgot."
        u "I have to go see [krystal] first."
        jump ch3ep3_inkrystal
    else:
        jump ch3ep3_felixcall
label ch3ep3_inkrystal:
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_302 with dissolve
    s "*Knocks*..............."
    mc "[krystal]...."
    krystal "Yesss?! [mc]?!"
    mc "Yes, it's me."
    mc "May I come in?"
    krystal "Sure. Come on in."
    scene black with dissolve
    scene ch3ep3_303 with dissolve
    mc "Hi, [krystal]."
    krystal "Good evening, [mc]."
    mc "I have something to tell you."
    scene ch3ep3_304 with dissolve
    krystal "Yeah? What's it?"
    mc "May I take a seat?"
    krystal "Sure. Come. Sit right next to me."
    mc "Thank you."
    scene ch3ep3_305 with dissolve
    mc "To think about it..."
    mc "This is my first time I come to your room after we moved here, right?"
    krystal "Oh, yeah. That's right."
    mc "It looks nice, but..."
    scene ch3ep3_306 with dissolve
    mc "Isn't it a bit too small?"
    krystal "Really? I like it a lot though."
    mc "Good for you then."
    krystal "So, what's it that you want to tell me?"
    mc "Xecon is going to announce Xecon Gear to public soon."
    mc "[rowan] told me invite you to the launch date."
    scene ch3ep3_307 with dissolve
    krystal "... Huh? When?"
    mc "The date has yet to be decided, but it will probably be next week.."
    mc "He wanted you to show up at the event as an influencer of the game."
    mc "You will probably be an MC as well."
    krystal "................."
    scene ch3ep3_308 with dissolve
    mc "... What's wrong?"
    krystal "I don't know..."
    krystal "I thought I became more confident now, but to hear that I'll have to participate in such a big event."
    krystal "Also, playing such a big role. I feel unconfident."
    mc "Calm down. Don't be too afraid."
    scene ch3ep3_307 with dissolve
    mc "Just be yourself and it will be alright."
    krystal "... Really?"
    mc "Yeah. Don't you believe me?"
    krystal "Yes, I do."
    mc "Good..."
    scene ch3ep3_309 with dissolve
    mc "By the way, have you bought a guitar?"
    mc "This is the first time I've seen you have one."
    krystal "Oh? That guitar?"
    krystal "Yeah, I just bought it a couple days ago."
    scene ch3ep3_310 with dissolve
    mc "I see... I know that you're good at dancing and singing, but I never knew you could play a guitar."
    krystal "I found it while I was surfing the internet."
    krystal "I reminded me of the old days. I used to have one like that."
    krystal "That's why I decided to buy it, but I still haven't played it yet."
    mc "Then, can you play a song for me, please?"
    scene ch3ep3_308 with dissolve
    krystal "... Are you sure?"
    mc "Yes, I am."
    krystal "I mean... I might not be as good as you expected."
    mc "................"
    krystal "... Okay. If you say so."
    scene black with dissolve
    scene ch3ep3_311 with dissolve
    krystal "It's been so long since the last time I played."
    krystal "Don't set your hopes too high, okay?"
    mc "Okay."
    krystal "What song do you want me to play?"
    mc "Up to you. Choose one."
    krystal "Alright, I'll play Consequences by Camila Cabello then."
    krystal "It's one of my favorite songs."
    mc "Sure. Go ahead."
    scene ch3ep3_312 with dissolve
    krystal "Dirty tissues, trust isses~"
    krystal "Glasses on the sink, they didn't fix you~"
    krystal "Lonely pillows in a strangers bed, little voices in my head~"
    scene black with dissolve
    $ renpy.pause()
    s "You listened to [krystal] singing until she finished...."
    scene ch3ep3_313 with dissolve
    krystal "That's it...."
    mc "..............."
    krystal "*Giggles* What...? Say something."
    menu:
        "You have a beautiful voice [krystal2]":
            $ ch3ep3krystalsing = 1
            $ krystal_relationship += 2
            $ krystal_ch3_ep3 += 2
            scene ch3ep3_314_a with dissolve
            mc "Brilliant...."
            mc "You have such a beautiful voice, [krystal]."
            krystal "*Smiles* Really? Thank you."
            krystal "*Smiles* I'm glad you liked it."
        "Not bad":
            $ ch3ep3krystalsing = 2
            scene ch3ep3_314_b with dissolve
            mc "Well..."
            mc "Some notes were a bit off-key, but it's not bad overall."
            krystal "Yeah... It must be that I haven't been singing for so long."
            krystal "I guess I'll have to practice harder."
    scene ch3ep3_315 with dissolve
    mc "Alright... I think I should leave now."
    krystal "Hm? Already?"
    mc "Yeah. It's been half an hour already."
    scene ch3ep3_316 with dissolve
    mc "Moreover, I'm hungry now."
    mc "I'm going to go have dinner."
    krystal "Oh, I haven't had dinner yet as well."
    krystal "Let's go together then."
    mc "Okay, sure."
    stop music fadeout 3.0
    jump ch3ep3_felixcall
label ch3ep3_felixcall:
    scene black with dissolve
    $ renpy.pause()
    s "Later that night........"
    play music "sfx/ep4_1.mp3" fadein 3.0
    $ bgm = "Sapajou - Intención"
    scene ch3ep3_317 with fade
    u "Alright, it's getting late now."
    u "I'm starting to feel sleepy."
    u "Let's go back to my room and sleep."
    scene black with dissolve
    scene ch3ep3_318 with dissolve
    s "*Phone vibrates*.............."
    u "Hm...?"
    u "Who's calling me at night like this?"
    scene ch3ep3_319 with dissolve
    u "Oh... It's [felix]."
    u "I wonder what makes him call me now."
    u "Let's hear him out."
    scene ch3ep3_320 with dissolve
    mc "Hello...."
    scene ch3ep3_323 with fade
    felix "Sorry for calling you at night like this."
    felix "Did I wake you up?"
    scene ch3ep3_320 with dissolve
    mc "No, you didn't."
    mc "What's happening?"
    scene ch3ep3_323 with dissolve
    felix "I just finished talking to him, the scapegoat."
    scene ch3ep3_321 with dissolve
    mc "Yeah? What did you guys talk about?"
    scene ch3ep3_324 with dissolve
    felix "I asked him about [westley]."
    felix "He seemed shocked when I said the old man's name."
    felix "But, he eventually admitted that he received money from the old man for killing your father."
    scene ch3ep3_321 with dissolve
    mc "... Does he have any evidence to proof that?"
    scene ch3ep3_323 with dissolve
    felix "No, he doesn't."
    felix "We can take a look at his account statement."
    scene ch3ep3_324 with dissolve
    felix "However, I don't think [westley] used his own account to transfer money."
    scene ch3ep3_321 with dissolve
    mc "Yeah, I think so."
    scene ch3ep3_325 with dissolve
    felix "So, I'm going to dig deep for more information."
    felix "I'm going to start with the account that was used to transfer money to the scapegoat."
    felix "Then, I'll find out who the owner of the account is."
    felix "It might point to [westley] in the end."
    scene ch3ep3_322 with dissolve
    mc "Thank you. I'm counting on you."
    mc "Call me if you need any help."
    mc "Bye."
    scene black with dissolve
    stop music fadeout 3.0
    scene ch3ep3_326 with dissolve
    u "Okay..."
    u "I guess that's it for today."
    u "Let's go to bed."
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    s "Next morning.........."
    scene ch3ep3_327 with dissolve
    u "Umm... It's already morning?"
    u "..................."
    u "... Well. Let's get up and go take a shower."
    u "Then, I'll find something to eat before going to work."
    scene black with dissolve
    $ renpy.pause()
    if ch2ep2suggestalice == 1:
        jump ch3ep3_meetalice
    else:
        s "You spent the whole day working........."
        jump ch3ep3_gohome
label ch3ep3_meetalice:
    play music "sfx/ch2ep1_1.mp3" fadein 3.0
    $ bgm = "Roa - Winter Magic"
    scene ch3ep3_328 with fade
    u "Hm...?"
    u "Isn't that [alice]."
    u "What is she doing here?"
    u "Let's approach her."
    scene ch3ep3_329 with dissolve
    mc "Good morning, [alice]."
    alice "Huh? Oh! Hi, [mc]!"
    mc "it's been a while."
    mc "How are you doing?"
    scene ch3ep3_330 with dissolve
    alice "Yeah... It's been a while."
    alice "I'm doing great. Thank you for asking."
    alice "What about you? Everything's alright?"
    mc "Yeah."
    scene ch3ep3_331 with dissolve
    mc "By the way, what are you doing here?"
    alice "I come here to see [faye]."
    alice "We're going to talk about the feedback of the game background music."
    mc "I see. I hope you get a good feedback."
    alice "*Smiles* Thanks."
    scene ch3ep3_332 at eyesblink("Ch.3/Ep.3/Scenes/ch3ep3_332.jpg", "Ch.3/Ep.3/Scenes/ch3ep3_332_blink.jpg", 1) with dissolve
    alice "[mc]."
    mc "... Yeah?"
    alice "I think I'm going to finish around lunch time."
    alice "Do you want to go have lunch with me today?"
    menu:
        "Sure. Why not? [alice1]":
            $ ch3ep3alicelunch = 1
            $ alice_relationship += 1
            $ alice_ch3_ep3 += 1
            scene ch3ep3_333 at eyesblink("Ch.3/Ep.3/Scenes/ch3ep3_333.jpg", "Ch.3/Ep.3/Scenes/ch3ep3_333_blink.jpg", 1) with dissolve
            mc "Sure. Why not?"
            alice "Really? You said it, okay?"
            mc "Yeah. Where are we going to meet up by the way?"
            alice "I'll be waiting for you here when I'm done."
            mc "Okay. I get it."
        "I'm sorry, but...":
            $ ch3ep3alicelunch = 2
            scene ch3ep3_334 at eyesblink("Ch.3/Ep.3/Scenes/ch3ep3_334.jpg", "Ch.3/Ep.3/Scenes/ch3ep3_334_blink.jpg", 1) with dissolve
            mc "I'm sorry, but..."
            mc "I've already had an appointment."
            u "Actually, I just feel like having lunch alone today..."
            alice "Oh... Is that so?"
            mc "Yeah..."
            alice "What a pity..."
            mc "May be next time, okay?"
            alice "Okay."
    scene ch3ep3_335 with dissolve
    s "*Elevator sounds*............"
    mc "Oh... The elevator has come."
    mc "Let's go, [alice]."
    alice "Sure. Let's go."
    scene black with dissolve
    $ renpy.pause()
    s "*About three hours later*.........."
    scene ch3ep3_336 with dissolve
    u "It's already lunch time."
    u "Let's go find something to eat."
    if ch3ep3alicelunch == 1:
        u "What shoud I eat though...?"
        scene ch3ep3_337 with dissolve
        alice "Over here, [mc]!"
        u "Oh... I almost forgot."
        u "I agreed to have lunch with [alice] today."
        scene ch3ep3_338 with dissolve
        mc "Sorry that I kept you waiting."
        alice "Don't be."
        alice "I haven't been waiting that long."
        alice "I've just got here as well."
        scene ch3ep3_339 with dissolve
        mc "I see..."
        mc "How was the talk with [faye] by the way?"
        alice "Brilliant. The feedback was a lot better than I expected."
        alice "There's only a few things I have to fix."
        mc "Is that so? I'm happy for you."
        alice "Thanks!"
        scene ch3ep3_340 with dissolve
        alice "By the way, what are we going to eat today?"
        mc "I don't know. What do you think?"
        alice "Ummm... Any idea?"
        mc "... Well, how about we eat something easy and quick?"
        scene ch3ep3_338 with dissolve
        alice "Like what? Burger Queen?"
        mc "Oh, yeah. Burger Queen sounds good to me."
        alice "Alright then, Burger Queen it is. Shall we go now?"
        mc "Sure. Let's go."
        scene black with dissolve
        $ renpy.pause()
        jump ch3ep3_lunchwithalice
    else:
        u "What should I eat though...?"
        u "... Well, let's eat something easy and quick."
        u "Let's go eat Burger Queen then."
        scene black with dissolve
        $ renpy.pause()
        jump ch3ep3_gohome
label ch3ep3_lunchwithalice:
    scene black with dissolve
    s "You spent time having lunch with [alice]..."
    scene ch3ep3_341 with fade
    alice "I'm full now. What about you?"
    mc "Yeah. Me, too."
    alice "Okay then, shall we leave now?"
    mc "Okay."
    scene black with dissolve
    scene ch3ep3_342 with dissolve
    alice "Thank you for having lunch with me today."
    alice "I enjoyed spending time with you a lot."
    mc "So do I."
    alice "Alright then, I'm going to leave now."
    if ch2ep1answeralice == 1:
        menu:
            "Can I walk you home? [alice1]":
                $ ch3ep3walkalicehome = 1
                $ alice_relationship += 1
                $ alice_ch3_ep3 += 1
                scene ch3ep3_343_a with dissolve
                mc "Can I take you home?"
                alice "Huh?!"
                mc "... Did I say something wrong?"
                alice "*Smiles* No, you didn't. I just didn't expect to hear that from you."
                alice "*Smiles* Of course, you can! If that's what you want."
                mc "Then, shall we go now?"
                alice "*Smiles* Sure. Let's go!"
                scene black with dissolve
                $ renpy.pause()
                scene ch3ep3_344 with fade
                alice "Okay... We've arrived."
                alice "Get inside first."
                mc "... Isn't this a new room?"
                mc "I remembered the last time I helped you moved. You room didn't look like this."
                scene ch3ep3_345 with dissolve
                alice "Oh? You noticed it?"
                alice "There was a little bit problem with that room, so I changed to this room."
                mc "Yeah? Since when?"
                alice "Ummm... About two weeks ago I guess."
                scene ch3ep3_346 with dissolve
                mc "Why didn't you tell me about that?"
                mc "I could've helped you moved again."
                alice "You had been busy recently, so I didn't want to trouble you."
                mc "I see... Your new room looks nice by the way."
                alice "*Smiles* Thank you."
                scene ch3ep3_347 with dissolve
                mc "Where is [kitty]? I haven't seen her here."
                mc "Is she... alright, right?"
                alice "Yeah, she's alright. She just has a fever."
                alice "She's at a clinic right now. I'll pick her up by tomorrow."
                scene ch3ep3_348 with dissolve
                mc "I see... I wish she gets better soon."
                alice "Thank you."
                mc "Alright then, since there's nothing to do here, I'm going to leave now."
                alice "Hm? Are you leaving now?"
                scene ch3ep3_349 with dissolve
                mc "Yeah..."
                alice "Do you want to have a cup of tea before leaving?"
                alice "I'll go make it for you."
                mc "Thank you, but... I'm not thirsty now."
                scene ch3ep3_350 with dissolve
                alice "Really? Don't you want to drink anything at all?"
                mc "... No, I don't. Thank you."
                alice "It's kinda hot in here...."
                scene black with dissolve
                scene ch3ep3_351 with dissolve
                alice "Don't you think so?"
                mc "................."
                alice "Are you really going to leave?"
                alice "After seeing this, hm...?"
                menu:
                    "Kiss her [alice2]":
                        stop music fadeout 3.0
                        $ ch3ep3kissalice = 1
                        $ alice_relationship += 2
                        $ alice_ch3_ep3 += 2
                        jump ch3ep3_alicesex
                    "Yeah. Good bye.":
                        $ ch3ep3kissalice = 2
                        scene ch3ep3_352_d with dissolve
                        mc "Yeah. I'm going to leave now."
                        mc "I have to go back to work. Sorry."
                        alice "Jeez... Okay."
                        mc "See you later."
                        alice "Okay. Good bye."
                        scene black with dissolve
                        $ renpy.pause()
                        jump ch3ep3_gohome
            "Good bye, [alice].":
                $ ch3ep3walkalicehome = 2
                scene ch3ep3_343_b1 with dissolve
                mc "Good bye, [alice]."
                alice "Good bye, [mc]. See you later."
                mc "Yeah... Get home safe."
                alice "Got it."
                scene black with dissolve
                $ renpy.pause()
                scene ch3ep3_343_b2 with dissolve
                u "Alright, [alice] has already left."
                u "I should leave here as well."
                u "Let's go back to the company."
                scene black with dissolve
                $ renpy.pause()
                jump ch3ep3_gohome
    else:
        scene ch3ep3_343_b1 with dissolve
        mc "Good bye, [alice]."
        alice "Good bye, [mc]. See you later."
        mc "Yeah... Get home safe."
        alice "Got it."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep3_343_b2 with dissolve
        u "Alright, [alice] has already left."
        u "I should leave here as well."
        u "Let's go back to the company."
        scene black with dissolve
        $ renpy.pause()
        jump ch3ep3_gohome
label ch3ep3_alicesex:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    play music "sfx/ep4_4.mp3" fadein 3.0
    $ bgm = "Le Gang - Bad Intentions"
    scene ch3ep3_352 with dissolve
    alice "*Kisses* Uhh...?!"
    mc "*Kisses*.............."
    scene ch3ep3_353 with dissolve
    alice "*Giggles* Hehe... Aren't you going to leave now?"
    mc "I've changed my mind."
    alice "*Giggles* Okay. Let's continue on the bed then."
    mc "Sure..."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_354 with dissolve
    mc "*Kisses* Put your tongue out."
    alice "*Kisses* Mhmm... Like this...?"
    mc "*Kisses* Yeah..."
    scene ch3ep3_355 with dissolve
    alice "Hmm...? Why did you stop?"
    mc "Take your clothes off."
    alice "Okay. You take your clothes off, too."
    mc "Of course."
    scene black with dissolve
    scene ch3ep3_356 with dissolve
    alice "*Giggles* Hello, little [mc]."
    alice "*Giggles* It's been a while since the last time we met."
    mc "Do you miss him?"
    alice "*Giggles* Yes, I do."
    mc "Alright then, talk to him as much as you want."
    alice "*Giggles* Okay!"
    scene ch3ep3_357 with dissolve
    show ch3ep3_alice1
    window hide
    alice "*Sucks* Mhmmm... [mc]..."
    mc "... Yeah?"
    alice "*Sucks* Mhmmm... Do you like the way I'm talking to him...?"
    mc "... Of course, I do."
    $ renpy.pause()
    scene ch3ep3_358 with dissolve
    hide ch3ep3_alice1
    show ch3ep3_alice2
    window hide
    alice "*Sucks* Mhmm...."
    mc "You can talk to him faster if you want..."
    $ renpy.pause()
    scene ch3ep3_359 with dissolve
    hide ch3ep3_alice2
    show ch3ep3_alice3
    window hide
    mc "Yeah... Just like that."
    alice "*Sucks* Mhmmm..... Hehe... I'm glad to you like it..."
    $ renpy.pause()
    scene ch3ep3_360 with dissolve
    hide ch3ep3_alice3
    mc "Alright, stop."
    alice "Hm...? What's wrong?"
    mc "Now, let me play with little [alice]."
    alice "*Giggles* If that's what you want!"
    scene black with dissolve
    scene ch3ep3_361 with dissolve
    alice "Be a little bit careful though."
    alice "*Giggles* She hasn't been playing with anyone for so long."
    mc "Understood."
    scene ch3ep3_362 with dissolve
    show ch3ep3_alice4
    window hide
    alice "*Softly breathes* Haah....."
    mc "She's so wet, [alice]...."
    alice "*Softly breathes* Mhmm... Because of whom...?"
    $ renpy.pause()
    scene ch3ep3_363 with dissolve
    hide ch3ep3_alice4
    show ch3ep3_alice5
    window hide
    alice "*Softly moans* Mhmm... Y-Yeah... Keep playing with her just like that..."
    mc "Okay...."
    $ renpy.pause()
    scene ch3ep3_364 with dissolve
    hide ch3ep3_alice5
    show ch3ep3_alice6
    window hide
    alice "*Heavily breathes* A-Ahhh...! [mc]...!"
    alice "*Heavily breathes* Y-Yeah... That's the spot...!"
    $ renpy.pause()
    scene black with dissolve
    scene ch3ep3_365 with dissolve
    hide ch3ep3_alice6
    mc "Alright...."
    mc "That's enough of teasing. Are you ready now?"
    alice "*Smiles* Yes, I am."
    alice "Put it in. I want it so badly."
    scene ch3ep3_366 with dissolve
    mc "As you...."
    scene ch3ep3_367 with dissolve
    mc "Wish!"
    alice "A-Ahhh~!"
    scene ch3ep3_368 with dissolve
    show ch3ep3_alice7
    window hide
    alice "*Softly breathes* Finally, they're playing with each other... Hehe..."
    alice "*Softly breathses* It feels... so good, [mc]."
    mc "Me, too..."
    $ renpy.pause()
    scene ch3ep3_369 with dissolve
    hide ch3ep3_alice7
    show ch3ep3_alice8
    window hide
    alice "*Softly moans* Ahh.... Mhmm...."
    alice "*Softly moans* Hahh... You can move... faster if you want..."
    $ renpy.pause()
    scene ch3ep3_370 with dissolve
    hide ch3ep3_alice8
    show ch3ep3_alice9
    window hide
    alice "*Moans* Hahhh... Yeah... Right there, [mc]..."
    alice "*Moans* Mhmm... You're driving me crazy..."
    $ renpy.pause()
    mc "*Softly breathes* Get on top of me."
    alice "*Softly breathes* Okay..."
    scene black with dissolve
    scene ch3ep3_371 with dissolve
    alice "A-Ahh..."
    alice "You're so big."
    mc "Does it hurt you?"
    alice "No... Don't worry. I'm going to continue now."
    scene ch3ep3_372 with dissolve
    show ch3ep3_alice10
    window hide
    alice "*Softly breathes* Mhmmm... Your cock...."
    alice "*Softly breathes* Ahhh... It keeps touching... my womb in this position."
    alice "*Softly breathse* It feels sooo.... good."
    $ renpy.pause()
    scene ch3ep3_373 with dissolve
    hide ch3ep3_alice10
    show ch3ep3_alice11
    window hide
    alice "*Moans* [mc]...! [mc]...!"
    mc "*Softly breathes* Yeah... Keep doing it like that. Don't stop."
    $ renpy.pause()
    scene ch3ep3_374 with dissolve
    hide ch3ep3_alice11
    show ch3ep3_alice12
    window hide
    alice "*Heavily breathes* A-Ahhh...! I-It feels so good...!"
    alice "*Heavily breathes* [mc]...! [mc]...!"
    alice "*Heaviyl breathes* H-Hahh...! I-I'm about to cum soon...!"
    mc "*Softly breathes* So do I...."
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch3ep3_alice12
            jump ch3ep3_alicebj1
        "Fingering":
            hide ch3ep3_alice12
            jump ch3ep3_alicefinger1
        "Missionary":
            hide ch3ep3_alice12
            jump ch3ep3_alicemis1
        "Slowest":
            hide ch3ep3_alice12
            jump ch3ep3_alicecow1
        "Slower":
            hide ch3ep3_alice12
            jump ch3ep3_alicecow2
        "Cum":
            jump ch3ep3_alicesexcum
label ch3ep3_alicebj1:
    scene ch3ep3_357 with dissolve
    show ch3ep3_alice1
    window hide
    $ renpy.pause()
    menu:
        "Fingering":
            hide ch3ep3_alice1
            jump ch3ep3_alicefinger1
        "Missionary":
            hide ch3ep3_alice1
            jump ch3ep3_alicemis1
        "Cowgirl":
            hide ch3ep3_alice1
            jump ch3ep3_alicecow1
        "Faster":
            hide ch3ep3_alice1
            jump ch3ep3_alicebj2
        "Fastest":
            hide ch3ep3_alice1
            jump ch3ep3_alicebj3
label ch3ep3_alicebj2:
    scene ch3ep3_358 with dissolve
    show ch3ep3_alice2
    window hide
    $ renpy.pause()
    menu:
        "Fingering":
            hide ch3ep3_alice2
            jump ch3ep3_alicefinger1
        "Missionary":
            hide ch3ep3_alice2
            jump ch3ep3_alicemis1
        "Cowgirl":
            hide ch3ep3_alice2
            jump ch3ep3_alicecow1
        "Slower":
            hide ch3ep3_alice2
            jump ch3ep3_alicebj1
        "Faster":
            hide ch3ep3_alice2
            jump ch3ep3_alicebj3
label ch3ep3_alicebj3:
    scene ch3ep3_359 with dissolve
    show ch3ep3_alice3
    window hide
    $ renpy.pause()
    menu:
        "Fingering":
            hide ch3ep3_alice3
            jump ch3ep3_alicefinger1
        "Missionary":
            hide ch3ep3_alice3
            jump ch3ep3_alicemis1
        "Cowgirl":
            hide ch3ep3_alice3
            jump ch3ep3_alicecow1
        "Slowest":
            hide ch3ep3_alice3
            jump ch3ep3_alicebj1
        "Slower":
            hide ch3ep3_alice3
            jump ch3ep3_alicebj2
label ch3ep3_alicefinger1:
    scene ch3ep3_362 with dissolve
    show ch3ep3_alice4
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch3ep3_alice4
            jump ch3ep3_alicebj1
        "Missionary":
            hide ch3ep3_alice4
            jump ch3ep3_alicemis1
        "Cowgirl":
            hide ch3ep3_alice4
            jump ch3ep3_alicecow1
        "Faster":
            hide ch3ep3_alice4
            jump ch3ep3_alicefinger2
        "Fastest":
            hide ch3ep3_alice4
            jump ch3ep3_alicefinger3
label ch3ep3_alicefinger2:
    scene ch3ep3_363 with dissolve
    show ch3ep3_alice5
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch3ep3_alice5
            jump ch3ep3_alicebj1
        "Missionary":
            hide ch3ep3_alice5
            jump ch3ep3_alicemis1
        "Cowgirl":
            hide ch3ep3_alice5
            jump ch3ep3_alicecow1
        "Slower":
            hide ch3ep3_alice5
            jump ch3ep3_alicefinger1
        "Faster":
            hide ch3ep3_alice5
            jump ch3ep3_alicefinger3
label ch3ep3_alicefinger3:
    scene ch3ep3_364 with dissolve
    show ch3ep3_alice6
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch3ep3_alice6
            jump ch3ep3_alicebj1
        "Missionary":
            hide ch3ep3_alice6
            jump ch3ep3_alicemis1
        "Cowgirl":
            hide ch3ep3_alice6
            jump ch3ep3_alicecow1
        "Slowest":
            hide ch3ep3_alice6
            jump ch3ep3_alicefinger1
        "Slower":
            hide ch3ep3_alice6
            jump ch3ep3_alicefinger2
label ch3ep3_alicemis1:
    scene ch3ep3_368 with dissolve
    show ch3ep3_alice7
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch3ep3_alice7
            jump ch3ep3_alicebj1
        "Fingering":
            hide ch3ep3_alice7
            jump ch3ep3_alicefinger1
        "Cowgirl":
            hide ch3ep3_alice7
            jump ch3ep3_alicecow1
        "Faster":
            hide ch3ep3_alice7
            jump ch3ep3_alicemis2
        "Fastest":
            hide ch3ep3_alice7
            jump ch3ep3_alicemis3
label ch3ep3_alicemis2:
    scene ch3ep3_369 with dissolve
    show ch3ep3_alice8
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch3ep3_alice8
            jump ch3ep3_alicebj1
        "Fingering":
            hide ch3ep3_alice8
            jump ch3ep3_alicefinger1
        "Cowgirl":
            hide ch3ep3_alice8
            jump ch3ep3_alicecow1
        "Slower":
            hide ch3ep3_alice8
            jump ch3ep3_alicemis1
        "Faster":
            hide ch3ep3_alice8
            jump ch3ep3_alicemis3
label ch3ep3_alicemis3:
    scene ch3ep3_370 with dissolve
    show ch3ep3_alice9
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch3ep3_alice9
            jump ch3ep3_alicebj1
        "Fingering":
            hide ch3ep3_alice9
            jump ch3ep3_alicefinger1
        "Cowgirl":
            hide ch3ep3_alice9
            jump ch3ep3_alicecow1
        "Slowest":
            hide ch3ep3_alice9
            jump ch3ep3_alicemis1
        "Slower":
            hide ch3ep3_alice9
            jump ch3ep3_alicemis2
label ch3ep3_alicecow1:
    scene ch3ep3_372 with dissolve
    show ch3ep3_alice10
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch3ep3_alice10
            jump ch3ep3_alicebj1
        "Fingering":
            hide ch3ep3_alice10
            jump ch3ep3_alicefinger1
        "Missionary":
            hide ch3ep3_alice10
            jump ch3ep3_alicemis1
        "Faster":
            hide ch3ep3_alice10
            jump ch3ep3_alicecow2
        "Fastest":
            hide ch3ep3_alice10
            jump ch3ep3_alicecow3
label ch3ep3_alicecow2:
    scene ch3ep3_373 with dissolve
    show ch3ep3_alice11
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch3ep3_alice11
            jump ch3ep3_alicebj1
        "Fingering":
            hide ch3ep3_alice11
            jump ch3ep3_alicefinger1
        "Missionary":
            hide ch3ep3_alice11
            jump ch3ep3_alicemis1
        "Slower":
            hide ch3ep3_alice11
            jump ch3ep3_alicecow1
        "Faster":
            hide ch3ep3_alice11
            jump ch3ep3_alicecow3
label ch3ep3_alicecow3:
    scene ch3ep3_374 with dissolve
    show ch3ep3_alice12
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch3ep3_alice12
            jump ch3ep3_alicebj1
        "Fingering":
            hide ch3ep3_alice12
            jump ch3ep3_alicefinger1
        "Missionary":
            hide ch3ep3_alice12
            jump ch3ep3_alicemis1
        "Slowest":
            hide ch3ep3_alice12
            jump ch3ep3_alicecow1
        "Slower":
            hide ch3ep3_alice12
            jump ch3ep3_alicecow2
        "Cum":
            jump ch3ep3_alicesexcum
label ch3ep3_alicesexcum:
    alice "*Heavily breathes* I-I can't hold it anymore, [mc]...!"
    menu:
        "Cum inside":
            $ ch3ep3cum = 1
            scene ch3ep3_375 with vpunch
            hide ch3ep3_alice12
        "Cum outside":
            $ ch3ep3cum = 2
            scene ch3ep3_375 with vpunch
            hide ch3ep3_alice12
    alice "*Heavily breathes* I-I'm cumming...!!"
    scene ch3ep3_375 with flash
    alice "*Heavily breathes* A-Ahhh....!!!"
    if ch3ep3cum == 1:
        scene ch3ep3_376_in1 with vpunch
        mc "*Softly breathes* Ugh...! Me, too...!"
        scene ch3ep3_376_in1 with flash
        mc "*Softly breahtes* Ahh...."
        scene ch3ep3_376_in2 with dissolve
    else:
        scene ch3ep3_376_out1 with vpunch
        mc "*Softly breathes* Ugh...! Me, too...!"
        scene ch3ep3_376_out1 with flash
        mc "*Softly breahtes* Ahh...."
        scene ch3ep3_376_out2 with dissolve
    alice "*Pants* T... That was... so... good."
    alice "*Pants* You... completely... made me... crazy...."
    mc "*Softly breathes* Shall we... rest for a bit?"
    alice "*Pants* Sure..."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_377 with dissolve
    mc "[alice]."
    alice "Yeah?"
    mc "I should leave now. Lunch time is almost over."
    alice "No, I won't let you leave."
    mc "What do you mean?"
    alice "It's been so long since the last time we had sex."
    alice "It wasn't enough. I'm not satisfied yet."
    scene ch3ep3_378 with dissolve
    alice "In fact... I'm not the only one. Am I right?"
    alice "Look... Your cock is still as hard as a rock even though you just came."
    mc "It's not what y-"
    alice "Let's do it again, okay?"
    mc "......................"
    mc ".... Okay."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_379 with dissolve
    show ch3ep3_alice13
    alice "*Loudly moans* Mhmmm...! Y... Yeah...!"
    s "You spent your time having sex with [alice]...."
    scene black with dissolve
    scene ch3ep3_380 with dissolve
    hide ch3ep3_alice13
    show ch3ep3_alice14
    alice "*Moans* So good...! Mhmmm... So good...!"
    s "Again...."
    scene black with dissolve
    scene ch3ep3_381 with dissolve
    hide ch3ep3_alice14
    show ch3ep3_alice15
    alice "*Heavily breathes* A-Ahhh...! Y-Yeah...! Keep fucking me like that...!"
    s "And again...."
    scene black with dissolve
    $ renpy.pause()
    s "About two hours later........."
    scene ch3ep3_382 with dissolve
    mc "*Pants* Are you satisfied now...."
    alice "*Pants* Y... Yeah... I'm so... exhausted now."
    alice "*Pants* I can't... do it... anymore..."
    mc "Alright then, get up. It's been almost two hours."
    mc "I have to go back to the company as soon as I can."
    mc "You aren't going to hold me here any longer, right?"
    alice "*Giggles* No, I'm not...."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_383 with dissolve
    mc "Okay... I'm going to leave now."
    alice "Thank you for walking me home today."
    mc "You're welcome."
    alice "Let's go find something to eat again soon."
    scene ch3ep3_384 with dissolve
    mc "Okay, sure."
    alice "Perfect."
    alice "Good bye, [mc]. Have a great day."
    mc "You, too. See you later."
    $ renpy.end_replay()
    scene black with dissolve
    jump ch3ep3_gohome
label ch3ep3_gohome:
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    s "Later that evening.........."
    scene ch3ep3_385 with fade
    play music "sfx/ch2ep1_2.mp3" fadein 3.0
    $ bgm = "Tokyo Music Walker - Your Little Wings"
    u "It's been a long day today."
    u "But, the day is almost over..."
    u "I'm so tired now. Let's relax for a bit before going to have dinner."
    scene ch3ep3_386 with dissolve
    u "... Hang on."
    u "To think about it, I still haven't set up the computer table after I moved here."
    u "Everything is still in the boxes."
    u "Let's just unbox them and get it done."
    u "I might need to use the computer soon."
    scene black with dissolve
    $ renpy.pause()
    s "About half an hour later..........."
    scene ch3ep3_387 with dissolve
    u "*Sighs* Finally...."
    u "It took me a bit longer than I thought."
    u "Well, but now it's ready for use after being in the boxes for a couple days."
    scene ch3ep3_388 with dissolve
    u "By the way..."
    u "My room is so non private, isn't it?"
    u "Anyone can see everything through the window from the outside."
    u "I'm going to need to buy a curtain very soon."
    u "... Let's go buy it now."
    scene ch3ep3_389 with dissolve
    u "But, I guess I'll have to clean myself up first."
    u "I'm so sweaty and stinky now."
    u "Let's go to the bathroom."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time taking a shower until finished...."
    scene ch3ep3_390 with dissolve
    u "Alright, I've finished taking a shower."
    u "My phone is on the bed."
    u "Let's go pick it up my phone before leaving."
    if ch3ep3krystalsing == 1:
        scene ch3ep3_391 with dissolve
        s "*Door knocks*................"
        u "... Hm?"
        mc "Who's it?"
        krystal "It's me, [krystal]. Can you open the door, please?"
        mc "Okay. Hang on a second."
        scene black with dissolve
        scene ch3ep3_392 at eyesblink("Ch.3/Ep.3/Scenes/ch3ep3_392.jpg", "Ch.3/Ep.3/Scenes/ch3ep3_392_blink.jpg", 1) with dissolve
        krystal "Hey... Good evening, [mc]."
        mc "Yeah... Good evening."
        scene ch3ep3_393 with dissolve
        krystal "How was your day?"
        mc "Nothing much."
        mc "What brings you here by the way?"
        scene ch3ep3_394 with dissolve
        krystal "Oh... I'm here to ask you if you could go outside with me."
        mc "Hm? Where are you going to go?"
        krystal "In the city. I want to buy a tablet."
        scene ch3ep3_395 with dissolve
        mc "A tablet? Why don't you order it online then?"
        mc "It's much more convenient."
        krystal "I want to go see a real one before buying."
        scene ch3ep3_396 with dissolve
        krystal "Then, we can have dinner right after we finish."
        krystal "It's been a while since we go outside together."
        mc "................"
        krystal "What do you say? Will you go with me?"
        menu:
            "Okay. [krystal1]":
                $ ch3ep3gowithkrystal = 1
                $ krystal_ch3_ep3 += 1
                $ krystal_relationship += 1
                scene ch3ep3_397_a with dissolve
                mc "Okay. I'll go with you."
                krystal "*Smiles* Really?! I'm glad to hear that!"
                krystal "*Smiles* Shall we go now?"
                mc "Yeah, sure."
                scene ch3ep3_398 with dissolve
                krystal "Thank you, [mc]."
                mc "Hm? For what?"
                krystal "For accepting my request."
                krystal "I've asked everyone, but they said they were too tired."
                mc "I see... You're welcome."
                jump ch3ep3shopping
            "I'm sorry.":
                $ ch3ep3gowithkrystal = 2
                scene ch3ep3_397_d1 with dissolve
                mc "I'm sorry. I'm very tired today."
                krystal "Aw...."
                mc "Can you ask someone else to go with you?"
                krystal "I've already done that. Everyone said they were tired as well."
                mc "... Then, shall we go another day?"
                krystal "It's alright... I guess I'll just order it online."
                mc "... Are you sure?"
                krystal "Yeah. Sorry for taking your time. Rest well."
                scene black with dissolve
                $ renpy.pause()
                scene ch3ep3_397_d2 with dissolve
                u "[krystal] looked very sad. I feel so guilty turning her down."
                u "I hope she doesn't get angry at me."
                u "But, I'm really tired today."
                u "Let's go find something to eat and then go to bed right away."
                jump ch3ep3continue
    else:
        scene ch3ep3_397_d2 with dissolve
        u "Alright, let's go find something to eat and then go to bed right away."
        u "I'm very tired today."
        scene black with dissolve
        $ renpy.pause()
        jump ch3ep3continue
label ch3ep3shopping:
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/atoffice.mp3" fadein 3.0
    $ bgm = "B3NJ4M1N - Rainy Days"
    scene ch3ep3_399 with fade
    mc "Okay... We've arrived."
    mc "Where are you going to buy a tablet?"
    krystal "A gadget store of course."
    mc "I don't know where it is. Do you?"
    krystal "Yes, I do."
    mc "Alright then, lead the way."
    krystal "Okay."
    scene ch3ep3_400 with dissolve
    krystal "*Giggles* Follow me close, so you don't get lost."
    mc "Yes, ma'am."
    krystal "*Giggles* Stop...!"
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_401 with fade
    krystal "Finally, we've arrived here."
    mc "It's pretty big."
    mc "I have no idea that there is such a big gadget store in this city."
    krystal "Me, too."
    krystal "Alright, let's go take a look at a tablet."
    mc "Okay."
    scene black with dissolve
    scene ch3ep3_402 with dissolve
    krystal "Here it is..."
    mc "Is this the one that you want?"
    krystal "Yeah."
    mc "Why do you want to buy a tablet by the way?"
    scene ch3ep3_403 with dissolve
    krystal "Hm? I haven't told you?"
    mc "No, you haven't."
    krystal "What? Really?"
    mc "Yeah. Why would I lie?"
    scene ch3ep3_404 with dissolve
    krystal "I'm going to compose a song."
    krystal "And in order to do that, I need a tool."
    krystal "That's why we are here now."
    mc "Hm? You know how to compose a song?"
    krystal "*Giggles* No. I'm just getting started. I still need to learn a lot."
    scene ch3ep3_405 with dissolve
    mc "Then, why does it have to be a tablet?"
    mc "I mean... you can just do it on your phone, as far as I know."
    krystal "I tried, but the screen was too small for me."
    krystal "Moreover, writing down lyrics on tablet is much easier."
    mc "I see..."
    scene ch3ep3_406 with dissolve
    krystal "What color should I buy, [mc]?"
    mc "Hm? Why are you asking me that?"
    mc "It's your tablet, so choose one."
    krystal "But, I want to hear your thoughts."
    scene ch3ep3_407 with dissolve
    krystal "Come on. Just choose one."
    krystal "I've already had a choice in mind."
    krystal "I want to know if you will choose the one I chose."
    mc "Okay then, I choose the white one."
    scene ch3ep3_408 with dissolve
    krystal "*Smiles* Me, too!"
    krystal "*Smiles* It looks like we share the same mind."
    krystal "*Smiles* let's take the white one then!"
    mc "As you wish."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_409 with dissolve
    mc "[krystal]."
    krystal "Yeah?"
    mc "Hand it to me. I'll carry it for you."
    krystal "Thank you. You're so sweet, but I'm alright."
    mc "Are you sure?"
    krystal "Yes, I am."
    scene ch3ep3_410 with dissolve
    krystal "I'm hungry now. What shall we eat today?"
    mc "Umm... How about a grilled meat?"
    mc "I feel like having a grilled beef today."
    krystal "That sounds great. Do you know a good restaurant around here?"
    mc "Yes, I do."
    krystal "Alright, let's go then!"
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_411 with fade
    krystal "Wow...! Look at these dishes."
    krystal "They look all delicious."
    mc "I know, right?"
    krystal "I can't wait to taste them!"
    scene ch3ep3_412 with dissolve
    mc "Well then..."
    mc "Take off your mask so that we can start eating."
    mc "And I mean take it off completely. Not just pulling them down."
    krystal "... What if someone notices me?"
    scene ch3ep3_413 with dissolve
    mc "Who?"
    mc "There is no one else except us here."
    krystal "Oh, yeah... You're right."
    mc "So, don't worry and take it off already."
    krystal "Okay then."
    scene ch3ep3_414 with dissolve
    krystal "*Giggles* This is much better!"
    krystal "*Giggles* I feel a lot more comfortable now."
    mc "That's why I told you to take it off."
    krystal "*Giggles* Thanks!"
    scene ch3ep3_415 with dissolve
    mc "By the way... there is something I haven't asked you yet."
    krystal "Hm? What is it?"
    mc "You said you're going to compose a song, right?"
    krystal "Yes, I did."
    mc "What made you decide to do that?"
    scene ch3ep3_416 with dissolve
    krystal "It's not that I suddenly decided to compose a song."
    krystal "It's always been one of my to-do list, but I just didn't have a chance to do it."
    krystal "Moreover, I stopped doing everything after that incident on stage. I stopped dancing, singing, and playing the guitar."
    krystal "And eventually, it had been so long that I forgot about my dreams, about the things I wanted to do."
    krystal "However, after I bought a new guitar and started playing it again, I'm starting to remember about it."
    mc "I see..."
    scene ch3ep3_417 with dissolve
    mc "What kind of song are you going to compose then? May I ask?"
    krystal "I haven't thought about that yet. I've just started writing the lyrics."
    mc "Yeah? What is it about?"
    krystal "It's about my experiences."
    krystal "I want to make a song that motivates everyone who listens to it."
    scene ch3ep3_418 with dissolve
    mc "That sounds like a very great song to me."
    krystal "Thank you for saying that."
    mc "I can't wait to listen to it."
    krystal "You'll be the first person who listens to it. I promise you."
    scene ch3ep3_419 with dissolve
    krystal "*Giggles* But, there's still a long way to go!"
    krystal "*Giggles* As I told you earlier, I've just getting started."
    krystal "*Giggles* There are a lot of things I need to learn."
    mc "Don't be too worried. As long as you're committed to it, it's going to turn out well."
    scene ch3ep3_420 with dissolve
    mc "Oh... By the way, I know someone who can help you with that."
    scene ch3ep3_421 with dissolve
    krystal "Yeah? Who is it? Do I know him?"
    scene ch3ep3_420 with dissolve
    mc "It's [alice]. You've already met her a couple times."
    scene ch3ep3_421 with dissolve
    krystal "Oh! I remember her!"
    scene ch3ep3_420 with dissolve
    mc "She graduated with a degree in music."
    mc "I think she can teach you."
    scene ch3ep3_421 with dissolve
    krystal "That's so brilliant!"
    krystal "Can you please ask for her help?"
    scene ch3ep3_420 with dissolve
    mc "I'll try that."
    scene ch3ep3_422 with dissolve
    krystal "Thank you so much, [mc]."
    krystal "I owe you big time again."
    mc "No worries. It's just a little bit of help."
    mc "Shall we start eating now? I'm very hungry."
    krystal "Yeah, sure!"
    scene black with dissolve
    $ renpy.pause()
    s "You spent time having dinner with [krystal]...."
    scene ch3ep3_423 with dissolve
    krystal "I'm so full now."
    krystal "All dishes were so delicious."
    krystal "This place has now become one of my favorite restaurants."
    mc "Yeah? I'm glad to hear that."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_424 with fade
    krystal "Thank you for accompanying me today."
    mc "You're welcome."
    krystal "I'll send you the demo of my song as soon as I can."
    mc "Okay. I'll be looking forward to it."
    scene ch3ep3_425 with dissolve
    krystal "Don't set your hopes too high though..."
    krystal "... Hm?"
    scene ch3ep3_426 with dissolve
    krystal "Oh?!"
    krystal "[mc]."
    mc "Yeah?"
    krystal "How long will it take for the next bus to arrive?"
    mc "About ten minutes. Why?"
    scene ch3ep3_427 with dissolve
    krystal "I'm going to go buy an ice cream over there."
    mc "Hm? Didn't you just say that you were full?"
    krystal "*Giggles* There's always room for dessert!"
    mc "Okay... Do you want me to go with you?"
    krystal "No, you don't have to. Just wait for me right here."
    krystal "I'll be right back as soon as I can."
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*............."
    scene ch3ep3_428 with dissolve
    krystal "*Hums* Hmmmm~~"
    krystal "(It's been a while since the last time I ate some ice cream.)"
    krystal "(So delicious... Should I go buy another one?)"
    scene ch3ep3_429 with dissolve
    stop music fadeout 3.0
    u "There she is..."
    u "She seems to be enjoying her ice cream so much."
    u "I can tell how happy she is even from here."
    u "Look at the way she's eating. She's making me want to try some..."
    scene ch3ep3_430 with dissolve
    play music "sfx/ep4_5.mp3" fadein 3.0
    $ bgm = "RYYZN - Waited (instrumental)"
    girl "*Screams*............"
    u "... What's happening over there?"
    scene ch3ep3_431 with dissolve
    girl "*Screams* Help!"
    girl "*Screams* Someone just got kidnapped! Help!"
    scene ch3ep3_432 with dissolve
    u "What the...?!"
    u "It can't be... Was it [krystal]?"
    u "I need to go help her as soon as I can."
    u "But, how am I going to help her. I don't have a car..."
    scene ch3ep3_433 with dissolve
    u "... Hm?"
    u "That bigbike's engine is turned on."
    u ".................."
    scene black with dissolve
    scene ch3ep3_434 with dissolve
    biker "Hey! What the fuck are you doing?!"
    mc "Sorry, sir."
    mc "I have no choice. I need to use this bike."
    biker "W... What are you t-"
    scene ch3ep3_435 with dissolve
    mc "Sorry. I'll turn it back real quick."
    rd "*Horn sounds* Are you crazy?! Do you want to die?!"
    biker "Help! That guy is stealing my bike!"
    biker "Someone help me catch that theif, please!"
    scene ch3ep3_436 with dissolve
    u "Who are those people?"
    u "Why did they kipnap [krystal]?"
    u "Did [victor] send them here?"
    u "Has he already found out that the bluepring is fake?"
    u "No... It can't be. It's too fast."
    scene ch3ep3_437 with dissolve
    u "They still hadn't gotten far. The van is over there."
    u "I still can catch them up."
    u "Let's find out who they are..."
    u "And why they are kidnapping [krystal]."
    scene ch3ep3_438 with vpunch
    rd "*Horn sounds*..............."
    u "!!!!!"
    u "What the...? Isn't it a red light for that lane now?"
    scene ch3ep3_439 with dissolve
    s "*Tire sounds*............."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_440 with dissolve
    u "Fuck...."
    crowd "*Sighs* That was so close...."
    crowd "Is that biker guy alright? They almost hit each other."
    crowd "That driver's driving away now. Someone calls the police, please."
    scene ch3ep3_441 with dissolve
    u "This situation is so bad..."
    u "The van is gone. I completely have no idea where it went."
    u "Looks like I'm going to ask for some help."
    u "Let's get up and call [felix]."
    scene black with dissolve
    scene ch3ep3_442 with dissolve
    mc "Hello, [felix]."
    mc "It's me. Do you have some time?"
    mc "I need your help."
    scene black with dissolve
    scene ch3ep3_445 with dissolve
    felix "I'm driving right now."
    felix "But, I do have some time. What do you want me to help you with?"
    scene ch3ep3_443 with dissolve
    mc "My friend just got kidnapped."
    scene ch3ep3_445 with dissolve
    felix "What? How did it happen?"
    scene ch3ep3_443 with dissolve
    mc "She was about to cross the road back to me."
    mc "But then, there was the van appearing out of no where and took her away right in front of my eyes."
    mc "I tried to chase them, but there was a car running a red light and cut me off."
    scene ch3ep3_446 with dissolve
    felix "That sucks. Do you know who they are?"
    felix "Are they [victor]'s crews?"
    scene ch3ep3_442 with dissolve
    mc "I'm not sure yet. The van blocked my vision."
    mc "The problem is, I couldn't see the van's plate number clearly."
    mc "So, can you track my friend's phone signals?"
    scene ch3ep3_445 with dissolve
    felix "Yes, I can."
    felix "What's her number?"
    felix "I'm going to help her as soon as I get the destination."
    scene ch3ep3_444 with dissolve
    mc "It's 307-XXX-XXXX."
    mc "Where are you right now? Can you come pick me up?"
    mc "I'm at the red light intersection in front of Good Times Coffee."
    mc "Do you know where it is?"
    scene ch3ep3_446 with dissolve
    felix "Yes, I do."
    felix "I'm not so far away from there."
    felix "I'll be there soon."
    scene ch3ep3_444 with dissolve
    mc "Okay. Thank you so much."
    scene ch3ep3_447 with dissolve
    biker "Nooo!! My bike!!!"
    biker "My bike...!!!"
    mc "... I'm sorry."
    scene ch3ep3_448 with dissolve
    biker "You fucker...!!"
    biker "What have you done!?"
    biker "Not only you tried to steal my bike, but also crashed it!!!"
    mc "It's not actually a crash, but still... I'm sorry, sir."
    scene ch3ep3_449 with dissolve
    biker "Sorry? Then what?"
    biker "Will my bike go back to the way it was?"
    mc "Calm down, sir..."
    mc "I'm willing to pay for the repair cost, but let's move away from here first."
    mc "It's dangerous here. We're in the middle of the red light intersection."
    biker ".... Fine!"
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_450 with dissolve
    mc "I'm sorry, sir. I had no choice."
    mc "My friend got kidnapped, so I had to use your bike."
    biker "I don't give a fuck about that."
    biker "How the fuck will you pay for it?"
    s "*Horn sounds*..............."
    scene ch3ep3_451 with dissolve
    u "Hm...? Oh, it's [felix]."
    biker "Hey! You fucker!!"
    biker "Where the fuck are you looking at?!"
    scene ch3ep3_452 with dissolve
    biker "I'm asking you the question!"
    biker "How the fuck are you going to pay for the damage you've done to my bike!?"
    biker "Come! I'll take you to the police station!"
    mc "I'm so sorry, but I have to leave now."
    biker "What?! Who said you can leave now?!"
    scene ch3ep3_453 with dissolve
    mc "My friend is in danger. I have to hurry up."
    mc "I'll give you twenty thousand dollars as an apology."
    biker "... W-What? Twenty thousand?"
    mc "Yeah, but I have no time now."
    mc "Go meet me at Xecon Company tomorrow at nine in the morning."
    mc "And I'll give you the money, but you have to bring me the tablet I left at the bus stop in exchange."
    scene ch3ep3_450 with dissolve
    biker "What if you don't show up?"
    mc "Then, you can report everything to the police."
    mc "I'm sure the CCTVs aroud here captured my face clearly."
    biker "... Fine! Tomorrow it is!"
    mc "Thank you."
    scene black with dissolve
    scene ch3ep3_454 with dissolve
    felix "What happened?"
    felix "Why did you argue with that guy?"
    mc "I took his bike and tried to chase the van."
    felix "Okay. I can guess the ending now."
    scene ch3ep3_455 with dissolve
    felix "By the way, are you alright?"
    felix "You have so many wounds right now."
    felix "Do you want to go to the hospital?"
    mc "Don't worry about me. I'm fine."
    scene ch3ep3_456 with dissolve
    felix "Are you sure?"
    mc "Yeah."
    mc "Helping my friend is way more important."
    mc "Have you got her location yet?"
    scene ch3ep3_457 with dissolve
    felix "No, I haven't."
    felix "But, I've already told [tom] to do it."
    felix "It's just a matter of time."
    mc "Okay..."
    scene ch3ep3_458 with dissolve
    s "*Phone rings*..............."
    felix "Oh... It's [tom]. That was fast. We were just talking about him."
    felix "I think he's already got your friend's location."
    mc "Well then, let's pick it up."
    felix "Okay."
    scene ch3ep3_459 with dissolve
    felix "Have you got anything updated?"
    tom "*Speaker sounds* Yes, sir. I've got her location."
    felix "Good. Send it to me and go meet me at the destination."
    tom "*Speaker sounds* Understood."
    scene ch3ep3_460 with dissolve
    felix "Well... Looking at the map, it looks like the van has already stopped."
    felix "They're about twenty minutes away from here."
    mc "That's great. I thought the van was going to head out of the city."
    mc "Let's hurry up and get there as soon as we can."
    felix "Sure."
    scene black with dissolve
    $ renpy.pause()
    s "*About twenty minutes later*............"
    scene ch3ep3_461 with fade
    mc "Hey. That's the van."
    mc "It's parked over there."
    felix "Yeah. I know..."
    felix "Let me find a place to park the car first."
    scene black with dissolve
    scene ch3ep3_462 with dissolve
    felix "Looks like they are in the building in front of the van."
    felix "But, I can't tell what floor they are on."
    mc "Then, we have no choice, but to search every room until we find them."
    mc "Let's g-"
    scene ch3ep3_463 with dissolve
    felix "Hold on."
    mc "What's wrong?"
    felix "Let's wait for my crew first."
    mc "What? For how long? We don't have much time here."
    mc "The more we wait, the more danger she might be."
    scene ch3ep3_464 with dissolve
    felix "I know, but we don't know how many people there are, and if this is a trap."
    felix "We know nothing at all. So, better be safe than sorry."
    mc "..................."
    felix "Come on. Just calm down and wait for a little bit."
    felix "I think my crew is about to arrive soon."
    mc "... Fine."
    scene black with dissolve
    $ renpy.pause()
    s "*A couple minutes later*........."
    scene ch3ep3_465 with dissolve
    felix "See? Speaking of the devils. Here they are."
    felix "It's only been less than five minutes."
    mc "Well...."
    scene ch3ep3_466 with dissolve
    tom "My apologies for coming late, sir!"
    felix "It's okay. Are you guys ready now?"
    tom "Sir, yes sir!"
    scene ch3ep3_467 with dissolve
    felix "This is the hostage rescue operation."
    felix "The culprits and the hostage are inside the building in front of the van."
    felix "But, We have no information about the exact location yet."
    felix "Therefore, we have to search every single room we can until we find them."
    tom "Loud and clear, sir!"
    scene ch3ep3_468 with dissolve
    tom "Don't worry, [mc]."
    tom "We're going to try our best rescuing your friend."
    tom "Just wait for us here. It won't going to take long."
    mc "What? Who said I'm going to wait here?"
    mc "I'm going to go with you guys, too."
    scene ch3ep3_469 with dissolve
    felix "It could be dangerous. There might even be a gun fight."
    felix "I can't give you a gun as well."
    mc "Don't worry about that. I won't get in your way."
    felix "... Can't you just leave it to us?"
    mc "To be honest the only person I trust, is myself."
    mc "You go deal with the culprits. I'm going to go rescue my friend."
    felix "... Fine. But since I cannot give you a gun to protect yourself, I want you to stay behind us until the path is clear."
    felix "Then, you can go rescue your friend."
    mc "Okay."
    scene ch3ep3_470 with dissolve
    felix "Alright then, let's get inside."
    felix "I'm reminding you all again, the most important thing is the safety of the hostage."
    felix "We won't do anything recklessly until we have no choice. Keep that in mind."
    tom "Sir, yes sir!"
    policea "Loud and clear, sir!"
    scene black with dissolve
    scene ch3ep3_471 with dissolve
    tom "Damn... There are so many rooms."
    tom "It also looks like the place is abandoned, sir..."
    tom "This place looks so deserted."
    scene ch3ep3_472 with dissolve
    felix "Then, it's even better for us."
    felix "Go ahead and check on every room."
    tom "Sir, yes sir!"
    scene ch3ep3_473 with dissolve
    tom "Alright guys, let's hurry up and search for the hostage."
    tom "The more time we take, the more worse situation gets."
    policeb "Understood!"
    policea "I'll go check the first room of the left side."
    policeb "Then, I'll go check the one on the right side."
    scene black with dissolve
    s "*Some time passed*............."
    scene ch3ep3_474 with dissolve
    tom "We've checked every single room except this room, sir."
    tom "All of them were completely clear."
    tom "They must be behind this door for sure."
    policea "I agree with him."
    scene ch3ep3_475 with dissolve
    unknown "*Girl's voice* No...! You can't do that...!"
    felix "Hm...? Did you guys hear that?"
    policea "Loud and clear, sir."
    unknown "*Man's voice* Hahah... Why can't I?"
    unknown "*Girl's voice* This's not right...!"
    mc "That's her voice..."
    felix "Alright, get ready everyone."
    scene ch3ep3_476 with dissolve
    policea "Let me see if the door's locked..."
    tom "What if it's locked? Can you unlock it?"
    policea "Of course, I can."
    tom "Okay. Do it quick and quiet so that they don't notice us coming."
    policea "Sure."
    felix "Stay behind us, okay?"
    mc "... Okay."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_477 with dissolve
    policea "The door is unlocked now, sir."
    felix "Great. On my count..."
    felix "One..."
    felix "Two..."
    felix "Three!"
    scene black with dissolve
    scene ch3ep3_478 with vpunch
    felix "Everybody, freeze!"
    felix "This is the po-"
    stop music fadeout 3.0
    scene ch3ep3_479 with dissolve
    felix "-lice...."
    man1 "Lovely! Yeah, that's right. You all are on the same tempo now."
    scene ch3ep3_480 with dissolve
    felix ".................."
    tom ".................."
    u "(.... What the hell are they doing?)"
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene ch3ep3_481 with dissolve
    man1 "Guys... Looks like our time is up now."
    krystal "Oh?! Hey, [mc]!"
    man2 "Damn... That was so fast."
    man3 "Yeah..."
    scene ch3ep3_482 with dissolve
    felix "Alright, guys. Stop whatever you're doing."
    man1 "Can you wait until we finish shooting a video, please?"
    felix "No, I can't. You all need to follow us to the police station now."
    tom "Put your hands in front of you together."
    man3 "Okay...."
    scene ch3ep3_483 with dissolve
    mc "Hey. Are you okay? Did they hurt you?"
    krystal "Yes, I am. They didn't hurt me at all."
    mc "I'm sorry for coming to rescue you so late."
    krystal "It's alright. As I told you, they didn't hurt me at all."
    scene ch3ep3_484 with dissolve
    krystal "Sir, can you let them go?"
    krystal "These people are my fans. They didn't actually do anything bad."
    krystal "They just wanted to take a video of them dancing with me."
    man2 "Aw... How sweet of you. As expected, you're truely an angel..."
    policeb "I'm sorry. I can't do that."
    policeb "Even if they didn't hurt you, the fact that they kidnapped you hasn't changed."
    krystal "Okay...."
    scene black with dissolve
    scene ch3ep3_485 with dissolve
    felix "Hey. What are you waiting for?"
    felix "Come. I'll bring both of you back to your house."
    mc "Don't waste your time. Just go back to the police station with them."
    felix "Are you sure?"
    scene ch3ep3_486 with dissolve
    mc "Yeah, I am."
    mc "Thank you for helping me out today though. I appreciate it a lot."
    felix "... You're welcome. I'll see you later then."
    mc "Sure thing. Bye."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_487 with dissolve
    krystal "[mc]. You're injured. What happened?"
    mc "... Well, I got accident while trying to chase the van."
    krystal "I'm so sorry..."
    mc "Don't be. It's not a big thing."
    scene ch3ep3_488 with dissolve
    krystal "Yes, it is!"
    krystal "Not only on the left arm, there is a scratch on your right arm, too!"
    mc "..................."
    krystal "Turn around. Let me see if there's somewhere else."
    mc "... Okay."
    scene ch3ep3_489 with dissolve
    krystal "Oh my god...!"
    krystal "You've got so many abrasions, [mc]!"
    krystal "Let's go to the hospital."
    mc "That's unnecessary."
    scene ch3ep3_490 with dissolve
    krystal "Yes, it is necessary! You're injured because of me!"
    krystal "I'm going to take you to the hospital no matter what!"
    mc "But...."
    krystal "There is no but! Go to the hospital right now!"
    mc "....................."
    krystal "*Deadly stares*..............."
    mc "*Sighs* Fine.... Let's go then."
    scene black with dissolve
    $ renpy.pause()
    s "You went to the hospital with [krystal], then came back home....."
    scene ch3ep3_491 with fade
    krystal "Thank you for today, [mc]. Sincerely."
    krystal "And the way you tried to do everything to rescue me was very impressed."
    mc "I let my guard down, so I had to take that responsibility."
    krystal "Still I appreciated it a lot."
    scene ch3ep3_492 with dissolve
    krystal "I'm not going to take any more of your time today. You can go get some rest."
    mc "Okay. Have a good sleep."
    mc "I'll bring you the tablet tomorrow evening."
    krystal "Oh! The tablet. I completely forgot."
    krystal "Thank you so much."
    mc "You're welcome. Bye."
    krystal "Good night."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_493 with dissolve
    u "What a long day it was..."
    u "I took a shower once in the evening, but I'm dirty again."
    u "Let's go take a quick shower."
    scene ch3ep3_494 with dissolve
    u "Alright, I've finished taking a shower."
    u "I'm very tired now. I really need a sleep."
    u "Let's go to bed."
    scene black with dissolve
    $ renpy.pause()
    jump ch3ep3continue
label ch3ep3continue:
    scene black with dissolve
    s "Next morning......"
    if ch3ep3gowithkrystal == 1:
        scene ch3ep3_495 with fade
    else:
        scene ch3ep3_495_d with fade
    play music "sfx/ch2ep1_2.mp3" fadein 3.0
    $ bgm = "Tokyo Music Walker - Your Little Wings"
    u "I had a good sleep last night. I feel so refreshed now."
    u "It's already half past seven."
    u "Let's go take a shower and get changed so that I can go to work."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_496 with dissolve
    u "Okay... Now, I have to eat something before leaving."
    u "I feel like having a bread and a cup of coffee this morning."
    u "Let's go to the kitchen."
    s "*Phone vibrates*............"
    u "... Hm?"
    scene ch3ep3_497 with dissolve
    u "Oh...? it's [maya]."
    u "I didn't expect her to call me this early in the morning."
    u "Let's pick it up and find out what she is up to."
    scene ch3ep3_498 with dissolve
    mc "Hey..."
    mc "Good morning, [maya]."
    scene ch3ep3_500 with dissolve
    maya "Hi. Good morning, [mc]."
    maya "Did I wake you up?"
    scene ch3ep3_498 with dissolve
    mc "No, you didn't."
    mc "I was about to go have breakfast before you called."
    scene ch3ep3_500 with dissolve
    maya "Oh... Then, I'm not going to take much of your time."
    maya "Are you free at lunch time? Let's go have lunch together."
    menu:
        "Agree to have lunch with her. [smrec]":
            scene ch3ep3_499 with dissolve
            mc "I don't have any particular plan. So yeah, I'm free."
            mc "Let's go have lunch together."
            mc "Where are we going to meet up?"
            scene ch3ep3_501 with dissolve
            maya "Lovely. I'm glad to hear that."
            maya "I'll go pick you up right in front of Xecon at twelve."
            maya "Is that okay for you?"
            scene ch3ep3_499 with dissolve
            mc "I have no problem with that."
            mc "See you soon."
            $ ch3ep3lunchwithmaya = 1
        "Refuse to have lunch with her.":
            scene ch3ep3_499 with dissolve
            mc "I'm sorry. I think it's too early for us to meet up now."
            mc "Let's wait for the situation is more safe."
            scene ch3ep3_501_d with dissolve
            maya "Oh... Is that so?"
            maya "Well... that makes sense."
            maya "I guess I'll have to wait then."
            scene ch3ep3_499 with dissolve
            mc "Yeah... Sorry for disappoint you."
            scene ch3ep3_501_d with dissolve
            maya "Don't be. I understand you."
            maya "I'm hanging up now. Good bye, [mc]. Stay safe."
            $ ch3ep3lunchwithmaya = 2
    scene ch3ep3_496 with dissolve
    u "Alright... Let's go have breakfast."
    scene black with dissolve
    $ renpy.pause()
    s "*About an hour later*.........."
    scene ch3ep3_502 with fade
    if ch3ep3gowithkrystal == 1:
        u "I wonder if that biker guy has arrived yet."
        unknown "Hey!"
        u "Hm...?"
        scene ch3ep3_503 with dissolve
        mc "Oh, there you are."
        mc "I was looking for you."
        biker "Thank god I didn't come here for nothing."
        scene ch3ep3_504 with dissolve
        biker "Here's the tablet. Take it."
        mc "Thanks. How's your bike by the way?"
        biker "The left mirror is broken, and there are scratches on the whole left side."
        mc "I'm so sorry again. I didn't want to do that to your bike."
        scene ch3ep3_505 with dissolve
        biker "Let's cut the crap and give me the money already."
        mc "Okay. I'll transfer it to you now."
        biker "What? You don't have cash?"
        mc "No, I don't. Why should I?"
        scene ch3ep3_506 with dissolve
        biker "Tsk...! Fine..."
        biker "It's 015xxxxxxx. XXX Bank."
        mc "Okay. Hang on a sec."
        biker "You better hurry up. I don't have all day."
        mc "....................."
        scene ch3ep3_507 with dissolve
        mc "Alright, I've already transferred it to you account."
        mc "You can check it now."
        biker "*Smirks* Yeah, I've got it now."
        mc "Well then, are we all good now?"
        scene ch3ep3_508 with dissolve
        biker "Of course, man. We're all good now."
        biker "It actually wasn't a big problem after all."
        mc "Alright then, please excuse me. I have to leave now."
        biker "Sure, man. Thank you for the money."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep3_509 with dissolve
        u "That's it. The problem solved."
        u "Twenty thousand is a little bit too much, but it's fine as long as that guy stopped bothering me."
        u "At least it's far better than him reporting me to the police."
        u "Alright, it's time to go to my department now."
    else:
        u "Alright, I've arrived at the company."
        u "Let's go get an elevator to my department."
    scene black with dissolve
    $ renpy.pause()
    if nominatekrystal == 1:
        scene ch3ep3_510 with fade
        mc "Hm...?"
        faye "Oh...?"
        scene ch3ep3_511 with dissolve
        faye "Good morning, [mc]."
        mc "Good morning, [faye]."
        faye "This is perfect. I was about to go to your department."
        mc "Hm? Why?"
        scene ch3ep3_512 with dissolve
        faye "I was about to go there and tell your about the launch date."
        mc "What's it about?"
        faye "The launch date has already been set."
        faye "It's going to begin in the next five days."
        scene ch3ep3_513 with dissolve
        mc "The next five days...?"
        mc "You mean... Wednesday, right?"
        faye "Yeah, that's right."
        faye "Please, inform [krystal] about it."
        scene ch3ep3_514 with dissolve
        mc "Sure. Where will the launch event be held by the way?"
        faye "Here."
        mc "Here?"
        faye "Yes, we have the area big enough to hold that kind of event."
        faye "We just have to arrange it a little bit."
        scene ch3ep3_513 with dissolve
        mc "Well... I never knew that."
        mc "What time should she arrive here?"
        faye "The event will start at ten in the morning, so she should arrive here around at least an hour before."
        scene ch3ep3_514 with dissolve
        mc "Okay. I'll tell her that."
        faye "Thank you."
        scene ch3ep3_515 with dissolve
        s "*Elevator bell rings*.........."
        faye "Oh. The elevator has arrived."
        faye "Let's get in."
        mc "Sure."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time working until lunch break...."
    scene ch3ep3_516 with dissolve
    u "Okay... I've already turned off the computer."
    u "It's lunch break now. Let's go find something to e-"
    unknown "[mc]."
    u "Hm?"
    scene ch3ep3_517 with dissolve
    mc "Oh... Hi, [liam]."
    mc "Is there something I could help you with?"
    liam "No, there isn't. That's not the reason I called you."
    mc "Hm? Then, what is it?"
    scene ch3ep3_518 with dissolve
    liam "I just heard that the president has been looking for someone to replace you."
    liam "Are you going to resign? Why?"
    liam "Is it... because of me?"
    liam "Did I give you too many workload?"
    mc "No, it's not because of you."
    scene ch3ep3_519 with dissolve
    liam "Then, what is the reason?"
    liam "To be honest I don't really want you to resign."
    liam "You're such a good co-worker."
    liam "I can rely on you every time I assign you some work."
    liam "Can you rethink about resigning?"
    scene ch3ep3_520 with dissolve
    mc "Calm down..."
    mc "It wasn't actually a resignation. It's more of an annual leave due to my personal reason."
    mc "Therefore, [rowan] wanted to give me more time and freedom to deal with my problem."
    mc "I will be back after everything is good."
    liam "I see..."
    scene ch3ep3_521 with dissolve
    mc "In fact, I can still come here whenever I want."
    liam "Is that so...?"
    mc "Yeah. So, if you ever need my help, don't be hesitate to call me."
    mc "I'll come and help you if I can."
    scene ch3ep3_522 with dissolve
    liam "Okay, I'm relieved now."
    liam "I'm sorry for acting like a kid earlier."
    mc "It's okay. I understand you."
    liam "Thank you. By the way, are you free now? Shall we go have lunch together?"
    scene ch3ep3_523 with dissolve
    mc "You're too late."
    mc "I already have an appointment."
    liam "Oh... Is that so?"
    mc "Yeah... I'm sorry."
    liam "It's okay. Have a good lunch."
    mc "You, too."
    scene black with dissolve
    scene ch3ep3_524 with dissolve
    if ch3ep3lunchwithmaya == 1:
        u "[liam] took my time a lot more than I expected..."
        u "Let's hurry up and go meet [maya]."
        u "She must have been waiting for me."
        jump ch3ep3_lunchwithmaya
    else:
        u "Well... I actually didn't have an appointment since I turned down [maya]."
        u "But, I just didn't feel like having lunch with him today."
        u "I'll just go find something to eat alone in a quiet place."
        jump ch3ep3_evening
label ch3ep3_lunchwithmaya:
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ch2ep1_1.mp3" fadein 3.0
    $ bgm = "Roa - Winter Magic"
    scene ch3ep3_525 with dissolve
    u "There they are."
    u "Looks like they must have been waiting for me for at least ten minutes already."
    u "Let's hurry up and walk to them."
    scene ch3ep3_526 with dissolve
    mc "I'm really sorry to kept you waiting."
    mc "My co-worker wanted to talk to me, so..."
    angela "It's alright. Let's get in the car first."
    mc "Okay."
    scene black with dissolve
    scene ch3ep3_527 with dissolve
    maya "Hello, son."
    mc "Hello, m... mother."
    maya "*Smiles* I'm so glad to see you today."
    mc "... Me, too."
    maya "Is everything alright?"
    mc "Yeah, it's still alright for now."
    scene ch3ep3_528 with dissolve
    mc "Where are we going to go by the way?"
    maya "It's an Italian restaurant nearby."
    mc "Italian restaurant?"
    maya "Why? Do you want to eat something else?"
    mc "No. It's fine by me."
    scene ch3ep3_529 with dissolve
    maya "Alright then, [angela]."
    angela "Yes?"
    maya "Let's get going."
    angela "Understood. Please, fasten your seat belt, [mc]."
    mc "Okay."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_530 with fade
    maya "Looks like they are no other customers here. It feels so private."
    mc "You didn't reserve the entire restaurant, right...?"
    maya "*Giggles* What? No, I didn't. Why should I do that?"
    maya "We're just so lucky today."
    scene ch3ep3_531 with dissolve
    maya "Let's take a seat right here. Shall we?"
    maya "Or you want to sit elsewhere?"
    mc "Let's just sit here."
    maya "Okay then."
    scene black with dissolve
    scene ch3ep3_532 with dissolve
    maya "Hm...? What are you waiting for, [angela]?"
    angela "Pardon?"
    maya "Why don't you take a seat already?"
    angela "I think I'm going to sit on another table."
    scene ch3ep3_533 with dissolve
    maya "That's unnecessary. Just sit here with us."
    angela "But... I want both of you to spend quality family time together."
    maya "What are you talking about? You're my family as well."
    angela "I very appreciated you saying that, but..."
    maya "Come on. Take a seat already."
    angela "... Understood."
    scene ch3ep3_534 with dissolve
    maya "Don't be considerate and order anything you want to eat, okay?"
    maya "I'll pay for both of you."
    mc "Okay. I get it."
    angela "Thank you so much."
    scene black with dissolve
    scene ch3ep3_535 with dissolve
    waitress "Welcome to our restaurant."
    waitress "What would you like to have, ma'am?"
    maya "Can I have Spaghetti Bolognese, please?"
    waitress "What about a drink?"
    maya "Just water. Thank you."
    waitress "Understood."
    scene ch3ep3_536 with dissolve
    waitress "What about you, sir?"
    mc "I'd like to have Pepperoni Pizza and Pork Lasagna."
    mc "And a bottle of coke, please."
    waitress "And you, miss?"
    angela "Can I have Spaghetti Carbonara and Garlic Bread."
    angela "And a bottle of coke as well. Thank you."
    waitress "Noted that. Please, wait for your food for about fifteen minutes."
    scene black with dissolve
    scene ch3ep3_537 with dissolve
    maya "How's your life after moving to the new house?"
    mc "It's actually closer to the company than the old house, so It's pretty good."
    maya "Glad to hear that."
    mc "But, there is no curtain in my room, so it is too open."
    maya "Oh. I'll buy you one."
    mc "Thanks, but I'm good. I'll buy it myself this evening."
    scene ch3ep3_538 with dissolve
    maya "Okay. If you say so."
    mc "By the way, I haven't seen [skylar] for so long."
    mc "Has she been busy recently?"
    maya "Yes, she has. Her midterm exam is incoming soon."
    mc "I see..."
    scene ch3ep3_539 with dissolve
    maya "[mc]."
    mc "Yes?"
    maya "What's your plan after everything is done?"
    maya "Do you want to move in and live with me and [skylar]?"
    scene ch3ep3_540 with dissolve
    mc "That sounds okay, but to be honest I haven't thought about it yet."
    mc "It's not that I don't want to live with you."
    mc "But, I don't want to think too far."
    mc "I'm only focusing on taking down [victor] at the moment."
    mc "I hope you understand."
    scene ch3ep3_541 with dissolve
    maya "Of course, I do understand you."
    maya "I was just asking. There is no need to take it serious now."
    mc "Thank you..."
    maya "By the way, do you have a girlfriend?"
    mc "Hm...? No, I don't. Why do you ask?"
    maya "Nothing much. I just want you to have a good woman beside you after everything is done."
    scene ch3ep3_542 with dissolve
    maya "How about [angela]?"
    angela "W-What?!"
    maya "I can confirm you that she is a very good woman."
    angela "T-Thank you for your compliment, but... I'm just an employee."
    angela "I don't dare to think about something like that."
    scene ch3ep3_543 with dissolve
    maya "*Giggles* No, you aren't just an employee."
    maya "In my opinion, you are a part of my family."
    maya "Therefore, it would be fantastic if you and my son can get along."
    angela "But..."
    scene ch3ep3_544 with dissolve
    maya "My son."
    mc "... Yes?"
    maya "What do you think about her?"
    maya "If it's [angela], I completely give the green light."
    if angela_relationship == 16:
        menu:
            "She's beautiful. [angela2]":
                $ ch3ep3complimentangela = 1
                $ angela_relationship += 2
                $ angela_ch3_ep3 += 2
                scene ch3ep3_545_a1 with dissolve
                mc "She is a very beautiful woman."
                angela "..... Thank you."
                mc "And she must be a very good woman since you complimented her that much."
                mc "But...."
                scene ch3ep3_545_a2 with dissolve
                mc "If I'm going to have a girlfriend, I want everything to happen naturally."
                maya "Heh... I never knew you were romantic."
                maya "*Giggles* I've learned something new about my son today."
                mc "..................."
                maya "Alright, I'll stop for now."
                maya "I don't want you to think that I like to dictate other people's lives."
                scene black with dissolve
                $ renpy.pause()
                s "You spent time having lunch with [maya] and [angela]...."
            "You're making her uncomfortable.":
                $ ch3ep3complimentangela = 2
                scene ch3ep3_545_d with dissolve
                mc "I understand that you wish me the best, but..."
                mc "If I'm going to have a girlfriend, I want everything to happen naturally."
                mc "Moreover, you're making her uncomfortable now."
                angela "I'm not that uncomfortable, but thank you for saying that, [mc]."
                scene ch3ep3_544 with dissolve
                maya "Oh... Is that so?"
                maya "I'm very sorry. I didn't mean that."
                scene black with dissolve
                $ renpy.pause()
                s "You spent time having lunch with [maya] and [angela]...."
    else:
        scene ch3ep3_545_d with dissolve
        mc "I understand that you wish me the best, but..."
        mc "If I'm going to have a girlfriend, I want everything to happen naturally."
        mc "Moreover, you're making her uncomfortable now."
        angela "I'm not that uncomfortable, but thank you for saying that, sir."
        scene ch3ep3_544 with dissolve
        maya "Oh... Is that so?"
        maya "I'm very sorry. I didn't mean that."
        scene black with dissolve
        $ renpy.pause()
        s "You spent time having lunch with [maya] and [angela]...."
    scene ch3ep3_546 with dissolve
    maya "Alright, let's go pay for the bill and leave."
    maya "I'm so full now. What about you guys?"
    mc "Me either."
    angela "Yes, I'm full as well..."
    scene black with dissolve
    $ renpy.pause()
    s "*About fifteen minutes later*..........."
    scene ch3ep3_547 with fade
    maya "Thank you for having lunch with me today, son."
    mc "I should be the one saying that."
    mc "Thank you for paying me a meal today."
    maya "*Smiles* It's not a big deal. I can pay you a meal for your life time."
    scene ch3ep3_548 with dissolve
    mc "... Thank you."
    mc "Alright, I have to get back in the company now."
    maya "Yeah. Me either."
    mc "Travel safely."
    maya "Thank you. See you again soon."
    mc "Yeah, see you again soon."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time working until evening...."
    jump ch3ep3_evening
label ch3ep3_evening:
    scene ch3ep3_549 with fade
    u "It's already evening."
    u "Let's go home... Wait. I feel like I forgot something."
    u "Oh, it's a curtain. I still haven't bought it."
    u "I was about to buy it the day [krystal] invited me go buy the tablet with her."
    u "But, I completely forgot."
    u "Let's go to the shopping mall and buy one before going home."
    scene black with dissolve
    scene ch3ep3_550 with dissolve
    u "I'll just go pick one real quick."
    u "Let's hope they have a delivery and an installation service."
    u "Judging from the height of my room, I'm going to need a very big curtain."
    u "There is no way I can carry a curtain that big home by myself."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time buying a curtain, and get back home with the curtain shop's employees...."
    scene ch3ep3_551 with fade
    man1 "Where do you want to hang the curtain, sir?"
    mc "Over there."
    man1 "Understood."
    scene ch3ep3_552 with dissolve
    mc "How long is it going to take? May I ask?"
    man1 "About half an hour, sir."
    mc "Okay. I get it. Thank you."
    man1 "Then, may we start now?"
    mc "Sure. Go ahead."
    if ch3ep3gowithkrystal == 1:
        scene ch3ep3_553 with dissolve
        u "There is nothing I can do in my room now."
        u "Let's just go and give [krystal] the tablet."
        u "I didn't see her anywhere else when entering the house."
        u "She must be in her bedroom now."
        scene ch3ep3_554 with dissolve
        s "*Door knocks*.............."
        krystal "... Yes?"
        mc "It's me. Can I come in?"
        krystal "Sure. Come on in. The door isn't locked."
        mc "Okay."
        scene ch3ep3_555 with dissolve
        krystal "Good evening, [mc]."
        mc "Good evening. Here is your tablet."
        krystal "Oh! Thank you so much."
        krystal "*Giggles* I almost spent money for nothing."
        scene ch3ep3_556 with dissolve
        mc "And about the launch event. It's going to be held in the next five days."
        krystal "Today is Friday, so... it's Wednesday, right?"
        mc "Yes, it is."
        mc "[faye] told me that you have to arrive at Xecon around nine o'clock."
        krystal "You're going to take me there, right?"
        mc "Yes, I am."
        krystal "Then, I have no problem with that."
        scene ch3ep3_557 with dissolve
        mc "Okay. That's it."
        mc "I'm going to go back to my room now."
        krystal "Sure. See you around."
        mc "See you."
        krystal "Thank you for the tablet again."
        mc "You're welcome."
    scene black with dissolve
    $ renpy.pause()
    s "Almost an hour later.........."
    scene ch3ep3_558 with dissolve
    man1 "Alright, it's done now, sir."
    mc "Thank you."
    man2 "Please accept our apologies for taking more time than we told you."
    man2 "The installation progress was harder than we thought."
    mc "It's alright."
    mc "There is no need for an apology. I'm happy with the outcome."
    man1 "Thank you."
    scene ch3ep3_559 with dissolve
    man1 "The curtain has 2 years warranty. So, if anything happens, you can contact us anytime."
    mc "I get it."
    man2 "Okay then, please excuse us."
    mc "Okay. I'll lead you the way."
    man1 "That'd be awesome. Thank you."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_560 with dissolve
    u "Well..."
    u "I'm so hungry now. Let's go find something to eat."
    u "Then, I'll go take a shower and find something to do before going to bed."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    s "The weekend has passed as the time flew by. Once you realised it, it's already Monday."
    play music "sfx/ch1ep2.mp3"
    $ bgm = "Bensound - Little Idea"
    scene ch3ep3_561 with fade
    mc "... Hm?"
    sally "Oh...?!"
    scene ch3ep3_562 with dissolve
    sally "Hey, [mc]! Good morning!"
    mc "Good morning, [sally]."
    mc "Did you just come out of my department?"
    sally "Yeah. I just gave the bug report to [liam]."
    sally "Now, I'm going to go back to my department."
    mc "I see... Good bye then."
    scene ch3ep3_563 at eyesblink("Ch.3/Ep.3/Scenes/ch3ep3_563.jpg", "Ch.3/Ep.3/Scenes/ch3ep3_563_blink.jpg", 1) with dissolve
    sally "Hang on a second."
    mc "Hm? Why?"
    sally "It's been awhile since the last time we dived into the game."
    sally "There's the boss that I can't beat yet."
    sally "So, I'm kind of wonder if you can help me at lunch break?"
    mc "What makes you think I can help you beat it?"
    sally "Well, the last time I saw you fought goblins, you were very good at it."
    mc "........................."
    menu:
        "Agree to help her. [sally1]":
            $ ch3ep3helpsally = 1
            $ sally_relationship += 1
            $ sally_ch3_ep3 += 1
            scene ch3ep3_564_a with dissolve
            mc "... Fine."
            mc "I don't know how much I could help, but let's just try it."
            sally "Yeah! I'm glad to hear that!"
            sally "Thanks, [mc]. See you at lunch break."
            mc "Okay. See you."
            jump ch3ep3sallymeet
        "Refuse to help her.":
            $ ch3ep3helpsally = 2
            scene ch3ep3_564_d with dissolve
            mc "... I'm sorry, but I can't help you with that."
            sally "... Why?"
            mc "It's lunch time we're talking about."
            mc "I'm going to be hungry by then. I better go have lunch."
            sally "Okay...."
            scene black with dissolve
            $ renpy.pause()
            s "You spent time working until lunch time, then went for lunch...."
            jump ch3ep3rowanmeet
label ch3ep3sallymeet:
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_565 with fade
    sally "Thanks for coming."
    mc "You're welcome."
    sally "Alright then, let's not waste any more time."
    sally "Let's get the Xecon Gear and dive into the game now."
    mc "Got it."
    scene black with dissolve
    scene ch3ep3_566 with dissolve
    sally "Are you ready now?"
    mc "Yes, I am."
    sally "Alright then, see you again soon."
    mc "Sure. See you in the game soon."
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_567 with fade
    sally "Hello, again."
    mc "Hey."
    mc "It's been quite some time since the last time I was in here."
    mc "This is my second time, but I still can't believe we are in the game right now."
    sally "Well then, you better get used to it soon."
    scene ch3ep3_568 with dissolve
    sally "We're going to fight one of the strongest bosses of the early game."
    sally "I tried soloing her a couple times, but always ended up failing."
    mc "Then, can we actually beat her?"
    sally "I don't know. We've just got to try."
    mc "Okay then, lead me the way."
    sally "Sure."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_569 with fade
    sally "Here we are..."
    mc "Hm...? It was a daytime earlier, but it has suddenly become dark as soon as we entered this area."
    sally "Well... That is because this area is in another dimension."
    mc "I see..."
    sally "We're getting close. As soon as we get up there, the boss is going to attack us."
    sally "So, you better be prepared."
    mc "I get it."
    scene ch3ep3_570 with dissolve
    mc "Hm...? Where is the boss?"
    mc "I don't see it here."
    sally "I have no idea..."
    play music "sfx/ep.3/ep3_7.mp3" fadein 3.0
    $ bgm = "Jeff II - Heartfül of Kerøsene"
    scene ch3ep3_571 with dissolve
    mc "Hey... Can you see that dark aura?"
    sally "Yes, I can."
    sally "Bring your swords out, [mc]. She's about to show herself soon."
    mc "Got it."
    scene ch3ep3_572 with dissolve
    sally "There she is..."
    mc "Hey. I completely forgot to ask you."
    mc "What's her ability. Is there any particular thing I should be careful of?"
    sally "What? Seriously? I haven't told you about that?"
    mc "Yes, you haven't...."
    scene ch3ep3_573 with dissolve
    grim "How dare you invade my territory, you low life humans."
    sally "*Sighs* Damn it..."
    sally "Her ability is dark magic and her strength."
    sally "And be careful of her scythe. It's really big, right?"
    mc "Yeah..."
    sally "Its attack range is no joke."
    scene ch3ep3_574 with vpunch
    grim "I'm gonna rip you apart and cut your souls into pieces for sins!"
    sally "Watch out! She's coming!"
    mc "Okay."
    scene ch3ep3_575 with vpunch
    sally "Holy shield...!"
    grim "What a useless defense... You think I can't cut through it...?"
    scene ch3ep3_576 with dissolve
    mc "Instead of cutting through that shield, I think you better watch your back."
    mc "Got you..."
    scene ch3ep3_577 with vpunch
    mc "!!!!???"
    mc "What the...?! Where has she gone?"
    grim "You think I'd have fallen for your stupid trick, human?"
    grim "So pathetic..."
    scene ch3ep3_578 with dissolve
    grim "I'm going to make you pay for your stupidity."
    grim "Die..."
    scene ch3ep3_579 with vpunch
    sally "Reflect shield!"
    grim "!!??"
    grim "You annoying human..."
    scene ch3ep3_580 with dissolve
    mc "Thank you, [sally]."
    mc "She almost got me."
    sally "You're welcome. Keep on fighting!"
    sally "I know you can do it. I'm going to support you from here."
    mc "Okay... I will try my best not to let you down."
    scene black with dissolve
    $ renpy.pause()
    stop music fadeout 3.0
    s "*About an hour later*............."
    scene ch3ep3_581 with dissolve
    sally "Yes! We did it, [mc]!"
    sally "We might be struggling, but we finally did it!"
    mc "*Sighs* Phew... Yeah... Finally..."
    mc "*Softly breathes* I almost died so many times if it wasn't for you."
    sally "*Giggles* That's what we called teamwork!"
    scene ch3ep3_582 with dissolve
    mc "*Softly breathes* Oh... That's her scythe."
    sally "Yeah. It's the reward for killing the boss."
    sally "But, the drop rate isn't a hundred percent. In fact, it's actually very low."
    sally "I guess the god of luck is on our team today."
    mc "*Softly breathes* Obviously..."
    scene ch3ep3_583 with dissolve
    sally "Imagine this isn't just a test server. We would become rich by selling it."
    sally "According to the information, it's one of the best weapons for the early stage of the game."
    mc "*Softly breathes* I think I've seen that information as well."
    sally "*Giggles* Looks like I'm going to make you my party member no matter what once the game opens."
    mc "*Softly breathes* What? I'm going to have to fight her again?"
    sally "Yeah! Why not?"
    scene ch3ep3_584 with dissolve
    mc "*Softly breathes* Come on... I got this tired after fighting her for only once."
    mc "*Softly breathes* I don't want to experience it again."
    mc "*Softly breathes* By the way, isn't the feeling system way too good?"
    mc "*Softly breathes* I feel everything as if we're in the real world right now."
    if ch2ep3showersally == 1:
        scene ch3ep3_585 with dissolve
        sally "Of course, it is! That's one of our main selling point!"
        sally "Should I tell you a big secret?"
        sally "*Giggles* You might be in the developer department, but I'm sure you don't know about it."
        mc "What secret?"
        scene ch3ep3_586 with dissolve
        mc "... Hm?"
        sally "It is so real that you can even feel... horny in here."
        scene ch3ep3_587 with dissolve
        sally "*Giggles* Alright, that's enough."
        sally "Let's just leave here and go back to the town."
        mc "...................."
        menu:
            "Hold her arm. [sally2]":
                $ ch3ep3sally_ingamesex = 1
                $ sally_relationship += 2
                $ sally_ch3_ep3 += 2
                jump ch3ep3sallysex
            "Follow her to the town.":
                $ ch3ep3sally_ingamesex = 2
                scene ch3ep3_588_d with dissolve
                mc "Okay, sure."
                scene black with dissolve
                $ renpy.pause()
                jump ch3ep3meetsally2
    else:
        sally "I know, right?"
        scene ch3ep3_588_d with dissolve
        sally "Alright, I think that's enough for today."
        sally "Let's just leave here and go back to the town."
        mc "Okay, sure."
        scene black with dissolve
        $ renpy.pause()
        jump ch3ep3meetsally2
label ch3ep3sallysex:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    play music "sfx/ep.3/ep3_8.mp3"
    $ bgm = "Johny Grimes - Double Vision"
    scene ch3ep3_588_a1 with dissolve
    sally "... Hm? What's wrong?"
    mc "Are you just going to leave like that?"
    sally "Yeah. Why?"
    mc "After just doing that to me?"
    mc "You just made me... horny."
    sally "What? I just touched you for a couple seconds..."
    scene ch3ep3_588_a2 with dissolve
    mc "Well... Looks like the feeling system is way too good."
    sally "... Then, what am I supposed to do?"
    mc "I don't know. You tell me. You're the one who started it."
    sally "......................"
    sally "... Just a little bit, okay?"
    mc "Okay..."
    scene ch3ep3_588_a3 with dissolve
    sally "*Kisses* Mhmm...."
    mc "*Kisses* Give me your tongue..."
    sally "*Kisses* Mhmm... Okay..."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_588_a4 with dissolve
    show ch3ep3_sally1
    window hide
    sally "*Sucks* Mmmmm....."
    mc "Yeah... Start it slow just like that...."
    $ renpy.pause()
    mc "Now, I want you do suck it faster."
    sally "*Sucks* Okay..."
    scene ch3ep3_588_a5 with dissolve
    hide ch3ep3_sally1
    show ch3ep3_sally2
    window hide
    mc "That's right... Keep sucking it like that."
    sally "*Sucks* Mhmmm... You're so big..."
    $ renpy.pause()
    mc "Alright, that's enough..."
    scene ch3ep3_588_a6 with dissolve
    hide ch3ep3_sally2
    mc "You acted as if you didn't want to do it, but you sucked my cock like crazy."
    sally "*Giggles* Hehe..."
    mc "But, that's only just the begining."
    mc "Let's do it for real now. Get up."
    sally "*Giggles* As you wish..."
    scene black with dissolve
    scene ch3ep3_588_a7 with dissolve
    mc "I'm going to put it in now."
    sally "Okay. I'm ready."
    scene ch3ep3_588_a8 with dissolve
    sally "*Soft moans* A-Ahh....!"
    mc "Are you alright?"
    sally "*Soft moans* Y... Yeah. Don't worry about me."
    sally "*Soft moans* Just keep continuing."
    scene ch3ep3_588_a9 with dissolve
    show ch3ep3_sally3
    window hide
    mc "Alright then..."
    sally "*Soft moans* Hahhh.... [mc]...."
    $ renpy.pause()
    scene ch3ep3_588_a10 with dissolve
    hide ch3ep3_sally3
    show ch3ep3_sally4
    window hide
    sally "*Soft moans* Arhnnng.... I can't believe it...."
    sally "*Soft moans* Mhhmmm... T... This feels.... too... real...."
    mc "*Softly breathes* I agree with you..."
    $ renpy.pause()
    scene ch3ep3_588_a11 with dissolve
    hide ch3ep3_sally4
    show ch3ep3_sally5
    window hide
    sally "*Moans* Arhhhh... I know that it's not forbidden, but..."
    sally "*Moans* I never thought that... Mhhmmm... I was going to... A-ahhh... have sex in the game..."
    mc "*Softly breathes* Then, you shouldn't have started teasing me in the first place..."
    $ renpy.pause()
    scene ch3ep3_588_a12 with dissolve
    hide ch3ep3_sally5
    mc "*Softly breathes* Turn around."
    sally "*Softly breathes* Like this...?"
    mc "Yeah... I'm going to put it in now."
    scene ch3ep3_588_a13 with dissolve
    show ch3ep3_sally6
    window hide
    sally "*Moans* Hahhh... [mc]...."
    sally "*Moans* Mhmmm... I... I'm getting there..."
    mc "*Softly breathes* Hold it for a little bit more...."
    $ renpy.pause()
    scene ch3ep3_588_a14 with dissolve
    hide ch3ep3_sally6
    show ch3ep3_sally7
    window hide
    sally "*Moans* A-Ahhh...! T-This is so good...!"
    mc "*Moans* I-If you keep fucking me like this...!"
    $ renpy.pause()
    scene ch3ep3_588_a15 with dissolve
    hide ch3ep3_sally7
    show ch3ep3_sally8
    window hide
    sally "*Loud moans* [mc]...! [mc]...!"
    mc "*Softly breathes* Yeah...?"
    sally "*Loud moans* Arhnnng... I-I'm... about to cum soon...!"
    mc "*Softly breathes* Me, too..."
    menu:
        "Slowest":
            hide ch3ep3_sally8
            jump ch3ep3sallystandbehind1
        "Slower":
            hide ch3ep3_sally8
            jump ch3ep3sallystandbehind2
        "Blowjob":
            hide ch3ep3_sally8
            jump ch3ep3sallybj1
        "Standing":
            hide ch3ep3_sally8
            jump ch3ep3sallystand1
        "Cum":
            jump ch3ep3sallycum
label ch3ep3sallybj1:
    scene ch3ep3_588_a4 with dissolve
    show ch3ep3_sally1
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ch3ep3_sally1
            jump ch3ep3sallybj2
        "Standing":
            hide ch3ep3_sally1
            jump ch3ep3sallystand1
        "Standing behind":
            hide ch3ep3_sally1
            jump ch3ep3sallystandbehind1
label ch3ep3sallybj2:
    scene ch3ep3_588_a5 with dissolve
    show ch3ep3_sally2
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ch3ep3_sally2
            jump ch3ep3sallybj1
        "Standing":
            hide ch3ep3_sally2
            jump ch3ep3sallystand1
        "Standing behind":
            hide ch3ep3_sally2
            jump ch3ep3sallystandbehind1
label ch3ep3sallystand1:
    scene ch3ep3_588_a9 with dissolve
    show ch3ep3_sally3
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ch3ep3_sally3
            jump ch3ep3sallystand2
        "Fastest":
            hide ch3ep3_sally3
            jump ch3ep3sallystand3
        "Blowjob":
            hide ch3ep3_sally3
            jump ch3ep3sallybj1
        "Standing behind":
            hide ch3ep3_sally3
            jump ch3ep3sallystandbehind1
label ch3ep3sallystand2:
    scene ch3ep3_588_a10 with dissolve
    show ch3ep3_sally4
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ch3ep3_sally4
            jump ch3ep3sallystand1
        "Faster":
            hide ch3ep3_sally4
            jump ch3ep3sallystand3
        "Blowjob":
            hide ch3ep3_sally4
            jump ch3ep3sallybj1
        "Standing behind":
            hide ch3ep3_sally4
            jump ch3ep3sallystandbehind1
label ch3ep3sallystand3:
    scene ch3ep3_588_a11 with dissolve
    show ch3ep3_sally5
    window hide
    $ renpy.pause()
    menu:
        "Slowest":
            hide ch3ep3_sally5
            jump ch3ep3sallystand1
        "Slower":
            hide ch3ep3_sally5
            jump ch3ep3sallystand2
        "Blowjob":
            hide ch3ep3_sally5
            jump ch3ep3sallybj1
        "Standing behind":
            hide ch3ep3_sally5
            jump ch3ep3sallystandbehind1
label ch3ep3sallystandbehind1:
    scene ch3ep3_588_a13 with dissolve
    show ch3ep3_sally6
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ch3ep3_sally6
            jump ch3ep3sallystandbehind2
        "Fastest":
            hide ch3ep3_sally6
            jump ch3ep3sallystandbehind3
        "Blowjob":
            hide ch3ep3_sally6
            jump ch3ep3sallybj1
        "Standing":
            hide ch3ep3_sally6
            jump ch3ep3sallystand1
label ch3ep3sallystandbehind2:
    scene ch3ep3_588_a14 with dissolve
    show ch3ep3_sally7
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ch3ep3_sally7
            jump ch3ep3sallystandbehind1
        "Faster":
            hide ch3ep3_sally7
            jump ch3ep3sallystandbehind3
        "Blowjob":
            hide ch3ep3_sally7
            jump ch3ep3sallybj1
        "Standing":
            hide ch3ep3_sally7
            jump ch3ep3sallystand1
label ch3ep3sallystandbehind3:
    scene ch3ep3_588_a15 with dissolve
    show ch3ep3_sally8
    window hide
    menu:
        "Slowest":
            hide ch3ep3_sally8
            jump ch3ep3sallystandbehind1
        "Slower":
            hide ch3ep3_sally8
            jump ch3ep3sallystandbehind2
        "Blowjob":
            hide ch3ep3_sally8
            jump ch3ep3sallybj1
        "Standing":
            hide ch3ep3_sally8
            jump ch3ep3sallystand1
        "Cum":
            jump ch3ep3sallycum
label ch3ep3sallycum:
    mc "*Softly breahtes* Ugh... I can't hold it anymore..."
    sally "*Loud moans* Me, too...!"
    menu:
        "Cum inside":
            scene ch3ep3_588_a17 with vpunch
            mc "I'm cumming...!"
            scene ch3ep3_588_a17 with vpunch
            $ renpy.pause()
            scene ch3ep3_588_a17 with vpunch
            $ renpy.pause()
        "Cum outside":
            scene ch3ep3_588_a18 with vpunch
            mc "I'm cumming...!"
            scene ch3ep3_588_a18 with vpunch
            $ renpy.pause()
            scene ch3ep3_588_a18 with vpunch
            $ renpy.pause()
    scene ch3ep3_588_a16 with vpunch
    sally "*Loud moans* I'm cumming...!!"
    scene ch3ep3_588_a16 with vpunch
    sally "*Loud moans* A-Ahhhh....!!"
    scene ch3ep3_588_a16 with vpunch
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*............."
    scene ch3ep3_588_a19 with dissolve
    sally "Alright... Are you satisfied now?"
    mc "How could you say that?"
    mc "I'm sure I wasn't the only one who enjoyed it."
    sally "*Giggles* Well... You aren't wrong about that."
    sally "Now can we leave here and get back to the town?"
    mc "Sure thing."
    stop music fadeout 3.0
    $ renpy.end_replay()
    scene black with dissolve
    $ renpy.pause()
    jump ch3ep3meetsally2
label ch3ep3meetsally2:
    s "You spent some more time in the game with [sally] before logging out...."
    scene ch3ep3_589 with dissolve
    sally "Thank you for joining me today, [mc]."
    sally "I had a good time."
    mc "Me, too. Thank you for inviting me here."
    sally "*Giggles* You're welcome."
    scene ch3ep3_590 with dissolve
    mc "Alright then, please excuse me."
    mc "I'm going to go grab some bread at the cafeteria, then go back to my department."
    sally "Oh! What a coincidence!"
    sally "I was thinking about doing that, too!"
    mc "Then, shall we go together?"
    sally "Sure. Let's go."
    scene black with dissolve
    $ renpy.pause()
    jump ch3ep3rowanmeet
label ch3ep3rowanmeet:
    play music "sfx/ep.3/ep3_4.mp3" fadein 3.0
    $ bgm = "Sarah Jansen - Moments"
    scene ch3ep3_591 with fade
    mc "Hm...?"
    mc "Isn't that [rowan]?"
    mc "I wonder what he is doing here."
    scene ch3ep3_592 with dissolve
    mc "Good afternoon, [rowan]."
    rowan "Oh. Hey, [mc]."
    rowan "I was just looking for you."
    rowan "Let's take a seat first."
    mc "Sure."
    scene ch3ep3_593 with dissolve
    mc "Okay... What is it?"
    mc "Why were you looking for me?"
    rowan "I'm here to tell you that I've already found someone to replace you."
    mc "Really? When is he going to start?"
    scene ch3ep3_594 with dissolve
    rowan "This Friday."
    mc "Okay... That means I have to stop coming here on Friday, right?"
    rowan "Well... Technically, yeah."
    rowan "But, as I told you, you can still come here any time you want."
    scene ch3ep3_595 with dissolve
    mc "I get it."
    rowan "I know It's going to be a hard time for you."
    rowan "Good luck."
    mc "Thank you so much."
    rowan "Alright, I'm leaving now. Good bye."
    mc "Good bye, [rowan]."
    jump ch3ep3unlockimage1
label ch3ep3unlockimage1:
    scene black with dissolve
    $ renpy.pause()
    $ ch3ep3special_image1 = True
    $ renpy.sound.play("sfx/alert.wav")
    s "You've unlocked special images......"
    jump ch3ep3special_image1
label ch3ep3unlockimage2:
    $ ch3ep3special_image2 = True
    jump ch3ep3special_image2
label ch3ep3unlockimage3:
    $ ch3ep3special_image3 = True
    jump ch3ep3special_image3
label ch3ep3unlockimage4:
    $ ch3ep3special_image4 = True
    jump ch3ep3special_image4
label ch3ep3unlockimage5:
    $ ch3ep3special_image5 = True
    jump ch3ep3special_image5
label ch3ep3_end:
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep3_596 with dissolve
    u "Okay, it's time to work now."
    u "Let's get back inside..."
    scene black with dissolve
    $ renpy.pause()
    s "Later that evening............"
    scene ch3ep3_597 with fade
    u "It's been a while..."
    u "Let's go to the pool and spend some time to relax for a little bit."
    scene black with dissolve
    scene ch3ep3_598 with dissolve
    u "This is perfect...."
    u "Everything has been happening so quick recently."
    u "I barely have some time alone with myself."
    unknown "[mc]!"
    u "Hm...?"
    scene ch3ep3_599 with dissolve
    rin "Good evening!"
    mc "Oh... Good evening, [rin], [yui]."
    rin "Wait... I'm sorry. Did I wake you up while sleeping?"
    mc "No, you didn't. I wasn't sleeping. I was just resting my eyes."
    scene ch3ep3_600 with dissolve
    rin "I'm relieved to hear that."
    mc "Are you guys going to swim?"
    rin "Yeah! It's been a while, but I don't want to swim alone."
    rin "So, I asked [yui] to join me."
    mc "I see..."
    scene ch3ep3_601 with dissolve
    rin "What about you? Do you want to join us?"
    mc "Thanks for inviting me, but I think I'm going to be lying up here for today."
    rin "Is that so? Alright, enjoy yourself then!"
    mc "Thanks."
    yui "Let's go, [rin]."
    scene black with dissolve
    scene ch3ep3_602 with dissolve
    u "Look at them enjoying their time."
    u "This is so satisfying to watch..."
    u "When was the last time I felt this peaceful?"
    u "These people have become important to me now."
    u "I have to do everything to protect them at all cost."
    s "*Phone vibrates*............"
    scene ch3ep3_603 with dissolve
    u "Hm...? It's [tobi]?"
    u "I wonder why he is calling."
    u "Let's pick up the call and find it out."
    scene ch3ep3_604 with dissolve
    mc "Hello, [tobi]."
    mc "Why did you call me?"
    stop music fadeout 3.0
    scene ch3ep3_605 with fade
    tobi "*Whispers* You're fucked, bro."
    tobi "*Whispers* [victor] knows that you betrayed him now."
    scene black with dissolve
    $ renpy.pause()
    hide screen smartphone
    $ episode = 11
    call screen ending

label ch3ep3special_image1:
    if _in_replay:
        scene ch3ep3special_image1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    jump ch3ep3unlockimage2
label ch3ep3special_image2:
    if _in_replay:
        scene ch3ep3special_image2 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    jump ch3ep3unlockimage3
label ch3ep3special_image3:
    if _in_replay:
        scene ch3ep3special_image3 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    jump ch3ep3unlockimage4
label ch3ep3special_image4:
    if _in_replay:
        scene ch3ep3special_image4 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    jump ch3ep3unlockimage5
label ch3ep3special_image5:
    if _in_replay:
        scene ch3ep3special_image5 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    jump ch3ep3_end
