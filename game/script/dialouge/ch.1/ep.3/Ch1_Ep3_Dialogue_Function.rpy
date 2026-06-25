define modDoBothEp3_001 = False

label Episode3:
    call mod_set_vars
    if rin_contact == False:
        $ rin_contact = True
    scene black with dissolve
    $ renpy.pause()
    scene ep3 with dissolve
    $ renpy.pause(3,hard=True)
    scene black with dissolve
    $ renpy.pause()
    scene ep3_1 with fade
    show screen smartphone
    unknown "Great. You've never let me down, [mc]."
    unknown "I made the right decision when I chose you to do this job."
    mc "....Thank you, sir."
    mc "By the way, I'd like to tell you that the code I just sent to you, is still in development."
    mc "I wanted to wait until they tested it again, and confirm that it works perfectly fine."
    scene ep3_2 with dissolve
    mc "But, since you wanted it now...."
    unknown "I know that."
    mc "Hm? How did you know about that?"
    unknown "........"
    scene ep3_3 with dissolve
    air "Do you want me to refill your glass of wine, sir?"
    alex "Yes, please."
    air "Is there anything else that you want?"
    alex "Then, I'll have to ask what you can do for me?"
    air "Well... I know some people feel stressed during the flight..."
    air "I can offer my service to help you reduce your stress..."
    alex "Hm...? That sounds really interesting...."
    scene ep3_2 with dissolve
    unknown "Let's say you don't have to worry about that."
    unknown "For now, you just need to keep acting as if you were a normal employee, and keep trying to blend in with them."
    unknown "Understood?"
    mc "Yes, sir."
    scene ep3_4 with dissolve
    unknown "Great. I have to hang up now. I'll talk to you later."
    mila "........"
    unknown "Okay."
    scene ep3_5 with dissolve
    mila "Who was on the phone, grandfather?"
    unknown "Hm?"
    mila "Was that [mc]?"
    scene ep3_6 with dissolve
    unknown "Yes, it was him."
    mila "Why did he call you?"
    unknown "He just sent me the code of Xecon Gear, so he called me to tell me about that."
    scene ep3_5 with dissolve
    mila "Oh? So, you almost got what you wanted then."
    unknown "Yeah, seems so..."
    scene ep3_6 with dissolve
    mila "Congrats, grandfather."
    unknown "You don't need to say such a thing like that. It's obvious that I was going to get it someday."
    victor "There is nothing in the world that this old man, [victor], can't achieve!"
    scene ep3_3 with dissolve
    alex "Wait for me in the toilet, okay?"
    air "*Winks*...Roger that..."
    scene ep3_7 with dissolve
    alex "What were you guys talking about?"
    alex "I heard you mentioning [mc]. What's going on?"
    alex "Is he coming back soon?"
    scene ep3_8 with dissolve
    mila "That's none of your concern...."
    mila "And who do you think you are to talk to me like that?"
    alex "Oh... I'm sorry, young master. I was just excited to hear about him."
    mila "You better prepare for the incoming meeting."
    alex "Understood."
    scene ep3_9 with dissolve
    mila "([mc].....)"
    mila "(He's been out there for too long... {w}When was the last time we saw each other?)"
    mila "(I wonder what he looks like now....)"
    mila "(*Giggles*...I can't wait to meet him again...)"
    scene black with dissolve
    $ renpy.pause()
    if sexwithrin == 1:
        jump ep3_gotmessage
    elif sexwithrin == 0 or sexwithrin == 2:
        jump ep3_checkcode

label ep3_gotmessage:
    $ ep3_rinmessage1 = True
    $ newmessage = True
    $ rin_messages_show = True
    $ rin_newmessage = True
    $ phone_alert = True
    scene ep3_10 with fade
    u "Hm...?"
    u "Did I just get a new message while I was on the phone?"
    u "I wonder who sent it to me."
    u "Let me check..."
    jump messagefromrin
label messagefromrin:
    if reply_rin1 == False:
        scene ep3_10 with vpunch
        u "I need to reply the message first!"
        jump messagefromrin
    elif reply_rin1 == True:
        jump ep3_afterreplytorin
label ep3_afterreplytorin:
    if rin_reply1_choice == 1:
        jump ep3_watchtv
    elif rin_reply1_choice == 2:
        stop music fadeout 3.0
        jump ep3_checkcode
label ep3_watchtv:
    scene ep3_10_a1 with dissolve
    u "The outfit I'm wearing now, isn't very comfortable."
    u "Let me change my outfit into something more flexible first..."
    scene black with dissolve
    stop music fadeout 3.0
    s "*Five minutes later*...."
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    scene ep3_10_a2 with dissolve
    u "Hm? Didn't she just say that she'd be waiting for me here?"
    u "Where has she gone...?"
    u "Well, let's go sit on the sofa right there, and wait for her..."
    u "She maybe in the bath-"
    scene ep3_10_a3 with vpunch
    rin "Surpriseeee!!"
    mc "........"
    mc "What are you doing?"
    rin "S..Surprise...."
    mc "........"
    scene ep3_10_a4 at eyesblink("Ch.1/Ep.3/Scenes/ep3_10_a4.jpg", "Ch.1/Ep.3/Scenes/ep3_10_a4_blink.jpg", 1) with dissolve
    rin "Jeez... Can you just at least pretend to be startled?"
    mc "You would have to do something more unexpected then..."
    rin "I'll think about that then."
    scene ep3_10_a5 with dissolve
    mc "Let's go to the sofa."
    rin "Wait. I want to ask you something."
    mc "Hm? What do you want to know?"
    scene ep3_10_a4 at eyesblink("Ch.1/Ep.3/Scenes/ep3_10_a4.jpg", "Ch.1/Ep.3/Scenes/ep3_10_a4_blink.jpg", 1) with dissolve
    rin "I know that you're quite different from the others..."
    rin "But, you didn't seem to be happy that I just hugged you."
    rin "So, I kind of was wondering if you liked it, or if shouldn't have done that in the first place..."
    mc "....Well."
    mc "I would've pushed you away if I didn't like it."
    rin "........"
    mc "I don't understand why you were so afraid that I wouldn't like your hug."
    mc "We even did something more than that last night..."
    scene ep3_10_a7 at eyesblink("Ch.1/Ep.3/Scenes/ep3_10_a7.jpg", "Ch.1/Ep.3/Scenes/ep3_10_a7_blink.jpg", 1) with dissolve
    rin "....Why did you have to mention what we did yesterday?"
    mc "Hm? What's the problem?"
    mc "I just want you to know that I didn't dislike you hugging me from behind."
    rin "It's just...."
    scene ep3_10_a6 at eyesblink("Ch.1/Ep.3/Scenes/ep3_10_a6.jpg", "Ch.1/Ep.3/Scenes/ep3_10_a6_blink.jpg", 1) with dissolve
    rin "I don't know..."
    rin "Yes, we did it together last night, and I was very happy to do it with you."
    rin "But, after thinking about it again, I thought we went a little bit too fast."
    rin "I don't want you to think that I'm such an easy girl..."
    rin "I mean... We haven't even done the first thing people usually do before it leads them into having sex."
    mc "The first thing people usually do?"
    scene ep3_10_a7 at eyesblink("Ch.1/Ep.3/Scenes/ep3_10_a7.jpg", "Ch.1/Ep.3/Scenes/ep3_10_a7_blink.jpg", 1) with dissolve
    rin "Yeah, you know that...."
    mc "Do you mean kiss?"
    rin "...Yeah. So, I'd like to slow things between us down for a bit."
    mc "I see... I don't have a problem with that at all."
    u "I mean... I don't even know if I should be doing this...."
    rin "By the way, since we've already talked about it, can we...."
    rin "....Kiss?"
    menu:
        "Kiss her [rin1]":
            $ ep3_kiss_rin = 1
            $ rin_relationship += 1
            $ rin_ch1_ep3 += 1
            jump ep3_kissrin
        "No, we can't":
            $ ep3_kiss_rin = 2
            mc "No, we can't."
            scene ep3_10_a7_refuse with dissolve
            rin ".....Okay."
            mc "I don't think we should do it here. Someone might see us."
            rin "Yeah, you're right..."
            mc "Then, let's go watch TV."
            rin "No. I think I want to go back to my room now."
            rin "Goodnight, [mc]."
            mc "Oh...."
            scene black with dissolve
            stop music fadeout 3.0
            s "*[rin] has left the room*...."
            jump ep3_beforebedtime
label ep3_kissrin:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    mc "Alright, let's do it."
    scene ep3_10_a7_kiss1 at eyesblink("Ch.1/Ep.3/Scenes/ep3_10_a7_kiss1.jpg", "Ch.1/Ep.3/Scenes/ep3_10_a7_kiss1_blink.jpg", 1) with dissolve
    rin "Really? You aren't kidding me, right?"
    mc "No, I'm not. Why would I do that?"
    rin "*Giggles*...Okay then..."
    scene black with dissolve
    s "[rin] starts moving her face closer to yours...."
    scene ep3_10_a7_kiss2 with dissolve
    rin "*Kisses*....Mmmmm...."
    rin "*Kisses*....Am I doing it right?"
    mc "*Kisses*....Yes, you are...."
    rin "*Kisses*...This feels a lot different than I thought, but it feels really good..."
    scene black with dissolve
    s "Both of you keep kissing for a little bit longer...."
    scene ep3_10_a7_kiss3 with dissolve
    rin "*Softly breathes*....[mc]."
    mc "Hm...?"
    rin "What are we now?"
    mc "...What do you think?"
    u "....Is it really okay for me to do this...?"
    rin "I don't think we're just friends, but we're not a couple either..."
    rin "We haven't even started dating yet."
    rin "Umm... How about close friends? Let's be close friends for now!"
    $ rin_relationship_status = "Close friend"
    mc "If you say so..."
    rin "*Giggles*...Don't be so sad! Just for now! We can be whatever you want after we know each other better!"
    mc "Whatever I want?"
    rin "Yes, whatever you want!"
    rin "Alright... Now let's go watch TV!"
    $ renpy.end_replay()
    scene black with dissolve
    $ renpy.pause()
    scene ep3_10_a8 with dissolve
    rin "What should we watch today?"
    mc "How about the show we watched last night. Let's finish the first season today."
    rin "Okay. That sounds good to me."
    scene ep3_10_a9 with dissolve
    s "[rin] and you spend time watching the series together...."
    scene ep3_10_a10 with dissolve
    u "Hm...? Did she just move closer to me?"
    rin "........."
    u "Was it the sign of her wanting me to put my arm around her?"
    u "What should I do?"
    menu:
        "Do it [rin1]":
            $ rin_relationship += 1
            $ rin_ch1_ep3 += 1
            $ ep3_armonrin = 1
            scene ep3_10_a10_hold with dissolve
            rin "*Giggles*...Hehe..."
            u "Yeah, she surely likes it."
        "Don't do it":
            $ ep3_armonrin = 2
            rin "........"
            u "...What? Why is it suddenly cold here...?"
    scene black with dissolve
    s "*A few hours later*......"
    scene ep3_11 with dissolve
    mc "I think that'd be enough for today. It's getting late."
    mc "I have something else to do before going to bed."
    rin "Okay then, I won't hold you here any longer."
    rin "See you tomorrow!"
    mc "See you."
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    jump ep3_beforebedtime
label ep3_beforebedtime:
    play music "sfx/ep.3/ep3_2.mp3" fadein 3.0
    $ bgm = "Pyrosion - Dreamer"
    scene ep3_12 with dissolve
    if ep3_kiss_rin == 1:
        u "Alright, I had enough fun. Now it's time to get back to work."
        u "Let's turn on the computer, and look at the code of Xecon Gear. I need to learn it."
    elif ep3_kiss_rin == 2:
        u "Seems like I just disappointed her..."
        u "But I think I did well, I didn't come here to make friends, or find a girlfriend anyway..."
        u "Let's turn on the computer, and look at the code of Xecon Gear. I need to learn it."
    scene ep3_13 with dissolve
    u "...This is something I've never seen before..."
    u "The company's president was surely a genius to successfully create such a crazy thing like Xecon Gear."
    u "[liam] is also a genius, too. I'm not sure if I could write this code on my own..."
    scene black with dissolve
    s "You spend your time looking, and trying to learn the code..."
    scene ep3_14 with dissolve
    $ ep3_rinmessage2 = True
    $ newmessage = True
    $ rin_messages_show = True
    $ rin_newmessage = True
    $ phone_alert = True
    u "Hm? It's midnight already?"
    u "...Time surely files by so fast..."
    u "It's time to sleep. Let's turn off the computer."
    scene ep3_15 with dissolve
    $ renpy.pause()
    jump ep3_krystalatkitchen
label ep3_checkcode:
    play music "sfx/ep.3/ep3_2.mp3" fadein 3.0
    $ bgm = "Pyrosion - Dreamer"
    scene ep3_10_d1 with dissolve
    u "Alright, let's look at the code of Xecon Gear. I need to learn about it."
    u ".........."
    u "...This is something I've never seen before..."
    u "The company's president is surely a genius to created such a crazy thing like Xecon Gear."
    u "[liam] is also a genius, too. I'm not sure if I could write this code on my own..."
    scene black with dissolve
    s "You spend your time looking, and trying to learn about the code..."
    scene ep3_10_d2 with dissolve
    u "Hm? It's already this late?"
    u "...Time surely files so fast..."
    u "It's time to sleep, but I'm kind of sweaty..."
    u "Let's take a quick shower first."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_10_d3 with dissolve
    u "Alright, let's go to bed..."
label ep3_krystalatkitchen:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_16 with dissolve
    u "........."
    u "I can't sleep... I'm thirsty..."
    u "Let's go to the kitchen and get some water..."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_17 with fade
    u "This is usually the time for [krystal] to have dinner."
    u "I wonder if she's in the kitchen right now...."
    stop music fadeout 3.0
    scene ep3_18 with dissolve
    play music "sfx/ep.3/ep3_3.mp3" fadein 3.0
    $ bgm = "Jay Someday - Rewind"
    u "Oh yeah, she is...."
    u "What is she doing right there?"
    u "Anyway, let's just get inside first..."
    scene ep3_19 with dissolve
    krystal "Hm...?"
    scene ep3_20 with dissolve
    krystal "What's up, [mc]. How are you?"
    mc "I'm good, and you?"
    krystal "I'm okay. Thanks for asking."
    mc "You seem so calm to see me coming here today."
    krystal "Well, because I know if someone's going to come here at this time, it has to be you."
    mc "I see..."
    krystal "Did you come to find something to eat again?"
    scene ep3_21 with dissolve
    mc "No. I'm just going to drink some water."
    krystal "Oh? I thought you were a late-night eater. Seems like I was wrong."
    mc "Yeah, I'm not a late-night eater."
    mc "By the way, what happened?"
    krystal "What do you mean?"
    mc "Why am I feeling like you look a little bit different today."
    scene ep3_22 with dissolve
    krystal "Hehhh~"
    krystal "To be honest I didn't expect you to notice that."
    krystal "Yeah, you're right. I just finished taking a shower, so I haven't fixed my hair yet."
    mc "Oh.... That's why..."
    if Krystalintoilet == True:
        krystal "You also noticed that I didn't wear make up last night..."
        krystal "You're really observant, aren't you?"
    elif Krystalintoilet == False:
        krystal "You're quite observant, aren't you?"
    mc "Am I?"
    krystal "Yes, you are."
    mc "By the way, what were you doing? {w}I saw you standing still doing nothing just before I came in."
    scene ep3_23 with dissolve
    krystal "Oh, I was just waiting for my ramyun to boil up!"
    mc "Ramyun?"
    krystal "Yeah, it's an instant noodle just like ramen, but it's from Korea."
    mc "I see..."
    krystal "Do you want to try it? I can share it with you."
    scene ep3_24 with dissolve
    krystal "Oh, I'm sorry! I shouldn't have asked you that."
    krystal "I completely forgot that you aren't a late-night eater."
    u "I wasn't really hungry before, but the smell...."
    u "It's making me hungry again. What should I do?"
    menu:
        "Let's try [krystal1]":
            $ krystal_relationship += 1
            $ krystal_ch1_ep3 += 1
            $ ep3_latedinner = 1
            scene ep3_24_a1 with dissolve
            mc "I want to try it."
            jump ep3_tryramyun
        "Stick with the reason why you're here":
            $ ep3_latedinner = 2
            scene ep3_24_d1 with dissolve
            mc "No, thanks."
            mc "I came here for some water."
            jump ep3_notryramyun
label ep3_tryramyun:
    krystal "*Giggles*...What did you just say?"
    mc "...I want to try it."
    krystal "*Giggles*...Didn't you just come here for some water?"
    mc "........."
    mc "Are you going to let me taste it or not...?"
    krystal "*Giggles*...Chill out! Don't be so mad. I was just kidding!"
    mc "I wasn't mad..."
    krystal "Alright, you better go take a seat and wait for me. {w}I'll serve you a bowl of ramyun once it's ready!"
    scene black with dissolve
    s "*Half an hour later*......"
    scene ep3_24_a2 with dissolve
    krystal "*Sigh*...I'm so full~"
    mc "So am I...."
    krystal "So, what do you think? Was it delicious?"
    krystal "I didn't have a chance to ask you, because you didn't stop eating until you ate it all."
    scene ep3_24_a3 with dissolve
    krystal "*Giggles*...Even though the way you eat already told me the answer, I'd prefer to hear it from your mouth!"
    mc "Yeah, it was very delicious."
    krystal "That's it?"
    mc "What do you want me to say?"
    krystal "How about you tell me what made you think it was delicious?"
    mc "........."
    mc "I like how the noodle was very thick, but soft at the same time. It's very different from what I've tried before."
    mc "The soup was quite spicy, but it's fine by me because I like spicy food."
    mc "Also, it tasted a little sweet which combined with the spicy taste pretty well. So, it was delicious overall."
    krystal "Hmm... I'm glad to know that we have something in common now. I also like spicy food as well."
    mc "You do?"
    scene black with dissolve
    s "You spend your time talking with [krystal] for a little bit longer..."
    scene ep3_24_a4 with dissolve
    krystal "You don't really have to do this. I can wash them by myself."
    mc "You shared your food with me, but I have nothing to give back to you. This is the least I can do."
    mc "So, let me do it."
    krystal "*Giggles*...Okay then!"
    scene ep3_24_a5 with dissolve
    mc "Alright, they're all clean now..."
    mc "...Hm?"
    krystal "Can I have your phone number?"
    mc "Why do you want it?"
    krystal "You seem like a good person. I want to spend time with you again."
    krystal "It will be easier for us to talk if we have each other's phone numbers."
    mc "........"
    menu:
        "Give [krystal2]":
            scene ep3_24_a5_give with dissolve
            $ krystal_contact = True
            $ ep3_givephonenumber = 1
            $ krystal_relationship += 2
            $ krystal_ch1_ep3 += 2
            mc "Okay then, I'll give you my phone number."
            krystal "*Giggles*...Thanks!"
            krystal "I'll text you when I want to hang out!"
            jump ep3_sleep
        "Don't give":
            s "If you don't give her your phone number, it means that you aren't interested in [krystal]."
            s "This choice will end up with the result of you not seeing her again in the future."
            s "Are you sure that you don't want to give her your phone number?"
            menu:
                "Yes, I am.":
                    scene ep3_24_a5_nogive with dissolve
                    $ ep3_givephonenumber = 2
                    mc "Look. I'm very glad to meet you, but I didn't come here to make friends."
                    mc "So, I don't have a choice, but to say no."
                    mc "I really enjoyed the moments we shared together, but that's it."
                    mc "I don't want us to improve our relationship."
                    krystal ".....Okay. I get it."
                    krystal "I'm sorry to think that we could be friends..."
                    jump ep3_sleep
                "On a second thought... [krystal2]":
                    scene ep3_24_a5_give with dissolve
                    $ krystal_contact = True
                    $ ep3_givephonenumber = 1
                    $ krystal_relationship += 2
                    $ krystal_ch1_ep3 += 2
                    mc "Okay then, I'll give you my phone number."
                    krystal "*Giggles*...Thanks!"
                    krystal "I'll text you when I want to hang out!"
                    jump ep3_sleep
label ep3_notryramyun:
    krystal "Are you sure that you don't want to try it?"
    mc "Yes, I am."
    krystal "Okay then, I won't force you to try it. I respect your decision."
    scene black with dissolve
    s "You drink a glass of water...."
    scene ep3_24_d2 with dissolve
    krystal "Are you leaving already?"
    mc "Yes, I am. It's already late. I have to go to bed."
    krystal "Gotta wake up in the morning to go to work, huh?"
    mc "Yeah, you guessed right."
    scene ep3_24_d3 with dissolve
    mc "...Hm?"
    krystal "By the way, can I have your phone number?"
    mc "Why do you want it?"
    krystal "You seem like a good person. I want to spend time with you again."
    krystal "It will be easier for us to talk if we have each other's phone numbers."
    mc "........"
    menu:
        "Give [krystal2]":
            scene ep3_24_d3_give with dissolve
            $ krystal_contact = True
            $ ep3_givephonenumber = 1
            $ krystal_relationship += 2
            $ krystal_ch1_ep3 += 2
            mc "Okay then, I'll give you my phone number."
            krystal "*Giggles*...Thanks!"
            krystal "I'll text you when I want to hang out!"
            jump ep3_sleep
        "Don't give":
            s "If you don't give her your phone number, it means that you aren't interested in [krystal]."
            s "This choice will end up with the result of you not seeing her again in the future."
            s "Are you sure that you don't want to give her your phone number?"
            menu:
                "Yes, I am.":
                    scene ep3_24_d3_nogive with dissolve
                    $ ep3_givephonenumber = 2
                    mc "Look. I'm very glad to meet you, but I didn't come here to make friends."
                    mc "So, I don't have a choice, but to say no."
                    mc "I really enjoyed the moments we shared together, but that's it."
                    mc "I don't want us to improve our relationship."
                    krystal ".....Okay. I get it."
                    krystal "I'm sorry to think that we could be friends..."
                    jump ep3_sleep
                "On a second thought... [krystal2]":
                    scene ep3_24_a5_give with dissolve
                    $ krystal_contact = True
                    $ ep3_givephonenumber = 1
                    $ krystal_relationship += 2
                    $ krystal_ch1_ep3 += 2
                    mc "Okay then, I'll give you my phone number."
                    krystal "*Giggles*...Thanks!"
                    krystal "I'll text you when I want to hang out!"
                    jump ep3_sleep
label ep3_sleep:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_10_d3 with dissolve
    u "Alright, it's time to sleep...."
    scene black with dissolve
    $ renpy.pause()
    if sexwithrin == 1:
        jump ep3_dream
    elif sexwithrin == 0 or sexwithrin == 2:
        scene ep3_27 with dissolve
        $ renpy.sound.play("sfx/Clock alarm.mp3")
        s "*Alarm sounds*....."
        scene ep3_28 with dissolve
        u "...Let's get up, and take a shower..."
        stop sound
        jump ep3_breakfast
label ep3_dream:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    scene black with dissolve
    $ renpy.pause()
    scene ep3_10_d3 with dissolve
    u "Alright, it's time to sleep...."
    scene black with dissolve
    $ renpy.pause()
    show rin_dreambj with dissolve
    rin "*Sucks*...Mmmmm...."
    u "....What the...?"
    mc "[rin]? What are you doing?"
    hide rin_dreambj with dissolve
    scene ep3_25 with dissolve
    rin "Oh... Now, you finally wake up."
    rin "But what kind of question was that, silly?"
    rin "*Giggles*...It's very obvious that I'm sucking your cock!"
    mc "...Yeah, you're right. It was very obvious..."
    rin "Okay, you've got your answer. Now, I'll get back to my business here."
    scene black with dissolve
    show rin_dreambj with dissolve
    rin "*Sucks*...Mmmmm.... I never knew your cock tasted this good...."
    rin "*Sucks*...Mmmmm... Only if I'd known it was this good, I would've sucked it already since the last time we enjoyed our moments together..."
    mc "....But, didn't you just tell me that you wanted to slow down things between us?"
    rin "*Sucks*....Mmmm.... Yes, I did...."
    mc "...Then why...?"
    $ renpy.pause()
    hide rin_dreambj with dissolve
    show rin_dreamfj with dissolve
    rin "*Giggles*...The reason is actually quite simple... It's because I'm so horny right now...!"
    rin "*Giggles*....This is my first time giving someone a foot job... It's actually a lot funnier than I thought!"
    rin "*Giggles*....I'm doing good, right? You're enjoying your foot job, right?"
    $ renpy.pause()
    mc "....Yes, I am...."
    hide rin_dreamfj with dissolve
    scene ep3_26 with dissolve
    rin "*Giggles*....Alright.... Now, it's time for you to...."
    mc "To?"
    rin "*Giggles*....{b}Wake up, and get to work!{/b}"
    scene ep3_27 with dissolve
    $ renpy.sound.play("sfx/Clock alarm.mp3")
    s "*Alarm sounds*....."
    u "..........."
    u "That was a dream....?"
    stop sound
    scene ep3_28 with dissolve
    u ".........."
    u "Why did I dream about [rin] doing something like that?"
    u "Well, dreams are basically stories and images that our mind creates while we sleep."
    u "Does it mean...I wanted to do something like that with her again?"
    u "....I don't know...."
    u "...To be honest, I don't even know why I chose to improve my relationship with her in the first place..."
    u "*Sigh*...Let's just forget about it. I better get up, and take a shower."
    $ renpy.end_replay()
    jump ep3_breakfast
label ep3_breakfast:
    scene black with dissolve
    $ renpy.pause()
    s "After you finished taking a shower, you decided to head to the kitchen..."
    scene ep3_29 with fade
    u "Hm...That's [yui]."
    u "She's also heading to have breakfast, as well."
    u "Should I greet her?"
    menu:
        "Do it [yui1]":
            $ yui_ch1_ep3 += 1
            $ yui_relationship += 1
            $ ep3_yuigreet = 1
            u "She's already changed her attitude towards me. So, why not?"
            u "Let's just do it."
            scene ep3_29_yuigreet with dissolve
            mc "Good morning, [yui]."
            yui "Hm...?"
            yui "Oh... Good morning, [mc]."
            mc "Did you sleep well?"
            yui "Yes, I did..... And you?"
            mc "....Me, too"
        "Don't do it":
            $ ep3_yuigreet = 2
            u "No, I don't want to do it."
            u "Even though she said she would try to be nice to me, she's still far from liking me."
            u "So, I think it's better for me to not get involved with her."
            u "I'll just follow her quietly..."
    scene black with dissolve
    $ renpy.pause(0.3,hard=True)
    scene ep3_30 with dissolve
    zeke "I was very sad that you didn't wake up to have breakfast yesterday."
    zeke "But it's okay since you're here now. Here is your coffee!"
    mika "*Giggles*...Thank you."
    zeke "I'll tell you what. I may not know how to cook, but when it comes to making a coffee, I'm the best in this house!"
    mika "*Giggles*...Are you sure about that?"
    zeke "Just try it! I'm sure you'll love it."
    s "*Footsteps coming*......"
    scene ep3_31 with dissolve
    rin "...Hm?"
    rin "Good morning, guys!"
    zeke "What's up, guys!"
    if ep3_yuigreet == 1:
        scene ep3_31_yuigreet with dissolve
        yui "Good morning."
        mc "Hi, everyone."
    if ep3_yuigreet == 2:
        yui "Guys?"
        zeke "Yeah, you and [mc]."
        scene ep3_31_yuinogreet with dissolve
        yui "W-What?! Since when were you behind me?"
        mc "I followed you since we were at the living room..."
        yui "*Sigh*...You should've let me know...."
    zeke "Come in. Come in. Let's have breakfast!"
    yui "Sure."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_32 with dissolve
    yui "[rin]."
    rin "Hm?"
    yui "Who is this woman? I've never seen her before."
    yui "Are you really not going to introduce her to me?"
    scene ep3_33 with dissolve
    zeke "Oh, I'm sorry! It's my bad."
    zeke "I thought you've already met her."
    zeke "She is my friend, [mika]!"
    mika "Hi. I'm [mika]. Nice to meet you."
    mika "You're [yui], right?"
    scene ep3_32 with dissolve
    yui "Do you know me?"
    mika "Yes. [zeke] already told me about everyone in this house."
    yui "Oh...."
    mika "You must be curious why I am here, right?"
    yui "To be honest... Yes, I am."
    yui "But you don't have to tell me about that if you don't feel uncomfortable telling me."
    mika "....Thank you."
    scene ep3_33 with dissolve
    zeke "Let's say she needs to stay here for a while until she can find a new place to live."
    mika "Yeah, that's right..."
    mika "But if you guys are uncomfortable with me being here, you can tell me now."
    mika "I'll just leave. I don't want to bother you guys."
    rin "No, we aren't. You can stay here as long as you want. Am I right, guys?"
    yui "Yeah, I don't have problem with that..."
    scene ep3_34 with dissolve
    mc "I thought she already left... I didn't see you guys last night."
    zeke "Well, it's because I took her to the cinema last night and came back here around 11 p.m."
    zeke "You guys were in your room already by that time."
    mc "...But, I didn't see you sleeping on the sofa in the hallway when I came here to get some water at midnight."
    mc "Where did you sleep last night?"
    zeke "Oh, it's because I slept in my room!"
    mc "..........."
    scene ep3_35 with dissolve
    zeke "No! Don't look at me like that! It's not what you think!"
    zeke "I let her sleep on my bed while I slept on the floor."
    zeke "I didn't do anything to her!"
    mc "....I didn't even say anything."
    mika "*Giggles*....What did you think? Your face has turned red, [zeke]."
    zeke "L-Let's just stop talking about that, and finish our breakfast!"
    scene ep3_32 with dissolve
    zeke "We need to leave a bit earlier, because [mika] will come with us, too."
    yui "Hm? Why?"
    zeke "She needs to pick up her stuff at her old place."
    zeke "It's on the way to the company, so I'll drop her off when we go to work."
    yui "Okay..."
    jump ep3_office
label ep3_office:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_36 with fade
    rin "Alright, guys... Have a good day!"
    rin "I'll be heading to my department now."
    zeke "Me, too. See you afterwork, guys!"
    yui "Okay."
    if ep3_kiss_rin == 1:
        scene ep3_37 with dissolve
        $ renpy.pause(0.2,hard=True)
        scene ep3_37_1 with dissolve
        rin "See you later, [mc]!"
        mc "Sure."
        rin "*Giggles*...Hehe..."
        scene ep3_38 with dissolve
        yui "........."
        mc "...What?"
        yui "...What was that? Did she just wink at you?"
        mc "...I don't know."
        yui "What's going on between you guys?"
        mc "It's ten to nine. Let's go to our department...."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_39 with dissolve
    stop music fadeout 3.0
    s "After working for a while...."
    scene ep3_40 with dissolve
    play music "sfx/ep.3/ep3_2.mp3" fadein 3.0
    $ bgm = "Pyrosion - Dreamer"
    pete "[mc]."
    u "...Hm?"
    scene ep3_41 with dissolve
    mc "Yes?"
    mc "Is there something that you want from me?"
    pete "Can you follow me to my office?"
    mc "....Sure."
    scene ep3_42 with dissolve
    u "Why did he ask me to do that?"
    u "Could it be that... He knows what I did...?"
    u "No, I don't think that's the case."
    u "I'm pretty sure that I deleted all the evidence..."
    u "Let's just follow him, and see what his deal is."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_43 with dissolve
    pete "So... This is our first time talking in private, right?"
    mc "Yes, it is."
    pete "Well... After you've been working here for about a week, I'd like to know your thoughts."
    pete "Do you like this company? Is everything okay?"
    u "........."
    scene ep3_44 with dissolve
    mc "Yes, I do. I like working here."
    mc "Also, everyone is so nice to me despite the fact that I'm not a talkative person."
    mc "So, I guess it's safe to say that everything is okay."
    pete "Great. I'm glad to hear that."
    scene ep3_45 with dissolve
    mc "...Was that question the reason why you brought me here?"
    pete "No, it wasn't."
    pete "Actually, I brought you here to give you a compliment."
    mc "........."
    pete "Usually, [liam] was the one who was generally responsible for checking codes, and bugs in the game to see if everything worked perfectly fine."
    pete "But, I know that you've been working in his place after he's been busy updating codes for Xecon Gear."
    pete "And, you've been doing a very good job. So, I really appreciated that."
    scene ep3_44 with dissolve
    mc "Well, I just did what I had to..."
    pete "Come on. Just accept the praise."
    pete "You may not realise it, but [liam] has been able to work without having to worry about anything because of you."
    mc "...Okay then, thank you."
    scene ep3_46 with dissolve
    pete "Also, I also want to let you know that you're going to attend today's meeting with me."
    mc "Hm? What meeting?"
    pete "A meeting between our president, and the heads of departments who are responsible for this project."
    mc "Am I allowed to be there?"
    pete "Don't worry. As the heads of departments, we're allowed to bring one of the employees in our own department to be the assistant in the meeting."
    mc "...I get it."
    scene ep3_47 with dissolve
    mc "But, why me?"
    mc "Why don't you bring [liam] or other people there instead of me?"
    pete "Good question...."
    pete "Of course, it makes a lot more sense for me to bring one of them there instead of you, because you're basically a new employee."
    scene ep3_48 with dissolve
    pete "But, I see a lot of potential in you."
    pete "I'm pretty sure that you will become one of the best employees soon."
    u "...I doubt that..."
    pete "So, I'd like you to have a chance to attend the meeting, and get involved with poeple who're going to be there."
    pete "I'm sure it will help you learn, and experience plenty of new things."
    mc "...Okay, I get it."
    pete "Lovely. Then, we'll meet again at 12.45 p.m. after you have lunch."
    mc "Sure."
    scene black with dissolve
    stop music fadeout 3.0
    s "*Time flies*......"
    scene ep3_49 with dissolve
    play music "sfx/ep.3/ep3_4.mp3" fadein 3.0
    $ bgm = "Sarah Jansen - Moments"
    pete "Alright, are you ready?"
    mc "Yes, I am."
    pete "Then, let's not waste anymore time here. The meeting will be starting soon."
    mc "Okay."
    scene ep3_50 with dissolve
    pete "Don't be too nervous, okay?"
    mc "Hm?"
    pete "I remember the first time that I took [joe] to the meeting with me."
    pete "He was so nervous that he passed out when we saw our president for the first time!"
    pete "Our president is a very nice person, so you don't have to be afraid of him."
    mc "Understood."
    if eiraatcafeteria == False:
        scene ep3_51 with dissolve
        s "*Door is closing*....."
        unknown "Wait, please!"
        u "...Hm?"
        scene ep3_52 with dissolve
        eira "Please, wait for me..."
        u "What should I do?"
        menu:
            "Wait for her [eira1]":
                $ ep3_waiteira = 1
                $ eira_relationship += 1
                $ eira_ch1_ep3 += 1
                scene ep3_52_wait1 with dissolve
                mc "........."
                scene ep3_52_wait2 with dissolve
                eira "*Softly breathes*......."
                eira ".....Thank you."
                mc "You're welcome."
                pete "Good afternoon, [eira]."
                eira ".....Good afternoon."
                scene ep3_52_wait3 with dissolve
                s "While the elevator is going up, none of you is saying anything..."
                jump ep3_companymeeting
            "Ignore her":
                $ ep3_waiteira = 2
                scene ep3_52_ignore with dissolve
                eira "........."
                jump ep3_companymeeting
    elif eiraatcafeteria == True:
        jump ep3_companymeeting
