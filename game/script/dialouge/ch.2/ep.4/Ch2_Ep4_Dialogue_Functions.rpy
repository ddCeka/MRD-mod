label ch2ep4start:
    scene black with dissolve
    $ renpy.pause(3, hard=True)
    scene ep4
    $ renpy.pause(3, hard=True)
    scene black with dissolve
    $ renpy.pause()
    show screen smartphone
    scene ch2ep4_1 with fade
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    mc "Tom...?"
    tom "Yeah! You remember me, right?!"
    tom "Well... this is so unbelievable."
    tom "How long has it been? 14? 15 Years? Wait, that doesn't matter."
    tom "I'm so glad to see you, bro."
    mc "................."
    u "(I feel kind of familiar with his name and his face, too, but I don't recall where I heard that from...)"
    scene ch2ep4_2 with dissolve
    tom "Wait... Don't tell me..."
    mc "................."
    tom "You don't remember me, right....?"
    mc "I'm sorry...."
    tom "*Sighs* It's okay. I don't blame you. It's been really such a long time."
    tom "We met each other when we were very young..."
    scene ch2ep4_3 with flash
    $ renpy.pause(1, hard=True)
    scene ch2ep4_4 with dissolve
    mc "Wait. I think I remember you now..."
    mc "You were the kid that got kicked out because you failed the exam..."
    tom "Bro! Out of every moments we had together, you remembered me because of that?!"
    mc ".... Yeah."
    tom "*Sighs* Whatever... At least you remember me now."
    scene ch2ep4_5 with dissolve
    tom "Unbelievable... You haven't changed a bit after all these years."
    mc "To talk about that, I think you also haven't changed a bit as well..."
    tom "Really? Then, how come you couldn't remember me?"
    mc "....................."
    tom "*Laughs* Just kidding!"
    tom "Hey! Why don't we go find a good place to sit and talk?"
    tom "There are lots of things I'd like to talk with you."
    scene ch2ep4_6 with dissolve
    u "......................."
    u "I didn't expect him to become a cop..."
    u "What should I do?"
    menu:
        "Go with [tom] [smrec]":
            $ ch2ep4gowithtom = 1
            u "Well... Hanging out with him for a bit wouldn't be such a bad choice."
            u "I'm sure that I can keep my secrets."
            scene ch2ep4_7_a1 with dissolve
            mc "Sure. Let's go get some coffee then."
            tom "Coffee sounds great..."
            mc "Okay, let's go then."
            scene ch2ep4_7_a2 with dissolve
            tom "Actually, I just moved here not so long ago."
            tom "Therefore, I don't know much about places around here. What cafe do you recommend?"
            mc "Well, follow me then. I will take you there."
            tom "Sure!"
            scene black with dissolve
            $ renpy.pause()
            scene ch2ep4_8 with fade
            mc "This cafe is great. I often come here at lunch."
            tom "Yeah? Noted that!"
            mc "By the way..."
            mc "What happened to you after you were expelled?"
            scene ch2ep4_9 with dissolve
            tom "Nothing much. I got sent back to the church I came from."
            tom "Then, I got lucky. I got adopted by a married couple."
            tom "They're now my parents."
            mc "That's great for you..."
            scene ch2ep4_10 with dissolve
            mc "And how come you became a police?"
            mc "I thought you wanted to become a professional footballer."
            mc "As I recall, you were very determinded back then..."
            scene ch2ep4_11 with dissolve
            tom "................"
            mc ".... Did I just ask something I shouldn't have?"
            mc "I'm so sorry."
            scene ch2ep4_12 with dissolve
            tom "*Sighs* No, you didn't do anything wrong."
            tom "It was my fault. I just suddenly got too sensitive."
            mc "You don't have to tell me if you don't want to."
            tom "No, it's alright. I will tell you."
            scene ch2ep4_13 with dissolve
            tom "Actually, it wasn't anything dramatically."
            tom "It was just that I wasn't good enough."
            tom "I thought I was special, but it turned out that there were plenty of kids who had more talent and potential than me."
            mc "I'm sorry to hear that."
            tom "*Laughs* Don't be! I'm happy with my life right now."
            tom "My parents always wanted me to become a cop, and I did it. I'm so happy that I made them proud."
            scene ch2ep4_14 with dissolve
            tom "By the way...."
            tom "Let me ask you something, too."
            mc "Hm? What do you want to ask me about?"
            tom "Are you still with [victor]?"
            scene ch2ep4_15 with dissolve
            mc "....................."
            u "When we were kids, we weren't allowed to know [victor]'s name until we graduated."
            u "But now, [tom] knows his name...."
            u "Actually, it's not that hard to find out [victor]'s name after we grew up."
            u "However, he is a cop.... I should be aware not to let my guard down."
            u "The fact that he asked me that question proves that he doesn't have any information about me."
            u "Or he might have, but he's just trying to test me...?"
            scene ch2ep4_16 with dissolve
            u "I think the first hypothesis sounds more possible."
            u "I mean... even a police with higher position than him doesn't have a clue about my information."
            mc "No, I'm not with him now. I got expelled a year after you."
            tom "For real, bro?! How come? You were like the best out of us!"
            mc "Well, it turned out that there were plenty of kids who were better than me as well."
            tom "I see. Actually, that's great for you, bro."
            tom "I'll tell you something."
            mc "What is it?"
            tom "Before I tell you, you have to promise me that you won't tell anyone."
            mc "... I promise."
            scene ch2ep4_17 with dissolve
            tom "Well, the police just formed the special unit to arrest [victor]."
            mc ".... Really? For what crime?"
            tom "You will surely be surprised if I tell you. He has done so many terrible things."
            mc "... Are you sure?"
            tom "Yeah! The guy who formed the unit has the evidence."
            tom "So, I'm very glad to know that you have nothing to do with [victor] anymore."
            mc "...................."
            scene black with dissolve
            $ renpy.pause()
            s "*Half an hour later*..........."
            scene ch2ep4_18 with dissolve
            tom "Thanks for the coffee, bro."
            tom "I have to leave now."
            mc "Me, too."
            scene ch2ep4_19 with dissolve
            tom "Oh! Give me your phone number so that we can keep in touch."
            tom "I still have plenty of things to talk to you."
            mc "..................."
            mc "Sure."
            scene black with dissolve
            scene ch2ep4_20 with dissolve
            tom "Alright, I'm leaving now."
            tom "See you later, bro."
            mc "Yeah, see you later."
            scene ch2ep4_21 with dissolve
            mc ".................."
            u "Well, I didn't expect to get such important information today..."
            u "He is surely a good person, but he trusts people too easily..."
            u "What should I do with that information...?"
            scene ch2ep4_22 with dissolve
            u "... Let's just do nothing."
            u "I won't inform that to [victor] as this isn't the first time some police try to arrest him."
            u "I'm sure he can deal with it himself."
            u "Moreover, he probably knows this already since he has tons of eyes in the police department."
            u "Let's just go back to the company."
            scene black with dissolve
            $ renpy.pause()
            jump ch2ep4afterlunch
        "Refuse":
            $ ch2ep4gowithtom = 2
            u "I shouldn't spend any more time with him."
            scene ch2ep4_7_d1 with dissolve
            mc "Sorry. I can't go with you."
            mc "I have to get back to work real soon."
            tom "Oh.... Is that so?"
            mc "Yeah, but you can give me your phone number if you don't mind."
            mc "So, we can still keep in touch later."
            scene ch2ep4_7_d2 with dissolve
            mc "Nice to meet you, [tom]."
            mc "Good bye."
            tom "Okay, see you again later..."
            mc "I hope so..."
            u "Alright, let's go get some coffee before going back to the company."
            scene black with dissolve
            $ renpy.pause()
            jump ch2ep4afterlunch
label ch2ep4afterlunch:
    if ch2ep3helpeira == 1:
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep4_23 with fade
        u "... Hm?"
        u "Isn't that [sally] and [eira]...?"
        scene ch2ep4_24 with dissolve
        sally "Oh?! Hi, [mc]!"
        eira "!!!!"
        sally "Just got back from having lunch, huh?"
        mc "Yeah. Good afternoon, [sally]."
        scene ch2ep4_25 with dissolve
        mc "... Good afternoon, [eira]."
        eira "................."
        eira "... Hi."
        mc "................."
        scene ch2ep4_26 with dissolve
        sally "*Giggles* What's wrong, [eira]?"
        sally "Why are you acting shy like that?"
        sally "I thought you already became much more comfortable with [mc]."
        eira "Yes, I did. It's just...."
        s "*Elevator sounds*......."
        scene ch2ep4_27 with dissolve
        sally "Oh?! The elevator has come."
        sally "Let's go, guys."
        eira "O... Okay."
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep4_28 with dissolve
        sally "Good bye, [mc]!"
        eira "Good... bye..."
        sally "Have a great afternoon."
        mc "Yeah, both of you, too."
    scene ch2ep4_29 with dissolve
    u "Alright...."
    u "Let's get back to work."
    mc "................."
    scene ch2ep4_30 with dissolve
    u "Hang on a sec...."
    u "It's been some time since [maya] asked me to go get the DNA test."
    u "I guess today is the day...."
    u "I'm going to go find somewhere more quiet and then call her."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_31 with dissolve
    mc "...................."
    mc "...................."
    scene ch2ep4_32 with dissolve
    u "She didn't answer..."
    u "Perhaps she is busy right now, I guess I will just call her l-"
    s "*Phone rings*............"
    u "Hm...? It's [angela]..."
    scene ch2ep4_33 with dissolve
    mc "................"
    mc ".... Yes?"
    scene ch2ep4_34 with dissolve
    angela "Sorry for earlier, the president didn't mean to ignore your call."
    angela "She's in the middle of the conference now."
    angela "You can talk to me now. I'll report your message to her after the conference."
    scene ch2ep4_35 with dissolve
    mc "Okay..."
    mc "Please tell her that I'd like to get the DNA test this evening if it's possible."
    mc "I mean... if her schedule is free in the evening."
    scene ch2ep4_36 with dissolve
    angela "Sure thing. I've looked at her schedule already."
    angela "She is free this evening. I'll inform her about your request."
    angela "What time do you want us to go and pick you up?"
    angela "A quarter past five p.m.? In front of your company? Sure, noted that."
    angela "See you in the evening. Bye."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_37 with dissolve
    u "Alright...."
    u "Let's get back to work for real now...."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    s "*About four hours later*.........."
    scene ch2ep4_38 with fade
    mc "....................."
    u "It's already fifteen past five. I wonder where they are..."
    u "Hm...?"
    scene ch2ep4_39 with dissolve
    maya "I'm so sorry, my dear."
    maya "The traffic was a little bit bad on the way here."
    maya "Get in the car, please."
    mc "..............."
    scene ch2ep4_40 with dissolve
    mc "Good evening, [maya]..."
    maya "*Smiles* Good evening. How's your day?"
    mc "Great, I suppose. What about you?"
    maya "Pretty rough day. I was busy all day until an hour ago."
    mc "... Do you want to go home and take a rest?"
    mc "We can do the DNA test another day."
    scene ch2ep4_41 with dissolve
    maya "No. No. Don't worry about me."
    maya "I feel much better now after I saw you."
    mc "Are you sure?"
    maya "Of course!"
    scene ch2ep4_42 with dissolve
    maya "[angela]."
    angela "Yes?"
    maya "You've already made an appointment, right?"
    angela "Yes. The appointment time is at half past six."
    maya "Alright then, we should get going now."
    angela "Understood."
    scene black with dissolve
    $ renpy.pause()
    s "*About an hour later*............."
    scene ch2ep4_43 with fade
    angela "Please, take a seat and wait here."
    angela "I'm going to get everything done, and come to get you to the examination room when it's time."
    maya "Thank you for your hard work, [angela]."
    angela "My pleasure."
    scene black with dissolve
    scene ch2ep4_44 with dissolve
    maya "[skylar] was so sad that she couldn't come with us today."
    mc "Hm? Why couldn't she?"
    maya "She has an evening class."
    mc "I see..."
    maya "By the way, are you excited?"
    scene ch2ep4_45 with dissolve
    mc "A little bit..."
    maya "Just a little bit? You've grown to be such a calm person."
    maya "*Giggles* And look at me..."
    maya "I'm an old woman who has lots of life experiences, yet I'm very excited right now!"
    scene ch2ep4_46 with dissolve
    mc "Well, I can't blame you for that."
    mc "By the way..."
    mc "Since you mentioned [skylar], can I ask you something?"
    maya "Hm? What do you want to know about her?"
    scene ch2ep4_47 with dissolve
    mc "Actually... I've always been curious, but I don't know if I should ask you about that."
    maya "Don't be hesitate to. I will answer your question no matter what."
    mc "Okay then..."
    mc "You said that [skylar] is my younger sister, but I've never seen her dad..."
    scene ch2ep4_48 with dissolve
    maya ".................."
    mc ".................."
    mc "... I'm sorry. I shouldn't have asked you that."
    scene ch2ep4_49 with dissolve
    maya "Don't be. You have your rights to wonder about that."
    mc "Are you sure? You don't have to answer if you don't want to..."
    maya "It's okay. I will answer your question."
    scene ch2ep4_50 with dissolve
    maya "Actually, I have no idea who [skylar]'s father is as well."
    mc "Hm...? What do you mean by that. I don't quite understand."
    maya "I mean... [skylar] is your younger sister, but you guys are actually not related by blood."
    mc "What?"
    maya "She was also an orphan."
    maya "After two years of attempting to search for you, I went back to the church."
    scene ch2ep4_51 with dissolve
    maya "That's when I met her. She was a smart and warm-hearted kid."
    maya "I decided to adopt her after some time passed to fill the hole in my heart."
    maya "But, don't get me wrong. I didn't see her as a tool to make me feel better."
    maya "I loved her as if she was my own daughter since then till now."
    maya "You and [skylar] will always be my son and daughter for the rest of my life...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_52 with dissolve
    angela "Mrs. President."
    angela "I come to get you and [mc] to the room. It's about time now."
    maya "Oh, is it? I didn't realise that."
    maya "Let's go, [mc]."
    mc "Sure...."
    scene black with dissolve
    $ renpy.pause()
    s "*About an hour later*............."
    scene ch2ep4_53 with dissolve
    doctor "Thank you for your cooperation today."
    doctor "The result will be sent to you in 7 days."
    maya "Thank you so much, doctor."
    doctor "My pleasure."
    scene ch2ep4_54 with dissolve
    maya "Okay, that's it. Now, we just have to wait."
    mc "Yeah..."
    maya "Have you eaten anything yet?"
    maya "Do you want me to take you to dinner?"
    mc "Thank you, but..."
    scene ch2ep4_55 with dissolve
    mc "Actually, I have something to do tonight."
    mc "So, I'd like to go home if you don't mind me."
    maya "Sure thing. If that's what you want."
    maya "Come with me. I will send you home."
    mc "................"
    mc "Thank you."
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    scene ch2ep4_56 with fade
    maya "Thank you for coming with me today, [mc]."
    maya "It meant a lot for me."
    mc "Me, too..."
    maya "Okay then, I have to leave now."
    maya "If there is anything you need, just call me, okay?"
    mc "Thank you."
    maya "Good night, [mc]."
    mc "You, too. Get home safely."
    scene black with dissolve
    scene ch2ep4_57 with dissolve
    u "It's been a really long day..."
    u "I'm feeling a little bit hungry now."
    u "Let's get inside the house and find something to eat."
    scene ch2ep4_58 with dissolve
    mika "Alright, I'm gonna go to the room now."
    mika "You're going to go grab a beer, right?"
    zeke "Yeah, I'll follow you after that."
    mika "Okay."
    scene ch2ep4_59 with dissolve
    mika "Good evening, [mc]."
    mc "Good evening, [mika]."
    mika "See you tomorrow."
    mc "See you."
    scene ch2ep4_60 with dissolve
    zeke "What's up, bro."
    mc "Hey."
    zeke "Where are you going?"
    mc "To the kitchen. I'm going to find something to eat."
    scene ch2ep4_61 with dissolve
    zeke "Alright then, let's go together."
    zeke "I need to go to the kitchen, too."
    mc "Sure."
    if ch2ep3helpeira == 1:
        jump ch2ep4saveeira
    else:
        jump ch2ep4nextday
