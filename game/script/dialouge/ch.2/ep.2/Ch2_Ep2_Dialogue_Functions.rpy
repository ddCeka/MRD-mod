label ch2ep2:
    scene black with dissolve
    $ renpy.pause(3, hard=True)
    scene ep2
    $ renpy.pause(3, hard=True)
    scene black with dissolve
    show screen smartphone
    if ch2ep1qa == 1:
        jump visitrinparents
    else:
        jump getbackhome
label visitrinparents:
    play music "sfx/ch2ep2_1.mp3" fadein 3.0
    $ bgm = "Roa Music - After the rain"
    scene ch2ep2_1 with fade
    u "Today is the day I'm going to visit [yui]'s parents."
    u "She told me to dress properly. I think this suit will do."
    scene ch2ep2_2 with dissolve
    u "Okay. I'm ready."
    u "I wonder if she is. Let's go to her room."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_3 with fade
    yui "*Hums* It's you. It's always you. Met a lot of people. But nobody feels like you~"
    yui "(Umm... What should I wear today?)"
    yui "(Let's see what I have here.)"
    s "*Knocks*..........."
    scene ch2ep2_4 with dissolve
    yui "Hm? [mc]?"
    mc "Yeah, it's me. I'm ready now. What about you?"
    yui "Not yet. Give me five minutes."
    mc "Okay. I'll wait for you out here, then."
    scene black with dissolve
    $ renpy.pause()
    show yuioutfit with dissolve
    $ renpy.pause(8, hard=True)
    scene ch2ep2_6 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_6.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_6_blink.jpg", 1) with dissolve
    yui "Sorry to keep you waiting..."
    yui "...Hm?"
    scene ch2ep2_5 with dissolve
    mc "What's wrong?"
    yui "Nothing. Your outfit just looks a little bit too dark."
    mc "You want me to go change?"
    yui "No, it's fine. Don't worry about it."
    mc "Are you sure about that?"
    scene ch2ep2_6 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_6.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_6_blink.jpg", 1) with dissolve
    yui "Yeah. You look good enough already."
    mc "Thanks. You look pretty today, too."
    yui "*Smiles* Thanks. Shall we go..."
    yui "...Wait a sec."
    mc "What's wrong again?"
    yui "We can't go meet them with that facial expression of yours."
    yui "I know that you don't often smile, but you need to do it today."
    mc "...I don't know how to do that."
    yui "What do you mean you don't know? It's just a smile."
    yui "Come on! Let me see you smile so that I can tell you if it looks great."
    mc ".................."
    scene ch2ep2_7 with dissolve
    mc "....Like this?"
    yui "................"
    mc "Say something."
    yui "...Are you planning on shocking my parents?"
    yui "I beg you, [mc]. Please, don't smile like this with anyone, or you will end up in jail."
    mc "..............."
    scene ch2ep2_8 with dissolve
    yui "Come on. You can do it. I've seen you smile before."
    yui "Look at me. You just need to relax. Then, lift the corners of your mouth into a small smile."
    yui "See? Easy, right? Just slightly lift them up."
    yui "And try to think of something that makes you happy."
    scene ch2ep2_9 with dissolve
    yui "Yes! That's right!"
    yui "Remember this feeling so that you can smile naturally."
    mc "Hm? Am I smiling right now?"
    yui "Yes, you are! Why did you ask?"
    mc "Nothing. It's just I didn't try to smile, but the way you taught me..."
    yui "What's wrong with that?"
    mc "I never thought you would do something like that. It was cute."
    yui "................"
    scene ch2ep2_10 with dissolve
    yui "....T-Thanks."
    yui "(What's wrong with me? Why does my face feel so hot? And why is my heart beating so fast right now?)"
    mc "Are you okay? Your face looks so red. Aren't you feeling well today?"
    yui "I-I'm good! Don't worry about me. Let's just go now."
    mc "...Alright, if you say so."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_11 with dissolve
    unknown "Oh?! [yui], [mc], good morning!"
    yui "Hm...?"
    scene ch2ep2_12 with dissolve
    yui "Oh, good morning, [rin]."
    rin "Hm? Why are you guys dressed so formally today?"
    rin "Are you guys going somewhere?"
    scene ch2ep2_13 with dissolve
    yui "Do you remember that I fought with my parents?"
    rin "Oh, yeah. I remember that."
    yui "So, I'm going to meet my parents today."
    rin "I see... What about you, [mc]?"
    scene ch2ep2_14 with dissolve
    yui "He's coming with me, too."
    mc "...Yeah."
    rin "Hm? Why?"
    yui "I asked him to pretend to be my boyfriend today."
    scene ch2ep2_15 with dissolve
    rin "P-pretend to be what?!"
    yui "My boyfriend. My parents planned to have me engaged with a random guy, right?"
    yui "I'm planning to go meet them to tell them I already have a boyfriend."
    yui "And there is no way I will get engaged to that guy."
    rin "...Are you sure that it will work?"
    yui "I don't know. I'm just trying as many things as possible to fix the problem."
    rin "................."
    rin "Alright. I respect your decision. I wish you luck, then."
    yui "*Smiles* Thank you so much. I appreciate that."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_16 with dissolve
    yui "Do you remember the answers we prepared, [mc]?"
    mc "Of course. You don't need to worry about that."
    yui "Great. Let's go then!"
    mc "Yeah...."
    scene ch2ep2_17 with dissolve
    yui "Oh! Wait a second!"
    yui "I almost forgot something."
    mc "Then, go grab it. I'll wait here."
    scene ch2ep2_18 with dissolve
    yui "It's not anything like that. I meant that I almost forgot that we shouldn't go meet them by bus."
    yui "There is no way they are going to allow you to be my boyfriend if we do that."
    mc "...Why?"
    yui "Think about it. If you were a father, would you want your daughter to date a guy who can't even afford to buy a car?"
    yui "Would you be positive that he could take care of your daughter?"
    scene ch2ep2_19 with dissolve
    mc "....You're overthinking it."
    yui "Well, you might be right, but better safe than sorry."
    mc "What's your plan then?"
    yui "Do you know how to drive?"
    mc "Yes, I do."
    yui "How about we go ask [zeke] to lend us his car for a day?"
    mc "I don't think he will agree to that. He really cherishes his car."
    yui "...Yeah, you're right. I think we have no other choice, but to go rent a car, then."
    mc ".................."
    scene ch2ep2_20 with dissolve
    mc "How about my car?"
    yui "Hm? Your car? Since when do you have a car?"
    mc "A couple years ago."
    yui "And where is it now? Why didn't you drive it here when you moved in?"
    mc "Where is your house at?"
    yui "Northern Town."
    mc "Great. We can drop by the place where I park my car. It's halfway to Northern Town."
    yui "Lovely! Then, what are we waiting for? Let's hurry up then!"
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_21 with fade
    mc "Alright, here we are."
    mc "Wait for me here. I will go get my car."
    yui "Hm? Why don't we go together now?"
    mc "...It's pretty far from here to walk. You better wait here."
    yui "....Alright, whatever you say."
    scene black with dissolve
    $ renpy.pause()
    s "*Fifteen minutes later*........."
    scene ch2ep2_22 with dissolve
    yui "................."
    yui "(What is taking him so long....?)"
    s "*Engine sounds*........."
    scene ch2ep2_23 with dissolve
    yui "(Hm....?)"
    scene ch2ep2_24 with dissolve
    s "*Engine sounds*........."
    yui "(Wow... I don't know much about cars, but that car looks so beautiful.)"
    yui "(It must be very expensive for sure.)"
    scene ch2ep2_25 with dissolve
    s "*Horn sounds*..........."
    yui "(By the way, I wonder where [mc] is now.)"
    yui "(It's about fifteen minutes since he left...)"
    u "(Hm? What is she looking at?)"
    s "*Horn sounds*..........."
    yui "..................."
    u "*Sighs*..........."
    scene ch2ep2_26 with dissolve
    mc "What are you looking at, [yui]?"
    yui "[mc]?! W-What?!"
    mc "What?"
    yui "I-Is this your car?!"
    mc "Yeah. Get in the car. I'm not allowed to park here for long."
    yui "O-Okay...."
    scene black with dissolve
    scene ch2ep2_27 with dissolve
    yui "...Is this really your car?"
    mc "Why are you looking at me like that?"
    yui "I'm sorry. I just didn't expect you to have a car like this."
    yui "I never knew you come from a very rich family. You've never acted like one."
    mc "It's a long story."
    yui "................"
    scene ch2ep2_28 with dissolve
    mc "Can you do me a favor?"
    yui "Hm? What's it?"
    mc "I need you to set the GPS to your house."
    yui "Sure. Wait a sec."
    mc "By the way, are you sure that your family is there right now?"
    mc "I know that it's Saturday today, but you should call them and ask if they are there so that we don't waste time going there for nothing."
    yui "Oh yeah, you're right. I'll call them now."
    scene ch2ep2_29 with dissolve
    yui "................"
    yui "Hi, mom. Are you home now?"
    yui "................"
    yui "Hm? Then, where are you?"
    yui "................"
    yui "Alright, I get it."
    scene ch2ep2_30 with dissolve
    mc "What's wrong? Are they away from home?"
    yui "Yeah, they are at a vacation house."
    mc "And where is it?"
    yui "It's about a hundred miles farther north from my home."
    mc "Okay. Let's go then."
    yui "...Are you sure that you can drive that far?"
    mc "Hm? Why not?"
    yui "Nothing. I'm just worried that you'll be tired."
    mc "Don't worry about me. I'm good."
    mc "It's not like we can go back now."
    scene ch2ep2_31 with dissolve
    yui "Okay. Let's go then."
    yui "I'm going to set a new GPS for you now."
    mc "Thanks."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_32 with dissolve
    yui "Okay. We've arrived."
    yui "That is their car. You can park right next to it."
    mc "Okay. Got it."
    scene black with dissolve
    scene ch2ep2_33 with dissolve
    yui "Alright, let's go in."
    mc "Are you okay? You don't look well."
    yui "Yeah, don't worry about me. I'm just a little bit nervous."
    mc "Relax. Everything is going to be fine."
    yui "I hope so."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_34 with dissolve
    s "*Door opens*..........."
    yui "Hm? There is no one here. Where are they? "
    yui "Mom! Dad! Where are you?"
    scene ch2ep2_35 with dissolve
    sofia "[yui]? How come are you here?"
    yui "Hi, Mo-"
    scene ch2ep2_36 with dissolve
    yui "!!!!!"
    yui "Mom! Why are you dressed like that?!"
    sofia "Hm? Why not? We're at the beach."
    sofia "What else should I wear?"
    yui "...Yeah, you're right. I'm sorry."
    scene ch2ep2_37 with dissolve
    sofia "By the way, aren't you going to introduce me to your friend?"
    yui "O-Oh! This is [mc], mom."
    yui "But, he isn't my friend. H-he's my b-boyfriend!"
    sofia "Hm? Your boyfriend?"
    yui "Y-Yeah!"
    scene ch2ep2_38 with dissolve
    sofia "Nice to meet you, [mc]. I'm [sofia]."
    yui "*Whispers* W-What are you doing? Introduce yourself now!"
    yui "*Whispers* Don't forget to smile, too. Don't be nervous. You need to calm down and behave naturally."
    u "*Sighs* You should tell that to yourself first..."
    scene ch2ep2_39 with dissolve
    mc "[yui] told me a lot about you."
    mc "It's my pleasure to meet you, [sofia]."
    sofia "Me, too. Come. Let's take a seat inside first."
    scene ch2ep2_40 with dissolve
    yui "Look, mom. I already have a boyfriend."
    yui "So, I'm not going to get engaged to that guy you were talking about."
    sofia "Not now, [yui]. We'll talk about it later."
    yui "B-But...!"
    yui "*Sighs* Fine! Where is dad by the way?"
    scene ch2ep2_41 with dissolve
    sofia "Out there. He said that he was going for a walk."
    yui "I see..."
    sofia "Oh! Speaking of the devil. There he comes..."
    sofia "[fred]! Come over here!"
    sofia "[yui] was looking for you!"
    scene ch2ep2_42 with dissolve
    fred "W-What did you s-"
    fred "Oh my...!"
    yui "Hi, dad."
    fred "Yuiiii~!"
    scene ch2ep2_43 with dissolve
    fred "I missed you soooooo much, sweetheart!"
    yui "D-Dad, calm down! I can't breathe!"
    u "...What is going on here?"
    u "By the way, her parents seem very different from what she told me. They seem like very nice parents."
    scene ch2ep2_44 with dissolve
    fred "*Sobs* I'm sorry for the last time we met, sweetheart."
    fred "*Sobs* Please, don't be angry at m-"
    scene ch2ep2_45 with dissolve
    fred "Hm...?"
    fred "Who is this young man?"
    yui "Oh! Let me introduce him."
    scene ch2ep2_46 with dissolve
    yui "This is [mc], dad."
    mc "Nice to meet you, sir."
    yui "He is my boyfriend."
    fred "You can just call me [fred]..."
    scene ch2ep2_47 with dissolve
    fred "W-Wait, what?!"
    fred "What did you just say?"
    fred "He is your boyfriend?"
    yui "What are you doing, dad? Shake his hand."
    scene ch2ep2_48 with dissolve
    fred "O-Oh, that was very rude of me. I'm sorry."
    fred "Nice to meet you, [mc]."
    mc "No, it wasn't. You don't have to say sorry to me at all."
    sofia "Alright, everyone. Let's go take a seat and talk."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_49 with dissolve
    fred "I'm sorry to ask this again, but are you really my daughter's boyfriend?"
    fred "How long have both of you been dating?"
    yui "D-Dad!"
    fred "What's wrong, sweetheart? I'm just asking."
    yui "B-But...!"
    scene ch2ep2_50 with dissolve
    yui "!!!!!"
    yui "(...Oh, he is purposely holding my hand just to keep me calm.)"
    yui "(*Sighs* Well, there is no other choice but to trust him and let him handle the situation now.)"
    mc "Yes, I'm really her boyfriend."
    mc "We've just been dating for about a month."
    mc "I know that it's only a month, but I really love her."
    scene ch2ep2_51 with dissolve
    sofia "I see..."
    sofia "However, don't you think it's too fast to come visit us here?"
    sofia "No matter how much you say that you love her, you guys have only been dating for a month."
    sofia "Are you sure that you already know each other well enough?"
    scene ch2ep2_52 with dissolve
    mc "Yeah, I know that. I won't say that I know her well."
    mc "But, we are learning more about each other now."
    mc "However, I heard that you tried to engage her with someone else."
    mc "So, I had no choice, but to come visit both of you here."
    mc "Can you please let us date?"
    scene ch2ep2_53 with dissolve
    yui "Yes, mom. Can you please stop trying to engage me with that guy?"
    yui "I don't really want to get engaged."
    yui "I mean I already have a boyfriend, and I don't even know that guy well."
    yui "There is no way you are going to do that to me, right?"
    scene ch2ep2_54 with dissolve
    sofia "................"
    fred "................"
    scene ch2ep2_55 with dissolve
    sofia "*Sighs*.........."
    fred "*Smiles* Just tell her."
    sofia "Okay..."
    scene ch2ep2_56 with dissolve
    sofia "Yeah, you guys can keep dating. You have my permission."
    yui "Really?! Thank you, mom! I love you so much!"
    mc "Thank you, ma'am."
    sofia "*Smiles* There is no need to be too polite. Just call me [sofia], okay?"
    mc "I get it, [sofia]."
    sofia "*Smiles* Great. However, there is something I need to tell you, sweetheart."
    scene ch2ep2_57 with dissolve
    sofia "You misunderstood us very much. We didn't try to get you engaged at all."
    yui "W-What?! But, didn't you...?"
    sofia "I'll tell you the truth now. There is a business partner who's been working with us for a long time."
    sofia "Yeah, I know that he asked us to introduce you to his son since both of you were single."
    sofia "And because we've known each other for a very long time, it would be rude if [fred] and I turned down his request."
    sofia "Moreover, he is a very good guy. So, I just wanted you to go meet his son for once. That's it."
    scene ch2ep2_58 with dissolve
    yui "B-But, I remember you said the word {b}engaged.{/b}"
    sofia "Yeah, you're right. He said that he wanted to get you and his son engaged if both of you liked each other and got along well."
    sofia "We didn't try to force you to get engaged with him at all, sweetheart."
    yui "B-But, why didn't you tell me that earlier?"
    sofia "How could we have done that? You immediately ran out of the house before we even had a chance to."
    sofia "We tried to call you to explain everything, but you didn't listen to us at all."
    yui "...................."
    yui ".....I'm sorry."
    fred "It's alright, sweetheart. We weren't angry at you."
    fred "*Smiles* However, I know that you can get angry very easy, but you have to learn to be a little bit more calm."
    yui "I'm trying, dad..."
    scene ch2ep2_59 with dissolve
    yui "*Sighs* What a relief! I'm much happier now!"
    u "......What am I doing here?"
    u "I thought things would've gotten serious, but it seems like she just misunderstood her parents."
    u "So, there is nothing I need to do here anymore."
    scene ch2ep2_60 with dissolve
    yui "Let's go home, [mc]."
    mc "What? Right now?"
    yui "*Smiles* Yeah! Didn't you already hear that? I'm not going to have to get engaged anymore!"
    mc "I know that, but we just arrived...."
    scene ch2ep2_61 with dissolve
    fred "That's right. You guys just got here. Why are you in a hurry to go back?"
    fred "As I remember, it takes about 6 hours to get here from there."
    fred "[mc] also seems tired. You should let him rest first."
    yui "Oh yeah, you're right..."
    sofia "Let's have dinner together, too. It's been a while since you paid us a visit."
    sofia "We want to spend time with you, too, sweetheart."
    scene ch2ep2_62 with dissolve
    yui "What do you think, [mc]?"
    mc "Yeah, let's rest for a bit."
    yui "Alright then!"
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ch2ep2_2.mp3" fadein 3.0
    $ bgm = "Roa Music - Summer Days"
    scene ch2ep2_63 with fade
    mc "................."
    u "Well, it seems like I didn't waste time coming here for nothing after all."
    u "At least I can relax and take a break from everything."
    scene ch2ep2_64 with dissolve
    u "This feels so nice..."
    u "If I were to buy a house in the future, I'd buy a house near a beach like this."
    scene ch2ep2_65 with dissolve
    yui "Aw... It's really sunny out today."
    sofia "I agree with you, sweetheart."
    sofia "Hm...?"
    scene ch2ep2_66 with dissolve
    sofia "What are you doing here, [mc]?"
    sofia "Why are you still wearing that suit?"
    u "Hm...?"
    scene ch2ep2_67 with dissolve
    mc "Oh, it's you."
    sofia "Hm?"
    mc "Nothing. Well, I didn't bring any other clothes with me, so..."
    sofia "I see..."
    sofia "Do you want me to borrow something from [fred] for you?"
    mc "Thank you, but don't mind me. I'll ask him myself."
    sofia "Okay then."
    scene ch2ep2_68 with dissolve
    sofia "Sweetie, do you mind helping me apply sunscreen on my back?"
    sofia "I will do it for you, too."
    yui "Of course not. Let's go lie down over there, mom."
    sofia "Yeah, sure."
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*........"
    scene ch2ep2_69 with dissolve
    fred "How are you now, [mc]?"
    fred "Feeling alright yet?"
    mc "Yeah, I'm fine now."
    fred "Good to hear that."
    scene ch2ep2_70 with dissolve
    fred "By the way, do you know how to surf?"
    mc "Yes, I do. Why did you ask?"
    fred "Well, I'm about to go surfing. Do you want to join me?"
    scene ch2ep2_71 with dissolve
    u "...Well, it's been a while since I last surfed."
    u "I'm kind of missing the waves. Moreover, it would be rude if I turned him down."
    u "Let's just join him."
    scene ch2ep2_72 with dissolve
    fred "What do you say?"
    mc "I'll join you, [fred]."
    fred "Great! I've finally got someone to surf with me now!"
    mc "By the way, can you lend me some shorts? I can't go surfing in this outfit."
    fred "Of course! Get up and follow me inside, then."
    mc "Okay."
    scene ch2ep2_73 with dissolve
    fred "Fortunately, you and I are the same size."
    fred "Well... even though you look a little bit taller than me, I think you can wear my shorts."
    fred "They will definitely fit you."
    mc "Thank you."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_74 with dissolve
    fred "Okay! We're ready now!"
    fred "Let's go pick up the surfboards over there!"
    mc "Got it."
    scene ch2ep2_75 with dissolve
    fred "How long have you been surfing?"
    mc "Um... six years. I learned how to surf when I was sixteen."
    fred "I see... So, you're quite experienced at it then."
    mc "Well, I won't say that. I stopped surfing when I was a freshman in the university, because I didn't have time to."
    fred "It's alright! Don't worry about that. I just wanted to make sure that you can take care of yourself while surfing."
    fred "You know... surfing is quite dangerous for a newbie, but since you've got some experience, I'm relieved."
    mc "I see..."
    fred "Alright, let's get started then!"
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*........."
    scene ch2ep2_76 with fade
    fred "(Whoa...! This kid is really good at surfing.)"
    fred "(To be honest, I thought he agreed to join me because he was too considerate to say no.)"
    fred "(So I was a little bit worried at first, but there is no need to worry now since he is this good.)"
    fred "(He said that he stopped surfing when he went to the university, but he doesn't seem like someone who stopped surfing that many years ago.)"
    fred "(This kid has really got talent. I like him.)"
    scene black with dissolve
    $ renpy.pause()
    s "*An hour later*.........."
    scene ch2ep2_77 with fade
    fred "Thank you for joining me, [mc]."
    fred "You were really good. I had so much fun surfing with you!"
    mc "Thank you. I had so much fun, too."
    fred "May I ask you something?"
    mc "Yeah, sure."
    scene ch2ep2_78 with dissolve
    fred "Are you an ex-professional surfer or what?"
    fred "I mean... even though I've been surfing for more than ten years, I couldn't surf like you just did."
    mc "No, I'm not. I've never participated in any competition."
    fred "Really....? That's a shame. You could've been a really successful surfer if you'd participated in competition."
    mc "You're too kind to me. I'm not that good."
    fred "Yes, you are!"
    mc "...Thank you."
    fred "By the way, are you hungry now?"
    mc "A little bit. Why did you ask?"
    fred "Well, it's already evening. I'm starting to get hungry. Let's head back inside."
    mc "Okay."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_79 with dissolve
    sofia "Oh? Finished surfing already?"
    fred "Yeah! And you know what?!"
    fred "[mc] is really good! You should've seen him surf!"
    sofia "*Smiles* I did. I watched you guys from here."
    scene ch2ep2_80 with dissolve
    sofia "*Giggles* By the way, you've never changed, [fred]. You are always so happy when you find someone who is good at surfing."
    fred "Well, I really like surfing, so why not?"
    fred "I once asked you to learn surfing, but you said that you didn't want to."
    fred "*Smiles* But, it's all good now since I have [mc] here!"
    sofia "*Giggles* Good for you then!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_81 with dissolve
    sofia "Alright, since you guys have spent a lot of energy, I assume that you guys are already hungry."
    sofia "[fred] and I are going to cook you dinner, [mc]."
    mc "Thank you very much. I appreciate that."
    fred "There is no need to say that. You're already one of us."
    sofia "By the way, would you mind going to tell [yui] to come have dinner, please?"
    mc "Sure, but where is she now?"
    sofia "She went out to walk along the beach. She should be somewhere around here."
    mc "Okay. I will go find her."
    sofia "Thank you."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_82 with dissolve
    u "...Alright, let's go find [yui]."
    u "I wonder where she is now..."
    scene black with dissolve
    $ renpy.pause()
    s "*Ten minutes later*........."
    scene ch2ep2_83 with dissolve
    u "Oh, there she is..."
    u "Let's approach her."
    scene ch2ep2_84 with dissolve
    mc "Hey...."
    yui "Hm..?!"
    scene ch2ep2_85 with dissolve
    yui "*Smiles* Oh, it's you."
    mc "Your mom asked me to come tell you to go have dinner."
    yui "Okay, but hey. We've still got time before they finish cooking."
    yui "Why don't you walk along the beach with me for a bit?"
    mc "..................."
    yui "Come on. There is nothing for you to do anyway, right?"
    mc "Okay then."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_86 with dissolve
    yui ".................."
    mc "................."
    yui "................"
    scene ch2ep2_87 with dissolve
    yui "I think I've never said this to you."
    mc "Said what?"
    yui "Thank you for coming here with me today, [mc]."
    mc "...Oh. You're welcome."
    yui "If you hadn't agreed to help me, I wouldn't have come here today."
    yui "Then, I wouldn't have known that I was misunderstanding my parents."
    yui "I've learned so many things today. And that's all because of you."
    mc "It's alright. I'm glad that you've cleared things up with your parents."
    scene ch2ep2_88 with dissolve
    yui "*Giggles* Well, to think about it, don't you think it was very funny?"
    mc "Hm? What was so funny about?"
    yui "I mean... We prepared that Q&A and practiced it so hard, but, we didn't have to use it at all!"
    mc "Oh yeah, you're right."
    mc "Well, I guess it's because they love you so much. That was why they were willing to believe you without asking any question."
    scene ch2ep2_89 with dissolve
    yui "Love me...?"
    mc "Why? What's wrong?"
    yui "Nothing... It's just if they really loved me, why didn't they trust me when I told them that I wanted to be a game developer?"
    mc "..................."
    yui "I mean... I understand that it was my fault this time, but I don't understand why they didn't give me their support back then?"
    mc "...You should ask them frankly then. I'm sure that they had a reason."
    yui "................."
    scene ch2ep2_90 with dissolve
    yui "*Sighs* Let's stop talking about it, okay?"
    yui "I'm in a good mood now. I don't want to ruin it."
    mc "Okay, if you say so."
    yui "Thank you. Alright, let's head back inside. I think dinner is ready now."
    mc "Hm? How do you know that?"
    yui "I just know it. Trust me."
    mc "Okay..."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_91 with dissolve
    yui "See? I was right. Dinner is ready now."
    yui "You can smell the food from here, right?"
    mc "Yeah, it smells so good."
    yui "Let's go enjoy our dinner then!"
    scene black with dissolve
    s "*About an hour later*..........."
    scene ch2ep2_92 with fade
    yui "Thank you for the food, mom, dad. It was so delicious."
    mc "Thank you for cooking me dinner, too."
    sofia "No need to thank us. I'm glad to see both of you enjoying the food we cooked."
    fred "Yeah, that's right."
    scene ch2ep2_93 with dissolve
    yui "Alright, shall we go now?"
    mc "Hm? Go where?"
    yui "Go back to our home, of course."
    mc "Oh..."
    scene ch2ep2_94 with dissolve
    sofia "Why don't you guys stay overnight here?"
    yui "M-Mom! W-What did you just say?!"
    sofia "It's already 7 p.m. You guys will get there very late at night."
    sofia "Plus, it's not safe to drive at night. Don't you agree?"
    yui "B-But, where am I going to sleep?"
    scene ch2ep2_95 with dissolve
    sofia "There are two bedrooms here. Have you already forgot that?"
    sofia "You can sleep in the one on the upper floor."
    fred "Yeah, listen to your mom, sweetheart. It's very dangerous to drive at night."
    fred "It's better to just spend the night here, then leave tomorrow morning."
    scene ch2ep2_94 with dissolve
    yui "B-But, where is he going to sleep at?"
    sofia "Hm? What are you talking about? Of course, he will sleep in your room."
    yui "B-But...?!"
    sofia "You guys are dating, aren't you? What's wrong with him sleeping in your room?"
    sofia "Unless you guys aren't actually...."
    yui "O-Okay! We'll spend the night here!"
    scene ch2ep2_96 with dissolve
    yui "But, I'm going to have to ask his opinion first."
    yui "What do you say, [mc]?"
    yui "Do you want to go home now, or spend the night here?"
    mc "I think your dad and mom are right. It's already too late to go home now."
    mc "Let's just stay overnight here."
    yui "*Sighs* Alright then...."
    scene ch2ep2_97 with dissolve
    sofia "Okay, since everything is settled now. I won't take your time anymore."
    sofia "Make yourself at home, [mc]."
    mc "Thank you, [sofia]."
    sofia "You're welcome."
    sofia "Alright, I'm going to wash the dishes now. Can you give me a hand, [yui]?"
    yui "Yeah, sure."
    mc "Let me help you, too."
    sofia "Hm? No. No, you're my guest. You don't need to help me."
    mc "You already cooked me a wonderful dinner. I want to do something for you in return, too."
    mc "Please, let me help you."
    sofia "...Okay then. If you insist."
    scene black with dissolve
    s "*A few moments later*............"
    scene ch2ep2_98 with dissolve
    sofia "Thank you both for helping me."
    sofia "I won't take your time anymore."
    sofia "Have a good rest. I will see you guys tomorrow."
    yui "Good night, mom."
    sofia "Good night, sweetie."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_99 with fade
    yui "...Alright, this is our bedroom."
    yui "*Sighs* I can't believe that they actually told us to sleep together."
    yui "What are we going to do now?"
    yui "Should I just go tell them that we aren't actually dating?"
    mc ".................."
    scene ch2ep2_100 with dissolve
    mc "I can sleep somewhere else if you want."
    yui "Hm? What are you talking about?"
    mc "I saw a living room while we were on the way here."
    mc "I can sleep on the sofa there. I don't mind that."
    yui "But, why...?"
    scene ch2ep2_101 with dissolve
    mc "You seem very uncomfortable that we're going to have to sleep together."
    mc "So, I'm just offering you an option."
    yui "But, what if my dad and my mom see you sleeping outside?"
    mc "Don't worry about it. I don't think they will come up to check on us."
    yui ".................."
    yui "*Smiles* Okay then. Thank you for understanding me, [mc]."
    mc "No problem."
    yui "Alright, I'm going to take a shower now. I'll call you when it's your turn."
    mc "Okay, sure."
    scene black with dissolve
    $ renpy.pause()
    stop music fadeout 3.0
    scene ch2ep2_102 with dissolve
    u "That's the sofa right there..."
    u "I guess I have no other choice, but to sleep here for the night."
    u "Well, at least it looks quite comfortable to sleep on."
    unknown "[mc]."
    scene ch2ep2_103 with dissolve
    u "Hm...?"
    scene ch2ep2_104 with dissolve
    play music "sfx/ch2ep2_3.mp3" fadein 3.0
    $ bgm = "Firefl!es - Broken"
    mc "Oh... Hi, [fred]."
    mc "Is there something you want from me?"
    fred "Well, I've just realized that you'll need some pajamas."
    fred "Can you follow me downstairs? I'll lend you some."
    mc "You're right. I'm going to need them. Thank you so much."
    scene ch2ep2_105 with dissolve
    fred "By the way, I'm going to drink some wine while lying on a beach chair outside."
    fred "Would you like to accompany me for a while?"
    mc "Sure. I'll drink with you."
    fred "Great to hear that. Let's go then."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_106 with fade
    fred "Cheers!"
    mc "Cheers..."
    scene ch2ep2_107 with dissolve
    fred "Mmm... It tastes so good."
    fred "The sales clerk suggested I buy another one, and I almost bought it, but I changed my mind at the very last second."
    fred "I'm not regretting buying this one now."
    scene ch2ep2_108 with dissolve
    mc "Well, I don't know much about wine, but I agree with you."
    mc "It does taste so good."
    fred "I know right?"
    fred "By the way, you're not really my daughter's boyfriend, are you?"
    scene ch2ep2_109 with dissolve
    mc ".................."
    mc "What made you think that? Yes, I'm really her boyfriend."
    fred "Come on. Just admit it. You don't need to lie to me at all."
    mc ".................."
    mc "*Sighs* Well, you're right. I'm not her boyfriend."
    scene ch2ep2_110 with dissolve
    fred "*Smiles* I knew it."
    mc "When did you realize?"
    fred "Since the beginning where both of you were trying to trick us to believe you."
    mc "What about [sofia]? Did she know?"
    fred "Of course she did."
    mc "...................."
    fred "*Laughs* You guys need to try to be better actors!"
    fred "No matter how much you said that you were her boyfriend, the way you looked at each other wasn't the way a real couple does."
    mc "....I'm sorry."
    scene ch2ep2_111 with dissolve
    fred "No, there is no need to say that to me. I'm not at angry at you."
    fred "[sofia] and I understood why both of you were trying to trick us."
    mc "Then, why haven't you exposed us?"
    fred "*Laughs* Why should we do that? It was so funny to see you guys trying!"
    mc "..................."
    scene black with dissolve
    s "*A few moments later*........"
    scene ch2ep2_112 with dissolve
    yui "[mc]! It's your turn now!"
    yui "....Hm?"
    scene ch2ep2_113 with dissolve
    yui "(He isn't here?)"
    yui "(Where is he? Where has he gone?)"
    yui "(He must have gone downstairs. Let's go find him.)"
    scene ch2ep2_114 with dissolve
    yui "(Hm? Isn't that mom?)"
    yui "(What is she doing there?)"
    scene ch2ep2_115 with dissolve
    yui "Mom! What are you doing here?"
    sofia "!!!!"
    scene ch2ep2_116 with dissolve
    sofia "Shhh.... Come here."
    yui "What's wrong, mom?"
    sofia "*Whispers* Don't talk too loud. They might hear us."
    yui "................."
    yui "*Whispers* What are you talking about?"
    scene ch2ep2_117 with dissolve
    sofia "*Whispers* Your dad and [mc] are hanging out together right there."
    yui "*Whispers* Then, why do we have to hide here? Let's go join them."
    sofia "*Whispers* No. I think we should stay here. Your dad is asking him a very interesting question."
    yui "*Whispers* Interesting question?"
    sofia "*Whispers* Yeah, don't you want to know how he thinks of you?"
    yui "..................."
    scene ch2ep2_118 with dissolve
    fred "What made you decide to help her actually?"
    fred "You know... not everyone would agree to do something like this."
    fred "Do you really like my daughter?"
    mc ".....I don't know."
    fred "What did you mean you didn't know?"
    mc "We had a very bad first impression. She was very rude to me at first, but things between us started to get better by days."
    mc "So, I don't hate her."
    scene ch2ep2_119 with dissolve
    fred "Well, I can imagine what it was like."
    fred "You know... [yui] has always had a short temper. She gets angry very easily when things don't go as planned, or someone doesn't agree with her."
    fred "However, she was a very good kid at first. She just became that way since the day we disagreed on letting her be a game developer."
    mc "May I ask why you and [sofia] disagreed with her on that?"
    fred "Well, I know that being a game developer has been her dream, but you know... it isn't an easy road for a woman."
    fred "No matter how much people say man and woman are equal, a woman is still judged unfairly by a man in many situations."
    fred "For example, in the game development area, where most people who are interested in it are men. I knew from the beginning that she was going onto a rough path."
    fred "I know that we were wrong to disagree with her. We should've given her our support instead of stopping her."
    fred "But, I can confirm to you that no parents would love to see their daughter go onto a rough path."
    fred "[sofia] and I have worked hard to become successful so that our daughter, [yui], can have an easy life."
    fred "That's why we wanted her to inherit the family business, because even if she struggled, we would be able to give her some useful advice."
    fred "But, in game development, we know nothing about it."
    scene ch2ep2_120 with dissolve
    yui "*Sobs* Is that true, mom...?"
    sofia "Of course, sweetie."
    yui "*Sobs* I thought you and dad disagreed with me because the two of you didn't love me...."
    sofia "No way was that case. We always love you, sweetie. We are going to love you every day until the last day of our lives."
    yui "*Sobs* Mom...."
    scene ch2ep2_121 with dissolve
    mc "To be honest I understand that you were worried about her, but I'd like to tell you something."
    fred "Yeah? What is it?"
    mc "I'd like to tell you that you don't need to worry about her at all. Yeah, it's true that she's immature sometimes, and her personality could cause some problems for her."
    mc "But, she's really got talent. She's been working pretty well at the company. She can be very successful in her career."
    mc "Yeah, she is going on a rough path, but that's the life she chose."
    mc "It's good that you want her to have the easy path that you chose for her, but this is my opinion; people don't grow up unless they suffer first."
    mc "So, you should trust your own daughter and show her your support. She is a strong woman."
    scene ch2ep2_122 with dissolve
    sofia "That was such a nice speech, don't you think?"
    yui "...Yeah. I never knew he thought of me like that."
    yui "(...Why is my heart beating so fast....?)"
    sofia "You've got such a nice guy with you. Don't let him slip away, sweetheart."
    sofia "You like him, do you?"
    scene ch2ep2_123 with dissolve
    yui "W-What are you talking ab-!"
    yui "O-Of course! He's my boyfriend."
    yui "W-Why would I not like him?"
    sofia "*Giggles* Stop acting, already. We knew from the first minute that you guys weren't actually dating."
    yui "W-What?! H-How?!"
    sofia "*Giggles* It was really obvious."
    yui "..........................."
    scene ch2ep2_124 with dissolve
    yui "*Sighs* I can't really trick you guys at all..."
    sofia "*Smiles* Well, at least you tried your best."
    yui "Then, why did you try to have us sleep together if you knew that we aren't actually a couple."
    sofia "Why not? I like him. I'm down if he's going to be my real son-in-law."
    yui "But, that's not the right way to do..."
    yui "Plus, I don't think about him in that way."
    sofia "You can say whatever you want, sweetheart. But, you can't lie to yourself."
    scene ch2ep2_125 with dissolve
    sofia "Well, it's your choice. I'm leaving now."
    sofia "But hey, I'm sure that there are many girls out there who are waiting to get him."
    sofia "You will surely lose him if you don't do anything at all."
    sofia "You know that I was the one who made the first move on your dad, right?"
    sofia "If you really like him, then, go for it."
    sofia "Good luck, sweetheart."
    yui "*Sighs*................"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_126 with dissolve
    fred "Alright, I think it's time for bed now."
    fred "Thank you again for joining me, [mc]."
    fred "And yeah, you're right. I should trust my daughter and show her my support."
    fred "Thank you for telling me your thoughts."
    mc "You're welcome."
    fred "See you tomorrow."
    mc "See you, too."
    scene black with dissolve
    $ renpy.pause()
    s "*A few moments later*.........."
    scene ch2ep2_127 with dissolve
    u "Alright, It's getting very late at night."
    u "I should get back inside, too."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_128 with fade
    u "Okay, I'm done with my shower."
    u "Time to go sleep now."
    $ ch2ep2visityuiparents = True
    $ yui_relationship += 2
    $ yui_ch2_ep2 += 2
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_129 with dissolve
    yui "[mc]...."
    mc "Hm....?"
    mc "Oh, it's you."
    scene ch2ep2_130 with dissolve
    mc "What are you doing here?"
    mc "Are you watching TV?"
    yui "No, I'm here waiting for you."
    mc "Hm? Why? Is there something you want from me?"
    scene ch2ep2_131 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_131.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_131_blink.jpg", 1) with dissolve
    yui "Well...."
    yui "Actually...."
    mc "Hm? What is it?"
    yui "I'm here to ask you if...."
    mc "If what?"
    yui "I-If you want to sleep in my room...."
    mc "................."
    yui "You know... you're my guest, and you came here to help me. So, I think it's a bit rude if I let you sleep out here."
    mc "But, are you really okay with that?"
    yui "Y-Yeah... I don't mind sleeping in the same bed with you for a night..."
    menu:
        "Alright then. [yui2] [yui2]":
            $ ch2ep2sleepwithyui = 1
            $ yui_relationship += 2
            $ yui_ch2_ep2 += 2
            scene ch2ep2_132 with dissolve
            mc "Alright then, if you say so."
            mc "Thank you, [yui]."
            yui "A-All good... Let's get inside then."
            mc "Sure."
            jump sleepwithyui
        "Insist on sleeping here":
            $ ch2ep2sleepwithyui = 2
            scene ch2ep2_132 with dissolve
            mc "It's alright. You don't have to do this."
            mc "I have no problem sleeping here."
            yui "....Are you sure about that?"
            mc "Yeah, don't worry about me."
            yui "Alright then... Good night, [mc]."
            mc "Good night."
            scene black with dissolve
            $ renpy.pause()
            scene ch2ep2_132_d with dissolve
            u "Finally, it's time to rest."
            u "Today has been a very long day. I also have to drive a very long way back home tomorrow."
            u "I should get enough sleep."
            jump ch2ep2nextmorning