label ep3_companymeeting:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_53 with fade
    pete "Good afternoon, everyone!"
    eira ".........."
    scene ep3_54 with dissolve
    unknown "Good afternoon, [pete]."
    pete "...[sandra]? Are you here, too?"
    sandra "Hehe... Yeah. What a surprise, right?"
    sandra "[faye] told me to come here, so..."
    pete "Yeah?.... But, why?"
    faye "Just take a seat. You'll find it out soon."
    pete "Alright."
    scene ep3_55 with dissolve
    pete "You sit here, [mc]."
    mc "Okay."
    scene ep3_56 with dissolve
    pete "Did you sleep well last night, [sandra]?"
    sandra "Yes, I did."
    pete "Then, are you better now?"
    pete "You didn't look so good yesterday."
    scene ep3_57 with dissolve
    sandra "Well, after I woke up in the morning, I didn't feel sick anymore."
    sandra "So yeah, I think I'm better now."
    pete "Alright, I'm glad to hear that."
    faye "Jeez... You guys do realise that you aren't here alone, right?"
    faye "So, stop flirting with each other, please."
    pete "We aren't flirting! She's my friend!"
    sandra "*Speaks at the same time*... We aren't flirting! He's my friend!"
    faye "*Sighs*....Whatever."
    s "*Footsteps coming*......."
    scene ep3_58 with dissolve
    u "...Hm?"
    u "...There he is..."
    scene ep3_59 with dissolve
    rowan "Oh? Everyone is here already?"
    rowan "Good afternoon, guys!"
    u "Well, considering from the last time I saw him, he doesn't look so much different."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_60 with dissolve
    rowan "Alright, are you guys ready?"
    rowan "Shall we start now?"
    faye "Yes, I think so. Let's get started."
    scene ep3_61 with dissolve
    rowan "Well, I just met with the investors this morning."
    rowan "They were so eager to see our project announced to public."
    rowan "So, they asked me if we could finish the project faster."
    rowan "I know that it's going to be more work for you guys, but I also understand their perspectives."
    rowan "You know... We wouldn't be where we are now without any of them."
    faye "Yes. I couldn't agree more."
    scene ep3_62 with dissolve
    rowan "So, how is everything going in your department, [pete]?"
    rowan "How far are you guys from being successful in updating codes for the completed version of Xecon Gear?"
    scene ep3_63 with dissolve
    pete "Well, last time I talked with [liam] who's responsible for doing that, was yesterday."
    pete "He said that he expected everything to be finished within a week."
    pete "At first, he thought that he would need more time than that due to another project he was responsible for."
    scene ep3_63_1 with dissolve
    pete "Fortunately, a massive thanks goes to [mc], the guy who's sitting right there."
    pete "He has been helping [liam] out a lot, so [liam] has been able to only focus on updating codes."
    mc "....You're welcome."
    scene ep3_63_2 with dissolve
    rowan "Oh! You're the new employee who just got hired last week, right?"
    mc "Yes, I am."
    rowan "We really chose the right person to be our employee then... Thank god."
    faye "(He was the guy I saw the other day...)"
    faye "(Well... I thought he was a normal employee, but seems like I was completely wrong.)"
    faye "(He has potential to be one of the best employees here.)"
    faye "(I think I'll have to find a chance to develop a relationship with him in the future.)"
    scene ep3_64 with dissolve
    rowan "What about you, [faye]?"
    rowan "How is everything going?"
    faye "Well, everything is going according to plan, so you don't need to worry about it."
    rowan "Great. I'm glad to hear that you've been managing things well."
    rowan "Now, let's talk about you, [sandra]..."
    rowan "You're probably wondering why you, the head of the community management department, was asked to be here."
    sandra "Yes, I am."
    rowan "Since you're an employee here, I assume that you already briefly know what we have been doing even though you weren't in the team involving the development progress."
    sandra "You're right. I know that you guys have been inventing something called Xecon Gear."
    rowan "Yes, that's right."
    scene ep3_65 with dissolve
    rowan "From now on I want you to know every single detail about it so that you can discuss it with people in your department on how to slightly release the rumours on social media to heat the thing up."
    rowan "[faye], I want you to tell her more details after this meeting."
    faye "Sure. You can count on me."
    scene ep3_66 with dissolve
    eira "........."
    eira "*Sigh*....."
    u "Hm...? What is she doing?"
    u "Did her pen run out of ink or what?"
    u "Should I lend her my pen?"
    menu:
        "Do it [eira3]":
            u "...Why not? It's just a pen."
            $ ep3_lendpen = 1
            $ eira_relationship += 2
            $ eira_ch1_ep3 += 2
            scene ep3_66_give1 with dissolve
            mc "...Here. Use mine."
            eira "....I...."
            eira "........."
            scene ep3_66_give2 with dissolve
            eira "....Thank you."
            mc "You're welcome."
        "Don't do it":
            u "...Why should I do that? It's none of my business."
            scene ep3_66_ignore with dissolve
            $ ep3_lendpen = 2
            u "No surprise... She clearly doesn't need help at all."
            u "She brought another one with her."
            u "To be honest, I don't know why she's writing everything down on a notebook though."
            u "I mean... She could just use her phone, or laptop instead. It's a lot more convenient."
    scene black with dissolve
    s "*An hour later*......."
    scene ep3_61 with dissolve
    rowan "Alright, I think that's enough for today's meeting."
    rowan "Before I let you guys leave, does anyone have any questions?"
    scene ep3_67 with dissolve
    eira "Yes."
    eira "I want to make a suggestion."
    scene ep3_68 with dissolve
    rowan "Sure, [eira]."
    rowan "What do you want to suggest?"
    scene ep3_69 with dissolve
    eira "It's an idea for marketing."
    eira "I know that we're going to get a lot of attention anyway when we announce Xecon Gear to public."
    eira "But, I also think we should hire a famous model for shooting an advertisement."
    eira "You know... Someone who can capture people's attention, and make them want to play our game."
    eira "That will help us gain even more customers."
    scene ep3_70 with dissolve
    rowan "Ummm.... Yeah, that's a pretty good idea. Let's do it."
    rowan "Thanks for your suggestion, [eira]."
    eira "...You're welcome."
    scene ep3_71 with dissolve
    rowan "Can you help [eira] find the person who is going to be the model, [faye]?"
    faye "Sure. I'll make sure to find someone who is eligible for our standards."
    rowan "Great...."
    rowan "Alright, that's it for today."
    rowan "Thank you everyone for working hard. I'll see you later, guys."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_72 with dissolve
    u "Alright, let's get back to the department."
    if ep3_lendpen == 1:
        scene ep3_73 with dissolve
        eira "....Wait."
        u "...Hm?"
        scene ep3_74 at eyesblink("Ch.1/Ep.3/Scenes/ep3_74.jpg", "Ch.1/Ep.3/Scenes/ep3_74_blink.jpg", 1) with dissolve
        mc "...What's wrong?"
        mc "Is there something that you want from me?"
        eira "Er....You're [mc], right?"
        mc "Yes, I am."
        eira "....Thanks for lending me your pen."
        if givelunchset == True:
            eira "...And also... Thanks for letting me have your lunch that one day."
        if ep3_waiteira == 1:
            eira "...And also... Thanks for holding the elevator for me..."
        scene ep3_75 with dissolve
        mc "Hm? Didn't you already say that to me?"
        mc "You don't need to thank me twice."
        eira "Okay.... I'm sorry."
        mc "........"
        scene ep3_76 with dissolve
        mc "Is there anything else you'd like to say?"
        eira "Err.... I think not."
        mc "........."
        mc "You know.... You don't act like what people said about you."
        eira ".....What did they say?"
        mc "They said that you were cold as ice. You'll only pay attention to other people only when they're talking about work."
        mc "But to be honest... I don't think you are, because you just talked to me first."
        scene ep3_77 with dissolve
        eira "........."
        u "Hm? She's blushing?... Why?"
        eira "...I had no idea that they thought of me like that..."
        mc "Really? You had no idea at all?"
        scene ep3_78 at eyesblink("Ch.1/Ep.3/Scenes/ep3_78.jpg", "Ch.1/Ep.3/Scenes/ep3_78_blink.jpg", 1) with dissolve
        eira "Yeah..."
        eira "Well... My face looks kinda cold... And I'm not quite good at talking to people."
        eira "So... I think I understand them...."
        eira "I've been trying to change myself.... But I still feel shy when talking to people"
        eira "....So, I've been trying to avoid talking to them."
        eira "However, I'm fine when talking about work because I know what to say exactly..."
        mc "I see...."
        mc "Maybe you should try to talk with them more often."
        mc "I think you'll eventually become better soon."
        eira "...Yeah, that makes sense..."
        mc "Alright, I think I have to leave now. I need to get back to my department."
        eira "Oh, sure...."
        $ eira_relationship += 1
        $ eira_ch1_ep3 += 1
        $ ep3_realstory = 1
        jump ep3_getoffwork
    elif ep3_lendpen == 2:
        jump ep3_getoffwork
label ep3_getoffwork:
    scene black with dissolve
    stop music fadeout 3.0
    s "*Few hours later*......."
    scene ep3_79 with dissolve
    play music "sfx/ep.3/ep3_5.mp3" fadein 3.0
    $ bgm = "Ghostrifter Official - Soaring"
    u "Okay, that's it for today. It's already 5 p.m."
    u "It's time to get off work now."
    joe "Woah!... What's happening here?!"
    scene ep3_80 with dissolve
    u "Hm...? What's going on?"
    joe "Dude! Is this a dream?! I can't believe my own eyes!"
    leo "Me too, dude!"
    scene ep3_81 with dissolve
    leo "Hello, girls! What are you doing here?"
    u "[rin], [wendy], and... Who is standing in front of [joe]?"
    u "I can't see her since he is blocking my view."
    u "But, to be honest I can guess who she is though, since she comes here with [wendy]."
    scene ep3_82 with dissolve
    joe "*Ahem*... What made you guys come here?"
    leo "Could it be that... You guys come to see me?"
    elaine "*Giggles*...No, we didn't. Why do we need to come to see you?"
    leo "Err...."
    rin "*Giggles*...Actually, we come to see [mc]..."
    scene ep3_83 with dissolve
    rin "...Oh! There he is!"
    elaine "*Giggles*...Yeah, there he is..."
    leo "Did you just say [mc]?!"
    scene ep3_84 with dissolve
    elaine "Good evening, [mc]!"
    joe "*Whispers*...What the hell is going on, dude?!"
    joe "*Whispers*...Not only [sally], but these angels also know him!"
    leo "*Whispers*...I don't fucking know! I'm fucking confused, too!"
    leo "*Whispers*...He's been working here for only a week. He also seems to be an introvert, yet four of the angels already know him!"
    joe "*Whispers*...Could it be that he's been pretending to be an introvert, but he's actually a fucking playboy?"
    leo "*Whispers*...I don't know!"
    scene ep3_85 with dissolve
    mc "What are you guys doing here?"
    elaine "We come here to pick you guys up."
    yui "Hm?... Why do you need to do that?"
    yui "Isn't it supposed to be [zeke] who has to come and take us home?"
    scene ep3_86 with dissolve
    rin "Well, [elaine] and [wendy] told me that they wanted to visit us this evening."
    rin "So, [zeke] told them to take us home, because he had to go pick [mika] up at her place."
    yui "You guys are going to our house?"
    elaine "Yeah, since we were busy when [rin] invited us to go there last time, I think it would be good for us to have dinner with you guys today."
    rin "Alright, let's not waste anymore time here. Let's leave now."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_87 with dissolve
    wendy "It's been a while since we visited you guys."
    rin "Yeah, it's been a while... Two months I guess?"
    wendy "I think so..."
    elaine "*Whispers*...Are you happy to see me, [mc]?"
    mc ".........."
    scene ep3_88 with dissolve
    joe "Damn... I want to be in his position so bad..."
    joe "Look at him being surrounded by those beautiful angels!"
    joe "Fuck!... I'm so jealous of him!"
    leo "So am I, man..."
    scene ep3_89 with dissolve
    joe "I heard they're going somewhere together."
    joe "Man... Why didn't you ask if we could join them?"
    leo "Are you crazy? Why would I have done that?"
    joe "Why not?!"
    leo "We aren't even close to them. Even if I asked them, there was no way they were going to let us join them."
    joe "....But you could've just tried..."
    liam "What are you guys still doing here? Just go home already!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_90 with dissolve
    elaine "Alright, here we are!"
    yui "Wow... You've got such a nice car."
    elaine "*Giggles*...Thanks!"
    u "Hm....?"
    scene ep3_91 with dissolve
    u "Isn't that [sally]?"
    u "Who's with her?...[eira]?"
    u "So, the rumour that [eira] doesn't have any friends, isn't true then."
    u "Since they're going somewhere together, I assume that she's a friend of [sally]."
    scene ep3_92 with dissolve
    elaine "What are you waiting for, [mc]?"
    elaine "Come on! Let's get in the car so we can leave."
    mc "Oh... My bad, I'm sorry."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_123 with fade
    rin "Okay, here we are!"
    rin "You guys go sit and wait on the sofa. I'm going to get changed first."
    wendy "Sure."
    rin "You can turn on the TV if you want."
    elaine "Thanks!"
    scene ep3_124 with dissolve
    rin "Wait a sec, [mc]."
    rin "You're going to join us later, right?"
    mc "........"
    u "[victor] told me to blend in with these people..."
    u "Then, I'll just go with the flow from now on."
    scene ep3_125 with dissolve
    mc "Yes, I'm going to join you guys."
    rin "*Giggles*...Great! I'm glad to hear that!"
    mc "Now, please excuse me. I'm going to get changed, too."
    rin "Sure! See you tonight!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_126 with dissolve
    u "...Alright, let's change my outfit..."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_127 with dissolve
    u "Let's find something to do..."
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Knocking*....."
    u "Hm....?"
    stop sound
    scene ep3_128 with dissolve
    mc "Who is it?"
    elaine "It's me, [elaine]."
    mc "What do you want?"
    elaine "Can you open the door for me, please?"
    mc "....Okay."
    $ renpy.sound.play("sfx/Door opening.mp3")
    scene ep3_129 at eyesblink("Ch.1/Ep.3/Scenes/ep3_129.jpg", "Ch.1/Ep.3/Scenes/ep3_129_blink.jpg", 1) with dissolve
    elaine "Hey..."
    elaine "What were you doing?"
    mc "Nothing. I was just going to find something to do."
    mc "By the way, how did you know my room?"
    scene ep3_130 with dissolve
    elaine "*Giggles*...Hehe... It's a secret!"
    mc "...So, you aren't going to tell me?"
    elaine "*Giggles*...No, I'm not!"
    mc "*Sighs*....Then, what do you want from me?"
    scene ep3_131 at eyesblink("Ch.1/Ep.3/Scenes/ep3_131.jpg", "Ch.1/Ep.3/Scenes/ep3_131_blink.jpg", 1) with dissolve
    elaine "I'm so lonely~"
    elaine "There is nobody down there."
    mc "What do you mean? Where has [wendy] gone?"
    elaine "She just went outside with [rin]."
    mc "Hm? Why?"
    elaine "To buy food and drinks for dinner."
    mc "I see..."
    elaine "So...."
    elaine "I want to stay with you. Can I come in?"
    scene ep3_132 with dissolve
    mc "Why don't you go stay with [yui]?"
    elaine "Come on! I'm not that close to her."
    elaine "I'd feel a bit weird staying with her alone."
    elaine "But, I'd be okay if it was you, because I think we're quite {b}close{/b}..."
    elaine "*Giggles*...At least our lips were close enough to touch each other..."
    mc ".........."
    u "What should I do?"
    menu:
        "Let her in [elaine2]":
            $ ep3_letelainein = 1
            $ elaine_ch1_ep3 += 2
            $ eliane_relationship += 2
            scene ep3_132_a1 with dissolve
            mc "Okay then, come in."
            elaine "Yes!"
            mc "Don't forget to close the door."
            elaine "*Giggles*...Sir! Yes Sir!"
            scene ep3_132_a2 with dissolve
            elaine "Hm...? You've got such a nice room!"
            mc "Thank you."
            elaine "Oh! You also have a computer. Can I use it?"
            mc "Hm? What do you want to use it for?"
            elaine "I don't know... I may just surf the internet, play games, or anything!"
            elaine "I'm bored to death right now..."
            mc "..........."
            elaine "Can I?"
            mc "...Sure. You can use it."
            elaine "*Giggles*...Hehe... Thanks!"
            u "I was afraid that she might find the source code for Xecon Gear, but to think about it carefully..."
            u "There is no way she will find it. I've already hide it in a very safe place...."
            scene ep3_132_a3 with dissolve
            s "You turn on the TV, then find something to watch on Netflix while [elaine]'s using your computer..."
            jump ep3_zekeintrouble
        "Refuse to let her in":
            scene ep3_132_d1 with dissolve
            $ renpy.sound.play("sfx/Door closing.mp3")
            s "*Door closing*......."
            elaine ".........."
            elaine "...Seriously?"
            elaine "Do you really have to do this?"
            scene ep3_132_d2 with dissolve
            mc "I'm sorry, but I don't think I can help you from being lonely."
            mc "There is nothing in my room for you to do."
            mc "Also, I've just decided that I'm going to work."
            mc "So, I don't want you to bother me."
            scene ep3_132_d3 with dissolve
            elaine "Pff! You didn't have to bring up those excuses..."
            elaine "Just say it that you don't want me to stay with you."
            mc ".........."
            elaine "Alright then, I'm going back to downstairs, and find something to do myself..."
            elaine "(But, you know what?)"
            elaine "(No matter how hard you try to avoid me, it's only going to make me want to get you more!)"
            $ ep3_letelainein = 2
            $ eliane_relationship += 1
            $ elaine_ch1_ep3 += 1
            scene black with dissolve
            $ renpy.pause()
            scene ep3_132_d4 with dissolve
            u "Alright... Let's learn the code of Xecon Gear again..."
            jump ep3_zekeintrouble
label ep3_zekeintrouble:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_93 with fade
    mika "...Thanks for helping me out lately, [zeke]."
    mika "I had no idea what I would have done if I didn't have you."
    scene ep3_94 with dissolve
    zeke "Come on! You don't have to thank me at all!"
    zeke "You can come and ask me for help anywhere, and anytime!"
    zeke "I just want you to know that that I'll always be by your side, and support you."
    mika "...Thank you. That really means a lot to me."
    scene ep3_93 with dissolve
    zeke "By the way, are you okay?"
    zeke "I mean... You went back to your place to pick up your stuff."
    zeke "Did you see him? Did he hurt you?"
    mika "I'm fine. He wasn't there when I went in. He's usually at work by that time."
    zeke "That's good for you. You should never go and meet him anymore."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ep3_95 with dissolve
    play music "sfx/ep.3/ep3_6.mp3" fadein 3.0
    $ bgm = "Crystal Drop! - Fall"
    dick "Fuck...! What's wrong with her seriously?!"
    ben "What happened, dude?"
    ben "You've been angry for two days."
    dick "My girlfriend has disappeared without telling me!"
    dick "She doesn't even pick up her phone!"
    ben "Why did she do that?"
    dick "I don't fucking know!"
    scene ep3_96 with dissolve
    s "Welcome!"
    s "What would you guys like to have?"
    ben "Could it be that she got kidnapped?"
    dick "I don't think so...."
    scene ep3_97 with dissolve
    dick "Fuck!... Just answer the damn phone!!"
    mika "!!!!!"
    scene ep3_98 with dissolve
    zeke "What are you doing, [mika]?"
    mika "*Whispers*...Shh!... Be quiet!"
    zeke "Hm?...What's happening?"
    mika "*Whispers*...I'll tell you later, okay?"
    scene ep3_99 with dissolve
    dick "This bitch....!"
    ben "Hm? Dude..."
    dick "What?!"
    scene ep3_100 with dissolve
    ben "Isn't that.... Your girlfriend?"
    dick "........."
    dick "Yeah, she is..."
    scene ep3_101 with dissolve
    jack "Who is that dude sitting with your girlfriend, man?"
    jack "Is she cheating on you?"
    dick "This fucking bitch...!"
    scene ep3_102 with dissolve
    dick "What the fuck are you doing here, [mika]?!"
    zeke "Hm...?!"
    ben "(Hm? This guy seems familiar...)"
    scene ep3_103 with dissolve
    zeke "Hey! Fuck off, dude!"
    zeke "Leave her alone!"
    dick "Shut the fuck up! This is none of your fucking business!"
    dick "Oh! Actually, this is your business since you were the reason why this bitch has been avoiding me, right?"
    zeke "Stop calling her that!"
    crowd "What's happening? Are they fighting?"
    scene ep3_104 with dissolve
    dick "Get up!!!"
    mika "Ouch! Release me! You are hurting me!"
    zeke "Hey! Let her go!!"
    jack "Where do you think you are going, cunt?"
    mika "[dick]! You're hurting me!"
    scene ep3_105 with dissolve
    zeke "Didn't you hear what she said, you fucking [dick]!!"
    zeke "Get out of my way!!"
    jack "Ouch!!"
    ethan "Be careful, bro!"
    crowd "Someone, please call the police!"
    mika "[zeke]! No!"
    mika "Don't you remember what I used to tell you?"
    dick "Oh? You actually care about him more than yourself in this situation, huh?"
    dick "How long have you been cheating on me?"
    dick "How long have you been fucking him behind my back, bitch?!"
    scene ep3_106 with dissolve
    mika "I...said..."
    mika "Release me!!!"
    scene ep3_107 with dissolve
    mika "What did you just say?!"
    mika "I've been cheating on you?!"
    mika "I've been fucking someone behind your back?!"
    mika "Seriously?!"
    dick "Was I wrong?!"
    dick "You've disappeared without telling me!"
    dick "You didn't even pick up your fucking phone when I called you!"
    dick "What would happen if I didn't come, and see you here with that cunt?!"
    scene ep3_108 with dissolve
    mika "Stop saying things that make me look like a bad person!"
    mika "Don't you really know why I disappeared without telling you?!"
    mika "Don't you really know why I didn't pick up my phone?!"
    mika "Don't you really think that I know what you did?!"
    mika "Do you think I'm stupid?!"
    mika "I knew that you went to the hotel with one of your co-workers!"
    mika "And that wasn't the first time!"
    mika "How could you do that to me?! How could you cheat on me?!"
    scene ep3_109 with dissolve
    crowd "Wow... This guy is a jerk..."
    crowd "What a poor girl... How could he do something like that behind her back?"
    dick "Shut the fuck up! Otherwise, I'm going to break your fucking nose!"
    dick "Every single one of you!!"
    crowd ".........."
    scene ep3_107 with dissolve
    mika "I never want to see you again."
    mika "You and I are done."
    dick "It's not what you think! I didn't do anything to her!"
    mika "Really?!"
    mika "Do I have to show you the picture she sent to me?"
    dick ".........."
    mika "Now, just get out of my face."
    dick "But...!"
    mika "Get lost! I don't want to see you anymore!!"
    scene ep3_110 with dissolve
    dick "Fuck!! You'll regret this, [mika]!!"
    zeke "Are you okay, [mika]?"
    zeke "Does your wrist still hurt?"
    mika "*Hics*...No... I'm not okay..."
    zeke "Don't cry. You did very well..."
    zeke "That asshole doesn't deserve such a good woman like you...."
    mika "*Hics*....T..Thank you..."
    scene black with dissolve
    u "*Half an hour later*........"
    scene ep3_111 with dissolve
    zeke "Are you feeling better now?"
    mika "Yes. I think so."
    mika "I'm sorry that you had to see me cry again, [zeke]."
    zeke "It's okay. What happens in the past stays in the past."
    zeke "I'll just make sure that you will not have to cry again."
    mika "..........."
    scene ep3_112 with dissolve
    zeke "Alright, I think we should leave now."
    zeke "Everyone is probably waiting for us."
    mika "Oh yeah, you're right."
    zeke "You wait for me here a for sec. I'll go get my car."
    mika "We can go there together actually."
    zeke "No. Just wait for me here. I parked my car quite a bit far from here."
    mika "Okay then..."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ep3_113 with fade
    zeke "*Humming a song*.....Hmmm....."
    scene ep3_114 with dissolve
    play music "sfx/ep.3/ep3_7.mp3" fadein 3.0
    $ bgm = "Jeff II - Heartfül of Kerøsene"
    dick "Fuck! I'm so fucking mad right now!"
    jack "Just forget her, man."
    jack "There are manymore beautiful women than her around you."
    dick "But, she's the only woman I love!"
    ben "Then, why did you cheat on her, man..."
    dick "I don't know...."
    jack "Hm...? Isn't that the guy from the cafe?"
    dick "What?! Go get him!"
    scene ep3_115 with dissolve
    jack "Where do you think you're going, huh?"
    zeke "Jeez... You guys again..."
    zeke "What do you want from me?"
    jack "Follow me!"
    zeke "What if I don't want to do that?"
    jack "I'm going to beat you to death!"
    zeke "*Sighs*...Fine..."
    scene ep3_116 with dissolve
    dick "You must be so over the moon now, huh?"
    zeke "What are you talking about?"
    dick "Stop playing dumb!"
    dick "Do you think I don't know that you've been following [mika]'s ass for years?!"
    scene ep3_117 with dissolve
    dick "Don't be too happy! There is no way I'm going to let her go!"
    zeke "It's not your decision to make. She already made up her mind."
    zeke "She doesn't want to be with you any longer."
    dick "Shut the fuck up!!"
    ethan "Dude! Can we just beat his ass up already?"
    ethan "I met this guy before. I really don't like him!"
    zeke "............."
    ethan "Also, I'm still mad at that red hair bitch!"
    ethan "How dare she give me a fake phone number?!"
    ethan "But since I can't find her, I'll make you pay for that!"
    scene ep3_118 with dissolve
    dick "I don't need you to tell me that!"
    dick "I've been hating him for a long time!"
    dick "Only if that bitch didn't stop me from beating her so called friend, he would be dead for a hundred times already!"
    zeke "............."
    dick "Now, there is nobody to stop me. You're fucking dead-"
    scene ep3_119 with dissolve
    dick "Ouch....!!"
    ethan "!!!!!"
    zeke "....Didn't I tell you to not call her that?"
    scene ep3_120 with dissolve
    ben "Dude, are you okay?"
    dick "I'm good! There is no way I'm going to get knocked out by a weak sucker punch!"
    dick "Don't worry about me! Beat him up!!"
    scene ep3_121 with dissolve
    ben "*Sighs*...I'm sorry, man. I neither hate you nor have a problem with you."
    ben "But, I have no choice...."
    jack "So, you're quite good at fighting, huh?!"
    jack "But, you're out of luck today because we have numbers. There is no way you are going to win this fight!"
    ethan "I'm going to beat the crap out of you until you beg for me to stop!!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_122 with dissolve
    zeke "*Sighs*....I didn't really want to do this, but you left me no choice...."
    zeke "....You guys reminded me of the old days that I've been trying to forget..."
    zeke "But since we just already had a little talk, I'll tell you something before leaving."
    zeke "Don't you ever come near [mika] again...."
    zeke "Otherwise, I'll make you guys experience something even more terrifying than this."
    if ep3_letelainein == 1:
        jump ep3_elaineinbedroom
    elif ep3_letelainein == 2:
        jump ep3_dinnerparty
label ep3_elaineinbedroom:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ep3_132_a4 with fade
    play music "sfx/ep.3/ep3_8.mp3"
    $ bgm = "Johny Grimes - Double Vision"
    elaine "*Yawns*......."
    elaine "So boring...."
    scene ep3_132_a5 with dissolve
    elaine "What are you doing?"
    mc "I'm watching an anime on Netflix..."
    elaine "Well, I don't know what to do next."
    elaine "So, let me just join you..."
    scene ep3_132_a6 with dissolve
    elaine "What's the story about?"
    mc "Well... Considering from what I've been watching...."
    mc "It's the story about a super elite school that was set up by the government."
    mc "It's dedicated to foster the youth in becoming leaders of the future."
    mc "The students are guaranteed to be employed upon graduation."
    elaine "Hm...? That sounds like a really good school to go, doesn't it"
    mc "Though students are not allowed to leave their entire high school career and communication is cut off with the outside world."
    mc "But, they've got everything they need in the school's area."
    mc "They're even given a budget to live on. Starting with 100,000 points which is worth around 938.20 dollars."
    elaine "Heh...? They're given such a pretty big amount of money, aren't they?"
    elaine "Considering the fact that they're just students..."
    scene ep3_132_a7 with dissolve
    mc "Yeah, I agree."
    mc "Students are judged as a classroom, based on merit, and points are awarded at the start of each month."
    mc "They basically are free to do, or buy whatever they want with those points."
    scene ep3_132_a8 with dissolve
    elaine "Is he the main character?"
    mc "Yes, he is."
    elaine "Well, you know what? He kind of reminds me of you."
    mc "Me?"
    scene ep3_132_a9 with dissolve
    elaine "Yeah, you guys look kind of similar."
    elaine "He also talks in a monotone voice just like you!"
    mc "..........."
    elaine "*Giggles*...Look! You guys even have the same facial expression!"
    mc "Well, may be you're right..."
    scene black with dissolve
    s "*A few moments later*....."
    scene ep3_132_a10 with dissolve
    elaine "........."
    elaine "[mc]...."
    mc "What?"
    elaine "Don't you feel bored?"
    mc "No, I don't."
    scene ep3_132_a11 with dissolve
    elaine "But, I do!"
    mc "Hey... Step aside. You're blocking my view."
    elaine "Come on! Let's find something fun to do!"
    mc "Then, what do you want to do?"
    scene ep3_132_a12 with dissolve
    elaine "Well, you know...."
    elaine "Let's do things that a man, and woman tend to do when they're all alone in a bedroom..."
    mc "........."
    scene ep3_132_a13 with dissolve
    elaine "Where were you looking at...?"
    scene ep3_132_a14 with dissolve
    elaine "Look at me..."
    scene ep3_132_a15 with dissolve
    elaine "Don't you think I'm more interesting than that anime, hm~?"
    mc "I'm not in such a mood...."
    scene ep3_132_a16 with dissolve
    elaine "Really?"
    scene ep3_132_a17 with dissolve
    elaine "Then..."
    scene ep3_132_a18 with dissolve
    elaine "How about...."
    scene ep3_132_a19 with dissolve
    elaine "...this?"
    elaine "Are you still not interested, hm~?"
    scene ep3_132_a20 with dissolve
    mc "........."
    u "She's surely such a seductive woman..."
    u "How would I able to resist her if she did something like this in front of me...?"
    u "I had no problem dealing with women before when I was in the university, because I lived my life there as an invisible man."
    u "But, after moving here, I've been meeting so many attractive women."
    u "It's getting a lot harder for me to stay the way I've always been..."
    elaine "Heh~? Someone is finally having a boner..."
    mc "Well, you know that I'm a human being, not a robot, right?"
    elaine "Then, what are you waiting for? Let's have fun!"
    u "What should I do?"
    menu:
        "Do it [elaine2] [smbo]":
            u "I have to blend in with them.... So, let's just do whatever she wants."
            mc "...Okay."
            $ ep3_havefunwithelaine = 1
            $ eliane_relationship += 2
            $ elaine_ch1_ep3 += 2
            scene ep3_132_a20_a1 with dissolve
            elaine "Yeah, that's the right thing to say!"
            elaine "Now, let me take your shorts off!"
            jump ep3_elainehavefun
        "Don't do it [elaine1]":
            scene ep3_132_a20_d1 with dissolve
            elaine "W-What are you doing...?!"
            mc "I'm still not interested."
            mc "If you are just going to keep bothering me, then I have no choice...."
            scene ep3_132_a20_d2 with dissolve
            mc "Get out."
            elaine "Aw....!"
            mc "Take your panties with you, too."
            scene ep3_132_a20_d3 with dissolve
            s "*Door closing*....."
            elaine "Argh...! I can't believe you just pushed me out of your room!"
            elaine "How could you ignore a sexy woman like me when I tried to seduce you?"
            elaine "*Sighs*...Fine! I'm going back downstairs. Good luck with your anime!"
            elaine "(But, you know what...?)"
            elaine "(No matter how hard you try to play hard, it's only going to make me want to get you more!)"
            $ ep3_havefunwithelaine = 2
            $ eliane_relationship += 1
            $ elaine_ch1_ep3 += 1
            scene black with dissolve
            s "*Half an hour later*......."
            scene ep3_133 with dissolve
            rin "Dinner is about to be ready, [mc]."
            rin "You should come downstairs with me now."
            mc "Okay."
            jump ep3_dinnerparty
label ep3_elainehavefun:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    scene ep3_132_a20_a2 with dissolve
    if elianehj == True:
        elaine "Hi, there~"
        elaine "*Giggles*....We meet again!"
    if refuseeliane == True:
        elaine "Wow... You've got such a good cock..."
        elaine "I like it!"
    mc "What are you going to do with it?"
    scene ep3_132_a20_a3 with dissolve
    elaine "*Giggles*...Hehe... What do you want me to do?"
    mc "....I'll let you decide what to do."
    elaine "I want to taste it. Can I suck it?"
    mc "Do you even need to ask?"
    elaine "You know... I just want to ask for your permission because I don't want to do things that you don't want me to do."
    mc "Yes, you can."
    elaine "*Giggles*...Hehe, then..."
    scene ep3_132_a20_a4 with dissolve
    show ep3_elainebj1 with dissolve
    window hide
    elaine "*Sucks*...Mmmmm...."
    elaine "*Sucks*....Mmmmm... Your cock is so big...."
    elaine "*Sucks*....It can barely fit in my mouth...."
    $ renpy.pause()
    hide ep3_elainebj1 with dissolve
    scene ep3_132_a20_a5 with dissolve
    show ep3_elainebj2 with dissolve
    window hide
    mc "*Softly breathes*...Ar...."
    elaine "*Sucks*...Mmmmmm...... I think I'm falling in love with your cock..."
    elaine "*Sucks*...Mmmmm.... I'm going to suck it faster...."
    $ renpy.pause()
    hide ep3_elainebj2 with dissolve
    scene ep3_132_a20_a6 with dissolve
    show ep3_elainebj3 with dissolve
    window hide
    elaine "*Sucks*.....Mmmmmm....."
    elaine "*Sucks*....Mmmmm.... Are you about to cum?"
    elaine "*Sucks*.... I can feel your cock is about to explode..."
    $ renpy.pause()
    mc "...Yeah, I'm almost there..."
    menu:
        "Slowest":
            hide ep3_elainebj3
            jump ep3elainebjslow
        "Slower":
            hide ep3_elainebj3
            jump ep3elainebjnormal
        "Cum":
            jump ep3elainebjcum
label ep3elainebjslow:
    scene ep3_132_a20_a4 with dissolve
    show ep3_elainebj1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ep3_elainebj1
            jump ep3elainebjnormal
        "Fastest":
            hide ep3_elainebj1
            jump ep3elainebjfastest
label ep3elainebjnormal:
    scene ep3_132_a20_a5 with dissolve
    show ep3_elainebj2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_elainebj2
            jump ep3elainebjslow
        "Fastest":
            hide ep3_elainebj2
            jump ep3elainebjfastest
label ep3elainebjfastest:
    scene ep3_132_a20_a6 with dissolve
    show ep3_elainebj3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slowest":
            hide ep3_elainebj3
            jump ep3elainebjslow
        "Slower":
            hide ep3_elainebj3
            jump ep3elainebjnormal
        "Cum":
            jump ep3elainebjcum
label ep3elainebjcum:
    mc "*Softly breathes*....I'm about to cum..."
    elaine "*Sucks*...Mmmmm... Please, cum in my mouth...."
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause(0.3,hard=True)
    hide ep3_elainebj3
    scene ep3_132_a20_a7 with dissolve
    mc "Ugh...!"
    elaine "Mmmmmm!!!"
    elaine "*Swallows*...Mmm...."
    $ renpy.pause()
    scene ep3_132_a20_a8 with dissolve
    elaine "*Giggles*...Hehe... So delicious..."
    elaine "*Giggles*...Heh~ You're still hard...?... Impressive...."
    elaine "...Alright, now it's your turn to please me..."
    mc "Hm? What do you want me to do?"
    scene ep3_132_a20_a9 with dissolve
    elaine "Well..I've already sucked your cock..."
    elaine "Then, how about you eat my pussy?"
    mc "Okay..."
    scene ep3_132_a20_a10 with dissolve
    show ep3_elainelick1 with dissolve
    window hide
    elaine "*Softly breathes*...Mmmmm..."
    elaine "*Softly breathes*...Arr... Yeah... That spot!...."
    elaine "*Softly breathes*....Mmmmm... You're so good...!"
    $ renpy.pause()
    hide ep3_elainelick1
    scene ep3_132_a20_a11 with dissolve
    show ep3_elainelick2 with dissolve
    window hide
    elaine "*Moans*...Ahhh!... Yeah! Keep licking it like that!"
    mc "*Licks*...Don't moan too loud. [yui] might hear us."
    elaine "*Moans*...Mmmmm!.... I don't care!... I'm feeling so good now!"
    $ renpy.pause()
    hide ep3_elainelick2
    scene ep3_132_a20_a12 with dissolve
    show ep3_elainelick3 with dissolve
    window hide
    elaine "*Heavily breathes*....Ahhh!...Ahhh!..."
    elaine "*Heavily breathes*...Mmmmm!... Don't... Don't... Stop...!"
    elaine "*Heavily breathes*...I'm...getting...there..!"
    $ renpy.pause()
    menu:
        "Slowest":
            hide ep3_elainelick3
            jump ep3elainelickslow
        "Slower":
            hide ep3_elainelick3
            jump ep3elainelicknormal
        "Cum":
            jump ep3elainelickcum
label ep3elainelickslow:
    scene ep3_132_a20_a10 with dissolve
    show ep3_elainelick1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ep3_elainelick1
            jump ep3elainelicknormal
        "Fastest":
            hide ep3_elainelick1
            jump ep3elainelickfastest
label ep3elainelicknormal:
    scene ep3_132_a20_a11 with dissolve
    show ep3_elainelick2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_elainelick2
            jump ep3elainelickslow
        "Faster":
            hide ep3_elainelick2
            jump ep3elainelickfastest
label ep3elainelickfastest:
    scene ep3_132_a20_a12 with dissolve
    show ep3_elainelick3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slowest":
            hide ep3_elainelick3
            jump ep3elainelickslow
        "Slower":
            hide ep3_elainelick3
            jump ep3elainelicknormal
        "Cum":
            jump ep3elainelickcum
label ep3elainelickcum:
    elaine "*Heavily breathes*...I'm...about...to cum...!"
    $ renpy.pause()
    scene black with dissolve
    hide ep3_elainelick3
    $ renpy.pause(0.4,hard=True)
    scene ep3_132_a20_a13 with dissolve
    elaine "I'm cumming!!!"
    elaine "Mmmmmmm!!"
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause(0.4,hard=True)
    scene ep3_132_a20_a14 with dissolve
    elaine "*Pants*...That...was...so...good...."
    elaine "*Pants*...You're the first person... Who made me cum by only using tongue..."
    elaine "*Pants*...You're...so...amazing..."
    scene black with dissolve
    $ renpy.pause(0.4,hard=True)
    scene ep3_132_a20_a15 with dissolve
    elaine "Come on! Let's have some real fun!"
    mc "You want more?"
    elaine "Of course! There is no way I'm going to stop just because I came once."
    elaine "I can't wait to have your cock inside me anymore. Take me!"
    scene ep3_132_a20_a16 with dissolve
    mc "Okay... If that's what you want...."
    elaine "*Giggles*...Hehe.... I've been waiting for this moment!"
    elaine "I can't wait to know how it feels to have your big cock inside me..."
    mc "Alright, I'm going to put it in...."
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Knocking*......."
    mc "Hm...?"
    scene ep3_132_a20_a17 with dissolve
    mc "Who's it?"
    rin "It's me, [rin]."
    u "Since when did she come back here?"
    mc "What do you want?"
    rin "Can you open the door, please?"
    mc "....Okay. Wait a sec."
    scene ep3_132_a20_a18 with dissolve
    mc "Seems like we can't do it now."
    mc "Let's get up and put on your clothes."
    elaine "*Sighs*....Okay."
    elaine "Jeez.... She's such a cock blocker..."
    $ renpy.end_replay()
    jump ep3_rininterrupt