label ch2ep4saveeira:
    stop music fadeout 3.0
    scene ch2ep4_62 with dissolve
    s "*Phone rings*..............."
    zeke "Hm? It's your phone, bro."
    zeke "Aren't you going to take it?"
    mc "Wait a sec..."
    play music "sfx/ep2_7.mp3" fadein 3.0
    $ bgm = "AERØHEAD - The Reckoning"
    scene ch2ep4_63 with dissolve
    zeke "Who's it?"
    mc "[eira]."
    zeke "Damn... I never knew you guys were so close that she could call you at the time like this."
    zeke "Pick it up already, bro. Don't let her wait too long."
    scene ch2ep4_64 with dissolve
    mc "Hello?"
    mc "Calm down. I don't understand what you're talking about."
    mc "Take a deep breathe and say it again."
    mc "...................."
    scene ch2ep4_65 with dissolve
    mc "Where are you right now?"
    mc "Look around yourself and try to find a pl-"
    mc "Hello...? [eira]....?"
    scene ch2ep4_66 with dissolve
    mc "Can I borrow your car, [zeke]?"
    zeke "What happened, bro?"
    mc "Hurry up, and give it to me. I don't have much time left."
    zeke "No! I'm not going to give you the key until you tell me what's going on."
    mc "*Sighs*.............."
    scene ch2ep4_67 with dissolve
    mc "I think [eira] got kidnapped."
    zeke "What?! For real, bro?!"
    mc "..................."
    mc "... Do I look like a guy who will joke about something like this?"
    scene ch2ep4_68 with dissolve
    zeke "Fuck!"
    zeke "What are you waiting for, bro?! Let's go!"
    mc "Just give me the key. You don't have to go with me."
    zeke "No, there is no way I'm going to let you go alone. I will go with you!"
    mc "*Sighs* Fine...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_69 with dissolve
    zeke "Where is she right now?"
    mc "I don't know. She was at the park nearby her house when I talked with her on the phone."
    mc "I think we should go there to find some clues first."
    zeke "Understood."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_70 with fade
    zeke "[eira]! [eira]!"
    zeke "Where are you!?"
    mc "I'll go that way...."
    scene black with dissolve
    s "*A few minutes later*............."
    scene ch2ep4_71 with dissolve
    mc "Have you found any clues, [zeke]?"
    zeke "No. I haven't found nothing at all."
    zeke "What about you?"
    mc "Me either...."
    scene ch2ep4_72 with dissolve
    mc ".... Hm?"
    zeke "What's wrong?"
    scene ch2ep4_73 with dissolve
    mc "I think I found something."
    zeke "Hm? What's it?"
    mc "I'm not sure. It's pretty dark here. I can't see it quite clearly."
    mc "I'll go pick it up...."
    scene ch2ep4_74 with dissolve
    mc "It's a phone..."
    zeke "Whose phone is it? [eira], right?"
    mc "Yeah. I think it's her phone."
    scene ch2ep4_75 with dissolve
    zeke "But, what can we do with that phone, bro?"
    zeke "We don't even know where she is right now."
    mc "Hang on a sec...."
    scene ch2ep4_76 with dissolve
    zeke "Who are you calling?"
    mc "My.... friend."
    zeke "Your friend?"
    mc "He's a cop. I'm going to ask for his help."
    zeke "Brilliant!"
    zeke "Fuck me... Why didn't I think about calling a cop earlier...?"
    scene ch2ep4_77 with dissolve
    tom "What's up, [mc]?"
    tom "To be honest I didn't expect you to call me first."
    tom "Hm? You need my help? What's going on?"
    scene ch2ep4_78 with dissolve
    mc "My friend just got kidnapped."
    scene ch2ep4_79 with dissolve
    tom "What?! Are you sure?!"
    scene ch2ep4_78 with dissolve
    mc "Yes, I am."
    mc "There is no CCTV at the crime scene."
    mc "But, I'm sure there are some CCTVs around here."
    mc "I need you to check them."
    scene ch2ep4_79 with dissolve
    tom "Sure thing. Where is the crime scene located at?"
    tom ".................."
    tom "Got it. I'll check the CCTVs around there and call you back real quick."
    scene ch2ep4_80 with dissolve
    zeke "So, what did you friend say?"
    mc "He will check the CCTVs, then call me back."
    zeke "And what are we going to do now?"
    mc "Wait."
    zeke "Bro. We don't know what they are going to do with [eira]."
    scene ch2ep4_81 with dissolve
    zeke "Is it okay for us to just wait here? Is there nothing we can do at all?"
    mc "Unfortunately, yes. We don't know where they're talking her to."
    mc "So, we can't just go to places randomly."
    mc "In the worst case, we might even end up going to the opposite way they're taking her to."
    mc "So, the best thing we can do now, is be patient and wait."
    zeke "*Sighs* Yeah,... you're right."
    scene black with dissolve
    $ renpy.pause()
    s "*Half an hour later*............"
    scene ch2ep4_82 with dissolve
    zeke "*Sighs* This is so irritating...."
    zeke "I have never once felt useless as I am today."
    zeke "It's been half an hour already. Why is your friend taking so long...?"
    mc "...................."
    scene ch2ep4_83 with dissolve
    s "*Phone rings*............"
    zeke "Is it from your friend?!"
    mc "Yeah."
    zeke "Then, what are you waiting for? Take it!"
    scene ch2ep4_84 with dissolve
    mc "Hello...."
    scene ch2ep4_85 with dissolve
    tom "I've checked every CCTV around there."
    tom "There was a van going in the park at 8.13 p.m. and coming out of the park at 8.35 p.m."
    tom "Your friend got kidnapped around that time, right?"
    scene ch2ep4_86 with dissolve
    mc "Yeah, she called me at 8.27 p.m. before the call was cut."
    mc "She must've been in that van for sure."
    mc "Do you know which direction it went?"
    scene ch2ep4_87 with dissolve
    tom "Yeah, I tracked down that van and saw it went past road 314."
    tom "But, unfortunately, it disappeared before the next CCTV on that road could capture the footage."
    tom "I've already informed my colleagues."
    tom "We're trying our best to figure out the destination."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_87_1 with dissolve
    zeke "So, what are we going to do now...?"
    mc "We're going to try searching for the van according to the information we've just got."
    zeke "Okay... But, where we should start?"
    mc "Actually.... "
    scene ch2ep4_88 with dissolve
    u "There is an abandoned warehouse located just only about 10 kilometers at the south of road 314..."
    if nominatekrystal == 1:
        u "It's the warehouse that I released the reporter that wrote fake news about [krystal]."
    u "I'm prety sure that's the place..."
    zeke "Bro, where are you going?"
    mc "I think I know where they're going to take [eira] to."
    zeke "For real?! How?!"
    mc "Follow me...."
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_89 with fade
    mc "There it is....."
    mc "That's the van we've been looking for."
    zeke "Damn, bro! You're right! How did you know that they'd be here?"
    mc "Shh... Quiet."
    zeke "... Sorry. My bad."
    scene ch2ep4_90 with dissolve
    mc "There they are...."
    mc "That's [eira]..."
    zeke "Fuck... One... Two... Three... Four... Five... "
    scene ch2ep4_91 with dissolve
    zeke "That's quite a lot... There are only two of us here."
    zeke "What's your plan, bro?"
    mc "................."
    scene ch2ep4_92 with dissolve
    mc "I'm going in..."
    zeke "What?! Bro? Are you insane?"
    zeke "I think we better wait for the police."
    mc "No, I'm going to wait for them."
    scene ch2ep4_93 with dissolve
    mc "We don't know what they're going to do with [eira] while we wait here."
    mc "The longer we wait, the more pain she has to take..."
    zeke "You're right, but..."
    zeke "Ah... Fuck it!"
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_94 with fade
    play music "sfx/ep2_8.mp3" fadein 3.0
    $ bgm = "Lahar - Genesis"
    roxy "Hey! Wake up!"
    roxy "Who gave you a permission to pass out?"
    eira "Ugh..."
    scene ch2ep4_95 with dissolve
    eira "P... Please... Stop....."
    eira "W... Why... are you... doing this... to me...?"
    eira "W... What have I... ever done... to you...?"
    roxy "*Sighs* Why do you always have to make me a bad person...?"
    roxy "Jeez... This is so boring."
    scene ch2ep4_96 with dissolve
    roxy "Hey, all of you."
    roxy "Come here."
    scene ch2ep4_97 with dissolve
    roxy "You did your job well."
    roxy "Here is the payment we agreed on. Take it."
    trevor "Thanks."
    scene ch2ep4_98 with dissolve
    roxy "Alright, I'm going to leave now."
    trevor "Hm? Then, what about that girl?"
    trevor "What should we do with her?"
    roxy "Up to you. You can do whatever you want."
    scene ch2ep4_99 with dissolve
    roxy "You guys understand the meaning of {b}'whatever you want'{/b}, right?"
    dax "Of course. Actually, we've been waiting to hear that."
    roxy "Great.... But, don't forget to clean everything up before you leave."
    roxy "And make it sure that this bitch won't ever tell anyone about today, okay?"
    scene ch2ep4_100 with dissolve
    wilson "Please forgive me for interrupting you, miss."
    wilson "But, we've got guests here."
    roxy "Hm? What are you talking about...?"
    scene ch2ep4_101 with dissolve
    roxy "Oh... I see now."
    roxy "They probably saw you all, but still get in here."
    roxy "They think they're some kind of whiteknights or what? Idiots...."
    roxy "Beat them up, guys."
    scene ch2ep4_102 with dissolve
    kasen "Hm? But, that's not what we agreed on."
    roxy "Don't worry. I won't ask you to do that for free."
    roxy "I'll give you three thousand dollars for that orange haired guy."
    roxy "And for the other one, I'll give you seven thousand. Beat him up real hard."
    kasen "Okay, deal."
    scene ch2ep4_103 with dissolve
    trevor "[kasen], [dax], both of you go and get them out of here."
    dax "Got it."
    trevor "Be quick. We have more important thing to do."
    kasen "*Laughs* Don't worry about that. It will only take a few seconds."
    scene ch2ep4_104 with dissolve
    kasen "Hey, kids..."
    kasen "Look, let's not make things difficult for us."
    kasen "Why don't you just leave? We'll get our money, and you won't have to get hurt."
    kasen "That sounds like a great idea, right?"
    mc "..................."
    scene ch2ep4_105 with dissolve
    zeke "Step back, [mc]."
    mc "Hm...?"
    zeke "I can't hold it anymore. I'm so angry right now."
    zeke "I really hate people who do bad things just for money."
    zeke "Especially when those things happen to someone I know."
    zeke "I'll deal with these assholes myself...."
    scene ch2ep4_106 with dissolve
    dax "*Sighs* Jeez... These kids are too stupid to understand the situation."
    dax "You think you can handle us?"
    zeke "Just shut up and come fight me already."
    kasen "What an arrogant bastard..."
    scene ch2ep4_107 with dissolve
    kasen "You think you're tough, huh?"
    kasen "I've met so many kids like you that I lost count of them."
    kasen "In the end, none of them stood a chance against me."
    scene ch2ep4_108 with dissolve
    kasen "You're no exception, too!"
    $ renpy.pause()
    scene ch2ep4_109 with dissolve
    zeke "Stop bragging already..."
    kasen "Ouch!"
    scene ch2ep4_110 with dissolve
    zeke "It's so..."
    kasen "Argh!!"
    scene ch2ep4_111 with dissolve
    zeke "Annoying...!"
    u "That was a good move..."
    u "He used a jab to create a distance, then landed a head kick to knock out his opponent."
    u "But, isn't that guy a little bit too weak...?"
    u "He talked so much that I expected him to be a little bit stronger..."
    scene ch2ep4_112 with dissolve
    dax "Damn you!"
    zeke "Ugh...!"
    scene ch2ep4_113 with dissolve
    zeke "Jeez... Punching someone from his back..."
    zeke "How coward of you..."
    dax "Shut up. I saw a chance, and I took it. That's all."
    zeke "Well, that's good for you then...."
    scene ch2ep4_114 with dissolve
    zeke "Because from now on, you won't have a chance anymore."
    dax "Just because you beat my friend, and now you think you're strong, huh?!"
    dax "You aren't any stronger than him. He lost just because he was too careless."
    zeke "Well..."
    scene ch2ep4_115 with dissolve
    zeke "Let's see!"
    dax "Too slow..."
    scene ch2ep4_116 with dissolve
    dax "Take it!"
    zeke "..............."
    scene ch2ep4_117 with dissolve
    dax "What the-?!"
    zeke "My turn..."
    scene ch2ep4_118 with dissolve
    dax "Ugh!!!"
    scene ch2ep4_119 with dissolve
    zeke "I'm not done yet..."
    dax "Ouch!!!!"
    scene ch2ep4_120 with dissolve
    roxy "Fuck! What's wrong with you guys?!"
    roxy "Why are they so weak?! They can't even beat a single person!"
    trevor "Believe me. They aren't as weak as you think they are."
    trevor "That guy is just stronger them."
    scene ch2ep4_121 with dissolve
    roxy "I don't give a fuck about that!"
    roxy "I need you to beat them up no matter what!"
    trevor "Relax. I got this."
    roxy "Really?! I doubt that now!"
    trevor "Just wait and see..."
    scene ch2ep4_122 with dissolve
    trevor "My friends don't usually lose when it comes to fighting 1 on 1."
    trevor "But, you beat them quite easily...."
    trevor "You're so good at fighting. I give you that."
    scene ch2ep4_123 with dissolve
    trevor "However, this is where you have to stop now."
    trevor "I'm not going to let you do whatever you want anymore."
    zeke "Yeah? How are you going to stop me?"
    zeke "Didn't you see what happened to your friends when they tried to stop me?"
    scene ch2ep4_124 with dissolve
    trevor "Don't be too cocky."
    trevor "I'm a lot stronger than you think."
    zeke "Your friends said something like that, too."
    zeke "Look at how they are now."
    trevor "*Sighs*.................."
    scene ch2ep4_125 with dissolve
    zeke "!!!!"
    zeke "(This guy... he's running towards me, yet he doesn't even keep his guard up.)"
    zeke "(What's he trying to do seriously...?)"
    zeke "(I will use a right jab, and let's see how he's going to react.)"
    scene ch2ep4_126 with dissolve
    zeke "(Fuck! I didn't expect this!)"
    scene ch2ep4_127 with dissolve
    zeke "Ugh...!!!"
    u "This guy is good..."
    u "Not only he took [zeke] down, he also use his knees to prevent [zeke] from using his arms."
    trevor "I told you... Don't be too cocky."
    scene ch2ep4_128 with dissolve
    zeke "Ouch...!!!"
    scene ch2ep4_129 with dissolve
    zeke "Ugh...!!!"
    scene ch2ep4_128 with dissolve
    zeke "Argh..!!!"
    scene ch2ep4_129 with dissolve
    zeke "Ouch...!!!"
    scene ch2ep4_130 with dissolve
    u "This is not good...."
    u "If [zeke] keeps getting punched in the face like this, he's surely going to pass out soon..."
    u "I can't let this continues."
    scene ch2ep4_131 with dissolve
    zeke "*Softly breathes*..........."
    trevor "That's it..."
    trevor "This is the end for you no-"
    scene ch2ep4_132 with dissolve
    trevor "Huh??!!"
    scene ch2ep4_133 with dissolve
    trevor "Ouch...!!!"
    trevor "(What was that?! A kick?! Why was it so heavy?!)"
    u "Huh? He managed to block it...?"
    scene ch2ep4_134 with dissolve
    mc "[zeke]...."
    zeke "Ugh......"
    mc "Are you okay? Can you get up?"
    zeke "Y-Yeah...."
    mc "Good. I will handle everything from now on..."
    scene ch2ep4_135 with dissolve
    trevor "Interrupting someone in the middle of a fight..."
    trevor "You have such bad manners."
    mc "We aren't in a competition. What do you expect?"
    scene ch2ep4_136 with dissolve
    trevor "*Laughs* You're right. I completely forgot about that."
    roxy "What the fuck are you doing?!"
    roxy "Stop talking to that bastard, and kick his ass already!"
    trevor "Alright, as you command, princess...."
    scene ch2ep4_137 with dissolve
    trevor "Come on! Show me what you got!"
    mc "...................."
    trevor "Are you just going to stand like that?"
    mc "Can't I?"
    trevor "Alright then, I will start a fight myself."
    scene ch2ep4_138 with dissolve
    trevor "(His kick was so strong... I bet he's a kickboxer.)"
    trevor "(I have to get closer to him...)"
    trevor "(And then I'll take him down so that he can't efficiently land a kick.)"
    trevor "(I need to trick him into thinking that I'm going to punch him in the face.)"
    scene ch2ep4_139 with dissolve
    trevor "(Great... He's brought his guard up as I expected....)"
    trevor "(He's fully protecting his face now.)"
    trevor "(Now, I just have to....)"
    scene ch2ep4_140 with dissolve
    trevor "(Take him down on the ground!!!)"
    zeke "[mc]! Watch out!!"
    trevor "Too late! There's nothing your friend can do n-"
    scene ch2ep4_141 with dissolve
    trevor "Hm...??"
    trevor "(Fuck.....)"
    scene ch2ep4_142 with dissolve
    trevor "Ugh...!!!"
    scene ch2ep4_143 with dissolve
    mc "................."
    scene ch2ep4_144 with dissolve
    trevor "Ouch...!!!!"
    scene ch2ep4_145 with dissolve
    zeke "(It's true that I lost to him, because I was being too cocky...)"
    zeke "(But, he's also very strong, otherwise, I wouldn't have lost like that...)"
    zeke "(I can't believe that [mc] just beat him up so easily...)"
    roxy "Fuck...! Useless! You guys are so fucking useless!!"
    scene ch2ep4_146 with dissolve
    zeke "I don't know who you are, but this is the end for you now!"
    zeke "To be honest I've never hit a woman once in my life..."
    zeke "But, you will be an exception since you hurts my friend so badly!"
    scene ch2ep4_147 with dissolve
    roxy "Pff!! You're going to hit me?!"
    roxy "Don't make me laugh! There is no way you can touch me."
    roxy "Don't you see who am I standing with? He is my personal bodyguard!"
    roxy "I bring him with me today just in case something like this happens."
    scene ch2ep4_148 with dissolve
    roxy "What are you waiting for, [wilson]?"
    roxy "Go beat them for me."
    wilson "Sure, if that's your command..."
    roxy "I can trust you unlike those trash, right?"
    scene ch2ep4_149 with dissolve
    wilson "Of course, I didn't train to lose to ordinary people..."
    roxy "Great. Go prove your word then."
    wilson "Roger that."
    scene ch2ep4_150 with dissolve
    mc "Step back, [zeke]."
    mc "This guy is on another level. I can feel it."
    zeke "Huh? Why don't we just fight him together then?"
    mc "No, you're only going to get in my way."
    zeke "....................."
    mc "Moreover, you're still injured now. So you better step back."
    zeke "Okay...."
    scene ch2ep4_151 with dissolve
    wilson "Are you sure that you want to fight me alone?"
    wilson "You should've listened to your friend."
    mc "....................."
    scene ch2ep4_152 with dissolve
    wilson "You don't talk much, do you?"
    mc "Do we have to talk before fighting?"
    wilson "No, we don't... It's just that I'm interested in you."
    wilson "You've got potential. Aren't you interested in becoming a bodyguard?"
    scene ch2ep4_153 with dissolve
    mc "No, I'm not."
    wilson "That's so unfortunate. What a waste of talent..."
    wilson "Actually, I don't want to do this..."
    scene ch2ep4_154 with dissolve
    wilson "But, I can't turn down the client's order. You got it, right?"
    mc "...................."
    wilson "Don't worry. It will be quick."
    scene ch2ep4_155 with dissolve
    mc "Yeah, I think so...."
    wilson "...................."
    wilson "(This guy... He is really good. He doesn't show any weakness at all.)"
    wilson "(I need to be very careful...)"
    scene ch2ep4_156 with dissolve
    roxy "What the fuck are you doing, [wilson]?"
    roxy "Why are you only standing still like that? It's been almost a minute now!"
    roxy "Kick his ass already!"
    zeke "(Jeez... That girl is so annoying....)"
    scene ch2ep4_157 with dissolve
    wilson "(Hm...?)"
    wilson "(What a great jab... He's punching through my block and aiming for my chin accurately.)"
    wilson "(But, I've been in this situation so many times that I lost count already.)"
    scene ch2ep4_158 with dissolve
    u "Hm? I thought I was quick enough, but he managed to push my arm away just like that?"
    u "Moreover, he's trying to aim for my neck?"
    u "I need to stop him."
    scene ch2ep4_159 with dissolve
    wilson "(!!!!)"
    wilson "(What a great decision... To be honest I expected him to step back from the range of my grab....)"
    scene ch2ep4_160 with dissolve
    wilson "(But, you left your face totally uncovered now!)"
    mc "..................."
    wilson "(How about this punch? How are you going to stop i-)"
    scene ch2ep4_161 with dissolve
    wilson "!!!!!"
    scene ch2ep4_162 with dissolve
    $ renpy.pause()
    scene ch2ep4_163 with dissolve
    wilson "Ugh...!!"
    scene ch2ep4_164 with dissolve
    wilson "....................."
    roxy "Hey! What the fuck!?"
    roxy "You told me that I could trust you?"
    roxy "Then, why the fuck did you get punched like that?!"
    scene ch2ep4_165 with dissolve
    wilson "Your punch was very heavy...."
    wilson "Who are you exactly? Are you a professional fighter?"
    mc "...................."
    mc "I'm just a mere programmer...."
    scene ch2ep4_166 with dissolve
    s "*Police siren sounds*............."
    wilson "Hm...?"
    u "They're finally here, huh? It took them longer than I thought...."
    scene ch2ep4_167 with dissolve
    wilson "Let's get out of here, miss."
    roxy "What the fuck?! You haven't beat a single person yet!"
    wilson "The police is coming here... It's better to leave now."
    wilson "Do you want to get arrested?"
    roxy "Tsk....!"
    scene ch2ep4_168 with dissolve
    roxy "Fine...!!"
    zeke "What the fuck?! Are you guys going to leave just like that!"
    zeke "There is no way I'm going to let you leave!"
    scene ch2ep4_169 with dissolve
    mc "Don't follow them...."
    zeke "What?! Why are you stopping me, bro?"
    zeke "Are you just going to let them run away?!"
    zeke "After everything they've done to [eira]?!"
    scene ch2ep4_170 with dissolve
    mc "Calm down...."
    mc "That girl's dad is a politician. I'm pretty sure that he must have some powers."
    mc "Otherwise, she wouldn't have done something like this fearlessly."
    mc "So, there's no point in turning her to the police now."
    mc "The more important thing is [eira]'s condition."
    zeke "....................."
    zeke "*Sighs* You're right...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_171 with dissolve
    mc "[eira]."
    mc "Hey...."
    zeke "[eira]! Wake up!"
    eira ".................."
    scene ch2ep4_172 with dissolve
    zeke "Bro, she didn't hear us at all..."
    zeke "What should we do?"
    mc "Hand me your car's key."
    zeke "Huh? Why?"
    scene ch2ep4_173 with dissolve
    mc "I'm going to take her to a hospital."
    zeke "Oh yeah, you should do that."
    mc "You're still okay, right? I mean... your injuries."
    zeke "Hm? Why do you ask?"
    scene ch2ep4_174 with dissolve
    mc "I need you to stay here and tell everything to the police."
    zeke "Sure! I'm fine now. Leave it to me."
    mc "Thanks... Alright then, I'm leaving now."
    zeke "Okay."
    scene ch2ep4_175 with dissolve
    tom "Everyone! Freeze! This is police!"
    tom "Hm....?"
    scene ch2ep4_176 with dissolve
    tom "[mc]?"
    tom "How come are you here before us?"
    mc "Everything is over now. You can ask that from my friend later."
    tom "Huh...?"
    scene ch2ep4_177 with dissolve
    mc "I'm sorry, but can you please step aside?"
    mc "I have to take her to a hospital."
    tom "Oh... Is she the victim?"
    mc "Yeah, but she's in a bad condition. She can't answer any question right now."
    tom "I see... That's fine. You better leave now."
    tom "I'll pay her a visit tomorrow."
    scene ch2ep4_178 with dissolve
    zeke "This way!"
    zeke "Send these guys to jail!"
    mc "....................."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ch2ep3_1.mp3" fadein 4.5
    $ bgm = "RYYZN - Memories Erased"
    scene ch2ep4_179 with fade
    mc "What did the police say?"
    mc "I see....."
    mc "Yeah, I'm at the hospital right now."
    scene ch2ep4_180 with dissolve
    mc "Hm...?"
    mc "Hey. I have to end the call now."
    mc "Okay. Get home safe."
    scene ch2ep4_181 with dissolve
    mc "You're already up?"
    eira "Y... Yeah...."
    eira "W... Where am I?"
    scene ch2ep4_182 with dissolve
    mc "We're at the hospital now."
    mc "You lost consciousness because of injuries, so I brought you here."
    eira "I see...."
    mc "How are you feeling now?"
    scene ch2ep4_183 with dissolve
    eira "My face still hurts..."
    eira "But, it's getting better..."
    eira "Thank you for saving me, [mc]."
    mc "It wasn't a big deal. You asked for my help. So, I helped you."
    scene ch2ep4_184 with dissolve
    eira "I would've ended up even worse if it wasn't for you..."
    mc ".................."
    eira "By the way...."
    eira "What happened to [roxy]? Have the police arrested her?"
    scene ch2ep4_185 with dissolve
    mc "No. She ran away before they came."
    mc "I could've caught her, but your condition was more important."
    mc "So, I basically let her run away..."
    eira "I see... It's alright. I don't blame you."
    scene ch2ep4_186 with dissolve
    mc "Okay. I think I should leave now."
    mc "You need to get some rest."
    eira "Hm...? Are you really going to... leave?"
    mc "Yeah, why?"
    eira "... Could you please... stay the night here...?"
    scene ch2ep4_187 with dissolve
    eira "I'm scared... that [roxy] might come here..."
    mc "....................."
    u "What should I do?"
    menu:
        "Stay the night [eira1]":
            $ eira_relationship += 2
            $ eira_ch2_ep4 += 2
            $ ch2ep4staythenight = 1
            scene ch2ep4_188_a1 with dissolve
            mc "Fine...."
            mc "If you want me to stay, I will."
            eira "*Smiles* Thank you, [mc]..."
            scene ch2ep4_188_a2 with dissolve
            mc "Don't be too worried."
            mc "Just close your eyes and get some sleep."
            mc "I'll sit here until you fall asleep, then I'll go sleep on the sofa."
            eira "Okay..."
            scene black with dissolve
            $ renpy.pause()
            s "*About fifteen minutes later*.........."
            scene ch2ep4_188_a3 with dissolve
            mc "[eira]."
            eira ".................."
            u "Seems like she already fell asleep...."
            u "Alright, I should turn off the light and go sleep, too."
            scene ch2ep4_188_a4 with dissolve
            u "...................."
            scene ch2ep4_188_a5 with dissolve
            u "[roxy]...."
            u "She's never going to stop harassing [eira]."
            u "I'm going to need to find a way to get rid of her."
            scene ch2ep4_188_a6 with dissolve
            u "But now, let's just sleep..."
            u "There is no point in thinking about that now."
            u "I'm also a little bit tired as well. I should sleep as much as I can."
            stop music fadeout 3.0
            scene black with dissolve
            $ renpy.pause()
            scene black with dissolve
            $ renpy.pause()
            scene ch2ep4_188_a7 with fade
            play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
            $ bgm = "Roa - Fresh Time"
            eira "*Yawns*............"
            eira "(Morning... already?)"
            scene ch2ep4_188_a8 with dissolve
            eira "(Hm...?)"
            eira "(Where is [mc]...?)"
            eira "(Did he wake up before me and already leave?)"
            scene ch2ep4_188_a9 with dissolve
            eira "(Oh....)"
            eira "(There he is...)"
            scene ch2ep4_188_a10 with dissolve
            eira "(I was so scared last night, then his face popped up in my head.)"
            eira "(Fortunately, I decided to call him just before I got kidnapped.)"
            eira "(But, I still can't believe that he was able to find me.)"
            eira "(It must have been hard for him. I owed him big time...)"
            scene ch2ep4_188_a11 with dissolve
            eira "(Look at him sleeping....)"
            eira "(It's already morning, yet he's still sleeping deeply.)"
            eira "(He must've been very tired...)"
            eira "(I should not wake him up.)"
            scene ch2ep4_188_a12 with dissolve
            eira "*Smiles*..................."
            eira "(He is pretty cute when sleeping...)"
            eira "(Look at his face....)"
            u "What is she doing...?"
            scene ch2ep3_513_a21 with flash
            $ renpy.pause(1, hard=True)
            scene ch2ep4_188_a13 with vpunch
            eira "(What was I thinking?!)"
            eira "(Why did that memory pop out all of sudden?!)"
            eira "...................."
            eira "(Argh...! I don't care anymore!)"
            scene ch2ep4_188_a14 with dissolve
            eira "*Kisses* Mmmm......"
            u "... What? Why is she kissing me?"
            scene ch2ep4_188_a15 with dissolve
            eira "Thank you for everything you've done for me...."
            eira "*Sighs* Thank god. I didn't wake him up."
            u "......................."
            u "I was already up since before you kissed me...."
            menu:
                "[smgr]Pull her for a kiss":
                    stop music fadeout 3.0
                    jump ch2ep4eirahospital
                "Pretend to be sleeping":
                    $ ch2ep4eirakiss = 2
                    scene ch2ep4_189_d1 with dissolve
                    eira "(Ahh! What have I done...!?)"
                    eira "(You are so shameless, [eira]... Why did you kiss him while he's sleeping?)"
                    eira "Ahh... I feel so embarrassed now."
                    mc "......................"
                    scene black with dissolve
                    $ renpy.pause()
                    s "*Ten minutes later*................."
                    scene ch2ep4_189_d2 with dissolve
                    mc "Good morning, [eira]..."
                    eira "Oh?! You're up now."
                    eira "Good morning, [mc]."
                    mc "How are you feeling?"
                    eira "Much better. I think I only need to rest for a couple more hours..."
                    mc "Good to hear that..."
                    scene black with dissolve
                    $ renpy.pause()
                    jump ch2ep4leavehospital
        "Leave":
            $ ch2ep4staythenight = 2
            scene ch2ep4_188_d1 with dissolve
            mc "Don't worry. There is no way she will come here."
            mc "So, just close your eyes and get some sleep."
            mc "I have to go back to my home, too."
            eira "Oh...."
            eira "Okay...."
            scene ch2ep4_188_d2 with dissolve
            mc "Good night, [eira]."
            eira "..................."
            eira ".... Good night, [mc]."
            jump ch2ep4nextday