label sleepwithyui:
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
    scene ch2ep2_132_a1 with dissolve
    play music "sfx/ch2ep2_4.mp3" fadein 3.0
    $ bgm = "LiQWYD - Lay Me Down"
    yui ".................."
    mc ".................."
    scene ch2ep2_132_a2 with dissolve
    yui "Do you want to sleep on the right or the left side?"
    mc "Either one is fine."
    yui "Alright, I'm going to sleep on the right side then."
    mc "Okay. Then, I'll sleep on the left."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_132_a3 with dissolve
    mc "................"
    yui "..............."
    mc "................"
    scene ch2ep2_132_a4 with dissolve
    yui "[mc]...."
    yui "Are you awake?"
    mc "................"
    scene ch2ep2_132_a5 with dissolve
    mc "Yeah, what's up?"
    yui "Thank you...."
    mc "You already said that to me."
    yui "I know... I just want to say it again."
    mc "...Well, even though I don't know what is it for this time, I'll accept it again, then."
    scene ch2ep2_132_a6 with dissolve
    yui "It's for the words you spoke to my dad."
    mc "Hm? Did you hear us talking?"
    yui "Yeah. I was going to tell you to take a shower, then I saw you and him lying down on the couch outside."
    mc "I see..."
    mc "Well, I didn't do anything much but speaking out my thoughts, to be honest."
    scene ch2ep2_132_a7 with dissolve
    yui "Yes, you did. What you said meant a lot to me. I'm grateful for that."
    yui "Moreover, you helped me understand my parents again."
    yui "You helped me know how much they love me."
    mc "Well, I guess there are no parents who don't love their own child, except...."
    yui "Hm? Except what?"
    mc "Nothing. Don't mind me."
    yui ".................."
    yui "Anyway, you looked very cool when speaking with my dad. When you told him to trust me and support me, you made...."
    mc "Made what?"
    yui "N-Nothing....!"
    yui "(Argh! That was close! I almost told him that he made my heart flutter...)"
    s "*Strange voices*............"
    mc "Hm? What was that sound...?"
    scene ch2ep2_132_a8 with dissolve
    sofia "Ahhh~! [fred]~!"
    sofia "Y-Yes...! Y-Yes...! D-Don't stop...!"
    yui "Oh my...!!!"
    mc "................."
    yui "E-Er.... P-Please, don't mind them. They always do this when they spend time here..."
    mc "...Of course, I won't."
    fred "Oooh! I love you, [sofia]~!"
    yui "Gosh... Mom! Dad!"
    mc "..................."
    scene ch2ep2_132_a9 with dissolve
    yui "Ugh...! I can't hold it anymore...!"
    mc "Hm? What are you talking ab-"
    scene ch2ep2_132_a10 with dissolve
    yui "*Kisses* Mmmmmm....."
    mc "Mmmmm...."
    yui "*Kisses* [mc].... Mmmm..."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_132_a11 with dissolve
    mc ".................."
    mc "....Why did you do that?"
    yui "I don't know.... I just felt like doing it."
    yui "I don't even know what's been happening to me recently either, [mc]."
    yui "You keep making my heart flutter. I don't know how it happens."
    mc "But, didn't you like [pete]?"
    yui "Yeah, I liked him. But, after spending time by myself thinking about him, I've found that I didn't really {b}like{/b} him."
    yui "I only admired him because he helped me out at the university."
    yui "I know that I did get sad when finding out that he and [sandra] like each other, but that's just it."
    yui "I didn't feel like I couldn't let him go. Unlike you...."
    yui "I like you, [mc]."
    mc "But, [yui]... To be honest I don't know how to love someone."
    yui "That's not a problem. I will teach you."
    mc "..................."
    scene black with dissolve
    yui "A-Aw...!"
    scene ch2ep2_132_a12 with dissolve
    yui "*Giggles* I didn't expect that...."
    mc "Are you sure that you aren't going to regret it?"
    yui "*Smiles* Yes, I am."
    yui "*Smiles* I know that our first time was a mistake, but it isn't this time."
    mc "..................."
    scene ch2ep2_132_a13 with dissolve
    mc "*Kisses*............"
    yui "*Kisses* Mmmmm....."
    yui "*Kisses* Ahhh.... [mc]...."
    mc "*Kisses* I'm going to take your clothes off...."
    yui "*Kisses* Mmmm... O...Okay..."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_132_a14 with dissolve
    yui "Come on... Stop staring at me already."
    yui "You're making me embarrassed."
    mc "Sorry. I didn't mean to."
    yui "And are you really going to leave me undressed alone?"
    yui "Undress yourself, too."
    mc "Yeah, sure."
    scene ch2ep2_132_a15 with dissolve
    yui "Okay, great. We're even now."
    yui "....What do you have in mind?"
    mc "Can you get up and bend over here?"
    yui "...Okay, got it."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_132_a16 with dissolve
    yui "...Like this?"
    mc "Yeah..."
    mc "I'm going to start now..."
    yui "Hm...? What are you talking ab-"
    scene ch2ep2_132_a17 with dissolve
    show ch2ep2_yui1 with dissolve
    window hide
    yui "Arr~!"
    yui "*Softly breathes* Mmmm... W-Wait a sec, [mc]...!"
    mc "Hm? Do you want me to stop?"
    yui "*Softly breathes*..............."
    yui "*Softly breathes* No, p-please keep going..."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_yui1
    scene ch2ep2_132_a18 with dissolve
    show ch2ep2_yui2 with dissolve
    window hide
    yui "*Softly breathes* Arrr... Your tongue is so wet, but it's making me feel good at the same time..."
    yui "*Softly breathes* H-How come you are so good at this...?"
    mc "I don't know."
    $ renpy.pause()
    menu:
        "Next":
            scene black with dissolve
            hide ch2ep2_yui2
    scene ch2ep2_132_a19 with dissolve
    mc "Alright, I think you're ready now."
    yui "Hm? Are you going to do it now?"
    mc "Yeah, why?"
    yui "What about you? Should I....?"
    mc "No, it's fine. I want to do it now."
    yui "Okay then, just don't cum inside, okay?"
    scene ch2ep2_132_a20 with dissolve
    mc "I'll try to..."
    mc "I'm going to put it in now."
    yui "O-Okay....."
    scene ch2ep2_132_a21 with dissolve
    yui "A-Ahhh...!"
    mc "It went in...."
    scene ch2ep2_132_a22 with dissolve
    yui "*Softly breathes* Y-Yeah, you're so big that I can tell it myself...!"
    mc "Can I start moving now?"
    yui "*Softly breathes* Y-Yeah, go ahead..."
    scene ch2ep2_132_a23 with dissolve
    show ch2ep2_yui3 with dissolve
    window hide
    yui "*Softly breathes* Mmmmm.... [mc]....."
    yui "*Softly breathes* Ahhhh... You're so big..."
    $ renpy.pause()
    menu:
        "Next":
            mc "I'm going to do it a bit faster."
            yui "*Softly breathes* Mmmmmm... O-Okay..."
    hide ch2ep2_yui3
    scene ch2ep2_132_a24 with dissolve
    show ch2ep2_yui4 with dissolve
    window hide
    yui "*Softly breathes* Ahhhh...! [mc]....!"
    yui "*Softly breathes* I-It feels so good...!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_yui4
    scene ch2ep2_132_a25 with dissolve
    show ch2ep2_yui5 with dissolve
    window hide
    yui "*Heavily breathes* Mmmmm...! Y-Yeah, keep fucking me like that...!"
    mc "Shhh... Lower your voice. Your parents might hear you."
    yui "*Heavily breathes* I don't think they will mind...!"
    $ renpy.pause()
    menu:
        "Next":
            scene black with dissolve
            hide ch2ep2_yui5
    scene ch2ep2_132_a26 with dissolve
    yui "*Softly breathes* Are you tired now?"
    mc "Not yet? Why?"
    yui "*Softly breathes* I'll do it myself if you are tired."
    yui "No... Actually, let me do it for you."
    mc "Alright, if that's what you want."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_132_a27 with dissolve
    yui "*Giggles* You're really so big..."
    show ch2ep2_yui6 with dissolve
    window hide
    $ renpy.pause(1.8, hard=True)
    scene ch2ep2_132_a27_a
    hide ch2ep2_yui6
    yui "*Softly breathes* Ahhh... It's in..."
    yui "*Softly breathes* I'm going to move now..."
    scene ch2ep2_132_a28 with dissolve
    show ch2ep2_yui7 with dissolve
    window hide
    yui "*Softly breathes* Mmmmm... So good... This feels so good...!"
    yui "*Softly breathes* How is it, [mc]? Do you like this?"
    mc "Yeah... Keep moving like that."
    $ renpy.pause()
    menu:
        "Next":
            yui "*Softly breathes* Hehe... I've got another idea."
            yui "*Softly breathes* I'm going to move my hips faster."
    hide ch2ep2_yui7
    scene ch2ep2_132_a29 with dissolve
    show ch2ep2_yui8 with dissolve
    window hide
    yui "*Moans* Ahhh....! [mc]...! Mmmm....!"
    yui "*Moans* This is so good...! I like it so much...!"
    $ renpy.pause()
    menu:
        "Next":
            yui "*Moans* Mmmmm... I-I'm almost there...!"
            mc "*Softly breathes* Me, too..."
    hide ch2ep2_yui8
    scene ch2ep2_132_a30 with dissolve
    show ch2ep2_yui9 with dissolve
    window hide
    yui "*Heavily breathes* Mmmm...! Almost there...! Almost there...!"
    yui "*Heavily breathes* Ahhh...! [mc]...! I'm about to cum...!"
    mc "*Softly breathes* So am I...."
    menu:
        "Lick pussy":
            hide ch2ep2_yui9
            jump ch2ep2yuipussylick1
        "Doggy":
            hide ch2ep2_yui9
            jump ch2ep2yuidoggy1
        "Slowest":
            hide ch2ep2_yui9
            jump ch2ep2yuicowgirl1
        "Slower":
            hide ch2ep2_yui9
            jump ch2ep2yuicowgirl2
        "Cum":
            jump ch2ep2yuicowgirlcum
label ch2ep2yuipussylick1:
    scene ch2ep2_132_a17 with dissolve
    show ch2ep2_yui1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Doggy":
            hide ch2ep2_yui1
            jump ch2ep2yuidoggy1
        "Reverse cowgirl":
            hide ch2ep2_yui1
            jump ch2ep2yuicowgirl1
        "Faster":
            hide ch2ep2_yui1
            jump ch2ep2yuipussylick2
label ch2ep2yuipussylick2:
    scene ch2ep2_132_a18 with dissolve
    show ch2ep2_yui2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Doggy":
            hide ch2ep2_yui2
            jump ch2ep2yuidoggy1
        "Reverse cowgirl":
            hide ch2ep2_yui2
            jump ch2ep2yuicowgirl1
        "Slower":
            hide ch2ep2_yui2
            jump ch2ep2yuipussylick1
label ch2ep2yuidoggy1:
    scene ch2ep2_132_a23 with dissolve
    show ch2ep2_yui3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Lick pussy":
            hide ch2ep2_yui3
            jump ch2ep2yuipussylick1
        "Reverse cowgirl":
            hide ch2ep2_yui3
            jump ch2ep2yuicowgirl1
        "Faster":
            hide ch2ep2_yui3
            jump ch2ep2yuidoggy2
        "Fastest":
            hide ch2ep2_yui3
            jump ch2ep2yuidoggy3
label ch2ep2yuidoggy2:
    scene ch2ep2_132_a24 with dissolve
    show ch2ep2_yui4 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Lick pussy":
            hide ch2ep2_yui4
            jump ch2ep2yuipussylick1
        "Reverse cowgirl":
            hide ch2ep2_yui4
            jump ch2ep2yuicowgirl1
        "Slower":
            hide ch2ep2_yui4
            jump ch2ep2yuidoggy1
        "Faster":
            hide ch2ep2_yui4
            jump ch2ep2yuidoggy3
label ch2ep2yuidoggy3:
    scene ch2ep2_132_a25 with dissolve
    show ch2ep2_yui5 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Lick pussy":
            hide ch2ep2_yui5
            jump ch2ep2yuipussylick1
        "Reverse cowgirl":
            hide ch2ep2_yui5
            jump ch2ep2yuicowgirl1
        "Slowest":
            hide ch2ep2_yui5
            jump ch2ep2yuidoggy1
        "Slower":
            hide ch2ep2_yui5
            jump ch2ep2yuidoggy2
label ch2ep2yuicowgirl1:
    scene ch2ep2_132_a28 with dissolve
    show ch2ep2_yui7 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Lick pussy":
            hide ch2ep2_yui7
            jump ch2ep2yuipussylick1
        "Doggy":
            hide ch2ep2_yui7
            jump ch2ep2yuidoggy1
        "Faster":
            hide ch2ep2_yui7
            jump ch2ep2yuicowgirl2
        "Fastest":
            hide ch2ep2_yui7
            jump ch2ep2yuicowgirl3
label ch2ep2yuicowgirl2:
    scene ch2ep2_132_a29 with dissolve
    show ch2ep2_yui8 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Lick pussy":
            hide ch2ep2_yui8
            jump ch2ep2yuipussylick1
        "Doggy":
            hide ch2ep2_yui8
            jump ch2ep2yuidoggy1
        "Slower":
            hide ch2ep2_yui8
            jump ch2ep2yuicowgirl1
        "Faster":
            hide ch2ep2_yui8
            jump ch2ep2yuicowgirl3
label ch2ep2yuicowgirl3:
    scene ch2ep2_132_a30 with dissolve
    show ch2ep2_yui9 with dissolve
    window hide
    menu:
        "Lick pussy":
            hide ch2ep2_yui9
            jump ch2ep2yuipussylick1
        "Doggy":
            hide ch2ep2_yui9
            jump ch2ep2yuidoggy1
        "Slowest":
            hide ch2ep2_yui9
            jump ch2ep2yuicowgirl1
        "Slower":
            hide ch2ep2_yui9
            jump ch2ep2yuicowgirl2
        "Cum":
            jump ch2ep2yuicowgirlcum
label ch2ep2yuicowgirlcum:
    menu:
        "Cum inside":
            scene black with dissolve
            scene ch2ep2_132_a30_in1 with vpunch
            mc "Ugh..! I'm cumming...!"
            yui "M-Me, too...! Ahhhhh~!"
            yui "*Pants*...T..That was great..."
            mc "I'm going to pull it out now."
            scene ch2ep2_132_a30_in2 with dissolve
            yui "*Pants* By the way, I told you to not cum inside me, didn't I?"
            mc "My bad. I couldn't take it out in time."
            yui "*Pants* It's alright, I'm going to remove it in the bathroom real quick...."
            mc "Okay, I'll let you go then."
        "Cum outside":
            scene black with dissolve
            scene ch2ep2_132_a30_out1 with vpunch
            mc "Ugh..! I'm cumming...!"
            yui "M-Me, too...! Ahhhhh~!"
            yui "*Pants*...T..That was great..."
            scene ch2ep2_132_a30_out2 with dissolve
            yui "*Pants* Hehe... You came so hard. My body is all covered by your semen."
            mc "I'm sorry."
            yui "*Pants* It's alright, I guess I will just have to take a shower again."
            mc "Okay, I'll let you go then."
    scene black with dissolve
    $ renpy.pause()
    s "After having sex with [yui], you got dressed and fell asleep in a few moments..."
    jump ch2ep2yuimorningbj
label ch2ep2yuimorningbj:
    unknown "Mmmmm......"
    u "Hm? What was that strange sound?"
    u "And why is my dick feeling so..."
    scene ch2ep2_132_a31 with dissolve
    show ch2ep2_yui10 with dissolve
    u "...Good?"
    $ renpy.pause()
    hide ch2ep2_yui10
    scene ch2ep2_132_a32 with dissolve
    u "So, it was [yui]..."
    mc "What are you doing, [yui]?"
    yui "!!!!!"
    scene ch2ep2_132_a33 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_132_a33.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_132_a33_blink.jpg", 1) with dissolve
    yui "Oh?! You're finally up?"
    mc "What were you doing?"
    yui "Hm? Wasn't it obvious? I was sucking your cock."
    mc "I know that... But, why?"
    yui "Well, I woke up and saw you had morning wood."
    yui "So, I decided to help you out. That's why."
    mc "It's just a normal thing for a man...."
    yui "I know... Then, tell me if you still want me to help you or not."
    mc "...Alright, since you've already started, you should keep doing it until the end."
    yui "*Giggles* I predicted that answer from miles away!"
    scene ch2ep2_132_a34 with dissolve
    show ch2ep2_yui11 with dissolve
    window hide
    yui "*Licks* Hehe... Do you enjoy what I'm doing for you?"
    yui "*Licks* ...Well, of course you do. I can tell by the look on your face."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_yui11
    scene ch2ep2_132_a35 with dissolve
    show ch2ep2_yui12 with dissolve
    window hide
    yui "*Licks* Mmmm... It tastes so good...."
    yui "*Licks* I think I'm starting to get addicted to it now..."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_yui12
    scene ch2ep2_132_a36 with dissolve
    show ch2ep2_yui13 with dissolve
    window hide
    yui "*Sucks* Mmmmmm......"
    yui "*Sucks* Mmmmm.... Your cock.... It can barely fit in my mouth...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_yui13
    scene ch2ep2_132_a37 with dissolve
    show ch2ep2_yui14 with dissolve
    window hide
    yui "*Sucks* Mmmmmmm....."
    yui "*Sucks* Mmmm... You're about to cum, right?"
    yui "*Sucks* Mmmmmm..... I can feel it's getting bigger and hotter like it's about to explode."
    yui "*Sucks* Don't hold it.... Mmmmm.... Just cum in my mouth..."
    $ renpy.pause()
    menu:
        "Tip lick":
            hide ch2ep2_yui14
            jump ch2ep2yuitiplick1
        "Slower":
            hide ch2ep2_yui14
            jump ch2ep2yuibj1
        "Cum":
            jump ch2ep2yuibjcum
label ch2ep2yuitiplick1:
    scene ch2ep2_132_a34 with dissolve
    show ch2ep2_yui11 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch2ep2_yui11
            jump ch2ep2yuibj1
        "Faster":
            hide ch2ep2_yui11
            jump ch2ep2yuitiplick2
label ch2ep2yuitiplick2:
    scene ch2ep2_132_a35 with dissolve
    show ch2ep2_yui12 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch2ep2_yui12
            jump ch2ep2yuibj1
        "Slower":
            hide ch2ep2_yui12
            jump ch2ep2yuitiplick1
label ch2ep2yuibj1:
    scene ch2ep2_132_a36 with dissolve
    show ch2ep2_yui13 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Tip lick":
            hide ch2ep2_yui13
            jump ch2ep2yuitiplick1
        "Faster":
            hide ch2ep2_yui13
            jump ch2ep2yuibj2
label ch2ep2yuibj2:
    scene ch2ep2_132_a37 with dissolve
    show ch2ep2_yui14 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Tip lick":
            hide ch2ep2_yui14
            jump ch2ep2yuitiplick1
        "Slower":
            hide ch2ep2_yui14
            jump ch2ep2yuibj1
        "Cum":
            jump ch2ep2yuibjcum
label ch2ep2yuibjcum:
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_132_a38 with vpunch
    mc "Ugh....!"
    yui "Mmmmmmm!!!"
    scene ch2ep2_132_a39 with dissolve
    $ renpy.pause()
    scene ch2ep2_132_a40 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_132_a40.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_132_a40_blink.jpg", 1) with dissolve
    yui "*Giggles* Hehe... You're surely a healthy man, aren't you?"
    mc "Hm? What made you think that?"
    yui "Well, you came quite a lot even though we just did it last night."
    yui "To be honest I wanted to try to swallow it, but I'm not ready yet."
    yui "*Giggles* But, thank you for a quick breakfast by the way!"
    mc "You're welcome, I guess?"
    yui "*Giggles* Alright, let's get up and take a shower."
    yui "We're going to have a real breakfast with my parents, then go home after that."
    mc "Okay then."
    scene black with dissolve
    $ renpy.end_replay()
    $ ch2ep2havesexwithyui = True
    $ yui_relationship += 2
    $ yui_ch2_ep2 += 2
    $ renpy.pause()
    stop music fadeout 3.0
    jump ch2ep2nextmorning
label ch2ep2nextmorning:
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ch2ep1_1.mp3" fadein 3.0
    $ bgm = "Roa - Winter Magic"
    scene ch2ep2_133 with dissolve
    yui "Alright, let's go downstairs for breakfast."
    mc "Sure..."
    scene ch2ep2_134 with dissolve
    yui "Morning, mom. Morning, dad."
    sofia "Morning, sweetie."
    fred "Good morning both of you."
    fred "There are bread and coffee on the counter, [mc]. Serve yourself."
    mc "Thank you, [fred]."
    scene black with dissolve
    $ renpy.pause()
    s "You spent about an hour having breakfast...."
    scene ch2ep2_135 with dissolve
    yui "Okay, we're leaving now."
    sofia "Are you going straight back to your house?"
    yui "I don't know. It depends on [mc]."
    mc "Yeah, we're going straight back there."
    sofia "I see..."
    scene ch2ep2_136 with dissolve
    sofia "Alright then, get home safe."
    sofia "Don't forget to call me when you get there, okay?"
    yui "Sure, mom."
    sofia "I love you, sweetheart."
    yui "Me, too."
    scene ch2ep2_137 with dissolve
    yui "Alright, I've got to go now."
    yui "Goodbye, mom. See you later, dad."
    fred "Goodbye, sweetheart."
    scene ch2ep2_138 with dissolve
    fred "Drive safe, [mc]."
    mc "Understood. Goodbye, [fred], [sofia]."
    sofia "Goodbye. I hope we'll meet again."
    mc ".....Me, too."
    scene black with dissolve
    s "*A few hours later*............"
    scene ch2ep2_139 with fade
    mc "Get out of the car, [yui]."
    yui "W-What? Why?"
    mc "Wait for me here. I'm going to park the car, then we'll take the bus home."
    yui "Hm? Why don't you just drive it back home? Why do you have to make things complicated?"
    mc "No. Things will get complicated if I actually drive this car back there."
    yui "...Alright, that sounds legit. Don't take too long then. It's pretty hot out there."
    mc "Got it."
    scene black with dissolve
    s "*A few more hours later*............"
    scene ch2ep2_140 with fade
    yui "Alright, we're back."
    yui "You must be tired. I'll let you go rest now."
    yui "Thank you for yesterday, [mc]."
    mc "You're welcome."
    yui "See you around."
    mc "Yeah."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_141 with dissolve
    u "...Alright, let's get some rest."
    u "However, this outfit feels a little uncomfortable. I should get changed."
    scene black with dissolve
    $ renpy.pause()
    s "*A few hours later*........"
    stop music fadeout 3.0
    jump getbackhome
label getbackhome:
    if ch2ep1krystalkiss == 1:
        jump ch2ep2krystalvisit
    else:
        jump ch2ep2part1ending