label ep3_rininterrupt:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_133 with dissolve
    rin "Hi!"
    mc "Hello."
    rin "I come here to tell you that dinner is about to be ready soon."
    rin "You should come down with me now."
    scene ep3_134 with dissolve
    mc "Alright, I get it. Let's go then."
    rin "Sure! Let's go."
    rin "By the way...do you know where [elaine] is?"
    mc "............."
    rin "I couldn't find her anywhere in the house."
    scene ep3_135 with dissolve
    elaine "I'm here!"
    rin "[elaine]?!"
    rin "What were you doing in [mc]'s room?"
    scene ep3_136 with dissolve
    elaine "Well, I was lonely after [wendy] and you went outside."
    elaine "So, I came here to stay with [mc]."
    elaine "I was just going to talk with him, but then I saw his computer."
    elaine "So, I asked him to let me use it so that I could find something to do."
    elaine "Right, [mc]?"
    mc "...Yeah."
    scene ep3_137 with dissolve
    rin "Oh! I never knew you would be that lonely."
    rin "My bad, I'm sorry. I should've insisted you to come with us."
    elaine "It's okay. I feel better now."
    elaine "A big thanks goes to [mc]!"
    elaine "Then, should we go downstairs now?"
    rin "Yeah, I think so."
    scene black with dissolve
    $ renpy.pause()
    if sexwithrin == 1:
        scene ep3_137_a1 with dissolve
        elaine "Hm? Aren't you guys coming?"
        rin "Actually... Can you go first?"
        rin "I have something to ask him."
        elaine ".........."
        elaine "Okay then!"
        scene ep3_137_a2 with dissolve
        rin "........."
        mc "What did you want to ask me?"
        rin "[mc]."
        mc "What?"
        scene ep3_137_a3 at eyesblink("Ch.1/Ep.3/Scenes/ep3_137_a3.jpg", "Ch.1/Ep.3/Scenes/ep3_137_a3_blink.jpg", 1) with dissolve
        rin "What [elaine] said... Was it real?"
        rin "Did she really come here to just use your computer?"
        mc ".........."
        rin "Can you tell me the truth?"
        rin "What exactly were you guys doing?"
        u "What should I say?"
        menu:
            "Tell her the truth [rin1]":
                u "Let's just tell her the truth..."
                u "It might not be a good idea, but I don't want to lie to her."
                if rin_hate2 == "Liars":
                    u "Also, she also used to tell me that she hated liars..."
                scene ep3_137_a4 with dissolve
                mc "No, she didn't come here just to use my computer..."
                rin "....Then, what exactly were you guys doing?"
                mc "We were just about to have sex, but you knocked on the door first."
                rin "........."
                rin "...Did you ask her for it?"
                mc "No, I didn't. She was the one trying to seduce me."
                scene ep3_137_a4_t1 with dissolve
                rin "Well, to be honest I don't know what to say."
                rin "But, at least you didn't choose to lie to me."
                rin "Thanks for telling me the truth, [mc]. I really do."
                mc "....Don't you feel mad at me?"
                scene ep3_137_a5 at eyesblink("Ch.1/Ep.3/Scenes/ep3_137_a5.jpg", "Ch.1/Ep.3/Scenes/ep3_137_a5_blink.jpg", 1) with dissolve
                rin "I'd be lying if I said that I didn't."
                if rin_relationship_status == "Close friend":
                    rin "But, we are just close friends now, and I was the one wanting us to be that."
                    rin "So, I don't think I could be mad at you even if you decided to have sex with her, or any other girls..."
                elif rin_relationship_status == "Acquaintances":
                    rin "But, we are nothing more than acquaintances, so I don't think I could be mad at you."
                    rin "Even if you decided to have sex with her, or any other girls..."
                u "What a surprise... It turned out to be much better than I thought."
                rin "Well... I think I'm going to have to give [elaine] some credit."
                rin "Even though she's well known for loving to have fun with guys, but I've never seen her making a move first."
                rin "But, she did that with you.... She must have known that you're such an incredible guy..."
                mc "I'm not really incredible to be honest...."
                rin "............"
                scene ep3_137_a6 with dissolve
                rin "Alright! I've made the decision!"
                rin "I'm not going to lie. I have some feelings towards you."
                rin "But, I don't know if you feel the same, because to be honest you're so hard to read."
                mc "..........."
                rin "However, I'm not going to give up!"
                rin "I'll do my best to make you say the words that I want to hear!"
                rin "Just you wait!"
                mc "....Okay."
                rin "Alright, I think we should go downstairs now. Everyone is probably waiting for us!"
                $ ep3_tellrinthetruth = 1
                $ rin_relationship += 1
                $ rin_ch1_ep3 += 1
                jump ep3_dinnerparty
            "Just lie to her":
                u "I don't think it's a good idea for me to tell her the truth."
                u "I don't know if she'll get mad at me after knowing it, so I think it's safer to just lie to her."
                if rin_hate2 == "Liars":
                    u "She once said that she wouldn't mind if it's a white lie, didn't she?"
                scene ep3_137_a4 with dissolve
                mc "Yes. She really came here to use my computer."
                rin "......Really?"
                mc "Yeah. What did you think we were doing?"
                rin ".....I don't know."
                mc "Trust me. I told you the truth."
                rin "........."
                scene ep3_137_a4_t1 with dissolve
                rin "Okay, I trust you!"
                rin "I don't think you lied to me."
                if rin_hate2 == "Liars":
                    rin "Especially after I told you that I hate liars..."
                    mc "Yeah, I knew that."
                mc "Thanks for believing me."
                rin "Alright, now that everything is clear."
                rin "I think we should go downstairs now. Everyone is probably waiting for us!"
                mc "Sure."
                $ ep3_tellrinthetruth = 2
                jump ep3_dinnerparty
    elif sexwithrin == 2:
        scene ep3_137_d1 with dissolve
        elaine "*Whispers*...Thanks a lot, hehe...."
        elaine "*Whispers*...Too bad that she interrupted us, but I had a lot of fun today."
        elaine "*Whispers*...Let's have fun again soon..."
        mc "........."
        jump ep3_dinnerparty