label ch2ep4eirahospital:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    play music "sfx/ep.3/ep3_12.mp3" fadein 3.0
    $ bgm = "Brook Xiao - Fire (ft. Rachel Horter)"
    scene ch2ep4_189_a1 with dissolve
    eira "!!!!!!"
    mc "*Kisses*..............."
    eira "(What's happening?! What should I do...?!)"
    eira "*Kisses*.............."
    eira "(To be honest... It feels so good. Maybe I should just go with the flow....)"
    scene ch2ep4_189_a2 with dissolve
    mc "Good morning, [eira]."
    eira ".... G... Good morning."
    eira "Since when did you wake up...?"
    mc "Since before you kissed me...."
    eira "Aw...."
    mc "Do you want to continue?"
    eira "...................."
    eira "Yeah...."
    scene ch2ep4_189_a1 with dissolve
    eira "*Kisses*........."
    mc "*Kisses*..........."
    scene ch2ep4_189_a3 with dissolve
    eira "*Softly breathes* [mc]...."
    mc "Hm...?"
    eira "*Softly breathes* N... Nothing..."
    scene ch2ep4_189_a4 with dissolve
    mc "Can I take off your top?"
    eira "....................."
    mc "Or do you want to stop here?"
    eira "No... Please, go on...."
    mc "Okay then...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_189_a5 with dissolve
    eira "Stop staring at me like that...."
    eira "You're making me embarrassed."
    mc "It can't be helped..."
    scene ch2ep4_189_a6 with dissolve
    eira "A-Ah!"
    mc "Sorry. Did I touch them too hard?"
    eira "N... No, it's just... I wasn't ready for that..."
    show ch2ep4_eira1
    window hide
    eira "*Softly breathes* Hah...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_eira1
    scene ch2ep4_189_a7 with dissolve
    show ch2ep4_eira2
    window hide
    eira "*Softly breathes* Ahhh..."
    eira "(I've never done this with anyone before... It feels so weird....)"
    eira "(But, it's not like I hate it....)"
    menu:
        "Next":
            hide ch2ep4_eira2
    scene ch2ep4_189_a8 with dissolve
    show ch2ep4_eira3
    window hide
    eira "*Softly moans* [mc]...."
    menu:
        "Next":
            hide ch2ep4_eira3
    scene ch2ep4_189_a9 with dissolve
    mc "Let me take this off..."
    eira "Wait a sec..."
    mc "Hm? What's wrong?"
    eira "It's embarrassing..."
    mc "No, it's not. Just relax."
    eira ".... Okay."
    scene ch2ep4_189_a10 with dissolve
    eira "Aw... Don't look at me..."
    mc "Calm down..."
    eira "How can I....?"
    scene ch2ep4_189_a11 with dissolve
    mc "*Licks*............"
    eira "A-ah~!"
    scene ch2ep4_189_a12 with dissolve
    show ch2ep4_eira4
    window hide
    eira "*Softly breathes* A... Arrr...."
    eira "*Softly breathes* Mmmm...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_eira4
    scene ch2ep4_189_a13 with dissolve
    show ch2ep4_eira5
    window hide
    eira "*Softly breathes* S... Stop... It's dirty..."
    mc "No, it's not..."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_eira5
    scene ch2ep4_189_a14 with dissolve
    show ch2ep4_eira6
    window hide
    eira "*Moans* Hahh.... This feels... so strange...."
    mc "You'll get used to it soon..."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_eira6
    scene ch2ep4_189_a15 with dissolve
    mc "... Are you ready?"
    eira "..................."
    eira ".... Yeah, I think so."
    mc "You're not going to regret it right?"
    eira "... No. Let's do it...."
    scene ch2ep4_189_a16 with dissolve
    mc "Okay then...."
    eira "Please, be gentle...."
    mc "Sure...."
    scene ch2ep4_189_a17 with dissolve
    eira "*Moans* A-Ahhh...!"
    mc "Does it hurt?"
    eira "A little... bit..."
    mc "Okay, I'll go slowly then."
    scene ch2ep4_189_a18 with dissolve
    show ch2ep4_eira7
    window hide
    eira "*Softly breathes* M.... Mhmmm....."
    mc "How does it feel? Does it still hurt?"
    eira "*Softly breathes* Y... Yeah, but don't worry. I can endure it...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_eira7
    scene ch2ep4_189_a19 with dissolve
    show ch2ep4_eira8
    window hide
    eira "*Softly breathes* A... Ahhh... Ahhh...."
    mc "Your pussy is so fit, [eira]...."
    eira "*Softly breathes* D... Don't say that..."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_eira8
    scene ch2ep4_189_a20 with dissolve
    show ch2ep4_eira9
    eira "*Softly breathes* [mc]..... Mmmm....."
    mc "Are you feeling better now?"
    eira "*Softly breathes* Y... Yeah... It feels good now..."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_eira9
    scene ch2ep4_189_a21 with dissolve
    mc "[eira]."
    eira "H... Hm...?"
    mc "Do you want to try doing it yourself?"
    eira "How...?"
    mc "Get up and turn around, then sit on me."
    eira "Okay... I will try that."
    scene ch2ep4_189_a22 with dissolve
    eira "Like this...?"
    mc "Yeah. Now, you can slowly put it in."
    eira "Okay...."
    scene ch2ep4_189_a23 with dissolve
    eira "*Softly breathes* A... Arng...."
    scene ch2ep4_189_a24 with dissolve
    show ch2ep4_eira10
    window hide
    eira "*Softly breathes* Ha.... Hah...."
    mc "How you like that? Do you like when you're taking control...?"
    eira "*Softly breathes* Y... Yeah, I guess... so...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_eira10
    scene ch2ep4_189_a25 with dissolve
    show ch2ep4_eira11
    window hide
    eira "*Moans* Mhmmm.... You're so big...."
    eira "*Moans* Ahhh... It.... It's really big, [mc]...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_eira11
    scene ch2ep4_189_a26 with dissolve
    show ch2ep4_eira12
    window hide
    eira "*Moans* Ahhh...! [mc]...!"
    mc "Yeah...?"
    eira "*Moans* I think... I'm about to cum....!"
    mc "Me, too. Let's cum together."
    menu:
        "Missionary":
            hide ch2ep4_eira12
            jump ch2ep4eiramis1
        "Slowest":
            hide ch2ep4_eira12
            jump ch2ep4eirasit1
        "Slower":
            hide ch2ep4_eira12
            jump ch2ep4eirasit2
        "Cum":
            jump ch2ep4eiracum
label ch2ep4eiramis1:
    scene ch2ep4_189_a18 with dissolve
    show ch2ep4_eira7
    window hide
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2ep4_eira7
            jump ch2ep4eirasit1
        "Faster":
            hide ch2ep4_eira7
            jump ch2ep4eiramis2
        "Fastest":
            hide ch2ep4_eira7
            jump ch2ep4eiramis3
label ch2ep4eiramis2:
    scene ch2ep4_189_a19 with dissolve
    show ch2ep4_eira8
    window hide
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2ep4_eira8
            jump ch2ep4eirasit1
        "Slower":
            hide ch2ep4_eira8
            jump ch2ep4eiramis1
        "Faster":
            hide ch2ep4_eira8
            jump ch2ep4eiramis3
label ch2ep4eiramis3:
    scene ch2ep4_189_a20 with dissolve
    show ch2ep4_eira9
    window hide
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2ep4_eira9
            jump ch2ep4eirasit1
        "Slowest":
            hide ch2ep4_eira9
            jump ch2ep4eiramis1
        "Slower":
            hide ch2ep4_eira9
            jump ch2ep4eiramis2
label ch2ep4eirasit1:
    scene ch2ep4_189_a24 with dissolve
    show ch2ep4_eira10
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch2ep4_eira10
            jump ch2ep4eiramis1
        "Faster":
            hide ch2ep4_eira10
            jump ch2ep4eirasit2
        "Fastest":
            hide ch2ep4_eira10
            jump ch2ep4eirasit3
label ch2ep4eirasit2:
    scene ch2ep4_189_a25 with dissolve
    show ch2ep4_eira11
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch2ep4_eira11
            jump ch2ep4eiramis1
        "Slower":
            hide ch2ep4_eira11
            jump ch2ep4eirasit1
        "Faster":
            hide ch2ep4_eira11
            jump ch2ep4eirasit3
label ch2ep4eirasit3:
    scene ch2ep4_189_a26 with dissolve
    show ch2ep4_eira12
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch2ep4_eira12
            jump ch2ep4eiramis1
        "Slowest":
            hide ch2ep4_eira12
            jump ch2ep4eirasit1
        "Slower":
            hide ch2ep4_eira12
            jump ch2ep4eirasit2
        "Cum":
            jump ch2ep4eiracum
label ch2ep4eiracum:
    mc "Almost there...."
    menu:
        "Cum inside":
            scene ch2ep4_189_a27_in with vpunch
        "Cum outside":
            scene ch2ep4_189_a27_out with vpunch
    eira "*Moans* Mhmmmmm...!!!"
    mc "Ahh...."
    scene ch2ep4_189_a28 with dissolve
    mc "How was it? Did you enjoy it?"
    eira "*Pants* Y... Yeah... I liked... it a lot...."
    mc "Shall we rest for a bit?"
    eira "*Pants* Y... Yeah, I think... we should do that."
    eira "*Pants* I'm so... exhausting right now...."
    stop music fadeout 3.0
    scene black with dissolve
    $ ch2ep4eirakiss = 1
    $ eira_relationship += 3
    $ eira_ch2_ep4 += 3
    $ renpy.end_replay()
    $ renpy.pause()
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    jump ch2ep4leavehospital
label ch2ep4leavehospital:
    scene ch2ep4_190 with dissolve
    mc "Alright...."
    mc "I think it's time now. I have to go to the company."
    eira "Okay...."
    mc "You can stay here alone, right?"
    scene ch2ep4_191 with dissolve
    eira "Yes. I think I can stay here alone now."
    eira "Don't worry about me."
    mc "Alright then, I'm leaving now...."
    scene ch2ep4_192 with dissolve
    eira "Good bye, [mc]."
    eira "Have a great day...."
    mc "You, too...."
    s "*Door opens*.........."
    scene ch2ep4_193 with dissolve
    sally "[eira]!!!!"
    u "Hm...?"
    eira "[sally]?"
    scene ch2ep4_194 with dissolve
    sally "*Hics* I just heard everything from [zeke]!"
    sally "*Hics* I'm so sorry! I should've waited until you finished working last night!"
    eira "It's alright, [sally]... It's not your fault."
    eira "I'm also fine right now... So, stop crying, okay?"
    scene ch2ep4_195 with dissolve
    sally "*Hics* Are you sure that you're fine now?"
    sally "You don't look fine to me at all...."
    eira "Believe me... I'm really okay now."
    eira "[mc] and [zeke] came to save me in time last night."
    sally "Oh...."
    scene ch2ep4_196 with dissolve
    sally "Thank you so much for saving her, [mc]..."
    eira "*Smiles* Me, too. Thanks again, [mc]..."
    mc "... You're welcome."
    scene ch2ep4_197 with dissolve
    mc "[sally]. Since you're here, I assume you've already taken a day off today, right?"
    sally "Yeah, that's right."
    mc "Okay then, I'll leave [eira] to you."
    mc "Please, take care of her."
    sally "Sure thing."
    mc "See you later, both of you."
    eira "See you, [mc]."
    scene black with dissolve
    $ renpy.pause()
    jump ch2ep4nextday
label ch2ep4nextday:
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_198 with fade
    s "*Door opens*......"
    maya "Thank you for coming."
    maya "Please, take a seat."
    scene ch2ep4_199 with dissolve
    maya "I heard that you wanted to meet me."
    maya "[angela] told me that you have something very important to inform me."
    maya "But first of all..."
    maya "May you introduce yourself, please?"
    felix "My name is [felix]. I'm the Director General of Police."
    maya "Oh... It's my pleasure to meet you."
    felix "Me either."
    scene ch2ep4_200 with dissolve
    maya "So, may I ask what the important thing, you wanted to inform me, is about?"
    felix "It's about your ex-husband."
    stop music fadeout 3.0
    maya "..................."
    felix "He didn't pass away because of the accident."
    maya "W... What are you talking about? I don't understand...."
    felix "He was murdered."
    maya "What?! What did you say?!"
    scene ch2ep4_201 with dissolve
    play music "sfx/ep4_5.mp3" fadein 3.0
    $ bgm = "RYYZN - Waited (instrumental)"
    felix "I said..."
    felix "Your husband was murdered."
    maya "Wh... What made you think like that?"
    felix "Here. Take a look at this."
    scene black with dissolve
    scene ch2ep4_202 with dissolve
    maya "This man...."
    felix "Do you recognize him?"
    maya "Yes I do. Even though he looks much older, how could I forget him?"
    maya "How could I forget a man who killed my ex-husband?"
    scene ch2ep4_203 with dissolve
    maya "But, why are you showing me his picture?"
    maya "This doesn't prove that my husband was murdered."
    maya "And wasn't it just an accident? According to the police, my husband was crossing the road while he was drunk."
    maya "This guy was also drunk when he was driving as well...."
    scene ch2ep4_204 with dissolve
    felix "Well, that's what you were told to believe."
    felix "But, there was something much more than that."
    maya "Hm? What do you mean?"
    felix "Swipe right on the screen, then you will see an audio file."
    felix "Play it and you will understand everything."
    scene ch2ep4_205 with dissolve
    s "*Audio sounds* So, you're asking me to kill this man by making it like an accident?"
    maya "!!!!!!"
    s "*Audio sounds* Yes. That's right."
    s "*Audio sounds* There is no way I'm going to do it. I don't want to go to jail."
    s "*Audio sounds* Don't worry about that. You will only need to be there for no more than ten years. I guarantee you."
    s "*Audio sounds* I will also pay you ten million dollars for the job."
    s "*Audio sounds* Doesn't it sound like a good offer? There is no way you can make ten million dollars in ten years by yourself."
    scene ch2ep4_206 with dissolve
    maya "My poor husband...."
    maya "What did he do to deserve that...?"
    felix "I'm so sorry for your loss."
    maya "....................."
    maya "Thank you. How did you get this file by the way?"
    maya "And who was the person he was talking to?"
    scene ch2ep4_207 with dissolve
    felix "I managed to convince him to tell me the truth. Then, he gave me the file."
    felix "And the person he was talking to... His name is [rio]."
    maya "[rio]? Who is he?"
    felix "No doubt you have never heard of him. His profile has been kept privately."
    felix "He's been working for [victor] for more than 20 years already."
    scene ch2ep4_208 with dissolve
    maya "[victor]...?"
    maya "Don't tell me it's that [victor]...? The most successful businessman in this country?"
    felix "Yes, that's right."
    maya "...................."
    maya "Do you have any evidence that can prove your word?"
    felix "Of course, I do."
    felix "However, please forgive me. I can't show them to you."
    felix "It's not like I don't trust you, but the less people know about this, the better."
    felix "I decided to tell you, because your husband was a victim of [victor]'s shady business."
    maya "................."
    maya "Okay... It's totally understandable."
    scene ch2ep4_209 with dissolve
    maya "(By the way.... Didn't [mc] tell me that he was adopted by [victor]?)"
    maya "(Does he know about [victor]'s shady business...?)"
    maya "(Don't tell me.... that he has always been involved with it?)"
    maya "(What should I do? Should I tell [felix] about [mc]?)"
    maya "(......................)"
    scene ch2ep4_210 with dissolve
    maya ".................."
    angela "(Hm...?)"
    angela "(It looks like she wants to ask me if she should tell [felix] about his son...)"
    scene ch2ep4_211 with dissolve
    $ renpy.pause()
    scene ch2ep4_212 with dissolve
    maya "(Okay... I think I should keep this a secret for now.)"
    maya "(Maybe he really has no clue about [victor]'s shady business...)"
    scene ch2ep4_213 with dissolve
    felix "What's wrong?"
    maya "Hm?"
    felix "You look like you want to say something."
    maya "Nothing. Don't mind me."
    scene ch2ep4_214 with dissolve
    felix "Alright then, I guess that's enough for today."
    maya "Is there something you want me to help you with?"
    felix "Thank you, but there is really nothing you can do."
    felix "Moreover, it's better for you to stay away from this. [victor] is a very dangerous guy."
    maya "Okay. If you say so."
    felix "Alright, I'm going to leave now."
    felix "I'll keep you updated when the time comes."
    scene ch2ep4_215 with dissolve
    maya "Thank you. Good bye, [felix]."
    maya "It was nice to meet you."
    felix "Me, too."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_216 with dissolve
    maya "*Sighs*................"
    angela "Are you okay, president?"
    maya "Yeah...."
    scene ch2ep4_217 with dissolve
    maya "(*Sighs* My poor son....)"
    maya "(I hope you haven't been involved with any of those shady stuffs...)"
    maya "(I have no idea what I should do if he has...)"
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    s "Later that evening......"
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene ch2ep4_218 with fade
    u "Today was so exhausting....."
    u "Let's take a seat and rest for a bit."
    scene ch2ep4_219 with dissolve
    mc ".................."
    if ch2ep4staythenight != 0:
        u "I need to find a way to get rid of [roxy]."
        u "First, let's gather every information about her and her family."
        scene ch2ep4_220 with dissolve
        mc ".................."
        u "Why is he taking so long to pick up my c-"
        u "Okay, he's picked it up now."
        scene ch2ep4_221 with dissolve
        alex "What's up?"
        alex "Why are you calling me out of no where, [mc]?"
        scene ch2ep4_222 with dissolve
        mc "I need your help."
        scene ch2ep4_221 with dissolve
        alex "Hm? What is it that you want me to do?"
        scene ch2ep4_222 with dissolve
        mc "There is a girl named [roxy]."
        mc "Her dad is a politician. I don't know his name, but he's a pretty big one I guess..."
        mc "I want you to check his background to see if he has any weakness."
        scene ch2ep4_223 with dissolve
        alex "Why me though?"
        alex "You can do it by yourself. It's not out of your range, isn't it?"
        scene ch2ep4_224 with dissolve
        mc "You're better than me at this thing."
        mc "That's why I'm asking for your help."
        scene ch2ep4_225 with dissolve
        alex "Wow... I never expected to hear such a compliment like that from you."
        alex "Alright, I will do it for you."
        alex "Give me a couple hours. I will call you back."
        scene ch2ep4_224 with dissolve
        mc "Thanks. Take your time."
        scene ch2ep4_226 with dissolve
        u "Alright...."
        u "What should be done is done."
        u "Now, I just have to wait..."
        if ch2ep2sexwithkrystal == 1:
            s "*Door knocks*..........."
            scene ch2ep4_227 with dissolve
            mc "Hm? Who is it?"
            krystal "It's me..."
            mc "[krystal]?"
            krystal "Yes. Can you open the door please?"
            scene ch2ep4_228 with dissolve
            mc "Okay... Wait a sec."
            scene black with dissolve
            scene ch2ep4_229 with dissolve
            krystal "Good evening, [mc]."
            mc "Good evening..."
            krystal "How's your day?"
            scene ch2ep4_230 with dissolve
            mc "Pretty exhausting."
            mc "What about you?"
            krystal "It was good, but pretty boring...."
            mc "I see... Is there something you want from me by the way?"
            scene ch2ep4_231 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_231.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_231_blink.jpg", 1) with dissolve
            krystal "Nothing much. It's just that it's been awhile since the last time we spent time together."
            mc "To think about it, yeah that's right."
            krystal "And there is a new movie that just came out."
            krystal "So, I'm here to ask you if you want to go to a theater together?"
            krystal "What do you say?"
            menu:
                "Go with her [krystal1]":
                    $ ch2ep4moviewithkrystal = 1
                    $ krystal_relationship += 1
                    $ krystal_ch2_ep4 += 1
                    scene ch2ep4_232_a at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_232_a.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_232_a_blink.jpg", 1) with dissolve
                    mc "That sounds like a good idea. I will go with you."
                    krystal "Really? You aren't kidding me, right?"
                    mc "No, I'm not."
                    krystal "*Smiles* I'm glad to hear that."
                    mc "What about the others?"
                    krystal "I haven't asked them yet. Should I?"
                    mc "....................."
                    mc "Well, it's up to you."
                    krystal "Then, I won't ask them. I want it to be just you and me this time."
                    mc "Okay then, give me a second. I'm going to change my outfit."
                    krystal "Me, too. Come knock on my door when you're ready then."
                    scene ch2ep4_233 with dissolve
                    u "Alright......"
                    u "Let's find something more comfortable to wear."
                    scene black with dissolve
                    $ renpy.pause()
                    jump ch2ep4_moviewithkrystal
                "Refuse":
                    $ ch2ep4moviewithkrystal = 2
                    scene ch2ep4_232_d at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_232_d.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_232_d_blink.jpg", 1) with dissolve
                    mc "That sounds like a good idea, but...."
                    mc "I'm so tired today. I just want to rest."
                    krystal "Oh... Okay then."
                    krystal "Sorry for taking your time. Have a good rest."
                    mc "Next time, okay?"
                    krystal "Okay...."
                    scene black with dissolve
                    $ renpy.pause()
                    s "You spent time with yourself until late night....."
                    jump ch2ep4_alexcall
        else:
            scene black with dissolve
            $ renpy.pause()
            s "You spent time with yourself until late night....."
            jump ch2ep4_alexcall
    else:
        mc ".................."
        if ch2ep2sexwithkrystal == 1:
            s "*Door knocks*..........."
            scene ch2ep4_227 with dissolve
            mc "Hm? Who is it?"
            krystal "It's me..."
            mc "[krystal]?"
            krystal "Yes. Can you open the door please?"
            scene ch2ep4_228 with dissolve
            mc "Okay... Wait a sec."
            scene black with dissolve
            scene ch2ep4_229 with dissolve
            krystal "Good evening, [mc]."
            mc "Good evening..."
            krystal "How's your day?"
            scene ch2ep4_230 with dissolve
            mc "Pretty exhausting."
            mc "What about you?"
            krystal "It was good, but pretty boring...."
            mc "I see... Is there something you want from me by the way?"
            scene ch2ep4_231 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_231.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_231_blink.jpg", 1) with dissolve
            krystal "Nothing much. It's just that it's been awhile since the last time we spent time together."
            mc "To think about it, yeah that's right."
            krystal "And there is a new movie that just came out."
            krystal "So, I'm here to ask you if you want to go to a theater together?"
            krystal "What do you say?"
            menu:
                "Go with her [krystal1]":
                    $ ch2ep4moviewithkrystal = 1
                    $ krystal_relationship += 1
                    $ krystal_ch2_ep4 += 1
                    scene ch2ep4_232_a at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_232_a.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_232_a_blink.jpg", 1) with dissolve
                    mc "That sounds like a good idea. I will go with you."
                    krystal "Really? You aren't kidding me, right?"
                    mc "No, I'm not."
                    krystal "*Smiles* I'm glad to hear that."
                    mc "What about the others?"
                    krystal "I haven't asked them yet. Should I?"
                    mc "....................."
                    mc "Well, it's up to you."
                    krystal "Then, I won't ask them. I want it to be just you and me this time."
                    mc "Okay then, give me a second. I'm going to change my outfit."
                    krystal "Me, too. Come knock on my door when you're ready then."
                    scene ch2ep4_233 with dissolve
                    u "Alright......"
                    u "Let's find something more comfortable to wear."
                    scene black with dissolve
                    $ renpy.pause()
                    jump ch2ep4_moviewithkrystal
                "Refuse":
                    $ ch2ep4moviewithkrystal = 2
                    scene ch2ep4_232_d at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_232_d.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_232_d_blink.jpg", 1) with dissolve
                    mc "That sounds like a good idea, but...."
                    mc "I'm so tired today. I just want to rest."
                    krystal "Oh... Okay then."
                    krystal "Sorry for taking your time. Have a good rest."
                    mc "Next time, okay?"
                    krystal "Okay...."
                    scene black with dissolve
                    $ renpy.pause()
                    s "You spent time with yourself until late night....."
                    jump ch2ep4_skipday
        else:
            scene black with dissolve
            $ renpy.pause()
            s "You spent time with yourself until late night....."
            jump ch2ep4_alexcall