label ch2ep2krystalvisit:
    scene ch2ep2_142 with dissolve
    s "*Door knocks*.........."
    u "..................."
    play music "sfx/ch2ep2_1.mp3" fadein 3.0
    $ bgm = "Roa Music - After the rain"
    scene ch2ep2_143 with dissolve
    s "*Door knocks*........."
    u "Hm....? Someone is knocking on my door?"
    scene ch2ep2_144 with dissolve
    mc "Who is it?"
    unknown "It's me..."
    mc "[krystal]?"
    krystal "Yeah, can you open the door, please?"
    mc "...Okay, wait a sec."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_145 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_145.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_145_blink.jpg", 1) with dissolve
    krystal "Hey!"
    mc "...Hey."
    krystal "Did I wake you up?"
    mc "...Not really. I was just about to wake up anyway."
    mc "By the way, why are you here?"
    krystal "Well, I'm here to ask if you want to go outside with me."
    mc "Outside? Where?"
    krystal "It's already evening. Let's go have dinner together."
    mc "..................."
    krystal "What do you say?"
    scene ch2ep2_146 with dissolve
    u "Well, actually, I have a reason to go outside, too..."
    mc "...Alright, let's go to a shopping mall then."
    krystal "Hm? Why does it have to be a shopping mall?"
    krystal "I mean... we can just eat at a restaurant on the street."
    krystal "There are too many people in a shopping mall..."
    mc "Well, I want to buy a new bed. That's why..."
    krystal "..................."
    scene ch2ep2_146_a1 with dissolve
    krystal "*Sighs* Alright, I get it."
    krystal "Let's go to a shopping mall then!"
    krystal "I'm going to grab a cap and a face mask."
    krystal "Let's meet downstairs in five minutes then."
    mc "Okay, sure."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_146_a2 with dissolve
    u "Alright, I've finished changing clothes."
    u "Let's go meet [krystal] downstairs."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_146_a3 with dissolve
    s "*Door closed*..........."
    u "Oh... There she is."
    scene ch2ep2_146_a4 with dissolve
    krystal "Oh? Hi, [mc]."
    krystal "Are you ready now?"
    mc "Yeah. What about you? You didn't forget anything, did you?"
    krystal "I don't think so. I think I've brought everything I need."
    mc "Alright, let's go then."
    scene black with dissolve
    s "*Half an hour later*.........."
    scene ch2ep2_146_a5 with fade
    krystal "Okay... We've arrived at the center of the city now."
    krystal "However, I know very little about this city since I barely come out of the house."
    krystal "Do you know where there is a shopping mall?"
    mc "Yeah, I saw one when walking around the city."
    mc "It's only a ten-minute walk from here."
    krystal "Alright, let's go then."
    mc "Okay."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_146_a6 with dissolve
    krystal "Wow...! This place is pretty big!"
    mc "I thought you were afraid to go to a shopping mall. You seem very excited."
    krystal "Well, I can't help but feel excited. It's been a while since I last went to a shopping mall."
    krystal "You know... I miss shopping so bad!"
    mc "We can do it if you want."
    scene ch2ep2_146_a7 with dissolve
    krystal "No, it's fine. Even though I miss shopping, I don't have anything that I want to buy now."
    krystal "I'll follow you today. Let's go buy your new bed."
    mc "Actually, I'm kind of hungry, so I think we better find something to eat first."
    krystal "Really? Then, what do you want to eat?"
    mc "Why did you ask me that question? You were the one asking me to go out and have a dinner with you."
    mc "So, you should choose what to eat."
    krystal "No! I want you to choose it."
    mc ".................."
    mc "Alright, then...."
    menu:
        "Hot pot":
            scene ch2ep2_146_a8 with dissolve
            mc "I want to have hot pot as a dinner today. Does it sound good to you?"
            mc "I saw the restaurant banner on the second floor."
            krystal "Absolutely! It's been a while since I last had hot pot!"
        "Sushi":
            scene ch2ep2_146_a8 with dissolve
            mc "I want to have sushi as a dinner today. Does it sound good to you?"
            mc "I saw the restaurant banner on the second floor."
            krystal "Absolutely! It's been a while since I last had sushi!"
        "Pizza":
            scene ch2ep2_146_a8 with dissolve
            mc "I want to have pizza as a dinner today. Does it sound good to you?"
            mc "I saw the restaurant banner on the second floor."
            krystal "Absolutely! It's been a while since I last had pizza!"
        "Barbecue":
            scene ch2ep2_146_a8 with dissolve
            mc "I want to have barbecue as a dinner today. Does it sound good to you?"
            mc "I saw the restaurant banner on the second floor."
            krystal "Absolutely! It's been a while since I last had barbecue!"
    scene ch2ep2_146_a9 with dissolve
    krystal "Alright! Let's take that escalator over there!"
    mc "Calm down... There is no need to hurry."
    krystal "Hm? But, didn't you just say you were kind of hungry?"
    mc "I did..."
    krystal "Then, what are you waiting for? Let's go!"
    scene black with dissolve
    $ renpy.pause()
    s "*An hour later*.........."
    scene ch2ep2_146_a10 with dissolve
    krystal "Ahh~! I'm so full~!"
    mc "Yeah, you should be full."
    mc "You made me confused if it was me or you who was very hungry."
    mc "You ate as if there was no tomorrow."
    scene ch2ep2_146_a11 with dissolve
    krystal "*Giggles* That's a bit rude to say to a girl, [mc]!"
    mc "Well, I was just saying what I saw..."
    krystal "*Giggles* I was just kidding! Don't be so serious!"
    krystal "It was my first meal of the day, so yeah I admit it."
    krystal "I was the one who was very hungry."
    mc "I'm not surprised to hear that...."
    scene ch2ep2_146_a12 with dissolve
    krystal "Oh....?!"
    mc "Hm? What now?"
    scene ch2ep2_146_a13 with dissolve
    krystal "Look over there! It's an ice cream shop!"
    krystal "Wow... It looks very delicious."
    krystal "I want to try it!"
    mc "But, didn't you just say that you were full...?"
    scene ch2ep2_146_a14 with dissolve
    krystal "*Giggles* A woman always has room for dessert!"
    krystal "Let's go take a look, [mc]!"
    mc "O-Oh... Okay."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_146_a15 with dissolve
    krystal "Mmmmmm~~~"
    mc "Is it that delicious?"
    mc "You look like you really enjoy eating it."
    scene ch2ep2_146_a16 with dissolve
    krystal "Of course, it is!"
    krystal "You made the wrong choice not buying one."
    mc "Well, I'm not that into dessert."
    krystal "*Giggles* That's bad for you. You've just missed such a delicious thing!"
    mc "You're over-exaggerating..."
    scene ch2ep2_146_a17 with dissolve
    krystal "No, I'm not!"
    krystal "Try it if you don't believe me!"
    mc "No, I'm good."
    krystal "Why? Are you scared that you'll have to admit that I wasn't over-exaggerating?"
    mc "Scared? Who? Me?"
    krystal "Yeah!"
    mc "Alright, I will take a bite then."
    scene ch2ep2_146_a18 with dissolve
    krystal "*Giggles* Hahaha! Got you!"
    mc "...What are you talking about?"
    krystal "I was just teasing you! I wasn't actually going to let you try it."
    mc "...................."
    scene ch2ep2_146_a19 with dissolve
    krystal "I'm sorry, [mc]. This ice cream is just way too delicious to share it with you."
    mc "..................."
    krystal "Mmmmm~! So delicious~!"
    mc "Really? You really have to play it this way?"
    krystal "*Giggles* Hm? What are you talking about? I don't understa-"
    scene ch2ep2_146_a20 with dissolve
    krystal "!!!!!!!!"
    scene ch2ep2_146_a21 with dissolve
    mc "Alright, I admit that you weren't just exaggerating."
    krystal ".................."
    mc "It was very delicious, like you said."
    krystal ".................."
    mc "Thank you for sharing it with me. I might buy one if I have an opportunity later."
    krystal ".................."
    scene ch2ep2_146_a22 with dissolve
    mc "Alright, let's not waste any more time here."
    mc "It's time to go looking for my new bed."
    krystal "................."
    krystal "...H-Hm? Where are you going, [mc]?"
    mc "...Didn't you hear what I said? I'm going to buy a bed."
    krystal "O-Oh! O-Okay...!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_146_a23 with dissolve
    sales "Thank you, sir."
    sales "Your bed will be delivered to your house tomorrow in the evening."
    mc "Got it."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_146_a24 with dissolve
    mc "Are you sure that you don't want to buy anything?"
    krystal "Yeah. I can't think of anything right now."
    mc "Okay then, shall we go home now?"
    krystal "Yeah, sure. Let's go."
    scene black with dissolve
    $ renpy.pause()
    s "*Half an hour later*.........."
    stop music fadeout 3.0
    scene ch2ep2_146_a25 with dissolve
    krystal "We're finally back!"
    krystal "Let's get inside, [mc]."
    mc "Okay...."
    play music "sfx/ch2ep2_5.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - I Saw A Ghost Last Night"
    scene ch2ep2_146_a26 with dissolve
    mc "Hm....?"
    scene ch2ep2_146_a27 with dissolve
    mc ".................."
    krystal "What's wrong? Why did you suddenly stop walking?"
    krystal "It's getting cold out here. Let's get inside the house."
    scene ch2ep2_146_a28 with dissolve
    mc "Then, you should go inside first. Don't worry about me."
    krystal "Hm? Is there anything wrong?"
    mc "No, there is nothing wrong. Everything is fine."
    mc "I just want to smoke for a sec before going inside."
    krystal "Hm? I never knew you smoked...."
    mc "Well, I don't often smoke. That's why."
    krystal "...................."
    krystal "...Okay then, but don't stay out here too long, okay?"
    krystal "You might catch a cold if you do."
    mc "Understood."
    $ ch2ep2shoppingmallwithkrystal = 1
    $ krystal_relationship += 2
    $ krystal_ch2_ep2 += 2
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_146_a29 with dissolve
    papa "(Well... Well... What a bunch of good pictures I've got.)"
    papa "(I went so many places and asked so many people around about her.)"
    papa "(Even though I didn't get that many useful answers, still those answers brought me here.)"
    papa "(I've been waiting here for so many days. Now, my effort and patience have finally paid off!)"
    scene ch2ep2_146_a30 with dissolve
    papa "(People have been wondering where she is right now after the truth about her was exposed.)"
    papa "(Who would've thought that she is living with a guy!)"
    papa "(Hehehe... These pictures are absolutely worth a million! I'm surely going to be rich now!)"
    papa "(Now, let's get the hell out of here.)"
    scene ch2ep2_146_a31 with dissolve
    mc "Who are you? Are you a [krystal] hater? What are you doing here?"
    papa "!!!!!!!"
    papa "(F-Fuck...! How did he know that I was here?!)"
    scene ch2ep2_146_a32 with dissolve
    papa "(I can't get caught, otherwise all my efforts are going to be wasted!)"
    mc "...Where do you think you are going?"
    papa "N-No...!!"
    scene ch2ep2_146_a33 with dissolve
    papa "Ouch....! It hurts...!"
    scene ch2ep2_146_a34 with dissolve
    mc "Look what you've got here..."
    mc "What were you planning to do with these pictures?"
    mc "Forget it. It doesn't matter what you were going to do, since I'm going to delete these pictures anyway."
    papa "W-Wait!!"
    scene ch2ep2_146_a35 with dissolve
    papa "S-Stop!!!"
    mc "Relax. Don't get up just yet. I'm not finished deleting these pictures yet."
    mc "Wait... Actually, I should just take the memory card out instead."
    papa "Ugh...! Let me go!"
    papa "Don't you know that hurting other people is against the law? I'm going to sue you!"
    mc "Well then, don't you know that taking a picture of someone else without his/her permission is also against the law, too?"
    papa "What the fuck are you talking about?! That's bullshit! It's a part of my job!"
    mc "Oh, you're a paparazzi then?"
    papa "So what?! What the fuck are you going to do about it?!"
    mc "Nothing. I was just trying to figure out who you are."
    papa "Ugh!! Take your fucking feet off me, and give me my camera back!"
    scene ch2ep2_146_a36 with dissolve
    mc "Alright then, take it back."
    papa "N-No! What the fuck are you doing?!"
    papa "Don't throw it like that!"
    scene ch2ep2_146_a37 with dissolve
    papa "*Sighs* Oh, my poor baby... Did you get hurt?"
    mc "..................."
    mc "(This guy is completely crazy. He's talking to a camera...)"
    scene ch2ep2_146_a38 with dissolve
    papa "Hey! Why the fuck did you do that?!"
    papa "What if I couldn't catch it?! What if it hit the ground?!"
    papa "You have no idea how much my baby costs!"
    mc "I don't care about it."
    papa "Of course, you don't! Because a low-life shit asshole like you wouldn't be able to afford it!"
    scene ch2ep2_146_a39 with dissolve
    mc "Say whatever you want."
    mc "Here is the money for your memory card that I took."
    papa "Ugh...!"
    scene ch2ep2_146_a40 with dissolve
    papa "Fuck! Where are you going?! We haven't finished talking yet!"
    papa "You have to go to a police station with me!"
    mc "Just go there alone and sue me if you really want to. But, you will regret it."
    papa "A-Are you threatening me?!"
    mc "No, I'm not. I'm just warning you."
    mc "Oh... and don't you dare come back here ever again."
    mc "Otherwise, I won't just take out a memory card, but break your beloved camera next time."
    papa "Ugh...!"
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    s "*Half an hour later*..........."
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    scene ch2ep2_147 with fade
    u "*Sighs*...Finally, I've got some time alone."
    u "I can continue with my plan now."
    u "I've already put it in the bag."
    scene ch2ep2_148 with dissolve
    u "Now, there is only one more thing that I need to do."
    u "I need to call {b}him.{/b}"
    s "*Door knocks*..........."
    scene ch2ep2_149 with dissolve
    u "Hm...?"
    mc "Who's it?"
    krystal "It's me again."
    mc "[krystal]?"
    krystal "Yeah... I have something really important to ask you. Can I come in?"
    scene ch2ep2_150 with dissolve
    mc "*Sighs*......"
    mc "Come on in. The door isn't locked."
    krystal "Oh! Okay!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_150_a1 with dissolve
    krystal "Hi again!"
    mc "What's up."
    mc "What did you want to ask me, by the way?"
    krystal "Er... May I take a seat first?"
    mc "Oh.. Okay."
    scene ch2ep2_150_a2 with dissolve
    mc "So, what did you want to ask me?"
    krystal "Umm... Err..."
    krystal "I thought I was going to ask you, but I'm not sure if I should now..."
    mc "What are you afraid of then?"
    krystal "It's not because I'm afraid of asking, it's just...."
    scene ch2ep2_150_a3 with dissolve
    krystal "...O-Oh! What is in that bag?"
    mc ".................."
    mc "Nothing important. It's just a suit."
    krystal "Hm? Can I see it?"
    mc ".................."
    scene ch2ep2_150_a4 with dissolve
    mc "Stop changing the subject, [krystal]."
    mc "Did you say that you had something really important to ask me? Just go ahead."
    krystal "*Sighs* Okay...."
    krystal "I wanted to ask to make sure if... you are really... single..."
    mc "..................."
    scene ch2ep2_150_a5 with dissolve
    mc "That's it? Was that something you really wanted to ask?"
    krystal "Yeah... I really wanted to know the answer."
    mc "Yes, I am single."
    krystal "...Really?"
    mc "You don't believe me?"
    krystal "O-Of course, I do!"
    krystal "It's just... there are many beautiful girls around you."
    krystal "So, I was curious if you were dating anyone...."
    mc "No, I'm not dating anyone."
    scene ch2ep2_150_a6 with dissolve
    if ch2ep1rinsex == 1:
        krystal "(...Well, there are many people who have sex without loving each other.)"
        krystal "(I guess [mc] and [rin] are in that case, too.)"
    krystal "*Sighs* That was such a relief..."
    mc "Why?"
    krystal "Well, I'm telling you the truth now, [mc]."
    krystal "I really really like you. You're the best guy I've ever met."
    krystal "I wanted to know your answer so that I could start thinking about our relationship seriously."
    mc "...................."
    krystal "I know it's still too early for you to think about it, [mc]."
    krystal "But, I really want to build a future with you."
    mc "I...."
    krystal "You don't need to give me your answer now. I'll give you time to think about it as long as you want."
    krystal "But, please don't reject me now, can you?"
    mc "Okay.... I will think about it."
    krystal "Thank you. I really appreciate that."
    scene ch2ep2_150_a7 with dissolve
    krystal "By the way! No matter how much I thought about it, I'm pretty sure that you don't smoke, [mc]."
    krystal "I mean... I've never smelt smoke when hanging out with you."
    krystal "So, what actually happened really? Why did you tell me to come in the house first?"
    krystal "Where did you go?"
    mc "Are you sure that you want to know about it?"
    krystal "Yeah, just tell me."
    mc "Alright then..."
    scene ch2ep2_150_a8 with dissolve
    mc "I noticed that there was a paparazzi taking pictures of us... actually, of you to be exact."
    mc "It wasn't going to be good for you if those pictures were leaked out."
    mc "So, I went to delete some pictures and eventually take a memory card from him."
    mc "Here is the memory card. You should keep it."
    krystal "Oh..."
    scene ch2ep2_150_a9 with dissolve
    krystal "Thank you so much, [mc]..."
    mc "You're welcome."
    krystal "You're right. Things would get worse if the pictures were leaked out."
    krystal "But, don't get me wrong. It's not like I don't want to have a picture with you."
    krystal "I'm just afraid that it would cause you problems..."
    mc "I see... Thank you for worrying about me."
    krystal "[mc]....."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_150_a10 with dissolve
    krystal "Kiss me...."
    mc "...Wait. Why so sudden?"
    krystal "I can't help it. You just made me like you even more..."
    mc ".................."
    menu:
        "Kiss her [krystal2]":
            $ ch2ep2sexwithkrystal = 1
            $ krystal_relationship += 2
            $ krystal_ch2_ep2 += 2
            stop music fadeout 3.0
            jump ch2ep2krystalsex
        "Not today":
            $ ch2ep2sexwithkrystal = 2
            scene ch2ep2_150_a10_d1 with dissolve
            mc "I'm sorry, [krystal]."
            krystal "...Why?"
            mc "Not today. I'm pretty tired now..."
            krystal "Oh, I see..."
            scene ch2ep2_150_a10_d2 with dissolve
            mc "I'm sorry."
            krystal "It's alright. I understand it."
            krystal "I'm going to leave then, so that you can have some rest."
            krystal "Let's talk later, okay?"
            mc "Yeah sure."
            krystal "Good night, [mc]."
            mc "Have a good night, [krystal]."
            jump ch2ep2part1ending
label ch2ep2krystalsex:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    play music "sfx/ch2ep2_6.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - Sicked & Tired (ft. Lily Hain)"
    scene ch2ep2_150_a10_a1 with dissolve
    krystal "*Kisses* Mmmmm.... [mc]...."
    mc "*Kisses* [krystal]...."
    krystal "*Kisses* I want to... do it..."
    mc "*Kisses* Are you sure about that?"
    krystal "*Kisses* Mmmm... Yeah, please do me. I'm yours for today..."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_150_a10_a2 with dissolve
    krystal "*Smiles* This is so embarrassing..."
    mc "...Why?"
    krystal "*Blushes* I know that we've had done it before, but I'm still not used to being naked in front of you..."
    mc "You will get used to it soon..."
    krystal "*Giggles* Hm? Will there be a next time?"
    mc "That's your choice..."
    krystal "*Giggles* I feel very important now!"
    mc "Let's take a seat on the bed..."
    scene ch2ep2_150_a10_a3 with dissolve
    mc "Shall we start now?"
    krystal "Hm? What do you want to do?"
    mc "Can you spread your legs a little bit wider?"
    krystal "*Giggles* Okay..."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_150_a10_a4 with dissolve
    show ch2ep2_krystal1 with dissolve
    window hide
    krystal "*Softly breathes* A-Ah....."
    mc "How do you feel?"
    krystal "*Softly breathes* G-Good... I like it..."
    $ renpy.pause()
    menu:
        "Next":
            krystal "*Softly breathes* Mmmm... Let me do it for you, too..."
    hide ch2ep2_krystal1
    scene ch2ep2_150_a10_a5 with dissolve
    show ch2ep2_krystal2 with dissolve
    window hide
    krystal "*Softly breathes* Ahhh... What about you? Do you feel good?"
    mc "Yeah, your hand is so soft... It feels so good."
    $ renpy.pause()
    menu:
        "Next":
            mc "Alright, I think that's enough warming up."
            krystal "*Softly breathes* Okay then, what do you want me to do?"
            mc "Can you lie down on your right side?"
            krystal "*Softly breathes* Sure..."
    hide ch2ep2_krystal2
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_150_a10_a6 with dissolve
    krystal "Like this...?"
    mc "Yeah, are you ready? I'm going to put it in."
    krystal "Yes, please..."
    scene ch2ep2_150_a10_a7 with dissolve
    krystal "*Softly breathes* A-Ahh...!"
    mc "It's in..."
    krystal "*Softly breathes* Hehe... Yeah..."
    mc "Should I start moving now?"
    krystal "*Softly breathes* Go ahead if that's what you want to..."
    mc "Okay then..."
    scene ch2ep2_150_a10_a8 with dissolve
    show ch2ep2_krystal3 with dissolve
    window hide
    krystal "*Softly breathes* Mmmm... [mc]...."
    mc "Are you okay? Does it hurt?"
    krystal "*Softly breathes* Ahhh... A little bit, but not as much as the first time."
    krystal "*Softly breathes* Mmmm... You can keep moving. Don't worry about me."
    $ renpy.pause()
    menu:
        "Next":
            mc "Okay then, I'm going to move a little bit faster."
    hide ch2ep2_krystal3
    scene ch2ep2_150_a10_a9 with dissolve
    show ch2ep2_krystal4 with dissolve
    window hide
    krystal "*Softly breathes* Arrr...! It's getting better now...!"
    krystal "*Softly breathes* [mc]... [mc]..."
    mc "Hm...?"
    krystal "*Softly breathes* Mmmm... N-Nothing... It just feels so good..."
    $ renpy.pause()
    menu:
        "Next":
            krystal "*Softly breathes* F-Faster...! I want you to do me faster, please...!"
            mc "Okay... As you wish..."
    hide ch2ep2_krystal4
    scene ch2ep2_150_a10_a10 with dissolve
    show ch2ep2_krystal5 with dissolve
    window hide
    krystal "*Heavily breathes* Mmmmm...! [mc]...!"
    krystal "*Heavily breathes* Ahh... This is too good...!"
    krystal "*Heavily breathes* Y... You're driving me crazy...!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_krystal5
    scene ch2ep2_150_a10_a11 with dissolve
    krystal "*Heavily breathes* H... Hang on a sec..."
    mc "Hm..? What's wrong?"
    krystal "*Heavily breathes* I want to do it for you..."
    mc "Alright then, get on me."
    krystal "*Giggles* Of course...!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_150_a10_a12 with dissolve
    show ch2ep2_krystal6 with dissolve
    window hide
    $ renpy.pause(1.7, hard=True)
    scene ch2ep2_150_a10_a12_1 with dissolve
    hide ch2ep2_krystal6
    krystal "*Softly breathes* Ahhh... It finally went in..."
    mc "Does it still hurt?"
    krystal "*Softly breathes* N...No, it doesn't hurt anymore..."
    mc "Good for you, then."
    krystal "*Giggles* I'm going to start moving now..."
    scene ch2ep2_150_a10_a13 with dissolve
    show ch2ep2_krystal7 with dissolve
    window hide
    krystal "*Softly breathes* Mmmmm.... Mmmmm...."
    krystal "*Softly breathes* Ahhh... Are you enjoying it?"
    mc "Absolutely...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_krystal7
    scene ch2ep2_150_a10_a14 with dissolve
    show ch2ep2_krystal8 with dissolve
    window hide
    krystal "*Heavily breathes* Ahhh~! This is sooo good~!"
    mc "Shhh... Don't shout too loud. We're not alone in the house."
    krystal "*Heavily breathes* I know, but...! It's hard to...!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_krystal8
    scene ch2ep2_150_a10_a15 with dissolve
    show ch2ep2_krystal9 with dissolve
    window hide
    krystal "*Moans* [mc]...! [mc]...!"
    krystal "*Heavily breathes* Mmmmm~! I...I'm about to cum...!"
    mc "Ugh..! Me, too..."
    $ renpy.pause()
    menu:
        "Side fuck":
            hide ch2ep2_krystal9
            jump ch2ep2krystalsidefuck1
        "Slowest":
            hide ch2ep2_krystal9
            jump ch2ep2krystalcowgirl1
        "Slower":
            hide ch2ep2_krystal9
            jump ch2ep2krystalcowgirl2
        "Cum":
            jump ch2ep2krystalcowgirlcum
label ch2ep2krystalsidefuck1:
    scene ch2ep2_150_a10_a8 with dissolve
    show ch2ep2_krystal3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch2ep2_krystal3
            jump ch2ep2krystalcowgirl1
        "Faster":
            hide ch2ep2_krystal3
            jump ch2ep2krystalsidefuck2
        "Fastest":
            hide ch2ep2_krystal3
            jump ch2ep2krystalsidefuck3
label ch2ep2krystalsidefuck2:
    scene ch2ep2_150_a10_a9 with dissolve
    show ch2ep2_krystal4 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch2ep2_krystal4
            jump ch2ep2krystalcowgirl1
        "Slower":
            hide ch2ep2_krystal4
            jump ch2ep2krystalsidefuck1
        "Faster":
            hide ch2ep2_krystal4
            jump ch2ep2krystalsidefuck3
label ch2ep2krystalsidefuck3:
    scene ch2ep2_150_a10_a10 with dissolve
    show ch2ep2_krystal5 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch2ep2_krystal5
            jump ch2ep2krystalcowgirl1
        "Slowest":
            hide ch2ep2_krystal5
            jump ch2ep2krystalsidefuck1
        "Slower":
            hide ch2ep2_krystal5
            jump ch2ep2krystalsidefuck2
label ch2ep2krystalcowgirl1:
    scene ch2ep2_150_a10_a13 with dissolve
    show ch2ep2_krystal7 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Side fuck":
            hide ch2ep2_krystal7
            jump ch2ep2krystalsidefuck1
        "Faster":
            hide ch2ep2_krystal7
            jump ch2ep2krystalcowgirl2
        "Fastest":
            hide ch2ep2_krystal7
            jump ch2ep2krystalcowgirl3
label ch2ep2krystalcowgirl2:
    scene ch2ep2_150_a10_a14 with dissolve
    show ch2ep2_krystal8 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Side fuck":
            hide ch2ep2_krystal8
            jump ch2ep2krystalsidefuck1
        "Slower":
            hide ch2ep2_krystal8
            jump ch2ep2krystalcowgirl1
        "Faster":
            hide ch2ep2_krystal8
            jump ch2ep2krystalcowgirl3
label ch2ep2krystalcowgirl3:
    scene ch2ep2_150_a10_a15 with dissolve
    show ch2ep2_krystal9 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Side fuck":
            hide ch2ep2_krystal9
            jump ch2ep2krystalsidefuck1
        "Slowest":
            hide ch2ep2_krystal9
            jump ch2ep2krystalcowgirl1
        "Slower":
            hide ch2ep2_krystal9
            jump ch2ep2krystalcowgirl2
        "Cum":
            jump ch2ep2krystalcowgirlcum
label ch2ep2krystalcowgirlcum:
    if ch2ep1rinsex == 1:
        jump ch2ep2rinfindout
    else:
        mc "Where do you want me to cum?"
        krystal "*Heavily breathes* A... Anywhere! You can cum either inside or outside. Your choice!"
        menu:
            "Cum inside":
                hide ch2ep2_krystal9
                scene black with dissolve
                $ renpy.pause()
                scene ch2ep2_150_a10_a18_in with vpunch
            "Cum outside":
                hide ch2ep2_krystal9
                scene black with dissolve
                $ renpy.pause()
                scene ch2ep2_150_a10_a18_out with vpunch
        mc "Ugh..! I'm cumming...!"
        krystal "*Moans* Mmmmmm!!! Me, too~~~~!!"
        krystal "*Pants*..............."
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep2_150_a10_a19 with dissolve
        krystal "*Pants* That was... so... good..."
        krystal "*Pants* I... loved... it."
        mc "So did I."
        krystal "*Pants* C..Can we stay... like this for... like five minutes...? I'm so...tired now..."
        mc "...Yeah, sure."
        jump ch2ep2krystalcowgirlfinish
label ch2ep2rinfindout:
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_150_a10_a16 with fade
    rin "(It's been a while since the last time I hung out with [mc].)"
    rin "(I was hoping to spend time with him this weekend, but he seemed pretty busy.)"
    rin "(I think this is the time he is finally free.)"
    rin "(Let's go to his room....)"
    scene ch2ep2_150_a10_a17 with dissolve
    rin "(Hm...? Why is the door ajar?)"
    s "*Strange sounds*........."
    rin "(Wait... What was that strange voice coming out of his room?)"
    rin "(Is there something happening to him? Let's go check real quick.)"
    scene ch2ep2_150_a10_a18 with dissolve
    show ch2ep2_krystal10 with dissolve
    rin "(W-What!!!???)"
    krystal "*Heavily breathes* Almost there...! [mc]...!"
    rin "(W... W... What is happening right now?! Why is [krystal] having sex with [mc]?!)"
    rin "(Am I dreaming? Is this actually happening? Since when have they been doing this?!)"
    menu:
        "Cum inside":
            hide ch2ep2_krystal9
            scene black with dissolve
            $ renpy.pause()
            scene ch2ep2_150_a10_a18_in with vpunch
        "Cum outside":
            hide ch2ep2_krystal9
            scene black with dissolve
            $ renpy.pause()
            scene ch2ep2_150_a10_a18_out with vpunch
    mc "Ugh..! I'm cumming...!"
    krystal "*Moans* Mmmmmm!!! Me, too~~~~!!"
    krystal "*Pants*..............."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_150_a10_a19 with dissolve
    krystal "*Pants* That was... so... good..."
    krystal "*Pants* I... loved... it."
    mc "So did I."
    krystal "*Pants* ...Alright, I'm going to get up n-"
    scene ch2ep2_150_a10_a20 with dissolve
    krystal "!!!!!!!"
    scene ch2ep2_150_a10_a21 with dissolve
    krystal "(Oh my god! Isn't that [rin]?! Since when has she been watching us?!)"
    mc "Hm? What's wrong?"
    krystal "*Pants* N-Nothing!"
    krystal "*Pants* C..Can we stay... like this for... like five minutes...? I'm so...tired now..."
    mc "...Yeah, sure."
    jump ch2ep2krystalcowgirlfinish
label ch2ep2krystalcowgirlfinish:
    scene black with dissolve
    s "*A few minutes later*........."
    scene ch2ep2_150_a10_a22 with dissolve
    krystal "Alright, it's getting late now."
    krystal "I think I should just leave."
    mc "Okay. See you tomorrow then."
    krystal "Good night, [mc]."
    mc "You, too."
    $ renpy.end_replay()
    $ krystal_relationship += 2
    $ krystal_ch2_ep2 += 2
    jump ch2ep2part1ending
label ch2ep2part1ending:
    scene black with dissolve
    $ renpy.pause()
    if ch2ep2sexwithkrystal == 0:
        scene black with dissolve
        s "*Later on Sunday night*........."
        scene ch2ep2_147 with fade
        u "*Sighs*...Finally, I've got some time alone."
        u "I can continue with my plan now."
        u "I've already put it in the bag."
        scene ch2ep2_148 with dissolve
        u "Now, there is only one more thing that I need to do."
        u "I need to call {b}him.{/b}"
    elif ch2ep2sexwithkrystal == 1 or ch2ep2sexwithkrystal == 2:
        scene ch2ep2_151 with dissolve
        u "...Alright, I think no one else will come and interrupt me anymore."
        u "Let's just call {b}him{/b} so that I can continue with the plan."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_152 with fade
    show ch2ep2_pt1ending with dissolve
    g1 "*Moans* Ahhhh...! Ahhhh...!"
    g2 "*Moans* Mmmmm...! D..Don't stop...! Keep fucking me like that, handsome...!"
    unknown "*Softly breathes* Ugh...! Your pussy is squeezing my cock so hard...!"
    g2 "*Moans* Ahhh~! I can't help it...! Your cock feels too good...!"
    scene ch2ep2_153 with dissolve
    hide ch2ep2_pt1ending
    $ renpy.sound.play("sfx/phone vibrating.mp3")
    s "*Phone vibrates*............"
    unknown "Hm...?"
    unknown "Tch..! Who the fuck is calling me at this time?"
    unknown "Wait a sec. I need to pick up my call."
    g1 "Whatever you say, handsome~"
    stop sound
    scene black with dissolve
    scene ch2ep2_154 with dissolve
    unknown "What's going on? Is today the day the world will end?"
    unknown "It's been so long that I can't remember since you called me first, [mc]."
    g2 "*Moans* Ahhh...! Ahhh...!"
    unknown "Hm? What was that sound? Nothing. You don't need to worry about it."
    unknown "I'm more interested in the reason that made you call me."
    unknown "Stop wasting time, and tell me already."
    scene ch2ep2_155 with dissolve
    mc "*Sighs* Alright then, listen carefully..."
    mc "I need you to copy someone's handprint for me..."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_156 with dissolve
    stop music fadeout 3.0
    mc "How long does it take until you can send it to me?"
    mc "Alright, got it. Thanks for your help in advance, [lucas]."
    mc "Don't worry. I will repay your favor later."
    mc "See you tomorrow."
    scene black with dissolve
    $ renpy.pause()
    s "*Next morning*.........."
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa Music - Summer Days"
    scene ch2ep2_157 with fade
    u "The weekend went by really fast. It's Monday again."
    u "I didn't even get enough time to rest."
    u "*Sighs* Whatever. Let's just get to work."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_158 with dissolve
    zeke "Oh! Yo! What's up, dude!"
    mc "....Hm?"
    mika "Good morning, [mc]."
    scene ch2ep2_159 with dissolve
    mc "Good morning, [mika]."
    zeke "How was your weekend, bro?"
    zeke "I haven't seen you at all until now."
    scene ch2ep2_160 with dissolve
    if ch2ep2visityuiparents == True:
        mc "Well, I went to visit [yui]'s parents this weekend."
        zeke "W-What?! I didn't know you two were dating. When did it start?"
        mc "No, we aren't dating."
        zeke "Then, why did you go to visit her parents?"
        mc "Well, she thought her parents were going to make her get engaged. So, she asked me to pretend to be her boyfriend."
        zeke "I see...."
    else:
        mc "Nothing much. I just hung out in my room."
        zeke "I see...."
    scene black with dissolve
    if ch2ep2sexwithkrystal == 1:
        scene ch2ep2_160_a1 with dissolve
        mika "Sorry to interrupt, but can we continue this in the kitchen, please?"
        mika "I'm kind of hungry."
        zeke "Oh! My bad."
        zeke "But hey, you can head there first if you want. There is no need to wait for me."
        mika "Are you sure?"
        zeke "Yeah, I need to talk to [mc] about something in private."
        mika "Alright then, see you downstairs."
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep2_160_a2 with dissolve
        zeke "Oh my god...."
        mc "Hm? What's wrong?"
        zeke "Nothing. I just can't believe that she is actually my girlfriend now."
        mc "Why? Are you not happy with her?"
        zeke "No. No. Don't get me wrong. I'm extremely happy that she is my girlfriend."
        zeke "To be dating a girl I've had a crush on for so many years, it just feels... like a dream. You know?"
        zeke "She's so beautiful and sweet. I've become a better person because of her."
        mc "...................."
        scene ch2ep2_160_a3 with dissolve
        mc "Did you just keep me here to make me listen to you admiring your girlfriend?"
        zeke "Of course not!"
        mc "Then, what was that something you wanted to ask me?"
        zeke "You know... you've been here a while already."
        zeke "Have you got yourself a girlfriend yet?"
        mc "No, I haven't."
        zeke "W-What?! Why not?"
        zeke "You seem to get along with everyone quite well. Don't you have any girl that you're interested in?"
        zeke "[rin]? [yui]? [eira]? [elaine]? Anyone?"
        mc "Why do you want me to date someone that much?"
        zeke "Well, to be honest... even though you've become a little bit more open to us, I'm still feeling like you have a burden on your heart."
        zeke "I want you to be happy, bro. I really do."
        zeke "And I think dating could help you! Look at me as an example! Look at how happy I am!"
        zeke "Just tell me who you are interested in. I will help you and make sure that you and her get along well!"
        mc "...................."
        mc "......Then, how about [krystal]?"
        zeke "..................."
        scene ch2ep2_160_a4 with dissolve
        zeke "Pffff!!!"
        zeke "*Laughs* Oops! Hahahahaha!!"
        mc "...................."
        zeke "*Laughs* I-I'm sorry! I know that I shouldn't be laughing at you, b-but it's too funny..!"
        zeke "*Laughs* You're surely a dreamer, bro!"
        scene ch2ep2_160_a5 with dissolve
        zeke "I can help you with anyone, but [krystal]..."
        zeke "She's way out of your league, bro!"
        mc "...................."
        zeke "Do you really like her that much?"
        mc "No, I was just asking. I don't.... have any special feeling for her."
        zeke "Really? Are you really sure about that?"
        mc "...................."
        scene ch2ep2_160_a6 with dissolve
        zeke "Come on, man! I know that I was making fun of you."
        zeke "But if you really like her, then go for it!"
        mc ".... Thanks for worrying about me, but I'm good."
        mc "I'm really not interested in dating anyone."
        zeke ".... For real?"
        mc "Yeah....."
        zeke "Alright, I respect your decision. If you are happy being alone, then go with it!"
        mc ".... Thanks."
        zeke "... Well, to be honest after hearing you say that, I had some crazy thoughts."
        mc "Crazy thoughts?"
        zeke "Yeah, if it wasn't for last night, I would've thought you were gay!"
        mc "What are you talking about?"
        scene ch2ep2_160_a7 with dissolve
        zeke "Come on! There is no need to play dumb! I know what you did last night."
        mc "...................."
        zeke "You damn bastard, [mc]...."
        mc "....................."
        zeke "How could you have done that when [mika] and I were in the room right next to you?"
        u "Shit.... Did he know that I was having sex with [krystal]?"
        u "He must've been very angry... She is his favorite idol."
        scene ch2ep2_160_a8 with dissolve
        zeke "I know that it's normal for a man to watch porn, but could you please at least lower the volume down?!"
        zeke "You have no idea how awkward we were last night!"
        mc "..................."
        zeke "I wanted to jump on the bed so bad, but I couldn't do that! It's still too fast for us!"
        mc "..... I'm sorry."
        zeke "Yeah, you should be! But, don't forget to lower the volume next time, okay?!"
        mc ".... Got it."
    else:
        scene ch2ep2_160_d1 with dissolve
        zeke "Alright, let's go downstairs first."
        zeke "I'm starting to feel a bit hungry. We can keep talking in the kitchen."
        mc "About that.... I'm not having breakfast today."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_161 with dissolve
    u "..................."
    s "While you watched TV, waiting for everyone to finish their breakfast, you heard some footsteps..."
    scene ch2ep2_162 with dissolve
    mc "Oh, it's you...."
    mc "Good morning, [rin]."
    mc "You already finished your breakfast?"
    scene ch2ep2_163 with dissolve
    rin "..................."
    mc "................."
    u ".... Hm? What's wrong with her? Why is she looking so upset?"
    mc ".... What's w-"
    scene ch2ep2_164 with dissolve
    rin "................."
    mc "..................."
    u ".... She just ignored me and walked past me like that."
    u "This is so unusual of her. What's going on?"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_165 with dissolve
    zeke "What are you doing, [mc]?"
    zeke "Let's go. Stop staring blankly at the door already."
    mc "Oh... Okay...."
    zeke "... What's wrong? Why do you look so confused?"
    scene ch2ep2_166 with dissolve
    mc "Do you know what's going on with [rin]?"
    mc "I talked to her, but she seemed angry and ignored me."
    zeke "Hm? Really?"
    mc "Yeah. She's never been like that."
    scene ch2ep2_167 with dissolve
    zeke "Umm... I didn't notice that at first, but now that I think about it, you're right."
    zeke "She seemed upset when we were having breakfast in the kitchen, too."
    zeke "Usually, she always talks and smiles, but she was very quiet today."
    yui "... I noticed that, but I didn't dare to say anything. She was so scary!"
    scene ch2ep2_168 with dissolve
    zeke "Did you guys have a fight?"
    mc "Who? Me?"
    zeke "Yeah. Did you fight with her?"
    mc "No, I didn't."
    zeke "That's weird... Then, why was she like that?"
    scene ch2ep2_169 with dissolve
    mika "I think I know the reason."
    zeke "Hm? Really?"
    mika "Yeah, I think she is on her period."
    zeke "... I don't think so. I've known her for many years, I've never seen her have a bad mood while she was on her period."
    mika "Who knows? You can't say that for sure. A girl's reaction to her period is unpredictable."
    yui "Yeah, I agree with you. I tend to get angry very easy when I'm on my period, as well."
    scene ch2ep2_170 with dissolve
    mika "I think that's the case, [mc]."
    mika "Don't worry about her. She will be fine in the next few days."
    zeke "[yui]."
    yui "... Hm?"
    zeke "What you said earlier... Does that mean you're always on your period?"
    zeke "*Laughs* Because you seem to always be angry!"
    yui "Y-You!!!"
    zeke "*Laughs* Hahaha! Chill! I was just kidding!"
    yui "Tch...!"
    scene ch2ep2_171 with dissolve
    zeke "Alright, I think we should get going now."
    zeke "[rin] is waiting for us and I'm sure that you guys don't want to keep her waiting long."
    yui "... Well, I agree with you on that."
    mc "Okay. Let's go then."
    scene black with dissolve
    $ renpy.pause()
    s "*A few hours later*............."
    scene ch2ep2_172 with fade
    u "................."
    u "... Alright, I've been working for a while."
    u "It's not good to sit still for too long. Let's just go walk around."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_173 with dissolve
    u "Well, I know I decided to go walking around."
    u "But, where should I go...?"
    u "Oh... Let's just go buy a soda to drink to regain my energy."
    unknown ".... No!!!"
    scene ch2ep2_174 with dissolve
    u "... Hm? What was that?"
    u "Someone was yelling from the above floor. Is something bad happening?"
    u "What should I do?"
    menu:
        "[smgr]Walk upstairs to check":
            $ ch2ep2fayeonphone = 1
            stop music fadeout 3.0
            scene ch2ep2_174_a1 with dissolve
            play music "sfx/ch2ep2_4.mp3" fadein 3.0
            $ bgm = "LiQWYD - Lay Me Down"
            u "...................."
            u "... Well, let's just go check what's going on for a bit."
            scene ch2ep2_174_a2 with dissolve
            u "Oh, it's [faye]..."
            u "Looks like she's on a call."
            u "I wonder who she is talking to that made her yell like that."
            scene ch2ep2_174_a3 with dissolve
            faye "No! I don't believe you!"
            faye "You always said it was the last time!"
            faye "Don't you ever call me again!"
            u "I think I better lea-"
            scene ch2ep2_174_a4 with dissolve
            faye "... [mc]?!"
            u "... Well, too late."
            faye "What are you doing up here?"
            mc "I'm sorry. I didn't mean to eavesdrop..."
            mc "I heard someone yelling, so I thought that something bad might be going on, so..."
            scene ch2ep2_174_a5 with dissolve
            faye "..................."
            faye "How long have you been here?"
            mc "Not too long, actually. I arrived here when you were about to hang up."
            faye "..................."
            scene ch2ep2_174_a6 with dissolve
            mc "My bad... Are you alright?"
            faye "Yeah... I'm good."
            mc "Good. Alright, I'll give you some time to yourself. I assume you need that."
            if ch2ep1photosession == 1:
                faye "Actually...."
                faye "Do you mind staying with me for a sec?"
                menu:
                    "If that's what you want\n[faye2]":
                        $ ch2ep2staywithfaye = 1
                        $ faye_relationship += 2
                        $ faye_ch2_ep2 += 2
                        mc "Sure, if that's what you want."
                        faye "Come up here, please...."
                        scene black with dissolve
                        $ renpy.pause()
                        scene ch2ep2_174_a7 with dissolve
                        faye "....................."
                        mc "....................."
                        u "This is kind of awkward...."
                        u "We've been here a couple minutes, yet she hasn't spoken a single word."
                        scene ch2ep2_174_a9 with dissolve
                        faye "... Why haven't you asked me about that?"
                        mc "Hm? About what?"
                        faye "About whom I was talking to, and why I was talking to her."
                        mc "Well, I thought it was better to wait until you wanted to tell me about that yourself."
                        faye "*Sighs*.........."
                        scene ch2ep2_174_a8 with dissolve
                        faye "That was my mom."
                        mc "I see.... Did you fight with her? You sounded very angry."
                        faye "... No, we didn't. But yeah, I was very angry at her."
                        faye "Actually, I still am..."
                        mc "... Why?"
                        faye "..................."
                        scene ch2ep2_174_a10 with dissolve
                        faye "... She asked me to lend her some money."
                        faye "But, before you judge me, it wasn't the first time."
                        faye "She's been borrowing money from me for a very, very long time."
                        faye "And do you have any idea what she's done with all money I lend her?"
                        mc "... No, I don't."
                        faye "*Sighs* She loses it on gambling..."
                        faye "And every time she loses all her money, she calls me to borrow more."
                        scene ch2ep2_174_a11 with dissolve
                        mc "... How long has she been addicted to gambling?"
                        faye "Almost 20 years now...."
                        faye "I've tried to tell her to stop so many times, but she didn't listen to me."
                        faye "So, we haven't gotten along well since then."
                        faye "*Sighs* I really don't know what I should do with her, [mc]."
                        faye "I've tried so hard to not give her any more money, but I still fail every time."
                        faye "You know... even though we don't get along well, she is still my mother after all...."
                        scene ch2ep2_174_a12 with dissolve
                        mc "I'm sorry, [faye]."
                        faye "Hm? What for?"
                        mc "I don't know what I do can help you..."
                        faye "*Smiles* It's okay. I don't need you to help me with anything."
                        faye "You've already helped a lot by staying here with me."
                        faye "You know... sometimes I need to unburden myself to someone."
                        mc "... Does anybody else know about this?"
                        faye "No, I've never told anyone about my situation. You're the first person who knows."
                        mc "I see..."
                        faye "Alright, thanks for listening to me. I feel much better now."
                        faye "We've been wasting time here for too long already. Let's get back to work!"
                        scene black with dissolve
                        $ renpy.pause()
                        scene ch2ep2_174_a13 with dissolve
                        u "...................."
                        u "I know I've been away from my desk for quite some time..."
                        u "But, I'm still thirsty. Let's grab a drink before going back to my department."
                        jump ch2ep2lunch
                    "I have to get back to work":
                        $ ch2ep2staywithfaye = 2
                        mc "I'm sorry. I've been out here for too long."
                        mc "I have to get back to work."
                        faye "... Fine. Good luck then."
                        jump ch2ep2lunch
            else:
                faye "Thank you. See you later, [mc]."
                jump ch2ep2lunch
        "Just go for a drink":
            $ ch2ep2fayeonphone = 2
            scene ch2ep2_174_d1 with dissolve
            u "... Just forget it."
            u "This is none of my business."
            u "Even if something bad happens, there is a security team to take care of it."
            u "Let's just keep going to buy a drink."
            jump ch2ep2lunch