label ep3_dinnerparty:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep.3/ep3_9.mp3" fadein 3.0
    $ bgm = "Atch - Freedom"
    if ep3_havefunwithelaine == 2 or sexwithrin == 1:
        scene ep3_137_a7 with fade
        rin "There they are!"
        scene ep3_137_a8 with dissolve
        yui "Hi, [rin]."
        rin "Hey. Have you seen the wine I bought for you?"
        yui "Yes, I have. Thank you so much."
        yui "To see that you guys have got plenty of beer, it would be a sad dinner for me without the wine."
        wendy "Hm? Why?"
        yui "Well, it's because I can't drink beer. I would get drunk very easy if I drank it."
        mc "...Yeah, I can confirm that."
    if ep3_havefunwithelaine == 1 and sexwithrin == 2:
        scene ep3_137_d2 with fade
        rin "There they are!"
        scene ep3_137_d3 with dissolve
        rin "Hi, girls."
        rin "What were you doing?"
        yui "We were just having a little chat."
        wendy "Yeah."
        rin "I see..."
        rin "Have you seen the wine I bought for you, [yui]?"
        yui "Yes, I have. Thank you so much."
        yui "To see that you guys have got plenty of beer, it would be a sad dinner for me without the wine."
        wendy "Hm? Why?"
        yui "Well, it's because I can't drink beer. I would get drunk very easy if I drank it."
        mc "...Yeah, I can confirm that."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_138 with dissolve
    yui "[rin]. Look at this dress. What do you think?"
    rin "It's so pretty!"
    yui "Then, should I buy it?"
    rin "Of course you should! It will look so good on you."
    yui "...Are you sure?"
    rin "Yes, I am!"
    rin "By the way... What about [zeke], and [mika]?"
    rin "Where have they gone?"
    yui "They just went to get changed. They said they'll be right back."
    rin "Hm? [mc]'s room is close to [zeke]'s room. Why didn't I see them?"
    yui "I don't know. Maybe they were in the garage when you guys were coming here?"
    rin "That makes sense... Okay then, let's wait for them here."
    scene black with dissolve
    s "*A few moments later*......"
    scene ep3_139 with dissolve
    zeke "Hi, everyone!"
    elaine "Hey!"
    rin "Finally, there you are!"
    zeke "Hehe... Sorry to kept you guys waiting!"
    scene ep3_140 with dissolve
    zeke "Alright, let's not waste anymore time."
    zeke "Come down here, guys! So, we can get started."
    rin "Sure!"
    scene ep3_141 with dissolve
    elaine ".........."
    zeke "Why don't you sit down, [elaine]? What's wrong?"
    elaine "Don't you guys think it's a bit too tight for us to sit here?"
    rin "To be honest, I think so..."
    rin "We always sat here when you guys came to have dinner with us, but I completely forgot to count [mc], [yui], and [mika] this time."
    zeke "Alright then, let's move to the kitchen."
    elaine "That sounds like a good idea."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_142 with dissolve
    zeke "Yeah, this is much better!"
    yui "Yeah, it is actually a lot better."
    mika "I couldn't agree more."
    wendy "Me, too."
    scene ep3_143 with dissolve
    zeke "Alright then, let's not waste anymore time."
    zeke "I'm so damn hungry right now."
    zeke "Let's enjoy our dinner, guys!"
    scene black with dissolve
    s "You guys spend time having dinner, and chatting with each other....."
    s "*About an hour later*........."
    scene ep3_144 with dissolve
    rin "*Sighs*...Ahh... I'm so full~"
    zeke "Well, seems like I wasn't the only one who was hungry."
    zeke "You guys finished everything so fast!"
    yui "I waited so long for you to get home, so...."
    zeke "Haha... My bad! I'm sorry."
    scene ep3_145 with dissolve
    wendy "I asked you so many questions, but I forgot to ask you one."
    mika "Hm? What is it?"
    wendy "What do you do for a living?"
    mika "Well, I'm a teacher. I teach high school students."
    wendy "Heh? What subject do you teach?"
    mika "Physical education."
    wendy "Really?!"
    mika "*Giggles*...You seem so surprised to hear that. Why?"
    mika "I don't look like a PE teacher?"
    wendy "To be honest.... No, you don't."
    wendy "You know... You look too kind to be a PE teacher."
    mika "*Giggles*...You aren't the first person to say that to me."
    scene ep3_146 with dissolve
    rin "Heh... You drank quite a lot today, didn't you?"
    rin "I thought you didn't like to drink."
    elaine "Hm? You don't like to drink, [mc]?"
    mc "Well... It's not either about like or dislike. I just didn't see any point to drink."
    mc "But, I think I'm starting to like it now."
    rin "*Giggles*...Good. I've got one more drinking partner now!"
    elaine "Me, too! I'm glad to hear that!"
    scene ep3_147 with dissolve
    elaine "Okay, guys! Now we finished all our food."
    elaine "But, I don't want us to end our dinner party now."
    elaine "How about we find something to do?"
    wendy "Hm? What do you want to do then?"
    scene ep3_148 with dissolve
    elaine "How about we play a game?"
    yui "Hm? What game?"
    elaine "A game that people often play when having a drinking party."
    elaine "Spin the bottle. What do you guys think?"
    zeke "Sounds good. Count me in!"
    wendy "Me, too."
    yui "I know that game, but I've never played it. Let's try it then."
    mika "Well, I have no problem playing if you guys want to play."
    elaine "We can use that bottle of wine. It's empty now, right?"
    yui "Yeah."
    scene ep3_149 with dissolve
    elaine "What about both of you?"
    rin "Sure! Why not?"
    mc "...Okay."
    elaine "Lovely! Then, let's clear the table!"
    scene ep3_150 with dissolve
    elaine "Alright, everyone agreed to play. But, before we start, let's agree on the rules."
    elaine "How about this? Let's combine the rules of Truth or Dare."
    elaine "When the bottle lands on someone, the spinner asks him or her an embarrassing personal question."
    elaine "If she or he decides not to answer, she or he has to perform the dare that the spinner chooses."
    elaine "However, the spinner can choose to let him or her do the dare in the first place without having to ask a question. Your choices!"
    rin "Heh... That's kind of frightening!"
    elaine "*Giggles*...I know right?"
    elaine "Does anyone have any problems with the rules?"
    everyone ".................."
    elaine "Okay then, let's get started!"
    scene ep3_151 with dissolve
    elaine "*Giggles*....Who's going to be the first person pointed by the bottle?"
    $ renpy.pause(0.1, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_157 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_158 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_159 with dissolve
    elaine "*Giggles*...It's you, [wendy]!"
    wendy "Heh.... Why am I so unlucky...?"
    mika "*Sighs*...Lucky me. I thought it was going point at me..."
    yui "...Me, too. I stopped breathing for a sec when the bottle started slowing down while spinning to my direction..."
    scene ep3_160 with dissolve
    elaine "*Giggles*...Hehe..."
    wendy "Wh... Why are you looking at me like that?"
    elaine "Alright I've made my decision...."
    elaine "I dare you to drink a full beer in one shot!"
    scene ep3_161 with dissolve
    wendy "*Giggles*...Okay!"
    zeke "Hey! That doesn't count!"
    elaine "Hm? Why?"
    zeke "It's just a beer. You went too easy on her!"
    elaine "*Giggles*...Just chill. We're just getting started..."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_158 with dissolve
    wendy "Alright, now it's my turn to spin!"
    yui "....Please, don't land on me."
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_155 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_162 with dissolve
    yui "Noooo!"
    mika "*Sighs*...That was close..."
    mika "*Giggles*...I really feel sorry for you, [yui]..."
    scene ep3_163 with dissolve
    yui "*Sighs*...Alright, what do you want me to do?"
    wendy "Relax...I'm just going to ask you a question."
    wendy "It will be really easy question~"
    yui "Judging from your tone of voice, I doubt that..."
    scene ep3_164 with dissolve
    wendy "I'm pretty sure that you don't have a boyfriend."
    wendy "So, I want to ask if you have a crush on someone, and who is that person."
    rin "Heh... I kind of want to know it, too."
    yui "You're cheating! You just asked me two questions, didn't you?"
    wendy "Heh...? You didn't deny that you have a crush on someone."
    yui "!!!!"
    wendy "Alright then, I'll ask you one question."
    wendy "Who is that person you're having a crush on?"
    yui ".........."
    yui "I don't want to answer. Just let me perform the dare."
    wendy "...Are you sure?"
    yui "Yes, I am. What do you want me to do?"
    wendy "(Could it be that that person is also here. That was why she didn't want to answer.)"
    wendy "(Let's see....)"
    scene ep3_165 with dissolve
    wendy "Alright then, I dare you to kiss either [zeke], or [mc]."
    yui "W-What?!!"
    rin "*Giggles*...I never knew you were this cruel, [wendy]! You're showing no mercy at all!"
    wendy "*Giggles*...I'm just playing a game..."
    yui "I can't do it!"
    elaine "You have no choice, [yui]. You must do it."
    elaine "You also agreed with the rules, didn't you?"
    yui "........."
    elaine "Come on! It's just a kiss!"
    yui "....Fine!!"
    scene ep3_166 with dissolve
    yui ".....You."
    mc "Me?"
    yui "Yes. Stand up."
    rin "Hmmm.... So you choose [mc] instead of [zeke]...."
    scene ep3_167 with dissolve
    mc ".........."
    yui "Bend your knees for a bit. You're too tall."
    mc "Okay..."
    everyone "Kiss! Kiss! Kiss!"
    scene ep3_168 with dissolve
    yui "Stay still... *Kisses*"
    mc "........."
    everyone "Boo!... Why are you kissing his cheek? Kiss his lips!"
    yui "Shut up!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_169 with dissolve
    yui "Now, it's time for payback!"
    zeke "Hahaha... She's so mad right now!"
    yui "Cut the crap with the question! I'll announce the dare now!"
    yui "The next person pointed by the bottle, has to take her top off!"
    elaine "*Whistles*...It's getting heated now!"
    yui "(....I'm going to make it land on you, [wendy]!)"
    scene ep3_151 with dissolve
    mika "....I really hope the bottle isn't going to point at me this turn..."
    $ renpy.pause(0.1, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_155 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_170 with dissolve
    yui "No!!! Not again!!"
    zeke "Hahahahaha!"
    rin "*Giggles*...Hahaha... I must say that I didn't expect this...!"
    wendy "*Giggles*...Karma is real..."
    mika "*Giggles*...I got lucky again...hehe..."
    scene ep3_171 with dissolve
    yui ".....Can I do something else?"
    zeke "Of course, you......{w}{b}CAN'T!{/b}"
    wendy "*Giggles*...Hurry up, and take your top off."
    yui "...Fine!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_172 with dissolve
    yui "Are you guys satisfied now?!"
    rin "*Giggles*...Why are you talking as if we were the bad guys...?"
    rin "*Giggles*...You were the one announcing that dare yourself!"
    yui "....Forget it! I'm going to do it again!"
    scene ep3_151 with dissolve
    yui "Next person pointed by the bottle is still going to have to take her top off!"
    yui "I'm sure that it won't land on me again!"
    $ renpy.pause(0.1, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_157 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_173 with dissolve
    yui "Ouch! That was close!"
    wendy "*Giggles*....She surely wanted it to land on me."
    yui "But, this isn't that bad of an outcome though...."
    yui "What are you waiting for, [elaine]? Take off your top now!"
    elaine "*Giggles*...Okay.. Okay..."
    scene ep3_174 with dissolve
    elaine "Alright, I took it off, okay?"
    yui "That's good! Now, you know how embarrassed I am!"
    elaine "Embarrassed? I don't think so."
    elaine "I'm not embarrassed being like this at all. {w}It feels the same as if I was wearing a bikini."
    rin "I know right?!"
    yui "........."
    scene ep3_157 with dissolve
    elaine "Alright, it's my turn again!"
    elaine "But, Let's use the original rule this time..."
    elaine "I'm going to kiss the person whom the bottle points to when it stops."
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_156 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_174_1 with dissolve
    rin "Aw!... It landed on me?!"
    elaine "*Giggles*...[rin]~"
    elaine "*Giggles*...Wait for me right there. I'm coming~"
    yui "*Giggles*...Haha... Karma is real!"
    yui "You were very happy when I had no choice, but to kiss [mc]."
    scene ep3_175 with dissolve
    rin "...Do we... Really have to do this?"
    elaine "Yes, we do!"
    elaine "(To be honest I wanted the bottle to point at [mc], but this isn't that bad.)"
    rin "....Can you just kiss me on the cheek just like [yui] did to [mc]?"
    elaine "No way! I didn't consider that a kiss. Let's show them a real kiss..."
    rin "But....."
    elaine "(*Giggles*....Look at her blusing. She's kind of cute~)"
    elaine "Why? Are you shy? You've never kissed anyone before?"
    zeke "No, she has never kissed anyone before! I can confirm that! Hahaha!"
    if ep3_kiss_rin == 1:
        rin "....Yes, I have."
        zeke "See? What did I... Wait, what?!"
        zeke "Since when did you do that? And whom did you kiss? Why didn't you tell me about it?"
        rin "But, I've never kissed a woman..."
        elaine "Don't worry. It won't be any different..."
    elif ep3_kiss_rin == 2:
        rin "....Yeah, you guys were right. I've never kissed anyone before."
        elaine "Then, let me take your first kiss..."
    scene ep3_176 with dissolve
    elaine "*Kisses*...Mmmm...."
    rin "*Kisses*...Mmmm...."
    zeke "Oooh! They're really kissing!"
    zeke "Damn... That is hot!"
    wendy "I agree...."
    scene ep3_177 with dissolve
    rin "(!!!!)"
    rin "(I didn't expect her to use tongue... What should I do?!)"
    elaine "*Kisses*....Mmmmm...."
    rin "(But, it feels so great... She is so good at kissing...)"
    rin "*Kisses*...Mmmmm...."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_178 with dissolve
    rin "*Ahem*...I'm going to spin the bottle now..."
    yui "*Giggles*...Your face has turned red, [rin]."
    mika "Hehe... We can't blame her for that though...."
    scene ep3_156 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_156 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_179 with dissolve
    rin "The bottle is pointing at you, [mc]."
    elaine "*Giggles*...I bet everyone has been waiting for this moment."
    zeke "Yeah, you're right!"
    wendy "I wonder how this is going to turn out..."
    scene ep3_180 with dissolve
    mc "Okay. What do I have to do?"
    rin "Well, there is one thing that I've always been wanting to see from you."
    rin "*Giggles*...I'm going to dare you to do that!"
    yui "Well, I think I know what it is..."
    scene ep3_181 with dissolve
    mc "Hm? What is it that you want me to do?"
    u "I hope she doesn't ask me to dance or something like that..."
    u "I'd rather kill myself if I had to do it..."
    rin "Relax! I'm not going to ask you to do something you don't like."
    u "Hm? Did she just read my mind, or what?"
    mc "...Okay then, what do you want me to do exactly?"
    scene ep3_180 with dissolve
    rin "I dare you to show us your smile!"
    yui "That's what I was talking about!"
    mc "...That's it?"
    rin "Yeah, so easy, right? Can you smile for me?"
    zeke "Well, to be honest I wanted you to ask him for more, but this is acceptable."
    zeke "I kind of want to see him smile, as well!"
    elaine "I think anyone would want to see it!"
    scene ep3_181 with dissolve
    u "Alright, I think I can do it."
    u "Well, to think about it, I can't remember the last time I smiled."
    mc "Okay then..."
    scene ep3_182 with dissolve
    mc "Is this enough?"
    zeke "Pfff! Hahahaha!!"
    zeke "What are you doing?! Do you call that a smile? Come on!"
    rin "Shut up, [zeke]! He's doing his best. You should give him some respect!"
    elaine "Yeah, she's right! This is the best smile I've ever seen!"
    zeke "...I'm sorry. I should've thought carefully before saying anything..."
    mc "...It's okay."
    mc "Alright, now let me spin the bottle."
    scene ep3_152 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_151 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_152 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene ep3_153 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_158 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_154 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep3_183 with dissolve
    zeke "Ouch! It's pointing at me now, huh?"
    mika "*Giggles*...You just made fun of him. Now, you're in deep trouble, [zeke]."
    scene ep3_184 with dissolve
    zeke "I knew that I was wrong...."
    zeke "Please, have mercy, [mc]."
    mc "Sure."
    scene ep3_185 with dissolve
    mc "What do you really think of [mika]?"
    mika "........"
    rin "Woah... That is really a deadly question."
    zeke "W-What do you mean?"
    mc "I mean what I said."
    rin "(Come on! Just say that you love her!)"
    scene ep3_186 with dissolve
    zeke "Ha!... What kind of question was that?"
    zeke "I'm not going to give you the answer!"
    zeke "You better dare me to do what you want!"
    mika "..........."
    rin "(*Sighs*......He's such a coward)"
    mc "Alright then, I will ask you the same as they did. I dare you to take your top off."
    zeke "Ha! That's very easy!"
    scene ep3_187 with dissolve
    zeke "Just tell me that you want to see my muscles, man!"
    zeke "Here you go!"
    mika "..........."
    elaine "*Giggles*...Haha... What are you doing, dude!"
    scene black with dissolve
    s "*An hour later*........."
    scene ep3_188 with dissolve
    elaine "Hm...? Since when did it get this late? I didn't realise it at all..."
    wendy "Me, too..."
    elaine "Alright, guys. I've had so much fun today, but I think we have to leave now."
    elaine "We still need to go to work tomorrow. So..."
    scene ep3_189 with dissolve
    rin "Yeah, that's right. We still need to go to work tomorrow."
    rin "Alright, let's call it a day then."
    elaine "Yeah, let's call it a day!"
    elaine "Alright, [wendy]. Let's put on our clothes, then leave."
    wendy "Sure."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_190 with dissolve
    elaine "Thanks for such a wonderful dinner, guys."
    elaine "*Giggles*...Too bad I can't stay here any longer, otherwise I'm going to get you guys all naked!"
    yui "There is no way I'm going to let that happen!"
    elaine "*Giggles*...Who knows?"
    scene ep3_191 with dissolve
    rin "Are you sure that you can drive home? You drank quite a lot, too."
    elaine "Yes, I am. Don't worry about me. I'm not even tipsy yet."
    rin "Are you sure?"
    wendy "Yeah, believe her. she usually drinks a lot more than she drank today."
    rin "Alright then, get home safely! I'll see you at work."
    elaine "Goodnight, everyone!"
    yui "Goodnight."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_192 with dissolve
    zeke "Are you okay, [mika]?"
    mika "Hm...? Umm...Ye..Yeah, I'm okay~"
    mika "Just... Open the door... Already~~~!"
    zeke "Calm down... You've got to stand still first..."
    scene ep3_193 with dissolve
    zeke "Goodnight, bro."
    mc "....Sure. You too."
    zeke "See you tomorrow!"
    scene black with dissolve
    s "You went in your bedroom, then went straight to the bed."
    s "But, just before you were about to fall aslep..."
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Knocking*...."
    scene ep3_194 with dissolve
    stop sound
    u "....Hm?"
    u "....Who's knocking on my door at this time...?"
    scene ep3_195 with dissolve
    mc "....Who is it?"
    s "........."
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Knocking*...."
    scene ep3_196 with dissolve
    stop sound
    mc ".....Wait a sec."
    $ renpy.sound.play("sfx/Door opening.mp3")
    scene ep3_197 with dissolve
    stop sound
    stop music fadeout 3.0
    mc "Hm?...[rin]?"
    mc "What are you doing here?"
    scene ep3_198 at eyesblink("Ch.1/Ep.3/Scenes/ep3_198.jpg", "Ch.1/Ep.3/Scenes/ep3_198_blink.jpg", 1) with dissolve
    rin ".........."
    rin "....Can I sleep in your room tonight?"
    mc "What?"
    scene ep3_199 with dissolve
    play music "sfx/ep2_4.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - Out of Time"
    mc "What did you just ask me?"
    rin "........"
    if sexwithrin != 1:
        scene ep3_199_d1 with dissolve
        rin "Nothing. Forget it."
        rin "I'm going back to my room now."
        rin "Sorry to bother you this late at night..."
        scene black with dissolve
        stop music fadeout 3.0
        s "You went back to sleep after [rin] left."
        jump ep3_p2_nextday
    if sexwithrin == 1:
        rin "Can I sleep in your room tonight?"
    u "How should I reply?"
    menu:
        "Let her sleep with you [rin1]":
            $ ep3_sleepwithrin = 1
            $ rin_ch1_ep3 += 1
            $ rin_relationship += 1
            mc "Okay... If that's what you want..."
            rin "...Really?"
            mc "Yeah. Come in."
            scene black with dissolve
            $ renpy.pause()
            jump ep3_p2_sleep
        "No, you can't":
            $ ep3_sleepwithrin = 2
            mc "No, you can't."
            rin "....Oh."
            mc "I'm sorry, but I prefer to sleep alone."
            scene ep3_199_d1 with dissolve
            rin "...Alright, then I'm going back to my room now."
            rin "Sorry to bother you this late at night..."
            scene black with dissolve
            stop music fadeout 3.0
            s "You went back to sleep after [rin] left."
            jump ep3_p2_nextday
label ep3_p2_sleep:
    scene ep3_200 with dissolve
    rin "*Giggles*...Hehe..."
    rin "Thank you for letting me in."
    mc "No worries."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_201 with dissolve
    s "After getting into bed, you and [rin] are trying to sleep. Either of you have said a single word."
    mc "........."
    rin "........."
    scene ep3_202 with dissolve
    rin "........."
    mc "........."
    scene ep3_203 with dissolve
    rin ".....Are you awake?"
    mc "....Yes, I am. Why?"
    rin "....Can I ask you something?"
    scene ep3_204 with dissolve
    mc "...Okay. Ask away."
    rin "....Can you hold me while we sleep?"
    mc "....Do you really want me to do that?"
    rin "Yes, I do."
    mc "........"
    u "To be honest, I didn't even expect myself to let her sleep in my room."
    u "No matter how hard I tried to think about that, {w}I still don't understand why I always chose to improve my relationship with her."
    u "And now she just asked me to hold her while we sleep."
    u "I know that we've already had sex. It doesn't make sense for me to be afraid of holding her."
    u "But that's it. It's just sex. {w}Even though I'm not one of them, many people have sex just for fun."
    u "For me, holding someone while sleeping means so much to me."
    u "It's a way for people to really show their love for each other..."
    rin "....Why did you suddenly become quiet?"
    rin "What do you say?"
    u "....Well, what should I say to her?"
    menu:
        "Okay [rin2]":
            scene ep3_204_a1 with dissolve
            $ ep3_hugwhilesleep = 1
            $ rin_ch1_ep3 += 1
            $ rin_relationship += 1
            mc "...Okay."
            rin "Really? Are you really going to do it?"
            mc "Yes. Come closer."
            rin "*Giggles*...Sure!"
            scene ep3_204_a2 with dissolve
            rin "*Giggles*...Hehe..."
            rin ".....I've never imagined that I would be doing something like this someday."
            rin "I'm so happy right now."
            mc "Just close your eyes, and try to sleep..."
            rin "*Giggles*...As you wish!"
            scene black with dissolve
            s "*A few moments later*......"
            jump ep3_p2_rinhj
        "I don't want to do that":
            scene ep3_204_d1 with dissolve
            $ ep3_hugwhilesleep = 2
            mc "I'm sorry, but I don't want to do that."
            mc "Let's just keep sleeping like this."
            rin ".........."
            rin "....Okay. If you say so..."
            stop music fadeout 3.0
            scene black with dissolve
            $ renpy.pause()
            jump ep3_p2_nextday
label ep3_p2_rinhj:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    scene ep3_204_a3 with dissolve
    rin "........"
    rin "......[mc]."
    mc "........."
    rin "......Did you fall asleep already...?"
    mc "........."
    scene ep3_204_a4 with dissolve
    $ renpy.pause()
    scene ep3_204_a5 with dissolve
    rin ".........."
    scene ep3_204_a6 with dissolve
    mc "...What do you think you're doing?"
    rin "!!!!!"
    scene ep3_204_a7 with dissolve
    rin "I'm sorry! I don't know what I was thinking!"
    rin "Did I wake you up?"
    mc "...No, you didn't. Actually, I didn't fall asleep."
    rin "You should've told me that. So, I wouldn't do such a crazy thing like touching your...."
    rin "...Um... Yeah, you know what I mean."
    mc "Why did you touch it?"
    rin "I don't know either. I'm sorry..."
    mc "You don't need to be sorry. I didn't ask you with anger."
    rin "...Then, can I touch it again?"
    mc "Hm? I don't have a problem with that, but why?"
    rin "I don't know... I just like touching it."
    mc ".....Okay."
    scene ep3_204_a8 with dissolve
    rin "*Giggles*.....Hehe...."
    mc ".........."
    rin "(...Hm... Am I imaging things or is it getting really hard?)"
    rin "(It feels like it's about to explode under his shorts...)"
    rin ".........."
    scene black with dissolve
    u "...Hm?"
    scene ep3_204_a9 with dissolve
    mc "...What are you doing?"
    mc "Why did you take it out of my shorts?"
    rin "Because it seemed uncomfortable hiding in your shorts..."
    mc ".....Are you drunk?"
    rin "*Giggles*...No, I'm not."
    scene ep3_204_a10 with dissolve
    show ep3_rinhj with dissolve
    window hide
    mc "...Then, why are you doing this?"
    mc "...Didn't you tell me that you wanted things to go slowly?"
    rin "...Yes, I did..."
    rin "So, this is the only thing we're going to do for today..."
    $ renpy.pause()
    hide ep3_rinhj with dissolve
    scene ep3_204_a11 with dissolve
    show ep3_rinhj2 with dissolve
    window hide
    rin "...How do you feel...?"
    rin "Am I doing better than last time?"
    mc "...Yeah...."
    rin "*Giggles*...Hehe... Thanks. I'm glad to hear that!"
    $ renpy.pause()
    hide ep3_rinhj2 with dissolve
    scene ep3_204_a12 with dissolve
    show ep3_rinhj3 with dissolve
    window hide
    rin "...Are you about to cum?"
    rin "I can feel it's getting hotter, and hotter...."
    mc "Yeah, I'm almost there."
    rin "*Giggles*...Okay, then feel free to cum whenever you want!"
    menu:
        "Slowest":
            hide ep3_rinhj3 with dissolve
            jump ep3rinhj
        "Slower":
            hide ep3_rinhj3 with dissolve
            jump ep3rinhj2
        "Cum":
            jump ep3rinhjcum
label ep3rinhj:
    scene ep3_204_a10 with dissolve
    show ep3_rinhj with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ep3_rinhj with dissolve
            jump ep3rinhj2
        "Fastest":
            hide ep3_rinhj with dissolve
            jump ep3rinhj3
label ep3rinhj2:
    scene ep3_204_a11 with dissolve
    show ep3_rinhj2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_rinhj2 with dissolve
            jump ep3rinhj1
        "Faster":
            hide ep3_rinhj2 with dissolve
            jump ep3rinhj3
label ep3rinhj3:
    scene ep3_204_a12 with dissolve
    show ep3_rinhj3 with dissolve
    window hide
    menu:
        "Slowest":
            hide ep3_rinhj3 with dissolve
            jump ep3rinhj
        "Slower":
            hide ep3_rinhj3 with dissolve
            jump ep3rinhj2
        "Cum":
            jump ep3rinhjcum
label ep3rinhjcum:
    mc "*Softly breathes*...I'm about to cum..."
    rin "Just cum! Don't hold it back."
    scene black with dissolve
    hide ep3rinhj3 with dissolve
    scene ep3_204_a13 with dissolve
    mc ".....Ah!"
    rin "*Giggles*...Wow! You're cumming quite a lot!"
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ep3_204_a14 with dissolve
    rin "Did you enjoy it?"
    mc "...Yes, I did."
    rin "...Great. I'm glad that you liked it."
    mc "Okay, but now, let me get up first. I need to change my shorts."
    mc "Their covered in my cum now..."
    rin "*Giggles*...Okay!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_204_a15 with dissolve
    mc "Alright, I've changed my shorts. Now, it's really time to sleep."
    mc "Do you mind moving aside?"
    rin "Sure! Let's sleep!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_204_a16 with dissolve
    s "After 15 minutes passed, you and [rin] finally fell asleep...."
    $ renpy.end_replay()
    $ ep3_rinhj = True
    $ rin_ch1_ep3 += 1
    $ rin_relationship += 1
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    jump ep3_p2_nextday
label ep3_p2_nextday:
    play music "sfx/Nextday.mp3" fadein 3.0
    $ bgm = "Bensound - Perception"
    if ep3_rinhj == True:
        unknown "......[mc]."
        u "...Hm? Who's calling me?"
        unknown "....Wake up!"
        scene ep3_205 at eyesblink("Ch.1/Ep.3/Scenes/ep3_205.jpg", "Ch.1/Ep.3/Scenes/ep3_205_blink.jpg", 1) with dissolve
        u "Oh...It's her. I completely forgot that we slept together last night."
        mc "....Good morning, [rin]."
        rin "*Giggles*...Thank god... You're finally up, sleepy boy."
        rin "I've been trying to wake you up for almost five minutes!"
        mc "I'm sorry."
        rin "..........."
        scene ep3_206 with dissolve
        u "Hm...?"
        rin "*Kisses*....Mmmm...."
        u "...Well, I really didn't expect this..."
        $ ep3_rinmorningkiss = True
        $ rin_ch1_ep3 += 1
        $ rin_relationship += 1
        scene ep3_207 at eyesblink("Ch.1/Ep.3/Scenes/ep3_207.jpg", "Ch.1/Ep.3/Scenes/ep3_207_blink.jpg", 1) with dissolve
        rin "*Giggles*...So, this is what a morning kiss feels like..."
        mc ".........."
        rin "There is no need to be sorry! I wasn't angry at you."
        rin "It was actually good for me since I learned one more thing about you."
        rin "You're quite a heavy sleeper, aren't you?"
        mc "....Well, maybe I was just really tired."
        rin "I see..."
        scene ep3_208 with dissolve
        rin "Alright, let's get up now!"
        rin "I'm going to take a shower. We can't be late for work. "
        rin "See you soon, [mc]."
        mc "Okay, see you."
        scene black with dissolve
        $ renpy.pause()
    scene ep3_209 with fade
    liam "We're going to have lunch outside of the company today."
    liam "Do you want to come with us, [mc]?"
    leo "You should come with us, man. {w}It's been a while since we had lunch together."
    david "Yeah, he's right."
    scene ep3_210 with dissolve
    mc "...Thanks for inviting me, but I feel like having lunch at cafeteria today."
    liam "Are you sure?"
    mc "Yes, I am."
    joe "Come on, man. Just come with us!"
    liam "It's okay. I hope you enjoy your lunch!"
    mc "Thanks."
    scene ep3_211 with dissolve
    joe "Why didn't you insist that he should come with us, [liam]?"
    liam "Why should I? It's obvious that he didn't want to come with us."
    joe "[mc].... He's such a weirdo..."
    joe "He always seems to want to be alone."
    joe "Do you really think that's a proper attitude to have towards your co-workers?"
    liam "I have no right to judge him. {w}also, I don't have any problem with his attitude as long as he keeps doing good work."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_212 with dissolve
    mc "......Hi."
    yui "Hey."
    mc "Where are you going to have lunch at?"
    yui "I don't know...."
    yui "I think I'm just going to walk along the street, and find a good restaurant."
    scene ep3_213 with dissolve
    mc "So, you're going to eat outside as well."
    mc "Why didn't you go with them? Didn't they ask you to?"
    yui "Yes, they did, but I refused them."
    mc "Hm? Why?"
    yui "Well, I heard they're going to some Chinese restaurant, {w}but I don't feel like having Chinese food today."
    mc "I see..."
    yui "Alright, I've got to go now. See you around."
    mc "Yeah, see you around."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_214 with fade
    s "Hello, sir. How's your day?"
    mc "....Good, thanks."
    s "What would you like to have for today?"
    mc "I'd like to have set B, please."
    scene ep3_215 with dissolve
    s "Okay, here you are. Enjoy your lunch!"
    mc "Thank you."
    scene ep3_216 with dissolve
    u "....Alright, let's find a place to sit..."
    u ".........."
    scene ep3_217 with dissolve
    u "....Hm?"
    scene ep3_218 with dissolve
    u "....Isn't that [eira]?"
    u "She's having lunch alone as usual."
    u "Well, I saw her with [sally] yesterday, so I thought that she's already got a friend."
    u "But maybe I was wrong..."
    u "Should I go sit with her?"
    menu:
        "Why not? [eira1]":
            $ ep3_lunchwitheira = 1
            $ eira_ch1_ep3 += 1
            $ eira_relationship += 1
            u "Why not? Let's go sit with her."
            scene ep3_218_a1 with dissolve
            eira ".........."
            scene ep3_218_a2 with dissolve
            eira "(.....Hm?)"
            scene ep3_218_a3 with dissolve
            eira "......[mc]?"
            mc "Yes, it's me."
            eira "....What are you doing here?"
            mc "Can I sit with you here?"
            eira "...You've already sat here though..."
            mc "....Yeah, you're right."
            scene ep3_218_a4 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a4.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a4_blink.jpg", 1) with dissolve
            eira ".....By the way, why did you want to sit with me?"
            mc "Well, I saw you sitting here alone. So, I thought you might be lonely."
            eira "....I'm okay. I'm used to being alone already."
            u "...She really reminds me of myself."
            scene ep3_218_a5 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a5.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a5_blink.jpg", 1) with dissolve
            eira "...But, thanks for worrying about me though..."
            if (ep3_lendpen == 1 and givelunchset == True) or (ep3_lendpen == 1 and ep3_waiteira == 1) or ( ep3_waiteira == 1 and givelunchset == True):
                eira "....You've been so nice towards me."
                eira ".....I don't know what I should do for you in return."
                eira "....Actually, I don't... Even know what to say..."
                mc "Relax, you don't need to do or say anything."
                eira "....Okay."
            scene ep3_218_a6 with dissolve
            s "You spend time having lunch with [eira]."
            eira "....Is there something wrong with my face?"
            mc "Hm? No, there isn't."
            mc "Why did you ask?"
            eira "....But, you just kept... Smiling while staring at my face."
            scene ep3_218_a7 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a7.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a7_blink.jpg", 1) with dissolve
            mc "What...? Did I really do that?"
            eira ".....Yes, you did."
            mc "........"
            u "I don't understand why I smiled though..."
            u ".....Could it be that because she really reminded me of myself, so I found it funny?"
            u "Like talking with myself in a mirror, or something like that..."
            if ep3_lendpen == 1:
                u "The only difference between us is that she's too shy to talk with people so she avoids them."
                u "However, I avoid people, because I don't want to improve my relationship with them since they're going to leave me someday anyway."
                u "But not in this case, I have to blend in with people in this company..."
            mc "Anyways, do you mind if I ask you a few questions?"
            eira "...Hm?... Is it an interview or something?"
            mc "No, it isn't. Just normal questions so that I can get to know you better."
            eira "Oh....Okay."
            mc "Then...."
            jump ep3_eira_talk
        "Why should I?":
            $ ep3_lunchwitheira = 2
            u "Why should I? It's none of my business."
            u "Plus, I don't think we're close enough to have lunch together."
            scene ep3_218_d1 with dissolve
            u "Let's go sit right there...."
            scene ep3_218_d2 with dissolve
            u "Let's finish the food, then go back to my department."
            scene black with dissolve
            s "*A few moments later*......"
            scene ep3_218_d2 with dissolve
            crowd "Look! [sally] is talking to [eira]!"
            u "....Hm?"
            scene ep3_218_d3 with dissolve
            crowd "[eira]?! Do you mean our cold angel, [eira]?"
            crowd "What was that dumb question? We've got only one [eira] in the company!"
            crowd "Oh yeah, you're right!"
            crowd "I never knew those girls are friends...."
            u "Well, seems like I wasn't wrong then."
            scene black with dissolve
            $ renpy.pause()
            scene ep3_218_d4 with dissolve
            u "Alright, it's time to go back to my department...."
            scene ep3_218_d5 with dissolve
            sally "Really? You should've just...."
            sally "....Hm?"
            scene ep3_218_d6 with dissolve
            sally "[mc]!!"
            eira "(Hm? That guy...)"
            sally "You are also here? Why didn't I see you?"
            scene ep3_218_d7 with dissolve
            sally "Are you about to leave? Where are you going?"
            mc "Yes, I'm going back to work."
            sally "I see...."
            sally "I'm sorry that I haven't been in touch lately. I was pretty busy moving into a new place."
            mc "New place?"
            scene ep3_218_d9 with dissolve
            sally "Yeah, I just moved to [eira]'s house two days ago."
            u "That's why I saw them going home together yesterday evening..."
            sally "Oh, pardon me. I forgot to introduce him to you."
            sally "This is [mc]."
            eira "....I already know him."
            sally "Really? How do you guys know each other?"
            mc "We met at the meeting yesterday."
            eira ".....Yeah, he's right."
            sally "I see..."
            scene ep3_218_d8 with dissolve
            sally "Oh! By the way, do you want to come hangout at my new place this evening?"
            sally "I've got a gaming console. We can play games together!"
            mc "...You should ask [eira] for her permission first."
            sally "Oh yeah, you're right!"
            scene ep3_218_d9 with dissolve
            sally "Can I invite him to your house, [eira]?"
            eira "..........."
            eira "...Yes, as long as you guys aren't too loud."
            sally "*Giggles*...Hehe... Thanks!"
            scene ep3_218_d8 with dissolve
            sally "Alright, she just said yes."
            sally "Then, what do you say?"
            if sally_reply1_choice == 2:
                sally "You already rejected me last time."
                sally "You aren't going to reject me again, right?"
            u "....How should I answer her?"
            menu:
                "Accept her invitation\n[eira1][smec] & [sally1]":
                    $ ep3_sallyinvite = 1
                    $ sally_ch1_ep3 += 1
                    $ sally_relationship += 1
                    $ eira_ch1_ep3 += 1
                    $ eira_relationship += 1
                    scene ep3_218_d9_a with dissolve
                    mc "Okay."
                    sally "*Giggles*....Great! I knew that you wouldn't let me down!"
                    sally "See you this evening, [mc]!"
                    mc "Sure."
                    scene black with dissolve
                    $ renpy.pause()
                    jump ep3_p2_evening
                "Refuse her invitation":
                    $ ep3_sallyinvite = 2
                    scene ep3_218_d9_d with dissolve
                    mc "Thanks for inviting me, but I'll have to say no."
                    mc "I have something else to do this evening."
                    sally "........."
                    sally "......Okay."
                    scene black with dissolve
                    $ renpy.pause()
                    jump ep3_p2_evening
label ep3_eira_talk:
    menu:
        "Personality":
            if ep3_lendpen == 1:
                mc "You told me that you're shy when talking to people, right?"
                eira "....Yes, I did."
                mc "I want to know why?"
            elif ep3_lendpen == 0 or ep3_lendpen == 2:
                mc "You seem shy when talking to people. I want to know why?"
            scene ep3_218_a8 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a8.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a8_blink.jpg", 1) with dissolve
            eira "....Actually, I think a word 'uncomfortable', suits me more."
            eira "....I feel uncomfortable to talk with people."
            eira "Even right now, I also feel....uncomfortable talking to you."
            mc "Oh... Do you want me to leave then?"
            eira "No...I didn't mean...that you annoyed me."
            eira "It's just.... A long story...."
            eira "....Can we talk about something else?"
            mc "Okay."
            scene ep3_218_a7 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a7.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a7_blink.jpg", 1) with dissolve
            jump ep3_eira_talk
        "Age":
            mc "How old are you?"
            scene ep3_218_a8 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a8.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a8_blink.jpg", 1) with dissolve
            eira "I'm 25."
            $ eira_age = "25"
            mc "....Really?"
            eira "....Why do you seem so shocked?"
            mc "It's just... You look younger."
            eira "......Thanks."
            scene ep3_218_a7 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a7.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a7_blink.jpg", 1) with dissolve
            jump ep3_eira_talk
        "Favorites":
            mc "Can you tell me what are your favorite things to do?"
            eira "....My favorite things to do?"
            mc "Yeah. Give me three things you like the most."
            if eira_like1 == "???" and eira_like2 == "???" and eira_like3 == "???":
                eira "Um...."
                scene ep3_218_a8 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a8.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a8_blink.jpg", 1) with dissolve
                eira ".....I like to listen to pop music the most."
                $ eira_like1 = "Pop music"
                eira "I always listen to pop music when working at home."
                mc "Yeah, listening to music when working really helps to keep you entertained."
                eira "I know right?"
                eira "...And I also like cooking."
                $ eira_like2 = "Cooking"
                mc "...And the last one?"
                eira "....Cats. They're so lovely."
                $ eira_like3 = "Cats"
                mc "I see.... I have someone I know that also love cats, too."
                eira "...Really?"
                mc "Yeah, I'm sure you can get along with her pretty well."
                scene ep3_218_a7 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a7.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a7_blink.jpg", 1) with dissolve
                jump ep3_eira_talk
            else:
                eira "Hm...?"
                eira "....Didn't we already talk about it?"
                mc "Yeah... You're right."
                jump ep3_eira_talk
        "Dislikes":
            mc "What about things you dislike?"
            eira "Things I dislike?"
            mc "Yeah. Tell me three things that you dislike the most."
            if eira_hate1 == "???" and eira_hate2 == "???" and eira_hate3 == "???":
                eira "Um...."
                scene ep3_218_a8 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a8.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a8_blink.jpg", 1) with dissolve
                eira ".....I don't like loud noises the most"
                $ eira_hate1 = "Loud noises"
                eira ".....I get shocked so easy. It's also... Dangerous for your ears..."
                mc "I agree with you."
                eira ".....I also don't like lizards, and snakes."
                eira "...They're so scary..."
                $ eira_hate2 = "Lizards"
                $ eira_hate3 = "Snakes"
                scene ep3_218_a7 at eyesblink("Ch.1/Ep.3/Scenes/ep3_218_a7.jpg", "Ch.1/Ep.3/Scenes/ep3_218_a7_blink.jpg", 1) with dissolve
                mc "I see..."
                jump ep3_eira_talk
            else:
                eira "Hm...?"
                eira "....Didn't we already talk about it?"
                mc "Yeah... You're right."
                jump ep3_eira_talk
        "End conversation":
            scene black with dissolve
            $ renpy.pause()
            scene ep3_218_a9 with dissolve
            sally "Heh~? [mc]?"
            u "Hm...?"
            mc "...[sally]?"
            sally "Well, I didn't expect to see you here with [eira]."
            sally "Since when do you guys know each other?"
            mc "....I've been hearing her name for a while, but technically, I've known her since yesterday."
            scene ep3_218_a10 with dissolve
            sally "I see...."
            sally "By the way, can I sit with you guys here?"
            eira "...Yes, you can."
            mc "I'm okay with that."
            scene ep3_218_a11 with dissolve
            crowd "Look! [sally] is sitting with those guys!"
            crowd "Who's she sitting with?"
            crowd "....[eira]... And who is that guy? Why have I never seen him before?"
            crowd "Really?! Is she really sitting with that cold angel, [eira]?"
            sally "Well, it's good to see that you guys know each other."
            sally "You know.... [eira] doesn't have a lot of friends around here."
            sally "Please, take care of her, okay?"
            mc "....Okay."
            sally "*Giggles*...Thanks!"
            mc "Actually, I also never knew [eira] had a friend until I saw you guys together yesterday evening."
            sally "Oh?! Did you see us?"
            scene ep3_218_a12 with dissolve
            mc "Yes. How long have you guys been going home together?"
            mc "Why has nobody ever noticed that?"
            eira "....The thing is, yesterday was.... The first day we went home together."
            mc "Yeah?"
            sally "Yeah, I just moved into her house the day before yesterday."
            scene ep3_218_a13 with dissolve
            mc "Hm? How come?"
            sally "Well, I had some problems with my housemates lately."
            sally "She's been playing her guitar too loud at night. I asked her to lower the volume down so many times."
            sally "She did lower it down when I asked her to, but just for a few days before it's back to normal."
            scene ep3_218_a12 with dissolve
            sally "So, I was in search of a new house to live in until I saw a nice room for rent on the internet."
            sally "And it turned out to be [eira] who was looking for a tenant."
            eira "....Yeah, I don't use that room... So I decided to rent it out."
            scene ep3_218_a13 with dissolve
            sally "By the way, since we're talking about my new room, do you want to come to come over and hangout?"
            sally "I've got a gaming console. We can play games together!"
            mc "...You should ask [eira] for her permission first."
            sally "Oh yeah, you're right!"
            scene ep3_218_a12 with dissolve
            sally "Can I invite him to your house, [eira]?"
            eira "..........."
            eira "...Yes, as long as you guys aren't too loud."
            sally "*Giggles*...Hehe... Thanks!"
            scene ep3_218_a13 with dissolve
            sally "Alright, she just said yes."
            sally "Then, what do you say?"
            if sally_reply1_choice == 2:
                sally "You already rejected me last time."
                sally "You aren't going to reject me again, right?"
            u "....How should I answer her?"
            menu:
                "Accept her invitation\n[eira1][smec] & [sally1]":
                    $ ep3_sallyinvite = 1
                    $ sally_ch1_ep3 += 1
                    $ sally_relationship += 1
                    $ eira_ch1_ep3 += 1
                    $ eira_relationship += 1
                    scene ep3_218_a13_a with dissolve
                    mc "Okay."
                    sally "*Giggles*....Great! I knew that you wouldn't let me down!"
                    sally "Alright, now let's finish our food before the lunch break ends."
                    mc "Sure."
                    scene black with dissolve
                    $ renpy.pause()
                    jump ep3_p2_evening
                "Refuse her invitation":
                    $ ep3_sallyinvite = 2
                    scene ep3_218_a13_d with dissolve
                    mc "Thanks for inviting me, but I'll have to say no."
                    mc "I have something else to do this evening."
                    sally "........."
                    sally "......Okay."
                    scene black with dissolve
                    $ renpy.pause()
                    jump ep3_p2_evening
label ep3_p2_evening:
    if ep3_sallyinvite == 1:
        if zeke_contact == False:
            $ zeke_contact = True
        $ ep3_sallymessage = True
        $ newmessage = True
        $ sally_messages_show = True
        $ sally_newmessage = True
        $ phone_alert = True
        $ zeke_messages_show = True
        $ zeke_newmessage = True
        scene ep3_219 with dissolve
        stop music fadeout 3.0
        u "[sally] and [eira] are waiting for me in the parking lot."
        u "Let's hurry up. I don't want to keep them waiting."
        scene black with dissolve
        $ renpy.pause()
        jump ep3_p2_hangout
    elif ep3_sallyinvite == 2:
        scene ep3_219 with dissolve
        u "It's already 5 p.m."
        u "Let's get off work, and go home."
        jump ep3_p2_nohangout
label ep3_p2_nohangout:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ep3_219_d1 with fade
    u "Alright, I've finally arrived home."
    u "Let's go to my room...."
    scene ep3_219_d2 with dissolve
    u "Let's turn on the computer, and learn more about the code of Xecon Gear...."
    $ ep3_rinmessage3 = True
    $ newmessage = True
    $ rin_messages_show = True
    $ rin_newmessage = True
    $ phone_alert = True
    scene black with dissolve
    s "After learning the code for a few hours, you got so hungry that you decided to go downstairs...."
    jump ep3_p2_firstnight
label ep3_p2_hangout:
    play music "sfx/ep.3/ep3_10.mp3" fadein 3.0
    $ bgm = "Peyruis - Triomphe"
    scene ep3_219_a1 with fade
    sally "Alright, here we are!"
    sally "*Giggles*....Welcome to [eira]'s house!"
    mc ".........."
    scene ep3_219_a2 with dissolve
    u "So, this is what her house looks like...."
    u "It looks so nice and clean..."
    scene ep3_219_a3 with dissolve
    sally "What do you think?"
    sally "It's so beautiful, right?"
    sally "I fell in love with her house since the first time I saw it."
    eira "....You're over exaggerating..."
    sally "No, I'm not! I really love your house!"
    sally "I've been dreaming of having a house like this to be honest!"
    menu:
        "Compliment on [eira]'s house [eira1]":
            $ ep3_complimenthouse = 1
            $ eira_ch1_ep3 += 1
            $ eira_relationship += 1
            scene ep3_219_a3_a1 with dissolve
            mc "Yeah, it's really beautiful."
            mc "I also like your house, too."
            eira "Oh...."
            eira ".....Thank you."
            mc "You managed to own a nice house at a very young age. You've earned my respect."
            eira "Er...."
            scene ep3_219_a3_a2 with dissolve
            eira "....Actually, this isn't my house.... I didn't buy it."
            mc "........."
            mc "....Then, whose house is this?"
            eira ".....This is my parents house."
            mc "I see.... So, you're living with your parents right now?"
            eira ".....No, I'm not. They went to work abroad two years ago..."
            scene ep3_219_a3_a3 with dissolve
            sally "Er...guys."
            mc "Hm?"
            sally "Let's get inside the house first."
            sally "You guys can continue talking later."
            eira "Oh... Okay."
        "Stay quiet":
            $ ep3_complimenthouse = 2
            mc ".........."
            scene ep3_219_a3_d with dissolve
            sally "Alright, let's not waste anymore time here."
            sally "Get inside the house!"
            eira "....Yeah, you're right."
            mc "Okay. Let's go then."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_219_a4 with dissolve
    sally "Alright, you can sit, and wait for me here."
    sally "My room is kind of a mess right now. I'm going to clean it up first."
    sally "*Giggles*...I don't want to freak you out by how mess up my room is!"
    mc "....Okay."
    scene ep3_219_a5 with dissolve
    mc ".........."
    scene ep3_219_a6 with dissolve
    u "[eira]'s really got a nice house."
    u "This house doesn't look beautiful only from the outside, it also looks nice inside as well."
    u "I like how minimalist it is...."
    u "If I was going to buy a house in the future, I'd buy a house like this."
    scene ep3_219_a7 with dissolve
    u "....But I wonder if it's ever going to be possible for me..."
    u "No... I don't have a normal life like other people."
    u "Since the moment that I chose to receive help from [victor], {w}my life was no longer mine..."
    u "But, what could I have done?"
    u "I probably would've ended up dead, if I had chosen to stay on the street..."
    u "I know that what I did back then at the company, was really bad."
    u "But, there was nothing I could do, but to obey his orders."
    u "If I didn't do that, I'd probably end up being abandoned again..."
    scene ep3_219_a8 with dissolve
    u "Twice is already enough... I won't let it happen again..."
    eira ".....[mc]."
    u "....Hm?"
    scene ep3_219_a9 with dissolve
    mc "....[eira]?"
    eira "........"
    mc "Did you call me?"
    eira "....Yes, I did."
    scene ep3_219_a10 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a10.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a10_blink.jpg", 1) with dissolve
    mc "Is there something that you want from me?"
    eira "....No, I don't want anything from you."
    eira ".... I just wanted to.... Give you this cup of water."
    eira "....Take it."
    u "What should I do?"
    menu:
        "Take it [eira1]":
            $ ep3_takecupofwater = 1
            $ eira_ch1_ep3 += 1
            $ eira_relationship += 1
            scene ep3_219_a10_t at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a10_t.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a10_t_blink.jpg", 1) with dissolve
            mc "Oh... I've been thristy for a while."
            mc "Thank you, [eira]. You're so kind."
            eira "....No, I'm not."
            eira "....I'm just doing what... A good host should do."
            eira "....But, I'm happy that I can help you."
        "Don't take it":
            $ ep3_takecupofwater = 2
            scene ep3_219_a10_r at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a10_r.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a10_r_blink.jpg", 1) with dissolve
            mc "....Thanks, [eira]."
            mc "But, I'm not thristy."
            eira "Oh.... I'm sorry"
            eira "....The weather is quite hot today... So I thought you would want a cup of water."
            mc ".....It's okay. You don't have to be sorry."
            eira ".....I get it."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_219_a11 with dissolve
    s "While you're waiting for [sally], [eira] decided to sit down right next to you...."
    mc "....What's happening? You look a little bit unhappy."
    eira "....Hm?"
    scene ep3_219_a12 with dissolve
    eira "Oh.... I'm not unhappy."
    eira "I just feel.... A bit stressed."
    mc "Hm...? Why?"
    eira "I'm searching for a female model to shoot an advertisement."
    eira "But, I still haven't found the one I think is the best for this project yet."
    mc "Aren't they beautiful enough?"
    eira "...It isn't just about beauty. You also have to consider if she is suitable."
    mc "I see...."
    sally "Guys!"
    scene ep3_219_a13 with dissolve
    mc "....Hm?"
    eira "........."
    scene ep3_219_a14 with dissolve
    sally "I finished cleaning up my room."
    sally "Let's go! Follow me!"
    mc "....Okay."
    scene ep3_219_a15 with dissolve
    sally "Hm...?"
    sally "Why are you still sitting there, [eira]?"
    sally "Come on! Hurry up!"
    eira "Hm...? You want me to go with you guys, too?"
    sally "Of course! Why not?"
    sally "Stop thinking about work for now. Let's just relax, and have fun!"
    eira "Oh....Okay then."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_219_a16 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a16.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a16_blink.jpg", 1) with fade
    sally "And....."
    sally "......Here we are!"
    sally "Welcome to my new room!"
    mc "............"
    scene ep3_219_a17 with dissolve
    sally "What do you think, [mc]?"
    mc "Hm? Why don't you ask [eira] instead?"
    sally "Why should I ask her? She has already seen this room a million times!"
    eira "Er... It hasn't been that many times..."
    sally "*Giggles*....I know! It was just a metaphor!"
    sally "So, what do you think, [mc]?"
    mc "..........."
    menu:
        "I like it [sally1]":
            $ ep3_complimentroom = 1
            $ sally_ch1_ep3 += 1
            $ sally_relationship += 1
            scene ep3_219_a18 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a18.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a18_blink.jpg", 1) with dissolve
            mc "It looks great. I like it."
            sally "Yeah? Do you really like it?"
            mc "Yes, I do."
            sally "*Giggles*....Hehe... Thanks."
        "I have no complaint":
            $ ep3_complimentroom = 2
            scene ep3_219_a19 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a19.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a19_blink.jpg", 1) with dissolve
            mc "I have no complaint."
            sally ".....Don't you like it?"
            mc "It's your bedroom. It doesn't matter if I like it or not."
            sally "Oh.... Okay."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_219_a20 with dissolve
    sally "Alright, let's not waste anymore time."
    sally "Here is your controller!"
    mc "Thanks..."
    scene ep3_219_a21 with dissolve
    sally "Okay, then... What game do you guys want to play?"
    mc "....I don't want to play anything in specific."
    mc "Just choose the one you want. I'm fine with it."
    sally "....What about you, [eira]?"
    eira "....I'm not going to play... So, please don't ask me."
    sally "Hm? Why aren't you going to play?"
    eira "....Because.... I'm not good at playing games...."
    sally "Alright then, I'll choose the game myself."
    scene ep3_219_a22 with dissolve
    sally "I've just chosen Tekken. Are you okay with that?"
    mc "Yes, I am."
    sally "*Giggles*....You look so chill. I bet you've got some skills, hm?"
    mc "....No, I don't."
    sally "*Giggles*....Stop being humble. I can feel a strong aura around you!"
    mc "Wait...... What?"
    sally "I don't know how good you are, so I will go all out from the start!"
    mc "*Sigh*......."
    scene ep3_219_a23 with dissolve
    sally "Yes! Take that!"
    mc "........."
    sally "Hey... Hey... What are you doing, [mc]?!"
    sally "Stop going easy on me already!"
    scene black with dissolve
    s "*Half a minute later*........"
    scene ep3_219_a24 with dissolve
    sally "Yes! I won!"
    mc ".........."
    eira "You're so good, [sally]..."
    scene ep3_219_a25 with dissolve
    sally "*Giggles*....Heh~"
    mc "....What?"
    sally "Now, I'm starting to wonder if you went easy on me, or if you're a noob..."
    mc "...A what?"
    sally "*Giggles*....Nothing!"
    scene ep3_219_a26 with dissolve
    mc "You invited me to hang out here, so I thought we would be playing games for fun."
    mc "But, seems like I misunderstood you...."
    sally "*Giggles*....Hehehe..."
    mc "It's fine. Now, I'm going to take this serious."
    sally "Good! I'm glad to hear that. Show me what you can do!"
    scene black with dissolve
    s "*One minute later*......."
    scene ep3_219_a27 with dissolve
    mc "..........."
    sally "Oops...! Did you really take it serious?"
    mc "....I'm just warming up."
    sally "*Giggles*....Alright, let's go another round then!"
    $ ep3_rinmessage3 = True
    $ newmessage = True
    $ rin_messages_show = True
    $ rin_newmessage = True
    $ phone_alert = True
    scene black with dissolve
    s "*Half an hour later*........"
    scene ep3_219_a28 with dissolve
    sally "*Sighs*....What should I do.....?"
    sally "I won again. This is my 15th consecutive win already..."
    sally "But this time you managed to not get beaten in a perfect game. Congrats!"
    mc "............"
    scene ep3_219_a29 with dissolve
    mc "Another round!"
    eira "....Calm down, [mc]."
    eira "....It's just a game...."
    sally "*Giggles*....I can't believe what I'm seeing."
    sally "Are you really angry?"
    mc "*Sighs*........"
    scene ep3_219_a30 with dissolve
    sally "Alright, let's just calm down for a bit."
    sally "You should play with him, [eira]."
    eira "....But, I'm not good at it."
    sally "Don't worry. I'll teach you how to play it."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_219_a31 with dissolve
    sally "Alright, step back... Step back..."
    eira "Oh....."
    sally "Now, lower kick, then finish him!"
    mc ".........."
    scene ep3_219_a32 with dissolve
    sally "Good job! You followed my orders very well!"
    eira "...Did I really win?"
    sally "Yes, you did!"
    eira "....I can't believe it..."
    scene ep3_219_a33 with dissolve
    sally "Hm...?"
    sally "Why did you suddenly stand up?"
    sally "Do you want to go to the toilet?"
    eira "....Do you need me to show you the way?"
    scene ep3_219_a34 with dissolve
    mc "No, I'm not going to the toilet."
    mc "I'm going home."
    sally "!!!!!"
    scene ep3_219_a35 with dissolve
    eira "(....He must be really angry....)"
    eira "(....I should've let him win.)"
    sally "Come on.... Don't be so childish. It's just a game..."
    mc ".........."
    sally "....Wait! Don't leave like t-"
    scene ep3_219_a36 with dissolve
    sally "Ouch!!"
    scene ep3_219_a37 with dissolve
    eira "[sally]!"
    sally "Aww!!"
    eira "(No!... It's too late! I can't reach her in time!)"
    mc ".........."
    menu:
        "Help her [eira2][smec] & [sally3]":
            scene black with dissolve
            $ renpy.pause()
            scene ep3_219_a37_a1 with dissolve
            sally "Ouch....!"
            mc ".....Are you okay?"
            sally "........."
            sally ".....Yeah. I'm okay..."
            u "Hm...? This feeling...."
            u "Don't tell me that...."
            scene ep3_219_a37_a2 with dissolve
            u "....She isn't wearing a bra...."
            u "............."
            u ".....Yeah, she isn't wearing one."
            u "I can feel her tits touching my body..."
            scene ep3_219_a37_a3 with dissolve
            u "....Hm?"
            u "What is this feeling coming from my left hand?"
            u "It's so...."
            scene ep3_219_a37_a4 with dissolve
            u "....soft."
            eira "[sally], are you o-"
            sally "Mmm....!!"
            scene ep3_219_a37_a5 with dissolve
            eira "....Hm?"
            sally "...D...Don't squeeze it..."
            scene ep3_219_a37_a6 with dissolve
            eira "..........."
            mc "I'm sorry....."
            mc "I didn't mean to...."
            sally "..........."
            sally "It's okay. I know you didn't...."
            mc "Thank you for understanding me."
            scene black with dissolve
            $ renpy.pause()
            $ ep3_helpsally = 1
            $ sally_ch1_ep3 += 3
            $ sally_relationship += 3
            $ eira_ch1_ep3 += 2
            $ eira_relationship += 2
            scene ep3_219_a37_a7 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a37_a7.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a37_a7_blink.jpg", 1) with dissolve
            sally "Hehe.... How clumsy I was...."
            sally "Thanks a lot for helping me... Again."
            eira "....Thanks for helping her, [mc]."
            mc "You're welcome."
            sally "By the way, I'm so sorry that I teased you so much today."
            sally "I shouldn't have done that...."
            mc "It's okay...."
            scene ep3_219_a37_a8 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a37_a8.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a37_a8_blink.jpg", 1) with dissolve
            sally "You aren't angry at us anymore, right?"
            mc "No, I'm not actually angry at you guys."
            u "Actually, I was angry at how bad I was..."
            sally "....Hm? Then, why did you suddenly want to go home?"
            mc "Well... It's getting dark out. So, I thought it was the time for me to leave."
            eira "Oh.... That's why...."
            sally "Hey. Why don't you have dinner with us before leaving?"
            mc "Thanks for asking, but I think I prefer to go home now."
            sally ".....Alright then, let me drive you home!"
            mc "....You don't have to..."
            sally "What are you talking about? Of course, I do!"
            sally "I invited, and brought you here. So, let me take you back home!"
            menu:
                "Let her take you home\n[eira1][smec] & [sally1]":
                    $ ep3_takehome = 1
                    $ sally_ch1_ep3 += 1
                    $ sally_relationship += 1
                    $ eira_ch1_ep3 += 1
                    $ eira_relationship += 1
                    scene ep3_219_a37_a9 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a37_a9.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a37_a9_blink.jpg", 1) with dissolve
                    mc "Alright, if you insist..."
                    mc "I'll let you drive me home then."
                    sally "*Giggles*.....Hehe....."
                    eira "....I'll go with you, too."
                    sally "Hm? Are you sure?"
                    eira ".....Yeah, so you won't be lonely on the way back."
                    sally "*Giggles*....Aw!... How cute you are!"
                    scene black with dissolve
                    $ renpy.pause()
                    scene ep3_220_a1 with fade
                    mc "Thank you for taking me home."
                    sally "No worries!"
                    sally "Let's hang out together again soon!"
                    scene ep3_220_a2 with dissolve
                    mc "..........."
                    mc "By the way, do you guys want to come inside to have a cup of water before leaving?"
                    sally "Thanks for inviting us, but next time, okay?"
                    sally "We want to go home before it gets too late."
                    eira "...Yeah, she's right."
                    mc "Okay then, drive safely."
                    sally "*Giggles*...Hehe... Thanks. See you soon!"
                    jump ep3_p2_firstnight
                "I can go home by myself":
                    $ ep3_takehome = 2
                    scene ep3_219_a37_a10 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a37_a10.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a37_a10_blink.jpg", 1) with dissolve
                    mc "No. I don't want to bother you guys."
                    mc "So, just let me go home by myself."
                    sally ".....Are you sure?"
                    mc "Yes, I am."
                    sally ".....Okay then...."
                    eira "................"
                    jump ep3_p2_firstnight
        "Let her fall":
            scene black with dissolve
            $ renpy.pause()
            scene ep3_219_a37_d1 with dissolve
            sally "Ouch!!...."
            eira "[sally]!"
            mc "............"
            scene ep3_219_a37_d2 with dissolve
            eira "....Are you okay?"
            eira "....You aren't injured, right?"
            sally "Hehe... I'm okay. I'm not injured."
            sally "Thanks for worrying about me, [eira]."
            scene ep3_219_a37_d3 with dissolve
            eira "..........."
            mc "..........."
            eira "....What have you done? Why didn't you catch her?"
            $ ep3_helpsally = 2
            sally "It's okay, [eira]. Don't be angry at him."
            sally "It wasn't his fault. It was mine."
            sally "...Hehe... If you wanted to blame him, then you better blame me for my clumsiness."
            scene ep3_219_a37_d4 with dissolve
            eira "..........."
            sally "I'm sorry, [mc]. She was just too worried about me."
            sally "Please, don't be mad at her, okay?"
            mc "....Yeah, I know that."
            sally "You helped me from falling to the ground last time..."
            sally "But, you were too shocked to catch me this time, right?"
            sally "It's okay. I don't blame you for that."
            scene ep3_219_a37_d5 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a37_d5.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a37_d5_blink.jpg", 1) with dissolve
            sally "By the way, I'm so sorry that I teased you so much today."
            sally "I shouldn't have done that...."
            mc "It's okay...."
            sally "You aren't angry at us anymore, right?"
            mc "No, I'm not actually angry at you guys."
            u "Actually, I was angry at how bad I was..."
            sally "....Hm? Then, why did you suddenly want to go home?"
            mc "Well...It's getting dark out. So, I thought it was the time for me to leave."
            sally "Oh.... That's why...."
            sally "Hey. Why don't you have dinner with us before leaving?"
            mc "Thanks for asking, but I think I prefer to go home now."
            sally ".....Alright then, let me drive you home!"
            mc "....You don't have to..."
            sally "What are you talking about? Of course, I do!"
            sally "I invited, and brought you here. So, let me take you back home!"
            menu:
                "Let her take you home [sally1]":
                    $ ep3_takehome = 1
                    $ sally_ch1_ep3 += 1
                    $ sally_relationship += 1
                    scene ep3_219_a37_d6 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a37_d6.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a37_d6_blink.jpg", 1) with dissolve
                    mc "Alright, if you insist..."
                    mc "I'll let you drive me home then."
                    sally "*Giggles*.....Hehe....."
                    sally "Okay then, let's go!"
                    scene black with dissolve
                    $ renpy.pause()
                    scene ep3_220_d1 with fade
                    mc "Thank you for taking me home."
                    sally "No worries!"
                    sally "Let's hang out together again soon!"
                    scene ep3_220_d2 with dissolve
                    mc "..........."
                    mc "By the way, do you want to come inside to have a cup of water before leaving?"
                    sally "Thanks for inviting me, but next time, okay?"
                    sally "[eira]'s waiting for me inside the car."
                    sally "She wants to go home before it gets too late."
                    mc "Okay then, drive safely."
                    sally "*Giggles*...Hehe... Thanks. See you soon!"
                    jump ep3_p2_firstnight
                "I can go home by myself":
                    $ ep3_takehome = 2
                    scene ep3_219_a37_d7 at eyesblink("Ch.1/Ep.3/Scenes/ep3_219_a37_d7.jpg", "Ch.1/Ep.3/Scenes/ep3_219_a37_d7_blink.jpg", 1) with dissolve
                    mc "No. I don't want to bother you guys."
                    mc "So, just let me go home by myself."
                    sally ".....Are you sure?"
                    mc "Yes, I am."
                    sally ".....Okay then...."
                    eira "................"
                    jump ep3_p2_firstnight
label ep3_p2_firstnight:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene ep3_221 at eyesblink("Ch.1/Ep.3/Scenes/ep3_221.jpg", "Ch.1/Ep.3/Scenes/ep3_221_blink.jpg", 1) with fade
    if ep3_sallyinvite == 1:
        zeke "Oh, you're finally back!"
        zeke "Welcome home, bro!"
        mc "Hm? Have you been waiting for me?"
        zeke "No, I haven't. I've been watching TV back there with [mika]."
        mc "I see...."
        zeke "Have you had dinner yet? If not, [rin] already cooked you dinner."
    elif ep3_sallyinvite == 2:
        zeke "[mc]."
        mc "Hm?... What?"
        zeke "[rin] told me to tell you that she already cooked you dinner."
    zeke "Your food is in the refrigerator. Just take it out, put it in the microwave."
    mc "Thanks for telling me."
    zeke "Anytime, man."
    mc "By the way, where is [rin]?"
    zeke "She's probably working in her room right now. She's been busy lately."
    mc "I see...."
    zeke "Alright then, enjoy your dinner! I'm going back to watch TV with [mika] now."
    mc "Sure. I hope you have a nice time watching TV with her, too."
    $ zeke_relationship += 1
    $ zeke_ch1_ep3 += 1
    scene black with dissolve
    $ renpy.pause()
    scene ep3_222 with dissolve
    s "You spend your time eating dinner....."
    scene black with dissolve
    s "*Half an hour later*....."
    scene ep3_223 with dissolve
    u "Alright, let's go to my room...."
    u "....Hm?"
    mc "....Just finished taking a shower?"
    yui "Hm...?"
    scene ep3_224 with dissolve
    yui "[mc]?"
    yui "What do you want?"
    mc "Nothing..."
    mc "I'm on the way to my room, but I saw you so I decided to say hey."
    yui "Is that so...?"
    mc "Yeah...."
    mc "Alright, I won't bother you anymore. See you tomorrow."
    scene ep3_225 at eyesblink("Ch.1/Ep.3/Scenes/ep3_225.jpg", "Ch.1/Ep.3/Scenes/ep3_225_blink.jpg", 1) with dissolve
    yui "Wait."
    mc "...Hm? Is there something that you want from me?"
    yui "Can you follow me inside for a sec?"
    mc "Hm? Why?"
    yui "Actually, before I decided to take a shower, I was working."
    yui "I want you to come and see if there is something that I should improve with my work."
    menu:
        "Accept [yui1]":
            $ ep3_helpyui = 1
            $ yui_ch1_ep3 += 1
            $ yui_relationship += 1
            mc "I don't know if I can help, but... Okay."
            scene ep3_225_a1 with dissolve
            yui "You already helped me since you decided to accept my request."
            yui "Thank you."
            mc "....You're welcome."
            u "To be honest... I'm really not used to her being nice like this...."
            yui "Alright, follow me then."
            scene black with dissolve
            $ renpy.pause()
            scene ep3_225_a2 with dissolve
            yui "Alright, here it is."
            yui "It's one of the maps that are going to be in the game."
            yui "I want to get some feedback from someone close to me first. What do you think?"
            mc "Um...."
            menu:
                "It looks fantastic [yui1]":
                    $ ep3_givesuggestion = 1
                    $ yui_ch1_ep3 += 1
                    $ yui_relationship += 1
                    scene ep3_225_a2_a with dissolve
                    mc "It looks fantastic."
                    yui "Really? You didn't say that just to make me happy, right?"
                    mc "No, I didn't. I really meant what I said."
                    yui "What about things that should be improved?"
                    scene ep3_225_a2 with dissolve
                    mc "Umm... I can't give you a suggestion in deep details since it isn't in a scope of my skills..."
                    mc "But, I think maybe... You should make it look less scifi?"
                    mc "I don't think sci-fi is the games main theme."
                    yui "....Yeah, I think you're right about that."
                    yui "Okay, thanks for your help."
                    mc "....You're welcome."
                "I don't know":
                    $ ep3_givesuggestion = 2
                    scene ep3_225_a2_d with dissolve
                    mc "I don't know...."
                    yui "What do you mean you don't know?"
                    mc "....Well, your work isn't in a scope of my skills."
                    mc "So, I don't know what to say..."
                    yui "*Sighs*...Okay, fair enough. I can't blame you for that."
                    yui "Alright then, I won't bother you anymore."
                    yui "Thanks for trying to help at least."
                    mc "....You're welcome."
        "Refuse":
            $ ep3_helpyui = 2
            mc "I'm sorry, but I don't think I can help you."
            mc "Your work isn't in a scope of my skills."
            scene ep3_225_d with dissolve
            yui "Can't you at least try to help?"
            mc "I'm sorry to say this, but I don't want to give you wrong suggestions."
            yui "Fine... Then, you can go to your room now."
            yui "I won't bother you anymore."
            mc "Okay."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_226 with dissolve
    u "Alright, let's get inside my room, and pick up some clothes."
    u "It's been a long day. I'm so tired, and sweaty right now."
    u "I better go take a shower now."
    scene black with dissolve
    s "*Twenty minutes later*......"
    scene ep3_227 with dissolve
    u "Alright, I finished taking a shower. I feel a lot better now."
    u "What should I do next....?"
    u "Um.... I don't want to do anything specific...."
    u "Let's just turn on the computer, and learn more about the code of Xecon Gear then."
    if ep3_givephonenumber == 1:
        $ renpy.sound.play("sfx/phone vibrating.mp3")
        s "*Phone vibrates*......"
        u "Hm....?"
        stop sound fadeout 3.0
        $ ep3_krystalmessage1 = True
        $ newmessage = True
        $ krystal_messages_show = True
        $ krystal_newmessage = True
        $ phone_alert = True
        scene ep3_228 with dissolve
        u "I've got a message. Let's see who sent it to me."
        jump messagefromkrystal
    else:
        scene ep3_228_d with dissolve
        s "You spend your time learning Xecon Gear's code."
        jump ep3_p2_endfirstnight
label messagefromkrystal:
    if reply_krystal1 == False:
        scene ep3_228 with vpunch
        u "I need to reply the message first!"
        jump messagefromkrystal
    elif reply_krystal1 == True:
        jump ep3_afterreplytokrystal
label ep3_afterreplytokrystal:
    if krystal_reply1_choice == 1:
        jump ep3_p2_hangoutwithkrystal
    elif krystal_reply1_choice == 2:
        stop music fadeout 3.0
        jump ep3_p2_learncode
label ep3_p2_learncode:
    scene ep3_228_d with dissolve
    s "You spend your time learning Xecon Gear's code."
    jump ep3_p2_endfirstnight
label ep3_p2_hangoutwithkrystal:
    u "Alright then, let's go to [krystal]'s room."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_228_a1 with fade
    u "Okay, I've arrived here."
    u "She told me to knock five times, right?"
    u "Let's do what she said then..."
    scene ep3_228_a2 with dissolve
    s "*Knocks*........."
    $ renpy.sound.play("sfx/Door opening.mp3")
    s "*Door opens*........"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_228_a3 at eyesblink("Ch.1/Ep.3/Scenes/ep3_228_a3.jpg", "Ch.1/Ep.3/Scenes/ep3_228_a3_blink.jpg", 1) with dissolve
    krystal "Hi!"
    mc "Hey."
    krystal "You came pretty fast. It's only been a minute since you replied my message."
    mc "Well, our rooms are quite close to be honest. That's why."
    krystal "Hm? Then, that means we live on the same floor?"
    scene ep3_228_a4 with dissolve
    mc "Yes, just go straight from your room to the end. You'll see it's on the left."
    krystal "I see...."
    krystal "Alright, let's not just stand here. Follow me."
    mc "Okay."
    scene ep3_228_a5 with dissolve
    krystal "Let's take a seat first."
    mc "Hm? You ordered a pizza?"
    krystal "Yes. Why?"
    mc "Nothing. I just thought you'd go to the kitchen for your dinner later."
    krystal "Oh... Well, last night you guys had a party until almost midnight."
    krystal "I don't know if it will happen again today. So, I decided to order the food to eat here."
    mc "That's fair enough..."
    scene ep3_228_a6 with dissolve
    krystal "You want some?"
    mc "Hm?"
    u "I just had dinner not too long ago."
    u "What should I do?"
    menu:
        "Thanks [krystal1]":
            u "Alright, I think I'm going to take a piece"
            u "I don't want to reject her act of kindness."
            $ ep3_takepizza = 1
            $ krystal_ch1_ep3 += 1
            $ krystal_relationship += 1
            scene ep3_228_a6_a1 with dissolve
            mc "Thank you. You're so kind."
            krystal "No worries! I invited you here, so I should take good care of you."
            krystal "Actually, it would be very rude of me if I didn't share my food with you!"
            mc "..........."
        "I'm still full":
            $ ep3_takepizza = 2
            scene ep3_228_a6_d1 with dissolve
            mc "Thanks for your kindness, but I already had dinner."
            mc "I'm still full right now."
            krystal "Oh, I see.... Never mind then!"
            krystal "But, if you feel hungry again, feel free to take a slice!"
            mc "Sure."
    scene black with dissolve
    s "You spend time hanging out with [krystal]...."
    s "*About an hour later*......"
    scene ep3_228_a7 with dissolve
    krystal "Ah~ I'm so full~"
    mc "I'd be surprised if you aren't."
    if ep3_takepizza == 1:
        mc "You finished the other five pieces by yourself."
    elif ep3_takepizza == 2:
        mc "You ate it all by yourself."
    krystal "*Giggles*...Hehe... You can't blame me for that. I was so hungry."
    mc "Yeah, I could tell that."
    scene ep3_228_a8 with dissolve
    mc "To be honest, I'm really surprised to see that you have a good shape."
    mc "I mean... Considering from the way you eat, you can easily get fat."
    krystal "*Giggles*...I know right?!"
    krystal "I think I'm a type of person who doesn't get fat no matter how much I eat."
    mc "I see..."
    krystal "[mc]."
    mc "Hm?"
    scene ep3_228_a9 with dissolve
    krystal "Do you mind me asking you some questions?"
    mc "Hm? Why?"
    krystal "I want to know you better."
    mc ".....Okay."
    krystal "How old are you?"
    mc "I'm 22."
    krystal "Hm... So, we are of the same age."
    $ krystal_age = "22"
    scene ep3_228_a10 with dissolve
    mc "Really?"
    krystal "Yeah... Where are you from?"
    mc "I'm from East Town."
    krystal "I see... I guess you moved here for work, right?"
    mc "How did you know that?"
    krystal "Well, there aren't many reasons for people to move from their old city to another city."
    mc "That makes sense...."
    scene ep3_228_a9 with dissolve
    krystal "Actually, the next question is the thing I want to know the most."
    mc ".... Hm? What is the question going to be about?"
    krystal "Well, it's about your personality."
    krystal "You know.... You're pretty weird in my opinion."
    krystal "I mean...you seem like someone who doesn't want to get involved with other people."
    krystal "But, you still decided to come, and be here with me."
    krystal "Is it your concept or what?"
    scene ep3_228_a10 with dissolve
    mc "No, it isn't. This is just the way I am."
    krystal "Yeah? Never mind then."
    krystal "I just feel like you're contradicting yourself."
    krystal "Is there something that makes you afraid of having relationships with people?"
    mc ".........."
    mc "*Sigh...Well..."
    s "*Incoming voices from TV*........"
    scene ep3_228_a11 with dissolve
    u "Hm....? Why did she suddenly look sad?"
    u "What's happening on the TV?"
    scene ep3_228_a12 with dissolve
    u "....Who are those girls...?"
    u "They look so young, but they seem to be very popular."
    scene ep3_228_a13 with dissolve
    u "What are they called?.... Idols...?... Girl group...?"
    u "Yeah, it has to be girl group. This thing has been very popular lately."
    lucy "Thank you, everyone! Thank you for coming to our concert!"
    lucy "I'm very happy to see you guys here!"
    lucy "I hope to see y-"
    stop music
    scene ep3_228_a14 with dissolve
    u "Hm...?"
    u "Why does she look so angry now?"
    mc "What's wrong?"
    play music "sfx/ep.3/ep3_11.mp3" fadein 3.0
    $ bgm = "Day7 - Journey Home"
    scene ep3_228_a15 with dissolve
    s "[krystal] didn't answer your question. She suddenly stood up instead."
    krystal "........."
    scene ep3_228_a16 with dissolve
    mc "Err......"
    u "Seems like she isn't in a mood to hang out anymore."
    u "I don't know what her problem is, but I think I should just leave her alone."
    mc "I'm leaving then. See you later."
    krystal "..........."
    scene ep3_228_a17 with dissolve
    u "She got angry after seeing that girl group on the TV."
    u "It's so obvious that she doesn't like seeing them."
    u "I'm now starting to wonder why she acted like that."
    u "Perhaps, they might've had a fight before. But, how?"
    u "Let's go back to my room, and search for the information."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_228_a18 with dissolve
    u "There it is...."
    u "So, [krystal] was really involved with these girls..."
    scene ep3_228_a19 with dissolve
    u "Umm... The group is called G-Flowers...."
    u "There were five members in the group, [krystal], [lucy], [ivy], [myla], and [allie]."
    u "Their first debut was 3 years ago, and they've been so popular since then."
    u "[krystal]... She was both the leader, and the center of the group."
    u "She was very popular because of how beautiful she looked, and how good she was at both singing, and dancing."
    u "She had about 50m followers on her IG during the time she still was in the group even though she was a member for only a year."
    scene ep3_228_a20 with dissolve
    u "Well, now it makes sense why she seemed very surprised that I didn't know her."
    u "50m followers in a year on IG is no joke..."
    u "....Hm?"
    u "....What is this video?..."
    scene ep3_228_a21 with dissolve
    u "..........."
    scene ep3_228_a22 with dissolve
    u "...[krystal] was caught slapping [lucy]'s face by the CCTV."
    u "After watching the video, [lucy]'s fans got very disappointed and angry at [krystal]."
    u "The company had no choice, but to force [krystal] to apologise at a press conference."
    u "However, bad rumors about [krystal] still kept coming nonstop day by day."
    u "Finally, a lot of her fans turned against her, and became her anti-fans."
    u "Although there were people who still believed, and supported [krystal], they were just nothing compared to the amount of anti fans."
    scene ep3_228_a20 with dissolve
    u "...Hm?... What is this video?...."
    u "What is this title?"
    u "......[krystal]'s final concert ended up in a disaster..."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_228_a23 with dissolve
    crowd "Boo! Boo! Boo!"
    crowd "Quit the group already! Get the fuck out of our faces!"
    crowd "We don't want an aggressive bitch in G-Flowers!!!"
    crowd "I even heard that you sold your body for money!"
    krystal "*Sobs*....N....No...That's.... Not true...."
    crowd "Being in a girl group doesn't give you enough money, huh?!"
    crowd "Tell me how much do I have to give you for a good fuck! Hahaha!!"
    krystal "*Sobs*...Why...are...you...doing...this...to...me...?"
    krystal "*Sobs*...I...didn't....do...anything...wrong...."
    ivy "Don't throw things at her, please!"
    ivy "Security!! What are you doing?! Help her!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_228_a20 with dissolve
    u "I've also suffered a lot, but I can't imagine how much she has been through...."
    u "So, after that concert, she decided to cancel her contract, and quit the group."
    u "Poor girl.... I feel so bad for her."
    stop music fadeout 3.0
    jump ep3_p2_endfirstnight
label ep3_p2_endfirstnight:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_229 with dissolve
    u "Alright, it's already so late."
    u "I should go to sleep...."
    $ ep3_alicemessage1 = True
    $ newmessage = True
    $ alice_messages_show = True
    $ alice_newmessage = True
    $ phone_alert = True
    u "Hm? I've got a new message? Let check who sent it to me."
    jump ep3_messagefromalice
label ep3_messagefromalice:
    if ep3_reply_alice1 == False:
        scene ep3_229 with vpunch
        u "I need to answer the message first!"
        jump ep3_messagefromalice
    else:
        scene black with dissolve
        s "*Next morning*......"
    scene ep3_230 with dissolve
    play music "sfx/ep.3/ep3_4.mp3" fadein 3.0
    $ bgm = "Sarah Jansen - Moments"
    u "Just another day of the working life...."
    u "Let's go have breakfast in the kitchen."
    scene ep3_231 with dissolve
    u "Actually, I woke up pretty early today."
    u "I wonder if there is anyone in the kitchen already."
    scene ep3_232 with dissolve
    u "....Hm?"
    rin "Heh...?"
    if ep3_sleepwithrin == 1:
        scene ep3_232_a1 with dissolve
        rin "Good morning, [mc]!"
        rin "Did you sleep well?"
        mc "Yes, I did. And you?"
        rin "Me, too. Thanks for asking!"
        scene ep3_232_a2 with dissolve
        mc ".....What are you doing?"
        rin "Stand still...."
        rin "I'm so tired. I've been pretty busy lately...."
        rin "I want to hug you to recharge my energy...."
        mc ".....Okay then."
        scene ep3_232_a3 with dissolve
        rin "*Giggles*....Have I ever told you how much I like your smell."
        mc "No, you haven't."
        rin "*Giggles*...Hehehe... Then, you should know that!"
        rin "............"
        scene ep3_232_a4 with dissolve
        u "....Hm?"
        u "Am I imagining things, or is her face really getting closer?"
        rin "....Why are you so tall...?"
        mc "....I don't kn-"
        scene ep3_232_a5 with dissolve
        mc "............"
        scene ep3_232_a6 with dissolve
        rin "*Kisses*.....Mmmm...."
        menu:
            "Kiss her back [rin1]":
                $ ep3_kissback = 1
                $ rin_ch1_ep3 += 1
                $ rin_relationship += 1
                scene ep3_232_a7 with dissolve
                rin "*Kisses*.....Mmmmm...."
                mc "*Kisses*......"
                if ep3_rinmorningkiss == True:
                    u "...I think... I'm starting to get addicted to her lips..."
                    u "....This isn't really good for me..."
                scene ep3_232_a8 with dissolve
                u "Hm...? She's using her tongue now...."
                u "Well, I didn't expect that...."
                rin "*Kisses*....Mmmmm...."
                scene black with dissolve
                $ renpy.pause()
                scene ep3_232_a9 with dissolve
                rin "*Softly breathes*....Did you like it...?"
                mc "...Yes, I did..."
                rin "*Softly breathes*....Can we do it again...?"
                mc "...If that's what you want...."
                rin "*Softly breathes*....Okay, th-"
                scene ep3_232_a10 with dissolve
                zeke "Hahahaha!"
                rin "!!!!"
                scene ep3_232_a11 with dissolve
                zeke "I told you, didn't I? But, you didn't believe me."
                mc "Aw...."
                scene ep3_232_a12 with dissolve
                rin "G-Good morning, guys!"
                mc "....Good morning."
                zeke "Oh?! You guys are here, too?"
                zeke "...Hm?"
                scene ep3_232_a13 with dissolve
                zeke "What were you doing?"
                zeke "You guys seem flustered...."
                rin "W-What are you talking about?!"
                rin "We didn't do anything, right? [mc]?"
                mc "...Yeah. We were just talking."
                mika "(Hmm...? This is getting interesting....)"
                rin "W-What are you guys waiting for? Let's have breakfast!"
                yui "Yeah, let's have breakfast. I'm so hungry."
                scene ep3_232_a14 with dissolve
                zeke "Okay then, let's hurry up guys."
                zeke "We'll have to drop [mika] off at her school, too!"
                mika "No, you don't have to do that. It's the opposite way to your company."
                mika "I don't want to bother you guys more than I already did."
                mika "So, just drop me off at the bus stop, okay?"
                zeke "Alright, if you say so."
                rin "*Whispers*...Hehe...We almost got caught...."
            "Push her away":
                $ ep3_kissback = 2
                scene ep3_232_a6_d1 with dissolve
                mc "No. We can't do it here."
                rin "....Why?"
                mc "It's too risky. [zeke] and the rest might come any second."
                rin "..........."
                scene ep3_232_a6_d2 with dissolve
                mc "I don't want to get caught doing that."
                mc "You understand me, right?"
                rin "............."
                rin ".....Okay..."
                mc "Let's just sit down, and have our breakfast..."
                scene black with dissolve
                s "*A few moments later*......"
                scene ep3_232_d2 with dissolve
                zeke "Good morning, guys!"
                mika "Did you sleep well, [rin]?"
                rin "....Yes, I did...."
                u "See? That's what I was talking about...."
                jump ep3_p2_atoffice
    else:
        scene ep3_232_d1 with dissolve
        rin "Good morning, [mc]!"
        rin "Did you sleep well?"
        mc "Yes, I did. And you?"
        rin "Me, too. Thanks for asking!"
        rin "You come here pretty early today, hm?"
        mc "Well, I woke up early today. That's why."
        rin "I see...."
        scene black with dissolve
        $ renpy.pause()
        scene ep3_232_d2 with dissolve
        zeke "Good morning, guys!"
        mika "Did you sleep well, [rin]?"
        rin "....Yes, I did. Thank you for asking."
        zeke "Alright, let's not waste anymore time. We should hurry up and finish our breakfast."
        zeke "We'll have to drop [mika] off at her school, too!"
        mika "No, you don't have to do that. It's the opposite way to your company."
        mika "I don't want to bother you guys more than I already did."
        mika "So, just drop me off at the bus stop, okay?"
        zeke "Alright, if you say so."
        jump ep3_p2_atoffice

label ep3_p2_atoffice:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_233 with fade
    s "While you're on the way to the department...."
    elaine "[mc]!"
    u "Hm....?"
    scene ep3_234 with dissolve
    elaine "Hi! Good morning!"
    mc "...Good morning, [elaine]."
    mc "What are you doing here this early?"
    scene ep3_235 with dissolve
    elaine "What kind of question is that? I can't be here?"
    mc "Of course, you can."
    mc "It's just... Work is about to start in fifteen minutes."
    mc "So, I thought you would be at your department by now."
    elaine "Well, I came here to see you."
    mc "Hm? What do you want to see me for?"
    scene ep3_236 with dissolve
    elaine "We can't talk about it here. Follow me."
    mc "Hm? Where are you taking me to?"
    elaine "Come on. Just follow me. It won't take you too long."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_237 with dissolve
    mc "Really? You really brought me to talk in the bathroom?"
    elaine "*Giggles*...Hehehe...."
    scene ep3_238 with dissolve
    u "....Hm?"
    scene ep3_239 with dissolve
    elaine "Come on..... Why did you dodge me?"
    elaine "It's not like we haven't kissed before."
    if ep3_havefunwithelaine == 1:
        elaine "Actually, we even almost had sex."
    mc "........."
    scene ep3_240 with dissolve
    mc "....If you don't have anything to talk about...."
    mc "Then, please excuse me."
    elaine "Why are you in such a hurry? We've still got ten minutes left!"
    scene ep3_241 with dissolve
    elaine "Come on.... Are you a robot?"
    elaine "All you ever do is think about work?"
    elaine "Let's just forget about it! Have some fun with me!"
    mc "..........."
    elaine "Aren't you interested in me? Don't you want to feel good before you start working?"
    elaine "Hmm~? What do you say?"
    menu:
        "Alright then,... [elaine2]":
            $ ep3_quickfun = 1
            $ elaine_ch1_ep3 += 2
            $ eliane_relationship += 2
            jump ep3quickfunbj
        "Push her away\n[smgr2](if you choose to Fuck her next.)\n[elaine2]":
            $ ep3_quickfun = 2
            if (ep3_havefunwithelaine != 1) and (refuseeliane == True):
                label modViewBothScenesEp3_001:
                scene ep3_241_s1 with dissolve
                elaine "Come on.... Am I not beautiful enough for you?"
                elaine "Why do you always reject me?"
                elaine "If I asked the other guys to have fun with me, they wouldn't hesitate to say yes."
                mc ".........."
                scene black with dissolve
                $ renpy.pause()
                scene ep3_241_s2 with dissolve
                elaine "....Okay, you like to play hard that much, huh?"
                elaine "You better put your cock inside my pussy now."
                elaine "Otherwise, I'm going to scream, and when people come in, I'll tell them that you tried to rape me."
                mc "....That's not true."
                elaine "Truth doesn't matter. You want to bet?"
                elaine "Who will they believe? You, or me?"
                mc "............"
                if modDoBothEp3_001:
                    jump ep3quickfundoggy
                menu:
                    "Fuck her [elaine2]":
                        $ ep3_quickfundoggy = 1
                        $ elaine_ch1_ep3 += 2
                        $ eliane_relationship += 2
                        jump ep3quickfundoggy
                    "Leave here":
                        scene ep3_241_s2_d with dissolve
                        mc "I'm leaving. Feel free to scream as loud as you want."
                        mc "I'm sure that CCTV has got footage of you dragging me in here."
                        mc "Then, your word won't matter anymore."
                        elaine "W-Wait...."
            else:
                scene ep3_241_d1 with dissolve
                mc "No, I don't think it's a good idea to do it here."
                mc "Also, we only have a short amount of time."
                mc "I don't want to be late for work."
                elaine "............"
                mc "Alright then, please excuse me."
            scene ep3_241_d2 with dissolve
            elaine "*Sighs*........"
            elaine "(....Am I really not attractive to him?)"
            elaine "(How did he just leave like that?)"
            elaine "(....This guy is really playing hard....)"
            elaine "(Even though I think he's interesting, I'm starting to get bored with him playing hard...)"
            elaine "(Maybe I should just stop chasing him....)"
            scene black with dissolve
            $ renpy.pause()
            scene ep3_241_d3 with dissolve
            u "Alright, let's get back to my department before I clock in late."
            jump ep3_p2_afterworkparty
        "[smgr2]MOD: Both. Will award all points":
            $ modDoBothEp3_001 = True
            $ ep3_quickfun = 1
            $ elaine_ch1_ep3 += 2
            $ eliane_relationship += 2
            jump modViewBothScenesEp3_001

label ep3quickfundoggy:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    scene ep3_241_s2_a1 with dissolve
    mc "I bet that your plan isn't going to work."
    mc "Because CCTV must have got footage of you dragging me in here."
    mc "Then, your word won't matter anymore."
    elaine "....Really? Then why did you take your cock out?"
    mc "Because you seem to really want it that bad, so I'll grant your wish...."
    elaine "*Giggles*...Hehe... Good boy..."
    scene ep3_241_s2_a2 with dissolve
    elaine "A-Ah!......"
    elaine "...Y...You're so big...."
    mc "I'm going to start moving now."
    elaine "Wait. Let me take my bra off first...."
    scene ep3_241_s2_a3 with dissolve
    elaine "Alright, you can move now...."
    scene ep3_241_s2_a4 with dissolve
    show ep3_quickfundoggy with dissolve
    window hide
    elaine "*Softly breathes*....Mmmmm....."
    elaine "*Softly breathes*....Ahhh.... You're so big inside me...."
    $ renpy.pause()
    elaine "*Softly breathes*....Mmmm... Faster... Fuck me faster...!"
    hide ep3_quickfundoggy
    scene ep3_241_s2_a5 with dissolve
    show ep3_quickfundoggy2 with dissolve
    window hide
    elaine "*Moans*.....Ahhh!....Ahhh!...."
    mc "Shh...Don't moan too loud. Someone might hear you."
    elaine "*Moans*...Ahh!...I don't care....!"
    $ renpy.pause()
    hide ep3_quickfundoggy2
    scene ep3_241_s2_a6 with dissolve
    show ep3_quickfundoggy3 with dissolve
    window hide
    elaine "*Heavily breathes*....Mmmmm!....Mmmmm!....."
    elaine "*Heavily breathes*....T...This feels... Soooo.... Good!"
    mc "....I'm almost there...."
    elaine "*Heavily breathes*...Ahhh...M....Me, too...!"
    menu:
        "Slowest":
            hide ep3_quickfundoggy3
            jump ep3quickfundoggyslow
        "Slower":
            hide ep3_quickfundoggy3
            jump ep3quickfundoggyfast
        "Cum":
            jump ep3quickfundoggycum
label ep3quickfundoggyslow:
    scene ep3_241_s2_a4 with dissolve
    show ep3_quickfundoggy with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ep3_quickfundoggy
            jump ep3quickfundoggyfast
        "Fastest":
            hide ep3_quickfundoggy
            jump ep3quickfundoggyfastest
label ep3quickfundoggyfast:
    scene ep3_241_s2_a5 with dissolve
    show ep3_quickfundoggy2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_quickfundoggy2
            jump ep3quickfundoggyslow
        "Faster":
            hide ep3_quickfundoggy2
            jump ep3quickfundoggyfastest
label ep3quickfundoggyfastest:
    scene ep3_241_s2_a6 with dissolve
    show ep3_quickfundoggy3 with dissolve
    window hide
    menu:
        "Slowest":
            hide ep3_quickfundoggy3
            jump ep3quickfundoggyslow
        "Slower":
            hide ep3_quickfundoggy3
            jump ep3quickfundoggyfast
        "Cum":
            jump ep3quickfundoggycum
label ep3quickfundoggycum:
    mc "*Softly breathes*....I'm about to cum..."
    elaine "*Heavily breathes*....Ahhhh... Don't hold it!... Please, cum for me....!"
    menu:
        "Cum inside":
            hide ep3_quickfundoggy3
            scene black with dissolve
            $ renpy.pause()
            scene ep3_241_s2_a6_in with dissolve
            mc "I'm cumming...!"
            elaine "M...Me, too!! Ahhhhh!!"
            $ renpy.pause()
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep3_241_s2_a7 with dissolve
            elaine "*Pants*....That was great...."
            elaine "*Pants*....You really came a lot inside my pussy...."
            if not modDoBothEp3_001:
                mc "...Is today your safe day?"
        "Cum outside":
            hide ep3_quickfundoggy3
            scene black with dissolve
            $ renpy.pause()
            scene ep3_241_s2_a6_out with dissolve
            mc "I'm cumming...!"
            elaine "M...Me, too!! Ahhhhh!!"
            $ renpy.pause()
            $ renpy.pause(0.2,hard=True)
            scene ep3_241_s2_a7 with dissolve
            elaine "*Pants*....That was great...."
            elaine "*Pants*....But, you should've came inside my pussy...."
            if not modDoBothEp3_001:
                mc "....Hm?... Is today your safe day?"
    if modDoBothEp3_001:
        elaine "I want more fun....*Giggles*"
        elaine "....And it looks like someone is still hard."
        mc "Fine but let's make it quick"
        jump modViewBothScenesEp3_002
    else:
        elaine "*Pants*...Yes, it is."
        elaine "If it wasn't, I wouldn't have asked you to cum inside me."
        elaine "....There is no way I will let myself get pregnant at this age."
        mc "That's good for you."
        elaine "....By the way... You feel so good inside me. I liked that."
        mc "....Thanks I guess?"
    elaine "Alright, let's dress up, and leave."
    elaine "We've only got two minutes before work starts."
    mc "Sure."
    $ renpy.end_replay()
    scene black with dissolve
    $ renpy.pause()
    scene ep3_241_a15 with dissolve
    elaine "*Winks*.... Thanks for having some fun with me today!"
    elaine "Let's do that again soon!"
    mc ".....Okay."
    elaine "Alright, I've got to go back to my department now."
    elaine "See you around!"
    mc "See you."
    jump ep3_p2_afterworkparty
label ep3quickfunbj:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    scene ep3_241_a1 with dissolve
    mc "....Alright then, let's do it."
    elaine "*Giggles*....Hehe... That's what I expected to hear!"
    mc "But, we've got to finish in ten minutes, okay?"
    elaine "....Well, that actually depends on you, not me."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_241_a2 with dissolve
    elaine "Heh~"
    elaine "Seems like someone has been ready for a while..."
    label modViewBothScenesEp3_002:
    elaine "*Giggles*...You're a boy after all~"
    mc "Let's get started already. The clock is ticking."
    elaine "Alright, got it."
    scene ep3_241_a3 with dissolve
    show ep3_quickfunbj with dissolve
    window hide
    elaine "*Sucks*.....Mmmmm....."
    elaine "*Sucks*.....Mmmm.... It's so...big...."
    $ renpy.pause()
    hide ep3_quickfunbj
    scene ep3_241_a4 with dissolve
    show ep3_quickfunbj2 with dissolve
    window hide
    elaine "*Sucks*......Mmmmmm...."
    mc "*Softly breathes*........"
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_quickfunbj2
            jump ep3quickfunbjslow
        "Next":
            hide ep3_quickfunbj2
            jump ep3quickfunsex
label ep3quickfunbjslow:
    scene ep3_241_a3 with dissolve
    show ep3_quickfunbj with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ep3_quickfunbj
            jump ep3quickfunbjfast
        "Next":
            hide ep3_quickfunbj
            jump ep3quickfunsex
label ep3quickfunbjfast:
    scene ep3_241_a4 with dissolve
    show ep3_quickfunbj2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_quickfunbj2
            jump ep3quickfunbjslow
        "Next":
            hide ep3_quickfunbj2
            jump ep3quickfunsex
label ep3quickfunsex:
    scene ep3_241_a5 with dissolve
    mc "Why did you stop?"
    elaine "Let's change the position."
    mc "Hm? What do you want to do?"
    scene ep3_241_a6 with dissolve
    elaine "Can you go sit right there?"
    mc "..........."
    mc "....Okay."
    scene ep3_241_a7 with dissolve
    elaine "Good boy..."
    mc "Why do I have to sit here?"
    elaine "*Giggles*....Because...."
    scene ep3_241_a8 with dissolve
    elaine "....I want to be on top of you~"
    mc ".........."
    if ep3_havefunwithelaine == 1:
        elaine "*Giggles*....Hehe... There is no one to stop us this time...."
    elaine "Finally... I've been waiting for this moment...."
    elaine "Alright... I'm going to put it in now...."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_241_a9 with dissolve
    elaine "Ahh....!"
    mc "Shh... Someone might hear us."
    elaine "I don't care...!"
    elaine "Ahh... Let me take my top off first..."
    scene ep3_241_a10 with dissolve
    elaine "Okay... I'm going to start moving now."
    show ep3_quickfungot with dissolve
    window hide
    elaine "*Softly breathes*....Ahh... This feels so good already..."
    elaine "*Softly breathes*....Mmmm.... It took me quite a long time to convince you to do this...."
    elaine "*Softly breathes*....But I can say that I'm not disappointed at all...."
    $ renpy.pause()
    hide ep3_quickfungot
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep3_241_a11 with dissolve
    elaine "*Kisses*....Mmmmm....."
    mc "*Kisses*....Mmmmm....."
    elaine "Let's move a bit faster...."
    scene ep3_241_a12 with dissolve
    show ep3_quickfungot2 with dissolve
    window hide
    elaine "*Moans*....Ahhh.... Ahhh...."
    elaine "*Moans*....Mmmmm... You're so big inside me...."
    mc "*Softly breathes*........"
    $ renpy.pause()
    elaine "*Moans*.... Faster! Faster!...."
    hide ep3_quickfungot2
    scene ep3_241_a13 with dissolve
    show ep3_quickfungot3 with dissolve
    window hide
    elaine "*Heavily breathes*....Ahhh!....Ahhhh!...."
    elaine "*Heavily breathes*....Mmmm!.... This is sooo good...!"
    mc "*Softly breathes*....I'm almost there...."
    elaine "*Heavily breathes*...Mmmm!.... Me, too....!"
    menu:
        "Slowest":
            hide ep3_quickfungot3
            jump ep3quickfungotslow
        "Slower":
            hide ep3_quickfungot3
            jump ep3quickfungotfast
        "Cum":
            jump ep3quickfungotcum
label ep3quickfungotslow:
    scene ep3_241_a10 with dissolve
    show ep3_quickfungot with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ep3_quickfungot
            jump ep3quickfungotfast
        "Fastest":
            hide ep3_quickfungot
            jump ep3quickfungotfastest
label ep3quickfungotfast:
    scene ep3_241_a12 with dissolve
    show ep3_quickfungot2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_quickfungot2
            jump ep3quickfungotslow
        "Faster":
            hide ep3_quickfungot2
            jump ep3quickfungotfastest
label ep3quickfungotfastest:
    scene ep3_241_a13 with dissolve
    show ep3_quickfungot3 with dissolve
    window hide
    menu:
        "Slowest":
            hide ep3_quickfungot3
            jump ep3quickfungotslow
        "Slower":
            hide ep3_quickfungot3
            jump ep3quickfungotfast
        "Cum":
            jump ep3quickfungotcum
label ep3quickfungotcum:
    mc "*Softly breathes*....I'm about to cum...."
    elaine "*Heavily breathes*....Ahhhh... Don't hold it!...Please, cum for me....!"
    menu:
        "Cum inside":
            hide ep3_quickfungot3
            scene black with dissolve
            $ renpy.pause()
            scene ep3_241_a13_in with dissolve
            mc "I'm cumming...!"
            elaine "M...Me, too!! Ahhhhh!!"
            $ renpy.pause()
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep3_241_a14 at eyesblink("Ch.1/Ep.3/Scenes/ep3_241_a14.jpg", "Ch.1/Ep.3/Scenes/ep3_241_a14_blink.jpg", 1) with dissolve
            elaine "*Pants*....That was great...."
            if modDoBothEp3_001:
                elaine "*Pants*....You really came a lot inside my pussy....again"
            else:
                elaine "*Pants*....You really came a lot inside my pussy...."
            mc "...Is today your safe day?"
        "Cum outside":
            hide ep3_quickfungot3
            scene black with dissolve
            $ renpy.pause()
            scene ep3_241_a13_out with dissolve
            mc "I'm cumming...!"
            elaine "M...Me, too!! Ahhhhh!!"
            $ renpy.pause()
            $ renpy.pause(0.2,hard=True)
            scene ep3_241_a14 at eyesblink("Ch.1/Ep.3/Scenes/ep3_241_a14.jpg", "Ch.1/Ep.3/Scenes/ep3_241_a14_blink.jpg", 1) with dissolve
            elaine "*Pants*....That was great...."
            if modDoBothEp3_001:
                elaine "*Pants*....But you should've came inside my pussy....again"
            else:
                elaine "*Pants*....But you should've came inside my pussy...."
            mc "....Hm?...Is today your safe day?"
    elaine "*Pants*...Yes, it is."
    elaine "If it wasn't, I wouldn't have asked you to cum inside me."
    elaine "....There is no way I will let myself get pregnant at this age."
    mc "That's good for you."
    elaine "....By the way... You feel so good inside me. I like that."
    mc "....Thanks I guess?"
    elaine "Alright, let's dress up, and leave."
    elaine "We've only got two minutes before work starts."
    mc "Sure."
    $ renpy.end_replay()
    scene black with dissolve
    $ renpy.pause()
    scene ep3_241_a15 with dissolve
    elaine "*Winks*....Thanks for having some fun with me today!"
    elaine "Let's do that again soon!"
    mc ".....Okay."
    elaine "Alright, I've got to go back to my department now."
    elaine "See you around!"
    mc "See you."
    jump ep3_p2_afterworkparty

label ep3_p2_afterworkparty:
    scene ep3_242 with dissolve
    pete "Guys! Let's have dinner together afterwork!"
    pete "What do you think?"
    liam "That sounds good to me."
    liam "It's been a while since we've had dinner together."
    scene ep3_243 with dissolve
    pete "What about you, [joe]?"
    joe "Of course, count me in!"
    joe "There is no way I'll say no to food."
    pete "Great! I like your spirit!"
    pete "And you, [david]?"
    david "[joe] just said what I was about to say. Hahaha!"
    pete "I had no doubt at all."
    scene ep3_244 with dissolve
    pete "What about you, [leo]?"
    leo "I don't have any plans this evening."
    leo "So... Yeah."
    scene ep3_245 with dissolve
    pete "[yui]?"
    yui "Yes, I'll go with you."
    pete "Lovely!"
    scene ep3_246 with dissolve
    pete "Will you come with us, [mc]?"
    u "Well... I should blend in with them...."
    u "Then...."
    mc "....Yes, I will."
    pete "Fantastic! I'll come, and tell you where we'll be going later."
    scene black with dissolve
    s "*8 hours later*........"
    scene ep3_247 with dissolve
    pete "Alright guys, are you ready?"
    joe "Yes, we are!"
    pete "Then, let's go to the same restaurant we went last time."
    scene ep3_248 with dissolve
    liam "Okay, I get it."
    pete "My friend will join us, too. I'm going to pick her up."
    pete "See you all at the restaurant!"
    joe "Sure!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_249 with dissolve
    liam "Alright guys, let's go."
    david "Okay then, let me turn off my computer first."
    joe "Hurry up, man!"
    joe "I'm so hungry right now..."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_250 with fade
    leo "Hm...? Did we come too fast?"
    leo "Where is [pete]?"
    liam "No, we didn't. There he is...."
    scene ep3_251 with dissolve
    pete "Right here, guys!"
    leo "Oh yeah, there he is."
    leo "Hm?... Isn't that [sandra]?"
    liam "Yes, it's her."
    scene ep3_252 with dissolve
    pete "Take your seat, guys."
    liam "Good evening, [sandra]."
    joe "Hi, [sandra]"
    sandra "Hi, everyone."
    scene ep3_253 with dissolve
    yui "(....Who's that woman...?)"
    liam "Alright, we have to seperate [david] and [joe] this time."
    liam "Last time you guys sat together, you looked a bit uncomfortable."
    joe "You're right!"
    david "Hahaha... Yeah, the sofa was quite small for the both of us!"
    liam "Then, sit with me here, [david]."
    leo "(...Let's go ask [yui] if she wants to sit with me...)"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_254 with dissolve
    david "Are you alright, [liam]?"
    david "You don't feel uncomfortable, right?"
    liam "Don't worry! I'm good!"
    david "I'm sorry that you have to sit with a big guy like me."
    liam "You don't need to say that. There is nothing for you to be sorry about!"
    leo ".............."
    leo "(How did it end up like this....?)"
    scene ep3_255 with dissolve
    pete "Alright, guys. Let's order the food!"
    pete "Don't worry about money. I'll pay for you guys!"
    joe "Woooh!! You're such a great boss!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_256 with dissolve
    joe "How are you doing, [sandra]?"
    sandra "I'm doing good. Thanks for asking!"
    joe "It's been a while since you came to hang out with us."
    sandra "Well, I've been pretty busy lately...."
    leo "But, you're here with us now. So, you aren't busy today then?"
    scene ep3_257 with dissolve
    sandra "Well, to be honest I still have a lot of work to do."
    sandra "But, [pete] wanted me to take a break for a couple hours."
    sandra "So, he insisted to bring me here."
    pete "Yeah, you shouldn't work nonstop like that!"
    pete "You need to have a good balance between working, and resting!"
    sandra "Yeah, that's what he told me when inviting me here."
    pete "Hahaha...."
    scene ep3_258 with dissolve
    pete ".....Hm?"
    scene ep3_259 with dissolve
    pete "What's wrong, [yui]?"
    pete "You seem a bit unhappy."
    yui "N-Nothing! Don't worry about me!"
    yui "I'm really happy right now."
    pete "Are you sure?"
    yui "Yes, I am."
    scene ep3_260 with dissolve
    pete "Alright then, let's enjoy our dinner!"
    pete "Cheers!"
    yui "..........."
    pete "Hm....? What are you waiting for?"
    pete "Are you not going to drink your beer?"
    scene ep3_261 with dissolve
    yui "Err......."
    u "She probably doesn't want to drink today."
    u "I remember that she said she can't drink beer, because it makes her drunk really easy."
    u "[pete] surely doesn't know about that....."
    u "She seems to be afraid to tell [pete] though..."
    u "What should I do?"
    menu:
        "Help her [yui1]":
            $ ep3_speakforyui = 1
            $ yui_ch1_ep3 += 1
            $ yui_relationship += 1
            scene ep3_261_a1 with dissolve
            mc "She can't drink beer, [pete]."
            yui "........."
            pete "Hm? Why?"
            mc "She'd get drunk very easy if she drank it."
            scene ep3_261_a2 with dissolve
        "Stay quiet":
            $ ep3_speakforyui = 2
            scene ep3_261_d1 with dissolve
            u "Well, that's none of my business...."
            u "She isn't a kid. She's an adult."
            u "She has to deal with her problem by herself."
            yui "Err....."
            scene ep3_261_d2 with dissolve
            yui "I'm sorry, [pete]. I can't drink beer."
            pete "Hm? Why?"
            yui "I'd get drunk very easy if I drank it."
    pete "What? Really? How come?"
    yui "....I don't know. It just happens."
    sandra "I can confirm that!"
    sandra "I have a friend who's really good at drinking vodka, but easily gets drunk when drinking beer, too!"
    pete "That's so weird...."
    scene ep3_262 with dissolve
    pete "Well, I guess I'm the same as [yui] then!"
    pete "I'm not a lightweight, but I'm just allergic to beer!"
    joe "Hm....? Yeah, maybe that's the case!"
    scene ep3_263 with dissolve
    sandra "*Giggles*.... No, it's not!"
    sandra "I saw him pass out just by drinking a glass of whisky when we were at the university!"
    pete "What?! Really?!"
    liam "Haha... So, you really are a lightweight."
    pete "....Since when did it happen? Why don't I remember it?"
    if ep3_speakforyui == 1:
        scene ep3_263_a1 with dissolve
        yui "....Thanks for speaking up for me."
        yui "I didn't have to drink the beer, because of you."
        mc "You don't have to thank me."
        mc "I didn't try to help you. I just did it for my own good."
        scene ep3_263_a2 with dissolve
        yui "............"
        yui "....Were you afraid that I would do something like that to you again?"
        mc "To be honest... Yeah, you got it right."
        yui "......I see."
    scene ep3_264 with dissolve
    pete "Alright everyone, I'd like to say something."
    pete "Please, stand up."
    joe "Okay."
    pete "Thanks for working hard. Our long journey is going to end soon."
    pete "I'm so proud to be working with you guys!"
    scene ep3_265 with dissolve
    pete "Let's celebrate for our incoming success!"
    pete "Cheers!"
    liam "Cheers!"
    david "Cheers!"
    scene black with dissolve
    s "*An hour later*........"
    scene ep3_266 with dissolve
    pete "Alright, guys. We're going to have to leave now."
    joe "What? Why are you guys leaving so fast?"
    joe "It's only been just an hour!"
    joe "Come on! Let's stay a little bit longer!"
    scene ep3_267 with dissolve
    pete "I'm sorry, guys."
    pete "Her family doesn't allow her to go home too late."
    sandra "I'm sorry to ruin the mood, guys."
    sandra "But, I really have to leave. My parents are kind of strict."
    liam "Then, you should hurry up. Don't worry about us. We understand you."
    scene ep3_266 with dissolve
    pete "Thanks, [liam]."
    pete "I can leave my card with you to pay the bill, right?"
    liam "Yeah, just leave it with me. I'll take care of it."
    pete "Alright then."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_268 with dissolve
    joe "Let's order more food!"
    liam "What do you want to order?"
    joe "Some chicken wings for me."
    liam "What about you, [leo]? Is there something that you want to order?"
    scene ep3_269 with dissolve
    leo "I don't know yet...."
    leo "Let me think first."
    mc "..........."
    yui "..........."
    scene ep3_270 with dissolve
    mc "Do you want to go home?"
    yui "Oh... I was about to ask you the same question."
    mc "Alright then, let's go home."
    yui "Sure."
    scene ep3_271 with dissolve
    david "Hm? Where are you guys going?"
    mc "We also want to leave, too."
    liam "Oh? Don't you want to stay here a little bit longer?"
    yui "No, thanks."
    liam "Okay then, get home safe. See you tomorrow."
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    scene ep3_272 with dissolve
    play music "sfx/ep2_6.mp3" fadein 3.0
    $ bgm = "Onycs - Eden"
    mc "............"
    mc "I think [pete] was right. You seem a bit unhappy."
    mc "What's wrong?"
    yui "..........."
    scene ep3_273 with dissolve
    mc "Hm....?"
    mc "....What are y-"
    scene ep3_274 with dissolve
    yui "Shh...!"
    yui "*Whispers*....Quiet! Don't say anything."
    mc "............"
    scene ep3_275 with dissolve
    sandra "To be honest, you don't have to drive me home actually."
    sandra "I can just take a taxi there."
    sandra "You should go back to them."
    scene ep3_276 with dissolve
    pete "............"
    sandra "....Hm?"
    pete "What are you talking about?"
    pete "It's getting dark. There is no way I'm going to let you take a taxi. It's dangerous."
    pete "So yeah, I do have to drive you home by myself."
    sandra "............."
    sandra ".....Okay, I get it, but your hand....."
    scene ep3_277 with dissolve
    pete "[sandra]."
    sandra ".....Hm? What?"
    pete "After the project is finished, will you go out with me?"
    sandra "....W...What did you just say?"
    scene ep3_278 with dissolve
    sandra "...S... Stop joking with me already. We're friends."
    pete "Are we?"
    pete "You know I like you, and I know you like me as well."
    sandra ".............."
    pete "I really like you, [sandra]."
    pete "Will you go out with me?"
    sandra "{size=-15}.......Yeah...{/size}"
    pete "Hm? What did you just say? I couldn't hear you."
    sandra ".....Yeah, I will....."
    scene ep3_279 with dissolve
    pete "Yes! That's what I've been wanting to hear!"
    pete "Today is the happiest day of my life!"
    sandra ".....You're exaggerating."
    pete "*Giggles*....No, I'm not!"
    yui "..............."
    u "....Well, I think I know why [yui] has been looking unhappy."
    u "She must've felt something was strange between [sandra] and [pete]."
    u "And now she just heard [pete] asking [sandra] out."
    u "She must be so sad right now."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_280 with fade
    yui "............."
    u "....Well, this is so awkward."
    u "She didn't say a single word after hearing them talk. She's been quiet all the way here."
    u "I usually prefer to be quiet, but the atmosphere around her is making me uncomfortable."
    u "I guess this is how other people feel when they're around me...."
    scene ep3_281 with dissolve
    u "Alright, we finally made it home."
    u "Let's just go straight to my room."
    u ".............."
    mc "Goodnight, [yui]."
    scene ep3_282 with dissolve
    yui "Wait a sec."
    u "...Hm?"
    mc "Is there something you want?"
    scene ep3_283 at eyesblink("Ch.1/Ep.3/Scenes/ep3_283.jpg", "Ch.1/Ep.3/Scenes/ep3_283_blink.jpg", 1) with dissolve
    yui "............."
    yui "I really want to get drunk tonight."
    yui "Do you want to go for a second round?"
    mc "............."
    $ krystal_profession = "Former girl group member"
    if ep3_quickfun == 1 or ep3_quickfundoggy == 1:
        $ elaine_sex += 1
    scene ep3_284 with dissolve
    yui "Why don't you answer me?"
    yui "What do you say?"
    u "...How should I answer her?"
    menu:
        "Okay then [yui2]":
            $ ep3_secondround = 1
            $ yui_ch1_ep3 += 2
            $ yui_relationship += 2
            mc "Okay, let's go then."
            scene black with dissolve
            $ renpy.pause()
            scene ep3_284_a1 with fade
            mc "We only have beer. We're out of wine."
            yui "It's okay."
            mc "Are you sure?"
            yui "Yeah, just give it to me."
            mc "Okay."
            scene ep3_284_a2 with dissolve
            u "I can't believe that I'm actually having a second round."
            u "But, she seems sad. So, let's just drink with her for a little bit more."
            u "Maybe she will...."
            scene ep3_284_a3 with dissolve
            u "....Hm?"
            scene ep3_284_a4 with dissolve
            mc "Hey...."
            mc "Take it easy. Don't drink too fast."
            mc "You'll get...."
            scene ep3_284_a5 with dissolve
            yui "Ahhh~!"
            mc ".........."
            u "She didn't listen to me at all. She really drank it in one shot..."
            scene ep3_284_a6 with dissolve
            yui ".........."
            u "Is she looking at the beer in my hand?"
            mc "...What?"
            scene ep3_284_a7 with dissolve
            yui "If you aren't going to drink it, give it to me."
            mc "Seriously? You should take it easy..."
            yui "I don't want to do that! I'm here to get drunk!"
            yui "Give me your beer and go grab another one from refrigerator."
            mc "............"
            scene ep3_284_a8 with dissolve
            mc "*Sighs*....Fine. Take it."
            yui "Thanks."
            yui "We haven't spend much time together, so I don't know what kind of person you really are."
            yui "But, at least I can see that you can read the situation, and know that you should be listening to my words now."
            scene black with dissolve
            s "*An hour later*........"
            scene ep3_284_a9 with dissolve
            mc "............"
            u "Well, it's been an hour since we started drinking."
            u "I wonder if she is still doing good...."
            scene ep3_284_a10 with dissolve
            yui "..........."
            yui "I want to pass out, and wake up not remembering anything that happened today."
            yui "I drank so many beers. I'm supposed to be drunk already."
            yui "But, why am I not drunk yet?"
            mc ".........."
            scene ep3_284_a11 with dissolve
            mc "I just don't get it."
            yui "Don't get what?"
            mc "I don't get why you want to forget about everything that bad."
            mc "I mean... It already happened, so it doesn't matter if you forget about it or not."
            mc "[pete] will still be going out with [sandra] anyway."
            yui "..........."
            yui "Have you never been heartbroken before?"
            mc "....No, I haven't."
            yui "Yeah, that's obvious...."
            yui "Well, you will understand me once you're in my position."
            mc "............"
            scene ep3_284_a12 with dissolve
            mc "Can I ask you a question?"
            yui "....What do you want to ask?"
            mc "Why do you love [pete]?"
            yui "What kind of question is that?"
            mc "Well, It's been a while since I loved, or was loved. So, I kind of forget why we love someone."
            yui ".........."
            yui "*Sighs*.... Alright, since I'm very appreciative that you decided to be here with me, I'll tell you my story."
            scene black with dissolve
            yui "Everything happened when I was a first year student at the university."
            scene ep3_284_a13 with fade
            yui "You might not believe me, but I was actually the only girl in the department."
            yui "So, there were a lot of guys asking me out, but I rejected all of them."
            yui "And one day, I walked into the lecture room..."
            scene ep3_284_a14 with dissolve
            man1 "Hey, look who's coming...."
            man1 "Isn't that our little princess?"
            man2 "Hi, [yui]! Do you not really want to go out with me?"
            man3 "Stop it man. You don't deserve our little princess!"
            man1 "Hahahaha!"
            yui "............"
            man2 "Ouch...! She ignored me again! Hahaha!"
            man3 "Hahahaha!"
            scene ep3_284_a15 with dissolve
            man3 "I just told you that you don't deserve her, didn't I?"
            man3 "Our little princess is so busy at studying. She doesn't want to date anyone!"
            man2 "Come on! Are you really not going to change your mind? You should go out with me, [yui]!"
            man2 "Don't you know I'm very rich? I'll buy you anything you need!"
            man2 "You won't need to worry about studying, and getting a good grade at all. I'll take care of you!"
            man1 "That isn't going to work bro. She really wants to get a good grade, so she can work in a game company!"
            man2 "Hahaha! I know that! I was just teasing her."
            man2 "Hey, [yui]! Why don't you become my secretary after we graduate?"
            man2 "You should forget about being a game developer! It isn't the right job for beautiful women like you!"
            man2 "You better be my secretary! I'll pay you a good salary! Hahaha!"
            scene ep3_284_a16 with dissolve
            pete "Hey there."
            man1 "...Hm?"
            pete "You shouldn't be saying something like that."
            yui "........"
            scene ep3_284_a17 with dissolve
            man2 "Excuse me? Who the hell are you?"
            pete "My name is [pete]. I'm a fourth year game developer student."
            man2 "Then, why the hell are you here, senior?"
            man2 "Has anyone ever told you to not stick your nose into other people's business?"
            pete "............"
            pete "Your teacher asked me to come here to give you guys some advice about being a game developer."
            pete "And I know that I shouldn't stick my nose into your business, but I can't stand what you were saying to that female student."
            man2 "Then what?"
            scene ep3_284_a18 with dissolve
            pete "Get out of here right now. This class doesn't need sexist students."
            man2 "Who the hell are you to say that? You have no rights to kick us out of here."
            pete "Well, you're right. I can't force you out."
            pete "You can stay, but once the professor comes, I'll tell him about what you said to that female student."
            man1 "Hahaha! Like he's going to believe you!"
            pete "Let's see... I'm sure that there were other students hearing you guys. They can be my witnesses."
            pete "I wonder what the professor is going to do to you guys. Deducting marks? Suspending?"
            man2 ".............."
            scene ep3_284_a19 with dissolve
            man2 "Alright, man. We'll leave. Just don't tell the professor."
            pete "Well, that depends on how you behave after this."
            pete "I'll keep my eyes on you guys, and if I hear you insulting someone again, I'll make you regret it."
            yui "............."
            scene black with dissolve
            $ renpy.pause()
            scene ep3_284_a20 with fade
            yui "Well, that was what happened. I fell in love with him the moment he came up to protect me."
            yui "Nobody had ever done that for me before."
            mc "Those guys... Why did they do that to you?"
            yui "I don't know."
            mc "Were you rude towards them?"
            yui "No, I wasn't. I'm sure that I nicely rejected one of them when he was asking me out."
            yui "Actually, I nicely rejected everyone. So, I don't know why they hated me that much."
            yui "To be honest, they still talked bad about me behind my back after that day."
            yui "[pete] didn't know that since he wasn't always around."
            yui "So, there was nothing I could do. I had no choice, but to continue ignoring them."
            mc "So, you hated men because of them?"
            scene ep3_284_a22 with dissolve
            yui "....Yeah, I think so."
            mc "To think of it, when we went to meet [pete] for the first time together. He didn't seem to know you."
            mc "Didn't you talk to him at the university?"
            yui "No, I didn't...."
            yui "It's hard to talk to someone you have a crush on. So, I didn't have the guts to talk to him."
            yui "But when I finally became brave enough to do that, he already fell for someone else...."
            scene ep3_284_a23 with dissolve
            yui "*Giggles*....I'm such an idiot!!"
            mc "Hey...Relax..."
            scene black with dissolve
            s "*Half an hour later*........"
            scene ep3_284_a24 with dissolve
            yui "..............."
            mc "..........."
            mc ".....[yui]."
            yui ".....Hmmmm~?"
            scene ep3_284_a25 with dissolve
            mc "Don't fall asleep here"
            mc "You should go sleep in your room."
            yui "............"
            mc "Are you listening to me?"
            yui "....Yes, I....am...."
            mc "*Sighs*....Okay then, let me clean up the table first. I'll take you to your room later."
            scene black with dissolve
            $ renpy.pause()
            scene ep3_284_a26 with dissolve
            mc "Alright, let's go upstairs...."
            yui "Ummmm...."
            mc "Stand up, [yui]."
            yui "....Ummmm..... Help me stand up, please~"
            mc "*Sighs*....Okay."
            scene ep3_284_a27 with dissolve
            mc "Stand straight...."
            yui "....I'm trying...."
            mc "Okay, let's go then."
            scene black with dissolve
            $ renpy.pause()
            scene ep3_284_a28 with dissolve
            yui "..........."
            yui "*Hics*.....My heart.... It really hurts...."
            yui "*Hics*....Why does it.... Hurt so much.... Like this....?"
            mc "............"
            yui "*Hics*....I'm sorry.... I didn't mean.... To cry.... In front of you...."
            menu:
                "Comfort her [yui2]":
                    $ ep3_comfortyui = 1
                    $ yui_ch1_ep3 += 2
                    $ yui_relationship += 2
                    scene ep3_284_a28_a with dissolve
                    mc "It's okay. Just cry."
                    mc "You can cry as much as you want."
                    yui "..........."
                    mc "Let yourself feel all the pain today, and wake up stronger tomorrow."
                    mc "Just forget about him. There are a lot of guys out there who want to date you."
                    yui "*Hics*.....Like who?"
                    mc "..........."
                    mc "........[leo]?"
                    yui ".....No, not him."
                    yui "But.... Thanks for comforting me..."
                "Stay quiet":
                    $ ep3_comfortyui = 2
                    scene ep3_284_a28_d with dissolve
                    yui "*Hics*......."
                    u "I don't know if I should comfort her. So, let's just stay quiet then."
                    mc "............."
            scene black with dissolve
            $ renpy.pause()
            scene ep3_284_a29 with dissolve
            yui "....Thank you for.... Being with me.... This late...."
            mc "You're welcome."
            yui "..........."
            yui ".....See you tomorrow, [mc]."
            mc "See you tomorrow."
            scene black with dissolve
            $ renpy.pause()
            scene ep3_284_a30 with dissolve
            u "....Alright, let's go back to my room."
            jump ep3_p3_sleep
        "Sorry":
            $ ep3_secondround = 2
            scene ep3_284_d with dissolve
            mc "I'm sorry, but I don't feel like drinking anymore beer."
            yui "..........."
            mc "I'm going to bed now."
            yui "....Okay."
            jump ep3_p3_sleep
label ep3_p3_sleep:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_285 with dissolve
    s "While you're trying to sleep....."
    $ renpy.sound.play("sfx/phone vibrating.mp3")
    s "*Phone vibrates*...."
    stop sound
    if krystal_reply1_choice == 1:
        $ ep3_krystalmessage2 = True
        $ krystal_messages_show = True
        $ krystal_newmessage = True
    $ ep3_alicemessage2 = True
    $ newmessage = True
    $ alice_messages_show = True
    $ alice_newmessage = True
    $ phone_alert = True
    scene ep3_286 with dissolve
    u "....Hm?"
    if krystal_reply1_choice == 1:
        u "Did I just get new messages?"
        u "I wonder who sent them to me this late at night."
    else:
        u "Did I just get a new message?"
        u "I wonder who sent it to me this late at night."
    jump ep3_p3_msbsleep
label ep3_p3_msbsleep:
    scene ep3_287 with dissolve
    u "Okay, let's just check them...."
    if krystal_reply1_choice == 1:
        u "Hm? They're from [alice], and [krystal]."
    else:
        u "Hm? It's from [alice]."
    jump ep3_p3_msbsleep1
label ep3_p3_msbsleep1:
    if ep3_krystalmessage2 == True:
        if reply_krystal2 == False:
            scene ep3_287 with vpunch
            u "I need to reply the message first!"
            jump ep3_p3_msbsleep1
        elif reply_krystal2 == True:
            jump ep3_p3_sleep1
    else:
        jump ep3_p3_sleep1
label ep3_p3_sleep1:
    stop music fadeout 3.0
    scene ep3_285 with dissolve
    u "Alright, let's go back to sleep."
    scene black with dissolve
    $ renpy.pause()
    $ renpy.sound.play("sfx/Clock alarm.mp3")
    scene ep3_288 with dissolve
    s "*Clock alarms*......"
    u "Time really flies so fast. It's morning again."
    u "Alright, let's get up and go take a shower...."
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene ep3_289 with dissolve
    u "Okay, I finished taking shower and dressing up."
    u "Let's go have breakfast in the kitchen...."
    $ renpy.sound.play("sfx/Door opening.mp3")
    s "*Door opens*......"
    stop sound
    scene ep3_290 with dissolve
    u "....Hm?"
    scene ep3_291 with dissolve
    yui "......Hm?"
    mc "Good morning, [yui]."
    if ep3_secondround == 1:
        scene ep3_291_a1 with dissolve
        yui "Good morning."
        mc "Did you sleep well?"
        yui "Yes, I did. What about you?"
        mc "Me, too."
        scene ep3_291_a2 with dissolve
        mc "..........."
        yui "....Hm? Why are you looking at me like that?"
        mc "I thought you would look sad today, but you look better than I thought."
        scene ep3_291_a3 with dissolve
        yui "Well, I can't be sad forever, can I?"
        yui "I have no choice but to move on with my life."
        mc "Oh...."
        if ep3_comfortyui == 1:
            yui "Why do you seem so surprised?"
            yui "Weren't you the one telling me to wake up stronger today?"
            mc "Yes, I was...."
            u "But, I actually didn't expect her to look this happy to be honest."
            u "Something is wrong...."
        yui "Alright, let's not waste anymore time here. We better go have breakfast."
        mc "Sure then."
    elif ep3_secondround == 2:
        scene ep3_291_d with dissolve
        yui ".........."
        u "Hm? Is she ignoring me?"
        u "Well, maybe she's angry at me that I didn't go for a second round with her last night."
    jump ep3_p3_nextday
label ep3_p3_nextday:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_292 with fade
    u "Alright, it's time to work...."
    scene black with dissolve
    s "*8 hours later*......"
    scene ep3_293 with dissolve
    s "You and [yui] come to see [rin] and [zeke] afterwork."
    rin "There they are!"
    zeke "How was your day, guys?"
    scene ep3_294 with dissolve
    mc "Nothing new for me. It was just another day of working life."
    yui "Yeah, me too."
    zeke "I see...."
    zeke "Alright then, let's go back to our home sweet home!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_295 with fade
    s "About twenty minutes later, you guys have finally arrived home."
    rin "So...."
    rin "What are you guys going to do next?"
    zeke "I think I'll go take a shower, and get changed."
    scene ep3_296 with dissolve
    rin "What about both of you?"
    mc "I think I'm going to do that, too."
    yui "I'm just going to go get changed. I'll take a shower later before going to bed."
    yui "What about you?"
    rin "I'm going to go work on my project. The deadline is coming soon."
    rin "But, before I do that, I'm going to cook you guys food. What would you like to eat?"
    zeke "You don't need to cook for me today. I'll go eat out with [mika]."
    scene ep3_297 with dissolve
    mc "You sound busy already. You don't need to cook for me, too."
    mc "I don't want to bother you. I'll just find something to eat myself."
    yui "Yeah, you should spend your time working on the project instead of cooking us food to be honest."
    rin "It's okay! I'm always cooking for you guys. It's become a habit for me!"
    rin "Just tell me what you guys want to have for dinner."
    mc "....Are you sure?"
    rin "Of course, I am!"
    mc "Well then, please cook me an omelette rice."
    mc "I think it's easy to cook. So, you don't have to waste a lot of time cooking for us."
    yui "Then, can you make me a salad, please?"
    rin "Sure! Just come to the kitchen when you guys are ready, okay?"
    scene ep3_298 with dissolve
    zeke "[mc]."
    mc "...Hm?"
    zeke "I'm going to the shopping mall after having dinner with [mika]."
    zeke "Is there anything you want me to buy for you?"
    mc "Thanks for asking, but I don't want anything."
    zeke "No worries bro."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_299 with fade
    u "Alright, I finished taking a shower, and getting changed."
    u "Let's go to the kitchen...."
    scene ep3_300 with dissolve
    u "Oh, there she is...."
    u "Seems like she just finished cooking our food."
    rin "....Hm?"
    scene ep3_301 with dissolve
    rin "Oh? You got here faster than I expected."
    rin "I thought you would take more time before coming here."
    mc "Well, I'm not the kind of person who spends a lot time taking a shower."
    rin "Yeah, I can tell that..."
    rin "Alright then, your food is already ready. Come sit here!"
    scene ep3_302 with dissolve
    mc "I don't know if I've already said it to you, but thank you so much for always cooking for me."
    rin "Aw... You don't have to thank me at all. It's just a little help from me."
    mc "Well, I'm still very appreciative for your help though."
    mc "Anyway, where is your food? Aren't you going to eat?"
    scene ep3_303 with dissolve
    rin "Oh...No, I'm not."
    rin "I've gained weight recently. So, I'm on diet now!"
    mc "............."
    mc "You've gained weight? I didn't notice that at all...."
    mc "You look perfectly fine actually."
    rin "*Giggles*....Thanks!"
    scene ep3_304 with dissolve
    rin "Alright, I think I've got to leave now. Enjoy your dinner!"
    mc "Sure, I will."
    if sexwithrin == 1:
        scene ep3_304_a1 with dissolve
        rin "(Wait a sec....)"
        rin "(I don't think I should leave like this....)"
        rin "(*Giggles*....Hehe... Let's just....)"
        scene ep3_304_a2 with dissolve
        mc "....Hm?"
        rin "*Kisses*....Mwuah~!"
        u "Well, I completely didn't see this coming...."
        $ ep3_cheekkiss = 1
        $ rin_relationship += 1
        $ rin_ch1_ep3 += 1
        scene ep3_304_a3 with dissolve
        mc "You should've warned me..."
        rin "*Giggles*...I'm sorry! I just wanted to surprise you."
        mc "Yeah, you really surprised me."
        rin "*Giggles*.... A big thanks to you. I've just gained the energy to work tonight!"
        mc "....Well, I'm happy to help then."
        scene ep3_304_a4 with dissolve
        rin "Alright, I'm going to leave for real now."
        rin "See you tomorrow, [mc]."
        mc "Yeah, see you tomorrow."
    scene ep3_305 with dissolve
    rin "...Oh? You're finally here, [yui]."
    yui "Hm? You're leaving already?"
    rin "Yeah, I've just finished cooking. Your food is on the table."
    if ep3_cheekkiss == 1:
        scene ep3_306 with dissolve
        yui "Thank you so much. I wish you the best on your project."
        rin "Aw...Thanks. You're so sweet."
        mc "............"
        yui ".....Hm?"
        scene ep3_307 with dissolve
        yui "....Why are you smiling?"
        mc "What? No, I'm not smiling."
        yui "But, you just did...."
        yui "Whatever...."
    scene ep3_308 with dissolve
    s "You spend time having dinner with [yui]...."
    if ep3_secondround == 1:
        scene ep3_309 with dissolve
        mc "[yui]."
        yui "....Hm? What?"
        mc "Are you really okay?"
        yui "What do you mean?"
        scene ep3_310 with dissolve
        mc "I'm talking about what happened yesterday."
        yui "............"
        yui "*Sighs*....Well, to be honest I'm not okay at all."
        yui "Do you know how hard it was for me to see [pete] at the company today?"
        yui "But, what could I have done? I just had to act as if I was okay."
        scene ep3_310_a with dissolve
        mc "Look. There is something that I don't really understand."
        mc "If you love him that much, why don't you confess to him?"
        yui "What's the point in doing that? He already has feelings for someone else."
        yui "Listen. Let's just stop talking about this already, okay?"
        mc "Alright, if you say so."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_311 with dissolve
    u "Let's go back to my room....."
    scene ep3_312 with dissolve
    u "Alright, let's turn on the computer, and find something to do."
    $ renpy.sound.play("sfx/phone vibrating.mp3")
    s "*Phone vibrates*......"
    stop sound
    u "...Hm? Who's calling me now?"
    scene ep3_313 with dissolve
    mc "..........."
    mc "Hello, sir."
    stop music fadeout 3.0
    scene ep3_314 with fade
    play music "sfx/beach3.mp3" fadein 3.0
    $ bgm = "MusicbyAden & Atch - Sunrise"
    victor "Good evening, [mc]."
    mc "Good evening, sir."
    victor "How are you doing?"
    mc "I'm doing good, sir."
    scene ep3_315 with dissolve
    victor "Well, I'm glad to hear that."
    mc "Is there something that you want from me?"
    victor "Hm? I can call you only when I want something from you?"
    mc "No, sir. You can call me whenever you want."
    scene ep3_314 with dissolve
    victor "Well, there is nothing I want you to do... For now."
    victor "I'm just calling to check if you are okay."
    victor "No one suspects you, right?"
    mc "No, sir. I'm still staying under the radar."
    victor "Great...."
    victor "Alright, I'm going to hang up now. Let's talk again later."
    scene ep3_316 with dissolve
    mila "Wait, grandpa."
    victor "Hm? What's going on, my sweetie?"
    mila "Let me talk to him."
    victor "....Okay."
    scene ep3_317 with dissolve
    mila "Hi, [mc]."
    mc ".........."
    mc "...[mila]?"
    mila "Yes, it's me."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_318 with dissolve
    mila "So, how long are you planning to stay there?"
    mc "I don't know. Until my job is done?"
    mila "Well.... I can't wait to have you back here."
    mila "It's been so long since I saw you."
    mc ".........."
    scene ep3_319 with dissolve
    mila "[mc]."
    mc "....Hm?"
    mila "My grandpa promised you that he'll grant your wish if you can get the job sucessfully done."
    mila "Actually, that's how things usually work here. You get your reward after finishing your mission."
    mila "Do you still remember the promise you made {b}that{/b} night?"
    mc "............"
    mila "[mc]?"
    mc "....Yes, I do."
    scene ep3_320 with dissolve
    mila "Great. I'm glad to hear that."
    mila "Alright, I've got to go back to my grandpa now."
    mila "Let's talk again later."
    mila "Goodbye, [mc]. Stay safe."
    mc "You, too."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_321 with dissolve
    u "Alright, let's find something to do...."
    scene black with dissolve
    s "You spend time playing computer....."
    scene ep3_322 with dissolve
    u "Okay, that's enough for today...."
    u "Let's turn the computer off, and go to bed."
    if krystal_reply1_choice == 1:
        $ ep3_krystalmessage3 = True
        $ krystal_messages_show = True
        $ krystal_newmessage = True
        $ newmessage = True
        $ phone_alert = True
        $ renpy.sound.play("sfx/phone vibrating.mp3")
        s "*Phone vibrates*......"
        stop sound
        scene ep3_323 with dissolve
        u "Hm? I've got a new message."
        u "Let see who sent it to me...."
        jump ep3_p3_ksm3
    else:
        jump ep3_p3_night2
label ep3_p3_ksm3:
    if reply_krystal3 == False:
        scene ep3_323 with vpunch
        u "I need to reply the message first!"
        jump ep3_p3_ksm3
    elif reply_krystal3 == True:
        jump ep3_p3_ksm3answer
label ep3_p3_ksm3answer:
    if krystal_reply3_choice == 1:
        jump ep3_p3_hangout
    elif krystal_reply3_choice == 2:
        jump ep3_p3_night2
label ep3_p3_hangout:
    scene ep3_323_a1 with dissolve
    u "Okay, let's go to [krystal]'s room...."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_323_a2 with fade
    mc "Hi, [krystal]."
    krystal "Hi, [mc]!"
    krystal "I'm so glad to see you here again!"
    krystal "I was so afraid that you wouldn't want to hang out with me anymore."
    mc "Well, it wasn't your fault to be honest. So, I don't see any reason to do that."
    krystal "Thanks...."
    krystal "Alright, let's take a seat inside!"
    scene ep3_323_a3 with dissolve
    mc ".........."
    u "Seeing her makes me realise that there is nothing certain in our life."
    u "Even someone who used to be very successful like [krystal] can also end up like this."
    u "What a poor girl...."
    scene ep3_323_a4 with dissolve
    krystal "Have you eaten dinner yet?"
    mc "Yes, I have."
    krystal "Okay then, let me finish my dinner for a bit, okay?"
    mc "Sure. No problem."
    scene black with dissolve
    s "*Ten minutes later*....."
    scene ep3_323_a5 with dissolve
    krystal "...Alright, I've finished eating."
    krystal "What should we do next?"
    krystal "Do you have any ideas?"
    mc "............"
    krystal "...Hm?"
    scene ep3_323_a6 with dissolve
    krystal "[mc]?"
    mc "............"
    krystal "(*Sighs*....He doesn't listen to me at all....)"
    krystal "(I wonder what he is so busy doing with his phone that he doesn't pay attention to me at all...)"
    scene ep3_323_a7 with dissolve
    krystal "(Oh, He's playing games...)"
    mc "............."
    krystal "(....Well, I think I'll just have to wait until he finishes it.)"
    scene ep3_323_a8 with dissolve
    mc "Did you ask me something?"
    krystal "Thank god. You're finally talking to me now."
    mc "....I'm sorry."
    krystal "No worries. It wasn't anything important."
    krystal "I just asked for your idea on what we should do next."
    mc "I see..."
    scene ep3_323_a9 with dissolve
    krystal "So, what game was it that you just played?"
    mc "It's called PUBG mobile."
    krystal "Was it fun?.... Wait... Why did I even ask that question?"
    krystal "Of course, it must be fun, because it easily drew your attention away from me."
    mc "Well, I just downloaded it not too long ago, but I think it's pretty fun though."
    mc "I think it is a good game for killing time."
    krystal "...Can I try it?"
    mc "Of course, you can."
    scene ep3_323_a10 with dissolve
    krystal "Okay... How do I play it? I've never played games before."
    mc "Well, you will spawn on the plane when the game starts."
    mc "Then, you have to choose where you want to land."
    mc "After landing, you have to be the last person surviving to win the game."
    mc "There are items randomly dropped in the map. You have to pick them up in order to be able to survive."
    krystal "Got it.... Let's try then!"
    scene black with dissolve
    s "*A few minutes later*......."
    scene ep3_323_a11 with dissolve
    krystal "....Aw! How did I die?"
    mc "You were shot by someone from behind...."
    krystal "*Giggles*...Hahaha... I didn't even notice there was someone behind me."
    krystal "I'm so bad, right?"
    mc "Well, it's your first time playing. This result is expected."
    scene ep3_323_a12 with dissolve
    krystal "Okay. I think I understand the game's concept now."
    krystal "Let's try one more round!"
    mc "Go ahead. You can play as much as you want."
    krystal "O-Oh! There is someone in front of me!"
    mc "Pick up the gun on your left side, and go kill him."
    krystal "Roger that!"
    scene ep3_323_a13 with dissolve
    krystal "*Giggles*...Hehe... I got him!"
    mc "..........."
    mc "....[krystal]."
    krystal "Aw! I die again...."
    scene ep3_323_a14 with dissolve
    krystal "...Hm? Did you call me?"
    mc "Yes, I did."
    krystal "Why? Is there something that you want from me?"
    mc "I know everything about you now."
    krystal "..........."
    scene ep3_323_a15 with dissolve
    krystal "...Oh, did you search for it on the internet?"
    mc "Yes, I did."
    krystal "Do you believe it?"
    krystal "I mean....."
    krystal "Do you believe that I'm a bad person like they said."
    mc "No, I don't."
    mc "Even though I've only known you for a couple of days, I don't think you're a bad person."
    mc "There must be something that people don't know about it."
    krystal "....Thanks for saying that."
    krystal "....Do you want to know why I did that?"
    mc "It's up to you. If you want to tell me, then I'm here to listen to you."
    mc "But, if you don't want to talk about it again, then you don't have to tell me."
    stop music fadeout 3.0
    scene black with dissolve
    krystal "*Sighs*....Well, this is the story from my side...."
    play music "sfx/ep2_7.mp3" fadein 3.0
    $ bgm = "AERØHEAD - The Reckoning"
    scene ep3_323_a16 with fade
    krystal "Alright, well done everyone!"
    krystal "Let's take a short break."
    ivy "Yes! Finally!"
    scene ep3_323_a17 with dissolve
    ivy "Do you know how much I've been hoping for you to say that."
    jasmine "Yeah, we've been practicing nonstop for two hours already!"
    myla "Ahh... I'm so tired~"
    krystal "*Giggles*....Sorry, girls. We've only got three days left before the concert."
    krystal "I want to make sure everyone is going to do well."
    $ renpy.sound.play("sfx/phone vibrating.mp3")
    s "*Phone vibrates*....."
    stop sound
    krystal "Hm...?"
    scene ep3_323_a18 with dissolve
    krystal "Please, excuse me. I have to pick up this call."
    krystal "It's from my manager."
    ivy "Sure! You can talk as long as you want!"
    krystal "*Giggles*....You just want to have more time to rest, right?"
    jasmine "*Giggles*...I bet everyone does!"
    scene ep3_323_a19 with dissolve
    krystal "Hello?"
    krystal "Hm? Really? I've got an offer to be a brand ambassador?"
    krystal "What brand is it?"
    krystal "Really?! You aren't kidding me, right?"
    lucy "..........."
    scene black with dissolve
    krystal "After finish talking with my manager, we started practicing again."
    krystal "That's when everything began...."
    scene ep3_323_a20 with dissolve
    krystal "Increase your tempo, [lucy]."
    krystal "You're one step behind us."
    lucy "....Alright."
    ivy "*Giggles*....Are you still tired, [lucy]?"
    scene ep3_323_a21 with dissolve
    krystal "[lucy]?"
    krystal "Are you not feeling good today?"
    krystal "You're always one step behind us."
    lucy "Tsk...!"
    scene ep3_323_a22 with dissolve
    lucy "Keep practicing without me. I'm leaving!"
    ivy "....Wait! Where are you going?!"
    myla "Seriously? Are you going to leave like this?"
    krystal "[lucy]!"
    scene ep3_323_a23 with dissolve
    krystal "What's wrong? Are you angry at me?"
    krystal "Why are you being like this?"
    lucy "Really? You still don't know why I'm being like this?"
    krystal "....I'm sorry, okay? I know that I went hard on you."
    krystal "But, it's because I want us to have a good performance at our next concert."
    jasmine "Yeah, she is right. We have to work hard for our fans so that they won't be disappointed."
    scene ep3_323_a24 with dissolve
    lucy "Work hard? So, you're telling me that I'm not working hard enough?"
    lucy "After all these years as a trainee?"
    krystal "Calm down, [lucy]. She doesn't mean it like that."
    krystal "We all know how hard you have been working, but you also must admit that you didn't dance good enough."
    krystal "You usually do better than that. What's wrong?"
    scene ep3_323_a25 with dissolve
    lucy "Well, since we're arguing now, I'll let you know what I've been thinking for a while."
    lucy "I've been wondering what I am doing here."
    lucy "What have I always been practicing hard for?"
    lucy "I've been a trainee much longer than any of you here. {w}But, they chose you, who was a trainee for only 2 years, to be our leader."
    lucy "And when the sponsors, or the companies came to look for a presenter."
    lucy "Why did it have to always be you?"
    lucy "What did they see in you seriously?"
    myla "What? Why did you just say that?"
    ivy "Yeah, do you realise what you just said?"
    ivy "You should take your words back, and apologize to [krystal] now."
    krystal "Calm down, everyone. It's okay. She is just speaking her mind."
    scene ep3_323_a26 with dissolve
    lucy "Oh... How sweet of you. You're still not angry at me after everything I've said to you?"
    lucy "Stop pretending like you are a princess already. I'm sick of it."
    myla "You are the one who should stop here, [lucy]."
    myla "We shouldn't be arguing about these things here. We're a team!"
    lucy "Oh? Are we?"
    lucy "Are you guys really okay with your situation right now?"
    lucy "Don't you feel like we're just supporting actresses for [krystal] to shine brightly?"
    krystal "....Enough, [lucy]."
    lucy "Well, no matter how hard I tried to think about it,"
    lucy "I still don't understand why the company chose you to be the leader, and the center of our group instead of someone who has more experience like me."
    krystal "............."
    lucy "There is no way you've got backup, because you're an orphan. And your host family is just an ordinary family."
    lucy "So, how did you convince the company?"
    lucy "Oh...."
    lucy "......Did you sell your body to the president?"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_323_a27 with fade
    krystal "After that, I lost control of my anger, and you already saw the rest."
    mc "Well, after hearing your story, I can't blame you for doing that at all."
    krystal "But still, I shouldn't have done that. I should've tried harder to control my anger."
    krystal "I was so young, and immature back then."
    krystal "It was such an idiot action of me since I lost everything after that day...."
    scene ep3_323_a28 with dissolve
    mc "But, why didn't you tell everyone about what actually happened?"
    krystal "Who would believe me?"
    krystal "The CCTV only got the video of me slapping [lucy]'s face."
    krystal "It had no sound, and she turned her back towards the camera."
    krystal "So, no one knew what she said to me, except other members."
    krystal "They tried to help me, but their efforts were worthless, because fans already turned against me."
    scene ep3_323_a29 with dissolve
    krystal "I was so depressed back then."
    krystal "How could people easily say bad words to someone who they don't personally know."
    krystal "And the fact that they judged me, because of one single video made it even worse."
    krystal "That experience gave me a lesson that people just want to spread their hate towards someone, because they feel satisfied when doing that."
    krystal "Even if the real story was revealed, I don't think they would care."
    krystal "*Hics*....I'm sick of it. That's why I've been hiding from everyone for 2 years."
    mc "............"
    menu:
        "Comfort her [krystal2]":
            $ ep3_comfortkrystal = 1
            $ krystal_relationship += 2
            $ krystal_ch1_ep3 += 2
            scene ep3_323_a29_a with dissolve
            mc "Come here...."
            mc "I don't know how to comfort someone because I haven't had to do it before."
            mc "But, feel free to cry on my shoulder if it's going to help you get better."
            mc "I'll be here for you until you stop crying."
            krystal "*Hics*....T...Thank...you...."
        "Don't do anything":
            $ ep3_comfortkrystal = 2
            scene ep3_323_a29_d with dissolve
            krystal "*Hics*.........."
            u "I don't know what to do. She's been through a lot more than I expected."
            u "I don't think I'm in a position that I can comfort her."
            u "Let's just stay quiet...."
    scene black with dissolve
    s "*Half an hour later*......."
    scene ep3_324 at eyesblink("Ch.1/Ep.3/Scenes/ep3_324.jpg", "Ch.1/Ep.3/Scenes/ep3_324_blink.jpg", 1) with dissolve
    krystal "....I'm so sorry to have you see me cry."
    krystal "This is the first time in two years that I have had someone to vent my problems to."
    krystal "I couldn't even talk about it with my family, because I was so ashamed that I let them down."
    mc "It's okay. If you have any other problems, you can just vent them to me."
    mc "I'll be listening to you."
    krystal "...How sweet of you. Thank you so much."
    krystal "It really means a lot to me."
    mc "So, do you feel better now?"
    krystal "I think so. It feels so good that I finally got it off my chest...."
    krystal "Thank you again, [mc]."
    mc "Anytime...."
    mc "Alright, it's already so late. I think I should go to bed now."
    krystal "Oh, okay. Goodnight then."
    mc "Goodnight."
    jump ep3_p3_night2
label ep3_p3_night2:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ep3_323_d with dissolve
    u "Alright, let's go to bed...."
    scene black with dissolve
    s "Clock is ticking as the time flies by...."
    s "Once you realise that, it's already Saturday morning."
    scene ep3_326 with dissolve
    u ".........."
    u "What should I do today?"
    u ".........."
    scene ep3_327 with dissolve
    u "Well, I will think about it later."
    u "Let's just get up, and go have breakfast first."
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    $ ep3freeroam = True
    $ area = "mcroom"
    jump house_ep3
label house_ep3:
    if ep3hiddenimages_count == 7:
        $ ep3hiddenimages = True
    if area == "yuiroom" and ep3yuiroom == False:
        jump ep3yuiroom
    if area == "zekeroom" and ep3zekeroom == False:
        jump ep3zekeroom
    if area == "rinroom" and ep3rinroom == False:
        jump ep3rinroom
    if area == "kitchen":
        jump ep3_breakfastwithrin
    call screen ep3house
label ep3_breakfastwithrin:
    $ ep3endfreeroam = True
    $ ep3breakfastwithrin = True
    scene black
    scene ep3_336 with fade
    u "...Hm? That's [rin]."
    u "She's having breakfast alone."
    rin "...Hm?"
    scene ep3_337 with dissolve
    rin "Oh? Hi, [mc]!"
    mc "Hello."
    rin "Such a lovely morning, isn't it?"
    mc "Yes, it is...."
    scene ep3_338 with dissolve
    rin "What about everyone else?"
    rin "Have you talked to them?"
    rin "Aren't they coming for breakfast?"
    if ep3zekesleep == True:
        mc "I don't think so. [zeke] is still sleeping."
        mc "[mika]'s probably waiting for him to wake up."
    if ep3yuigoout == True:
        mc "And [yui], she is going to go see her family."
        mc "So, I don't know if she will come here."
    else:
        mc "I don't know. I guess they will probably have it later."
    rin "I see...."
    rin "Then, what are you waiting for? Take a seat!"
    mc "Sure."
    scene ep3_339 with dissolve
    rin "I forgot to ask you. Did you sleep well?"
    mc "Yes, I did. And you?"
    rin "*Sighs*...Well, not likely."
    rin "I was a bit stressed because of the project."
    rin "*Sighs*...These whole things are very new to me..."
    mc "What project have you been doing?"
    scene ep3_340 with dissolve
    rin "I've been creating contents for promoting the game we're going to release."
    mc "Oh, so you know everything now."
    rin "Yeah, [sandra] just told me. Do you know that she is my boss?"
    mc "I can guess that since she's the head of your department."
    rin "That's right."
    scene ep3_341 at eyesblink("Ch.1/Ep.3/Scenes/ep3_341.jpg", "Ch.1/Ep.3/Scenes/ep3_341_blink.jpg", 1) with dissolve
    rin "Well, up until now, I still can't believe that the Xecon Gear dream is going to be real very soon."
    rin "It will be so amazing, don't you think so?"
    mc "Yes, I do."
    mc "It's going to change humanity's future as no one could have imagined."
    rin "That's so true...."
    rin "I can't wait to have the gear now!"
    rin "I'm so excited to see how great the game is going to look with my own eyes!"
    scene black with dissolve
    s "*Fifteen minutes later*......."
    scene ep3_342 with dissolve
    rin "What are you planning to do today?"
    mc "Nothing special to be honest."
    mc "What about you?"
    rin "Well, I guess there isn't much I can do, but to keep working on finishing my project."
    mc "I see..."
    rin "But, I think it's still too early. So, I'm going to watch a movie first."
    rin "You know.... I can't spend all of my time working. I've got to relax, too."
    mc "I agree with that."
    rin "Do you want to join me?"
    u "Well, it wouldn't be so bad to watch a movie with her for a couple hours...."
    mc "Okay, let's go then."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_343 with dissolve
    rin "*Giggles*...It's been a while since we spent time watching TV together."
    mc "Yeah...."
    rin "Is there a specific movie that you want to watch?"
    mc "No, there isn't."
    rin "Then, let me choose a movie to watch, okay?"
    mc "Sure. Go ahead."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_344 with dissolve
    s "You spend time watching a movie with [rin]...."
    if sexwithrin == 1:
        rin "............"
        scene ep3_344_a1 with dissolve
        mc "....Hm?"
        rin "*Giggles*....Hehe..."
        rin "This is much better."
        rin "You don't mind me borrowing your shoulder, right?"
        menu:
            "Put your hand on her shoulder\n[rin1]":
                $ ep3puthandonrin = 1
                $ rin_relationship += 1
                $ rin_ch1_ep3 += 1
                scene ep3_344_a1_a1 with dissolve
                mc "No, I don't."
                rin "Heh~ It's good to see that you know what to do."
                rin "*Giggles*....Hehe..."
            "Do nothing":
                $ ep3puthandonrin = 2
                scene ep3_344_a1_d with dissolve
                mc "No, I don't."
                rin ".........."
                rin "(To be honest, I expected him to put his hand on my shoulder, too...)"
                rin "(Seems like my expectation was too much...)"
        s "*Foot steps are coming*......"
        scene ep3_344_a1_a2 with dissolve
        mc "Someone is coming...."
        rin "Aw.... What a bad timing...."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_345 with dissolve
    zeke "Good morning, guys!"
    mika "Hello, [mc]. Hi, [rin]."
    mc "Hi."
    rin "Hello, guys!"
    scene ep3_346 with dissolve
    zeke "Have you guys had breakfast yet?"
    rin "Yes, we just ate."
    zeke "Oh, I'm so sorry..."
    mc "Hm? Why did you say that."
    zeke "We didn't have breakfast together because I woke up late today."
    rin "It's okay! It's Saturday today. You don't have to wake up early at all."
    rin "Also, I think we don't really need to always have breakfast together."
    scene ep3_347 with dissolve
    zeke "Thanks for saying that."
    rin "You're welcome."
    zeke "Alright then, we're going to the kitchen now."
    zeke "Please, excuse us."
    rin "Sure. Go ahead."
    scene black with dissolve
    if sexwithrin == 1 and ep3puthandonrin == 1:
        scene ep3_344_a1_a1 with dissolve
    elif sexwithrin == 1 and ep3puthandonrin == 2:
        scene ep3_344_a1_d with dissolve
    else:
        scene ep3_344 with dissolve
    s "After both of them have left, you continue watching a movie with [rin]."
    scene black with dissolve
    s "*Half an hour later*........"
    $ renpy.sound.play("sfx/doorbell.mp3")
    scene ep3_348 with dissolve
    stop sound
    mc "............."
    mc "....Did you hear that?"
    rin "Yeah, I did."
    mc "Was it from our house?"
    rin "Ummm....? I don't think so. I didn't hear it clear enough because of the movie's sound."
    rin "Wasn't it from the next house?"
    mc "Maybe...."
    scene ep3_349 with dissolve
    $ renpy.sound.play("sfx/doorbell.mp3")
    s "*Doorbell sounds*......"
    stop sound
    mc "Hm? I think it's from our house."
    rin "Yeah, I agree with you now."
    scene ep3_350 with dissolve
    mc "Is it your friend? Could it be either [elaine], or [wendy]?"
    rin "I don't think so..."
    rin "They didn't tell me that they will visit us today."
    mc "Then, what about [zeke]'s friend?"
    rin "Beside you, his only friends is me and [mika]...."
    mc "............"
    rin "..........."
    rin "Well, he does have friends, but I don't think they're close enough to visit him on the weekend like this."
    mc "Okay then, I'll go see who it is."
    rin "Sure. Do you want me to pause the movie?"
    mc "No. You can continue watching it if you want."
    rin "Are you sure?"
    mc "Yeah, don't worry about me."
    scene ep3_351 with dissolve
    $ renpy.sound.play("sfx/doorbell.mp3")
    s "*Doorbell sounds*......"
    stop sound
    mc "Coming...."
    scene black with dissolve
    stop music fadeout 3.0
    mc "Who is it-"
    scene ep3_352 at eyesblink("Ch.1/Ep.3/Scenes/ep3_352.jpg", "Ch.1/Ep.3/Scenes/ep3_352_blink.jpg", 1) with dissolve
    play music "sfx/Nextday.mp3" fadein 3.0
    $ bgm = "Bensound - Perception"
    alice "Surprise!!!!"
    mc "............"
    alice "Hm? Why aren't you saying anything?"
    mc "....[alice]?"
    alice "*Giggles*...Yep, it's me!"
    alice "*Giggles*...Hehe... Do you like my surprise?"
    mc "....How did you get here?"
    alice "Well, I took a train, and got off at the center of the city."
    alice "Then, I took a taxi here."
    mc ".....I see."
    scene ep3_353 at eyesblink("Ch.1/Ep.3/Scenes/ep3_353.jpg", "Ch.1/Ep.3/Scenes/ep3_353_blink.jpg", 1) with dissolve
    alice "*Giggles*...Hehe... I missed you so much."
    alice "It's been awhile since I saw you last time."
    alice "Do you miss me?"
    mc "..........."
    alice "It's okay. You don't have to answer me."
    alice "By the way, are we going to keep talking here?"
    alice "Aren't you going to invite me in?"
    alice "And we can go hang out in the city together later."
    menu:
        "Invite her [alice1]":
            $ ep3invitealice = 1
            $ alice_relationship += 1
            $ alice_ch1_ep3 += 1
            u "To be honest, I don't like this kind of surprise."
            u "But, East town is pretty far from here..."
            u "I know how boring it was to sit on the train for many hours."
            u "It would take a lot of effort for her to come here."
            alice "Hm? What do you say?"
            scene ep3_354_a1 at eyesblink("Ch.1/Ep.3/Scenes/ep3_354_a1.jpg", "Ch.1/Ep.3/Scenes/ep3_354_a1_blink.jpg", 1) with dissolve
        "Don't invite her":
            s "This choice will end your relationship with [alice]. You'll no longer see her in the future."
            s "Are you sure that you want to do this?"
            menu:
                "Yes, I am":
                    $ ep3invitealice = 2
                    mc "I'm sorry, but I think you should go back to East Town."
                    scene ep3_354_d1 at eyesblink("Ch.1/Ep.3/Scenes/ep3_354_d1.jpg", "Ch.1/Ep.3/Scenes/ep3_354_d1_blink.jpg", 1) with dissolve
                    alice "...Hm? What did you just say?"
                    mc "I told you to go back to East Town."
                    alice "...You're just kidding me, right?"
                    mc "No, I'm not."
                    alice "............"
                    alice "Why did you just say that? I came a long way to see you here..."
                    alice "Is it because I come here without telling you?"
                    mc "Well, I do hate this kind of surprise, but it isn't the reason."
                    scene ep3_354_d2 at eyesblink("Ch.1/Ep.3/Scenes/ep3_354_d2.jpg", "Ch.1/Ep.3/Scenes/ep3_354_d2_blink.jpg", 1) with dissolve
                    mc "Look. I know that you've been crushing on me."
                    mc "And I'm thankful for your feelings."
                    mc "But, I just don't see the picture of me going out with you."
                    alice "....How can you know that? We haven't even tried yet."
                    mc "That will be just a waste of time."
                    alice "..............."
                    alice "Then, why have you always been texting with me if you don't like me?"
                    mc "I was just trying to be polite."
                    mc "But, I think it's time to stop now."
                    alice "............."
                    mc "Thank you for the 4 years of friendship even though we didn't spend much time talking to each other."
                    mc "Goodbye, [alice]. I hope you find a better guy than me."
                    alice "*Hics*...W...Wait!"
                    $ alice_relationship = 0
                    $ alice_ch1_ep3 = 0
                    scene black with dissolve
                    $ renpy.sound.play("sfx/Door closing.mp3")
                    $ renpy.pause()
                    stop sound
                    scene ep3_354_d3 with dissolve
                    rin "What took you so long?"
                    rin "Did something bad happen?"
                    mc "Nothing..."
                    mc "It was my friend."
                    mc "You don't need to worry about that."
                    scene ep3_354_d4 with dissolve
                    rin "Hm? Then, why didn't you invite your friend in?"
                    mc "There was another thing that just came up for her to deal with."
                    rin "I see..."
                    rin "So, I've just missed the opportunity to get to know your friend. How unlucky I am..."
                    scene black with dissolve
                    s "*An hour later*........"
                    scene ep3_354_d5 with dissolve
                    rin "Okay, the movie is over."
                    rin "Not bad.... I think it has just become one of my top 10 favorite movies."
                    mc "Has it?"
                    rin "Yeah... Alright, I think I've got to leave now."
                    rin "I'm going to continue working on my project."
                    mc "Okay. Good luck with your project."
                    rin "Thank you! See you later, [mc]."
                    mc "See you."
                    scene ep3_354_d6 with dissolve
                    u "Alright, I think it's time for me to go, too...."
                    jump ep3_p3_thirdnight
                "No, I've changed my mind [alice1]":
                    $ ep3invitealice = 1
                    $ alice_relationship += 1
                    $ alice_ch1_ep3 += 1
                    scene ep3_354_a1 at eyesblink("Ch.1/Ep.3/Scenes/ep3_354_a1.jpg", "Ch.1/Ep.3/Scenes/ep3_354_a1_blink.jpg", 1) with dissolve
    mc "Okay. Let's talk inside."
    alice "*Giggles*....Hehe... Okay!"
    scene ep3_354_a2 with dissolve
    alice "Aw... I'm so excited to see your new house!"
    mc "Well, technically, this isn't my house."
    mc "It's a shared house...."
    alice "*Giggles*....I know!"
    mc "Follow me. I'm going to introduce you to my housemate."
    alice "Whatever you say!"
    scene ep3_354_a3 with dissolve
    rin "Oh, you're back?"
    mc "Yes, I am."
    rin "What took you so long...."
    rin "....Hm? Who is that?"
    scene ep3_354_a4 with dissolve
    mc "This is my friend from the university, [alice]."
    alice "Hello. Nice to meet you!"
    scene ep3_354_a5 with dissolve
    mc "And this is my housemate, [rin]."
    rin "Hi, I'm [rin]. Nice to meet you, too!"
    rin "You're so cute!"
    alice "Aw! Don't say that!"
    alice "You're so beautiful, too!"
    rin "*Giggles*....Hehe... Thanks!"
    scene ep3_354_a6 with dissolve
    mc "Alright then, go sit with [rin] and wait for me here."
    mc "I'm going to take a shower."
    alice "Sure!"
    scene ep3_354_a7 with dissolve
    rin "Come sit here."
    rin "*Giggles*...I can't wait to get to know you!"
    alice "Me, too!"
    scene ep3_354_a8 with dissolve
    rin "You must be so tired, right?"
    rin "You travelled such a long way."
    rin "Please, sit and take a deep breath."
    alice "Hm? How did you know that?"
    scene ep3_354_a9 with dissolve
    rin "Well, [mc] said that you're his friend from the university."
    rin "So, I assume that you must be living in East Town now."
    alice "Oh yeah, you're right."
    alice "It took me almost 5 hours to get here!"
    scene ep3_354_a8 with dissolve
    rin "Did you come here just to visit [mc]?"
    alice "Actually no, I didn't."
    alice "I have a meeting with a music entertainment company here."
    alice "They want to buy my song, so they called me to come here and talk with them in person."
    rin "Wow! You're a composer?"
    alice "Yeah, I'm a freelance composer. What about you?"
    rin "I'm working at Xecon company."
    alice "Hm? You and [mc] are working for the same company?"
    rin "Yeah, everyone in this house works there, too."
    alice "I see..."
    rin "By the way, does [mc] know about that?"
    scene ep3_354_a9 with dissolve
    alice "No, he doesn't. I haven't told him yet."
    rin "Then, you should tell him! I'm sure that he'll be happy for you."
    alice "Really?"
    rin "Yeah! Why not? His friend is being successful right now."
    alice "*Giggles*....It's just one song that they want to buy."
    alice "I'm still so far from being successful."
    rin "Come on. You'll never know that!"
    alice "*Giggles*...Thanks."
    scene ep3_354_a8 with dissolve
    rin "By the way, I'm still surprised to see that [mc] has another friend besides us."
    alice "....Us?"
    rin "Oh, I meant everyone in this house."
    rin "You know... He is kind of like.... That."
    alice "*Giggles*....I know right!"
    alice "I'm glad to see you being his friend, too!"
    alice "He was always alone when studying at the university."
    alice "Even when it came to working as a group, he didn't hesitate to ask the professor to allow him to work alone."
    rin "Hm? How do you know about that?"
    rin "You guys didn't study in the same faculty."
    alice ".... Well, I asked someone from his faculty."
    scene ep3_354_a10 with dissolve
    rin "I see..."
    rin "You really care about him."
    rin "[mc] has a really good friend, doesn't he?"
    alice "..A..Actually, I don't know if I can consider myself his friend to be honest."
    rin "Hm? Why?"
    alice "...W..Well, I've known him for 4 years, but we didn't spend much time together..."
    alice "The amount of time that we've actually had a conversation together is even countable..."
    scene ep3_354_a11 with dissolve
    rin "Hm? How is that even possible?"
    alice "...Well... We didn't talk with each other that much."
    alice "It's just me... Following him around."
    rin "Heh~ I see now...."
    scene ep3_354_a12 with dissolve
    rin "You like him, don't you?"
    alice "...Hehe... Yes, you're right."
    rin "Now, it makes more sense why you're paying him a visit here."
    rin "I know you said that you came here because of your business meeting with the music company."
    rin "But still, you've come here too early since it's only 10 a.m. now."
    alice "...Hehehe... You got me now."
    scene ep3_354_a13 with dissolve
    if sexwithrin == 1:
        rin "Well, then...."
        rin "Since you're so open to me like this, I'll be frank towards you as well."
        rin "I also like [mc], too."
    else:
        rin "Well, you will have to put more effort in then."
        alice "...Hm? What are you talking about?"
        rin "From what I've seen, [mc] is pretty popular here."
    scene ep3_354_a14 with dissolve
    if sexwithrin == 1:
        alice "W-What? Are you for real?"
        rin "Yes, I am."
        rin "But, don't worry. I won't do anything bad to you only because we like the same guy."
        rin "*Giggles*...I just want you to know that you have a rival now."
    else:
        alice "W-What? Is that true?"
        rin "Yes, it is. Many girls seem to like hanging around him."
        alice "...Then, what should..."
    scene ep3_354_a15 with dissolve
    mc "Let's go, [alice]."
    alice "!!!!"
    alice "[mc]?!"
    mc "Hm? Why are you so shocked to see me?"
    mc "Were you having a conversation that I'm not allowed to hear?"
    alice "N-No, we weren't!"
    rin "(*Giggles*.....She's so cute....)"
    scene ep3_354_a16 with dissolve
    mc "Alright then, let's go."
    alice "....O-Oh!"
    scene ep3_354_a17 with dissolve
    mc "Thanks for staying with [alice], [rin]."
    rin "You're welcome!"
    mc "We're going to the central city."
    mc "If there is something that you want me to buy, you can text me."
    rin "Roger that!"
    scene ep3_354_a18 with dissolve
    mc "Okay then, let's go."
    alice "(I've never seen him talking so much like this.)"
    alice "(...He has become quite talkative, hasn't he?)"
    alice "(I think I feel more comfortable talking to him now.)"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a19 with fade
    mc "Alright, we've arrived."
    mc "What do you want to do first?"
    alice "Ummm.... I want to go buy a dress first."
    mc "Hm? A dress? Why do you want to buy that?"
    scene ep3_354_a20 with dissolve
    alice "Well, I have a business meeting here this evening."
    alice "I think it would be inappropriate to go with my current outfit."
    mc "Hm? What business meeting?"
    alice "I've got a company wanting to buy my song."
    mc "Really?"
    alice "Yeah, that's the reason why I come here in the first place!"
    mc "Congratulations."
    alice "*Giggles*...Thanks!"
    mc "Alright, let's go then."
    scene ep3_354_a21 with dissolve
    s "Welcome, customers!"
    s "Feel free to look around!"
    s "There are changing rooms right there in case you want to try on our clothes."
    scene black with dissolve
    s "*About an hour later*......."
    scene ep3_354_a22 with dissolve
    u "I heard that many women can spend hours in clothes store."
    u "At first, I didn't buy that. But I think I believe it now."
    mc "............"
    alice "...Ahem, [mc]."
    scene ep3_354_a23 with dissolve
    mc "....Hm?"
    scene ep3_354_a24 at eyesblink("Ch.1/Ep.3/Scenes/ep3_354_a24.jpg", "Ch.1/Ep.3/Scenes/ep3_354_a24_blink.jpg", 1) with dissolve
    alice "How do I look?"
    mc "............"
    alice "...Hm?"
    mc "You look great."
    alice "Really? Do I really look great?"
    mc "....Yes, you do."
    alice "Okay, wait a sec..."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a25 at eyesblink("Ch.1/Ep.3/Scenes/ep3_354_a25.jpg", "Ch.1/Ep.3/Scenes/ep3_354_a25_blink.jpg", 1) with dissolve
    alice "What about this one?"
    mc "You look more mature wearing this one."
    mc "Also, I think the color red looks good on you."
    alice "*Giggles*...Thanks. I'm glad to hear that."
    alice "There is one more...."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a26 at eyesblink("Ch.1/Ep.3/Scenes/ep3_354_a26.jpg", "Ch.1/Ep.3/Scenes/ep3_354_a26_blink.jpg", 1) with dissolve
    alice ".....Any thoughts?"
    mc "....I think it's better to wear this when you have to go to a party."
    mc "But, it's a little bit too much for a business meeting."
    alice "...Yeah, I agree with that."
    alice "I didn't expect it to be this revealing."
    alice "By the way, which one do you think I should buy?"
    mc "Well, it's up to you."
    alice "No, I want you to choose it for me."
    mc "..........."
    mc "Alright then....."
    menu:
        "The white one":
            $ ep3alicedress = 1
            mc "I think I prefer you to wear the white one."
            mc "It's the best dress to wear for your meeting this evening, in my opinion."
        "The red one":
            $ ep3alicedress = 2
            mc "I think I prefer you to wear the red one."
            mc "It can be worn in many different occasions. So, I think it is worth to buy."
        "This one":
            $ ep3alicedress = 3
            mc "Well, I think I prefer you to wear this."
            mc "Even though it's too revealing, but I think you look sexier wearing it."
            mc "It gives me a different feeling when looking at you."
    alice "Really?"
    mc "Yeah."
    alice "Okay, I'll buy it then!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a27 with dissolve
    alice "(*Giggles*...Hehe... I've never imagined that I would have a chance to do that.)"
    alice "(...[mc] helping me choose a dress....)"
    alice "(*Giggles*...It's like we're dating!)"
    alice "(...Hehehe....)"
    alice "(Alright, let's change my outfit back. I shouldn't let him wait for me any longer.)"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a28 with dissolve
    s "Thank you, customers!"
    s "Please come back again soon!"
    alice "(*Giggles*...Hehe... The dress that [mc] picked for me.)"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a29 with dissolve
    alice "....Hehehe...."
    mc "What are we going to do next?"
    alice "...Hehehe...."
    mc "[alice]!"
    scene ep3_354_a30 with dissolve
    alice "W-What?"
    mc "What were you thinking?"
    mc "Why did you keep giggling when I asked you a question?"
    alice "Well, I was so happy that I didn't hear you asking."
    scene ep3_354_a31 with dissolve
    mc "It's just a dress...."
    mc "You don't have to be that happy."
    alice "Of course, I do!"
    alice "This dress is the first thing you've ever chosen for me!"
    mc "....Okay. I won't argue that."
    alice "What did you just ask me though?"
    mc "I asked for your opinion on what we should do next."
    scene ep3_354_a32 with dissolve
    alice "Let's go to the theatre!"
    mc "Theatre?"
    alice "Yeah! Let's watch a movie!"
    alice "There is the movie that I've been waiting to watch since I saw the trailer!"
    mc "Alright then, let's go."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a33 with dissolve
    alice "Those are our seats."
    alice "Let's go."
    mc "Okay."
    scene ep3_354_a34 with dissolve
    alice "*Giggles*...Hehe... I'm so excited!"
    alice "This is the first time we come to a theatre together!"
    mc "You're so overreacting..."
    alice "*Giggles*...I know right?"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a35 with dissolve
    s "You and [alice] spend time watching a movie together...."
    scene black with dissolve
    s "*About two hours later*........"
    scene ep3_354_a36 with dissolve
    alice "How was the movie?"
    mc "Well, it was pretty fun. It was better than I thought it would be."
    alice "Of course! It's the movie I was waiting to watch!"
    alice "There was no way it was going to be bad."
    scene ep3_354_a37 with dissolve
    mc "Okay then, what do you want to do next?"
    alice "Umm...I don't know...."
    alice "Oh! What about we g-"
    s "*Stomach growls*......."
    scene ep3_354_a38 with dissolve
    alice ".....Ah!"
    mc "............"
    alice "..........."
    mc "Let's go find something to eat then."
    alice "....Yeah, I was about to say that...."
    scene ep3_354_a39 with dissolve
    alice "Is there a Chinese restaurant nearby?"
    alice "I want to have Chinese food."
    mc "Let's see...."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a40 with dissolve
    alice "Have you ever been here before?"
    mc "No, I haven't."
    mc "But, I guess my co-workers have since they just went to a Chinese restaurant recently."
    mc "And this restaurant is pretty close to my company."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a41 with dissolve
    waiter "Welcome to our restaurant, customers!"
    waiter "What would you like to have?"
    scene ep3_354_a42 with dissolve
    mc "You wanted to come here, [alice]."
    mc "I'll let you order the food."
    alice "Alright then!"
    scene ep3_354_a43 with dissolve
    alice "Ummm.... I'd like to have Sichuan pork."
    waiter "Sichuan Pork..."
    alice "And.... Dumplings."
    waiter "Dumplings...."
    alice "Peking Roasted Duck."
    alice "Ma Po Tofu."
    alice "And.... A set of steamed buns, please."
    waiter "Got it. Please, wait a moment."
    scene ep3_354_a44 with dissolve
    mc "You ordered quite a lot...."
    alice "Hm? Did I?"
    mc "Yeah, are you sure that we can eat all that?"
    alice "Of course, we can!"
    alice "I'm sooooo hungry right now!"
    mc "Yeah, I believe you...."
    scene ep3_354_a45 at eyesblink("Ch.1/Ep.3/Scenes/ep3_354_a45.jpg", "Ch.1/Ep.3/Scenes/ep3_354_a45_blink.jpg", 1) with dissolve
    mc "By the way, you know a lot of Chinese foods, don't you?"
    mc "You ordered them without even looking at the menu."
    alice "Well, Chinese food is one of my favorite foods to eat."
    alice "So yeah, I know a lot of them."
    mc "I see...."
    scene ep3_354_a46 with dissolve
    mc "What time is your meeting?"
    alice "It's at 4.30 p.m."
    alice "But, I think I should be there at least a half an hour before."
    mc "Okay then, we don't have to hurry."
    mc "We still have time left."
    alice "Yeah."
    scene ep3_354_a47 with dissolve
    waiter "Sorry to keep you waiting...."
    alice "No problem!"
    waiter "I'm going to serve the food now."
    scene black with dissolve
    s "You spend time eating with [alice]...."
    s "*About an hour later*......."
    scene ep3_354_a48 with dissolve
    alice "Aww... My stomach...."
    alice "*Giggles*....I wonder if I can wear the dress now...."
    scene ep3_354_a49 with dissolve
    alice "Are you full, [mc]?"
    scene ep3_354_a50 with dissolve
    mc "Yes, I am."
    alice "How was the food?"
    mc "It was so delicious."
    scene ep3_354_a49 with dissolve
    alice "Right? I couldn't agree more!"
    alice "I think I've just found my favorite Chinese restaurant in this city!"
    alice "I'll surely come back here again in the future."
    scene ep3_354_a50 with dissolve
    mc "That's good for you."
    mc "Since we are full now, let's pay the bill, and leave then."
    mc "The clock is ticking."
    alice "Sure, let's leave!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a51 at eyesblink("Ch.1/Ep.3/Scenes/ep3_354_a51.jpg", "Ch.1/Ep.3/Scenes/ep3_354_a51_blink.jpg", 1) with dissolve
    alice "Okay... It's sad, but I think we have to say goodbye now."
    alice "I've got to go to the meeting."
    mc "Yeah, sure."
    alice "Thanks for today, [mc]. It was so much fun."
    alice "I hope I'll have a chance to spend time with you again."
    mc "We'll see..."
    scene ep3_354_a52 at eyesblink("Ch.1/Ep.3/Scenes/ep3_354_a52.jpg", "Ch.1/Ep.3/Scenes/ep3_354_a52_blink.jpg", 1) with dissolve
    alice "Alright, I've got to go for real."
    alice "Goodbye, [mc]. See you later!"
    mc "Good luck with your business meeting, too."
    mc "I hope it turns out as you wish."
    alice "*Giggles*... Thank you! I hope so!"
    $ ep3hangoutwithalice = True
    $ alice_relationship += 3
    $ alice_ch1_ep3 += 3
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a53 with dissolve
    u "Okay.... Let's go back home...."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_354_a54 with dissolve
    u "Alright, I've arrived home."
    u "Let's go to my room, and find something to do."
    jump ep3_p3_thirdnight
label ep3_p3_thirdnight:
    stop music fadeout 3.0
    if ep3_givephonenumber == 1:
        scene black with dissolve
        s "*Many hours later*......"
        scene ep3_355 with fade
        mc ".........."
        $ ep3_krystalmessage4 = True
        $ krystal_messages_show = True
        $ krystal_newmessage = True
        $ newmessage = True
        $ phone_alert = True
        $ renpy.sound.play("sfx/phone vibrating.mp3")
        s "*Phone vibrates*......"
        stop sound
        u "....Hm?"
        scene ep3_356 with dissolve
        u "I've got a new message."
        u "Let's check it."
        jump ep3_p3_ksm4
    else:
        scene black with dissolve
        s "*Many hours later*......"
        jump ep3_p3_night3
label ep3_p3_ksm4:
    if reply_krystal4 == False:
        scene ep3_356 with vpunch
        u "I need to reply the message first!"
        jump ep3_p3_ksm4
    elif reply_krystal4 == True:
        jump ep3_p3_ksm4answer
label ep3_p3_ksm4answer:
    if krystal_reply4_choice == 1:
        jump ep3_p3_hangout2
    elif krystal_reply4_choice == 2:
        scene ep3_356_d with dissolve
        u "Let's continue learning about the code...."
        scene black with dissolve
        s "*One and a half hour later*....."
        jump ep3_p3_night3
label ep3_p3_hangout2:
    play music "sfx/ep.3/ep3_4.mp3" fadein 3.0
    $ bgm = "Sarah Jansen - Moments"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_356_a1 with dissolve
    u "Alright, [krystal] is waiting for me."
    u "Let's go to her room."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_356_a2 with dissolve
    u "Do I have to knock on the door first?"
    u "...Or I can just call her name?"
    u "....Let's knock on the door then."
    krystal "....What?! Did you just call me a noob?!"
    u "............."
    scene ep3_356_a3 with dissolve
    krystal "I'm not a noob! You're a noob!"
    krystal "I literally told you that the enemies were waiting for us."
    krystal "You didn't listen to me, and ran out of the house!"
    u "............"
    u "....Now, I'm starting to wonder if I made the right choice to let her try playing the game..."
    u "Should I knock on the door now?"
    u "She isn't going to be pissed at me, right?"
    scene ep3_356_a4 with dissolve
    u "...Screw it. Let's just do it."
    s "*Knocks*......"
    krystal "....Hm? [mc]?"
    mc "Yeah, it's me."
    krystal "O-Oh! Wait a sec!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_356_a5 at eyesblink("Ch.1/Ep.3/Scenes/ep3_356_a5.jpg", "Ch.1/Ep.3/Scenes/ep3_356_a5_blink.jpg", 1) with fade
    krystal "Welcome!"
    krystal "Hehe... You came here quicker than I thought."
    mc "Hi. Yes I was in my room. How is your day?"
    krystal "So-So. And you?"
    mc "Good.... I guess?"
    krystal "*Giggles*...What do you mean 'I guess'?"
    krystal "If you think it's good, then it's good."
    mc "Alright, if you say so..."
    scene ep3_356_a6 with dissolve
    krystal "Well, let's not just stand here."
    krystal "Come. We better take a seat first."
    mc "Okay."
    scene ep3_356_a7 with dissolve
    mc "What are we going to do today?"
    krystal "What about watching a series?"
    u "Ah... Here we go again...."
    if ep3hangoutwithalice == 1:
        u "I've spent so many hours watching TV today..."
    krystal "There is a series that I'm interested in right now."
    krystal "I want to watch it. What do you think?"
    mc "...Okay. If that's what you want."
    scene ep3_356_a8 with dissolve
    u "...Hm?"
    u "There are plenty of cup noodles right there..."
    u "Did she just buy them?"
    u "I don't think they were there last time I came here."
    scene ep3_356_a9 with dissolve
    mc "[krystal]."
    krystal "Hm? What?"
    mc "Why do you have so many cup noodles in your room?"
    mc "As I can recall, you also had a cup noodle as your dinner last time I came here, too."
    mc "You've been eating it too much recently."
    mc "Don't you know that it isn't good for your health."
    scene ep3_356_a10 with dissolve
    krystal "....Yeah, I know that."
    mc "Then, why....?"
    krystal "But, what could I have done?"
    krystal "You know... Spending 2 years living without working was really hard."
    krystal "I'm running out of money now."
    mc "Hm? How come?"
    mc "Weren't you supposed to earn a massive amount money back then?"
    mc "I mean.... You were very famous."
    krystal "Well yeah, I used to earn a lot of money."
    krystal "But I had to pay for the contract termination, and the compensation for damaging the company."
    mc "....What?"
    mc "They didn't even try to protect you, yet they demanded you to pay them?"
    scene ep3_356_a11 with dissolve
    krystal "*Giggles*....That was very unfair, right?"
    krystal "But, what could I have done? That's how this cruel world works."
    krystal "So, since I'm running out of money now, I have no choice, but to spend as little money as I can per day."
    mc "Why don't you start looking for a job then?"
    krystal "*Giggles*...Don't you think I've never tried to?"
    mc "............"
    krystal "Let alone a full-time job. I couldn't even find a part-time job."
    krystal "No one wanted to hire someone with a really bad self-image like me."
    mc "..........."
    scene ep3_356_a12 with dissolve
    krystal "Well, let's just stop talking about it, okay?"
    krystal "We need to look at the positive side. I still have enough money for at least 3 months!"
    krystal "So, I still have time to think about my future."
    mc "...Do you want me to help you?"
    krystal "Hm? How can you help me?"
    mc "I can lend you my money."
    krystal "*Giggles*...Really?"
    mc "...Yeah. How much do you need?"
    krystal "Thanks a lot. You're so kind."
    krystal "But, I don't want to bother you."
    krystal "This is my problem. I've been running away from it for 2 years already."
    krystal "I think it's time for me to face it now."
    mc "Alright, if you say so."
    krystal "*Giggles*...Come on. Stop talking about this serious thing!"
    krystal "We better watch the series!"
    mc "Sure."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_356_a13 with dissolve
    s "You spend time watching the series with [krystal]....."
    scene black with dissolve
    s "*An hour later*...."
    scene ep3_356_a14 with dissolve
    krystal "So, that was the end of the episode...."
    krystal "What do you think?"
    mc "It was pretty interesting."
    mc "I want to know what'll happen next."
    krystal "Me, too!"
    krystal "I can't wait for the next episode!"
    mc "By the way, what do you want to do next?"
    krystal "Ummm.... Do you still remember the game you let me play?"
    mc "Yes, I do."
    krystal "Can we play it together?"
    mc "....Sure."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_356_a15 with dissolve
    krystal "I was so close to get first place so many times, but I still haven't got it."
    krystal "*Giggles*....Hehe... Finally, I'm going to be a winner soon."
    mc "Hm? What makes you so confident?"
    krystal "You, of course!"
    krystal "*Giggles*....Please, carry me! I'm sure that you can lead me to victory!"
    mc "We'll see..."
    scene ep3_356_a16 with dissolve
    krystal "Ah! There is an enemy in front of us!"
    krystal "He is in the blue house on the second floor!"
    mc "Roger that. I'll take him down."
    krystal "Yes! That's right! Go kill him, [mc]!"
    mc "Don't just stand still watching me. You need to be careful, too."
    mc "We still haven't seen his teammate yet."
    krystal "Understood!"
    scene ep3_356_a17 with dissolve
    krystal "N..N...No!"
    krystal "Ah! I'm dead...."
    mc "...What? How?"
    krystal "I don't know..."
    krystal "I didn't hear the gun shot at all."
    mc "Did you stand close to a window?"
    krystal "....I think so."
    mc "...He must've shot you from a far distance away by a gun attached with a suppressor."
    krystal "...Yeah, that makes sense."
    mc "It's okay. I'll get them all."
    scene black with dissolve
    s "*About fifteen minutes later*....."
    scene ep3_356_a18 with dissolve
    krystal "There are only three people left!"
    krystal "Fighting, [mc]!"
    mc "Shh... I can't hear anything."
    krystal "O-Oh! I'm sorry."
    krystal "*Whispers*...Fighting..."
    scene black with dissolve
    krystal "Yeah! That's right!"
    krystal "...Take him down!"
    mc ".........."
    scene ep3_356_a19 with dissolve
    krystal "Aw! You did it!!"
    mc "....O..Oh."
    krystal "*Giggles*...I'm not disappointed that I put my hope in you at all!"
    krystal "You're so good at this game!"
    mc "*Coughs*...Take it easy, [krystal]..."
    scene ep3_356_a20 with dissolve
    mc "...I know that you're very happy."
    mc "But, don't you think that we're too close...?"
    krystal "...Hm?"
    krystal "............."
    scene ep3_356_a21 with dissolve
    krystal ".....Oh yeah, you're right...."
    krystal "I'm sorry."
    krystal "I'm going to take my hands off you now."
    mc "...Okay."
    scene ep3_356_a22 with dissolve
    krystal "..P..Please, don't mind me."
    krystal "I was too happy. I haven't had this much fun for such a long time."
    mc "It's alright. I understand you."
    krystal "...T-Thanks...."
    scene ep3_356_a23 with dissolve
    mc "Alright, I think I've got to leave now."
    krystal "Hm? Why is it so sudden?"
    mc "Well, I think we've had enough fun."
    mc "So, let's call it a day then."
    krystal "Okay, if you say so."
    krystal "Goodnight, [mc]."
    mc "You, too."
    $ ep3hangoutwithkrystal = True
    $ krystal_relationship += 2
    $ krystal_ch1_ep3 += 2
    scene black with dissolve
    $ renpy.pause()
    scene ep3_357 with dissolve
    u "Alright, let's go back to my room...."
    if sexwithrin == 1 and rin_relationship >= 20:
        $ ep3_rinmessage4 = True
        $ rin_messages_show = True
        $ rin_newmessage = True
        $ newmessage = True
        $ phone_alert = True
        $ renpy.sound.play("sfx/phone vibrating.mp3")
        s "*Phone vibrates*......"
        stop sound
        scene ep3_358 with dissolve
        u "....Hm?"
        u "I've got a new message again?"
        scene ep3_359 with dissolve
        u "It's from [rin]."
        u "Let's see what she sent me..."
        jump ep3_p3_rm4
    else:
        jump ep3_p3_spendnightalone
label ep3_p3_night3:
    scene ep3_356_d with dissolve
    if sexwithrin == 1 and rin_relationship >= 20:
        $ ep3_rinmessage4 = True
        $ rin_messages_show = True
        $ rin_newmessage = True
        $ newmessage = True
        $ phone_alert = True
        $ renpy.sound.play("sfx/phone vibrating.mp3")
        s "*Phone vibrates*......"
        stop sound
        u "....Hm?"
        scene ep3_356 with dissolve
        u "I've got a new message again?"
        u "It's from [rin]."
        u "Let's see what she sent me..."
        jump ep3_p3_rm4
    else:
        jump ep3_p3_spendnightalone
label ep3_p3_rm4:
    if reply_rin2 == False:
        if krystal_reply4_choice == 1:
            scene ep3_359 with vpunch
        else:
            scene ep3_356 with vpunch
        u "I need to reply the message first!"
        jump ep3_p3_rm4
    elif reply_rin2 == True:
        jump ep3_p3_rm4answer
label ep3_p3_rm4answer:
    if rin_reply2_choice == 1:
        jump ep3_p3_spendnightwithrin
    elif rin_reply2_choice == 2:
        jump ep3_p3_spendnightalone
label ep3_p3_spendnightwithrin:
    stop music fadeout 3.0
    if krystal_reply4_choice == 1:
        scene ep3_359_a1 with dissolve
    else:
        scene ep3_356_a1 with dissolve
    u "Alright, let's go to her room."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_359_a2 with fade
    play music "sfx/ep.3/ep3_8.mp3" fadein 3.0
    $ bgm = "Johny Grimes - Double Vision"
    rin "*Song hummings*........."
    rin "(*Giggles*...I can't wait for [mc] to be here...)"
    s "*Door knocks*......"
    rin "(...Hm? Is that him?)"
    scene ep3_359_a3 with dissolve
    rin "Who is it?"
    mc "It's me."
    mc "Can you open the door?"
    scene ep3_359_a4 with dissolve
    rin "(*Giggles*...Hehehe... He got here pretty fast.)"
    rin "Yeah, sure."
    rin "Wait a sec!"
    scene black with dissolve
    $ renpy.pause()
    scene ep3_359_a5 with dissolve
    rin "[mc]!"
    mc "...Hm?"
    scene ep3_359_a6 with dissolve
    mc "....What are you doing?"
    rin "Shh... Stand still."
    rin "I'm so exhausted...."
    rin "Let me recharge my energy~"
    mc "...Alright..."
    scene ep3_359_a7 with dissolve
    rin "*Giggles*...Hehe...Thank you."
    rin "I'm ready to continue working now!"
    mc "That's it? You called me here just to do that?"
    rin "*Giggles*...Of course not!"
    rin "I want you to stay with me while I'm working."
    rin "Can you do that for me, please?"
    menu:
        "Yes, I can. [rin1]":
            $ ep3spendnightwithrin = 1
            $ rin_relationship += 1
            $ rin_ch1_ep3 += 1
            scene ep3_359_a7_a1 with dissolve
            mc "...Okay. I'll stay with you."
            rin "*Giggles*...Thanks! I'm so glad to hear that!"
            rin "I'm so glad to see you...."
            rin "..........."
            mc "...Hm? See me what?"
            rin "Hehe... Nothing"
            rin "(I'm so glad to see him smile at me, but I'm not going to say that.)"
            rin "(That's only going to make him stop smiling.)"
            scene ep3_359_a7_a2 with dissolve
            rin "Alright, please go sit, and wait for me on my bed."
            rin "I'm going to pick up my laptop."
            mc "Sure."
            scene ep3_359_a7_a3 with dissolve
            rin "*Giggles*...Hehe... I'm so happy right now."
            rin "This is the first time that you come to stay in my room."
            mc "...To think about it.... Yeah, you're right."
            mc "I've been here before, but I've never really stayed here long."
            scene black with dissolve
            $ renpy.pause()
            scene ep3_359_a7_a4 with dissolve
            mc "..............."
            mc "By the way, what is the deadline date for your project?"
            mc "I kind of was wondering that since you've been very busy recently."
            rin "Well..."
            scene ep3_359_a7_a5 with dissolve
            rin "The real deadline date is in the next two weeks."
            rin "But, I have to send it to [sandra] this Monday."
            rin "She'll check, and discuss with me if there is something that could be fixed, or improved."
            mc "I see...."
            scene ep3_359_a7_a6 with dissolve
            rin "Okay then, if you don't mind...."
            rin "I'll continue working on the project."
            mc "Then, what am I supposed to do here?"
            rin "You can do whatever you want as long as you stay beside me."
            rin "*Giggles*...Your presence is already enough to give me motivation to work!"
            scene black with dissolve
            s "*About two hours later*......."
            scene ep3_359_a7_a7 with dissolve
            rin "Arrr.... Finally~~!"
            mc "Hm? Is it finished?"
            rin "Yes, it is! I feel so relieved now..."
            scene ep3_359_a7_a8 with dissolve
            rin "It took me so many days...."
            rin "I barely had a chance to spend time with you."
            mc "Well, you had no choice. It's your work."
            rin "I know...."
            scene ep3_359_a7_a9 with dissolve
            rin "But, everything is alright now!"
            rin "I'm going to make up for the lost time later."
            rin "However, let me rest on your shoulder for a sec..."
            mc "...Okay."
            scene ep3_359_a7_a10 with dissolve
            rin "Arr... It feels so comfortable every time I put my head on your shoulder..."
            rin "I wish we could stay like this forever..."
            mc "...That's not possible though."
            rin "I know...."
            rin "[mc]."
            mc "Hm....?"
            scene ep3_359_a7_a11 with dissolve
            rin "Since it's already so late, why don't you sleep here?"
            mc "...Are you sure?"
            rin "Yeah, why not?"
            rin "Don't you want to?"
            mc ".........."
            scene ep3_359_a7_a12 with dissolve
            mc "Okay then, let's sleep together."
            rin "*Giggles*...Good! That's what I wanted to hear!"
            rin "Alright, let's lie down then!"
            mc "Sure..."
            scene ep3_359_a7_a13 with dissolve
            rin "To be honest, I want to talk with you more."
            rin "But, I'm so tired today. I feel so sleepy now."
            mc "It's alright. You should sleep then."
            rin "*Giggles*...Okay then...."
            rin ".... Goodnight, [mc]."
            mc "Goodnight."
            $ ep3_alicemessage3 = True
            $ alice_messages_show = True
            $ alice_newmessage = True
            $ newmessage = True
            $ phone_alert = True
            jump ep3_p3_morningsex
        "I'm sorry.":
            $ ep3spendnightwithrin = 2
            scene ep3_359_a7_d with dissolve
            mc "..........."
            mc "I'm sorry, but I want to go back to my room."
            mc "I've also got to work to do."
            rin "....Oh..."
            rin "Okay then, you should leave now."
            jump ep3_p3_refuserin
label ep3_p3_morningsex:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    play music "sfx/ep.3/ep3_12.mp3" fadein 3.0
    $ bgm = "Brook Xiao - Fire (ft. Rachel Horter)"
    rin "...Mmmm...."
    u "...Hm? What is this strange voice....?"
    show ep3_rinbj with dissolve
    window hide
    u "...What? Is that, [rin]?"
    u "Why is she sucking my cock...?"
    u "Should I let her know that I'm already up?"
    $ renpy.pause()
    u "...Yeah, I should let her know."
    hide ep3_rinbj with dissolve
    scene ep3_359_a7_a15 with dissolve
    mc "[rin]...."
    rin "!!!!"
    rin "A-Ah...!"
    scene ep3_359_a7_a16 with dissolve
    rin "O-Oh?! You're awake?"
    mc "Yes, I am."
    rin "Er....."
    mc "............."
    scene ep3_359_a7_a17 with dissolve
    rin "Don't get me wrong, okay?"
    rin "I woke up, and saw that you had a boner...."
    rin "It looked like it was going to explode in your pants."
    rin "I was afraid that you were in pain."
    rin "So, I thought I was going to help you by giving you a handjob."
    rin "But, I have no idea how I ended up....Err...{w} You know what I'm talking about."
    scene ep3_359_a7_a18 with dissolve
    mc "Well, it's a common occurrence for many guys, and for men to have an erection when waking up in the morning."
    rin "...Really?"
    mc "Yeah, and I'm no exceptional, too."
    scene ep3_359_a7_a17 with dissolve
    rin "Then, should I continue...?"
    rin "You still haven't cum yet."
    mc "............"
    scene ep3_359_a7_a19 with dissolve
    mc "No, I've got another idea."
    rin "Aw...!"
    scene ep3_359_a7_a20 with dissolve
    rin "...W...What are you going to do?"
    u "I know that I shouldn't be doing this...."
    u "But, I can't stop myself..."
    mc "...Well, if you left it like that, it would've eventually gone down itself."
    mc "But, you just turned me on. And now, I want more..."
    rin "...Are we really going to do it again?"
    mc "...Can we?"
    rin "............"
    rin "....Okay, if that's what you want...."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_359_a7_a21 with dissolve
    mc "...Hm?"
    rin "....What's wrong?"
    mc "Nothing...."
    u "She's already quite wet...."
    show ep3_fingerrin1 with dissolve
    window hide
    rin "...A-Ah....!"
    mc "............"
    rin "*Softly breathes*.......Mmmmm...."
    rin "(...Even though I used to finger myself, it still feels weird having someone else touch my pussy...)"
    $ renpy.pause()
    hide ep3_fingerrin1
    scene ep3_359_a7_a22 with dissolve
    show ep3_fingerrin2
    window hide
    rin "*Softly breathes*...Ahhh...."
    rin "*Softly breathes*...D....Don't... Stop..."
    mc "...Okay...."
    $ renpy.pause()
    hide ep3_fingerrin2
    scene ep3_359_a7_a23 with dissolve
    rin "*Softly breathes*...W..Wait a sec."
    mc "...What's wrong?"
    rin "...Can you.... Use your tongue, please?"
    mc "Hm...? You want me to lick your pussy?"
    rin "....Yeah. Can you...?"
    mc ".....Okay."
    mc "Let's change to a more comfortable position then."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_359_a7_a24 with dissolve
    rin "Is it okay now?"
    mc "...Yes, it is...."
    scene ep3_359_a7_a25 with dissolve
    show ep3_lickrin1
    window hide
    rin "*Moans*...A-Ah...!"
    rin "*Softly breathes*.....This feels so good..."
    rin "*Softly breathes*.....P...Please...D...Don't... Stop..."
    $ renpy.pause()
    hide ep3_lickrin1
    scene ep3_359_a7_a26 with dissolve
    show ep3_lickrin2
    window hide
    rin "*Moans*...Mmmm....!"
    rin "*Moans*...Y..Yeah.... That's the spot...!"
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_lick2
            jump ep3lickrinslow
        "Finger her pussy":
            hide ep3_lick2
            jump ep3fingerrinslow
        "Next":
            hide ep3_lick2
            jump ep3rincow1
label ep3fingerrinslow:
    scene ep3_359_a7_a21 with dissolve
    show ep3_fingerrin1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ep3_fingerrin1
            jump ep3fingerrinfast
        "Lick her pussy":
            hide ep3_fingerrin1
            jump ep3lickrinslow
label ep3fingerrinfast:
    scene ep3_359_a7_a22 with dissolve
    show ep3_fingerrin2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_fingerrin2
            jump ep3fingerrinslow
        "Lick her pussy":
            hide ep3_fingerrin1
            jump ep3lickrinslow
label ep3lickrinslow:
    scene ep3_359_a7_a25 with dissolve
    show ep3_lickrin1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ep3_lickrin1
            jump ep3lickrinfast
        "Finger her pussy":
            hide ep3_lickrin1
            jump ep3fingerrinslow
label ep3lickrinfast:
    scene ep3_359_a7_a26 with dissolve
    show ep3_lickrin2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_lick2
            jump ep3lickrinslow
        "Finger her pussy":
            hide ep3_lick2
            jump ep3fingerrinslow
        "Next":
            hide ep3_lick2
            jump ep3rincow1
label ep3rincow1:
    scene ep3_359_a7_a27 with dissolve
    rin "Hm...? Why did you stop?"
    mc "I think it's time to go for the next step."
    rin "...What do you want to do next?"
    mc "Can you ride my cock?"
    rin "............."
    rin ".... Okay, let's try that..."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_359_a7_a28 with dissolve
    rin "...You're so big..."
    mc "Don't be in such a hurry. Just slowly put it in."
    rin "..O..Okay..."
    scene ep3_359_a7_a29 with dissolve
    rin "A-Ah!...It went in...!"
    mc "Well done..."
    mc "You can start moving now."
    scene ep3_359_a7_a30 with dissolve
    rin "Wait a sec...."
    rin "Let me take my top off first."
    mc "Okay..."
    scene ep3_359_a7_a31 with dissolve
    rin "...Aw... This is so embarrassing..."
    mc "....No, it isn't."
    mc "..........."
    mc ".....You're so beautiful."
    rin "...You're such a cheater to say something like that now...."
    rin "You know that?"
    mc "..........."
    rin "*Giggles*...But still, I'm glad to hear it from you..."
    scene black with dissolve
    $ renpy.pause()
    scene ep3_359_a7_a32 with dissolve
    rin "....Alright, I'm going to start moving now...."
    show ep3_rincow1 with dissolve
    window hide
    rin "*Softly breathes*....Mmmm...."
    rin "*Softly breathes*...Mmmm....Y..You're...so...big..."
    mc "Relax.... Take it easy...."
    $ renpy.pause()
    hide ep3_rincow1 with dissolve
    scene ep3_359_a7_a33 with dissolve
    show ep3_rincow2 with dissolve
    window hide
    rin "*Moans*....A...Ah...!"
    rin "*Moans*....Mmmm....This...feels...so...good...."
    rin "*Moans*...Ahhh...It's going in....and out so deep....inside my....."
    $ renpy.pause()
    hide ep3_rincow2 with dissolve
    scene ep3_359_a7_a34 with dissolve
    show ep3_rincow3 with dissolve
    window hide
    rin "*Heavily breathes*....Mmmmm....!"
    rin "*Heavily breathes*....A...Ahh... I'm...getting there...!"
    $ renpy.pause()
    menu:
        "Slowest":
            hide ep3_rincow3
            jump ep3rincowslow
        "Slower":
            hide ep3_rincow3
            jump ep3rincowfast
        "Cum":
            jump ep3rincowcum
label ep3rincowslow:
    scene ep3_359_a7_a32 with dissolve
    show ep3_rincow1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ep3_rincow1
            jump ep3rincowfast
        "Fastest":
            hide ep3_rincow1
            jump ep3rincowfastest
label ep3rincowfast:
    scene ep3_359_a7_a33 with dissolve
    show ep3_rincow2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ep3_rincow2
            jump ep3rincowslow
        "Faster":
            hide ep3_rincow2
            jump ep3rincowfastest
label ep3rincowfastest:
    scene ep3_359_a7_a34 with dissolve
    show ep3_rincow3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slowest":
            hide ep3_rincow3
            jump ep3rincowslow
        "Slower":
            hide ep3_rincow3
            jump ep3rincowfast
        "Cum":
            jump ep3rincowcum
label ep3rincowcum:
    rin "*Heavily breathes*...Mmmm!...I'm going to cum soon!"
    mc "Me, too...."
    rin "*Heavily breathes*....Ahhh....Don't cum inside, please."
    mc "...Sure..."
    scene black with dissolve
    hide ep3_rincow3 with dissolve
    $ renpy.pause()
    scene ep3_359_a7_a35 with dissolve
    rin "Mmmmm...."
    rin "....I'm cumming!!!"
    mc "Arr...!"
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ep3_359_a7_a36 at eyesblink("Ch.1/Ep.3/Scenes/ep3_359_a7_a36.jpg", "Ch.1/Ep.3/Scenes/ep3_359_a7_a36_blink.jpg", 1) with dissolve
    rin "*Pants*.....Hehe....."
    rin "*Pants*...That was...so...good...."
    mc "Yeah...I agree with you."
    rin "*Pants*...O...Oh!...Let's not forget to do this, too..."
    mc "...Do wh-"
    scene ep3_359_a7_a37 with dissolve
    rin "*Kisses*....Mmmmm..."
    u "Okay, I know it now...."
    scene ep3_359_a7_a36 at eyesblink("Ch.1/Ep.3/Scenes/ep3_359_a7_a36.jpg", "Ch.1/Ep.3/Scenes/ep3_359_a7_a36_blink.jpg", 1) with dissolve
    rin "*Giggles*....Hehe... What a special lovely morning..."
    mc "Yeah...."
    rin "Alright, we've had enough fun. Let's get up, and go have breakfast!"
    mc "Sure."
    $ renpy.end_replay()
    $ ep3morningsex = True
    $ rin_relationship += 2
    $ rin_ch1_ep3 += 2
    scene black with dissolve
    $ renpy.pause()
    hide screen smartphone
    $ episode = 3
    call screen ending
label ep3_p3_refuserin:
    scene black with dissolve
    $ renpy.pause()
    scene ep3_359_d with dissolve
    u "You spend time learning about the Xecon Gear code..."
    jump ep3_p3_ending1
label ep3_p3_ending1:
    scene black with dissolve
    s "*About two hours later*......."
    scene ep3_359_d3 with dissolve
    $ ep3_alicemessage3 = True
    $ alice_messages_show = True
    $ alice_newmessage = True
    $ newmessage = True
    $ phone_alert = True
    u "Okay...It's already late."
    u "I should go to bed...."
    scene black with dissolve
    $ renpy.pause()
    hide screen smartphone
    $ episode = 3
    call screen ending
label ep3_p3_spendnightalone:
    scene black with dissolve
    $ renpy.pause()
    if krystal_reply4_choice == 1:
        scene ep3_359_d1 with dissolve
        u "Okay. Let's continue going back to my room..."
        scene black with dissolve
        $ renpy.pause()
        scene ep3_359_d2 with dissolve
        u "It's still too early to sleep, I better turn on the computer."
        u "Let's study the Xecon Gear code more."
    elif krystal_reply4_choice == 2:
        scene ep3_356_d with dissolve
        u "You continue spending time learning about the code......"
    jump ep3_p3_ending1
label ep3zekeroom:
    scene black
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Door knocks*........."
    stop sound
    scene ep3_327_1 with fade
    mika "Hm? Who is it?"
    mc "It's me, [mc]."
    mc "Can I come in?"
    mika "Oh, sure!"
    $ ep3zekeroom = True
    jump house_ep3
label ep3yuiroom:
    scene black
    scene ep3_331 with fade
    yui "(Ummm... What should I wear today?)"
    yui "(I want to wear something casual.)"
    yui "(Let's see what I've got here....)"
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Door knocks*........."
    stop sound
    scene ep3_332 with dissolve
    yui "Hm? Who is it?"
    mc "It's me, [mc]."
    yui "What do you want?"
    mc "Can I come in?"
    yui "...Wait a sec!"
    scene black with dissolve
    yui "Alright, you may come in now!"
    $ ep3yuiroom = True
    jump house_ep3
label ep3rinroom:
    scene black
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Door knocks*........."
    stop sound
    mc "Are you in there, [rin]?"
    s "............."
    u "Hm? Seems like there is no one in the room."
    $ ep3rinroom = True
    jump house_ep3
label ep3_zekeroom_talk:
    scene black
    scene ep3_328 at eyesblink("Ch.1/Ep.3/Scenes/ep3_328.jpg", "Ch.1/Ep.3/Scenes/ep3_328_blink.jpg", 1) with dissolve
    mika "Good morning, [mc]."
    mc "Good morning."
    mika "What are you doing here?"
    menu:
        "[smgr2]Where's [zeke]?":
            mc "I come here looking for [zeke], but it seems like he is not here."
            mc "Do you know where he is?"
            if ep3zekesleep == False:
                mika "Oh...[zeke]."
                scene ep3_329 with dissolve
                mika "He's right there."
                mc "Hm? Where?"
                mika "Really? Don't you see him?"
                scene ep3_330 with dissolve
                mika "He is sleeping right there."
                mc "Oh... I see him now."
                mika "Why are you looking for him though?"
                mika "Do you want to talk with him?"
                mika "Should I wake him up?"
                mc "No, thanks. It's nothing important."
                mc "We should just let him sleep."
                mika "Are you sure?"
                mc "Yes, I am."
                mc "Alright, I'm leaving now."
                mika "Okay. See you later."
                mc "See you."
                scene black with dissolve
                $ ep3zekesleep = True
                jump house_ep3
            else:
                mika "Hm? Didn't you just ask about that?"
                mc "Oh yeah, I did..."
                scene black with dissolve
                jump house_ep3
        "Leave":
            mc "Nothing. I'm leaving now."
            mika "Okay. See you later then."
            mc "See you."
            scene black with dissolve
            jump house_ep3
label ep3_yuiroom_talk:
    scene black
    scene ep3_333 at eyesblink("Ch.1/Ep.3/Scenes/ep3_333.jpg", "Ch.1/Ep.3/Scenes/ep3_333_blink.jpg", 1) with dissolve
    mc "Good morning, [yui]."
    yui "...Morning."
    mc "....You look good in that dress."
    yui "Thanks."
    yui "Anyway, what are you doing here?"
    jump ep3_yuiroom_talkchoice
label ep3_yuiroom_talkchoice:
    menu:
        "Talk":
            menu:
                "Favorites":
                    mc "So, can you tell me more about your favorite things to do now?"
                    if yui_relationship >= 10:
                        if yui_like2 == "???" and yui_like3 == "???":
                            scene ep3_334 at eyesblink("Ch.1/Ep.3/Scenes/ep3_334.jpg", "Ch.1/Ep.3/Scenes/ep3_334_blink.jpg", 1) with dissolve
                            yui "Sure."
                            yui "Well, this one I guess it's pretty obvious. I like making games."
                            $ yui_like2 = "Making games"
                            mc "Yeah, I can tell that."
                            yui "There is one more thing left, right?"
                            mc "Yes, there is."
                            yui "Umm.... I like flowers, especially cherry blossoms."
                            $ yui_like3 = "Cherry blossom"
                            mc "Really? I didn't see that one coming."
                            yui "Why? Am I not allowed to like flowers?"
                            mc "Yes, you are. It's just...."
                            yui "Just what?"
                            mc "Nothing...."
                            scene ep3_333 at eyesblink("Ch.1/Ep.3/Scenes/ep3_333.jpg", "Ch.1/Ep.3/Scenes/ep3_333_blink.jpg", 1) with dissolve
                            $ ep3yuifavask = True
                            jump ep3_yuiroom_talkchoice
                        else:
                            yui "Hm? Didn't we just talk about that?"
                            mc "Yeah, we did. Sorry, I forgot."
                            jump ep3_yuiroom_talkchoice
                    else:
                        scene ep3_335 at eyesblink("Ch.1/Ep.3/Scenes/ep3_335.jpg", "Ch.1/Ep.3/Scenes/ep3_335_blink.jpg", 1) with dissolve
                        yui "....Hm? I don't think we're close enough to."
                        yui "So, I'm sorry, but I won't tell you."
                        mc "....Okay."
                        scene ep3_333 at eyesblink("Ch.1/Ep.3/Scenes/ep3_333.jpg", "Ch.1/Ep.3/Scenes/ep3_333_blink.jpg", 1) with dissolve
                        $ ep3yuifavask = True
                        jump ep3_yuiroom_talkchoice
                "Dislikes":
                    mc "So, can you tell me more about things you don't like now?"
                    if yui_relationship >= 10:
                        if yui_hate2 == "???" and yui_hate3 == "???":
                            yui "Sure."
                            scene ep3_335 at eyesblink("Ch.1/Ep.3/Scenes/ep3_335.jpg", "Ch.1/Ep.3/Scenes/ep3_335_blink.jpg", 1) with dissolve
                            yui "Um....Things I don't like...."
                            yui "Well, I told you that I hate being insulted."
                            yui "And people who always look for an opportunity to insult other people are jerks."
                            mc "I couldn't agree more."
                            yui "So, I hate jerks."
                            $ yui_hate2 = "Jerks"
                            mc "What about the last one?"
                            yui "Umm... I don't like spiders."
                            yui "I always freak out every time I see them."
                            $ yui_hate3 = "Spiders"
                            scene ep3_333 at eyesblink("Ch.1/Ep.3/Scenes/ep3_333.jpg", "Ch.1/Ep.3/Scenes/ep3_333_blink.jpg", 1) with dissolve
                            $ ep3yuihateask = True
                            jump ep3_yuiroom_talkchoice
                        else:
                            yui "Hm? Didn't we just talk about that?"
                            mc "Yeah, we did. Sorry, I forgot."
                            jump ep3_yuiroom_talkchoice

                    else:
                        scene ep3_335 at eyesblink("Ch.1/Ep.3/Scenes/ep3_335.jpg", "Ch.1/Ep.3/Scenes/ep3_335_blink.jpg", 1) with dissolve
                        yui "....Hm? I don't think we're close enough to."
                        yui "So, I'm sorry, but I won't tell you."
                        mc "....Okay."
                        scene ep3_333 at eyesblink("Ch.1/Ep.3/Scenes/ep3_333.jpg", "Ch.1/Ep.3/Scenes/ep3_333_blink.jpg", 1) with dissolve
                        $ ep3yuihateask = True
                        jump ep3_yuiroom_talkchoice
                "Where are you going?":
                    mc "I see that you're dressing too nice for staying at home."
                    mc "Are you going outside today?"
                    if yui_relationship >= 7:
                        if ep3yuigoout == False:
                            yui "Well, you're right."
                            yui "I'm going to see my family. So, I have to dress nicely."
                            mc "Your family? I've never heard you talk about them before."
                            yui "Well, we weren't close enough to talk about personal things though."
                            mc "Yeah, that makes sense..."
                            mc "I assume that they live in a different city, right?"
                            mc "Otherwise, you wouldn't have had to move here."
                            scene ep3_334 at eyesblink("Ch.1/Ep.3/Scenes/ep3_334.jpg", "Ch.1/Ep.3/Scenes/ep3_334_blink.jpg", 1) with dissolve
                            yui "Yeah, they live pretty far from here."
                            yui "It will take me 5 hours to go there by bus."
                            mc "I bet you'll come back here very late at night then."
                            yui "Hm? No, I won't come back here today."
                            yui "I'm going to stay with my family until tomorrow."
                            mc "I see...."
                            scene ep3_333 at eyesblink("Ch.1/Ep.3/Scenes/ep3_333.jpg", "Ch.1/Ep.3/Scenes/ep3_333_blink.jpg", 1) with dissolve
                            $ ep3yuigoout = True
                            jump ep3_yuiroom_talkchoice
                        else:
                            yui "Hm? Didn't we just talk about that?"
                            mc "Yeah, we did. Sorry, I forgot."
                            jump ep3_yuiroom_talkchoice
                    else:
                        yui "Yes, I am."
                        mc "I see...."
                        scene black with dissolve
                        $ renpy.pause()
                        jump house_ep3
                "Back":
                    jump ep3_yuiroom_talkchoice
        "Leave":
            mc "Nothing. I just come to say hi."
            yui "Okay. Then, you may leave now."
            mc "Sure."
            scene black with dissolve
            jump house_ep3
label ep3_mcroom_pic:
    if _in_replay:
        scene ep3_mcroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep3_mcroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep3mcroom_pic = True
    $ ep3hiddenimages_count += 1
    jump house_ep3
label ep3_yuiroom_pic:
    if _in_replay:
        scene ep3_yuiroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep3_yuiroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep3yuiroom_pic = True
    $ ep3hiddenimages_count += 1
    jump house_ep3
label ep3_rinroom_pic:
    if _in_replay:
        scene ep3_rinroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep3_rinroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep3rinroom_pic = True
    $ ep3hiddenimages_count += 1
    jump house_ep3
label ep3_livroom_pic1:
    if _in_replay:
        scene ep3_livingroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    if ep3livroom_pic2 == False:
        scene ep3_livingroom_photo1
    else:
        scene ep3_livingroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep3livroom_pic1 = True
    $ ep3hiddenimages_count += 1
    jump house_ep3
label ep3_livroom_pic2:
    if _in_replay:
        scene ep3_livingroompic2 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    if ep3livroom_pic1 == False:
        scene ep3_livingroom_photo2
    else:
        scene ep3_livingroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep3livroom_pic2 = True
    $ ep3hiddenimages_count += 1
    jump house_ep3
label ep3_hallway_pic:
    if _in_replay:
        scene ep3_hallwaypic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep3_hallway
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep3hallway_pic = True
    $ ep3hiddenimages_count += 1
    jump house_ep3
label ep3_garage_pic:
    if _in_replay:
        scene ep3_garagepic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep3_garage
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep3garage_pic = True
    $ ep3hiddenimages_count += 1
    jump house_ep3
label ep3_mcroom_door:
    if ep3mcroom_pic == False:
        scene ep3_mcroom_photo
    else:
        scene ep3_mcroom
    s "That is my room's door."
    jump house_ep3
label ep3_rinroom_bed:
    if ep3rinroom_pic == False:
        scene ep3_rinroom_photo
    else:
        scene ep3_rinroom
    s "That is [rin]'s bed."
    jump house_ep3
label ep3_hallway_bookcase:
    if ep3hallway_pic == False:
        scene ep3_hallway_photo
    else:
        scene ep3_hallway
    s "It's just a book case."
    jump house_ep3
label ep3_hallway_ftable:
    if ep3hallway_pic == False:
        scene ep3_hallway_photo
    else:
        scene ep3_hallway
    s "It's a football table."
    jump house_ep3
label ep3_garage_car:
    if ep3garage_pic == False:
        scene ep3_garage_photo
    else:
        scene ep3_garage
    s "It's [zeke]'s car."
    jump house_ep3