label ch2ep4_moviewithkrystal:
    scene ch2ep4_234 with dissolve
    u "Okay..."
    u "I'm done changing my outfit. Let's go see [krystal]."
    u "I wonder if she's ready now."
    scene ch2ep4_235 with dissolve
    s "*Door knocks*........."
    mc "[krystal], are you done?"
    krystal "Hang on a sec, please!"
    mc "Okay...."
    scene black with dissolve
    s "*A few minutes later*..........."
    scene ch2ep4_236 with dissolve
    krystal "Alright, let's go."
    mc "Hm? Are you going to go there while dressing like this?"
    krystal "Hm? What's wrong with my outfit?"
    mc "Are you not going to wear a cap, or something to hide your face?"
    scene ch2ep4_237 with dissolve
    krystal "Oh...."
    krystal "No, I don't. I feel a little bit uncomfortable when wearing it."
    krystal "I think it's okay to go out like this. I mean... I'm wearing a face mask, right?"
    krystal "And a theater is usually dark. I think no one will recognise me."
    mc "Alright, if you say so."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_238 with fade
    mc "[krystal]...."
    krystal "Hm, yeah?"
    mc "What's the name of the movie you want to watch? I'm going to buy a ticket."
    krystal "Unconditional Love. It's a romantic movie. Do you watch romantic movie?"
    mc "I can watch anything. Wait here, I'm going to get the tickets and some drinks."
    mc "Then, I will bring you inside."
    krystal "Sure, thanks."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_239 with dissolve
    krystal "I watched the teaser this morning."
    mc "Yeah? How was it?"
    krystal "It was so good that I couldn't wait to see the whole movie."
    mc "Really? Since it was able to make you this excited, I can get my hopes up high, right?"
    krystal "Well.... Don't get it up too high though..."
    krystal "It's just a teaser after all. We can only say if a movie is good or bad after we have seen the full movie."
    scene black with dissolve
    $ renpy.pause()
    stop music fadeout 3.0
    s "While you were watching a movie with [krystal], an unexpected scene came up...."
    scene ch2ep4_240 with dissolve
    play music "sfx/ep4_4.mp3" fadein 3.0
    $ bgm = "Le Gang - Bad Intentions"
    s "*Movie sounds* Ahhh.... Mhhmmm...."
    krystal "!!!!!!!!"
    mc "..................."
    scene ch2ep4_241 with dissolve
    krystal "*Whispers* I-I-I swear... I never knew it was an erotic movie...."
    krystal "*Whispers* I... I... mean... There was no scene like this in the teaser...."
    krystal "*Whispers* D... Don't get me wrong. I... I didn't mean to...."
    mc "*Whispers* Calm down, [krystal]..."
    mc "*Whispers* It's okay... You didn't do anything wrong."
    mc "*Whispers* Let's just enjoy watching the movie, okay?"
    krystal "*Whispers* Okay...."
    scene ch2ep4_242 with dissolve
    s "*Movie sounds* Yeah, baby... Harder.... Do it harder..."
    krystal "(Oh my god.... this is too much.)"
    krystal "(It's so close to becoming a porno.)"
    krystal "(I can't believe they allowed a movie like this to show in a theater....)"
    scene ch2ep4_243 with dissolve
    krystal "(This is bad.... I'm getting horny just by watching the movie....)"
    krystal "([krystal]... You're such a naughty woman...)"
    krystal "(But, it can't be helped.... I'm so turned on right now....)"
    scene ch2ep4_244 with dissolve
    krystal "....................."
    krystal "(I can't hold it anymore.....)"
    scene ch2ep4_245 with dissolve
    mc "*Whispers* Hm? Where are you going? Toilet?"
    krystal "....................."
    scene ch2ep4_246 with dissolve
    mc "*Whispers* W... What are you doing, [krystal]?"
    krystal "*Whispers* I know you're turned on, too...."
    krystal "*Whispers* Let me help you out."
    mc "......................"
    menu:
        "Allow her [smrec]":
            $ ch2ep4hintheater = 1
            jump ch2ep4_hscenekrystal
        "Stop her":
            $ ch2ep4hintheater = 2
            scene ch2ep4_247_d with dissolve
            stop music fadeout 3.0
            mc "No, [krystal]. Stop."
            krystal ".... Why?"
            mc "You shouldn't be doing something like this here."
            mc "Every theater has a CCTV. You don't want to get caught, right?"
            mc "Especially, since your situation just got better..."
            krystal "....................."
            krystal "Yeah... You're right. I didn't think it through..."
            mc "Okay then, go back to your seat and continue watching the movie as if nothing happened."
            krystal "I get it."
            scene black with dissolve
            $ renpy.pause()
            s "You spent time watching the movie until it ended...."
            jump ch2ep4_movieend
label ch2ep4_hscenekrystal:
    scene ch2ep4_247_a with dissolve
    mc "Alright...."
    mc "It's a little bit risky, but I won't stop you."
    mc "Do whatever you want."
    krystal "See? I know you need my help..."
    scene ch2ep4_248 with dissolve
    krystal "*Giggles* It popped out as soon as your zipper was down..."
    krystal "*Whispers* You are surely horny now..."
    krystal "*Whispers* Let me help you getting better..."
    scene ch2ep4_249 with dissolve
    show ch2ep4_krystal1
    krystal "*Whispers* How does it feel?"
    mc "*Whispers* Great... Keep doing what you're doing now."
    $ renpy.pause()
    menu:
        "Next":
            scene ch2ep4_250 with dissolve
            hide ch2ep4_krystal1
            show ch2ep4_krystal2
            krystal "*Whispers* It's so hard and hot...."
            krystal "*Whispers* It's not going to explode, right?"
            mc "*Whispers* That's impossible...."
            krystal "*Giggles* I know that..."
            menu:
                "Next":
                    hide ch2ep4_krystal2
                    scene ch2ep4_251 with dissolve
                    show ch2ep4_krystal3
                    krystal "*Sucks* Mmmm.... It's so big...."
                    krystal "*Sucks* It can barely fit my mouth... I'm still not used to it..."
                    mc "You will eventually...."
                    $ renpy.pause()
                    menu:
                        "Next":
                            hide ch2ep4_krystal3
                            scene ch2ep4_252 with dissolve
                            show ch2ep4_krystal4
                            krystal "*Sucks* Mhhmm..........."
                            krystal "*Sucks* Mmmmm.... Tell me if you're going to cum, okay?"
                            $ renpy.pause()
                            menu:
                                "Next":
                                    hide ch2ep4_krystal4
                                    scene ch2ep4_253 with dissolve
                                    mc "*Whispers* Stop...."
                                    krystal "*Whispers*.... Hm? Why?"
                                    krystal "*Whispers* Did I do something wrong?"
                                    scene ch2ep4_254 with dissolve
                                    mc "*Whispers* No, you didn't."
                                    mc "*Whispers* It's just I've got another idea..."
                                    krystal "*Whispers* Hm? What idea are you talking about?"
                                    scene ch2ep4_255 with dissolve
                                    mc "*Whispers* Come on. Follow me."
                                    krystal "*Whispers* Okay...."
                                    krystal "(His hand... is holding mine....)"
                                    krystal "(I know we had sex together, but to hold hands like this.... I don't know why, but it feels very good.)"
                                    scene black with dissolve
                                    $ renpy.pause()
                                    scene ch2ep4_256 with fade
                                    krystal "*Kisses* Mhmmm....."
                                    mc "*Kisses* Stick your tongue out...."
                                    krystal "*Kisses* Mhmmm... Okay...."
                                    scene black with dissolve
                                    scene ch2ep4_257 with dissolve
                                    mc "Let me take your skirt and panties off."
                                    krystal "Just do it.... You don't have to say that...."
                                    mc "Alright then..."
                                    scene ch2ep4_258 with dissolve
                                    krystal "Are we really going to do it here...?"
                                    mc "Yeah, why not?"
                                    krystal "I don't know... We might get caught..."
                                    krystal "Unlike in the theater, it was darker there."
                                    mc "Don't worry. No one will come here at a time like this."
                                    mc "Even if they come, we will notice him first."
                                    krystal "Okay...."
                                    scene ch2ep4_259 with dissolve
                                    show ch2ep4_krystal5
                                    mc "*Licks* Let me get you ready first..."
                                    krystal "*Softly breathes* Ahh.... [mc]...."
                                    krystal "*Softly breathes* It's ticklish...."
                                    $ renpy.pause()
                                    menu:
                                        "Next":
                                            hide ch2ep4_krystal5
                                            scene ch2ep4_260 with dissolve
                                            show ch2ep4_krystal6
                                    krystal "*Softly breathes* Mhmmm... Right there..."
                                    krystal "*Softly breathes* Yeah... Don't stop...."
                                    $ renpy.pause()
                                    menu:
                                        "Next":
                                            hide ch2ep4_krystal6
                                            scene ch2ep4_261 with dissolve
                                            show ch2ep4_krystal7
                                    krystal "*Softly breathes* Ahhh... [mc]...."
                                    krystal "*Softly breathes* Why are you... so good at this...?"
                                    $ renpy.pause()
                                    menu:
                                        "Next":
                                            hide ch2ep4_krystal7
                                            scene ch2ep4_262 with dissolve
                                    mc "Alright, I think you're ready now."
                                    mc "Get up."
                                    krystal "Hm? Why?"
                                    scene ch2ep4_263 with dissolve
                                    mc "I want you to do it for me."
                                    krystal "... How?"
                                    mc "Let me take a seat first, then I will tell you."
                                    krystal "Okay..."
                                    scene ch2ep4_264 with dissolve
                                    mc "Alright...."
                                    mc "Now I want you to come closer, turn around, then sit on my cock."
                                    krystal "You're quite bossy today...."
                                    krystal "But, it's not that I hate it..."
                                    scene black with dissolve
                                    scene ch2ep4_265 with dissolve
                                    krystal "...Is this what you want?"
                                    krystal "You want me to sit on you just like this?"
                                    mc "Yeah, go ahead...."
                                    krystal "*Giggles* As you wish...."
                                    scene ch2ep4_266 with dissolve
                                    krystal "*Softly moans* Arhh....."
                                    krystal "*Softly breathes* It's so... big...."
                                    mc "Hang on a sec...."
                                    scene ch2ep4_267 with dissolve
                                    mc "Alright, you can start moving your hips now..."
                                    krystal "Okay, boss..."
                                    scene ch2ep4_268 with dissolve
                                    show ch2ep4_krystal8
                                    krystal "*Softly breathes* Mhhmm.... Your cock...."
                                    krystal "*Softly breathes* It's reaching.... in so deep.... in this position...."
                                    krystal "*Softly breathes* It feels.... so good...."
                                    $ renpy.pause()
                                    menu:
                                        "Next":
                                            hide ch2ep4_krystal8
                                    scene ch2ep4_269 with dissolve
                                    show ch2ep4_krystal9
                                    krystal "*Softly breathes* Ahh.... Mhhmm...."
                                    mc "Great... Keep moving your hips just like that..."
                                    krystal "*Softly breathes* Should I.... move it a little bit.... faster....?"
                                    mc "If that's what you want...."
                                    $ renpy.pause()
                                    menu:
                                        "Next":
                                            hide ch2ep4_krystal9
                                    scene ch2ep4_270 with dissolve
                                    show ch2ep4_krystal10
                                    krystal "*Heavily breathes* Ahhh.... [mc]....."
                                    mc "Shh... Lower your voice down...."
                                    krystal "*Heavily breathes* I... I'm trying, but it's... hard...."
                                    $ renpy.pause()
                                    menu:
                                        "Next":
                                            hide ch2ep4_krystal10
                                    scene ch2ep4_271 with dissolve
                                    mc "Stop. Hang on a sec."
                                    krystal "... W... What? Why?"
                                    mc "Now, let me do it myself...."
                                    krystal "Okay...."
                                    scene black with dissolve
                                    scene ch2ep4_272 with dissolve
                                    mc "Bend over here.... Lower your knees down a little bit."
                                    krystal "Like this....?"
                                    mc "Yeah, like that...."
                                    mc "Alright, I'm going to put it...."
                                    scene ch2ep4_273 with dissolve
                                    mc "... in."
                                    krystal "Softly breathes* Arrr....."
                                    scene ch2ep4_274 with dissolve
                                    show ch2ep4_krystal11
                                    mc "How does it feel? Which position do you like the most?"
                                    mc "This one? Or the previous one?"
                                    krystal "*Softly breathes* Mhhmmm... I don't know...."
                                    krystal "*Softly breathes* It both feels so good to be honest...."
                                    $ renpy.pause()
                                    menu:
                                        "Next":
                                            hide ch2ep4_krystal11
                                    scene ch2ep4_275 with dissolve
                                    show ch2ep4_krystal12
                                    krystal "*Softly breathes* Y... Yeah...! That's spot...!"
                                    krystal "*Softly breathes* D.. Don't stop...! Keep hitting that spot, please...!"
                                    mc "Alright, since you like that much, I will do it faster...."
                                    $ renpy.pause()
                                    menu:
                                        "Next":
                                            hide ch2ep4_krystal12
                                    scene ch2ep4_276 with dissolve
                                    show ch2ep4_krystal13
                                    krystal "*Heavily breathes* Mhhhmmm....! A... Almost there...!"
                                    krystal "*Heavily breathes* I'm.... I'm about to cum...!"
                                    mc "Me, too...."
                                    krystal "*Heavily breathes* Please, cum for me... Let's cum together..."
                                    $ renpy.pause()
                                    menu:
                                        "Sitting":
                                            hide ch2ep4_krystal13
                                            jump ch2ep4_hscenekrystal_sit1
                                        "Slowest":
                                            hide ch2ep4_krystal13
                                            jump ch2ep4_hscenekrystal_behind1
                                        "Slower":
                                            hide ch2ep4_krystal13
                                            jump ch2ep4_hscenekrystal_behind2
                                        "Cum":
                                            jump ch2ep4_hscenekrystal_cum
label ch2ep4_hscenekrystal_sit1:
    scene ch2ep4_268 with dissolve
    show ch2ep4_krystal8
    window hide
    $ renpy.pause()
    menu:
        "From behind":
            hide ch2ep4_krystal8
            jump ch2ep4_hscenekrystal_behind1
        "Faster":
            hide ch2ep4_krystal8
            jump ch2ep4_hscenekrystal_sit2
        "Fastest":
            hide ch2ep4_krystal8
            jump ch2ep4_hscenekrystal_sit3
label ch2ep4_hscenekrystal_sit2:
    scene ch2ep4_269 with dissolve
    show ch2ep4_krystal9
    window hide
    $ renpy.pause()
    menu:
        "From behind":
            hide ch2ep4_krystal9
            jump ch2ep4_hscenekrystal_behind1
        "Slower":
            hide ch2ep4_krystal9
            jump ch2ep4_hscenekrystal_sit1
        "Faster":
            hide ch2ep4_krystal9
            jump ch2ep4_hscenekrystal_sit3
label ch2ep4_hscenekrystal_sit3:
    scene ch2ep4_270 with dissolve
    show ch2ep4_krystal10
    window hide
    $ renpy.pause()
    menu:
        "From behind":
            hide ch2ep4_krystal10
            jump ch2ep4_hscenekrystal_behind1
        "Slowest":
            hide ch2ep4_krystal10
            jump ch2ep4_hscenekrystal_sit1
        "Slower":
            hide ch2ep4_krystal10
            jump ch2ep4_hscenekrystal_sit2
label ch2ep4_hscenekrystal_behind1:
    scene ch2ep4_274 with dissolve
    show ch2ep4_krystal11
    window hide
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2ep4_krystal11
            jump ch2ep4_hscenekrystal_sit1
        "Faster":
            hide ch2ep4_krystal11
            jump ch2ep4_hscenekrystal_behind2
        "Fastest":
            hide ch2ep4_krystal11
            jump ch2ep4_hscenekrystal_behind3
label ch2ep4_hscenekrystal_behind2:
    scene ch2ep4_275 with dissolve
    show ch2ep4_krystal12
    window hide
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2ep4_krystal12
            jump ch2ep4_hscenekrystal_sit1
        "Slower":
            hide ch2ep4_krystal12
            jump ch2ep4_hscenekrystal_behind1
        "Faster":
            hide ch2ep4_krystal12
            jump ch2ep4_hscenekrystal_behind3
label ch2ep4_hscenekrystal_behind3:
    scene ch2ep4_276 with dissolve
    show ch2ep4_krystal13
    window hide
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2ep4_krystal13
            jump ch2ep4_hscenekrystal_sit1
        "Slowest":
            hide ch2ep4_krystal13
            jump ch2ep4_hscenekrystal_behind1
        "Slower":
            hide ch2ep4_krystal13
            jump ch2ep4_hscenekrystal_behind2
        "Cum":
            jump ch2ep4_hscenekrystal_cum
label ch2ep4_hscenekrystal_cum:
    krystal "*Heavily breathes* I... I can't hold it anymore...!"
    menu:
        "Cum inside":
            hide ch2ep4_krystal13
            scene ch2ep4_277 with vpunch
            krystal "I'm cumminggg...!!!"
            krystal "Mhhmmmm.....!!!!"
            mc "Ugh...! Me, too...!"
            scene ch2ep4_278_in with dissolve
            mc "I'm pulling it out...."
            krystal "You came a lot.... I can feel it...."
            mc "Yeah...."
        "Cum outside":
            hide ch2ep4_krystal13
            scene ch2ep4_277 with vpunch
            krystal "I'm cumminggg...!!!"
            krystal "Mhhmmmm.....!!!!"
            scene ch2ep4_278_out with vpunch
            mc "Ugh...! Me, too...!"
    scene black with dissolve
    scene ch2ep4_279 with dissolve
    mc "Let's rest for a bit...."
    krystal "*Pants* G... Great idea... I'm so tired right now...."
    mc "You moaned so loud.... Luckily, we didn't get caught...."
    krystal "*Pants* I... couldn't help it.... It felt too good...."
    krystal "*Pants* It's not.... my fault entirely, isn't it?"
    mc "Yeah, you could say that..."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_280 with dissolve
    stop music fadeout 3.0
    mc "Alright... What are we going to do now?"
    mc "Should we go find something to eat, then go home?"
    mc "Or do you want to go back and continue watching the movie?"
    mc "I'll let you decide."
    krystal "Ummm....."
    scene ch2ep4_281 with dissolve
    krystal "Let's just go back and finish the movie."
    krystal "We are out here for only 10 minutes, right? We haven't missed out the most part of the movie."
    krystal "Plus, I really want to see how it ends."
    mc "Alright then, let's go...."
    $ renpy.end_replay()
    $ krystal_relationship += 3
    $ krystal_ch2_ep4 += 3
    scene black with dissolve
    $ renpy.pause()
    s "You spent time watching the movie until it ended...."
    jump ch2ep4_movieend
label ch2ep4_movieend:
    scene ch2ep4_282 with dissolve
    krystal "The movie was so good, wasn't it?"
    krystal "What do you think, [mc]?"
    mc "Yeah, I agree with you. It was good."
    krystal "Right? Even though the ending was a little bit sad, the whole story was very heart-warming."
    mc "Yeah, I feel that, too."
    krystal "Hey. Why don't we find something to eat before going home?"
    krystal "We can also continue talking about the movie when we are in the restaurant."
    mc "That sounds like a good idea. Let's go."
    scene black with dissolve
    $ renpy.pause()
    s "You spent more time with [krystal], then came back home...."
    if ch2ep4staythenight != 0:
        jump ch2ep4_alexcall
    else:
        jump ch2ep4_skipday