label ch2ep2lunch:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    s "You went back to the department and worked until lunch break...."
    play music "sfx/ch2ep2_1.mp3" fadein 3.0
    $ bgm = "Roa Music - After the rain"
    scene ch2ep2_175 with fade
    u "... Alright, it's lunchtime."
    u "Let's go find something to eat."
    if ch2ep1lunchateirahouse == 1:
        scene ch2ep2_176 with dissolve
        u "... Hm?"
        scene ch2ep2_177 with dissolve
        mc "Hi, [eira]."
        eira "O-Oh..?!"
        eira "Hello, [mc]. How are you doing?"
        mc "I'm doing pretty good, and you?"
        eira "Me, too."
        scene ch2ep2_178 with dissolve
        mc "By the way, where is [sally]?"
        mc "I always see you guys together recently. Why are you alone today?"
        eira "She didn't come to work today. She told me in the morning that she wasn't feeling well."
        mc "Did she catch a cold?"
        eira "No, it's not that..."
        mc "Hm? Then, what happened to her?"
        scene ch2ep2_179 with dissolve
        eira "{size=-15}It's... err... you know... the thing that... women have to... deal with every month.{/size}"
        mc "What did you say? I couldn't hear you."
        eira "... I'm sorry, but it's too embarrassing to say it out loud."
        mc "..................."
        mc "Oh... I get it now."
        eira "... Good for you."
        scene ch2ep2_180 with dissolve
        u "Well, that means she has to have lunch alone today."
        u "Should I invite her to go together?"
        u "I mean... it's not such a bad idea."
        menu:
            "Do you want to get lunch together?\n[eira1]":
                $ ch2ep2inviteeira = 1
                $ eira_ch2_ep2 += 1
                $ eira_relationship += 1
                scene ch2ep2_180_a1 with dissolve
                mc "Do you want to come have lunch with me, [eira]?"
                eira "... H-Hm? What did you just say?"
                mc "I asked you if you wanted to have lunch together."
                eira "Yes! Sure!"
                u "(I think I made the right choice. She looks very happy that I asked.)"
                mc "Alright, let's go, then."
                scene black with dissolve
                s "*A few minutes later*.........."
                scene ch2ep2_180_a2 with fade
                mc "Okay. Here we are..."
                mc "... Hm?"
                eira "... What's wrong?"
                scene ch2ep2_180_a3 with dissolve
                mc "I think we got here a little bit too late."
                mc "The seats inside are already full."
                eira "Oh yeah, you're right."
                mc "Let's go find somewhere else then."
                scene ch2ep2_180_a4 with dissolve
                eira "Hm? Why do we have to leave?"
                mc "Hm? Why not? All the seats inside are full."
                eira "I know that, but there are still seats outside available, aren't there?"
                mc "Yes, there are..."
                mc "But, are you sure that you want to sit outside?"
                scene ch2ep2_180_a5 with dissolve
                eira "Yeah! Why not?"
                mc ".... Nothing. I was just assuming that you wouldn't want to sit outside."
                eira "*Smiles* I'm not picky, [mc]."
                eira "I'm not afraid of sunlight. Plus, the weather today is quite nice."
                eira "Let's just go take a seat."
                mc "Alright, if you say so."
                scene black with dissolve
                $ renpy.pause()
                s "*About fifteen minutes later*........"
                scene ch2ep2_180_a6 with dissolve
                eira "*Smiles* Wow... The food looks so delicious."
                mc "I agree."
                eira "What are you waiting for, then? Let's eat."
                mc "After you, [eira]."
                stop music fadeout 3.0
                scene ch2ep2_180_a7 with dissolve
                play music "sfx/ep2_6.mp3" fadein 3.0
                $ bgm = "Onycs - Eden"
                g1 "... Hm?"
                man1 "What's wrong, honey?"
                g1 "Isn't that...?"
                scene ch2ep2_180_a8 with dissolve
                g1 "Yeah! It's really you, [eira]!"
                eira "... R-Roxy?!"
                roxy "Wow! What a coincidence! I've never expected to see you here!"
                roxy "How long has it been since the last time? 7 years, right?!"
                scene ch2ep2_180_a9 with dissolve
                eira "... Y...Yeah."
                roxy "I almost didn't recognize you."
                roxy "You look a lot different than you did in high school!"
                roxy "Do you mind me sitting here for a sec?"
                eira "Err..."
                scene ch2ep2_180_a10 with dissolve
                roxy "Thank you!"
                roxy "By the way, who is this man? Is he your boyfriend?"
                roxy "Aren't you going to introduce him to me?"
                eira "... N.. No, he... isn't...."
                roxy "Hmmm... What a pity."
                u "......................"
                u "[eira] became much more talkative recently, which is really good for her, but now she is back to her old self again."
                u "I don't know this woman, but she is really making [eira] uncomfortable."
                scene ch2ep2_180_a11 with dissolve
                roxy "Look. I'm on vacation and I'll be staying in this city for a couple days."
                roxy "You changed your phone number, right? Give me your new one."
                scene ch2ep2_180_a12 with dissolve
                eira "... E... Eh? Why do you... want it?"
                roxy "This is my first time here. I know nothing about the tourist attractions."
                roxy "So, I need you to be my tour guide! It's better to have someone who knows places around here."
                eira "... But, I don't... have time... for that. I've got... to work."
                scene ch2ep2_180_a13 with dissolve
                roxy "What?! How could you say that?!"
                man1 "Calm down, honey. Your friend can't just skip work for us. It wouldn't be that easy."
                roxy "Shut up, [mx]."
                mx "...................."
                roxy "What's wrong with you, [eira]? Why did you have to turn me down? Can't you just do me a favor?"
                roxy "We haven't seen each other for like 7 years!"
                eira "....................."
                roxy "*Smirks* You haven't changed a bit. You're still as annoying as you were."
                menu:
                    "Stand up for [eira] [eira2]":
                        jump ch2ep2_standupforeira
                    "Do nothing":
                        s "Are you sure that you want to do nothing?"
                        s "This will end any possibility of having a romantic relationship with [eira]."
                        menu:
                            "Yes, I am":
                                $ ch2ep2standupforeira = 2
                                scene ch2ep2_180_a13_d1 with dissolve
                                eira "I... I... I'm sorry."
                                roxy "Tch...! Why did I even notice you in the first place."
                                roxy "I was very happy, but you made me so pissed."
                                mx "Let's just leave them alone, [roxy]."
                                scene ch2ep2_180_a13_d2 with dissolve
                                roxy "I don't need you to tell me that."
                                roxy "I don't want to stay here for any longer either."
                                roxy "My mood is ruined now because of this annoying bitch!"
                                mx "I know.... So, let's just hurry up and leave so that you don't have to see her anymore."
                                roxy "Tsk...! Fine!"
                                jump ch2ep2_eiralunchdone
                            "I've changed my mind":
                                jump ch2ep2_standupforeira
            "Say goodbye":
                $ ch2ep2inviteeira = 2
                scene ch2ep2_180_d1 with dissolve
                mc "Alright... I think I should leave now."
                mc "See you around, [eira]. Enjoy your lunchtime."
                eira "... Okay. You, too."
                scene black with dissolve
                $ renpy.pause()
                s "You had lunch and returned to work until evening...."
                jump ch2ep2newbed
    else:
        scene black with dissolve
        $ renpy.pause()
        s "You had lunch and returned to work until evening...."
        jump ch2ep2newbed
label ch2ep2_standupforeira:
    $ ch2ep2standupforeira = 1
    $ eira_relationship += 2
    $ eira_ch2_ep2 += 2
    stop music fadeout 3.0
    scene ch2ep2_180_a13_a1 with dissolve
    play music "sfx/ep4_5.mp3" fadein 3.0
    $ bgm = "RYYZN - Waited (instrumental)"
    mc "What are you doing?"
    roxy "Hm? What are you talking about? I don't understand."
    mc "Don't you realise that she's uncomfortable with you being here?"
    mc "And who gave you the permission to sit with us in the first place?"
    mc "Didn't your parents teach you any manners?"
    scene ch2ep2_180_a13_a2 with dissolve
    roxy "W-What?! How dare you talk about my parents?!"
    roxy "I was just talking to my friend. Who the hell are you to intervene?!"
    mc "Friend? No one talks to their friend the way you did. Apologize to her now."
    roxy "Who do you think you are to command me like that?!"
    mx "Leave them alone, [roxy]."
    roxy "What?! Seriously, [mx]?!"
    roxy "This asshole is insulting your girl in front of you and you wanted me to just leave!!??"
    mx "*Sighs*........."
    scene ch2ep2_180_a13_a3 with dissolve
    roxy "W-What are you doing?! Let me go! I'm going to slap that asshole in his fucking face!!"
    mx "Enough, [roxy]. I won't repeat myself."
    roxy "Let me g-"
    mx "I said..."
    mx "{b}ENOUGH!!!{/b}"
    roxy ".................."
    mx "Are you a fucking high school kid? You can't just go around causing problems like that!! I'm so fucking tired of this!!"
    roxy "................."
    mx "Sorry, guys. Don't mind us. We're leaving."
    jump ch2ep2_eiralunchdone
label ch2ep2_eiralunchdone:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep2_7.mp3" fadein 3.0
    $ bgm = "AERØHEAD - The Reckoning"
    scene ch2ep2_180_a14 with dissolve
    eira "*Hics*................"
    mc "..................."
    mc ".... Are you alright?"
    eira "*Hics*... Y... Yeah...."
    scene black with dissolve
    $ renpy.pause()
    s "[eira] kept crying for about five minutes more...."
    scene ch2ep2_180_a15 with dissolve
    eira "I'm sorry you had to see my cry, [mc]."
    eira "I just couldn't control myself..."
    mc "It's alright. You have nothing to be sorry for."
    mc "Was she one of the high school friends you told us about the other day?"
    eira "....................."
    scene ch2ep2_180_a16 with dissolve
    eira "... Yeah. Seeing her again reminded me of those days."
    eira "The days that I try to forget...."
    mc "She did more to you than you told me and [sally], right?"
    eira "... Yeah, you're right."
    eira "She bullied me until the last day of high school after I told them that I heard them talking behind my back."
    scene ch2ep2_180_a17 with dissolve
    mc "I don't know how hard it was for you, but you did a good job enduring all that pain, [eira]."
    mc "She probably thought that she was better than you back then."
    mc "However, I'm sure that your life is much better than hers right now."
    eira "... Thank you."
    scene ch2ep2_180_a18 with dissolve
    eira ".... Alright, let's just stop talking about her."
    eira "Our food is getting cold. We should eat it while it's still hot."
    mc "Yeah, sure."
    if ch2ep2standupforeira == 1:
        scene ch2ep2_180_a18_a1 with dissolve
        eira "By the way, [mc]..."
        mc "... Hm?"
        eira "Thank you for standing up for me there."
        mc "You don't have to thank me. It's not a big deal."
        eira "Still, I really appreciate that."
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    s "*Half an hour later*.........."
    play music "sfx/ch1ep2.mp3" fadein 3.0
    $ bgm = "Bensound - Little Idea"
    scene ch2ep2_180_a19 with dissolve
    mc "... Alright, let's head back to work."
    eira "Sure...."
    scene ch2ep2_180_a20 with dissolve
    eira "Wait. Hold on, [mc]."
    mc "Hm? What's wrong?"
    eira "Actually, can we stop by a pharmacy for a sec?"
    eira "I'm going to buy [sally] some medicine."
    mc "Yeah, sure."
    eira "*Smiles* Thank you."
    scene black with dissolve
    $ renpy.pause()
    s "After she bought medicine for [sally], you went back to the company and worked until evening...."
    jump ch2ep2newbed
label ch2ep2newbed:
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_181 with fade
    u "... Okay, I'm back home."
    if ch2ep2shoppingmallwithkrystal == 1:
        u "It's about time for my new bed to arrive."
        u "I should get ready."
    else:
        u "I went to buy a new bed yesterday."
        u "They said it would arrive here this evening."
        u "So, it's about time. I should get ready."
    scene ch2ep2_182 with dissolve
    s "*Phone vibrates*......."
    u "... Hm?"
    scene ch2ep2_183 with dissolve
    mc "Hello..."
    mc "Oh, you're already in front of the house?"
    mc "Okay. Wait a sec. I'm going to open the door for you real quick."
    scene ch2ep2_184 with dissolve
    u "Well, speak of the devil...."
    u "Let's hurry up and get everything."
    u "I have something more important that needs to be done as well."
    scene black with dissolve
    $ renpy.pause()
    s "*About an hour later*............."
    scene ch2ep2_185 with dissolve
    u "Alright, here we go. Finally, I can say goodbye to my old bed."
    u "I bought this one because it felt really comfortable to lie on."
    u "I tried it yesterday at the shopping mall."
    scene ch2ep2_186 with dissolve
    u "Well, let's just stop talking to myself."
    u "I need to take the suit to [lucas]."
    u "It's almost time for the appointment."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_187 with dissolve
    u "..................."
    unknown "Oh?! Yo, [mc]!"
    u "... Hm?"
    scene ch2ep2_188 with dissolve
    zeke "Is everything done?"
    zeke "I heard you bought a new bed."
    mc "Oh yeah, you're right."
    scene ch2ep2_189 with dissolve
    mika "Hm? I didn't know you guys were allowed to renovate your room."
    mika "I thought it was prohibited in a shared house."
    zeke "Well, I don't know about the other places, but you can do anything you want to your room here."
    zeke "Our landlord doesn't mind it as long as you don't damage the room too much."
    mika "I see... You guys have got such a good landlord. He's so kind."
    zeke "I know, right?! That's why I love this place so much!"
    scene ch2ep2_190 with dissolve
    zeke "By the way... Where are you going, bro?"
    zeke "Why have you got a backpack?"
    zeke "What is in there?"
    mc "It's nothing important. Just some of my personal belongings."
    scene ch2ep2_191 with dissolve
    mc "And yeah, I'm going to the central city. I have something to do there."
    zeke "Oh? Do you want me to drive you there, then?"
    mc "Thanks, but I'm good. Don't worry about me."
    zeke "Are you sure?"
    mc "Yeah. You just got back from work. So, you should spend some time with [mika], here."
    zeke "*Laughs* Hahaha! You're right! See you tomorrow then!"
    mc "Sure."
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    s "*About half an hour later*........."
    play music "sfx/ch2ep2_5.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - I Saw A Ghost Last Night"
    scene ch2ep2_192 with dissolve
    u "... Alright, I'm at the meeting place."
    u "I wonder where he is right now. Let's call him."
    unknown ".... [mc]!!"
    u "... Hm?"
    scene ch2ep2_193 with dissolve
    u "Oh... There he is."
    scene ch2ep2_194 with dissolve
    mc "Well... To be honest I'm impressed that you are on time."
    mc "It's very unusual for you."
    lucas "... Is that something you should say to someone after asking him for a favor?"
    mc "... Why not? I was just stating a fact."
    lucas "Fuck you, [mc]."
    lucas "Well, I was already in the city. That's why I managed to get here on time."
    lucas "Let's just stop wasting time. Where is that thing?"
    mc "It's in my backpack."
    lucas "Then, what are you waiting for. Give it to me already."
    lucas "I don't have much time to waste here. I have something important later."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_195 with dissolve
    mc "It will take you about a week to send me back the handprint, right?"
    lucas "Yeah, I have to do it back in my lab."
    lucas "But, I have to finish my mission before I go back there."
    mc "No problem."
    lucas "Great. I will call you when it's done."
    scene black with dissolve
    $ renpy.pause()
    stop music fadeout 3.0
    scene ch2ep2_196 with dissolve
    u "... Alright, what had to be done was done."
    u "Now, I just need to wait until he calls me back."
    if ch2ep2inviteeira == 1:
        scene ch2ep2_197 with dissolve
        u "Well, I finished my business a lot earlier than I expected."
        u "There is still a lot of time left before it gets dark."
        u "What should I do next?"
        u "...................."
        menu:
            "[smgr]Go visit [sally]":
                $ ch2ep2visitsally = 1
                scene ch2ep2_197_a1 with dissolve
                u "I don't know why, but thoughts of [sally] suddenly came up in my head."
                u "I mean... [rin] was on her period as well, but she was able to go to work."
                u "It must have been really bad for [sally], otherwise, she would've been able to go to work."
                u "Let's pay her a visit and check if she's any better."
                jump ch2ep2_visitsally
            "Go back home":
                $ ch2ep2visitsally = 2
                scene ch2ep2_197_d1 with dissolve
                u "... Well, I don't think there is anything interesting for me to do here."
                u "Let's just go home, and get some rest."
                jump ch2ep2_gobackhome
label ch2ep2_visitsally:
    play music "sfx/ch2ep2_1.mp3" fadein 3.0
    $ bgm = "Roa Music - After the rain"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_197_a2 with fade
    u "... Finally, here I am."
    u "...................."
    u "... Well, now that I'm here, I'm starting to wonder why I decided to come in the first place."
    u "I mean... it's completely none of my business."
    u "But, whatever... Since I'm already here, let's just ring the doorbell..."
    scene black with dissolve
    $ renpy.pause()
    s "*A minute later*............."
    scene ch2ep2_197_a3 with dissolve
    eira "I'm coming...."
    eira "(... Hm? Isn't that [mc]?)"
    eira "(What made him visit me here?)"
    eira "(Well, there is only one way to find out.)"
    scene ch2ep2_197_a4 with dissolve
    eira "Good evening, [mc]."
    mc "Hi...."
    eira "... What are you doing here?"
    mc "I'm here because I wanted to see how [sally] is. Is she okay now?"
    scene ch2ep2_197_a5 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_197_a5.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_197_a5_blink.jpg", 1) with dissolve
    eira "... Hm? Did you come all the way here because of that?"
    mc "Yeah, why?"
    eira "Nothing. I mean... you could've just called either her or me."
    mc "....................."
    mc "Oh yeah, you're right. I completely forgot I could've done that."
    eira "*Smiles* I never knew you could be silly sometimes."
    eira "Don't worry about her. She's feeling better."
    mc "Good... Alright then, I'll leave now."
    eira "... Wait. Are you going to just leave like that?"
    eira "Since you're already here, why don't you come in for a bit?"
    eira "You can check her for yourself."
    menu:
        "That's a pretty good idea [sally2]":
            $ ch2ep2visitsally1 = 1
            scene ch2ep2_197_a6 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_197_a6.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_197_a6_blink.jpg", 1) with dissolve
            mc "Well, you're right. That's a pretty good idea."
            eira "Alright then, what are you waiting for? Come on in."
            mc "... I can't."
            eira "Hm? Why not?"
            mc "You have to open the gate for me first..."
            eira "... M-My bad!"
            mc "It's alright...."
            scene black with dissolve
            $ renpy.pause()
            scene ch2ep2_197_a8 with dissolve
            eira "Come on in."
            mc "Thank you..."
            scene ch2ep2_197_a9 with dissolve
            mc "Hm...?"
            mc "I don't see her. Where is she?"
            scene ch2ep2_197_a10 with dissolve
            eira "She is in her room right now."
            eira "Do you want to go see her?"
            mc "... I think I should just let her sleep."
            eira "It's alright. She just went into her room not long ago."
            eira "I'm sure that she is still awake. I think she will be happy to see that you're worrying about her."
            mc "Okay then, I'll take your word for it."
            scene black with dissolve
            $ renpy.pause()
            scene ch2ep2_197_a11 with fade
            sally "Uhm...."
            sally "(I... really hate... this feeling every month...)"
            sally "(Even though I'm getting a little bit better now, it still hurts a lot...)"
            scene ch2ep2_197_a12 with dissolve
            s "*Door knocks*........"
            sally "... Yes, [eira]?"
            mc "... Actually, it's me."
            sally "Hm...? [mc]?"
            mc "Yeah, can I come in?"
            sally "... Yeah, sure."
            scene ch2ep2_197_a13 with dissolve
            sally "... Hello, [mc]."
            sally "... I'm sorry... I can't stand up... and greet you properly."
            mc "It's alright. You don't have to apologize for that at all."
            sally "... Thank you... for understanding me."
            scene ch2ep2_197_a14 with dissolve
            mc "Are you alright?"
            mc "[eira] said that you were getting better, but to be honest you look worse than I expected..."
            sally "*Smiles* I'm good.... Don't worry... about me."
            sally "It's not something new. Women deal with... this problem... every month."
            sally "It's just... a little bit... harder to deal with... in my case, but... I'm getting used to it."
            mc "I see...."
            scene ch2ep2_197_a15 with dissolve
            sally "Hey. I'm really fine. It was a lot... worse in the morning."
            sally "[eira] has been... taking care of me... so well."
            sally "Thank you for... the medicine and... this hot water bottle, [eira]."
            eira "You don't have to thank me at all, [sally]."
            eira "I'm sure that you are going to do the same for me when it's my turn."
            eira "That's what friends are for, right?"
            sally "*Smiles* Y... Yeah, absolutely."
            scene ch2ep2_197_a16 with dissolve
            u "Well... Even though [sally] seems to struggle a lot with her period, she doesn't seem to be moody at all, unlike [rin]."
            u "I don't know why, but I guess women's menstruation affects them in different ways."
            scene ch2ep2_197_a17 with dissolve
            sally "... What's wrong, [mc]? Why did you... suddenly get quiet?"
            mc "Nothing. I was just thinking about things."
            mc "Alright, I won't take any more of your time. You should get some rest."
            sally "... Okay. Goodbye then, [mc]."
            mc "All good. Get well soon, [sally]."
            sally "... Thanks."
            scene black with dissolve
            $ renpy.pause()
            $ sally_relationship += 2
            $ sally_ch2_ep2 += 2
            scene ch2ep2_197_a18 with fade
            mc "... Alright, I think it's time for me to go."
            eira "Hm? Are you really going to leave now?"
            mc "... Yeah, why?"
            eira "Have you had your dinner yet?"
            mc "No. Not yet."
            scene ch2ep2_197_a19 with dissolve
            eira "Then, why don't you stay for dinner?"
            eira "I'm about to have mine. I can cook some for you, too."
            mc "Are you sure about that? I mean... you don't have to."
            eira "Why not? It's not a big deal."
            mc "Alright then, if you insist.."
            scene black with dissolve
            $ renpy.pause()
            scene ch2ep2_197_a20 with dissolve
            mc "Thank you for dinner, [eira]."
            mc "I owe you one."
            eira "Don't say that. You don't owe me anything. It's just a dinner."
            stop music fadeout 5.0
            eira "In fact, I'm the one owing you since you've been helping me a lot recently."
            play music "sfx/ch2ep2_7.mp3" fadein 3.0
            $ bgm = "Neutrin05 - Rain and Tears"
            s "*Rain sounds*.........."
            scene ch2ep2_197_a21 with dissolve
            eira "Aw... Don't tell me..."
            eira "Is it raining out there?"
            mc "Yeah, apparently it is."
            eira "It's not good for you. How are you going to go home then?"
            mc "Have you got an umbrella I can borrow?"
            eira "I have, but look... it's raining harder now. The wind is getting stronger, too."
            scene ch2ep2_197_a22 with dissolve
            eira "It won't be easy for you to get to the bus stop."
            mc "... Yeah, you're right."
            eira "When is the last bus tonight?"
            mc "A quarter to eleven, I think."
            eira "Umm... You still have 2 hours until then."
            eira "Then, why don't you wait here until the rain stops or gets lighter, at least?"
            mc "... Well, I think I have no other choice."
            eira "Alright, I'll keep you company until you leave then."
            eira "But, let me wash these dishes first."
            mc "Yeah, sure."
            scene black with dissolve
            $ renpy.pause()
            s "*A few minutes later*..........."
            scene ch2ep2_197_a23 with dissolve
            u "...................."
            eira "... [mc]."
            u "... Hm?"
            scene ch2ep2_197_a24 with dissolve
            mc "....What's wrong, [eira]?"
            mc "You look troubled."
            eira "... Well, it's because the rain keeps raining harder."
            eira "I don't like it...."
            mc "... Hm? Wh-"
            if ch2ep2standupforeira == 1:
                $ renpy.sound.play("sfx/lightning.mp3")
                scene ch2ep2_197_a25_a1 with flash
                s "*Lightning sounds*........"
                eira "*Screams* Eyahh...!"
                stop sound
                mc "...!!!"
                scene ch2ep2_197_a25_a2 with flash
                $ renpy.sound.play("sfx/lightning.mp3")
                s "*Lightning sounds*........"
                eira "*Screams* E-Eeek...!!"
                stop sound
                mc "C...Calm down, [eira]."
                mc "It's just lightning."
                eira "*Screams* P-Please, don't leave me alone, [mc]!"
                scene ch2ep2_197_a25_a3 with dissolve
                mc "Don't worry. I won't."
                mc "I'm here, [eira]. I'm here with you.  You will be fine."
                mc "I won't leave you alone."
                eira "*Hics*.... Are you sure...?"
                mc "Yeah. I'll stay with you until the rain stops."
                eira "*Hics*.... T... Thank you...."
                scene black with dissolve
                $ renpy.pause()
                s "*About half an hour later*..........."
                scene ch2ep2_197_a25_a4 with dissolve
                mc "[eira]..."
                eira "... Yes?"
                mc "I think you're okay now. The rain has lightened up."
                eira ".... Has it?"
                mc "Yeah. Just listen for yourself."
                eira "......................"
                eira "You're right... It has gotten lighter now, and there is no more thunder and lightning."
                mc "I told you... So, can I release you now? I'm starting to get numb..."
                eira "Okay..."
                eira "................"
                eira "Wait...."
                scene ch2ep2_197_a25_a5 with dissolve
                eira "Oh my...!!!"
                mc "What's wrong, [eira]?"
                eira "N-Nothing...!"
                eira "(Oh my god...! I can't believe that I actually stayed like this with him for half an hour!)"
                eira "(Aww... This is so embarrassing...)"
                mc "[eira]...."
                scene ch2ep2_197_a25_a6 with dissolve
                eira "N-No, I wasn't thinking about anything weird!"
                mc "Hm? What do you mean? I didn't even say anything yet."
                eira "E-Er... Nothing. Don't mind me...."
                eira "Okay... You can let go of my legs now, [mc]."
                mc "Yeah, sure."
                scene ch2ep2_197_a25_a7 with dissolve
                eira "...................."
                mc "... What's wrong? Why are you looking at the ground?"
                eira "I feel too embarrassed to look you in the eye...."
                eira "... Thank you for taking care of me earlier."
                mc "No worries. It's not a big deal."
                mc "By the way, why are you so scared of lighting?"
                mc "Did something bad happen to you on a rainy day back then?"
                eira "......................"
                eira "... Yeah, I got like this after [roxy] and her friends locked me in the toilet after school."
                eira "... It was getting dark and was raining heavily."
                eira "I was stuck in there for almost two hours."
                eira "Fortunately, the janitor heard me crying. He followed my voice and opened the door for me."
                mc "... I'm so sorry to hear that."
                eira "You don't have to...."
                mc "...................."
                mc "By the way, you are pretty strong. Do you realize that?"
                scene ch2ep2_197_a25_a8 with dissolve
                eira "Hm? Strong? Me?"
                mc "Yeah..."
                eira "What made you think that? Because I managed to endure bullying?"
                mc "That's right, but I meant that you're physically strong."
                mc "I never expected you to be able to jump that high. You impressed me a lot."
                eira ".... Are you making fun of me?"
                mc "No, I'm not. I was really impressed."
                eira "Stop it already... I know that I shouldn't have jumped on you like that."
                mc "That's not what I meant..."
                eira "Even though I'm scared of lightning, I don't usually freak out like that."
                eira "It's just... I wasn't ready when the lightning suddenly struck."
                eira "But I'm prepared now. There won't be a second t-"
                scene ch2ep2_197_a25_a2 with flash
                $ renpy.sound.play("sfx/lightning.mp3")
                s "*Lightning sounds*.........."
                eira "*Screams* T-Time...!!"
                stop sound
                scene ch2ep2_197_a25_a9 with dissolve
                mc "......................"
                eira "...................."
                mc "... There won't be a second what?"
                eira "S-Shut up...."
                scene black with dissolve
                $ renpy.pause()
                s "*An hour and a half later*......."
                scene ch2ep2_197_a26 with dissolve
                mc "Alright, I'm going now."
                mc "See you tomorrow, [eira]."
                eira "Okay. See you tomorrow, [mc]."
                eira "Get home safely."
                jump ch2ep2_gobackhome
            else:
                scene ch2ep2_197_a25_d1 with flash
                $ renpy.sound.play("sfx/lightning.mp3")
                s "*Lightning sounds*........"
                eira "*Screams* Eyahh...!"
                stop sound
                mc "...!!!"
                scene ch2ep2_197_a25_d2 with dissolve
                $ renpy.sound.play("sfx/lightning.mp3")
                s "*Lightning sounds*........"
                eira "*Screams* E-Eeek...!!"
                stop sound
                mc "C...Calm down, [eira]."
                mc "It's just lightning."
                eira "*Sobs* N-No... You don't understand..."
                scene ch2ep2_197_a25_d3 with dissolve
                eira "*Sobs* I-I'm sorry, [mc]...."
                eira "*Sobs* I wanted... to stay here... with you, but I think... I can't now..."
                eira "*Sobs* Can I... go back to... my room?"
                mc "Oh... Okay. Don't worry about me."
                mc "I'll stay until the rain stops, then I'll leave."
                eira "*Sobs* Please, don't forget... to lock the door when you go, too. Thank you..."
                scene black with dissolve
                $ renpy.pause()
                scene ch2ep2_197_a25_d4 with dissolve
                u "Thinking about [eira], she seemed so freaked out."
                u "I guess she might have had a bad experience on a rainy day in the past."
                u "*Sighs*... It's raining pretty hard right now."
                u "Well, I hope it stops before the last bus."
                scene black with dissolve
                $ renpy.pause()
                s "You waited until the rain stopped, then left the house and went home...."
                jump ch2ep2_gobackhome
        "It's getting dark":
            $ ch2ep2visitsally1 = 2
            scene ch2ep2_197_a7 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_197_a7.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_197_a7_blink.jpg", 1) with dissolve
            mc "Thanks, but knowing that she is okay is already enough."
            mc "And, it's getting dark now. I should really just go back home."
            eira "... Alright, if you say so."
            eira "Goodbye then. See you tomorrow, [mc]."
            mc "Yeah, see you."
            jump ch2ep2_gobackhome
label ch2ep2_gobackhome:
    stop music fadeout 3.0
    if ch2ep2visitsally1 == 1:
        scene ch2ep2_198 with fade
        u "*Sighs*... It's been a really long day. I'm so tired."
        u "I also feel very sweaty and sticky now."
        u "Let's go take a shower first, and then go to bed."
    else:
        scene black with dissolve
        $ renpy.pause()
        s "*Later that night*........."
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    scene ch2ep2_199 with dissolve
    u "Okay, it's already pretty late."
    u "Let's get in bed...."
    if ch2ep2standupforeira == 1 and ch2ep2visitsally1 == 1:
        scene ch2ep2_199_a1 with dissolve
        s "*Ringtone sounds*........."
        u "Hm...? Who's calling me at a time like this?"
        u "Well, there is only one way to find out. Let's check..."
        scene ch2ep2_199_a2 with dissolve
        u "Oh... It's [eira]."
        u "I wonder why she is calling me now."
        u "Let's see..."
        scene ch2ep2_199_a3 with dissolve
        mc "................."
        mc "... Hello, [eira]."
        scene ch2ep2_199_a4 with dissolve
        eira "... Hi, [mc]."
        eira "Hm? Why am I calling you this late at night?"
        eira "Well, I've just finished my work and it's been a while since you left here."
        eira "So, I wanted to call you to ask if you made it home yet."
        scene ch2ep2_199_a5 with dissolve
        eira "That's great..."
        eira "Oh... I didn't wake you up, right?"
        eira "Hm? [sally]? Don't worry about her. I think she feels a lot better now."
        eira "She's even walking around the house now. I saw her in the kitchen finding something to eat like half an hour ago."
        scene ch2ep2_199_a6 with dissolve
        eira "Alright, I won't take any more of your time."
        eira "Oh... And thank you... so much again for... today."
        eira "... S... Sleep well, [mc]."
        eira "... Yeah, bye..."
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep2_199_a2 with dissolve
        u "... Alright, I think that's it for today."
        u "It's almost midnight already. I should really go to sleep now."
        scene ch2ep2_200 with dissolve
        u "Arr...."
        u "Perfect... This bed is way more comfortable than the previous one."
        u "I made the right choice to buy it."
        jump ch2ep2_eiramasturbate
    else:
        scene black with dissolve
        $ renpy.pause()
        jump ch2ep2_latenight