label ch2ep4_alexcall:
    scene ch2ep4_283 with fade
    play music "sfx/ch2ep2_7.mp3" fadein 3.0
    $ bgm = "Neutrin05 - Rain and Tears"
    mc "........................"
    s "*Phone vibrates*................"
    u "Hm....?"
    scene ch2ep4_284 with dissolve
    u "Oh...."
    u "It's [alex]."
    u "Well, that was quite fast. I guess he's already found something."
    u "Let's hear him out."
    scene ch2ep4_285 with dissolve
    mc "................."
    mc "... Hello."
    scene black with dissolve
    scene ch2ep4_286 with dissolve
    alex "Have you seen the email that I sent it to you?"
    alex "Hm? You haven't seen it yet?"
    alex "That dude named [arlo]. Like you said, he's a politician. Quite powerful one."
    alex "But, that's not a problem. I've found tons of his weaknesses."
    scene ch2ep4_287 with dissolve
    alex "I've already sent them to you via email."
    alex "You better check it out, then thanks me later."
    alex "By the way...."
    alex "Why are you going after him? This isn't a part of the original plan, right?"
    alex "What's going on?"
    scene ch2ep4_288 with dissolve
    mc "..................."
    mc ".... No, it's not. But, you don't have to worry about it."
    mc "I will not let it effects the original plan in a negative way."
    mc "Alright, I'm going to hang up now. Thank you for your help. Bye."
    scene ch2ep4_289 with dissolve
    u "Okay....."
    u "Let's check the email...."
    u "I wonder what weaknesses he was talking about..."
    scene ch2ep4_290 with dissolve
    u "Hm...?"
    u "What is this transaction document?"
    u "He often deposit a great amount of money to a company named Alta."
    u "Wait... Alta company doesn't really exist. It's just a paper company."
    scene ch2ep4_291 with dissolve
    u "There are also other evidences of crimes he committed...."
    u "Well, Tax evasion.... Accepting bribes from many companies...."
    u "Yeah... these documents can surely end his whole life."
    scene ch2ep4_292 with dissolve
    u "Hm...? I was about to search for it, but looks like [alex] already provided me [arlo]'s personal email address..."
    u "Alright, let's send these documents to him...."
    u "..........................."
    u "Okay... It's done."
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*................"
    scene ch2ep4_293 with dissolve
    mc "........................"
    scene ch2ep4_294 with dissolve
    s "*Phone vibrates*............"
    u "Well... That didn't take so long. I guess it must be him."
    u "*Phone vibrates*............"
    u "Let's pick it up and see what's going to happen."
    scene ch2ep4_295 with dissolve
    mc "......................"
    u "Wait... I better don't say anything."
    u "Let's wait for him to start the conversation."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_296 with fade
    arlo "Who the hell are you?"
    arlo "Why did you send me these documents? Where did you get them?"
    arlo "What do you want?"
    scene ch2ep4_295 with dissolve
    mc "Embezzlement.... Tax evasion.... Taking bribes...."
    mc "To be honest I shouldn't be the one saying this, but..."
    mc ".... That's quite a lot of crimes you committed."
    scene ch2ep4_296 with dissolve
    arlo "Shut up. What party are you from?"
    arlo "What? You aren't a politician. Stop fucking kidding me."
    arlo "Why are you trying to blackmail me then if you aren't a politician?"
    arlo "What do you fucking want? Money?"
    scene ch2ep4_297 with dissolve
    mc "No, I don't want any money. I only want you to do one thing."
    mc "It's very easy and simple. If you can do it, I'm going to delete everything."
    scene ch2ep4_296 with dissolve
    arlo "Alright then...."
    arlo "Tell me what you want me to do."
    scene ch2ep4_297 with dissolve
    mc "I want you to stop your daughter from harrassing my friend."
    mc "Tell her that. She will know who's the person she has to stop harrassing."
    mc "That's it. It's very easy and simple, right?"
    mc "I don't care how you are going to do it, but I and my friend must not see your daughter again."
    scene ch2ep4_298 with dissolve
    arlo "Okay, sure."
    arlo "I will tell her to stop. You have my promise."
    arlo "Now, delete everything as you said."
    scene ch2ep4_297 with dissolve
    mc "......................."
    mc "Do you think I'm stupid?"
    mc "Your promise doesn't mean anything."
    mc "You've got to do better than that."
    scene ch2ep4_299 with dissolve
    mc "You have to do something to convince me that your daughter will stay away from us."
    mc "Call me back when you are done with your daughter."
    mc "And don't even think about doing something stupid."
    mc "I don't feel like wasting time ruining your whole life.... if not necessary...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_300 with dissolve
    u "Alright.... It's pretty late now."
    u "Let's go take a shower, then go to bed...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_301 with dissolve
    arlo "Fuck! Ordering me around with that tone of voice."
    arlo "Who the hell he think he is?!"
    unknown "I heard you were looking for me, sir."
    scene ch2ep4_303 with dissolve
    wilson "Is there something you want me to do?"
    arlo "Where is [roxy]? Aren't you supposed to be with her?"
    wilson "She's at a nightclub, sir. She insisted on going there alone, so..."
    arlo "Tsk... And you really let her go alone?"
    wilson ".... My apologies."
    scene ch2ep4_302 with dissolve
    arlo "Forget it. Where did you go with [roxy] last night?"
    arlo "What did you guys do?"
    wilson "...................."
    arlo "Answer me."
    scene ch2ep4_303 with dissolve
    wilson ".... She kidnapped a girl and beat her up, sir."
    arlo "Who's that girl?"
    wilson "Her name is [eira], sir. She's a high school friend of young miss."
    arlo "Then, why did my daughter do that to her?"
    wilson "She said that she hated her, sir."
    arlo "*Sighs*.............."
    scene ch2ep4_304 with dissolve
    arlo "*Smirks* I guess I just got a call from her friend."
    arlo "He tried to threaten me with the information he isn't supposed to have."
    arlo "Do you know this guy?"
    wilson "There were two guys coming to help that girl. I think I know which one called you."
    scene ch2ep4_305 with dissolve
    arlo "Great. Then, investigate him."
    arlo "Gather every information you can get."
    arlo "Then, bring him to me."
    wilson "Understood."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    jump ch2ep4_nextday
label ch2ep4_skipday:
    scene ch2ep4_300 with dissolve
    u "Alright.... It's pretty late now."
    u "Let's go take a shower, then go to bed...."
    scene black with dissolve
    $ renpy.pause()
    jump ch2ep4_nextday
label ch2ep4_nextday:
    scene black with dissolve
    $ renpy.pause()
    s "*Next morning*............."
    play music "sfx/ch2ep2_1.mp3" fadein 3.0
    $ bgm = "Roa Music - After the rain"
    scene ch2ep4_306 with dissolve
    u "Alright...."
    u "It's almost time for work."
    u "Let's go to the company."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_307 with fade
    mc "......................."
    if ch2ep2suggestalice == 1:
        unknown "[mc]..."
        u "Hm....?"
        scene ch2ep4_308 with dissolve
        mc "Oh, it's you...."
        mc "Good morning, [faye]."
        faye "Good morning, [mc]."
        scene ch2ep4_309 with dissolve
        faye "It's been awhile, huh?"
        faye "How have you been?"
        mc "Great, and you?"
        faye "Me either."
        scene ch2ep4_310 with dissolve
        faye "By the way, have you heard the news?"
        mc "Hm? What news?"
        faye "Your friend, [alice], is going to work with us now."
        faye "Hasn't she told you yet?"
        mc "No, she hasn't...."
        faye "Oh.... Well, I guess she just wants to tell that to you in person."
        mc "May be...."
        scene ch2ep4_311 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_311.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_311_blink.jpg", 1) with dissolve
        faye "Oh, hey...."
        faye "Have you got any plan at lunch time yet?"
        mc ".... No, I haven't. Why?"
        faye "Do you want to have lunch with me today?"
        faye "[alice] will come, too."
        faye "What do you think?"
        mc "......................."
        menu:
            "Agree to have lunch [faye2]":
                $ ch2ep4lunchfayealice = 1
                $ faye_relationship += 2
                $ faye_ch2_ep4 += 2
                scene ch2ep4_312_a at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_312_a.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_312_a_blink.jpg", 1) with dissolve
                mc "Okay. I will go with you guys."
                faye "Great. Twelve fifteen at Burger Queen."
                faye "Let's meet up there, okay?"
                mc "Got it."
            "Refuse":
                $ ch2ep4lunchfayealice = 2
                scene ch2ep4_312_d at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_312_d.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_312_d_blink.jpg", 1) with dissolve
                mc "Actually...."
                mc "I think I want to have lunch alone today."
                faye "Well, I just thought we should go celebrate together since you were the one suggesting her after all."
                faye "But, it's fine. I'm not going to force you."
                mc "I'm sorry..."
        scene ch2ep4_313 with dissolve
        s "*Elevator sounds*............."
        faye "The elevator has arrived. Let's go."
        mc "Okay."
        jump ch2ep4lunchbreak
    else:
        s "*Elevator sounds*............."
        u "Alright, the elevator has arrived. Let's go the my department."
        jump ch2ep4lunchbreak
label ch2ep4lunchbreak:
    scene black with dissolve
    $ renpy.pause()
    s "You spent time working until lunch break....."
    scene ch2ep4_314 with dissolve
    u "Alright...."
    if ch2ep4lunchfayealice == 1:
        u "[faye] said twelve fifteen at Burger Queen."
        u "It's five past twelve now. I better hurry up...."
        scene black with dissolve
        $ renpy.pause()
        jump ch2ep4burgerqueen
    else:
        u "It's lunch break now. Let's go find something to eat...."
        scene black with dissolve
        $ renpy.pause()
        s "You spent your time having lunch........."
        jump ch2ep4breakend
label ch2ep4burgerqueen:
    scene ch2ep4_315 with fade
    mc "....................."
    u "Where is she....?"
    scene ch2ep4_316 with dissolve
    u "Hm...?"
    u "There she is...."
    u "[alice] is here as well. Seems like they've been there for some time already."
    u "They still haven't noticed me. Let's approach them."
    scene ch2ep4_317 with dissolve
    mc "Hi, [faye]."
    faye "Oh? Hey."
    scene ch2ep4_318 with dissolve
    mc "[alice]..."
    alice "Hi, [mc]! Long time to see!"
    mc "How long have you guys been here?"
    alice "Not too long. Five minutes ago I guess."
    mc "I see..."
    scene ch2ep4_319 with dissolve
    faye "I'm sorry to interrupt you guys, but I think you should go order your food first, [mc]."
    faye "The restaurant is getting more crowded."
    mc "Yeah... you're right."
    mc "You guys can eat first. No need to wait for me. I'll be right back."
    alice "It's alright. We can wait. Just go order your food."
    mc "Alright then."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_320 with dissolve
    nina "Hello, [mc]. It's been a while!"
    mc "Yeah, it's been a while."
    nina "How have you been?"
    mc "Pretty busy, and you?"
    scene ch2ep4_321 with dissolve
    nina "Me, too."
    nina "Is that the reason why you haven't visited the gym since that day?"
    mc "Yeah, pretty much that."
    mc "I had a lot of things to deal with."
    nina "I see...."
    scene ch2ep4_322 with dissolve
    nina "Alright, what do you want to eat for today?"
    mc "I'd like to have a set of beef burger, please."
    nina "What about a drink?"
    mc "A cup of cola will do."
    nina "Got it. A set of beef burger and a cup of cola..."
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*.........."
    scene ch2ep4_323 with dissolve
    nina "Sorry to have kept you waiting."
    nina "Here is your meal. Please, enjoy your lunch!"
    mc "Thank you."
    scene ch2ep4_324 with dissolve
    alice "[mc]."
    mc "Yeah?"
    alice "Come sit with me here."
    mc "Okay..."
    scene ch2ep4_325 with dissolve
    mc "...................."
    alice "Hm? What's wrong?"
    alice "Why are you staring at me like that?"
    mc "It's just... I'm not familiar with you dressing formally."
    mc "You look good today."
    alice "*Smiles* Hehe... Thanks!"
    scene ch2ep4_326 with dissolve
    faye "[mc]."
    mc "Huh?"
    faye "I don't remember if I already said it, so I will say it now."
    faye "Thank you introducing [alice] to me."
    faye "The project is progressing because of you."
    mc "...................."
    mc "Well, I actually didn't do nothing much."
    faye "Still... Thank you."
    scene ch2ep4_327 with dissolve
    faye "I listened to the demo you sent me this morning, [alice]."
    faye "The theme song when entering the second main quest."
    alice "Yeah? What do you think about it?"
    faye "It was wonderful. I loved it."
    scene ch2ep4_328 with dissolve
    alice "*Smiles* Really?! I'm glad to hear that!"
    alice "To hear such a compliment from someone like you, is the best motivation for you!"
    alice "I'm going to make the full version even more better!"
    mc "...................."
    u "To see [alice] being happy working her dream job like this,...."
    u "It makes me a little bit happy, too..."
    scene ch2ep4_329 with dissolve
    alice "I think the full version will be finished within a week."
    alice "I will send it to you as soon as I finish."
    faye "I'm looking forward to it."
    u "They seem to be having a good time, let's not interrupt them...."
    scene black with dissolve
    $ renpy.pause()
    s "*About half an hour later*........."
    scene ch2ep4_330 with dissolve
    alice "Thank you for the lunch, [faye]."
    alice "I had a genuinely great time talking to you."
    faye "Me, either."
    scene ch2ep4_331 with dissolve
    alice "I didn't talk with you much today, [mc]..."
    mc "It's okay. Don't worry about that."
    alice "I wish we could hang out together for a little bit more."
    alice "But, I've got to leave now. I have to go see my family."
    scene ch2ep4_332 with dissolve
    faye "May I ask where your family is?"
    alice "Sure. They live in city C."
    faye "Hm? City C?"
    alice "Yeah. It's pretty far from here, isn't it?"
    scene ch2ep4_334 with dissolve
    faye "I can take you there if you want."
    alice "No. No. No. You don't have to do that."
    alice "It's 2 hours away from here. I don't want to take your time."
    faye "Don't worry about that. Actually, I have a business meeting this evening over there as well."
    scene ch2ep4_335 with dissolve
    alice "Really?! What a coincidence!"
    faye "Right? That's why I told you I could take you there."
    faye "So, what do you say? Do you want to come with me?"
    alice "That would be my pleasure! Thank you so much!"
    faye "Alright, let's go then."
    alice "Sure!"
    scene ch2ep4_336 with dissolve
    alice "Good bye, [mc]! See you later!"
    mc "Yeah, see you later."
    mc "Travel safely, [faye]."
    faye "Sure, thank you."
    scene ch2ep4_337 with dissolve
    u "The lunch break is about to end."
    u "Let's go back to the company...."
    jump ch2ep4breakend
label ch2ep4breakend:
    scene ch2ep4_338 with dissolve
    if ch2ep4staythenight != 0:
        mc "....................."
        jump ch2ep4arlovisit
    else:
        u "The lunch break is about to end."
        u "Let's go back to the company...."
        jump ch2ep4finishday
label ch2ep4arlovisit:
    scene ch2ep4_339 with dissolve
    play music "sfx/ep4_5.mp3" fadein 3.0
    $ bgm = "RYYZN - Waited (instrumental)"
    s "*Tire sounds*.........."
    mc "....................."
    u "... Why does that car suddenly stop like that?"
    scene ch2ep4_340 with dissolve
    s "*Door closed*......."
    u "Hm....?"
    u "That guy...."
    scene ch2ep4_341 with dissolve
    mc "We meet again..."
    wilson "Yeah. I need you to come with me."
    wilson "The politician wants to meet you."
    mc "..................."
    scene ch2ep4_342 with dissolve
    mc "Did I not make myself clear last night?"
    mc "Which part of my suggestion didn't he understand?"
    wilson "I'm not in a position to answer you that."
    wilson "My duty here is to bring you to him."
    scene ch2ep4_343 with dissolve
    mc "What if I refuse to go?"
    wilson "Then, there is nothing I can do, but to let you leave."
    wilson "But, are you not worried about your friend, [eira]?"
    wilson "I have my men in front of the hospital she is, waiting for my command...."
    mc "........................"
    scene ch2ep4_344 with dissolve
    mc "Alright..."
    mc "I will go meet him."
    wilson "Good choice..."
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    s "*About an hour later*.............."
    scene ch2ep4_345 with fade
    wilson "Follow me...."
    mc "...................."
    scene ch2ep4_346 with dissolve
    wilson "I've brought him here, sir."
    arlo "Well done..."
    scene ch2ep4_347 with dissolve
    arlo "You. Take a seat."
    mc "...................."
    arlo "I won't repeat myself."
    scene ch2ep4_348 with dissolve
    arlo "Good...."
    arlo "You look younger than I expected, boy..."
    mc "...................."
    arlo "What's wrong? Why don't you talk the way you did last night?"
    arlo "Are you scared now?"
    scene ch2ep4_349 with dissolve
    arlo "That's right. You should be scared."
    arlo "Did you really think I'd let you tell me what to do?"
    arlo "Just because you somehow found those documents?"
    arlo "Wake up, kid. I've been through more shit than you thought I would."
    arlo "I'm not someone you can just easily mess with."
    scene ch2ep4_350 with dissolve
    arlo "Well, but I must admit that you impressed me a lot."
    arlo "How did you manage to get those documents?"
    arlo "I'm pretty sure they were kept in a safe place."
    mc "........................"
    arlo "*Sighs*.........."
    scene ch2ep4_351 with dissolve
    arlo "[wilson]."
    wilson "Yes, sir."
    arlo "Since he isn't going to talk, let's end this quickly."
    wilson "Understood."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_352 with dissolve
    mc "..................."
    scene ch2ep4_353 with dissolve
    arlo "Impressive...."
    arlo "The gun is pointing at your head, yet your expression haven't changed a bit."
    arlo "I've never seen anyone like you in my entire life."
    arlo "Are you sure you're just a programmer?"
    scene ch2ep4_354 with dissolve
    mc "*Sighs*................"
    mc "So, this is the decision you made."
    mc "Instead of punishing your daughter, you chose to this path..."
    mc "You could've just taken responsibility for her behaviour...."
    mc "The apple doesn't fall far from the tree. No wonder why your daughter is like that."
    scene ch2ep4_355 with dissolve
    arlo "Only people with no power take responsibility for what they did."
    arlo "But, for people like me, we don't have to do that."
    arlo "You may think it's bullshit, but the world works just like that."
    mc "........................"
    arlo "By the way...."
    scene ch2ep4_356 with dissolve
    arlo "I heard [wilson] giving you such a high praise."
    arlo "Now that I'm watching you behaving so calm in this situation."
    arlo "I'm starting to think it would be such a pity to let you die here."
    arlo "I'm going to give you a chance. Why don't you come work under me?"
    scene ch2ep4_357 with dissolve
    mc "No, I don't want to do that."
    mc "I'm here to remind you of the offer I gave you last night."
    mc "But, looks like it's pointless now."
    mc "What a pity. This problem could've been fixed easily."
    scene ch2ep4_358 with dissolve
    arlo "Yeah? And what are you going to do now?"
    arlo "With the gun pointing at your head like this?"
    arlo "If I tell him to pull the trigger, you die. Just like that."
    arlo "Stop acting so calm already. I know that you're scared."
    mc "Scared? Who? Me?"
    mc "I'm not afraid of dying."
    scene ch2ep4_359 with dissolve
    arlo "*Sighs* I don't know either it's braveness, or stupidity."
    arlo "I really wanted you to work for me."
    arlo "But, looks like it's useless to talk with you now."
    arlo "And if you want to blame someone, blame yourself for going after me."
    scene ch2ep4_360 with dissolve
    stop music fadeout 3.0
    arlo "[wilson]."
    wilson "Yes, sir."
    arlo "We're wasting too much time here. Finish him."
    wilson "Underst-"
    play music "sfx/ep2_8.mp3" fadein 3.0
    $ bgm = "Lahar - Genesis"
    scene ch2ep4_361 with vpunch
    wilson "!!!???"
    mc "................"
    scene ch2ep4_362 with vpunch
    wilson "Ugh...!!"
    scene ch2ep4_363 with vpunch
    wilson "F...Fuck..."
    scene ch2ep4_364 with vpunch
    wilson "Ouch!!!!"
    scene black with dissolve
    scene ch2ep4_365 with dissolve
    mc "..................."
    scene ch2ep4_366 with dissolve
    arlo "W-What the hell just happened?!"
    mc "..................."
    bg1 "P-Protect the politician!"
    scene black with dissolve
    scene ch2ep4_367 with dissolve
    bg2 "Stop right there, or I will fucking shoot you!"
    mc "....................."
    bg1 "(Fuck... I couldn't stop him....)"
    bg1 "(How did he do all that in just a few seconds....?)"
    scene ch2ep4_368 with dissolve
    arlo "N-Now, what are you going to do, huh?"
    arlo "I-If you shoot me, my men will fucking kill you, too!"
    mc "....................."
    arlo "C-Come on! What are you waiting for?! Shoot me if you dare!!"
    scene ch2ep4_369 with dissolve
    mc "What made you think that I'm not going to pull the trigger?"
    mc "Like I said, I'm not afraid of dying."
    mc "What about you? Are you ready to die?"
    arlo "!!!!!!"
    scene ch2ep4_370 with dissolve
    wilson "You fucking idiots! Lower your gun down!"
    bg1 "T-Team leader?"
    wilson "I said lower your fucking gun down!"
    bg2 "B-But...!"
    wilson "The safety of the politician is the first priority!"
    scene ch2ep4_371 with dissolve
    wilson "Don't do something stupid. Lower your gun down."
    bg1 "Tch...!!"
    wilson "Shooting a real human, is different from shooting a practice target."
    wilson "You guys can't pull the trigger, but he can. I can tell that."
    mc "You better listen to your team leader..."
    bg1 "....................."
    scene ch2ep4_372 with dissolve
    bg1 "*Sighs* Fine....!"
    wilson "(That guy, he attacked me before I triggered the safety button.)"
    wilson "(He's not just an ordanary person. Maybe the politician is messing with the wrong guy....)"
    arlo "O-Okay! O-Okay! I surrender!"
    arlo "I'm going to do what you told me to! You'll never see my daughter again!"
    mc "Now, we speak the same language, huh?"
    scene ch2ep4_373 with dissolve
    mc "For your information, I work for [victor]."
    arlo "W-W-What?! Is he-"
    mc "Yeah, he's the one you're thinking about. So, if you want to get your revenge, you better think twice."
    arlo "N-No, I'm not going to do that! O-Only if I knew you worked for him, I wouldn't have caused you such a problem!"
    mc "Great. Now, get up."
    arlo "O-Okay...."
    scene ch2ep4_374 with dissolve
    mc "Walk towards the exit door..."
    mc "And three of you, stay still...."
    mc "If you do anything stupid, I'm going to shoot him."
    arlo "You heard the man! S-Stay still, all of you! Don't move!"
    wilson "Tch....!!!"
    scene ch2ep4_375 with dissolve
    mc "Keep walking...."
    arlo "O-Okay..."
    mc "Hurry up."
    arlo "I-I'm sorry!!"
    scene black with dissolve
    $ renpy.pause()
    s "You've left the place....."
    scene ch2ep4_376 with dissolve
    wilson "What are you guys waiting for?! Follow them!"
    wilson "We've got to make sure that the politician will be unharmed."
    bg2 "Roger that!"
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_377 with dissolve
    mc "Like I said, if you want to get your revenge..."
    mc "I don't need to remind you, right?"
    arlo "No, you don't...."
    arlo "I'm not going to cause you a problem anymore..."
    arlo "Please, forgive me."
    mc "Great. Now, go deal with your daughter..."
    scene black with dissolve
    scene ch2ep4_378 with dissolve
    wilson "Sir! Are you okay?!"
    wilson "You aren't hurt anywhere, right?"
    arlo "Stop fucking ask me a stupid question! Where the hell is [roxy]?!"
    arlo "Bring her to me as soon as you can! Understood?!"
    wilson "Loud and clear, sir."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    jump ch2ep4finishday
label ch2ep4finishday:
    scene black with dissolve
    $ renpy.pause()
    s "You spent time working until evening....."
    scene ch2ep4_379 with fade
    u "Alright...."
    u "It's already 5 p.m."
    u "Let's go home."
    if ch2ep4staythenight != 0:
        play music "sfx/ep4_5.mp3" fadein 3.0
        $ bgm = "RYYZN - Waited (instrumental)"
        scene ch2ep4_380 with dissolve
        s "*Phone vibrates*................"
        u "Hm...?"
        scene ch2ep4_381 with dissolve
        u "Oh... It's him."
        u "I should find somewhere quiet before picking it up."
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep4_382 with dissolve
        mc "................"
        mc ".... Hello?"
        scene ch2ep4_383 with dissolve
        arlo "I've handled the problem."
        arlo "I sent her overseas an hour ago."
        arlo "She should be on the plane now."
        arlo "You and your friend will never see her again."
        scene ch2ep4_384 with dissolve
        arlo "Now that I did what you told me to."
        arlo "Could you please get rid of those documents?"
        scene ch2ep4_385 with dissolve
        mc "Well done, but...."
        mc "I've changed my mind."
        mc "I'm not going to get rid of them."
        scene ch2ep4_386 with dissolve
        arlo "W-What do you mean?! You made a promise!"
        arlo "I did what you told me to, so you should keep your promise, too!"
        arlo "I can't let anyone find those documents at all!"
        scene ch2ep4_387 with dissolve
        mc "I need to keep them just in case your daughter somehow appears before my eyes again."
        mc "So, you better pray that it won't happen."
        mc "But, don't worry. I'll keep them in a safe place."
        mc "No one will ever find out about them."
        mc "I'm hanging up now. Let's hope that we will not need to see each other again."
        stop music fadeout 3.0
        jump ch2ep4beforedaysskip
    else:
        jump ch2ep4beforedaysskip
label ch2ep4beforedaysskip:
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_388 with fade
    play music "sfx/ep2_7.mp3" fadein 3.0
    $ bgm = "AERØHEAD - The Reckoning"
    victor "..................."
    unknown "Excuse me, sir."
    scene ch2ep4_389 with dissolve
    victor "Hm...?"
    victor "What is it?"
    scene ch2ep4_390 with dissolve
    rio "I've just got such a very crucial information."
    rio "Therefore, I'm here to inform you, sir."
    victor "Yeah? What information is it about?"
    rio "The police has been going after us for a while, sir."
    scene ch2ep4_391 with dissolve
    victor "Well, that's not something new."
    victor "We have our people in the police industry, don't we?"
    victor "Just let them handle the problem as always."
    scene ch2ep4_392 with dissolve
    rio "Here is the thing, sir."
    rio "The guy named [felix], is the chief of this operation."
    rio "Not only that his position is quite high, he's well known for his stubbornness."
    rio "No one in the police industry could tell him what to do."
    rio "Even for a police who is higher ranked than him."
    scene ch2ep4_393 with dissolve
    rio "Moreover, he already got rid of some of our people over there."
    victor "Uhm....."
    victor "[felix]? Why have I never heard of a guy like him?"
    scene ch2ep4_394 with dissolve
    victor "Go find out who he is, where he lives, and where he comes from."
    victor "No, actually. Find every information about him."
    victor "No matter how stubborn he is, he has to have some weaknesses."
    victor "I don't believe he doesn't have one."
    rio "Understood, sir."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_395 with dissolve
    victor "......................"
    victor "([felix].....)"
    scene ch2ep4_396 with dissolve
    victor "(It's been a while since someone was going after me.)"
    victor "(It's been so long that I forgot the feelings of those days.)"
    victor "(Now that I'm starting to feel excited again.)"
    victor "(Let's see what you got....)"
    scene black with dissolve
    $ renpy.pause()
    stop music fadeout 3.0
    s "A week later............."
    jump ch2ep4daysskip
label ch2ep4daysskip:
    scene ch2ep4_397 with fade
    play music "sfx/ep2_1.mp3" fadein 3.0
    $ bgm = "Vendredi - Te Amo"
    mc "...................."
    scene ch2ep4_398 with dissolve
    u "I spent so many weeks since I started working at Xecon."
    u "Finally, I managed to draw the building structure."
    u "Especially, the floor that the lab is located at."
    u "Now, I need to remember every single detail on that floor."
    u "Specifically, where all CCTVs are so that I can delete every footage in case I get caught by one of them..."
    scene ch2ep4_399 with dissolve
    s "*Phone vibrates*................."
    u "Hm...? It's [angela]?"
    u "Why is she calling me on Saturday morning like this?"
    scene ch2ep4_400 with dissolve
    mc "....................."
    mc ".... Hello?"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_401 with fade
    angela "Good morning, [mc]."
    angela "I hope I didn't wake you up."
    scene ch2ep4_400 with dissolve
    mc "No, you didn't."
    mc "I've been up for some time already."
    scene ch2ep4_401 with dissolve
    angela "What a relief...."
    angela "I was thinking if I should've called you, but I couldn't have waited any longer."
    scene ch2ep4_402 with dissolve
    mc "Why's that?"
    mc "Is there something important I needed to know?"
    scene ch2ep4_403 with dissolve
    angela "Yes, there is."
    angela "Last night, the president told me to call you and ask if you are free this evening."
    angela "But, I was so tired that I fell asleep as soon as I got home."
    scene ch2ep4_402 with dissolve
    mc "I see...."
    mc "This evening...? I'm not sure."
    mc "Why do you ask?"
    scene ch2ep4_405 with dissolve
    angela "The president wanted to invite you for dinner."
    angela "If it's not too much to ask...."
    angela "Could you clear your schedule.... for me, please?"
    angela "She told me to ask you since last night, but I was really tired."
    angela "Please accept my apologies...."
    scene ch2ep4_404 with dissolve
    mc "Well...."
    mc "Okay, I think I can go have dinner with her this evening."
    mc "And there is no need to apologise. It's totally understandable."
    scene ch2ep4_406 with dissolve
    angela "Thank you. Thank you so much."
    angela "I will inform the president right away."
    angela "Have a great day, sir."
    $ angela_relationship += 2
    $ angela_ch2_ep4 += 2
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_407 with dissolve
    u "It's already been a week since I did the DNA test."
    u "I guess she wants to talk about that this evening."
    u "That's why she invited me..."
    scene ch2ep4_408 with dissolve
    u "*Sighs* Alright...."
    u "Let's continue studying the structure."
    u "I need to remember everything so that I don't screw up..."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    s "*Later that evening*........."
    $ renpy.pause()
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene ch2ep4_409 with dissolve
    u "Alright, it's about time."
    u "[angela] told me that she will come to pick me up at five in the evening."
    u "Now, it's five to five. I should go wait her in front of the house."
    scene black with dissolve
    scene ch2ep4_410 with dissolve
    angela "Good evening, [mc]."
    u "Hm? She's already here?"
    mc "Good evening. You're here quite early."
    scene ch2ep4_411 with dissolve
    mc "How long have you been waiting?"
    angela "Not that long. I literally just arrived here a minute before you came out."
    angela "By the way, I'm glad to see you here. And thank you for accepting my request."
    angela "Even though I already told you that on the phone, I still want to tell you again in person."
    mc "Well, it's not a big deal..."
    menu:
        "You look good [angela1]":
            $ angela_relationship += 1
            $ angela_ch2_ep4 += 1
            $ ch2ep4complimentangela = 1
            scene ch2ep4_412 with dissolve
            mc "You look good today."
            angela "Hm...? All of sudden?"
            angela "I always dress like this when working, but thanks for the compliment though."
        "Say nothing":
            $ ch2ep4complimentangela = 2
            mc ".................."
    scene ch2ep4_413 with dissolve
    mc "Where is my m...."
    mc "Where is [maya] by the way? I don't see her here."
    angela "She went to pick up [skylar] at the university. We will meet her at the restaurant."
    mc "I see. Let's go then."
    angela "Sure thing."
    scene black with dissolve
    $ renpy.pause()
    s "*An hour later*.............."
    scene ch2ep4_414 with fade
    angela "President."
    maya "Oh, there you guys are..."
    scene ch2ep4_415 with dissolve
    angela "I've brought him here, president."
    maya "Appreciated it, [angela]."
    maya "Please take a seat. Both of you."
    angela "Thank you for your kindness, but..."
    scene ch2ep4_416 with dissolve
    angela "I'll go find something to eat outside."
    maya "Hm? Why's that?"
    angela "I think I should leave you all some time alone."
    maya "Okay, I get it. I'll call you once we finish eating then."
    angela "Understood. Please, have a great time."
    scene black with dissolve
    scene ch2ep4_417 with dissolve
    maya "Good evening, [mc]."
    skylar "Hello, [mc]."
    mc "Good evening."
    maya "How have you been?"
    mc "Pretty good, and you?"
    maya "Me, too."
    scene ch2ep4_418 with dissolve
    mc "What about you, [skylar]?"
    mc "I heard you went to the university today. How was it?"
    skylar "Yeah, I had a lecture class today. It was a little bit tiring...."
    skylar "But fortunately, the professor was funny, so the class was not boring at all."
    mc "That's great for you."
    scene ch2ep4_419 with dissolve
    mc "[maya]."
    maya "Yes?"
    mc "I assume that you've already got the DNA test, right?"
    mc "That's why you invited me here."
    scene ch2ep4_420 with dissolve
    maya "Yeah, you're right. I've already got it."
    maya "Here you are. Have a look."
    mc "Thank you."
    scene ch2ep4_421 with dissolve
    maya "*Smiles* Even though I knew from the start that you're my son, I was still so nervous when I was about to see the result..."
    u "The document stated that the probability of maternity is 99.9998 percent...."
    mc "..................."
    u "So, that means she is really my birth mother...?"
    scene ch2ep4_422 with dissolve
    maya "[mc]...?"
    mc "... Yeah?"
    maya "What's wrong? Why were you so silent out of sudden?"
    mc "It's just...."
    mc "I don't know what I should say...."
    scene ch2ep4_423 with dissolve
    mc "Deep down I know that you're my mother. And this paper is the proof of that fact."
    mc "But the truth is, I grew up without you. I had no memory about you before."
    mc "So, it's very hard for me to suddenly accept you...."
    maya "It's alright. I totally understand you."
    maya "Don't feel too pressured. I'm not going to force you to act like I'm your mother all of sudden."
    maya "Just like I've always said, feel free to take as much time as you want."
    mc "Thank you for saying that. It means a lot...."
    scene ch2ep4_424 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_424.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_424_blink.jpg", 1) with dissolve
    maya "Let's start with getting to know each other better."
    maya "Is there something you want to ask me and [skylar]?"
    jump ch2ep4qa
label ch2ep4qa:
    menu:
        "What made you decide to build a perfume company?":
            mc "What made you decide to build a perfume company?"
            scene ch2ep4_425 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_425.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_425_blink.jpg", 1) with dissolve
            maya "Well...."
            maya "I've always had a passion for perfumes since before I met your father."
            maya "So, after he passed away, I started with inventing my own makeup as a hobby."
            maya "However, the feedback was so good that I decided to launch a company. It started from a very small company, then became one of the best cosmetic company for the past few years."
            scene ch2ep4_424 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_424.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_424_blink.jpg", 1) with dissolve
            jump ch2ep4qa
        "What's your plan for the future, [skylar]?":
            mc "What's your plan for the future, [skylar]?"
            scene ch2ep4_426 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_426.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_426_blink.jpg", 1) with dissolve
            skylar "My plan for the future...?"
            skylar "Well... Right now I'm a third-year student. I'm studying chemistry as my major."
            skylar "I've always had a passion for fragrant things like flowers, trees, especially perfumes."
            skylar "So, my dream is to create as many high quality perfumes as I can."
            scene ch2ep4_424 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_424.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_424_blink.jpg", 1) with dissolve
            jump ch2ep4qa
        "What would you do if...":
            mc "What would you do if someone you think you know him or her turns out to be a different person?"
            scene ch2ep4_425 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_425.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_425_blink.jpg", 1) with dissolve
            maya "Umm... That's an interesting question."
            maya "I think it depends on what kind of person he truely is. If he's a good, then I will still get in touch with him."
            maya "But if he's a bad person and has done something bad, I would want to know the reason behind that before I can judge him."
            scene ch2ep4_426 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_426.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_426_blink.jpg", 1) with dissolve
            skylar "For me, I share the same idea as my mother..."
            mc "I see..."
            jump ch2ep4qa
        "Next":
            jump ch2ep4dinnercontinue
label ch2ep4dinnercontinue:
    scene ch2ep4_427 with dissolve
    maya "Let's talk about you now. I want to know you better."
    skylar "Me, too."
    maya "Would you mind telling us more about yourself?"
    mc "About myself?"
    maya "Yes. Like what kind of person do you think you are, and what made you decide to work for Xecon."
    mc "...................."
    scene ch2ep4_428 with dissolve
    mc "Well...."
    mc "I think I'm a determined person. If I'm told to do something, I will do it until it succeeds no matter what."
    maya "That's a very good trait to have."
    mc "But I'm bad at expressing feelings. Sometimes I don't know what I should say, or do in a specific situation."
    skylar "*Smiles* I could tell that..."
    scene ch2ep4_429 with dissolve
    mc "And what made I decided to work for Xecon, right?"
    maya "Yeah... I kind of wonder since it's like a miracle that we've finally met again."
    maya "And it's all because you're working for Xecon."
    mc "........................"
    u "Well, I can't tell her the truth..."
    mc "I didn't have a lot of friends since I was young."
    mc "Games were like my friends. I spent time playing a lot of games."
    mc "So, I've always been interested in gaming industry. Xecon is one of the best game companies, so I decide to apply for the job there."
    maya "That makes a lot of sense..."
    scene ch2ep4_430 with dissolve
    maya "Alright, I think it's about time now."
    maya "Let's just order something to eat first."
    maya "What's your favorite food, [mc]?"
    mc "Umm... Actually I can eat everything. What's the recommended menu here?"
    skylar "Smoked Salmon Steak. It's very delicious. You should try it."
    mc "Thank you, [skylar]. I will try it."
    scene black with dissolve
    $ renpy.pause()
    s "You spent your time having dinner with [maya] and [skylar]..........."
    scene ch2ep4_431 with dissolve
    maya "Sweetheart."
    skylar "Yes, mom?"
    maya "Would you mind going home with [angela] first?"
    skylar "No, I wouldn't... But, where are you going to go?"
    scene ch2ep4_432 with dissolve
    maya "I will take [mc] home. I have something to talk with him."
    mc "Hm? Me?"
    maya "You're okay with that, right?"
    mc "Yeah, if that's what you want."
    scene ch2ep4_433 with dissolve
    maya "[angela]."
    angela "Yes, president?"
    maya "Please, take [skylar] home safe."
    angela "Do you want me to go with you?"
    angela "I'm sure [mrw] can take her home alone."
    scene ch2ep4_434 with dissolve
    maya "Thank you, but don't worry about me."
    maya "I want to have some time alone with [mc]."
    angela "Understood."
    scene ch2ep4_435 with dissolve
    skylar "Alright then, see you later, [mc]."
    skylar "It was nice spending time with you."
    skylar "Have a good night. Bye-bye."
    scene ch2ep4_436 with dissolve
    mc "It was nice spending time with you, too."
    mc "Good bye, [skylar]."
    maya "(Oh, look how cute they are...)"
    maya "(To see them get along well, is the best thing I could've asked so far...)"
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep2_7.mp3" fadein 3.0
    $ bgm = "AERØHEAD - The Reckoning"
    scene ch2ep4_437 with fade
    maya "Okay... We're arrived."
    mc "Yeah...."
    scene ch2ep4_438 with dissolve
    mc "Thank you for taking me home, [maya]."
    mc "Also thanks for today. The food was nice."
    maya "All good. I'm glad to hear that."
    scene ch2ep4_439 with dissolve
    mc "By the way, what's that something you wanted to talk with?"
    mc "You said you wanted to talk with me, but we still haven't talked about it yet."
    maya "Oh... yeah, we're supposed to talk about that. I almost forgot."
    maya "Well... I know that [victor] adopted you, but I don't know how close you are to him."
    maya "I mean... do you know what kind of person he really is...?"
    scene ch2ep4_440 with dissolve
    mc "......................."
    mc "Yeah, I guess I'm kind of close to him."
    scene ch2ep4_441 with dissolve
    maya "Like... father and son?"
    scene ch2ep4_440 with dissolve
    mc "I don't think [victor] and I have that kind of relationship."
    mc "He's more likely my benefactor."
    scene ch2ep4_441 with dissolve
    maya "I see...."
    mc "Why did you ask about that by the way?"
    maya "Well... The thing is, a few days ago I was informed a crucial information about your father."
    mc "My father?"
    scene ch2ep4_442 with dissolve
    maya "Yeah..."
    maya "I told you that he passed away because of an accident, right?"
    mc "Yes, that's what you told me."
    maya "I was told that it wasn't an accident, but a murder."
    scene ch2ep4_443 with dissolve
    mc ".... What?"
    mc "Who told you that?"
    maya "A police. His name is [felix]."
    maya "He also showed me the evidence. It's an audio file."
    scene ch2ep4_444 with dissolve
    maya "I played that file and found out that the culprit was hired to kill your father."
    mc "........................."
    mc ".... By whom?"
    maya ".... A guy named [rio]. [felix] told me that he's the butler that has been working for [victor] for more than 20 years."
    mc "........................"
    scene ch2ep4_445 with dissolve
    mc "What the....?"
    maya "Hey, are you alright...?"
    mc "......................."
    scene ch2ep4_446 with dissolve
    mc "Thank you for taking me home. I'm leaving now."
    maya "Wait...."
    maya "If you don't believe me. I can arrange you a meeting with [felix]."
    mc "I...."
    mc "I need some time to think. Good bye, [maya]."
    scene ch2ep4_447 with dissolve
    maya "(My poor son....)"
    maya "(I'm worried about him, but there is nothing I can do now.)"
    maya "(He hasn't fully opened up to me yet.)"
    maya "(I guess I can only give him time like he said.)"
    scene black with dissolve
    $ renpy.pause()
    s "*An hour later*..............."
    scene ch2ep4_448 with fade
    mc "......................"
    u "Ugh... My head...."
    scene ch2ep4_449 with dissolve
    u "I can't believe my father was killed like that...."
    u "Even though I had no memory about him, I feel so pissed right now."
    u "Did [rio] really hire that culprit to kill my father? That's impossible. Why would he have done that?"
    u "But, [maya] didn't seem like lying to me though."
    u "Was it [victor] who told [rio] to hire the culprit? I don't think [rio] would've done something like that on his own...."
    scene ch2ep4_450 with dissolve
    u "Ugh...."
    u "I can't believe I've been working for a guy who basically destroyed my life...."
    u "What am I supposed to do now...?"
    u "........................."
    scene ch2ep4_451 with dissolve
    u "*Sighs* Well...."
    u "I think I should call [maya]."
    scene ch2ep4_452 with dissolve
    u "I need to meet [felix] to hear and see everything by my own."
    mc "....................."
    scene ch2ep4_453 with dissolve
    mc "Hi, [maya]. It's me, [mc]."
    mc "Have you arrived home yet?"
    scene ch2ep4_454 with dissolve
    maya "Yeah, I've just arrived home like five minutes ago."
    maya "I didn't expect you to call me at all. What's going on?"
    maya "Is there something I can help you with?"
    scene ch2ep4_455 with dissolve
    mc "About what we talked earlier...."
    mc "You said that you heard everything from the police named [felix], right?"
    scene ch2ep4_454 with dissolve
    maya "That's right. He made an appointment to meet me at my office."
    maya "At first I was confused why the police wanted to meet me."
    maya "To be honest I felt very sad after hearing everything from him, but I also felt happy as well."
    maya "Even though we thought your father passed away by accident, some people said that he committed a suicide because he couldn't pay for the debt."
    maya "Yeah, he changed into a different person and became an alcoholic, but deep down I knew he wasn't that kind of person who would avoid trouble like that."
    scene ch2ep4_455 with dissolve
    mc "...................."
    mc "Can you arrange me a meeting with [felix], please?"
    scene ch2ep4_456 with dissolve
    maya "Sure, of course I can."
    maya "Thank you for asking me that. I will try to reach him, then I will tell you the date and time as soon as he agrees to meet you."
    scene ch2ep4_453 with dissolve
    mc "Thank you so much."
    mc "Alright, that'd be all. Good night, [maya]."
    scene ch2ep4_456 with dissolve
    maya "Okay. You, too."
    scene black with dissolve
    scene ch2ep4_457 with dissolve
    mc "..................."
    u "It's getting late now...."
    u "Let's go take a shower before sleep."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_458 with fade
    rin "Oh...?! Hello, [mc]."
    mc "Hi, [rin]. What are you doing here?"
    rin "I'm going to take a shower. The bathroom on the first floor is occupied."
    rin "Are you about to use this one?"
    scene ch2ep4_459 with dissolve
    mc "Yeah...."
    rin "Hm...? What happened?"
    mc "What do you mean?"
    rin "You look so sad right now."
    mc "Do I?"
    rin "Yeah, you do! What's going on?"
    mc "......................."
    if ch2ep1rinsex == 1:
        scene ch2ep4_460 at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_460.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_460_blink.jpg", 1) with dissolve
        rin "You know what? Forget it."
        rin "If you don't feel like telling me, I'm not going to force you."
        mc "Okay...."
        rin "But why don't we take a shower together?"
        rin "I'll accompany you and make you feel better."
        rin "That sounds good, right? What do you say?"
        menu:
            "Take a shower with [rin] [rin1]":
                $ ch2ep4showerwithrin = 1
                $ rin_relationship += 1
                $ rin_ch2_ep4 += 1
                scene ch2ep4_461_a with dissolve
                mc "How are you going to make me feel better though?"
                rin "*Giggles* Why don't you join me and see it yourself?"
                mc "Alright, let's do it."
                rin "*Giggles* Let's get in the bathroom then!"
                jump ch2ep4bathewithrin
            "Refuse to do so":
                $ ch2ep4showerwithrin = 2
                scene ch2ep4_461_d with dissolve
                mc "Thank you for caring for me. I really do."
                mc "But I don't feel like doing it now. I'm sorry."
                rin "Alright, if you say so."
                rin "Like I said earlier, I'm not going to force you to do something you don't want to."
                rin "Good night, [mc]."
                mc "Good night, [rin]."
                scene black with dissolve
                $ renpy.pause()
                s "You waited until [rin] finished taking a shower, then you spent your time cleaning up yourself....."
                jump ch2ep4weirdnoise
    else:
        mc "Nothing. You can get in first."
        mc "I'll take a shower after you finish."
        rin "Okay, then."
        stop music fadeout 3.0
        scene black with dissolve
        $ renpy.pause()
        s "You waited until [rin] finished taking a shower, then you spent your time cleaning up yourself....."
        jump ch2ep4weirdnoise