label ch2ep2_eiramasturbate:
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
    stop music fadeout 5.0
    $ renpy.pause()
    play music "sfx/ep2_4.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - Out of Time"
    scene ch2ep2_199_a7 with fade
    eira "(*Sighs* What a day...)"
    eira "(So many things happened today....)"
    eira "([mc]... He's been so kind to me recently.)"
    eira "(Not only did he help me with my work, but also he stood up for me against [roxy], too.)"
    eira "(He even let me....)"
    scene ch2ep2_197_a25_a2 with flash
    $ renpy.pause(0.1, hard=True)
    scene ch2ep2_199_a8 with vpunch
    eira "(...!!!)"
    eira "(Aw... I can't get those memories out of my head...)"
    eira "(That was so embarrassing... How could I have done that?)"
    eira "(Oh my god... I can feel my heart beating so hard. I can't stop it.)"
    eira "(...................)"
    scene ch2ep2_199_a9 with dissolve
    eira "(*Softly breathes* It's feeling so weird down there.....)"
    eira "(*Softly breathes* Well, I can't say that actually. I know another word which is more suitable in this situation...)"
    eira "(*Softly breathes* I'm already 25 years old. I'm not that innocent after all...)"
    eira "(*Softly breathes* It's been a while since... I did it last time...)"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_199_a10 with dissolve
    show ch2ep2_eira1 with dissolve
    window hide
    eira "*Softly breathes*.... Arr......"
    eira "*Softly breathes*.... Mmmm... So good...."
    $ renpy.pause()
    menu:
        "Next":
            scene black with dissolve
            hide ch2ep2_eira1
    $ renpy.pause()
    scene ch2ep2_199_a11 with dissolve
    show ch2ep2_eira2 with dissolve
    window hide
    eira "*Softly breathes*.... Ahh...."
    eira "*Moans*... Mmmm... [mc]...."
    $ renpy.pause()
    menu:
        "Next":
            scene black with dissolve
            hide ch2ep2_eira2
    $ renpy.pause()
    scene ch2ep2_199_a12 with dissolve
    show ch2ep2_eira3 with dissolve
    window hide
    eira "(*Heavily breathes*.... Mmmm....!!)"
    eira "(*Heavily breathes*.... A-Ah...! Almost there...!)"
    $ renpy.pause()
    menu:
        "Slowest":
            hide ch2ep2_eira3
            jump ch2ep2masturbate1
        "Slower":
            hide ch2ep2_eira3
            jump ch2ep2masturbate2
        "Cum":
            jump ch2ep2masturbatecum
label ch2ep2masturbate1:
    scene ch2ep2_199_a10 with dissolve
    show ch2ep2_eira1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ch2ep2_eira1
            jump ch2ep2masturbate2
        "Fastest":
            hide ch2ep2_eira1
            jump ch2ep2masturbate3
label ch2ep2masturbate2:
    scene ch2ep2_199_a11 with dissolve
    show ch2ep2_eira2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ch2ep2_eira2
            jump ch2ep2masturbate1
        "Faster":
            hide ch2ep2_eira2
            jump ch2ep2masturbate3
label ch2ep2masturbate3:
    scene ch2ep2_199_a12 with dissolve
    show ch2ep2_eira3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slowest":
            hide ch2ep2_eira3
            jump ch2ep2masturbate1
        "Slower":
            hide ch2ep2_eira3
            jump ch2ep2masturbate2
        "Cum":
            jump ch2ep2masturbatecum
label ch2ep2masturbatecum:
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_199_a13 with vpunch
    eira "(I'm cumming...!!!)"
    eira "(Mmmmmmm....!!!!)"
    $ renpy.pause()
    scene ch2ep2_199_a14 with dissolve
    eira "(*Pants*.... I can't believe... that I just did it.)"
    eira "(*Pants*.... I mean... I don't really... do it often..."
    eira "(*Pants*.... But, it's been a while... since I felt this good...)"
    eira "(*Giggles*.... Well, I guess once in a while won't hurt.)"
    eira "(Alright, let's take a bath and clean myself up.)"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_199_a15 with dissolve
    eira "(Ahh... This is so great...)"
    eira "(There is nothing better than lying in a bath after working for a whole day...)"
    eira "(Let's stay like this for as long as I can...)"
    $ renpy.end_replay()
    $ eira_relationship += 2
    $ eira_ch2_ep2 += 2
    jump ch2ep2_latenight
label ch2ep2_latenight:
    scene black with dissolve
    $ renpy.pause()
    if ch2ep2sexwithkrystal == 1 and ch2ep1rinsex == 1:
        play music "sfx/ch2ep2_6.mp3" fadein 3.0
        $ bgm = "Leonell Cassio - Sicked & Tired (ft. Lily Hain)"
        scene ch2ep2_201 with fade
        rin "(*Sighs* It was so hard to fall asleep.)"
        rin "(Weird. I drank a lot of water before bed, but now I'm thirsty again.)"
        rin "(Let's go grab a bottle of water in the kitchen...)"
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep2_202 with dissolve
        rin "(..... Hm? Who's that?)"
        rin "(Oh.... It's [krystal]....)"
        scene ch2ep2_203 with dissolve
        krystal ".... Hm? O-Oh...?!"
        krystal "*Sighs* You almost surprised me, [rin]."
        rin ".................."
        rin ".... I'm sorry."
        krystal "No need. I wasn't complaining."
        rin "Oh........"
        krystal "..... What are you doing up this late at night?"
        rin "..... I'm here for a bottle of water."
        krystal "I see......"
        rin "..... Okay then, if you don't mind....."
        krystal "O-Oh! Don't mind me! Go ahead!"
        rin "Thanks........"
        scene ch2ep2_204 with dissolve
        rin "......................."
        krystal "...................."
        krystal "(Ugh.... This is so awkward....)"
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep2_205 with dissolve
        rin "....................."
        krystal "..................."
        rin "..... Good night, [krystal]."
        krystal ".... Y-Yeah. You, too."
        scene ch2ep2_206 with dissolve
        krystal "(I don't like how this is going now....)"
        krystal "(She's always been sweet and friendly, but now she doesn't even smile.)"
        krystal "(She must be very angry at me for last night.)"
        krystal "(Well, I can't blame her for that, though....)"
        scene ch2ep2_207 with dissolve
        krystal "(Argh...! This is so awkward. I can't hold it anymore...!)"
        krystal "Hold on, [rin]..."
        rin "..................."
        krystal "..... Can we talk?"
        rin ".... Fine."
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep2_208 with dissolve
        rin "................."
        krystal "................."
        krystal "(*Sighs* Where should I begin?)"
        rin "*Sighs*.............."
        scene ch2ep2_209 with dissolve
        rin "... Are you and [mc] dating?"
        krystal "H-Hm...? Oh... No, we aren't."
        krystal "But, I like him."
        rin "What about [mc]? Does he like you?"
        scene ch2ep2_210 with dissolve
        krystal "I don't know.... I'm trying to figure it out."
        rin "...................."
        krystal "I mean... he is surely a good guy, but I can't read him at all."
        krystal "However, he's been helping me out a lot. I can assume he's been doing that because he likes me, right?"
        rin "So, you guys aren't dating, but you had sex with him."
        krystal "There is nothing wrong about that, right? I mean... this is 2021"
        krystal "We both have these thoughts, don't we?"
        rin ".... What do you mean?"
        krystal "We just want him to be ours first. Relationships can be developed afterwards."
        krystal ".... I also saw you having sex with him as well."
        scene ch2ep2_211 with dissolve
        rin "W-What...?! Where?! When?!"
        krystal "In his room one night...."
        krystal "I was about to go visit him and the door was ajar, so...."
        rin "Then, why didn't you ask me anything?"
        scene ch2ep2_212 with dissolve
        krystal "How could I...? No one seemed to know about things between you and him."
        krystal "So, I thought you didn't want anyone to know."
        rin "I see...."
        krystal "I felt so sad back then. I thought you guys were dating."
        krystal "I was wondering if I should give up on him, but I like him way too much to do that."
        krystal "So, when he said that you guys weren't dating. I was very happy and we ended up...."
        krystal "Can you forgive me? You're my friend. I don't want to see you angry at me."
        scene ch2ep2_213 with dissolve
        rin "*Sighs* To make things clear, I'm not angry at either you or him, okay?"
        rin "It's just.... I got jealous when I saw you guys last night."
        rin "*Smiles* It seems that our situations are pretty much the same."
        rin "Yeah, [mc] and I aren't dating, but I like him."
        rin "And just like you, I wanted to make him mine, so...."
        scene ch2ep2_214 with dissolve
        krystal "*Sighs* Well, looks like we're both having a tough time right now."
        krystal "There are many men out there, but we fall in love with the same guy."
        krystal "The worst part is, he is very, very, very reserved. Sometimes I can't begin to tell what he's thinking."
        rin "*Giggles* I know, right?"
        rin "Plus, I don't even know if he really knows what love is."
        rin "I don't blame him though, because I'm the one getting myself into this love game after all."
        rin "I'm just saying that there must be something that made him the way he is now."
        krystal "I totally agree with you."
        scene ch2ep2_215 with dissolve
        rin "*Smiles* Alright, let's stop being awkward with each other, shall we?"
        krystal "*Smiles* I should be the one saying that..."
        rin "*Giggles* What are you talking about? You weren't acting as awkward as I was!"
        krystal "*Giggles* Maybe you're right!"
        rin "*Smiles* Let's just have a fair fight!"
        rin "I'm not going to tell you to stop going after [mc], but I'll do whatever I want with him as well."
        rin "How does that sound?"
        krystal "Yeah, that sounds pretty good! And can promise me one thing?"
        rin "Yeah? What's it?"
        krystal "No matter who wins in the end, we won't be angry with each other, okay?"
        if ch2ep2havesexwithyui == True:
            rin "Sure! I promise y-"
            scene ch2ep2_215_a1 with dissolve
            unknown "Hang on a sec!"
            rin "H-Hm...?"
            scene ch2ep2_215_a2 with dissolve
            rin "... Y-Yui?! What are you doing here?"
            yui "Ha! Why are you so shocked to see me?!"
            rin "..................."
            yui "Well, I was going to get a cup of noodles, but guess what I just heard?!"
            scene ch2ep2_215_a3 with dissolve
            yui "Lucky me! I'm telling both of you now..."
            yui "There is no way I'm going to let you guys compete without me!"
            yui "[mc]. Is. Mine!"
            krystal "Oh my...!!"
            rin "W-What did you just say?!"
            rin "I thought you didn't like him?"
            scene ch2ep2_215_a4 with dissolve
            yui "*Blushes* Well, to be honest you're half right...."
            yui "I didn't like him at first, but after some time has passed I like him now."
            yui "He's been the only guy who's always on my side every time I needed him."
            yui "I confessed my feeling when we went to visit my parents..."
            rin "*Sighs* I knew it...."
            krystal "Wait... What?! Since when did you take him to visit your parents?"
            krystal "Why didn't anyone tell me about it before?"
            scene ch2ep2_215_a5 with dissolve
            yui "We went there Saturday, [krystal]."
            yui "I asked him to pretend to be my boyfriend, because I didn't want to get engaged."
            yui "But, it doesn't matter now. I've changed my plan."
            yui "I'm going to make him become my real boyfriend."
            krystal "Aw....."
            yui "I'm sorry, [krystal]. Even though you're my favorite idol, I won't let you have him without trying my best first."
            rin "*Sighs* Well, looks like our competition just became harder, [krystal]...."
            krystal "*Sighs* Yeah...."
            scene black with dissolve
            $ renpy.pause()
            stop music fadeout 3.0
            $ ch2ep2girltalk = True
            jump ch2ep2_nextmorning
        else:
            rin "Sure! I promise you!"
            scene black with dissolve
            $ renpy.pause()
            $ ch2ep2girltalk = True
            jump ch2ep2_nextmorning
    else:
        jump ch2ep2_nextmorning
label ch2ep2_nextmorning:
    if ch2ep2girltalk == True:
        play music "sfx/ch2ep2_2.mp3" fadein 3.0
        $ bgm = "Roa Music - Summer Days"
        scene ch2ep2_216 with fade
        u "Alright, I'm almost ready to go to work."
        u "Let's go have breakfast...."
        scene ch2ep2_217 with dissolve
        mc "Good morning...."
        rin "Oh, good morning, [mc]!"
        krystal "Hi, [mc]!"
        if ch2ep2havesexwithyui == True:
            yui "Good morning, [mc]!"
        else:
            yui "Hey...."
        scene ch2ep2_218 with dissolve
        zeke "What's up, bro!"
        mika "Morning, [mc]."
        zeke "Come on in! Let's have breakfast together!"
        mc "Sure."
        scene ch2ep2_219 with dissolve
        rin "*Smiles* [mc]...."
        mc "... Yes?"
        rin "This seat is available."
        rin "Go grab your breakfast and come sit right next to me."
        u "Hm...? She's acting normal now. All of sudden?"
        u "... Well, I guess it's because her period is already over."
        scene ch2ep2_220 with dissolve
        krystal "[mc]!"
        mc "... Hm?"
        krystal "The bench over there doesn't have a backrest."
        krystal "You should sit right here. This chair is way more comfortable to sit on!"
        if ch2ep2havesexwithyui == True:
            scene ch2ep2_220_a1 with dissolve
            yui "Don't listen to them, [mc]."
            yui "You should sit with me instead!"
            mc "Hm? What are you talking about, [yui]?"
            yui "What do you mean?"
            scene ch2ep2_220_a2 with dissolve
            rin "[mc] is right. What are you talking about, [yui]?"
            rin "There is no seat right next to you!"
            krystal "*Giggles* Hehe... Yeah, that's right."
            yui "W-What?!"
            scene ch2ep2_220_a3 with dissolve
            yui "Ugh...!"
            yui "*Sighs* Tch...! Now I know now why you guys hurried to take your seats."
            rin "*Giggles* Hehehehe...."
            mc "....................."
        scene ch2ep2_221 with dissolve
        zeke "Hm? What's up with you guys today?"
        zeke "Why are you trying so hard to make [mc] sit right next to you?"
        mika "(*Giggles* Look at them. They are so cute...)"
        scene ch2ep2_222 with dissolve
        mc "..................."
        u "Where should I sit?"
        menu:
            "Sit with [rin]":
                scene ch2ep2_222_r1 with dissolve
                rin "*Giggles* Good job, [mc]. You made the right choice..."
                mc "... Is that so?"
                rin "Of course it is! It's been a while since we last spent time together."
                rin "I have a lot of things to tell you about, so it is better for you to sit right next to me!"
                mc "I see...."
                if ch2ep2havesexwithyui == True:
                    scene ch2ep2_222_r2 with dissolve
                    yui "Jeez...."
                    krystal "Boo...."
            "Sit with [krystal]":
                scene ch2ep2_222_k1 with dissolve
                krystal "*Giggles* Good job, [mc]. You made the right choice..."
                mc "... Is that so?"
                krystal "Yeah! Why should you sit there when there is a better seat."
                krystal "You're going to have to spend a lot of energy on work today, so you better relax yourself as much as you can!"
                mc "I see...."
                if ch2ep2havesexwithyui == True:
                    scene ch2ep2_222_k2 with dissolve
                    yui "Jeez...."
                    rin "Boo...."
        scene black with dissolve
        $ renpy.pause()
        jump ch2ep2_fayeatpark
    else:
        scene black with dissolve
        $ renpy.pause()
        s "Next morning, you woke up and went to work as usual..."
        jump ch2ep2_fayeatpark
label ch2ep2_fayeatpark:
    stop music fadeout 5.0
    scene ch2ep2_223 with fade
    leo "Finally, it's lunch time, boys!"
    leo "Let's go find something delicious to eat!"
    joe "Yeah, let's go!!"
    u "....Well, I should probably go have lunch as well."
    if ch2ep2staywithfaye == 1:
        play music "sfx/ch2ep2_3.mp3" fadein 3.0
        $ bgm = "Firefl!es - Broken"
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep2_224 with dissolve
        u "Hm...?"
        u "I never knew there was a park right here."
        u "Well, there is still some time before the lunch break ends. Let's go see if it's any good."
        u "Who knows? Maybe this will be a good place for me to sit and relax in the future."
        scene black with dissolve
        scene ch2ep2_225 with dissolve
        u "... Great. I think I've just discovered my new favorite hideout."
        u "All these shade trees make the atmosphere so good here."
        u "I think I should come here more often...."
        scene ch2ep2_226 with dissolve
        u "... Hm?"
        scene ch2ep2_227 with dissolve
        u "Isn't that [faye]?"
        u "What is she doing here...?"
        u "She doesn't look so great right now. I can tell that from afar."
        menu:
            "[smgr]Approach her":
                u "I wonder what made her like that..."
                u "Let's go check if she needs help."
                scene black with dissolve
                scene ch2ep2_227_a1 with dissolve
                faye "Ugh......."
                mc "You alright?"
                faye "Hm....?"
                scene ch2ep2_227_a2 with dissolve
                faye "Oh, it's you."
                faye "What are you doing here?"
                mc "I was just walking around, and I saw you sitting here."
                mc "You didn't look good, so..."
                scene ch2ep2_227_a3 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_227_a3.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_227_a3_blink.jpg", 1) with dissolve
                faye "I see...."
                faye "Well, you're right. I'm not feeling very well. I've got a bit of a headache."
                mc "Hm? Do you need me to take you to a doctor, then?"
                faye "Thanks, but there is no need to. I think I will get better soon."
                mc "Are you sure?"
                faye "Yeah, I just need to sit here and rest for a little bit longer, then I will be fine."
                menu:
                    "Can I sit with you? [faye1]":
                        $ ch2ep2sitwithfaye = 1
                        $ faye_relationship += 1
                        $ faye_ch2_ep2 += 1
                        scene ch2ep2_227_a4_a1 with dissolve
                        mc "Do you mind if I sit with you for a sec?"
                        faye "No, I don't. Just take a seat, if that's what you want."
                        mc "Good to hear that. Thanks."
                        scene ch2ep2_227_a5 with dissolve
                        mc "... What gave you a headache?"
                        faye "Hm...?"
                        faye "*Sighs* Well, my work isn't going well right now."
                        mc "Why? What's wrong?"
                        faye "The composer we've been working with got in a car accident."
                        mc "... Really? Was it bad?"
                        faye "Yeah, it was. I just came from the hospital."
                        faye "The doctor said that he's got a very serious brain injury."
                        faye "The doctor couldn't even tell if he's going to wake up again."
                        mc "I'm sorry to hear that..."
                        scene ch2ep2_227_a6 with dissolve
                        faye "You have no idea how I felt on hearing the news."
                        faye "There are still plenty of in-game soundtracks missing, but the accident came out of nowhere."
                        faye "I mean... don't get me wrong. I feel very sad for him indeed, but I have to keep working."
                        faye "What's even worse is, there is no good composer available right now."
                        faye "I don't know if I can find one before the deadline."
                        if ch2ep1answeralice == 1:
                            mc "......................."
                            menu:
                                "Suggest [alice] [faye2]":
                                    $ ch2ep2suggestalice = 1
                                    $ faye_relationship += 2
                                    $ faye_ch2_ep2 += 2
                                    scene ch2ep2_227_a6_a1 with dissolve
                                    mc "Can I suggest someone?"
                                    faye "Hm? You know a good composer?"
                                    mc "Well...."
                                    mc "She's my friend. I don't know if she will be good enough in your opinion, but I think it's worth trying."
                                    faye "I'm down. Can you tell her to come to the company then? I want to talk with her in person."
                                    mc "Wait, I'm not sure if she'll be available right away. She signed a contract with another company not so long ago."
                                    mc "I'll ask her about that first, then I'll tell you if there is news."
                                    faye "I get it. Thank you so much, [mc]. I owe you one."
                                "Stay quiet":
                                    $ ch2ep2suggestalice = 2
                                    scene ch2ep2_227_a6_d1 with dissolve
                                    mc ".................."
                                    faye "*Sighs* What's wrong with me?"
                                    faye "Think positive! It's not like this is my first time dealing with problems, isn't it?"
                                    faye "Don't mind what I said earlier!"
                                    faye "I'm sure everything is going to be alright!"
                        else:
                            scene ch2ep2_227_a6_d1 with dissolve
                            mc ".................."
                            faye "*Sighs* What's wrong with me?"
                            faye "Think positive! It's not like this is my first time dealing with problems, isn't it?"
                            faye "Don't mind what I said earlier!"
                            faye "I'm sure everything is going to be alright!"
                        scene ch2ep2_227_a7 with dissolve
                        faye "Hey, it's almost 1 p.m."
                        faye "Let's go back to the office, [mc]."
                        mc "Sure. Let's go."
                        scene black with dissolve
                        stop music fadeout 5.0
                        $ renpy.pause()
                        s "*A few minutes later*..........."
                        play music "sfx/ch2ep2_5.mp3" fadein 3.0
                        $ bgm = "Leonell Cassio - I Saw A Ghost Last Night"
                        scene ch2ep2_227_a8 with dissolve
                        unknown "What do you mean I can't see her?!"
                        unknown "I'm her mother! Tell her to come down here right now!"
                        u "Hm...? What's going on over there?"
                        faye "Wait.... It can't be...."
                        scene ch2ep2_227_a9 with dissolve
                        faye ".... Mom?"
                        u "Hm...?"
                        faye "*Sighs* I was just starting to feel better, but here comes another problem..."
                        scene ch2ep2_227_a10 with dissolve
                        rg "I'm so sorry, ma'am...."
                        rg "You can't just come see her without making an appointment first."
                        rg "Even though you're her mother, I still can't let you in. This is one of our company's rules."
                        fayemom "What kind of bullshit rule is this? I don't care! Bring her to me now!"
                        faye ".... Mom? What are you doing here?"
                        scene ch2ep2_227_a11 with dissolve
                        fayemom "Oh! There you are!"
                        faye "Thank you, [ma]. You can leave it to me now."
                        ma "I'm sorry...."
                        faye "No worries. You're just doing your job. I understand that."
                        scene ch2ep2_227_a12 with dissolve
                        faye "What are you doing here, mom? You can't be here."
                        fayemom "Why can't I? My daughter is working here."
                        fayemom "Am I not allowed to visit my own daughter?"
                        mc "I think I should leave now. See you later, [faye]."
                        scene ch2ep2_227_a13 with dissolve
                        faye "Wait a sec."
                        mc "... Hm?"
                        faye "Don't leave just yet. Could you please stay?"
                        faye "I want your help with something."
                        mc "... Okay then."
                        scene ch2ep2_227_a14 with dissolve
                        fayemom "Well... Well... What am I seeing...?"
                        fayemom "Is he your boyfriend, [faye]?"
                        faye "You don't need to know that."
                        faye "We shouldn't talk here. Come, follow me."
                        scene black with dissolve
                        $ renpy.pause()
                        scene ch2ep2_227_a15 with dissolve
                        fayemom "Hmm...? What a beautiful room this is."
                        fayemom "Is this your office?"
                        faye "..................."
                        mc "..................."
                        scene ch2ep2_227_a16 with dissolve
                        faye "Why did you have to make such a scene down there, mom?"
                        fayemom "Who? Me? When did I make a scene?"
                        faye "Okay... Forget about it. What are you here for?"
                        fayemom "Why are you asking such a silly question?"
                        fayemom "You keep ignoring my calls. That's why I came here."
                        faye "What do you want?"
                        scene ch2ep2_227_a17 with dissolve
                        fayemom "Stop playing dumb already, [faye]."
                        fayemom "I know you know what I want..."
                        faye "*Sighs* Fine. How much do you want?"
                        fayemom "Not much. Just $50,000."
                        scene ch2ep2_227_a18 with dissolve
                        faye "W-What?! $50,000!!??"
                        faye "You've got to be kidding me!"
                        faye "What've you done? What do you need that amount of money for?!"
                        scene ch2ep2_227_a19 with dissolve
                        fayemom "Why do you have to overreact?"
                        fayemom "It's just $50,000. Before, I never cared about your job, but I decided to check some background information."
                        fayemom "I know that you earn that in only a month."
                        fayemom "Don't worry. I will pay back your money once I get mine back as well."
                        scene ch2ep2_227_a20 with dissolve
                        faye "Ouch...!! My head...!!"
                        mc "... Are you alright, [faye]?"
                        faye ".... I'm good. Don't worry about me."
                        faye "When are you going to stop, mom?!"
                        faye "Seriously? After all these years, you've still never learned your lesson?"
                        fayemom "Shut up! You know nothing!"
                        faye "*Sighs*..............."
                        scene ch2ep2_227_a21 with dissolve
                        faye "You aren't going to leave until I give you that money, right?"
                        fayemom "Yeah, that's right."
                        fayemom "Just trust your mom, [faye]. I have a really strong feeling that this time I'm going to win!"
                        faye "You said that a million times already."
                        faye "*Sighs* Fine.... Wait a sec then."
                        fayemom "That's my daughter! I knew that you wouldn't let me down!"
                        scene black with dissolve
                        scene ch2ep2_227_a22 with dissolve
                        faye "...................."
                        mc "..................."
                        u ".... What's she doing?"
                        scene black with dissolve
                        scene ch2ep2_227_a23 with dissolve
                        faye "...................."
                        mc "...................."
                        scene ch2ep2_227_a24 with dissolve
                        faye "Sign this...."
                        fayemom "... Hm? What's it?"
                        faye "Just read it for yourself."
                        fayemom "Fine..."
                        scene ch2ep2_227_a25 with dissolve
                        faye "[mc]."
                        mc "Yes?"
                        faye "Can you come here real quick, please? I'm going to need your help."
                        mc "Oh. Okay...."
                        fayemom "What is this...?!"
                        scene ch2ep2_227_a26 with dissolve
                        faye "It's a letter of agreement. You don't know what it is?"
                        fayemom "Of course, I do."
                        fayemom "I just don't understand why you have to make things so complicated."
                        fayemom "You're my daughter. I'm your mother. We don't need this paper."
                        scene ch2ep2_227_a27 with dissolve
                        faye "Of course, we do."
                        faye "At first, I didn't want to do this, either, because you're my mother."
                        faye "But, I've had enough. So, I'm offering you a choice."
                        faye "You and I sign this paper. [mc], as a witness, will also sign, too."
                        faye "Then, I'm going to give you the money."
                        faye "However, this is going to be the last time as I wrote in the agreement."
                        fayemom "W-What?!"
                        faye "So, if you come to borrow any more money, I will have no choice, but let the law take its course..."
                        fayemom "There is no way I'm going to sign it!!"
                        faye "Well then, you can leave now."
                        scene ch2ep2_227_a28 with dissolve
                        fayemom "What?! What an ungrateful daughter you are!!"
                        fayemom "How can you do this to your own mother!?"
                        fayemom "You can't do this to me! I'm the one who raised you up!!"
                        faye "What...?! You're the one who raised me up?!"
                        faye "Excuse me? As I remember, I was the one raising myself!"
                        faye "What kind of mother are you treating your own daughter like this?"
                        faye "You're the worst mother ever!"
                        scene ch2ep2_227_a29 with dissolve
                        fayemom "W-What?! How dare you...!!"
                        menu:
                            "Protect [faye] [faye2]":
                                $ ch2ep2protectfaye = 1
                                $ faye_relationship += 2
                                $ faye_ch2_ep2 += 2
                                scene ch2ep2_227_a29_a1 with dissolve
                                faye "!!!!!"
                                fayemom "W-What..?!"
                                mc "Step back, [faye]..."
                                scene ch2ep2_227_a29_a2 with dissolve
                                fayemom "Step aside, young man! This is none of your business."
                                fayemom "I am trying to punish my bad daughter. Who are you to intervene?"
                                mc ".... I'm well aware that she is your daughter. That's why I did nothing until you tried to hit her."
                                fayemom "So what? I'm her mother. I can do anything I want to her!"
                                mc ".... No, you c-"
                                scene ch2ep2_227_a29_a3 with dissolve
                                faye "[mc]...."
                                mc "... Hm?"
                                faye "Thank you for protecting me. I truly appreciate your kindness."
                                faye "But, that's enough. Let me take care of her now, okay?"
                                mc "Okay. If you say so."
                                scene ch2ep2_227_a29_a4 with dissolve
                                faye "If you aren't going to sign the paper, then get out of here now!"
                                fayemom "You can't do this to me, [faye]!"
                                faye "I'm not going to repeat myself, mom..."
                                fayemom "Ugh...! Fine! I'm going to sign it!"
                            "Warn her":
                                $ ch2ep2protectfaye = 2
                                mc "Watch out, [faye]."
                                scene ch2ep2_227_a29_d1 with dissolve
                                faye "Ouch...!"
                                u "Shit... That was too late."
                                scene ch2ep2_227_a29_d2 with dissolve
                                mc "... Are you okay?"
                                faye "... I'm alright. Don't worry about me."
                                faye "It's not like this is my first time getting hit."
                                scene ch2ep2_227_a29_d3 with dissolve
                                faye "It's been a while, [mom]."
                                faye "Thanks for reminding me how it feels to get slapped in the face."
                                faye "Well... It doesn't hurt much this time, though. You are indeed getting older, mom."
                                fayemom "What...?! I'm gonna slap you real hard this tim-!"
                                scene ch2ep2_227_a29_d4 with dissolve
                                faye "I don't care even if you're going to slap me more, but I'm not going to change my mind."
                                faye "Sign the paper if you want the money. This is your last chance."
                                faye "Otherwise, I will have no choice but to call security."
                                fayemom "You can't do this to me, [faye]!"
                                faye "I'm not going to repeat myself, mom..."
                                fayemom "Ugh...! Fine! I'm going to sign it!"
                        scene black with dissolve
                        $ renpy.pause()
                        s "*A few minutes later*........."
                        scene ch2ep2_227_a30 with dissolve
                        faye "Don't you ever come back again, mom."
                        faye "I don't want to see you anymore."
                        fayemom "I don't want to see you either!"
                        fayemom "Tch...! I really shouldn't have let you be born in the first place!"
                        fayemom "That was the stupidest mistake I've ever made!"
                        scene black with dissolve
                        $ renpy.pause()
                        scene ch2ep2_227_a31 with dissolve
                        faye "................"
                        mc "................."
                        faye "*Hics*........."
                        mc "... Are you okay?"
                        scene ch2ep2_227_a32 with dissolve
                        $ renpy.pause()
                        scene ch2ep2_227_a33 with dissolve
                        faye "Yeah, I'm good! Never been any better!"
                        mc "... Are you sure?"
                        faye "Yes, I am! Don't worry about me!"
                        u "There is no way she is okay. It's so obvious that she's just trying to act strong...."
                        faye "Alright, I think I should let you go now."
                        faye "I've taken a lot of your time already."
                        mc "Oh... Okay. I'll go, then."
                        faye "Thanks a lot, [mc]. See you around."
                        jump ch2ep2_afterwork
                    "Alright, I'm leaving then":
                        $ ch2ep2sitwithfaye = 2
                        scene ch2ep2_227_a4_d1 with dissolve
                        mc "Alright then, I'm leaving now."
                        mc "See you later."
                        faye "Bye, [mc]."
                        u "She might be stressed because of work."
                        u "I don't think it's a good idea to bother her."
                        u "Let's just leave her some time alone."
                        scene black with dissolve
                        $ renpy.pause()
                        jump ch2ep2_afterwork
            "Leave":
                scene ch2ep2_227_d1 with dissolve
                u "She might be stressed because of work."
                u "I don't think it's a good idea to bother her."
                u "Let's just leave her some time alone."
                scene black with dissolve
                $ renpy.pause()
                jump ch2ep2_afterwork
    else:
        scene black with dissolve
        $ renpy.pause()
label ch2ep2_afterwork:
    stop music fadeout 4.0
    scene black with dissolve
    s "*A few hours later*.........."
    scene ch2ep2_228 with dissolve
    u "... Okay. It's time to go home now."
    if ch2ep2protectfaye == 1:
        $ ch2ep2fayemessage = True
        $ newmessage = True
        $ faye_messages_show = True
        $ faye_newmessage = True
        $ phone_alert = True
        s "*Phone vibrates*.........."
        scene ch2ep2_229 with dissolve
        u "Hm...?"
        u "Was that a new message?"
        u "Well, let's check it."
        jump ch2ep2_checkfayemessage
    else:
        scene ch2ep2_231 with dissolve
        mc "Let's go home, [yui]."
        yui "Yeah, let's go."
        jump ch2ep2_pt2end
label ch2ep2_checkfayemessage:
    if ch2ep2_reply_faye1 == False:
        scene ch2ep2_230 with vpunch
        u "I should answer the message first!"
        jump ch2ep2_checkfayemessage
    elif ch2ep2_reply_faye1 == True:
        scene ch2ep2_230 with dissolve
        u "Alright, that is it."
        jump ch2ep2_afterwork2
label ch2ep2_afterwork2:
    if ch2ep2suggestalice == 1:
        u "Oh... I almost forgot."
        u "I have to ask [alice] if she can come meet [faye]."
        u "Let's send her a message..."
        scene black with dissolve
        $ renpy.pause()
        s "*A few minutes later*........"
        $ ch2ep2alicemessage = True
        $ newmessage = True
        $ alice_messages_show = True
        $ alice_newmessage = True
        $ phone_alert = True
        scene ch2ep2_230 with dissolve
        u "Okay... She's answering now."
        u "Let's see what she says..."
        jump ch2ep2_checkalicemessage
    jump ch2ep2_afterwork3
label ch2ep2_checkalicemessage:
    if alice_newmessage == True:
        scene ch2ep2_230 with vpunch
        u "I need to read [alice]'s message first!"
        jump ch2ep2_checkalicemessage
    elif alice_newmessage == False:
        scene ch2ep2_230 with dissolve
        u "Okay... Looks like there is nothing I can do now."
        u "Let's just wait until she sends me the answer."
        jump ch2ep2_afterwork3
label ch2ep2_afterwork3:
    scene ch2ep2_231 with dissolve
    if ch2ep2_reply_faye1_choice == 1:
        mc "Hey, [yui]."
        yui "Hm...?"
        mc "I'm not going home with you guys today."
        mc "I have to take care of something. Don't wait for me."
        yui "Oh... Okay."
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep2_232 with dissolve
        u "There she is...."
        scene ch2ep2_233 with dissolve
        mc "Sorry to keep you waiting."
        faye "No worries. It only took you five minutes to get here."
        faye "Alright, let's not waste any time here. Let's go."
        mc "Where are we going, by the way?"
        faye "My house."
        mc "Oh, I see... Let's go then."
        jump ch2ep2_dinnerwithfaye
    elif ch2ep2_reply_faye1_choice == 2:
        mc "Let's go home, [yui]."
        yui "Yeah, let's go."
        jump ch2ep2_pt2end
label ch2ep2_dinnerwithfaye:
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa Music - Summer Days"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_234 with fade
    faye "Come on in."
    faye "Make yourself at home."
    mc "Sure."
    scene ch2ep2_235 with dissolve
    u "Hm...? So, this is what her house looks like..."
    mc "Nice house. I like it."
    faye "Thanks...."
    mc "By the way, do you live here all alone?"
    faye "Yeah, why?"
    mc "Nothing. It just seems a little too big for one person, in my opinion."
    faye "I understand that, but I don't like living in a small place, so..."
    scene ch2ep2_236 with dissolve
    faye "Alright, I'm going to get changed first."
    faye "Can you take a seat and wait for me here?"
    faye "I'll start cooking after I get changed."
    mc "Sure. Take your time."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_237 with dissolve
    u "................"
    faye "... [mc]."
    u "Hm...?"
    scene ch2ep2_238 with dissolve
    mc "Oh... that was quick. It's only been five minutes."
    faye "Well, I didn't want to make you wait too long."
    faye "Look. I'm going to cook steak for dinner today."
    faye "Is there anything you want to eat in particular?"
    mc "No, there isn't. Steak sounds good to me."
    faye "Alright then."
    scene ch2ep2_239 with dissolve
    mc "By the way, is there anything I can help with?"
    faye "Hm? You know how to cook, too?"
    mc "No, I don't...."
    mc "But, I want to help."
    faye "Well... If you say so, follow me to the kitchen."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_240 with dissolve
    faye "Alright, I've got an idea."
    faye "Can you wash vegetables while I'm cooking?"
    faye "It will save us a lot of time if you can."
    mc "Sure. Leave it to me."
    scene black with dissolve
    s "*Half an hour later*........."
    scene ch2ep2_241 with dissolve
    faye "[mc], could you go set the table, please?"
    faye "Dinner is almost ready."
    mc "Okay. I get it."
    faye "Oh! By the way, there is a wine bottle on the shelf near the table out there."
    faye "You might want to pick it up."
    mc "Understood."
    scene black with dissolve
    $ renpy.pause()
    s "After that, you had dinner with [faye] for almost an hour..."
    scene ch2ep2_242 with dissolve
    mc "Thank you for dinner, [faye]."
    mc "It was very tasty. I enjoyed it a lot."
    faye "You're welcome. I'm glad to hear that."
    mc "Alright then, let me wash these dishes before I leave."
    scene ch2ep2_243 with dissolve
    faye "Hm? You want to leave already?"
    mc "... Yeah, why?"
    faye "Why so hasty? The night is still young."
    faye "Let's hang out together for a little bit more."
    mc "... Okay. What do you want to do then?"
    faye "Why don't we watch a movie for a while?"
    mc "Alright then."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_244 with dissolve
    faye "*Laughs* Oops...! Hahahaha...!"
    faye "*Laughs* Hahahaha...!"
    mc "..................."
    u "I've never seen her laugh this hard before. Something is wrong here..."
    scene ch2ep2_245 with dissolve
    faye "*Laughs* [mc]..."
    mc "... Yes?"
    faye "*Laughs* That was funny, wasn't it?!"
    faye "*Laughs* He was such an idiot! I wonder what was going through his mind!"
    mc "................"
    scene ch2ep2_246 with dissolve
    faye "Hey! What's wrong?"
    faye "Why aren't you drinking? Where is your glass?"
    mc "I've had enough drink, [faye]."
    faye "Don't be like that! Here! Take my glass!"
    mc "I don't think I should drink more. I still have to go ho-"
    faye "Take it!"
    mc "..................."
    mc "*Sighs* Fine...."
    scene ch2ep2_247 with dissolve
    faye "Come on. Drink up."
    faye "You better not waste a single drop."
    mc "Okay... Okay..."
    scene ch2ep2_248 with dissolve
    mc "All good now?"
    stop music fadeout 4.0
    faye "*Giggles* Yeah~! Good boy~!"
    play music "sfx/ch2ep2_7.mp3" fadein 3.0
    $ bgm = "Neutrin05 - Rain and Tears"
    mc "................"
    scene ch2ep2_249 with dissolve
    faye "................."
    u "Hm....?"
    scene ch2ep2_250 with dissolve
    faye "*Hics*..............."
    mc "................"
    u "... I knew it. It's been a very tough day for her today."
    u "She was way too happy for what's she been through."
    u "No matter how much we try to act strong, everyone has their own weak spots."
    scene ch2ep2_251 with dissolve
    faye "*Hics* I'm sorry... I know I shouldn't be like this, but..."
    mc "It's okay. There is no need for you to apologize at all."
    faye "*Hics*................."
    faye "*Hics* Do you think I made the right choice today?"
    faye "*Hics* I shouldn't have done that to my mother, right?"
    scene ch2ep2_252 with dissolve
    mc "... Well, I don't think I can judge you for that."
    mc "Since I'm an orphan after all. I don't know what it's like to have a mother."
    faye "*Hics* I'm so sorry...."
    mc "No worries..."
    faye "*Hics* To be honest, I feel you. Even though I have a mother, I've never felt like I had one."
    faye "*Hics* My mom worked as a hooker. She often said I was an accident."
    faye "*Hics* As I remember, she never really took care of me."
    faye "*Hics* She often brought a guy home. It was so funny actually."
    faye "*Hics* Could you imagine how weird I felt seeing her take care of them better than her own daughter?"
    mc "....................."
    scene ch2ep2_253 with dissolve
    faye "*Hics* What's worse is, she's an alcoholic, and she hit me whenever she was drunk."
    faye "*Hics* She'd say that I was an accident when she did it."
    faye "*Hics* I decided to not be someone like her, so I started working part-time for money as soon as I got into a high school."
    faye "*Hics* But when my mother found out I was earning some money, she took it to spend it on gambling."
    faye "*Hics* Moreover, no matter how hard I worked or studied, other kids treated me like I had some kind of disease knowing that I was a daughter of a hooker."
    faye "*Hics* A guy I was dating was no different. At first, he was so nice to me, that's why I started dating him."
    faye "*Hics* But after he found out about my mom, he dumped me like I was a piece of trash."
    u "... That's terrible. I'd never imagine that someone with such a strong image like [faye], would've had a terrible life as a child."
    mc "Hey... You aren't what they said. Don't let anyone define your self-worth."
    faye "*Hics* Thank you...."
    scene black with dissolve
    $ renpy.pause()
    s "*An hour later*............"
    scene ch2ep2_254 with dissolve
    faye "..................."
    mc "..................."
    mc "... [faye]. Are you better now?"
    mc "It's already dark. I think I should go home now."
    faye "...................."
    scene ch2ep2_255 with dissolve
    u ".... Hm?"
    faye "..................."
    u "Oh, she fell asleep already? I didn't notice that at all."
    u "*Sighs* Well, looks like I have no choice..."
    scene black with dissolve
    scene ch2ep2_256 with dissolve
    mc "Hey... I'm going to take you to your room."
    mc "Where is it at?"
    faye "..................."
    mc "*Sighs*.............."
    scene ch2ep2_257 with dissolve
    u "Well...."
    u "Let's just go randomly open doors until I find her room."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_258 with dissolve
    u "Okay. Here we are...."
    u "I'm pretty sure this is her room since it's the only one so far with a bed."
    u "Let's go put her down on the bed, and leave."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_259 with dissolve
    u "Alright, it's time to go home...."
    mc "Hey, [faye]. I'm leaving now."
    mc "See you tomorro-"
    scene ch2ep2_260 with dissolve
    u "Hm....?"
    faye "Hold on..."
    scene ch2ep2_261 with dissolve
    mc "Oh, you're awake?"
    faye "... Yeah, I was awake while you were looking for my room."
    mc "Hm? Why didn't you tell me, then?"
    faye "I thought it would've been a little awkward if I did, so...."
    mc "I see... Is there anything you want by the way? Why are you holding me here?"
    faye "..................."
    faye "... Could you please stay here with me for a night?"
    mc "... Are you still drunk?"
    faye "No, I'm not. Just a little bit tipsy."
    mc "................."
    menu:
        "Stay here for the night [faye2]":
            $ ch2ep2spendnightwithfate = 1
            $ faye_relationship += 2
            $ faye_ch2_ep2 += 2
            scene ch2ep2_261_a1 with dissolve
            mc "... Alright, if you say so."
            faye "*Smiles* I wanted to have someone by my side tonight."
            faye "*Smiles* Thank you for being the one for me"
            mc "You're welcome. Alright, I'm going to the living room then. Sleep well, [faye]."
            scene ch2ep2_261_a2 with dissolve
            faye "Hm...? What are you talking about?"
            faye "I meant... I wanted you to stay {b}here{/b} with me."
            faye "Get in the bed, [mc]. I want you to sleep right next to me tonight."
            mc "Oh... Okay, let me turn off the light first then."
            faye "Sure."
            scene black with dissolve
            $ renpy.pause()
            scene ch2ep2_261_a3 with dissolve
            mc ".................."
            faye "................."
            scene ch2ep2_261_a4 with dissolve
            faye ".... [mc]. Are you still awake?"
            u "Hm...?"
            mc "Yes, I am."
            faye ".... Could you please hug me from behind?"
            faye "I want to sleep like that tonight, but if it's too much to ask, I understand."
            mc "..................."
            scene ch2ep2_261_a5 with dissolve
            faye "Thank you...."
            mc "Anytime."
            scene black with dissolve
            $ renpy.pause()
            s "*A few moments later*.........."
            stop music fadeout 4.0
            scene ch2ep2_261_a6 with dissolve
            u "................"
            u "... Hm?"
            scene ch2ep2_261_a7 with dissolve
            mc "Hey... Stop moving your hips like that, [faye]."
            mc "This won't be good...."
            faye "................."
            mc "... [faye]?"
            faye "... zzzZZZ"
            u "Looks like she's really sleeping, and wasn't doing that intentionally."
            u "She's probably just moving her body without realizing it."
            u "I should sleep, too. It's getting very late."
            jump ch2ep2dream
        "I better leave":
            $ ch2ep2spendnightwithfate = 2
            scene ch2ep2_261_d1 with dissolve
            mc "I'm sorry, [faye]."
            mc "But, I think I should really go home."
            mc "I don't want others to worry about me."
            faye ".... Okay. I get it."
            faye "You should leave now then. Thank you for today, [mc]."
            faye "Good night."
            mc "You, too. See you later."
            jump ch2ep2_pt2end
label ch2ep2dream:
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
    play music "sfx/ch2ep2_8.mp3" fadein 3.0
    $ bgm = "Sabai - Million Days (Acoustic) feat. Hoang & Claire Ridgely"
    scene ch2ep2_261_a8 with dissolve
    show ch2ep2_faye1 with dissolve
    window hide
    u "... Hm? What's going on?"
    faye "*Licks* Mmmm...."
    u "Hm? What was that sound?"
    u "I'm also feeling so weird, but great at the same ti-"
    u "Oh, wait..."
    $ renpy.pause()
    hide ch2ep2_faye1
    scene ch2ep2_261_a9 with dissolve
    mc "... [faye]? What are you doing?"
    faye "Hm~? Finally, you're awake, hehe..."
    mc "... Wait. Are you drunk?"
    faye "I told you that I'm not, didn't I?"
    faye "Come on. Since you're already awake, what are you waiting for?"
    faye "Why haven't you started to lick my pussy yet?"
    mc "Err... Okay."
    u "I don't know what she's thinking, but I'll just play along."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_261_a10 with dissolve
    show ch2ep2_faye2 with dissolve
    window hide
    faye "*Sucks* Mmmm... Yeah, keep licking... it like that..."
    faye "*Sucks* Mmmm... If you... do it good, I'll... suck you real good in return, too!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_faye2
    scene ch2ep2_261_a11 with dissolve
    show ch2ep2_faye3 with dissolve
    window hide
    faye "*Sucks* Mmmm... A-Ah... That's the spot...!"
    faye "*Sucks* A-Ah... Don't... stop...!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_faye3
    scene ch2ep2_261_a12 with dissolve
    faye "Alright, I think that's enough of a warm-up."
    faye "I'm already wet enough. Let's do it."
    mc "... Are you sure?"
    faye "Yep!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_261_a13 with dissolve
    faye "Okay... Stay still, I'm going to put it in..."
    faye "*Smiles* It's been so lo-!"
    scene ch2ep2_261_a14 with dissolve
    faye "Long...!!!"
    faye "*Softly breathes* A... As expected, it feels so good..."
    mc "Ugh... Your pussy is so fit, [faye]..."
    scene black with dissolve
    scene ch2ep2_261_a15 with dissolve
    show ch2ep2_faye4 with dissolve
    window hide
    faye "*Softly breathes* A..Ahh...!"
    faye "*Softly breathes* Mmmm... Y.. You're so big..!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_faye4
    scene ch2ep2_261_a16 with dissolve
    show ch2ep2_faye5 with dissolve
    window hide
    faye "*Softly breathes* Mmmm...! It's also... so long...!"
    faye "*Softly breathes* Ahh...! This feels too good...! It keeps... touching my womb non-stop...!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_faye5
    scene ch2ep2_261_a17 with dissolve
    show ch2ep2_faye6 with dissolve
    window hide
    faye "*Heavily breathes* A-Ahhh...! [mc]...! [mc]...!"
    faye "*Heavily breathes* Mmmm...! You're driving me crazy...!"
    $ renpy.pause()
    menu:
        "Next":
            mc "*Softly breathes* Can I take the lead?"
            faye "*Heavily breathes* Mmmmm...! Y-Yeah...! Whatever you want...!"
            hide ch2ep2_faye6
    scene ch2ep2_261_a18 with dissolve
    show ch2ep2_faye7 with dissolve
    window hide
    faye "*Softly breathes* A-Ah...!"
    mc "Hm? What's wrong? Did it hurt?"
    faye "*Softly breathes* N... No, it didn't. It's just... boobs are my weak spot..."
    mc "I see...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_faye7
    scene ch2ep2_261_a19 with dissolve
    show ch2ep2_faye8 with dissolve
    window hide
    faye "*Moans* Mmmm...! Y-Yeah...! Keep squeezing my boobs like that...!"
    faye "*Moans* A-Ahh...! Harder...! Harder...!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2_faye8
    scene ch2ep2_261_a20 with dissolve
    show ch2ep2_faye9 with dissolve
    window hide
    faye "*Heavily breathes* Mmmm...! I'm almost there....!"
    mc "Ugh...! I'm about to cum...!"
    faye "*Heavily breathes* W..Wait...! Mmmm...! Don't you cum just yet...!"
    faye "*Heavily breathes* Mmmm...! I want you... to fuck my boobs, then we can... cum together...!"
    menu:
        "Next":
            hide ch2ep2_faye9
    scene ch2ep2_261_a21 with dissolve
    show ch2ep2_faye10 with dissolve
    window hide
    faye "*Heavily breathes* Mmmmm...! H-Hehe...! Yeah, keep fucking my boobs like that...!"
    faye "*Heavily breathes* A-Ah...! A-Almost there...!"
    mc "Me, too...!"
    menu:
        "Cum":
            jump ch2ep2fayeboobfuckcum
        "69":
            hide ch2ep2_faye10
            jump ch2ep2faye69slow
        "Reverse cowgirl":
            hide ch2ep2_faye10
            jump ch2ep2fayereverse1
        "Missionary":
            hide ch2ep2_faye10
            jump ch2ep2fayemis1
label ch2ep2faye69slow:
    scene ch2ep2_261_a10 with dissolve
    show ch2ep2_faye2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ch2ep2_faye2
            jump ch2ep2faye69fast
        "Reverse cowgirl":
            hide ch2ep2_faye2
            jump ch2ep2fayereverse1
        "Missionary":
            hide ch2ep2_faye2
            jump ch2ep2fayemis1
        "Boobs fuck":
            hide ch2ep2_faye2
            jump ch2ep2fayeboobfuck
label ch2ep2faye69fast:
    scene ch2ep2_261_a11 with dissolve
    show ch2ep2_faye3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ch2ep2_faye3
            jump ch2ep2faye69slow
        "Reverse cowgirl":
            hide ch2ep2_faye3
            jump ch2ep2fayereverse1
        "Missionary":
            hide ch2ep2_faye3
            jump ch2ep2fayemis1
        "Boobs fuck":
            hide ch2ep2_faye3
            jump ch2ep2fayeboobfuck
label ch2ep2fayereverse1:
    scene ch2ep2_261_a15 with dissolve
    show ch2ep2_faye4 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ch2ep2_faye4
            jump ch2ep2fayereverse2
        "Fastest":
            hide ch2ep2_faye4
            jump ch2ep2fayereverse3
        "69":
            hide ch2ep2_faye4
            jump ch2ep2faye69slow
        "Missionary":
            hide ch2ep2_faye4
            jump ch2ep2fayemis1
        "Boobs fuck":
            hide ch2ep2_faye4
            jump ch2ep2fayeboobfuck
label ch2ep2fayereverse2:
    scene ch2ep2_261_a16 with dissolve
    show ch2ep2_faye5 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ch2ep2_faye5
            jump ch2ep2fayereverse1
        "Faster":
            hide ch2ep2_faye5
            jump ch2ep2fayereverse3
        "69":
            hide ch2ep2_faye5
            jump ch2ep2faye69slow
        "Missionary":
            hide ch2ep2_faye5
            jump ch2ep2fayemis1
        "Boobs fuck":
            hide ch2ep2_faye5
            jump ch2ep2fayeboobfuck
label ch2ep2fayereverse3:
    scene ch2ep2_261_a17 with dissolve
    show ch2ep2_faye6 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slowest":
            hide ch2ep2_faye6
            jump ch2ep2fayereverse1
        "Slower":
            hide ch2ep2_faye6
            jump ch2ep2fayereverse2
        "69":
            hide ch2ep2_faye6
            jump ch2ep2faye69slow
        "Missionary":
            hide ch2ep2_faye6
            jump ch2ep2fayemis1
        "Boobs fuck":
            hide ch2ep2_faye6
            jump ch2ep2fayeboobfuck
label ch2ep2fayemis1:
    scene ch2ep2_261_a18 with dissolve
    show ch2ep2_faye7 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            hide ch2ep2_faye7
            jump ch2ep2fayemis2
        "Fastest":
            hide ch2ep2_faye7
            jump ch2ep2fayemis3
        "69":
            hide ch2ep2_faye7
            jump ch2ep2faye69slow
        "Reverse cowgirl":
            hide ch2ep2_faye7
            jump ch2ep2fayereverse1
        "Boobs fuck":
            hide ch2ep2_faye7
            jump ch2ep2fayeboobfuck
label ch2ep2fayemis2:
    scene ch2ep2_261_a19 with dissolve
    show ch2ep2_faye8 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            hide ch2ep2_faye8
            jump ch2ep2fayemis1
        "Faster":
            hide ch2ep2_faye8
            jump ch2ep2fayemis3
        "69":
            hide ch2ep2_faye8
            jump ch2ep2faye69slow
        "Reverse cowgirl":
            hide ch2ep2_faye8
            jump ch2ep2fayereverse1
        "Boobs fuck":
            hide ch2ep2_faye8
            jump ch2ep2fayeboobfuck
label ch2ep2fayemis3:
    scene ch2ep2_261_a20 with dissolve
    show ch2ep2_faye9 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slowest":
            hide ch2ep2_faye9
            jump ch2ep2fayemis1
        "Slower":
            hide ch2ep2_faye9
            jump ch2ep2fayemis2
        "69":
            hide ch2ep2_faye9
            jump ch2ep2faye69slow
        "Reverse cowgirl":
            hide ch2ep2_faye9
            jump ch2ep2fayereverse1
        "Boobs fuck":
            hide ch2ep2_faye9
            jump ch2ep2fayeboobfuck
label ch2ep2fayeboobfuck:
    scene ch2ep2_261_a21 with dissolve
    show ch2ep2_faye10 with dissolve
    window hide
    menu:
        "Cum":
            jump ch2ep2fayeboobfuckcum
        "69":
            hide ch2ep2_faye10
            jump ch2ep2faye69slow
        "Reverse cowgirl":
            hide ch2ep2_faye10
            jump ch2ep2fayereverse1
        "Missionary":
            hide ch2ep2_faye10
            jump ch2ep2fayemis1
label ch2ep2fayeboobfuckcum:
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_261_a22 with dissolve
    mc "I'm cummi-"
    mc "................"
    mc "... Hm?"
    scene ch2ep2_261_a23 with dissolve
    u "Wait... Was it just a dream?"
    u "...................."
    u "Yeah, it seems so...."
    u "I'm sorry, [faye]. I don't know why I dreamed about doing something like that with you..."
    u "*Sighs* Fortunately, I didn't actually cum. It would've been a disaster if I did."
    u "It's still dark right now. Let's just get back to sleep...."
    scene black with dissolve
    $ renpy.pause()
    s "*A few hours later*........."
    scene ch2ep2_261_a24 with dissolve
    faye "................"
    faye "(....Hm? It's already morning?)"
    scene ch2ep2_261_a25 with dissolve
    faye "(Ouch...! My head...!)"
    faye "(What happened last night...?!)"
    scene ch2ep2_261_a26 with dissolve
    faye "(.... Wait. Why is he here?)"
    faye "...................."
    faye "(Oh, I remember now. I was the one who asked him to sleep here myself.)"
    scene ch2ep2_261_a27 with dissolve
    faye "...................."
    faye "(... Well, now that I think about it, I can't believe I actually asked him that.)"
    faye "(I guess it was because I was a little bit drunk...)"
    faye "(Anyway, I'm very happy that he chose to stay by my side as I asked him to.)"
    faye "(Yesterday was a very tough day for me, but he helped me get through it.)"
    faye "...................."
    faye "*Giggles* Look at you sleeping. So cute...."
    scene ch2ep2_261_a28 with dissolve
    faye "(You did well yesterday, [mc].)"
    faye "(This is your reward....)"
    scene ch2ep2_261_a29 with dissolve
    faye "Hey. Wake up, sleepyhead."
    faye "It's already morning."
    faye "We need to go to work soon."
    scene black with dissolve
    s "*A few seconds later........."
    scene ch2ep2_261_a30 with dissolve
    mc "................."
    u "What was that weird feeling earlier? I couldn't clearly tell..."
    faye "Finally, you're up."
    mc "... Good morning, [faye]."
    faye "*Smiles* Good morning."
    mc "What time is it now?"
    faye "It's half-past seven."
    mc "I see..."
    faye "Get up already, lazy. I don't want to be late for work."
    mc "Okay, sure."
    scene black with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    $ faye_relationship += 2
    $ faye_ch2_ep2 += 2
    jump ch2ep2_pt2end
label ch2ep2_pt2end:
    stop music fadeout 4.0
    scene black with dissolve
    $ renpy.pause()
    jump ch2ep2_pt3start
label ch2ep2_pt3start:
    if ch2ep2spendnightwithfate == 1:
        $ ch2ep2spendnightwithfaye = 1
    if ch2ep2spendnightwithfaye == 1:
        jump ch2ep2gotoworkwithfaye
    else:
        s "*Next morning*.........."
        scene ch2ep2_263 with dissolve
        u "... Alright, it's almost time for work."
        u "Let's go to the department office."
        jump ch2ep2pt3atwork
label ch2ep2gotoworkwithfaye:
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    scene ch2ep2_262 with fade
    faye "Alright, your department is on this floor, right?"
    faye "Let's part ways here, then."
    mc "Okay, sure."
    faye "Good luck with your work today."
    mc "Thanks. You, too."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_263 with dissolve
    u "... Alright, let's go to the department office."
    unknown "Finally, there you are."
    u "Hm...?"
    scene ch2ep2_264 with dissolve
    u "Oh? It's [yui]."
    u "I wonder what she is doing over there."
    scene ch2ep2_265 with dissolve
    mc "Good morning, [yui]."
    yui "So, you're still alive, huh?"
    mc "Hm? What do you mean?"
    yui "Everyone has been looking for you because you didn't come home last night."
    yui "We tried to contact you, but you didn't pick up your phone or answer our messages."
    $ phone_alert = True
    $ newmessage = True
    $ ch2ep2rinmessage = True
    $ rin_messages_show = True
    $ rin_newmessage = True
    $ ch2ep2yuimessage = True
    $ yui_messages_show = True
    $ yui_newmessage = True
    $ ch2ep2zekemessage = True
    $ zeke_messages_show = True
    $ zeke_newmessage = True
    if krystal_contact == True:
        $ ch2ep2krystalmessage = True
        $ krystal_messages_show = True
        $ krystal_newmessage = True
    scene ch2ep2_266 with dissolve
    mc "Oh... Yeah, you're right."
    if krystal_contact == True:
        u "[rin], [yui], [zeke], [krystal]. I've got new messages from all of them."
    else:
        u "[rin], [yui], [zeke]. I've got new messages from all of them."
    mc "My bad. I didn't check my phone until now."
    scene ch2ep2_265 with dissolve
    yui "*Sighs* It's alright, but next time if you are going to stay out overnight, please tell everyone first, okay?"
    mc "... Okay. I get it."
    yui "By the way, why were you with that woman earlier? Did you come to work together?"
    mc "You mean [faye]?"
    yui "So, that was her? I've never met her in person before."
    mc "... Well, something bad happened to her yesterday, so I decided to stay overnight at her house."
    yui "I see..."
    scene ch2ep2_267 with dissolve
    yui "Alright, let's get inside then. It's almost time to work."
    yui "Oh! And don't forget to answer everyone's messages. They are worried about you."
    mc "Sure. You go in first. I'll answer them before going in."
    yui "Alright, if you say so."
    jump ch2ep2pt3atwork
label ch2ep2pt3atwork:
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    if ch2ep2visitsally1 == 1:
        scene black with dissolve
        $ renpy.pause()
        s "*An hour later*..........."
        scene ch2ep2_268 with dissolve
        u "......................"
        u "... To think about it, I haven't had any coffee yet for today."
        u "My head isn't working as it should be."
        u "Maybe I should go get one real quick..."
        scene ch2ep2_268_a1 with dissolve
        sally "{b}Good morning, everyone!!{/b}"
        sally "*Giggles* It's been a while since the last time I came here."
        sally "*Giggles* Did you guys miss me?"
        liam "Hello, [sally]."
        david "It's really been a while like you said. Good morning, [sally]."
        joe "I don't know about anyone else, but I miss you a lot!"
        david "I think we all do. We really miss the energy you always bring with you when coming here."
        sally "*Giggles* Thanks! I'm glad to hear that!"
        sally "Talking about energy... guess what?"
        scene ch2ep2_268_a2 with dissolve
        sally "Tada~! I've brought cups of coffee for you guys!"
        joe "Damn... I was actually a bit sleepy. You're absolutely my lifesaver."
        liam "Thanks a lot, [sally]. But, you really don't have to..."
        sally "It's alright. I'm in a good mood today, so it's not a big deal!"
        liam "That's very kind of you."
        liam "Alright, guys, don't leave her hanging. Go grab yourself a cup of coffee."
        sally "No. No. No. Wait for me at your seats, I'm going to give it to you one by one."
        liam "... Okay, sure. Whatever you say."
        scene black with dissolve
        scene ch2ep2_268_a3 with dissolve
        sally "Okay... Here you go."
        leo "Thank you so much, [sally]."
        leo "I owe you one. Let me buy you a meal next time."
        sally "*Giggles* Thanks, but you don't have to!"
        leo "... Okay, then."
        scene black with dissolve
        scene ch2ep2_268_a4 with dissolve
        sally "And this one is for you."
        yui "Thank you, [sally]. I really appreciate your kindness."
        sally "*Giggles* You're welcome!"
        sally "Oh! By the way, this is our first time talking together, right?"
        yui "To think about it... Yeah, It seems like that."
        sally "You are... [yui], right?"
        yui "Yes, I am."
        scene ch2ep2_268_a5 with dissolve
        sally "*Giggles* It might be a little bit late to say this, but nice to meet you, [yui]!"
        yui "*Smiles* Nice to meet you, too!"
        sally "Alright, I won't bother you anymore. Let's talk again soon!"
        yui "Yeah, sure!"
        scene black with dissolve
        scene ch2ep2_268_a6 with dissolve
        sally "Now, it's your turn, [liam]."
        liam "Cheers. I'll buy you one next time."
        sally "*Giggles* You sure?"
        liam "Yeah, but you'll need to remind me if I forget to, okay?"
        sally "*Giggles* Alright, deal!"
        scene black with dissolve
        scene ch2ep2_268_a7 with dissolve
        u "Hm? She's looking at me now."
        u "I guess it's my turn then...."
        sally ".................."
        scene ch2ep2_268_a8 with dissolve
        u "...................."
        u "Hm? Did she just ignore me like that?"
        u "Could it be that she didn't buy one for me?"
        u "*Sighs* Well, that could be the case. Let's just get back to work then."
        scene black with dissolve
        scene ch2ep2_268_a9 with dissolve
        sally "Take it, [joe]."
        joe "Thanks a bunch!"
        joe "I'm so sleepy now. I hope it helps."
        sally "*Giggles* I hope so!"
        scene black with dissolve
        scene ch2ep2_268_a10 with dissolve
        sally "This one is for you, [david]!"
        david "Cheers! I'm sorry that I don't have anything to give you in return."
        sally "*Giggles* No worries! I just want to make you guys happy. That's all!"
        sally "I didn't expect to get anything back in return in the first place!"
        david "I see... I wish you a good day then!"
        sally "*Giggles* Thanks! You, too!"
        scene black with dissolve
        scene ch2ep2_268_a11 with dissolve
        u "...................."
        sally "...................."
        scene ch2ep2_268_a12 with dissolve
        sally "*Poking*............"
        u ".... Hm?"
        scene ch2ep2_268_a13 with dissolve
        sally "*Giggles* Hehe... Take this."
        mc "Oh...?"
        sally "Hm? What's wrong? What are you waiting for?"
        mc "Is it mine? I thought you didn't buy one for me."
        sally "Hm? What made you think that?"
        scene ch2ep2_268_a14 with dissolve
        mc "Because you ignored me earlier...."
        sally "*Giggles* What? I didn't mean ignore you."
        sally "It's just because I wanted you to be the last person."
        mc "....................."
        sally "Come on! Take it!"
        mc "Okay..."
        scene black with dissolve
        scene ch2ep2_268_a15 with dissolve
        mc "Thank you for the coffee, [sally]."
        sally "No worries!"
        mc "I was about to go buy one just before you came."
        sally "*Giggles* Really?! Well then, I'm happy I could help you save your time!"
        scene ch2ep2_268_a16 with dissolve
        sally "Oh! I almost forgot this."
        sally "Here is your cookie. Take it."
        mc "Hm? You bought a cookie for everyone, too? I didn't see you giving it to them."
        sally "*Giggles* No, this is especially for you."
        mc "Really? For what?"
        scene ch2ep2_268_a17 with dissolve
        sally "*Winks* For paying me a visit a couple days ago!"
        mc "I see..."
        sally "Take it as a thank-you gift for showing that you worried about me."
        mc "Okay then, I'll take it. Thank you."
        sally "*Giggles* My pleasure...."
        scene black with dissolve
        $ renpy.pause()
        scene ch2ep2_268_a18 with dissolve
        sally "Alright, guys. I'm leaving now."
        sally "Enjoy your coffee! Have a great workday, everyone!"
        liam "You, too. Have a great working day, [sally]."
        joe "Thanks for the coffee! I'm much better now!"
        david "See you later, [sally]."
        scene black with dissolve
        $ ch2ep2sallycoffee = 1
        $ renpy.pause()
        jump ch2ep2pt3lunch
    else:
        scene black with dissolve
        $ renpy.pause()
        jump ch2ep2pt3lunch
label ch2ep2pt3lunch:
    scene black with dissolve
    s "*A couple hours later*.........."
    scene ch2ep2_269 with dissolve
    u "... Alright, it's time for lunch now. Let's go find something to eat."
    if ch2ep2alicemessage == True:
        $ renpy.sound.play("sfx/phone vibrating.mp3")
        s "*Phone vibrates*.........."
        u "Hm....?"
        jump ch2ep2talkwithalice
    else:
        scene black with dissolve
        s "You went outside of the company to have lunch, and got back by 1 p.m."
        jump ch2ep2meetmaya
label ch2ep2talkwithalice:
    scene ch2ep2_269_a1 with dissolve
    u "Oh, it's [alice] calling."
    u "It must be about the job we talked about yesterday."
    u "Let's pick up the call and hear her answer."
    stop sound
    scene ch2ep2_269_a2 with dissolve
    mc "Hello...."
    mc "I'm good. What about you?"
    mc "... Yeah, I'm free right now. It's lunch break."
    mc "Where do you want us to meet?"
    mc "Okay, got it."
    scene ch2ep2_269_a3 with dissolve
    u "Alright, off to meet [alice]."
    u "She said that she wanted to give me an answer in person."
    u "According to Google Maps, I can get there in 15 minutes walking."
    u "But, I want to get there as fast as possible, so I'll hurry."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_269_a4 with fade
    u "...................."
    u "... Alright, I've arrived."
    u "Umm.... It should be somewhere around here."
    scene ch2ep2_269_a5 with dissolve
    u "The GPS is showing that the destination is on the right..."
    u "Is it that building? Let's go check it out."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_269_a6 with dissolve
    cg "Welcome to our restaurant, sir!"
    unknown "Oh! There you are!"
    u "Hm...?"
    scene ch2ep2_269_a7 with dissolve
    alice "Here! I'm right here!"
    mc "Oh..."
    scene ch2ep2_269_a8 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_269_a8.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_269_a8_blink.jpg", 1) with dissolve
    alice "*Hi, [mc]!"
    mc "Hi. Sorry to keep you waiting."
    alice "*Smiles* Aye! No need to say that!"
    alice "It wasn't that long. I just arrived here a few minutes before you."
    mc "I see...."
    menu:
        "Compliment her [alice1]":
            $ ch2ep2complimentalice = 1
            $ alice_ch2_ep2 += 1
            $ alice_relationship += 1
            scene ch2ep2_269_a9 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_269_a9.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_269_a9_blink.jpg", 1) with dissolve
            mc ".... You look good today."
            alice "*Smiles* Heh?! Really?!"
            mc "Yes...."
            alice "*Giggles* Hehe... To be honest, I didn't expect you to say that, but thanks for such a compliment!"
            mc "Your outfit suits you well. Why have I never seen you wear it before?"
            alice "*Smiles* Seems like I made the right choice. I'm glad that you like it. I just bought it last week."
            mc "I see..."
        "Say nothing":
            $ ch2ep2complimentalice = 2
            scene black with dissolve
    scene ch2ep2_269_a10 with dissolve
    alice "Alright, let's just sit down before we continue talking!"
    alice "I'm so hungry now."
    mc "Oh, okay."
    scene ch2ep2_269_a11 with dissolve
    mc "So, are you allowed to compose some music for our company?"
    mc "What did your company say?"
    alice "*Giggles* Relax. We've just met. Why so hasty?"
    alice "Can't we just finish our lunch first before talking about it?"
    mc "....................."
    alice "*Sighs*............"
    scene ch2ep2_269_a12 with dissolve
    alice "Alright, since you're so eager to hear my answer, I'll tell you now."
    alice "Yes, my company gave me permission to compose music for your company."
    mc "That's great."
    alice "Can you tell me the process again?"
    scene ch2ep2_269_a11 with dissolve
    mc "Sure. The project manager, [faye], has been looking for a new composer because the one we had been working with had a serious car accident."
    alice "Oh... I'm sorry to hear that. Is he alright?"
    mc "From what I heard... he's still alive, but the doctor isn't sure if he will wake up again."
    alice "Aw... It must've been a very serious accident."
    mc "Yeah... When I heard that, I mentioned your name to her, but she said that she needed to see your skills first."
    scene ch2ep2_269_a12 with dissolve
    alice "I see... So, I'll have to go see her, right?"
    mc "Yeah, I think so."
    alice "Alright, that's fine."
    scene ch2ep2_269_a13 with dissolve
    cg "Sorry to keep you waiting. Here is a menu."
    alice "O-Oh! Thank you."
    scene ch2ep2_269_a14 with dissolve
    alice "Um... I'd like to have an order of barbecue chicken wings, please."
    cg "Sure. One BBQ chicken wings. Anything else?"
    alice "Let me see.... I'd like to have sweet potato and...  a lemonade, please."
    cg "I get it. One dish of sweet potato, and one lemonade..."
    scene ch2ep2_269_a15 with dissolve
    alice "Alright, that's all for my order."
    alice "It's your turn now, [mc]. Here. Take the menu."
    mc "Thank you."
    if ep4gowithgirls == 1:
        scene ch2ep2_269_a16_a1 with dissolve
        cg "*Smiles* We meet again, sir. It's been a while."
        cg "How are you doing? Also, what about her? How is she doing?"
        u "Hm...?"
        scene ch2ep2_269_a16_a2 with dissolve
        mc "...................."
        mc ".... Excuse me, but do I know you?"
        cg "Hmm...? Am I mistaking you for someone else...?"
        scene ch2ep2_269_a16_a3 with dissolve
        cg "No, I'm not! I'm pretty sure it was you! I'm quite good at remembering people."
        cg "I work at Burger Queen. We met there last time. Did you already forget?"
        cg "You know... the day that you went there with [krystal]!"
        mc "Oh... I remember you now. I'm sorry."
        cg "*Giggles* No worries. I understand you."
        cg "I'm just a normal part-time worker. There is nothing special about me."
        cg "So, it's not your fault that you didn't remember me."
        scene ch2ep2_269_a16_a4 with dissolve
        cg "By the way, may I ask you a question?"
        mc "Sure. Go ahead."
        cg "How is [krystal]? Is she doing alright?"
        cg "Even though it's already been a while, I'm still worried about her."
        mc "Yes, she's doing very good right now. Don't worry about her."
        cg "Really...?"
        mc "Yeah...."
        cg "*Giggles* Thanks! That's all I wanted to hear!"
        cg "Sorry for taking your time. Please continue ordering now!"
        mc "Okay...."
    scene ch2ep2_269_a17 with dissolve
    mc "I'd like to have pork lasagna, and creamy garlic shrimp pasta, please."
    cg "One pork lasagna... and one creamy garlic shrimp pasta. Is that correct?"
    mc "Yes, it is."
    scene ch2ep2_269_a18 with dissolve
    cg "Your food should be done in around 15 minutes."
    cg "I'll bring it right out when it's ready."
    alice "We get it. Thank you so much."
    if ep4gowithgirls == 1:
        scene ch2ep2_269_a19_a1 with dissolve
        alice "................."
        u "... Hm? Why is she looking at me like that?"
        alice "... [krystal], huh? Who is she?"
        alice "I've never heard you mention her before."
        scene ch2ep2_269_a19_a2 with dissolve
        mc "...................."
        mc "She's another housemate."
        alice "Is that so?"
        mc "... Yeah."
        alice "How many housemates do you have actually?"
        mc "Four. [zeke], [rin], [yui], and [krystal]."
        alice "Oh, [rin], I remember her."
        scene ch2ep2_269_a19_a3 with dissolve
        alice "*Sighs* Judging from their names, there are three girls living in the same house with you...."
        mc "... Actually, there are four."
        alice "Jeez... That's not good news for me. Why is that?"
        mc "It's [zeke]'s girlfriend, [mika]. She's been living with us for a while now."
        alice "I see...."
    scene black with dissolve
    $ renpy.pause()
    s "*Fifteen minutes later*......"
    scene ch2ep2_269_a20 with dissolve
    cg "Sorry to keep you waiting...."
    cg "Here is your order of barbecue chicken wings, and your sweet potato."
    cg "But, we had a little bit problem with your lemonade."
    alice "Hm? What's wrong?"
    cg "We ran out of lemon, but don't worry. An employee went to buy some at a nearby market and he is on the way back."
    cg "So, you might have to wait a little longer for that."
    cg "We're so sorry for causing you such an inconvenience."
    alice "I see... It's alright. I can wait."
    cg "Thank you for your understanding."
    cg "And you, sir. Please, wait a sec. I'll bring your food right out."
    mc "Thank you."
    scene black with dissolve
    s "*About half an hour later*........"
    scene ch2ep2_269_a21 with dissolve
    mc "Alright, now that we've finished, Let's leave."
    alice "*Smiles* Okay!"
    cg "Thank you for having lunch at our restaurant! Please come back again soon!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_269_a22 with dissolve
    mc "... Alright. Let's go."
    alice "Hm? To where?"
    mc "To my company. You need to come meet [faye]. Did you already forget?"
    alice "No, I didn't! But, not today. I'm busy this afternoon."
    mc "I see..."
    scene ch2ep2_269_a23 with dissolve
    mc "Then, when will you be able to go meet her?"
    alice "I'll clear up my responsibilities, and go meet her tomorrow morning."
    mc "Tomorrow morning?"
    alice "Yes, why?"
    mc "Nothing. I was just making sure I heard it correctly."
    scene ch2ep2_269_a24 with dissolve
    mc "Hand me your phone then."
    alice "Hm? Why do you need my phone?"
    mc "I've already done my part. It's not up to me now."
    mc "I'm going to give you [faye]'s phone number so that you guys can talk and plan for tomorrow directly."
    alice "I see..."
    scene ch2ep2_269_a25 with dissolve
    alice "Alright then, here you go."
    mc "Thanks..."
    alice "The password is 210917."
    mc "Okay."
    scene ch2ep2_269_a26 with dissolve
    mc ".... Hm?"
    alice "Hm? What's wrong?"
    scene ch2ep2_269_a27 with dissolve
    u "When did she take this picture?"
    alice "... [mc]?"
    mc "Nothing.... What's the password again?"
    alice "*Smiles* Two-one-o-nine-one-seven. It's the day I first met you!"
    mc "... Really?"
    alice "*Giggles* Hehehe... Yeah!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_269_a28 with dissolve
    mc "Okay. Done. Here you go."
    alice "Thank you."
    mc "I suggest you call her as soon as you can."
    mc "She's pretty busy. I'm not sure if she will be free tomorrow morning."
    alice "Got it!"
    scene ch2ep2_269_a29 with dissolve
    mc "Good luck. I hope you meet her expectation."
    alice "Thanks! I will try my best!"
    mc "You're welcome."
    mc "Alright, I think I should leave now."
    alice "Me, too. See you later then!"
    mc "Yeah, see you later."
    scene ch2ep2_269_a30 with dissolve
    alice "Goobye, [mc]!"
    mc "See you tomorrow, [alice]."
    alice "*Smiles* Hope so!"
    $ ch2ep2meetalice = 1
    $ alice_relationship += 2
    $ alice_ch2_ep2 += 2
    jump ch2ep2meetmaya