label ch2ep4bathewithrin:
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
    play music "sfx/ep2_4.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - Out of Time"
    scene ch2ep4_462 with fade
    rin "*Giggles* To be honest... I'm getting embarrassed now."
    rin "I've never done something like this."
    rin "But I'd rather feel embarrassed than see you sad."
    mc "That's very sweet of you...."
    scene ch2ep4_463 with dissolve
    rin "Alright...."
    rin "Before taking a bath, we have to undress first, right?"
    rin "I'll undress myself. You undress yourself, too."
    scene ch2ep4_464 with dissolve
    $ renpy.pause()
    scene ch2ep4_465 with dissolve
    $ renpy.pause()
    scene ch2ep4_466 with dissolve
    rin "Alright, I took everything off now."
    rin "Wait. Why haven't you undressed yet?"
    mc "I'm sorry. I was busy watching you, so...."
    rin "*Giggles* Did you enjoy what you were watching?"
    mc "... Yeah."
    scene ch2ep4_467 with dissolve
    rin "Come on. I don't want to be the only one naked here."
    rin "Put your arms up. I'll help you undress."
    mc "As you please...."
    scene ch2ep4_468 with dissolve
    rin "Ugh... I can't take it off. You'll have to do it by your own."
    mc "Didn't you say you'd help me undress?"
    rin "Yeah, but... you're too tall."
    mc "It's fine. I was just teasing you. I'll take it off myself."
    scene ch2ep4_469 with dissolve
    mc "Okay... Now what?"
    rin "*Giggles* Hehe...."
    scene ch2ep4_470 with dissolve
    $ renpy.pause()
    scene ch2ep4_471 with dissolve
    show ch2ep4_rin1 with dissolve
    rin "*Kisses* It's been a while...."
    rin "*Kisses* Mmmm... I miss the touch of your lips so much...."
    mc "*Kisses* Me, too..."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin1
    scene black with dissolve
    scene ch2ep4_472 with dissolve
    rin "*Smiles* What do you want me to do, master?"
    mc "Master...?"
    rin "*Giggles* Yeah, I'm going to make you feel better, so you're my master now."
    mc "I never knew you had this side of yours."
    rin "*Giggles* So, what do you want me to do for you, master?"
    mc "How about using your boobs to make me feel good?"
    rin "*Smiles* As you wish, master."
    scene ch2ep4_473 with dissolve
    show ch2ep4_rin2 with dissolve
    rin "How does it feel, master?"
    rin "Are my boobs making you feel great?"
    mc "Absolutely...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin2
    scene ch2ep4_474 with dissolve
    show ch2ep4_rin3 with dissolve
    rin "Am I doing good, master?"
    mc "Yes, you are. Keep doing what you're doing."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin3
    scene ch2ep4_475 with dissolve
    show ch2ep4_rin4 with dissolve
    rin "Can you promise me one thing, master?"
    mc "... Hm? What do you want?"
    rin "Promise me that you won't feel sad any longer after this."
    mc ".... Yeah, sure."
    rin "*Smiles* That's all I need to hear."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin4
    scene ch2ep4_476 with dissolve
    show ch2ep4_rin5 with dissolve
    rin "*Sucks* Mmmmm.... It's been a while, master..."
    rin "*Sucks* I almost forgot how big you are...."
    mc "I almost forgot how good it feels when you're doing this to me, too..."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin5
    scene ch2ep4_477 with dissolve
    show ch2ep4_rin6 with dissolve
    rin "*Sucks* Mmmm.... Tell me if you want me to do it faster or slower, master..."
    mc "Ahh... Faster. I want you to do it faster..."
    rin "*Sucks* Mmmmm.... As you wish."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin6
    scene ch2ep4_478 with dissolve
    show ch2ep4_rin7 with dissolve
    rin "*Sucks* Mmmmm.... Am I doing it fast enough?"
    rin "*Sucks* Mmmmm.... Are you satisfied now, master?"
    mc "*Softly breathes* Yeah.... I'm about to cum now."
    rin "*Sucks* Mmmmm.... Go ahead, master. Please, cum in my mouth."
    $ renpy.pause()
    menu:
        "Cum":
            hide ch2ep4_rin7
    scene ch2ep4_479 with vpunch
    mc "Ugh! I'm cumming....!"
    scene ch2ep4_479 with vpunch
    rin "Mmmmmm.....!!!!"
    scene black with dissolve
    scene ch2ep4_480 with dissolve
    rin ".................."
    scene ch2ep4_481 with dissolve
    rin "*Smiles* You came quite a lot. Hehe..."
    rin "I guess you've kept it quite some time, right?"
    mc "...................."
    rin "Hey. It's kind of hot. I'm getting sweaty now."
    rin "Let's get in the tub. Shall we?"
    mc "Sure thing."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_482 with dissolve
    rin "Well....."
    rin "I never realize this tub is very small until now."
    rin "We almost couldn't fit in."
    mc "Maybe it's designed for one person?"
    rin "*Giggles* I guess so."
    scene ch2ep4_483 with dissolve
    mc "To think about it, I haven't spent much time with you recently."
    rin "Right?"
    mc "How have you been?"
    rin "Pretty great I'd say. I'm enjoying my life right now."
    rin "There were some time I felt a little bit tired because of work, but that's just how life works, doesn't it?"
    mc "I couldn't agree more."
    scene ch2ep4_484 with dissolve
    rin "*Giggles* Well. Well. Well...."
    rin "*Giggles* Looks like {b}the little you{/b} want to join our conversation."
    rin "*Giggles* While we were talking, someone just got an erection."
    rin "*Giggles* I never knew you were such a naughty boy...."
    mc "Well.... It couldn't be helped. You were grinding on it all the time...."
    scene black with dissolve
    scene ch2ep4_485 with dissolve
    rin "*Smiles* You're ready for round two, master?"
    mc "Yeah. Pretty much like that."
    rin "And what you want me to do for you? How can I please you, master?"
    mc "I don't know. Why don't you decide?"
    rin "Well then..."
    scene ch2ep4_486 with dissolve
    rin "I wanted to try doing this for some time."
    rin "I don't know if it's going to be good, but I'll try my best."
    mc "Okay. Don't pressure yourself."
    rin "*Giggles* Got it!"
    scene ch2ep4_487 with dissolve
    show ch2ep4_rin8 with dissolve
    rin "How does it feel, master?"
    mc "I don't know... Weird, but good at the same time I guess?"
    rin "*Giggles* I guess I'm doing it right then!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin8
    scene ch2ep4_488 with dissolve
    show ch2ep4_rin9 with dissolve
    mc "Ahh...."
    rin "Should I do it faster, master?"
    mc "Yeah... Do it faster."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin9
    scene ch2ep4_489 with dissolve
    show ch2ep4_rin10 with dissolve
    rin "*Giggles* Well, I must say that I'm enjoy doing this a lot more than I thought."
    rin "It's pretty fun moving my legs like this... Hehe..."
    mc "I think that's enough teasing...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin10
    scene ch2ep4_490 with dissolve
    rin "Yeah? Then, what are we going to do next?"
    mc "Come closer. I want you to sit on me."
    rin "*Giggles* As you wish, master!"
    scene ch2ep4_491 with dissolve
    rin "Okay...."
    rin "I'm going to put it in now...."
    scene ch2ep4_492 with dissolve
    mc "Ugh... You're so tight...."
    rin "Ahh.... It's... because.... you're too big...."
    scene ch2ep4_493 with dissolve
    show ch2ep4_rin11 with dissolve
    rin "*Softly breathes* Ahhh.... [mc]....."
    rin "*Softly breathes* It hurts a little bit.... It's so big...."
    mc "*Softly breathes* Relax. Keep this pace until you feel more comfortable...."
    menu:
        "Next":
            hide ch2ep4_rin11
    scene ch2ep4_494 with dissolve
    show ch2ep4_rin12 with dissolve
    rin "*Softly breathes* Mhmmmm.... It's getting better now...."
    rin "*Softly breathes* Ahhh.... Your cock keeps touching my womb... It feels so good...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin12
    scene ch2ep4_495 with dissolve
    show ch2ep4_rin13 with dissolve
    mc "*Heavily breathes* Arrr.... You're so much better than the last time we did, [rin]...."
    rin "*Heavily breathes* Mmmmm... Don't... say something like that...."
    rin "*Heavily breathes* You're... making me... embarrassed...."
    $ renpy.pause()
    menu:
        "Next":
            mc "Hold on. Let me do it for you now."
            rin "*Softly breathes* Okay...."
            hide ch2ep4_rin13
    scene black with dissolve
    scene ch2ep4_496 with dissolve
    rin "Aw...!!"
    rin "*Giggles* Are you sure you want to do it in this position? I'm quite heavy, you know?"
    mc "No, you aren't...."
    rin "*Giggles* Hehe... You're so strong, master!"
    scene ch2ep4_497 with dissolve
    rin "A-Ahhh...!! Y-You...!!"
    mc "Hm? What?"
    rin "You should've told me before putting it in...."
    mc "Does it feel bad?"
    rin "*Giggles* Absolutely not. It's just... Forget it. Just do whatever you want, master."
    scene ch2ep4_498 with dissolve
    show ch2ep4_rin14 with dissolve
    mc "How does it feel?"
    rin "*Softly breathes* Ahhh... Great. Don't stop. I love it, master."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin14
    scene ch2ep4_499 with dissolve
    show ch2ep4_rin15 with dissolve
    rin "*Softly breathes* Mmmmm.... Ahhhh....."
    rin "*Softly breathes* To be honest.... It feels a little bit.... weird doing it in this posion, but...."
    rin "*Softly breathes* It feels so great.... Please, do it faster, master!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep4_rin15
    scene ch2ep4_500 with dissolve
    show ch2ep4_rin16 with dissolve
    rin "*Heavily breathes* Ahhhh...! Mmmmmm...!"
    rin "Heavily breathes* M-Master...! I-I'm about to cum...!"
    mc "*Softly breathes* Me, too...!"
    $ renpy.pause()
    menu:
        "Footjob":
            hide ch2ep4_rin16
            jump ch2ep4bathe_footjob1
        "Reverse cowgirl":
            hide ch2ep4_rin16
            jump ch2ep4bathe_reversecow1
        "Slowest":
            hide ch2ep4_rin16
            jump ch2ep4bathe_lift1
        "Slower":
            hide ch2ep4_rin16
            jump ch2ep4bathe_lift2
        "Cum":
            jump ch2ep4bathecum
label ch2ep4bathe_footjob1:
    scene ch2ep4_487 with dissolve
    show ch2ep4_rin8 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Reverse cowgirl":
            hide ch2ep4_rin8
            jump ch2ep4bathe_reversecow1
        "Lifting":
            hide ch2ep4_rin8
            jump ch2ep4bathe_lift1
        "Faster":
            hide ch2ep4_rin8
            jump ch2ep4bathe_footjob2
        "Fastest":
            hide ch2ep4_rin8
            jump ch2ep4bathe_footjob3
label ch2ep4bathe_footjob2:
    scene ch2ep4_488 with dissolve
    show ch2ep4_rin9 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Reverse cowgirl":
            hide ch2ep4_rin9
            jump ch2ep4bathe_reversecow1
        "Lifting":
            hide ch2ep4_rin9
            jump ch2ep4bathe_lift1
        "Slower":
            hide ch2ep4_rin9
            jump ch2ep4bathe_footjob1
        "Faster":
            hide ch2ep4_rin9
            jump ch2ep4bathe_footjob3
label ch2ep4bathe_footjob3:
    scene ch2ep4_489 with dissolve
    show ch2ep4_rin10 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Reverse cowgirl":
            hide ch2ep4_rin10
            jump ch2ep4bathe_reversecow1
        "Lifting":
            hide ch2ep4_rin10
            jump ch2ep4bathe_lift1
        "Slowest":
            hide ch2ep4_rin10
            jump ch2ep4bathe_footjob1
        "Slower":
            hide ch2ep4_rin10
            jump ch2ep4bathe_footjob2
label ch2ep4bathe_reversecow1:
    scene ch2ep4_493 with dissolve
    show ch2ep4_rin11 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Footjob":
            hide ch2ep4_rin11
            jump ch2ep4bathe_footjob1
        "Lifting":
            hide ch2ep4_rin11
            jump ch2ep4bathe_lift1
        "Faster":
            hide ch2ep4_rin11
            jump ch2ep4bathe_reversecow2
        "Fastest":
            hide ch2ep4_rin11
            jump ch2ep4bathe_reversecow3
label ch2ep4bathe_reversecow2:
    scene ch2ep4_494 with dissolve
    show ch2ep4_rin12 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Footjob":
            hide ch2ep4_rin12
            jump ch2ep4bathe_footjob1
        "Lifting":
            hide ch2ep4_rin12
            jump ch2ep4bathe_lift1
        "Slower":
            hide ch2ep4_rin12
            jump ch2ep4bathe_reversecow1
        "Faster":
            hide ch2ep4_rin12
            jump ch2ep4bathe_reversecow3
label ch2ep4bathe_reversecow3:
    scene ch2ep4_495 with dissolve
    show ch2ep4_rin13 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Footjob":
            hide ch2ep4_rin13
            jump ch2ep4bathe_footjob1
        "Lifting":
            hide ch2ep4_rin13
            jump ch2ep4bathe_lift1
        "Slowest":
            hide ch2ep4_rin13
            jump ch2ep4bathe_reversecow1
        "Slower":
            hide ch2ep4_rin13
            jump ch2ep4bathe_reversecow2
label ch2ep4bathe_lift1:
    scene ch2ep4_498 with dissolve
    show ch2ep4_rin14 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Footjob":
            hide ch2ep4_rin14
            jump ch2ep4bathe_footjob1
        "Reverse cowgirl":
            hide ch2ep4_rin14
            jump ch2ep4bathe_reversecow1
        "Faster":
            hide ch2ep4_rin14
            jump ch2ep4bathe_lift2
        "Fastest":
            hide ch2ep4_rin14
            jump ch2ep4bathe_lift3
label ch2ep4bathe_lift2:
    scene ch2ep4_499 with dissolve
    show ch2ep4_rin15 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Footjob":
            hide ch2ep4_rin15
            jump ch2ep4bathe_footjob1
        "Reverse cowgirl":
            hide ch2ep4_rin15
            jump ch2ep4bathe_reversecow1
        "Slower":
            hide ch2ep4_rin15
            jump ch2ep4bathe_lift1
        "Faster":
            hide ch2ep4_rin15
            jump ch2ep4bathe_lift3
label ch2ep4bathe_lift3:
    scene ch2ep4_500 with dissolve
    show ch2ep4_rin16 with dissolve
    $ renpy.pause()
    menu:
        "Footjob":
            hide ch2ep4_rin16
            jump ch2ep4bathe_footjob1
        "Reverse cowgirl":
            hide ch2ep4_rin16
            jump ch2ep4bathe_reversecow1
        "Slowest":
            hide ch2ep4_rin16
            jump ch2ep4bathe_lift1
        "Slower":
            hide ch2ep4_rin16
            jump ch2ep4bathe_lift2
        "Cum":
            jump ch2ep4bathecum
label ch2ep4bathecum:
    mc "*Softly breathes* I'm about to cum...."
    rin "*Heavily breathes* Me, too...! Let's cum together, master!"
    menu:
        "Cum inside":
            scene ch2ep4_501_in with vpunch
        "Cum outside":
            scene ch2ep4_501_out with vpunch
    mc "I'm cumming!!!"
    scene ch2ep4_502 with vpunch
    rin "*Heavily breathes* Ahhhhhh...!!!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_503 with dissolve
    rin "*Pants* That was so great....."
    mc "Yeah.... That's right."
    rin "*Pants* Let's stay... like this for... a little bit...."
    mc "Okay...."
    $ rin_relationship += 2
    $ rin_ch2_ep4 += 2
    $ renpy.end_replay()
    jump ch2ep4bathecontinue
label ch2ep4bathecontinue:
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_504 with dissolve
    rin "*Hums a song* Hmmm~"
    rin "So, are you feeling better now, [mc]?"
    mc "Yeah... Thanks to you."
    scene ch2ep4_505 with dissolve
    rin "[mc]..."
    mc "Yes?"
    rin "Do you mind telling me what happened? What made you sad?"
    rin "Don't get me wrong though. It's not like I'm forcing you, it's... I want you to know that I'm willing to listen if you want to tell me."
    rin "Who knows you might feel better after getting something off your chest."
    rin "But if you don't want to, it's completely fine. I respect your decision."
    mc "........................"
    $ renpy.pause()
    menu:
        "Okay... [rin3]":
            $ ch2ep4tellrin = 1
            $ rin_relationship += 3
            $ rin_ch2_ep4 += 3
            scene ch2ep4_506_a1 with dissolve
            mc "Can I ask you something?"
            rin "*Smiles* Of course, you can."
            rin "What is it?"
            scene ch2ep4_506_a2 with dissolve
            mc "Well...."
            mc "What would you do if someone, whom you thought was your benefactor, happened to be the person that did something that effected your life badly?"
            rin "Umm... That's quite a hard question."
            rin "You said that he did something that effected your life badly, right?"
            mc "Yeah, why?"
            rin "I'm wondering like.... how bad the effect was."
            scene ch2ep4_506_a3 with dissolve
            mc "I'd say it changed my life completely."
            mc "Not in a good way though."
            rin "Well.... Now, I get why you looked so sad."
            rin "To be honest I have never been in such a situation like yours, so I don't know if I can give you a good advice. But, I'll try my best."
            rin "If I were you, I'd slowly bring myself out of his life. Even if he said that he meant well, I wouldn't believe him. It doesn't make sense at all."
            mc "I see...."
            scene ch2ep4_506_a4 with dissolve
            rin "That's just my opinion though. You don't need to follow it if you don't feel comfortable to."
            rin "Just be yourself, okay? I know you can get through it."
            mc "(It won't be that easy though....)"
            mc ".... Thank you for saying that."
            scene ch2ep4_506_a5 with dissolve
            rin "And if you ever need my help, don't be hesitate to come to me."
            rin "I don't know if I could help you, but I will try my best."
            mc "That's very kind of you...."
            rin "Alright... I hope you feel a little bit better now."
            rin "Let's enjoy our time for a little bit longer before we leave, shall we?"
            mc "Yeah, sure."
        "I'm sorry":
            $ ch2ep4tellrin = 2
            scene ch2ep4_506_d with dissolve
            mc "I'm really sorry, [rin]."
            mc "It's not like I don't want to tell you. I'm just not ready...."
            rin "It's alright. There is no need for you to say sorry at all."
            rin "Like I said earlier, I respect your decision."
            mc "Thank you."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time taking a bath with [rin]....."
    scene ch2ep4_507 with dissolve
    rin "I wish we could stay in there for a little bit more, but it's almost midnight now."
    rin "I should get to bed already."
    mc "Me either. Today has been such a long day."
    scene ch2ep4_508 with dissolve
    rin "*Smiles* Right?"
    rin "Okay... Let's go get some rest now."
    rin "Have a good night, [mc]."
    rin "I'll see you tomorrow."
    mc "Good night, [rin]."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    jump ch2ep4weirdnoise
label ch2ep4weirdnoise:
    scene ch2ep4_509 with dissolve
    u "Alright....."
    u "Let's go back to my ro-"
    unknown "Ahhhh.... Harder....! Harder....!"
    scene ch2ep4_510 with dissolve
    u ".........................."
    u "What was that sound? It came out from [zeke]'s room."
    u "That can't be happening... The wall in this house is soundproo-"
    scene ch2ep4_511 with dissolve
    u "Oh, I see...."
    u "The door is ajar. That's why I can hear them."
    u "I guess they didn't realise that...."
    menu:
        "Take a peek [smrec]":
            u "Well........."
            scene ch2ep4_512_a1 with dissolve
            u "......................"
            scene black with dissolve
            $ renpy.pause()
            play music "sfx/ep4_2.mp3" fadein 3.0
            $ bgm = "Leonell Cassio - Woho, I Thought It Be Me & You (ft. Lily Hain)"
            scene ch2ep4_512_a2 with dissolve
            show ch2ep4_peek1 with dissolve
            mika "*Heavily breathes* Ahhh...! Yeah....! It feels so great...!"
            zeke "*Heavily breathes* Oh... Fuck... Your pussy is so tight, babe..."
            zeke "*Heavily breathes* Keep fucking me like that.... Don't stop..."
            hide ch2ep4_peek1 with dissolve
            scene ch2ep4_512_a3 with dissolve
            show ch2ep4_peek2 with dissolve
            mika "*Heavily breathes* Mhmmmm....!! [zeke]....!!"
            mika "*Heavily breathes* Ahhh.... I'm... about to cum, babe...!"
            zeke "*Heavily breathes* Fuck... Okay...! Let's cum together...!"
            scene black with dissolve
            stop music fadeout 3.0
            scene ch2ep4_512_a4 with dissolve
            u "What the hell was I thinking....?"
            u "Why were I peeking at them like a pervert?"
            u "Let's just leave them alone and go back to my room."
        "Go back to your room":
            scene ch2ep4_513 with dissolve
            u "That's none of my business."
            u "They're just enjoying their time."
            u "Let's just leave them alone and go back to my room."
    scene ch2ep4_514 with dissolve
    u "*Sighs*.............."
    u "I'm very exhausted now..."
    u "I guess I will just fall asleep in no time....."
    scene black with dissolve
    $ renpy.pause()
    s "Next morning............"
    scene ch2ep4_515 with dissolve
    u "What a lovely morning...."
    u "I fell asleep as soon as I got on the bed last night. Now, I'm feeling very refreshed."
    u "Let's go take a shower, then go get something to eat...."
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    $ area = "secondhall"
    $ ch2ep3endfreeroam = True
    $ ch2ep4freeroam = True
    jump ch2ep4_freeroam
label ch2ep4_endfreeroam:
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_516 with dissolve
    u "Alright...."
    u "Let's go to wor-"
    s "*Phone vibrates*..............."
    scene ch2ep4_517 with dissolve
    u "Hm...?"
    u "Who's calling me at such an early morning like this?"
    scene ch2ep4_518 with dissolve
    u "Oh... It's [maya]."
    u "I guess it must be about the meeting with [felix]."
    scene ch2ep4_519 with dissolve
    u "Let's hear her out...."
    mc "Good morning, [maya]."
    scene ch2ep4_520 with dissolve
    maya "Good morning, [mc]."
    maya "Did you sleep well last night?"
    scene ch2ep4_519 with dissolve
    mc "Yes, I did. What about you?"
    scene ch2ep4_520 with dissolve
    maya "*Smiles* Thank you for asking me back."
    maya "Yeah. I had a very good sleep last night."
    scene ch2ep4_521 with dissolve
    maya "About what we talked last night...."
    maya "I've already asked [felix]. He said he could meet you."
    scene ch2ep4_522 with dissolve
    mc "Really? When can I meet him?"
    scene ch2ep4_521 with dissolve
    maya "Are you free at 6 p.m. today?"
    maya "You can come meet him at my company."
    scene ch2ep4_522 with dissolve
    mc "Sure thing."
    mc "Can you send me the company's location, please?"
    scene ch2ep4_521 with dissolve
    maya "Are you sure you want me to send it?"
    maya "I can send [angela] to pick you up if you want."
    scene ch2ep4_519 with dissolve
    mc "Thank you, but you don't have to do that for me."
    mc "I can go there by my own."
    scene ch2ep4_520 with dissolve
    maya "Okay... If you say so."
    maya "See you this evening, son."
    scene ch2ep4_522 with dissolve
    mc "........................."
    mc "See you this evening, mo... [maya]."
    scene black with dissolve
    $ renpy.pause()
    s "You went to the company and spent time working until noon......"
    scene ch2ep4_523 with fade
    u "It's already lunchtime......"
    u "Let's go find something to eat."
    u "I feel like having a spaghetti as my today lunch..."
    if ch2ep2spendnightwithfaye == 1:
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep4_524 with dissolve
        u "Hm....?"
        u "Isn't that [faye]?"
        u "Why is she walking like that?"
        mc ".... [faye]."
        faye "Hm...?"
        scene ch2ep4_525 with dissolve
        faye "Oh.... Hello, [mc]."
        u "Hm? She seems a little bit weird today..."
        u "Her face looks so red. It also looks like she's suffering as well."
        scene ch2ep4_526 with dissolve
        mc "... Are you okay, [faye]?"
        faye "Y... Yeah, I am."
        mc "Are you sure? You don't look quite good right now."
        scene ch2ep4_527 with dissolve
        faye "I know...."
        faye "I have a little bit... of a cold, but... don't worry about me."
        faye "I just need to.... go buy some medicine, then I'll... be fine."
        mc "......................."
        scene ch2ep4_528_a1 with dissolve
        faye "Uhh... What are you doing?"
        mc "Stay still. I need to check your body temperature."
        faye "I told you... I'm okay...."
        mc "No, you aren't."
        mc "Your body temperature is very high right now. Don't you realize?"
        scene ch2ep4_528_a2 with dissolve
        faye "......................"
        mc "Do you have a meeting this afternoon?"
        faye "No.... Why do... you ask?"
        mc "So, you're basically free today, right?"
        faye "Yeah... you could say that."
        mc "Then you better take a sick leave and go home."
        faye "No, I can't... I've got to prepare some documents for a tomorrow meeting."
        menu:
            "Insist to take her home [faye3]":
                $ faye_relationship += 3
                $ faye_ch2_ep4 += 3
                $ ch2ep4takefayehome = 1
                scene ch2ep4_528_a3 with dissolve
                mc "Listen. I'm not a doctor, but I can tell you that won't get better by only taking a medicine."
                mc "You can't even stand straight right now. You need some rest real quick. Stop being stubborn and just go home."
                faye "I'm not... being stubborn. I'm just... trying to be responsible... for the work assigned."
                mc "But what if you don't get better by tomorrow?"
                mc "What's the point in preparing those documents if you aren't able to attend the meeting?"
                faye "......................."
                scene ch2ep4_528_a4 with dissolve
                mc "Give me the key."
                faye "What key... are you talking about?"
                mc "Your car's key. I'm going to take you home."
                faye "But....."
                mc "You can prepare those documents after taking some rest and getting better."
                faye "......................."
                scene ch2ep4_528_a5 with dissolve
                faye "*Sighs* Alright.... Take it."
                faye "*Sighs* I've never been put... in a corner like this before...."
                faye "But, everything you said was right...."
                mc "Great. You made a wise decision."
                scene ch2ep4_528_a6 with dissolve
                mc "Let's go."
                faye "Okay...."
                stop music fadeout 3.0
                jump ch2ep4takecarefaye
            "Fine...":
                $ ch2ep4takefayehome = 2
                scene ch2ep4_528_d with dissolve
                mc "*Sighs* Fine...."
                mc "Your life. Your choice. I hope you get well soon then."
                faye ".................."
                faye ".... Thanks."
                scene black with dissolve
                $ renpy.pause()
                s "You spent your time at the company until 5 p.m."
                s "Then, you got off work and headed to [maya]'s company...."
                jump ch2ep4meetfelix
    else:
        scene black with dissolve
        $ renpy.pause()
        s "You spent your time at the company until 5 p.m."
        s "Then, you got off work and headed to [maya]'s company...."
        jump ch2ep4meetfelix
label ch2ep4takecarefaye:
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ch2ep2_3.mp3" fadein 3.0
    $ bgm = "Firefl!es - Broken"
    scene ch2ep4_528_a7 with fade
    mc "To think about it, you haven't eatten anything, right?"
    mc "Are you hungry? I have never cooked before, but I guess I can make something easy for you."
    faye "Thank you, but... I don't feel... like eating anything now."
    mc "Alright then, let's head forward to your room."
    scene black with dissolve
    scene ch2ep4_528_a8 with dissolve
    faye "[mc]...."
    mc "Yeah?"
    faye "Thank you... so much. I owe you... again."
    mc "No, you don't. It's not a big deal."
    scene ch2ep4_528_a9 with dissolve
    mc "I'm going to bring you a damp cloth."
    mc "Put in on your head while sleeping. It will help decreasing your body temperature."
    faye "Okay...."
    faye "Oh... Could you please... call the president and... inform him of my absence? You can use my phone."
    mc "Sure thing. I'll be right back."
    scene black with dissolve
    scene ch2ep4_528_a10 with dissolve
    u "Alright...."
    u "I need to find [rowan]'s contact. Where is it....?"
    u "Okay... I've found it. Let's call him."
    scene ch2ep4_528_a11 with dissolve
    mc "....................."
    mc "... Good afternoon, sir. I'm [mc]. I don't know if you remember me."
    scene ch2ep4_528_a12 with dissolve
    rowan "Oh? [mc]?"
    rowan "Of course, I remember you."
    rowan "But, isn't this [faye]'s phone number? How come you're using her phone?"
    scene ch2ep4_528_a11 with dissolve
    mc "I happened to meet [faye] at the company an hour ago."
    mc "She didn't look quite good. Her body temperature was very high."
    mc "At first she was trying to continue working, but I insisted to bring her home so that she can get some rest."
    mc "So, I'm calling you now to inform you that [faye] just took a sick leave."
    scene ch2ep4_528_a13 with dissolve
    rowan "I see...."
    rowan "Thank you for doing that, [mc]. You made a right choice."
    rowan "She's a very good employee, but sometimes she works too hard."
    rowan "And please tell her to stop worrying about work and focus on getting better."
    scene ch2ep4_528_a14 with dissolve
    mc "Understood...."
    mc "I will make sure to tell her that."
    mc "Thank you for your understanding."
    scene black with dissolve
    scene ch2ep4_528_a15 with dissolve
    u "Alright......"
    u "Let's go prepare a damp cloth."
    scene black with dissolve
    scene ch2ep4_528_a16 with dissolve
    u "Hm...?"
    u "She already fell asleep? That's quite quick."
    u "But, it's actually good for her. She needs a lot of rest."
    u "Let's just put this damp cloth on her head..."
    scene ch2ep4_528_a17 with dissolve
    faye "[mc]...."
    mc "I'm sorry. Did I wake you up?"
    faye "No, you didn't. I haven't fallen asleep yet."
    scene ch2ep4_528_a18 with dissolve
    mc "Are you sure you don't want to eat anything?"
    mc "You should eat something so that you can take a medicine."
    faye "I've already had... a sandwich at half past eleven."
    faye "And don't worry... about the medicine, I already took it.... while you were... going to prepare the damp cloth."
    scene ch2ep4_528_a19 with dissolve
    mc "Is that so?"
    faye "Yeah...."
    mc "Great... Alright, I'm not going to bother you any longer."
    mc "Take a rest and get well soon."
    faye "Thank you...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_528_a20 with dissolve
    u "Well...."
    u "What shall I do now? Should I go back to the company?"
    u "......................."
    scene ch2ep4_528_a21 with dissolve
    u "I think I better stay here just in case [faye] needs any help."
    u "Let's go sit on the sofa and find something to do."
    u "There are so many hours left before it's 6 p.m."
    scene ch2ep4_528_a22 with dissolve
    u "There is no interesting book for me to read here."
    u "Let's just find some series to watch on Netflix."
    u "I haven't watched a series for a while already..."
    scene black with dissolve
    $ renpy.pause()
    s "*Two hours later*..............."
    scene ch2ep4_528_a23 with dissolve
    s "*Door opens*........"
    u "Hm....?"
    scene ch2ep4_528_a24 with dissolve
    faye "Hm...? [mc]...?"
    faye "Why are you still here?"
    faye "I thought you already left."
    scene ch2ep4_528_a25 with dissolve
    mc "I decided to stay here for a bit so that I can assist you if you need any help."
    mc "I'll leave before half past four though."
    faye "That's very kind of you..."
    mc "Where are you going to go by the way?"
    scene ch2ep4_528_a26 with dissolve
    faye ".... A toilet."
    mc "I see... Have you got any better?"
    faye "Yeah... I think I've got a little bit better..."
    faye "Even though I'm fully recovered yet, I don't feel as suffer as I did two hours ago."
    mc "Great..."
    scene black with dissolve
    $ renpy.pause()
    s "You spent your time at [faye]'s house until it's 4.30 p.m."
    scene ch2ep4_528_a27 with dissolve
    u "Alright.... It's already 4.30 p.m."
    u "The GPS says that it will take me about an hour to get to [maya]'s company."
    u "Let's just leave and go find a taxi now...."
    scene ch2ep4_528_a28 with dissolve
    mc "..................."
    mc "I'm leaving now, [faye]."
    s "...................."
    u "Looks like she's still sleeping...."
    u "Let's just leave quitely so that I do not wake her up."
    jump ch2ep4meetfelix
label ch2ep4meetfelix:
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/beach.mp3"
    $ bgm = "Bensound - Adventure"
    scene ch2ep4_529 with fade
    u "Here I am....."
    u "There are so many people here. They're all wearing suits."
    u "This place really gives a different vibe from Xecon..."
    unknown "Mr. [mc]."
    scene ch2ep4_530 with dissolve
    u "Hm....?"
    mc "Oh... It's you."
    scene ch2ep4_531 with dissolve
    mc "Good evening, [angela]."
    angela "Good evening, [mc]. Welcome to Teliene."
    mc "How long have you been standing here?"
    mc "I didn't see you when looking around, so I was about to go to the reception..."
    scene ch2ep4_532 with dissolve
    angela "It's because I just came down here a minute ago."
    angela "The president told me to come and wait for you here so that I can take you to her."
    angela "But, you arrived here quite faster than I thought...."
    mc "The traffic was light, so..."
    angela "I see...."
    scene ch2ep4_533 with dissolve
    angela "Alright... Let's not waste any more time here."
    angela "The president and Director [felix] are waiting for you now."
    mc "Hm? Is he here already?"
    angela "Yes. He arrived here about ten minutes ago."
    mc "I see... Okay, let's go then."
    angela "Sure. Please, follow me."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep4_534 with dissolve
    angela "President..."
    angela "I've already brought him here."
    maya "Oh...!?"
    maya "Thank you, [angela]."
    scene ch2ep4_535 with dissolve
    maya "You're here quite early, [mc]. It's not even 6 p.m. yet."
    maya "But, being on time is always good."
    mc "Hello, [maya]...."
    u "Judging from his uniform.... That guy must be [felix]."
    scene ch2ep4_536 with dissolve
    maya "Let me introduce both of you."
    maya "[mc]. This is [felix]. He's the police that I told you about."
    felix "Nice to meet you."
    u "He looks.... pretty big. I think I'm quite tall, but he's surely taller than me."
    scene ch2ep4_537 with dissolve
    maya "And this is [mc]. He's my son. Just like I told you."
    u "Hm...? She already told him about that?"
    mc "Nice to meet you, too."
    scene ch2ep4_538 with dissolve
    maya "Alright then..."
    maya "I have things to waiting for me to get them done, so I'll leave you guys alone."
    maya "Please, excuse me. I'll be right back as soon as I can."
    mc "Okay...."
    scene ch2ep4_539 with dissolve
    maya "Oh... I forgot to say this to you in person."
    maya "Thank you very much for agreeing to come here today, [felix]."
    felix "There is no need to thank me. It's just a part of my job."
    maya "Still... If there is anything you need me to help you with, please tell me so."
    maya "It would be my honor."
    felix "Thank you."
    scene black with dissolve
    $ renpy.pause()
    stop music fadeout 3.0
    scene ch2ep4_540 with dissolve
    felix "Okay...."
    felix "Shall we take a sit first? Before we start?"
    mc "Sure thing."
    scene ch2ep4_541 with dissolve
    play music "sfx/ch2ep2_5.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - I Saw A Ghost Last Night"
    felix "Alright..."
    felix "Since there are only two of us here, I'll be frank to you."
    felix "I can't belive you really turned out to be [maya]'s son."
    felix "I already know who you are. What is your plan?"
    scene ch2ep4_542 with dissolve
    mc "Plan? What plan are you talking about? I don't understand."
    mc "[maya] told me that you have an evidence to prove that my... father death wasn't an accident."
    mc "So, I'm here because I want to see that evidence."
    scene ch2ep4_543 with dissolve
    felix "Don't play dumb with me."
    felix "I know you work for [victor]."
    mc "....................."
    u "Did [maya] tell him that? But, I'm sure she doesn't know that I work for [victor] though..."
    u "She only knows that I was adopted by him. Then, how did this guy know that?"
    scene ch2ep4_544 with dissolve
    mc "You must be misunderstanding."
    mc "Yes, I did get adopted by him, but I'm not working for him."
    mc "I'm working as a programmer at Xecon right at the moment."
    scene ch2ep4_545 with dissolve
    felix "Alright. Alright. A programmer it is."
    felix "Anyway, I'm quite interested in your real purpose of working in that company."
    mc ".........................."
    mc "There is nothing like that. I always wanted to become a programmer. That's it."
    scene ch2ep4_546 with dissolve
    felix "You're lying to a wrong person. I know a lot more than you think I do."
    felix "Actually, you can just tell me the truth, but I understand why you don't want to."
    mc "......................"
    felix "Just relax. I'm going to arrest you today. Actually, I have no reason to do that."
    felix "It's only going to make [victor] stronger because he's surely going to be a lot more careful than ever."
    mc "....................."
    scene ch2ep4_547 with dissolve
    felix "Here is what you asked for. Take it."
    felix "Play the audio file to find out everything yourself."
    mc ".... Thank you."
    scene ch2ep4_548 with dissolve
    s "*Audio sounds* So, you're asking me to kill this man by making it like an accident?"
    s "*Audio sounds* Yes. That's right."
    s "*Audio sounds* There is no way I'm going to do it. I don't want to go to jail."
    felix "That's the audio recorded by the murderer while he was being hired."
    scene ch2ep4_549 with dissolve
    s "*Audio sounds* Don't worry about that. You will only need to be there for no more than 10 years. I guarantee you."
    s "*Audio sounds* I will also pay you ten million dollars for the job."
    s "*Audio sounds* Doesn't it sound like a good offer? There is no way you can make ten million dollars in ten years by yourself."
    felix "You can swipe left and see how he looks."
    mc "........................"
    scene ch2ep4_550 with dissolve
    felix "Don't think about doing something bad to him though."
    felix "He's under my protection since he's always been helpful lately."
    mc "......................."
    mc "You said [rio] was the person hiring him, right?"
    mc "What made you think so? Do you have any evidence?"
    felix "I knew only the audio file wouldn't make you believe me, so yeah I prepare another evidence for you."
    felix "Swipe left again and you'll see it."
    scene ch2ep4_551 with dissolve
    felix "The murderer secretly filmed this video while they were making the deal because he was afraid of getting betrayed."
    mc "......................"
    felix "So...? Does the other guy remind you of someone you know?"
    mc ".... Yeah. He looked younger than the first time I met him, but that's definitely [rio]."
    scene ch2ep4_552 with dissolve
    felix "And do you think he hired the murderer by his own will?"
    felix "I personally don't think so."
    felix "It must have been [victor] who was behind that murder."
    scene ch2ep4_553 with dissolve
    mc "....................."
    mc "Yeah... That could've been possible."
    felix "So... I will give you a chance."
    mc "A chance? What chance?"
    scene ch2ep4_554 with dissolve
    felix "Help me arrest [victor]."
    mc "....................."
    felix "He might have adopted you, but he's actually the person who messed up your whole life."
    felix "Your father died because of him. Don't you want to take a revenge?"
    felix "If you agree to help me, I'll not arrest you after we take down [victor]."
    mc "......................"
    scene ch2ep4_555 with dissolve
    felix "How does it sound? It sounds like a good deal for you, doesn't it?"
    mc "....................."
    mc ".... I need some time to think about it."
    felix "Sure. Let me know once you've decided."
    mc "Okay...."
    scene black with dissolve
    $ renpy.pause()
    s "Later that night............"
    scene ch2ep4_556 with fade
    $ renpy.pause()
    scene ch2ep4_557 with dissolve
    mc "........................."
    u "So, it's confirmed now that I've been working for the person who messed up my entire life."
    u "What am I supposed to do from now on...?"
    scene ch2ep4_558 with dissolve
    s "*Phone vibrates*.........."
    u "Hm...? [victor]...? I didn't expect him to call me at all."
    u "Moreover, he's calling through FaceTime. There must be something wrong."
    u "Looks like I have no choice. I have to answer this call."
    scene ch2ep4_559 with dissolve
    mc "......................"
    mc "Is there something you want me to do, sir?"
    scene black with dissolve
    scene ch2ep4_560 with fade
    victor "....................."
    mc "Hello, sir? Can you hear me?"
    victor "....................."
    scene ch2ep4_561 with dissolve
    victor "I heard [lucas] already gave you the thing you need that will help you get in the company's lab."
    victor "It's been more than a week already. Why haven't you got the blueprint yet?"
    victor "You usually don't take too much time to finish your mission. What's wrong?"
    scene ch2ep4_562 with dissolve
    mc "......................."
    mc "... This time is quite difficult, sir. The security system here is very good."
    mc "I've been thinking about the plan to get the blueprint and get out of the company without getting noticed."
    mc "I'm still figuring it out. I need a bit more time."
    scene ch2ep4_563 with dissolve
    victor "....................."
    victor "Fine. I'll give you one more week. Bring that fucking blueprint to me."
    mc ".... Understood."
    victor "You know what's going to happen if you fail, right?"
    mc "Yes, sir."
    victor "Great. Don't disappoint me then."
    scene ch2ep4_564 with dissolve
    s "*Call ended*.............."
    u "He ended the call just like that...."
    u "There must have been something wrong over there for sure."
    u "He's never been that impatient before.... That was the first time I see him like that."
    scene routewarning with dissolve
    $ renpy.pause()
    scene ch2ep4_565 with dissolve
    u "I guess [felix] has done something that made [victor] became like that."
    u "I've seen a lot of polices trying to arrest [victor]. But, all of them ended up failing to do so."
    u "However, this [felix] guy is completely different. He's on another level. I can feel it."
    u "I'm not even sure that I can beat him if we have to fight..."
    u "The deal he offered me sounds very promising, too. What should I do?"
    jump ch2ep4_crucialchoice
label ch2ep4_crucialchoice:
    menu:
        "Take down [victor]":
            scene ch2ep4_566 with dissolve
            u "Alright.... I've made my decision."
            u "If I continue working for [victor], many people are going to be in a big trouble."
            u "Especially, [maya]. She will just lose all money she invested in Xecon company."
            u "Moreover, my... family... was destroyed once because of [victor]. I won't let it happen again."
            u "I'm going to take him down...."
            $ ch2ep4decision = 1
            jump ch2ep4end
        "Be on [victor]'s side":
            scene ch2ep4_566 with dissolve
            u "It is true that Maya is my mother and Victor is a suspect in my father's death."
            u "But..."
            u "To be honest, [maya] and [skylar] are complete strangers who I have only known for a few days."
            u "And even if she had her reasons, it doesn't change the fact that she chose to leave me when I was a child."
            u "So, to be honest, I don't have any feelings for Maya at all, let alone Skylar."
            u "It was Victor who gave me the opportunity to grow up to where I am today."
            u "Let's not do anything stupid like betraying him and just stick to the original plan."
            jump victor_route_ending
label ch2ep4end:
    stop music fadeout 3.0
    scene black with dissolve
    hide screen smartphone
    $ rin_ch2_ep4 = 6
    $ episode = 8
    call screen ending

label ch2ep4_freeroam:
    if ch2ep4hiddenimages_count == 5:
        $ ch2ep4hiddenimages = True
    if area == "frontyard":
        jump ch2ep4_endfreeroam
    call screen ch2ep4_house
label ch2ep4_kitchen_rin:
    if ch2ep4kitchen_pic1 == False and ch2ep4kitchen_pic2 == False:
        scene ch2ep4_kitchen_photos
    if ch2ep4kitchen_pic1 == True and ch2ep4kitchen_pic2 == False:
        scene ch2ep4_kitchen_photo2
    if ch2ep4kitchen_pic1 == False and ch2ep4kitchen_pic2 == True:
        scene ch2ep4_kitchen_photo1
    elif ch2ep4kitchen_pic1 == True and ch2ep4kitchen_pic2 == True:
        scene ch2ep4_kitchen
    if ch2ep4breakfastrin == 0:
        scene ch2ep4_rintalk at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_rintalk.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_rintalk_blink.jpg", 1) with dissolve
        mc "Good morning, [rin]."
        rin "*Smiles* Good morning, [mc]."
        mc "Have you slept well last night?"
        rin "Never been better. What about you?"
        mc "I had a good sleep, too."
        rin "Lovely... Come. Let's have a breakfast together."
        mc "Sure thing."
        scene black with dissolve
        $ renpy.pause()
        s "You spent some time having a breakfast with [rin]...."
        $ ch2ep4breakfastrin = 1
        jump ch2ep4_freeroam
    else:
        u "I've already done that."
        jump ch2ep4_freeroam
label ch2ep4_secondhall_yui:
    if ch2ep4secondhall_pic == False:
        scene ch2ep4_secondhall_photo
    else:
        scene ch2ep4_secondhall
    scene ch2ep4_yuitalk at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_yuitalk.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_yuitalk_blink.jpg", 1) with dissolve
    mc "Good morning, [yui]."
    yui "Good morning."
    mc "What are you doing here?"
    yui "Just standing here enjoying the sky. Nothing special."
    mc "I see..."
    jump ch2ep4_freeroam
label ch2ep4_zekeroom_zeke:
    if ch2ep4zekeroom_pic == False:
        scene ch2ep4_zekeroom_photo
    else:
        scene ch2ep4_zekeroom
    scene ch2ep4_zeketalk at eyesblink("Ch.2/Ep.4/Scenes/ch2ep4_zeketalk.jpg", "Ch.2/Ep.4/Scenes/ch2ep4_zeketalk_blink.jpg", 1) with dissolve
    mc "Hi, [zeke]."
    zeke "Hey! What's up, bro."
    mc "What are you doing here? Where's [mika]?"
    zeke "She's taking a shower right now."
    zeke "I'm waiting for her to finish, then we'll go for a breakfast together."
    mc "Alright. See you around then."
    zeke "See you, bro."
    jump ch2ep4_freeroam
label ch2ep4_kitchen_pic1:
    if _in_replay:
        scene ch2ep4_kitchenpic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    if ch2ep4kitchen_pic2 == False:
        scene ch2ep4_kitchen_photo2
    else:
        scene ch2ep4_kitchen
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep4kitchen_pic1 = True
    $ ch2ep4hiddenimages_count += 1
    jump ch2ep4_freeroam
label ch2ep4_kitchen_pic2:
    if _in_replay:
        scene ch2ep4_kitchenpic2 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    if ch2ep4kitchen_pic1 == False:
        scene ch2ep4_kitchen_photo1
    else:
        scene ch2ep4_kitchen
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep4kitchen_pic2 = True
    $ ch2ep4hiddenimages_count += 1
    jump ch2ep4_freeroam
label ch2ep4_secondhall_pic:
    if _in_replay:
        scene ch2ep4_secondhallpic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ch2ep4_secondhall
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep4secondhall_pic = True
    $ ch2ep4hiddenimages_count += 1
    jump ch2ep4_freeroam
label ch2ep4_hallway_pic:
    if _in_replay:
        scene ch2ep4_hallwaypic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ch2ep4_hallway
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep4hallway_pic = True
    $ ch2ep4hiddenimages_count += 1
    jump ch2ep4_freeroam
label ch2ep4_zekeroom_pic:
    if _in_replay:
        scene ch2ep4_zekeroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ch2ep4_zekeroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep4zekeroom_pic = True
    $ ch2ep4hiddenimages_count += 1
    jump ch2ep4_freeroam