label ch2ep2meetmaya:
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep.3/ep3_9.mp3" fadein 3.0
    $ bgm = "Atch - Freedom"
    scene ch2ep2_270 with fade
    s "*Elevator sounds*............"
    u "Alright, I'm back...."
    u "Let's go in and get to work."
    if ch2ep2meetalice == 1:
        scene ch2ep2_270_a1 with dissolve
        u "Ah... I almost forgot."
        u "I should at least call [faye] to tell her about [alice]."
        u "Let's call her now..."
        scene ch2ep2_270_a2 with dissolve
        u "...................."
        u "... Why isn't she answering? Could it be that she is busy right now?"
        u "Maybe I should call her lat... Hm?"
        mc "Hello, [faye]. Are you busy right now?"
        scene black with dissolve
        scene ch2ep2_270_a3 with fade
        faye "No, [mc]. I'm not busy right now."
        faye "... Hm? Oh, I was picking up my earpod, that's why it took me so long to answer."
        faye "I'm driving right now. I'm on the way to meet a new composer."
        faye "Hm? [alice]? Yeah. I remember her. Why?"
        faye "Really? That's such very good news to hear!"
        scene ch2ep2_270_a4 with dissolve
        faye "Hm? No, he isn't officially our new composer, but he's pretty skilled."
        faye "Therefore, I'm going to talk to him and see if he's interested in working with us."
        faye "I can't just rely on you, right? It's not your job after all. I've got to fix my problems myself, as well."
        faye "Don't worry. Even though the composer I'm going to meet is interested in working with us, he'll also have to show his skills first, too."
        faye "And if your friend is better than him, I'll definitely make her our partner. You have my promise."
        faye "Alright, I see. Goodbye, [mc]."
        scene black with dissolve
        scene ch2ep2_270_a5 with fade
        u "Alright, I've done my part. There is nothing more I can do."
        u "Now, it's all up to [faye] to eventually make a decision."
        u "Let's get in the department...."
    unknown "[mc]...!!"
    scene ch2ep2_271 with dissolve
    u "Hm...?"
    pete "Come over here!"
    u "Oh, it's [pete]...."
    u "Well, I wonder what he wants from me."
    scene ch2ep2_272 with dissolve
    mc "Good afternoon, [pete]."
    pete "Good afternoon, [mc]. Did you enjoy your lunch?"
    mc "Yes, I did."
    pete "That's good..."
    mc "What about you?"
    pete "Hm? Oh, I haven't had lunch yet. But, I'm going to have it soon!"
    mc "I see... By the way, is there something you wanted?"
    scene ch2ep2_273 with dissolve
    pete "I just called you here to tell you that there is someone waiting to meet you."
    pete "She's waiting for you inside my office."
    u "Hm? This woman...."
    u "I can't tell who she is now because I can only see a little bit of her back from here, but it feels so familiar."
    mc "I see..."
    pete "Let's go on in! Don't make her wait too long for you!"
    mc "Alright, I get it."
    scene black with dissolve
    s "*Door opens*......."
    scene ch2ep2_274 with dissolve
    pete "I've brought you the man, ma'am."
    u "Oh... I remember her now. I met her at [rowan]'s house."
    u "I wonder why she wants to meet me and what she wants from me."
    maya "*Smiles* Thank you. I appreciate your help."
    pete "Anytime! Alright, I have to go to lunch now. Take your time."
    maya "*Smiles* Enjoy your lunch, [pete]."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_275 with dissolve
    maya "*Smiles* Hello, [mc]."
    mc "Good afternoon, ma'am."
    maya "*Sighs* Jeez... You guys didn't listen to me at all, did you?"
    maya "I told you to just call me by my name, didn't I?"
    mc "... I'm sorry."
    maya "*Smiles* Forget it. Come here. Take your seat."
    mc "Okay...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_276 with dissolve
    mc "...................."
    maya "*Smiles* ..................."
    u "... What's going on? It's been about a minute now since I took a seat, yet she hasn't said a single word, but just smiles at me."
    u "Perhaps I should be the one to start a conversation..."
    scene ch2ep2_277 with dissolve
    mc "... Have you had lunch?"
    maya "Hm...? Oh! Yes, I have. What about you?"
    mc "Me, too."
    maya "*Smiles* That's great..."
    scene ch2ep2_278 with dissolve
    mc "[pete] told me that you were looking for me..."
    maya "H-Hm...? Oh, yeah. You're right. I was looking for you."
    mc "Yes, I know that...."
    mc "So... Is there something that you want from me?"
    maya "I....."
    maya "(*Sighs*... I thought it would be easy, but I was obviously wrong....)"
    maya "(I can't just tell him that he is....)"
    maya "(*Sighs* What should I do now?)"
    scene ch2ep2_279 with dissolve
    mc "Are you okay, [maya]? You look uncomfortable...."
    maya "Hm? Do I?"
    mc "Yeah...."
    maya "*Smiles* I-I'm fine! Don't worry about me."
    mc "I see..."
    maya "What made you think that I wasn't okay?"
    mc "Your face.... Your mouth is smiling, but your eyes..."
    scene ch2ep2_280 with dissolve
    maya "*Giggles* Is that so? I never knew that!"
    mc "...................."
    maya "*Giggles* I'm good. Really. There's no need for you to worry about me."
    scene ch2ep2_281 with dissolve
    mc "Alright then. If you say so..."
    maya "*Smiles* But, thanks for worrying. I appreciate it."
    mc "So, can you tell me now why you were looking for me?"
    scene ch2ep2_282 with dissolve
    maya "Well... I'm here to invite you for dinner at my house."
    maya "(Phew.... That sounds like a good beginning. Start with something casual first...)"
    mc "Hm? You want me to go have dinner with you?"
    maya "Yeah. You heard it right. I want you to come and have dinner with me and my daughter."
    scene ch2ep2_283 with dissolve
    mc "But, why...? I'm just a normal employee."
    mc "(... Isn't it kind of weird for someone in your position to invite someone like me for a dinner? Especially at your house...)"
    mc "(What are you actually looking to do....?)"
    maya "Why not? [rowan] said you had a lot of potential, so I want to get to know you better."
    maya "I'm busy this evening, so it can't be today. How about tomorrow?"
    mc "......................"
    mc "(I'll just go with the flow. I shouldn't turn her down and piss her off.)"
    mc "(At least it's better to waste some time than to act suspicious.)"
    scene ch2ep2_284 with dissolve
    mc "Okay. I get it...."
    maya "*Smiles* Lovely! I'm really looking forward to tomorrow!"
    mc "Me, too..."
    maya "Wait for me after work in front of the company, okay? I'll pick you up and take you to my house."
    mc "Actually, you don't have to. You can just send me the location."
    maya "Yes, I do. It's not a big deal. I want to pick you up myself."
    mc "Okay, if you say so. Thank you so much for your kindness...."
    maya "*Smiles* Anytime...!"
    scene black with dissolve
    s "*A few minutes later*........"
    scene ch2ep2_285 with dissolve
    mc ".................."
    maya "*Smiles* Hehe....."
    u "Well, the conversation ended just like that...."
    u "She's been in her own world for a few minutes now."
    u "Well, I guess there is nothing for me to do here anymore..."
    scene ch2ep2_286 with dissolve
    mc "Excuse me, [maya]..."
    maya "Hm? Yes?"
    mc "I'm afraid that I'm going to have to leave now."
    scene ch2ep2_287 with dissolve
    maya "Already? Why so sudden?"
    mc "You might not notice it, but it's actually a quarter past one already...."
    mc "I'm supposed to be at my workstation right now."
    maya "I see...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_288 with dissolve
    maya "Alright then! I'm won't take any more of your time!"
    u "Hm...? What is she doing? Why is she holding my hand?"
    maya "I wish you good luck with your work, [mc]."
    maya "And if there is anything that you need my help with, don't hesitate to ask me, okay?"
    scene ch2ep2_289 with dissolve
    mc "Thank you so much. I appreciate your kindness."
    maya "Anytime! Alright, I shouldn't hold you here any longer."
    maya "I'm leaving, too. Let's go."
    mc "Okay, sure."
    scene black with dissolve
    scene ch2ep2_290 with dissolve
    mc "Let me walk you to the elevator...."
    maya "*Smiles* Thanks, but I'm good. You don't need to do that."
    mc "Are you sure?"
    maya "Yes, I am. Don't worry about me. Didn't you say that you were supposed to be working now?"
    maya "You should hurry up and get inside your department then. I'll see you tomorrow."
    mc "Okay then, see you tomorrow."
    scene black with dissolve
    scene ch2ep2_291 with dissolve
    u "..................."
    scene ch2ep2_292 with dissolve
    u "... Okay. She's left."
    u "Let's get ins-"
    scene ch2ep2_288 with flash
    scene ch2ep2_293 with dissolve
    u "......................"
    u "... To think about it, I still don't understand why she held my hand like that..."
    u "Is she always that friendly with every employee here?"
    u ".... By the way, I know it might sound weird, but why do I feel so familiar with her touch?"
    u "Yeah... It's really weird...."
    scene ch2ep2_294 with dissolve
    u "*Sighs* Let's just forget about it. I am probably just overthinking..."
    u "It's pointless to think seriously about it."
    u "Let's just get back to work..."
    scene black with dissolve
    $ renpy.pause()
    s "*A few hours later*..........."
    scene ch2ep2_295 with dissolve
    yui "Hey, [mc]."
    mc "Hm? What's up?"
    yui "Let's go home."
    mc "Hm? Is it time already?"
    scene ch2ep2_296 with dissolve
    yui "Yeah. It's already a quarter past five actually."
    yui "Everyone else has already left."
    mc "I see... I was so focused on the work that I didn't notice."
    yui "Right? I was wondering when you were going to stop working."
    yui "So, let's leave and go home."
    mc "Yeah, sure."
    if ch2ep2sallycoffee == 1:
        jump ch2ep2_invitetomovie
    else:
        jump ch2ep2_backhome
label ch2ep2_invitetomovie:
    scene ch2ep2_297 with dissolve
    yui "Let's hurry up. [rin] and [zeke] are waiting for us."
    mc "Got it."
    unknown "... [mc]!"
    scene ch2ep2_298 with dissolve
    u "Hm...?"
    u "Did someone just call my name?"
    scene ch2ep2_299 with dissolve
    sally "[mc]!"
    u "Oh, it's [sally].... [eira] is with her, too."
    u "I wonder why they are looking for me."
    scene ch2ep2_300 with dissolve
    mc "Hi, [sally]. Good evening, [eira]."
    sally "*Smiles* Hi, [mc]."
    eira "Good evening, [mc]."
    yui "Hello, [sally]."
    scene ch2ep2_301 with dissolve
    sally "Hi, [yui]! How's your day?"
    yui "Pretty good. How about you?"
    sally "Me, too. Oh! How was the coffee by the way?"
    yui "Now that you mention it, thanks again for the coffee, [sally]. I liked it."
    sally "*Smiles* I'm glad to hear that!"
    scene ch2ep2_302 with dissolve
    sally "Oh! By the way, you guys don't know each other yet, right?"
    eira "... Yeah, you're right."
    yui "Actually, I do. You're [eira], right?"
    eira "Hm? How did you know my name?"
    scene ch2ep2_303 with dissolve
    yui "I've seen you around the company. I've also heard people saying your name."
    eira "I see..."
    eira "And you're... [yui], right?"
    yui "Yep, that's me."
    scene ch2ep2_304 with dissolve
    eira "Nice to meet you, [yui]."
    yui "*Smiles* Nice to meet you, too."
    yui "I hope we can get along with each other."
    eira "Me, too."
    scene ch2ep2_305 with dissolve
    mc "Sorry to interrupt, but [rin] and [zeke] are waiting for us."
    mc "Did you want something?"
    mc "You seemed to be looking for me?"
    sally "Well, the thing is, [eira] and I are going to a movie this evening."
    mc "And...?"
    scene ch2ep2_306 with dissolve
    sally "*Smiles* And I'm here to ask you if you want to join us!"
    eira "Come with us, [mc]. [sally] will buy your ticket."
    mc "Really? But, why?"
    sally "*Smiles* Because I'm still grateful that you were worried about me, so I'd like to do something for you in return."
    sally "We're planning to watch F9. What do you say?"
    if ch2ep2havesexwithyui == True:
        $ yui_relationship += 1
        $ yui_ch2_ep2 += 1
        scene ch2ep2_306_a1 with dissolve
        mc "..................."
        yui "Hm? Why are you looking at me like that?"
        yui "They're waiting for your answer."
        scene ch2ep2_306_a2 with dissolve
        mc "I can go with you guys, but..."
        mc "What about [yui]? Aren't you going to invite her?"
        yui "*Smiles* [mc]...."
    scene ch2ep2_307 with dissolve
    sally "Of course, I am! That's why I'm here to ask you instead of sending you a message!"
    sally "Do you want to come with us, [yui]?"
    yui "*Smiles* Of course, I do!"
    scene ch2ep2_308 with dissolve
    sally "You heard her, right?"
    mc "Yeah, loud and clear."
    sally "Now, what about you?"
    menu:
        "Okay. Let's go.\n[eira2] [sally2] [yui2]":
            $ ch2ep2movie = 1
            $ yui_ch2_ep2 += 2
            $ yui_relationship += 2
            $ eira_ch2_ep2 += 2
            $ eira_relationship += 2
            $ sally_ch2_ep2 += 2
            $ sally_relationship += 2
            scene ch2ep2_309_a1 with dissolve
            mc "Okay. I'll go with you guys."
            sally "*Smiles* Lovely! I'm glad to hear that!"
            eira "Me, too..."
            sally "Alright, let's go then!"
            mc "Wait a sec..."
            sally "Hm...?"
            scene ch2ep2_309_a2 with dissolve
            mc "What about [rin]? We can't just leave her like this, right?"
            mc "I think we should ask her if she also wants to come with us."
            sally "Oh yeah, you can invite her if you want. I don't mind that."
            yui "Alright then, let me call her real quick."
            scene black with dissolve
            $ renpy.pause()
            s "*A few seconds later*........."
            scene ch2ep2_309_a3 with dissolve
            yui "Alright, I've asked her."
            sally "Then, what did she say?"
            yui "She said yes. She'll be waiting in the parking lot."
            sally "*Smiles* Lovely! Let's go meet her then!"
            jump ch2ep2_watchmovie
        "I'm not interested":
            $ ch2ep2movie = 2
            scene ch2ep2_309_d1 with dissolve
            mc "... I'm sorry, but I'm not interested in F&F."
            yui "What? Are you for real? F&F is a pretty good movie!"
            scene ch2ep2_309_d2 with dissolve
            mc "... Is it?"
            yui "Yeah! Everything in the movie is so perfect. I'm a big fan of F&F!"
            mc "I don't know... I don't feel it that way. Maybe it's because I don't have a family."
            yui "....................."
            mc "You can go with them if you want."
            scene ch2ep2_309_d3 with dissolve
            sally "Look. We can watch something else if that's what you want."
            mc "I appreciate your kindness, but please don't."
            mc "You want to watch F9. I don't want you to just change your plans because I don't want to watch it."
            sally "Come on..."
            mc "I'm sorry..."
            scene ch2ep2_309_d4 with dissolve
            mc "... Alright, I'm leaving now. Enjoy your movie."
            yui "...................."
            sally ".................."
            eira "Aw...."
            scene black with dissolve
            $ renpy.pause()
            s "*Later that night*.........."
            jump ch2ep2_backhome
label ch2ep2_watchmovie:
    scene black with dissolve
    $ renpy.pause()
    stop music fadeout 3.0
    scene ch2ep2_310 with dissolve
    play music "sfx/ep.3/ep3_13.mp3" fadein 3.0
    $ bgm = "Roa Music - Freedom"
    yui "Alright, there she is..."
    yui "Hm? But why is she alone? Where's [zeke]?"
    mc "There is only one way to find out. Let's go ask her."
    yui "Yeah, you're right."
    scene ch2ep2_311 with dissolve
    yui "Hey. Sorry to keep you waiting."
    rin "It's alright. There is nothing to be sorry about."
    yui "Where's [zeke] by the way? Why are you alone?"
    rin "Oh, [zeke]... He already left."
    yui "Hm? I thought he would join us."
    rin "He said he'd love to, but he already has plans with [mika]."
    yui "I see..."
    scene ch2ep2_312 with dissolve
    sally "*Smiles* Long time no see, [rin]!"
    rin "*Smiles* Yeah, it's been a while, [sally]."
    eira "Good evening, [rin]."
    rin "*Smiles* Good evening, [eira]."
    scene ch2ep2_313 with dissolve
    sally "Looks like everyone is ready. Shall we go?"
    rin "Yeah, sure."
    sally "Alright, hop in the car then!"
    scene black with dissolve
    $ renpy.pause()
    s "*Half an hour later*........."
    scene ch2ep2_314 with fade
    sally "*Sighs* Finally, here we are."
    sally "Rush hour traffic is no joke..."
    eira "I couldn't agree more..."
    sally "Okay, the theatre is upstairs. Let's go."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_315 with dissolve
    sally "Alright, guys..."
    sally "I know that [eira] and I planned to watch F9, but I've been thinking about it on the way here."
    sally "Since you guys are here with us, it isn't about only two of us now."
    sally "I should ask for your opinions, too. Is there a particular movie that you guys really want to watch?"
    sally "If there is, don't hesitate to speak up so that we can talk it over."
    scene ch2ep2_316 with dissolve
    sally "What do you say, [rin]?"
    rin "Hm? Me?"
    sally "Yeah, let's start with you."
    rin "Okay then. For me, I don't have any movie I particularly want to watch."
    rin "I can watch anything. If most of you want to watch F9, then F9 it is!"
    scene ch2ep2_317 with dissolve
    sally "What about you, [yui]?"
    yui "Of course, it's F9! I'm a big fan of F&F!"
    sally "*Smiles* Really?! Me, too!"
    sally "Alright, [mc]. What do you say?"
    mc "Since three of you have chosen F9 already, let's just watch it then."
    scene ch2ep2_315 with dissolve
    sally "Alright then, [eira] and I are going to buy tickets for you guys."
    sally "It's pretty crowded right in front of the box office, you guys better wait here."
    rin "Sure. No problem."
    scene ch2ep2_318 with dissolve
    sally "Okay guys, I've got all the tickets."
    sally "There were a lot of people buying tickets. Fortunately, I've got you guys good seats."
    rin "*Giggles* Well done, [sally]."
    yui "When is the show time?"
    sally "Half-past six."
    rin "Now, it's a quarter of. Shall we go do something else while we wait?"
    sally "Yeah, sure!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_319 with dissolve
    rin "To think about it, it's really been quite a while since the last time we hung out together, [sally]."
    sally "*Giggles* I know, right?"
    rin "How've you been recently?"
    sally "I've been great. What about you?"
    rin "I've been through some rough times, but everything's been good for me mostly."
    sally "I see...."
    scene ch2ep2_320 with dissolve
    sally "Heh...?"
    rin "Hm? What's wrong, [sally]?"
    scene ch2ep2_321 with dissolve
    sally "Guys, look! That's an arcade over there!"
    rin "Hm? Is it always there? I didn't notice it when we were here last time."
    sally "Right? I didn't see it either. I bet they've probably just built it."
    sally "Let's get inside! We can kill time in there until the movie!"
    yui "That's a pretty good idea!"
    rin "I have no problem with that."
    scene ch2ep2_322 with dissolve
    sally "What about you, [eira]?"
    eira "At first I was going to suggest we have dinner..."
    eira "But, as I think about it carefully, forty minutes is too hasty for a dinner."
    eira "So, if you want us to kill time in there, I'm okay with that."
    sally "What about you, [mc]?"
    mc "I have no problem with that either."
    sally "Perfect! Let's go then!"
    scene black with dissolve
    scene ch2ep2_323 with dissolve
    sally "Wow! This place is pretty cool!"
    sally "Hey, look! It's Top Gun! I'm not mistaken, right?"
    rin "*Giggles* No, you aren't."
    sally "This reminds me of the old days. I remember playing that when I was young. It was so classic."
    rin "*Giggles* Me, too. Do you want to play?"
    sally "Of course! You don't even need to ask me that!"
    yui "Let's go have a look over there, [eira]."
    eira "Yeah, sure."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_324 with dissolve
    u "... Everyone seems to be having a good time here."
    u "[rin] and [sally] are playing Top Gun while [eira] and [yui] are doing something together right now."
    mc "....................."
    menu:
        "Join [rin] and [sally]":
            scene black with dissolve
            jump ch2ep2_rinandsally
        "Join [eira] and [yui]":
            scene black with dissolve
            jump ch2ep2_eiraandyui
label ch2ep2_rinandsally:
    scene ch2ep2_335 with dissolve
    sally "That's right, [rin]! Shoot them!"
    rin "O-Okay, I get it!"
    u "Well, looks like they're having a great time..."
    scene ch2ep2_336 with dissolve
    sally "Yes! That's what I'm talking about!"
    sally "Good job, [rin]! You played really well!"
    rin "*Giggles* Aw... Thanks, but actually it was you carrying me all the way."
    sally "*Laughs* Really? I didn't notice th-!"
    scene ch2ep2_337 with dissolve
    sally "-Oh?!"
    sally "What's up, [mc]!"
    rin "... Hm?"
    scene ch2ep2_338 with dissolve
    rin "Hey, [mc]. How long since you've been behind us?"
    rin "I didn't notice you at all."
    mc "I'm not surprised to hear that. You were so focused on the game."
    mc "Plus, I only got here a few seconds before you guys won."
    rin "I see... By the way, do you want to play? You can take my spot if you want."
    mc "Thanks, but I'm good. You can keep playing if you want."
    rin "It's alright, [mc]. Actually, I prefer to watch you team up with [sally] and play."
    sally "That sounds like a good idea for me!"
    mc "But, I don't know how to play this..."
    sally "Don't worry. I'll teach you while playing!"
    rin "There you go. You heard her, right?"
    mc "... Fine. Let's give it a try."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_339 with dissolve
    sally "Listen. The gameplay is very simple, [mc]."
    sally "All you have to do is shoot all the enemies you see."
    mc "... That's it?"
    sally "Actually... There is a little bit more, but you can just leave it to me!"
    mc "Alright then...."
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*........"
    scene ch2ep2_340 with dissolve
    sally "*Smiles* Perfect! We won! Well done, [mc]!"
    mc "Thanks...."
    rin "*Smiles* I knew it. I'm not surprised at all."
    rin "I had a feeling that both of you were going to dominate the game."
    scene ch2ep2_341 with dissolve
    mc "... Really? What made you think that?"
    rin "Well, it's pretty simple...."
    rin "Even someone who isn't quite good at gaming, like me, was able to play it well. So, why can't you?"
    mc "... Don't say that. I'm not much better at gaming than you, [rin]."
    sally "*Giggles* Hehe... I can confirm that!"
    mc "Thanks, [sally]...."
    $ ch2ep2rinsally = 1
    if ch2ep2yuieira == 1:
        jump ch2ep2_watchmovie2
    else:
        mc "Alright, you can have your spot back."
        rin "Hm? Why? You can keep playing if you want. I don't mind that."
        mc "No, thanks. I'm going to have a look at what [eira] and [yui] are playing."
        rin "Okay then!"
        scene black with dissolve
        $ renpy.pause()
        jump ch2ep2_eiraandyui
label ch2ep2_eiraandyui:
    scene ch2ep2_325 with dissolve
    mc "Hey..."
    eira "Hm? Oh, it's you. Hey."
    mc "What are you guys playing?"
    eira "It's called Heart Catch. Have you ever heard of it?"
    mc "No, I haven't..."
    scene ch2ep2_326 with dissolve
    eira "No doubt. I never heard of it until now either."
    eira "But, I think it looks pretty fun."
    eira "I can tell by look at how [yui] is enjoying playing it right now."
    mc "I see...."
    scene ch2ep2_327 with dissolve
    yui "{b}OH MY GOD!!{/b}"
    u "Hm...?"
    eira "Wow... [yui], you've just gotten the highest score."
    yui "Have I?! I'm not mistaken, right?!"
    eira "No, you aren't. It's literally showing on the screen."
    scene ch2ep2_328 with dissolve
    yui "You wanna try it, [eira]?"
    eira "Hm? Me?"
    yui "Yeah! Try it. It's very easy and fun to play!"
    eira "Okay then."
    scene black with dissolve
    scene ch2ep2_329 with dissolve
    yui "Yes, that's right, [eira]!"
    yui "Keep going! The highest score will soon be yours! Don't let it slip away!"
    eira "O-Okay..."
    scene black with dissolve
    scene ch2ep2_330 with dissolve
    yui "Yes! You did it!"
    mc "Congrats, [eira]."
    eira "It was a lot easier than I thought..."
    yui "See? I told you, didn't I?"
    scene ch2ep2_331 with dissolve
    yui "It's your turn now, [mc]."
    mc "Hm? Do I have to play it?"
    yui "Yeah! Why not? Are you just going to only watch us play?"
    yui "We still have half an hour left. It's better to find something to do than stand still doing nothing."
    eira "Yeah, [yui] is right, [mc]."
    mc "... Alright, then."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_332 with dissolve
    yui "Heh? You're pretty good at this, aren't you?"
    eira "If he can keep up his pace, I think he's going to beat our scores, [yui]."
    yui "Yeah, too bad. It seems that way."
    yui "But, it's good for him!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_333 with dissolve
    yui "You did it! You actually beat our scores!"
    eira "Congratulations, [mc]."
    mc "Well... it was pretty easy to play, just like you said."
    mc "And after watching you guys play it twice, I learned about it. So..."
    yui "I see.... Alright, move aside then. It's now my turn again. I'm going to try to get the highest score again."
    mc "Sure."
    $ ch2ep2yuieira = 1
    if ch2ep2rinsally == 1:
        jump ch2ep2_watchmovie2
    else:
        scene ch2ep2_334 with dissolve
        u ".... Alright, I'll just leave them alone."
        u "I wonder what [sally] and [rin] are up to."
        u "Let's go to them."
        scene black with dissolve
        $ renpy.pause()
        jump ch2ep2_rinandsally
label ch2ep2_watchmovie2:
    scene ch2ep2_342 with dissolve
    sally "Alright, everyone! It's almost time for the movie!"
    sally "We should go to the theatre and find our seats."
    rin "Let's go, [mc]."
    mc "Sure...."
    scene black with dissolve
    scene ch2ep2_343 with dissolve
    sally "By the way, should we buy some popcorn?"
    sally "We should have something to eat while watching, shouldn't we?"
    eira "It's up to you, but I'm not going to buy it."
    eira "We're going to have dinner after the movie anyway, so I don't think I should eat before the meal."
    rin "I agree with [eira] on that."
    yui "Me, too."
    sally "Alright then, I won't buy any either!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_344 with dissolve
    s "You and the girls watch the movie....."
    scene black with dissolve
    $ renpy.pause()
    s "*About two hours and a half later*.........."
    scene ch2ep2_345 with dissolve
    yui "Oh my god... It was really fun! Dom and his gang were very cool!"
    sally "I know, right! I've been waiting for it to come out, and I'm not disappointed at all!"
    rin "To be honest, I'm not a die-hard fan of F&F like you two, but I must say that I had a great time watching it."
    mc "........................"
    scene ch2ep2_346 with dissolve
    eira "[mc]...."
    mc "... Hm? Yes?"
    eira "How was the movie?"
    menu:
        "It was pretty good [eira1]":
            $ ch2ep2eiraq = 1
            $ eira_relationship += 1
            $ eira_ch2_ep2 += 1
            scene ch2ep2_347_a with dissolve
            mc "Well..."
            mc "I'm not a fan of F&F just like [rin], but it was pretty good."
            eira "Really? Do you really think that?"
            mc "Yeah...."
            eira "If you say so, I'm relieved now."
            mc "Hm? Why?"
            eira "To be honest, you look like you're a little bit bored, so I was worrying if you felt unhappy being here with us..."
            mc "... No, it's not the case. You're just overthinking it."
            eira "*Giggles* I'm glad to hear that."
        "Not bad":
            $ ch2ep2eiraq = 2
            scene ch2ep2_347_d with dissolve
            mc "Umm... Not bad."
            eira "Hm? What does that mean? You didn't find it fun to watch?"
            mc "I mean... I had no problem watching it, but I just didn't think it was that fun."
            eira "Oh. I see..."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_348 with dissolve
    sally "Alright, let's get something to eat before we leave!"
    rin "Yeah, let's go."
    scene black with dissolve
    $ renpy.pause()
    s "You spent about an hour having dinner with the girls before leaving........."
    scene ch2ep2_349 with fade
    rin "Thanks for dropping us off, [sally]."
    sally "All good. It's not a big deal!"
    sally "I had so much fun today. Let's hang out together again some time!"
    yui "Of course. Let's do it!"
    scene ch2ep2_350 with dissolve
    rin "By the way, do you guys want to come in for a bit?"
    rin "We could have some tea and talk more about the movie."
    yui "Yeah, that sounds like a good idea!"
    sally "Umm... Yeah, it sounds like a good idea, but..."
    scene ch2ep2_351 with dissolve
    sally "What do you say, [eira]?"
    eira "Hm? Why did you ask me that?"
    sally "I wanted to know your opinion."
    eira "I mean... I'd love to, but it's pretty dark already."
    eira "So, I think we better get back home before it gets any darker."
    scene ch2ep2_352 with dissolve
    sally "... Yeah, [eira]'s right."
    eira "I'm sorry...."
    rin "It's alright! Don't take it too seriously."
    rin "It isn't like today is the last day we're going to live here, is it?"
    yui "[rin]'s right. There is always another day. You can visit us whenever you want!"
    sally "Thanks... Alright, we're leaving now. Goodbye, everyone."
    rin "Goodbye. Get home safely."
    scene black with dissolve
    $ renpy.pause()
    s "*A few seconds later, after [sally] and [eira] have left*........"
    scene ch2ep2_353 with dissolve
    rin "Alright, we should also get inside as well."
    rin "It's getting chilly out here."
    mc "Yeah, you're right."
    rin "See you tomorrow, [mc]."
    yui "Good night, [mc]."
    mc "See you all tomorrow."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    jump ch2ep2_backhome
label ch2ep2_backhome:
    scene ch2ep2_354 with fade
    u "*Sighs* What a day...."
    u "Let's dry myself off, go back to my room, and find something to do before sleep."
    scene black with dissolve
    $ renpy.pause()
    if ch2ep2havesexwithyui == True:
        jump ch2ep2_yuivisitatnight
    else:
        scene ch2ep2_355 with dissolve
        s "You watch a Netflix series for a while before going to bed....."
        jump ch2ep2_mayapickup
label ch2ep2_yuivisitatnight:
    scene ch2ep2_355 with dissolve
    u "...................."
    scene ch2ep2_356 with dissolve
    u "...................."
    s "*Door knocks*............"
    scene ch2ep2_357 with dissolve
    u "Hm...?"
    unknown "[mc]. Are you awake?"
    u "That voice...."
    scene ch2ep2_358 with dissolve
    mc "[yui]...?"
    yui "Yes, it's me. Can I come in?"
    menu:
        "[smgr]Come on in":
            play music "sfx/ch2ep1_1.mp3" fadein 3.0
            $ bgm = "Roa - Winter Magic"
            $ ch2ep2letyuiin = 1
            mc "Come on in. The door isn't locked."
            scene ch2ep2_359_a1 with dissolve
            yui "*Smiles* Thanks..."
            mc "You're welcome. And please close the door for me, too. Thanks."
            yui "Yeah, sure."
            scene ch2ep2_359_a2 with dissolve
            yui "Hm? What are you watching?"
            mc "It's a series called Peaky Blinders."
            yui "Oh, I see. I've seen it on Netflix while I was trying to find something to watch."
            yui "I've never watched it. Is it fun?"
            mc "I can't tell you yet. I've never watched it either. This is the first episode."
            yui "I see...."
            scene ch2ep2_359_a3 with dissolve
            mc "By the way, what are you here for?"
            mc "Why did you bring your laptop?"
            yui "Oh, this? Don't mind it. I was doing some work."
            yui "In the middle of working, I suddenly felt like spending time with you."
            yui "So, I'm here to ask if you can let me work here."
            mc "... You want to work in here? Are you sure?"
            mc "I mean... I'm watching a series right now. Won't you be disturbed by the noise?"
            scene ch2ep2_359_a4 with dissolve
            yui "It's okay! I don't mind that!"
            mc "... Are you sure?"
            yui "Yeah! Don't worry about me. You can continue watching it."
            mc "Okay then."
            scene black with dissolve
            scene ch2ep2_359_a5 with dissolve
            yui "*Smiles* Hehe... Thanks for letting me stay here."
            mc "You're welcome."
            yui "Alright, I'm gonna start working now. Enjoy your series."
            mc "Okay, sure."
            scene ch2ep2_359_a6 with dissolve
            s "You spend time watching series while having [yui] works at your side...."
            scene black with dissolve
            $ renpy.pause()
            s "*Two hours later*........."
            scene ch2ep2_359_a7 with dissolve
            yui "Yes! Finally!"
            mc "Hm...? You're done working now?"
            scene ch2ep2_359_a8 with dissolve
            yui "*Smiles* Hehe... Yeah, I'm done now."
            mc "Good for you. Congrats."
            yui "*Giggles* Cheers!"
            scene ch2ep2_359_a9 with dissolve
            yui "*Sighs* Ahhh~! I'm so tired right now."
            yui "You don't mind me borrowing your bed for a bit, right?"
            mc "Well, what can I do? You're already on it anyway."
            yui "*Giggles* Hehehe....."
            yui "Are you about to go sleep now?"
            mc "Yeah. After I finish this episode."
            yui "Okay, I'll stay here until then."
            scene black with dissolve
            $ renpy.pause()
            s "*Ten minutes later*........."
            scene ch2ep2_359_a10 with dissolve
            mc "Alright, I'm going to sleep now."
            mc "You should get up and go back to your room, [yui]."
            yui "Hmmm~? Really? Why should I do that?"
            mc "..................."
            mc "... What did you mean?"
            scene ch2ep2_359_a11 with dissolve
            yui "I mean... Why can't I sleep here with you tonight?"
            mc ".................."
            yui "Come on~! It's not like we have never slept on the same bed together, is it?"
            yui "*Giggles* We did more than that, to be honest."
            yui "Plus, I'm way too lazy to get up and walk back to my room...."
            menu:
                "You can sleep here tonight [yui1]":
                    $ ch2ep2letyuisleep = 1
                    $ yui_relationship += 1
                    $ yui_ch2_ep2 += 1
                    scene ch2ep2_359_a12 with dissolve
                    mc "Fine. You can sleep here tonight if you want."
                    yui "*Smiles* You're the best!"
                    yui "If you don't mind, would you please put my laptop somewhere safe before you get in bed? Thanks."
                    mc "Alright...."
                    jump ch2ep2_yuih
                "I want to sleep alone tonight":
                    $ ch2ep2letyuisleep = 2
                    scene ch2ep2_359_d3 with dissolve
                    mc "Stop playing already, [yui]. It's getting late right now."
                    mc "You should really get up and go back to your room."
                    yui "Come on...."
                    mc "I'm sorry, but I want to sleep alone tonight."
                    yui "...................."
                    yui "*Sighs* Fine...."
                    scene black with dissolve
                    $ renpy.pause()
                    s "You went to bed after [yui] had left the room......"
                    jump ch2ep2_mayapickup
        "Can we talk tomorrow?":
            $ ch2ep2letyuiin = 2
            mc "I don't know what you want, but can we talk about it tomorrow?"
            mc "I'm very tired today."
            yui "Oh... Okay. Sorry for disturbing you."
            scene ch2ep2_359_d1 with dissolve
            s "You spend some time watching Netflix series before going to bed....."
            scene black with dissolve
            $ renpy.pause()
            jump ch2ep2_mayapickup
label ch2ep2_yuih:
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
    play music "sfx/ch2ep2_6.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - Sicked & Tired (ft. Lily Hain)"
    scene ch2ep2_359_a13 with dissolve
    yui "Jeez........"
    mc "...... What?"
    yui "To think about it, there are really so many girls around you..."
    yui "This isn't going to be good for me. I've got to do something now."
    scene black with dissolve
    $ renpy.pause()
    mc "Huh..?"
    scene ch2ep2_359_a14 with dissolve
    mc "What are you doing, [yui]?"
    yui "I'm going to get you addicted to me only."
    mc "Pff... Really? How?"
    yui "Just you wait...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_359_a15 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_359_a15.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_359_a15_blink.jpg", 1) with dissolve
    yui "*Giggles* Look what we've got here."
    yui "I haven't even done anything yet, so how come you are this hard?"
    mc "Believe it or not, but I don't know myself."
    yui "*Giggles* No matter how hard to try to keep that poker face, you're just a horny man. You little pervert~"
    mc "... No, I'm not."
    yui "*Giggles* Whatever you say~"
    scene ch2ep2_359_a16 with dissolve
    show ch2ep2f_yui1 with dissolve
    window hide
    yui "Alright, let's start with a little bit of warm-up...."
    $ renpy.pause()
    menu:
        "Next":
            yui "Should I move my hands a little bit faster?"
            mc "... Yes. Do it."
            hide ch2ep2f_yui1
    scene ch2ep2_359_a17 with dissolve
    show ch2ep2f_yui2 with dissolve
    window hide
    yui "How does it feel, hm?"
    mc "... You're doing good."
    $ renpy.pause()
    menu:
        "Next":
            mc "But, it will be a lot better if you do it a little bit faster."
            yui "*Giggles* You're so demanding, aren't you?"
            hide ch2ep2f_yui2
    scene ch2ep2_359_a18 with dissolve
    show ch2ep2f_yui3 with dissolve
    window hide
    yui "Satisfied now, huh?"
    mc "Well, not bad..."
    $ renpy.pause()
    menu:
        "Next":
            yui "Not bad, huh?"
            yui "Well then, I guess I have no choice now..."
            hide ch2ep2f_yui3
    scene ch2ep2_359_a19 with dissolve
    show ch2ep2f_yui4 with dissolve
    window hide
    yui "*Sucks* Mmmmm....."
    mc "Ahh...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2f_yui4
    scene ch2ep2_359_a20 with dissolve
    show ch2ep2f_yui5 with dissolve
    window hide
    yui "*Sucks* Mmmmm... You enjoy what I am doing, huh?"
    mc "Yeah. You're doing pretty good..."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2f_yui5
    scene ch2ep2_359_a21 with dissolve
    show ch2ep2f_yui6 with dissolve
    window hide
    yui "*Sucks* Mmmmmmm....."
    mc "Keep sucking it like that, [yui]."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2f_yui6
    scene ch2ep2_359_a22 with dissolve
    mc "Hm? Why did you stop?"
    yui "Well, I think that's enough of a warm-up."
    yui "You're ready now, and I'm soaking wet down there."
    scene ch2ep2_359_a23 with dissolve
    yui "So...."
    scene ch2ep2_359_a24 with dissolve
    yui "Let's just do it."
    mc "......................"
    yui "What are you waiting for?"
    mc "Hm...?"
    yui "Are you really going to let me go full naked alone?"
    yui "Take off your top, dumbass!"
    mc "Oh, okay...."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_359_a25 with dissolve
    yui "Wait a sec...."
    mc "Hm...? What's wrong?"
    yui "I know that we did it before, but I'm not still used to your dick."
    yui "It's really big. Please, be gentle, okay?"
    mc "Sure, I will."
    scene ch2ep2_359_a26 with dissolve
    show ch2ep2f_yui7 with dissolve
    window hide
    $ renpy.pause(1.5, hard=True)
    hide ch2ep2f_yui7
    scene ch2ep2_359_a27 with dissolve
    yui "Ugh...!"
    mc "Are you alright?"
    yui "Yeah... This time it hurts a lot less than I expected."
    mc "Alright then, I'm going to start moving now."
    yui "Okay, do as you please."
    show ch2ep2f_yui8 with dissolve
    window hide
    yui "*Softly breathes* Ahhhh..... [mc]....."
    yui "*Softly breathes* Mmmmmm... We're just getting started, but it already feels so good...."
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2f_yui8
    scene ch2ep2_359_a28 with dissolve
    show ch2ep2f_yui9 with dissolve
    window hide
    yui "*Softly breathes* A-Mmmmm.... D-Don't stop....!"
    $ renpy.pause()
    menu:
        "Next":
            hide ch2ep2f_yui9
    scene ch2ep2_359_a29 with dissolve
    show ch2ep2f_yui10 with dissolve
    window hide
    yui "*Heavily breathes* Mmmmmmm~ [mc]....!!"
    yui "*Heavily breathes* A-Ahh...! You're so good...!!"
    $ renpy.pause()
    menu:
        "Next":
            yui "*Heavily breathes* H-Hold on a sec...!"
            mc "Hm...? Why?"
            yui "*Heavily breathes* I want to try something else."
            mc "Alright, what do you want to try, then?"
            hide ch2ep2f_yui10
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_359_a30 with dissolve
    yui "*Smiles* Let's do it like this..."
    mc "Okay. If that's what you want."
    yui "*Smiles* Hehe... Kiss me, [mc]."
    scene ch2ep2_359_a31 with dissolve
    mc "*Kisses* Mmmmm...."
    yui "*Kisses* Mmmmmm...."
    scene ch2ep2_359_a32 with dissolve
    yui "A-Ah...!"
    u "Hm? She put it in already? I didn't notice it because we were kissing."
    u "Well, that was smooth...."
    show ch2ep2f_yui11 with dissolve
    window hide
    yui "*Softly breathes* M-Mmmmmmm...... How's this position? Do you like it?"
    mc "Yeah....."
    $ renpy.pause()
    menu:
        "Next":
            yui "*Softly breathes* Let me move my hips a little bit faster..."
            hide ch2ep2f_yui11
    scene ch2ep2_359_a33 with dissolve
    show ch2ep2f_yui12 with dissolve
    window hide
    yui "*Moans* A-Ahhhh.... Mmmmmm.... [mc]....."
    yui "*Moans* M-Mmmmmm.... Y-Your cock is going so deep inside me in this position."
    yui "*Moans* I-It's driving me crazy now~!"
    menu:
        "Next":
            hide ch2ep2f_yui12
    scene ch2ep2_359_a34 with dissolve
    show ch2ep2f_yui13 with dissolve
    window hide
    yui "*Heavily breathes* M-Mmmmmm... A-Almost there....!"
    yui "*Heavily breathes* I-I'm almost cumming, [mc]...!"
    mc "*Heavily breathes* Me, too."
    menu:
        "Missionary":
            hide ch2ep2f_yui13
            jump ch2ep2_yuimis1
        "Slowest":
            hide ch2ep2f_yui13
            jump ch2ep2_yuiface1
        "Slower":
            hide ch2ep2f_yui13
            jump ch2ep2_yuiface2
        "Cum":
            jump ch2ep2_yuifacecum
label ch2ep2_yuimis1:
    scene ch2ep2_359_a27 with dissolve
    show ch2ep2f_yui8 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Face to face":
            hide ch2ep2f_yui8
            jump ch2ep2_yuiface1
        "Faster":
            hide ch2ep2f_yui8
            jump ch2ep2_yuimis2
        "Fastest":
            hide ch2ep2f_yui8
            jump ch2ep2_yuimis3
label ch2ep2_yuimis2:
    scene ch2ep2_359_a28 with dissolve
    show ch2ep2f_yui9 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Face to face":
            hide ch2ep2f_yui9
            jump ch2ep2_yuiface1
        "Slower":
            hide ch2ep2f_yui9
            jump ch2ep2_yuimis1
        "Faster":
            hide ch2ep2f_yui9
            jump ch2ep2_yuimis3
label ch2ep2_yuimis3:
    scene ch2ep2_359_a29 with dissolve
    show ch2ep2f_yui10 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Face to face":
            hide ch2ep2f_yui10
            jump ch2ep2_yuiface1
        "Slowest":
            hide ch2ep2f_yui10
            jump ch2ep2_yuimis1
        "Slower":
            hide ch2ep2f_yui10
            jump ch2ep2_yuimis2
label ch2ep2_yuiface1:
    scene ch2ep2_359_a32 with dissolve
    show ch2ep2f_yui11 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch2ep2f_yui11
            jump ch2ep2_yuimis1
        "Faster":
            hide ch2ep2f_yui11
            jump ch2ep2_yuiface2
        "Fastest":
            hide ch2ep2f_yui11
            jump ch2ep2_yuiface3
label ch2ep2_yuiface2:
    scene ch2ep2_359_a33 with dissolve
    show ch2ep2f_yui12 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch2ep2f_yui12
            jump ch2ep2_yuimis1
        "Slower":
            hide ch2ep2f_yui12
            jump ch2ep2_yuiface1
        "Faster":
            hide ch2ep2f_yui12
            jump ch2ep2_yuiface3
label ch2ep2_yuiface3:
    scene ch2ep2_359_a34 with dissolve
    show ch2ep2f_yui13 with dissolve
    window hide
    menu:
        "Missionary":
            hide ch2ep2f_yui13
            jump ch2ep2_yuimis1
        "Slowest":
            hide ch2ep2f_yui13
            jump ch2ep2_yuiface1
        "Slower":
            hide ch2ep2f_yui13
            jump ch2ep2_yuiface2
        "Cum":
            jump ch2ep2_yuifacecum
label ch2ep2_yuifacecum:
    mc "Where do you want me to cum?"
    yui "*Heavily breathes* Y-You can cum inside if you want! It's a safe day today."
    menu:
        "Cum inside":
            scene ch2ep2_359_a34_in with vpunch
        "Cum outside":
            scene ch2ep2_359_a34_out with vpunch
    mc "I'm cumming!!"
    yui "M-Me, too!!!"
    scene ch2ep2_359_a35 with dissolve
    yui "A-Ahhhhh....!!!!"
    u "Hm? Her boobs are right in front of my face."
    u "Maybe I should...."
    scene ch2ep2_359_a36 with vpunch
    yui "N-No!! That's my w-"
    yui "M-Mmmmmm...! I-I'm cumming again...!!!"
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_359_a37 with dissolve
    mc "Did you enjoy it?"
    yui "*Pants* Y... Yes.... I... enjoyed it... a lot...."
    yui "*Pants* L... Let me... rest for... a bit... okay?"
    mc "Sure."
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*........"
    scene ch2ep2_359_a38 with dissolve
    yui "Good night, [mc]."
    mc "Yeah. Good night, [yui]."
    stop sound fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    $ yui_relationship += 2
    $ yui_ch2_ep2 += 2
    jump ch2ep2_mayapickup
label ch2ep2_mayapickup:
    play music "sfx/ch2ep1_1.mp3" fadein 3.0
    $ bgm = "Roa - Winter Magic"
    scene ch2ep2_360 with dissolve
    u "... It's already morning."
    u "Today I have an appointment with [maya] in the evening."
    u "No matter how friendly she is, she is still someone at a much higher level than me."
    u "I should dress formally today. Let's get up and go take a shower."
    if ch2ep2letyuisleep == 1:
        scene ch2ep2_361 with dissolve
        u "[yui] already left."
        u "I thought I woke up pretty early today, but clearly she woke up earlier than me."
    scene black with dissolve
    $ renpy.pause()
    s "*Half an hour later*.........."
    scene ch2ep2_362 with dissolve
    u "Alright, let's go have breakfast...."
    u "I guess everyone is already in the kitchen."
    scene ch2ep2_363 with dissolve
    rin "O-Oh!?"
    mc "Hm...? [rin]?"
    scene ch2ep2_364 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_364.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_364_blink.jpg", 1) with dissolve
    rin "Wow...."
    mc "Good morning, [rin]."
    rin "Good morning, [mc]."
    rin "Is today a special day or something? Why are you dressed so formal?"
    rin "By the way, you look really handsome today, [mc]."
    menu:
        "You look so beautiful, too. [rin1]":
            $ ch2ep2comrin = 1
            $ rin_relationship += 1
            $ rin_ch2_ep2 += 1
            scene ch2ep2_365 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_365.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_365_blink.jpg", 1) with dissolve
            mc "I have an important appointment this evening. I can't just dress casually."
            rin "I see..."
            mc "By the way, you look really beautiful today, yourself."
            rin "*Smiles* Heh~? Really?"
            mc "Yeah... Your sweater suits you really well."
            rin "*Giggles* Hehe. Thanks!"
            if ch2ep2girltalk == True:
                $ rin_relationship += 1
                $ rin_ch2_ep2 += 1
                scene ch2ep2_366 with dissolve
                rin "Come here...."
                mc "Hm...?"
                scene ch2ep2_367 with dissolve
                rin "*Kisses* Mmmm....."
                mc "*Kisses*.........."
                scene ch2ep2_365 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_365.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_365_blink.jpg", 1) with dissolve
                rin "*Smiles* Thanks for such a nice compliment."
                rin "It's really good to hear that at the start of the day."
                mc "You're welcome."
        "Thank you.":
            $ ch2ep2comrin = 2
            mc "Thank you. I have an important appointment this evening, so..."
            rin "I see...."
    rin "Alright, I'm leaving now."
    mc "Hm? Already?"
    rin "Yeah. I already ate my breakfast. I'll be waiting for you guys in the hallway."
    mc "Okay then...."
    scene black with dissolve
    $ renpy.pause()
    if ch2ep2meetalice == 1:
        s "*A few hours later*............."
        scene ch2ep2_368 with fade
        u "........................."
        u "... Alright, it's lunchtime. Let's go find something to eat."
        s "*Phone vibrates*.........."
        $ ch2ep2alicemessage2 = True
        $ newmessage = True
        $ alice_messages_show = True
        $ alice_newmessage = True
        $ phone_alert = True
        scene ch2ep2_369 with dissolve
        u "Hm? Did I just get a new message?"
        u "Let's see...."
        scene ch2ep2_370 with dissolve
        u "Hm? It's from [alice]."
        u "Oh... I almost forgot that she wanted to meet with [faye] this morning."
        u "I wonder what she sent to me."
        jump ch2ep2_checkalicem2
    else:
        scene black with dissolve
        $ renpy.pause()
        s "You spent your day working until evening....."
        jump ch2ep2_mayapickup2
label ch2ep2_checkalicem2:
    if ch2ep2_reply_alice == False:
        scene ch2ep2_370 with vpunch
        u "I should answer the message first!"
        jump ch2ep2_checkalicem2
    elif ch2ep2_reply_alice == True:
        scene ch2ep2_371 with dissolve
        u "Okay, that is it. Let's go have lunch."
        scene black with dissolve
        $ renpy.pause()
        s "You went to have lunch, then came back to work until evening...."
        jump ch2ep2_mayapickup2
label ch2ep2_mayapickup2:
    scene ch2ep2_372 with dissolve
    u "... Alright, it's almost 5 p.m. now."
    u "Let's go wait for [maya] in front of the company, as she told me to."
    u "I better go wait for her instead of making her wait for me."
    scene black with dissolve
    $ renpy.pause()
    s "*About ten minutes later*..........."
    scene ch2ep2_373 with fade
    u "..................."
    s "*Horn sounds*........."
    unknown ".... [mc]."
    scene ch2ep2_374 with dissolve
    u "... Hm?"
    scene ch2ep2_375 with dissolve
    u "Oh, there she is...."
    maya "*Smiles* Come. Get in the car."
    mc "Okay, got it."
    scene black with dissolve
    scene ch2ep2_376 with dissolve
    maya "I'm sorry. I'm late."
    mc "It's alright. You don't have to say that at all."
    maya "Yes, I do. I shouldn't have made you wait for me like that."
    maya "I'm truly sorry. I had a meeting before I came here, but it took a bit longer than I expected."
    mc "It was out of your control. I understand you."
    maya "*Smiles* Thank you."
    scene ch2ep2_377 with dissolve
    maya "Alright, we're ready now."
    maya "Let's go to my house, [mrw]."
    mrw "Understood, president."
    scene black with dissolve
    $ renpy.pause()
    s "*About an hour later*.........."
    scene ch2ep2_378 with fade
    $ renpy.pause()
    scene ch2ep2_379 with dissolve
    maya "Thanks for working hard today, [angela]."
    maya "You may go home now."
    angela "Then, see you tomorrow, president."
    angela "I wish you a great dinner."
    maya "You, too."
    scene ch2ep2_380 with dissolve
    maya "Oh, by the way.... [mc]."
    mc "... Yes?"
    maya "I've just realized that I never introduced my secretary to you."
    maya "Let me introduce her to you since from now on you guys will no longer be strangers."
    scene ch2ep2_381 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_381.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_381_blink.jpg", 1) with dissolve
    maya "This is [angela]."
    angela "Nice to meet you, sir."
    u "... Sir?"
    mc "Nice to meet you, too...."
    mc "But, I'm no sir. You can just call me [mc]."
    angela "As you wish, [mc]."
    scene ch2ep2_382 with dissolve
    angela "Alright, I'm leaving now."
    angela "What time do you want [mrw] to come take [mc] back home?"
    maya "He should be here at 9 p.m."
    angela "Understood. I will tell him that."
    angela "Enjoy having dinner with your s-"
    scene ch2ep2_383 with dissolve
    angela "*Coughs*... W-with him!!"
    maya "(*Sighs* Jeez, [angela]... That was close...)"
    mc "... Are you alright?"
    angela "*Coughs* I'm good, thanks. Don't worry about me."
    scene ch2ep2_382 with dissolve
    angela "Alright, I'm leaving for real now."
    angela "Have a good time, president."
    maya "See you tomorrow, [angela]."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_384 with dissolve
    maya "Okay... now, it's just the two of us here."
    maya "Relax. Make yourself at home. Feel free to look around the house."
    maya "I'm going to prepare dinner real quick."
    mc "Thank you. I appreciate it."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_385 with dissolve
    $ renpy.pause()
    scene ch2ep2_386 with dissolve
    maya "Hm? Why did you follow me here?"
    mc "I feel bad letting you prepare dinner alone."
    mc "Is there anything you need me to help with?"
    mc "I'm not good at cooking, but I want to be a little bit of help."
    scene ch2ep2_387 with dissolve
    maya "*Smiles* There is really nothing I need your help with in here."
    maya "But, if you really want to help....."
    maya "My daughter, [skylar], should be in her room upstairs because she doesn't have a class at the university today."
    maya "And she might not have noticed that we're back home."
    maya "So, could you please go tell her to get ready for dinner?"
    maya "Her room has the biggest door on the floor."
    maya "Actually, it's literally the first room you see when you walk up there."
    mc "Yes, I can do that. You can leave it to me."
    maya "*Smiles* Thank you. I'm glad to hear that."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    $ ch2ep2freeroam = True
    $ area = "kitchen"
    play music "sfx/ch1ep2.mp3"
    $ bgm = "Bensound - Little Idea"
    jump ch2ep2_freeroam
label ch2ep2_freeroam:
    if ch2ep2hiddenimages_count == 7:
        $ ch2ep2hiddenimages = True
    if area == "bedroomentrance":
        jump ch2ep2_endfreeroam
    call screen ch2ep2house
label ch2ep2_kitchen_maya:
    if ch2ep2kitchen_pic == False:
        scene ch2ep2_kitchen_photo
    else:
        scene ch2ep2_kitchen
    scene ch2ep2_388 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_388.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_388_blink.jpg", 1) with dissolve
    maya "Hm? Is there still something that you want from me?"
    mc "... Can you tell me where to find your daughter again, please?"
    maya "Sure. You can find her upstairs. Her room has the biggest door on the floor."
    maya "Actually, it's literally the first room you see when you walk up there."
    mc "Okay, I think I get it now. Thank you."
    maya "*Smiles* You're welcome."
    jump ch2ep2_freeroam
label ch2ep2_endfreeroam:
    $ ch2ep2endfreeroam = True
    scene black
    $ renpy.pause()
    scene ch2ep2_390 with dissolve
    u "There it is...."
    u "[maya] said that her room is literally the first one I'll see when walking up here."
    u "It can't be anywhere else. That must be [skylar]'s room for sure."
    scene ch2ep2_391 with dissolve
    s "*Door knocks*........"
    skylar "... Yes, Mom?"
    mc "Err... I'm sorry, but I'm not [maya]."
    skylar "Oh... Wait a second, please."
    scene black with dissolve
    s "*Door opens*........."
    scene ch2ep2_392 at eyesblink("Ch.2/Ep.2/Scenes/ch2ep2_392.jpg", "Ch.2/Ep.2/Scenes/ch2ep2_392_blink.jpg", 1) with dissolve
    skylar "*Smiles* Good evening, [mc]!"
    mc "... Hm? You remember me?"
    skylar "Of course. How could I forget?"
    skylar "Mom said that you were going to come and have dinner with us this evening."
    mc "I see..."
    skylar "When did you get here? I was listening to music, so I didn't notice."
    mc "Not too long ago. Ten minutes I guess?"
    skylar "By the way, why did you come to my room? Is there something that you wanted?"
    mc "[maya] told me to come tell you to get ready for dinner."
    skylar "I see... Alright, let's go downstairs, then! I'm already ready."
    mc "Sure, let's go..."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_393 with dissolve
    skylar "Oh, there she is..."
    skylar "*Smiles* Welcome home, Mom!"
    scene ch2ep2_394 with dissolve
    maya "Oh, good evening, sweetheart."
    maya "How was your day?"
    skylar "It was great. What about you?"
    maya "*Smiles* It was a tiring day, but I'm better now."
    skylar "I'm glad to hear that. By the way, do you need any help there?"
    maya "No. No, it's alright. But, if you really want to help...."
    maya "How about you entertain [mc] while you wait for dinner?"
    skylar "Sure, Mom."
    scene ch2ep2_395 with dissolve
    skylar "*Smiles* You heard her, right?"
    mc "... Yes, I did."
    skylar "*Smiles* I'm now responsible for taking care of you."
    skylar "Is there something that you want to do in particular?"
    skylar "Have you looked around the house yet?"
    mc "Actually, there is nothing specific I want to do."
    mc "What about you? Do you have any ideas?"
    skylar "... Me?"
    mc "Yes, you."
    skylar "But, mom told me to entertain you, so we should do what you want, not what I want...."
    mc "...................."
    mc "Well then, I want to do whatever you want to do. How about that?"
    skylar "That could work I guess..."
    skylar "Alright then, how about we watch TV while we wait?"
    mc "Yeah, sure."
    scene black with dissolve
    $ renpy.pause()
    s "*Half an hour later*..........."
    scene ch2ep2_396 with dissolve
    maya "Alright, kids. Dinner is ready now."
    u "... Kids?"
    maya "Let's get to the table."
    skylar "Sure, Mom."
    mc "Understood."
    scene black with dissolve
    $ renpy.pause()
    scene ch2ep2_397 with dissolve
    skylar "Wow...! Did you really make all this, Mom?!"
    skylar "It all looks wonderful."
    u "... Why is she so surprised?"
    maya "*Smiles* Thanks, sweetheart. I'm glad to hear that."
    scene ch2ep2_398 with dissolve
    maya "[mc]."
    mc "Yes?"
    maya "You're probably wondering why she got so excited for just food, right?"
    u "Wait.... How did she know that?"
    maya "It's because I hardly ever cook for myself or for her."
    maya "I'm too busy to do it, so it's my personal cook who makes us food most of the time."
    maya "But, I felt like cooking today, because you're here with us."
    scene ch2ep2_399 with dissolve
    mc "......................."
    mc "... Thank you. I feel so honored now."
    maya "*Smiles* Alright, let's just stop talking and eat. Shall we?"
    mc "Yeah, sure."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    s "*After some time passed*..........."
    play music "sfx/ch2ep2_4.mp3" fadein 3.0
    $ bgm = "LiQWYD - Lay Me Down"
    scene ch2ep2_400 with dissolve
    skylar "That was really delicious. I'm full now."
    skylar "Thank you for dinner, mom."
    maya "Anytime, dear. I'm glad that you liked it."
    skylar "You should really cook more often, mom. I'm serious."
    maya "*Giggles* I'll consider that."
    scene ch2ep2_401 with dissolve
    maya "What about you, [mc]? Did you like the food?"
    mc "Yes, it was very delicious. I've never had Japanese food this delicious before."
    maya "*Giggles* Stop it. You're exaggerating."
    mc "No, I'm not. I really meant that."
    maya "*Smiles* Aw... Thank you then."
    scene ch2ep2_402 with dissolve
    maya "By the way... how is your life? Is everything alright?"
    mc "Hm...? Why do you ask?"
    maya "Well, I'm just trying to get to know you better."
    mc "......................"
    mc "Well... I have a job and a house to live in. I think my life is pretty good right now."
    maya "I'm glad to hear that...."
    maya "But if there is anything you ever want my help with, please come to me, okay?"
    mc ".... Thank you. I really appreciate it."
    scene ch2ep2_403 with dissolve
    skylar "You can also come to me, too."
    skylar "I know I'm younger than you, but I'll try my best to help."
    mc "...................."
    mc "Thank you, [skylar]. You're so kind."
    scene ch2ep2_404 with dissolve
    maya "By the way, you live in a shared house with [rin], [zeke], and [yui], right?"
    mc ".... How did you know that?"
    maya "[rowan] told me that. I asked him about you."
    mc "...................."
    mc "... Yeah, I live with them."
    maya "I see.... Then, do you always go to the company with them?"
    mc "Yes, [zeke] has a car. He takes us to the company and back home."
    mc "But recently, there are times that we have to go home by ourselves because he has to go pick up his girlfriend."
    maya "Well, that doesn't sound so convenient to me..."
    scene ch2ep2_405 with dissolve
    maya "How about this? I will hire a personal driver for you so that you don't have to rely on anyone."
    mc "What? No. I mean... I'm grateful for your kindness, but you don't have to do that."
    maya "It's alright. I'm willing to do it. It's not a big deal at all."
    maya "It's better for you if you have a personal driver to drive you home when you feel tired after working."
    skylar "Yeah, she is right, [mc]."
    mc "......................"
    scene ch2ep2_406 with dissolve
    maya "I can arrange it for you tomorrow. How does that sound?"
    mc "......................."
    maya "[mc]? Do you hear me?"
    scene ch2ep2_407 with dissolve
    mc "Excuse me, but can I ask you something?"
    maya "Yeah, sure. What do you want to ask?"
    mc "Why are you doing this for me?"
    maya "Hm? What are you talking about? I don't understand."
    scene ch2ep2_408 with dissolve
    mc "I thought it was odd that you invited me to have dinner with you here."
    mc "But, maybe you just wanted to take care of an employee of the company you invested your money in. So, it was understandable."
    mc "However, since I stepped foot in here, everything has been getting weirder and weirder."
    mc "Both of you have been way too kind towards me."
    mc "If I were someone in the upper echelons of the company, yeah it might make sense."
    mc "But, no matter how much I try to understand it, I just can't understand why you want to hire a personal driver for just a normal employee like me."
    mc "There is no way that you'd do this for every employee, so why me?"
    maya "I........"
    scene ch2ep2_409 with dissolve
    maya "[skylar]....."
    skylar "Mom...."
    scene ch2ep2_410 with dissolve
    skylar "It's alright, mom. No matter what happens, I'll always be with you."
    maya "Sweetheart...."
    skylar "So, don't be afraid. Just tell him the truth."
    u "Hm...? The truth?"
    maya "..................."
    maya "*Sighs* Okay...."
    scene ch2ep2_411 with dissolve
    mc "What truth was she talking about?"
    maya "Calm down. I'm going to tell you now."
    mc "..................."
    maya "Yeah, you're right. I've never invited anyone here before. Not even [rowan]. I only invited him to my vacation house once."
    maya "And to make it clear, you aren't just a normal employee to me."
    maya "The reason I invited you here, is because...."
    maya "...................."
    mc ".... Because?"
    maya "You're my son."
    scene ch2ep2_412 with dissolve
    mc ".... W-What?"
    stop music fadeout 3.0
    scene black with dissolve
    hide screen smartphone
    $ rin_ch2_ep2 = 2
    $ episode = 6
    call screen ending
label ch2ep2_backyard_pool:
    if ch2ep2backyard_pic == False:
        scene ch2ep2_backyard_photo
    else:
        scene ch2ep2_backyard
    u "Nice pool, but it's not time to swim now."
    jump ch2ep2_freeroam
label ch2ep2_livingroom_sofa:
    if ch2ep2livingroom_pic1 == False and ch2ep2livingroom_pic2 == False:
        scene ch2ep2_livingroom_photos
    if ch2ep2livingroom_pic1 == True and ch2ep2livingroom_pic2 == False:
        scene ch2ep2_livingroom_photo2
    if ch2ep2livingroom_pic1 == False and ch2ep2livingroom_pic2 == True:
        scene ch2ep2_livingroom_photo1
    elif ch2ep2livingroom_pic1 == True and ch2ep2livingroom_pic2 == True:
        scene ch2ep2_livingroom
    u "Nice sofa. It looks very comfortable."
    jump ch2ep2_freeroam
label ch2ep2_bathroom_bathtub:
    if ch2ep2bathroom_pic == False:
        scene ch2ep2_bathroom_photo
    else:
        scene ch2ep2_bathroom
    u "What a nice bathtub this is. It must be very expensive."
    jump ch2ep2_freeroam
label ch2ep2_livingroom_pic1:
    if _in_replay:
        scene ch2ep2_livingroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    if ch2ep2livingroom_pic2 == False:
        scene ch2ep2_livingroom_photo2
    else:
        scene ch2ep2_livingroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep2livingroom_pic1 = True
    $ ch2ep2hiddenimages_count += 1
    jump ch2ep2_freeroam
label ch2ep2_livingroom_pic2:
    if _in_replay:
        scene ch2ep2_livingroompic2 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    if ch2ep2livingroom_pic1 == False:
        scene ch2ep2_livingroom_photo1
    else:
        scene ch2ep2_livingroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep2livingroom_pic2 = True
    $ ch2ep2hiddenimages_count += 1
    jump ch2ep2_freeroam
label ch2ep2_kitchen_pic:
    if _in_replay:
        scene ch2ep2_kitchenpic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ch2ep2_kitchen
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep2kitchen_pic = True
    $ ch2ep2hiddenimages_count += 1
    jump ch2ep2_freeroam
label ch2ep2_backyard_pic:
    if _in_replay:
        scene ch2ep2_backyardpic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ch2ep2_backyard
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep2backyard_pic = True
    $ ch2ep2hiddenimages_count += 1
    jump ch2ep2_freeroam
label ch2ep2_bathroom_pic:
    if _in_replay:
        scene ch2ep2_bathroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ch2ep2_bathroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep2bathroom_pic = True
    $ ch2ep2hiddenimages_count += 1
    jump ch2ep2_freeroam
label ch2ep2_balcony_pic:
    if _in_replay:
        scene ch2ep2_balconypic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ch2ep2_balcony
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep2balcony_pic = True
    $ ch2ep2hiddenimages_count += 1
    jump ch2ep2_freeroam
label ch2ep2_fitness_pic:
    if _in_replay:
        scene ch2ep2_fitnesspic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ch2ep2_fitness
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ch2ep2fitness_pic = True
    $ ch2ep2hiddenimages_count += 1
    jump ch2ep2_freeroam
