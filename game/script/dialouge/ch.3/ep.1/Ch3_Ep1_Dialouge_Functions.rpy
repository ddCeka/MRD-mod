label ch3ep1start:
    scene black with dissolve
    $ renpy.pause(3, hard=True)
    scene ch3 with dissolve
    $ renpy.pause(3, hard=True)
    scene ep1 with dissolve
    $ renpy.pause(3, hard=True)
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ch2ep2_1.mp3" fadein 3.0
    $ bgm = "Roa Music - After the rain"
    show screen smartphone
    if ch2ep4decision == 1:
        $ ch3ep1yuims = True
        scene ch3ep1_1 with fade
        s "*Elevator sounds*..........."
        u "Finally, it's time to get off work..."
        u "I need to go b-"
        unknown "Hey, [mc]!"
        scene ch3ep1_2 with dissolve
        u "Hm...?"
        mc "Oh... Hey, [zeke]."
        scene ch3ep1_3 with dissolve
        zeke "How was your work today?"
        mc "Same as always. Just checking codes to see if there was any error."
        zeke "I see... Pretty boring, huh?"
        mc "Not for me."
        mc "Why are you guys together though? Are you going home?"
        scene ch3ep1_4 with dissolve
        yui "No, it's Friday. There is no need to rush home, so we're going for a movie together."
        mc "Hm? How come I never knew about that?"
        rin "We made the decision at lunchtime, but you weren't there with us."
        rin "Therefore, I told [yui] to send you a message to ask if you wanted to come together."
        yui "And I already did, but you didn't reply my message."
        yui "I also couldn't find a chance to ask you when we were in the department room since you were lost in thought for the whole afternoon."
        scene ch3ep1_5 with dissolve
        mc "Sorry..."
        mc "I had a lot of things to think about."
        yui "Yeah, I could tell that."
        scene ch3ep1_6 with dissolve
        zeke "Are you sure you are alright, bud?"
        zeke "Is there something I can help you with?"
        mc "Yeah, I'm good. Don't worry about me."
        zeke "Are you sure? If you happen to need my help, come to me no matter what. Okay?"
        mc "Sure thing. Thank you."
        scene ch3ep1_7 with dissolve
        zeke "By the way, do you want to come with us?"
        mc "I can't. I already have a plan for this evening."
        zeke "Oh, is that so? Alright then, see you at home."
        mc "See you. Enjoy the movie, guys."
        scene black with dissolve
        $ renpy.pause()
        s "You waited until everyone has left.........."
        scene ch3ep1_8 with dissolve
        u "Okay...."
        u "Let's continue with the plan."
        scene black with dissolve
        $ renpy.pause()
        s "*About an hour later*.............."
        scene ch3ep1_9 with fade
        u "Alright.... I've already got it."
        u "To think about it, it was very careless that I used my phone to contact with [maya] and [angela]."
        u "So, I've brought a new one."
        u "Well... it's actually not new since it's second handed."
        u "But, that's not the point. What's more important, is that I'll be safe from now on if [victor] somehow decide to check my call history."
        scene ch3ep1_10 with dissolve
        u "Well...."
        u "Let's call [felix] now...."
        u "......................."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_12 with fade
        felix "[mc]...."
        felix "I'm glad that you called."
        scene ch3ep1_11 with dissolve
        mc "Wait..."
        mc "I haven't said a single word. How did you know it was me?"
        scene ch3ep1_12 with dissolve
        felix "Well, it's not that hard to guess."
        felix "I barely give my contact to someone."
        felix "So... Have you made up your mind yet?"
        scene ch3ep1_11 with dissolve
        mc "Yeah. I'm going to cooperate with you."
        mc "Let's take down [victor] together."
        scene ch3ep1_12 with dissolve
        felix "You made the right decision. Well done."
        scene ch3ep1_13 with dissolve
        mc "By the way, do you happen to know a place where there is no CCTV, and unknown to people?"
        scene ch3ep1_14 with dissolve
        felix "What would you want such a place like that for?"
        scene ch3ep1_13 with dissolve
        mc "There is something I need to give to you."
        mc "We have to meet at a place like that in order to not get caught."
        scene ch3ep1_14 with dissolve
        felix "Well, in that case, I know a place that would work."
        felix "I will send you the location after the call ends."
        felix "When are we going to meet?"
        scene ch3ep1_13 with dissolve
        mc "Tomorrow morning at 10."
        scene ch3ep1_14 with dissolve
        felix "Noted."
        felix "See you tomorrow."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_15 with dissolve
        u "Alright...."
        u "It's been a long time since the last time I touched {b}it{/b}."
        scene ch3ep1_16 with dissolve
        u "I keep it safely inside my luggage that is very well protected."
        u "I never knew that I'm going to have to use it this quick."
        u "Let's go take it out..."
        scene black with dissolve
        scene ch3ep1_17 with dissolve
        u "....................."
        u "I've seen what [victor] did to those kids who failed to complete missions."
        u "So, I recorded an audio every time I was given a task. I also made a copy of some illegal documents."
        u "I have to have the upper hand in order to deal with him."
        scene ch3ep1_18 with dissolve
        u "To be sure...."
        u "Let's turn on the computer and check if every file still works well."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_19 with dissolve
        u "Alright..."
        u "Every single file works perfectly. I have no problem opening each of them at all."
        u "I should also make a copy of them first before giving this USB drive to [felix] tomorrow."
        scene ch3ep1_20 with dissolve
        u "Okay, it's done...."
        u "To be honest I don't know if this will be enough to take [victor] down."
        u "But, I hope [felix] can make use of these files to their best."
        scene black with dissolve
        $ renpy.pause()
        s "Next morning............"
        scene ch3ep1_21 with fade
        u "According to Google Maps, it takes me about an hour and a half to get there by car."
        u "But, I don't have a car now, so I need to go there by bus and drop by the nearest stop."
        u "Then, walk all the way to the meeting point."
        u "It's half past seven now. I better hurry up...."
        scene black with dissolve
        $ renpy.pause()
        s "*About two hours later*.............."
        scene ch3ep1_22 with fade
        u "Okay, here we are...."
        u "[felix] told me in the message that the meeting point is an abandoned house."
        u "Looks like this is it."
        scene ch3ep1_23 with dissolve
        u "...................."
        u "Yeah... This place will do."
        u "No way [victor]'s going to know about this place and what I'm going to do today."
        u "But, where's [felix] though...?"
        scene black with dissolve
        $ renpy.pause()
        s "*Fifteen minutes later*.........."
        scene ch3ep1_24 with dissolve
        felix "Oh, you're already here?"
        mc "You're late...."
        mc "I told you to meet up at 10."
        felix "I'm sorry. I had to deal with something before coming here."
        felix "And it took more time than I thought."
        scene ch3ep1_25 with dissolve
        mc "Fine...."
        felix "Alright, let's get down to business."
        felix "What's that something you are going to give to me?"
        scene ch3ep1_26 with dissolve
        mc "Yeah, let's get down to business."
        mc "I need you to confirm that you are not going to betray me by putting me in jail."
        felix "Yes, I'm not going to put you in jail. You're not the person I've been targeting in the first place."
        mc "........................"
        mc ".... Hang on a sec."
        scene ch3ep1_27 with dissolve
        mc "Say that again. I'm going to record it."
        mc "I also need you to say your name as well."
        felix "Aren't you being too skeptic? If I'm going to arrest you, I would have done that since the last time we met already."
        mc "......................."
        felix "*Sighs* Fine. My name is [felix], I'm the Director General of Police."
        felix "I'm here making a deal with [mc] who agreed to cooperate with me in order to arrest [victor]."
        felix "In return, I will let him free after we successfully do so."
        felix "Are you satisfied now?"
        mc "Yeah. That'd be enough."
        scene ch3ep1_28 with dissolve
        mc "Here you are. Take it."
        felix "What's in that USB drive?"
        mc "Audio files of [victor] ordering me to do something, and a copy of illegal documents."
        mc "I think it might be helpful for you."
        felix "Thank you..."
        scene ch3ep1_29 with dissolve
        mc "Hold on."
        felix "... What now?"
        mc "You do realize that I'm risking my life doing this, right?"
        mc "Are you sure you can take down [victor]?"
        felix "I'd be lying if I say that I'm sure."
        felix "It's going to be hard, but there is a high possibility of success."
        felix "I'll try my best to make that possibility higher."
        mc "........................"
        scene ch3ep1_28 with dissolve
        mc "*Sighs* Fine... It's not like I can go back now."
        mc "I'll bet on you then."
        felix "Thank you."
        scene ch3ep1_30 with dissolve
        mc "By the way, can I ask why are you going after [victor]?"
        mc "Not everyone wants to mess with such a powerful person like him."
        felix "......................."
        mc "Is it personal?"
        scene ch3ep1_31 with dissolve
        felix "Personal? No, it's nothing personal."
        felix "[victor] has been breaking the law like it's nothing for years now."
        felix "As a police, I'm just doing my job as I'm supposed to."
        mc "I never knew police was supposed to make a deal with people like me."
        scene ch3ep1_32 with dissolve
        felix "Well, the world isn't always black and white."
        felix "I'm also not a good person. But, I have never ruined anyone's life unlike people like [victor]."
        felix "So, I can sometimes turn a blind eye. I don't mind letting go a little fish if it helps me get a larger one."
        mc ".... Okay."
        scene ch3ep1_33 with dissolve
        felix "Alright, I'm leaving now."
        felix "Thank you for the USB. I'll use it well."
        mc "Yeah, you better will."
        felix "Good bye for now. Contact me whenever you have anything updated."
        mc "You, too."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_34 with dissolve
        u "I hope I made the right decision...."
        u "*Sighs* Whatever. There is no turning back now."
        scene ch3ep1_35 with dissolve
        u "Now, there is one more thing to do...."
        u "Let's call her now."
        scene ch3ep1_36 with dissolve
        u "I don't know if she will pick up my call."
        u "Since it's an unknown phone number for her after all."
        u "I hope she answers the call."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_38 with fade
        maya ".... Hello?"
        maya "Who's it?"
        scene ch3ep1_37 with dissolve
        u "Oh, she picked up the call now."
        mc "Good morning, [maya]."
        mc "It's me, [mc]."
        scene ch3ep1_39 with dissolve
        maya "Oh?!"
        maya "Good morning, [mc]."
        maya "I never knew it was you. Why did you change your number?"
        scene ch3ep1_37 with dissolve
        mc "It's a long story."
        mc "Do you have some time for me? Can we meet?"
        scene ch3ep1_39 with dissolve
        maya "Sure. I'll always have time for you."
        maya "When should we meet?"
        scene ch3ep1_37 with dissolve
        mc "In an hour. Where can I meet you?"
        scene ch3ep1_38 with dissolve
        maya "Hm...? In an hour?"
        scene ch3ep1_37 with dissolve
        mc "Why? Are you busy now?"
        scene ch3ep1_39 with dissolve
        maya "Nothing. You can come meet me at my company."
        maya "I'll be waiting for you here."
        scene ch3ep1_37 with dissolve
        mc "Thank you."
        scene ch3ep1_40 with dissolve
        u "Alright...."
        u "Let's hurry up and go to her company...."
        scene black with dissolve
        $ renpy.pause()
        s "*About an hour later*............"
        scene ch3ep1_41 with fade
        angela "[mc]...."
        mc "Hi."
        scene ch3ep1_42 with dissolve
        mc "There are quite a lot of employees here."
        mc "I thought the company is closed on the weekends."
        angela "No, it isn't. Our company opens everyday."
        angela "But, we allow our employees to choose two days they want for days off."
        scene ch3ep1_43 with dissolve
        mc "I see..."
        mc "Alright, I guess [maya] sent you here. Shall we go see her now?"
        angela "Sure thing. Follow me, please. I'll take you there."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_44 with fade
        angela "President."
        maya "Thank you for your service, [angela]."
        maya "Please, have a seat, [mc]."
        mc "Sure."
        scene ch3ep1_45 with dissolve
        maya "How are you?"
        mc "Not so good. Still trying to figure things out, but thank you for asking."
        mc "What about you?"
        scene ch3ep1_46 with dissolve
        maya "Pretty busy lately, but it's not the first time. So, I'll get through it soon."
        maya "Anyway, I was surprised that you wanted to see me."
        maya "Why do you want to meet me? Is there anything I can help you with?"
        scene ch3ep1_47 with dissolve
        mc "Well....."
        mc "........................"
        maya "Hm...?"
        scene ch3ep1_48 with dissolve
        maya "Oh? There is no need to be worry about [angela]."
        maya "I've been working with her for years. She's always by my side."
        mc "......................."
        maya "I guarantee that you can trust her. She's very good at keeping secrets."
        scene ch3ep1_49 with dissolve
        mc "Fine... If you say so."
        mc "I've decided to help [felix] taking down [victor]."
        mc "I went to see him before coming here...."
        scene black with dissolve
        $ renpy.pause()
        s "You told [maya] everything about you since the first day you met [victor]....."
        scene ch3ep1_50 with dissolve
        maya "Oh my...."
        maya "I never knew you grew up being treated like that...."
        maya "I'm so sorry, sweetheart. It was all my fault."
        scene ch3ep1_51 with dissolve
        mc "... It's fine. I don't blame you."
        mc "It can't be denied that I'm alive right now because I met him as well."
        mc "Otherwise, I'd have ended up death in the slum already."
        maya "...................."
        scene ch3ep1_52 with dissolve
        maya "I know that [victor] is bad, but..."
        maya "I never knew he was that evil until hearing everything from you."
        maya "I'm so worried about you now, sweetheart. You will surely be in danger if you mess with him."
        mc "Yeah... But, it's not like a have a choice."
        maya ".... Is there anything I can do for you?"
        scene ch3ep1_53 with dissolve
        mc "Thank you, but I can do this myself."
        mc "Your kindness is already enough."
        mc "I don't want to put you in danger."
        scene ch3ep1_54 with dissolve
        maya "But..."
        maya "I can't just stay still doing nothing after knowing your situation."
        maya "Please, let me help you. Even if it's just a little matter."
        mc "......................."
        scene ch3ep1_53 with dissolve
        mc "Alright...."
        mc "Then, can you please tell everything to [rowan]?"
        mc "He's the owner of Xecon after all. He should know this, too."
        maya "Sure thing. I will tell him as soon as I can."
        scene ch3ep1_55 with dissolve
        maya "Aw... It's already twelve?"
        maya "I'm so sorry, but I have to go now. I have an appointment at 1 p.m."
        mc "Oh, sure."
        scene ch3ep1_56 with dissolve
        maya "[angela]."
        angela "Yes, president."
        maya "You don't have to come with me today, but can you please take [mc] home?"
        angela "As you wish."
        scene ch3ep1_57 with dissolve
        mc "It's fine... I can go home by myself."
        maya "I know, but I will feel better if [angela] goes with you."
        maya "I'm sorry for being so sensitive..."
        mc "...................."
        mc "Okay, if that's what you want..."
        maya "Thank you. Please stay safe, son."
        mc "Yeah, I will...."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_58 with fade
        $ renpy.pause()
        scene ch3ep1_59 with dissolve
        angela "Okay..."
        angela "Please, go wait for me here in front of the company."
        angela "I'll go get a car to pick you up."
        mc "....................."
        mc "Hang on a sec."
        scene ch3ep1_60 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_60.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_60_blink.jpg", 1) with dissolve
        angela "Hm? What's wrong?"
        mc "....................."
        menu:
            "I'm kind of hungry [angela1]":
                $ ch3ep1lunchwithangela = 1
                $ angela_relationship += 1
                $ angela_ch3_ep1 += 1
                mc "Aren't you hungry? I'm kind of hungry now."
                angela "Actually... I'm a little bit hungry, too."
                mc "Great. Then, why don't we go find something to eat first."
                scene ch3ep1_61 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_61.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_61_blink.jpg", 1) with dissolve
                angela "Sure thing."
                angela "What do you want to eat in specific?"
                mc "I don't want to eat anything specificly. I'm not familiar with places around here as well."
                mc "Why don't you take me to your favorite restaurant?"
                angela "Okay sure."
                jump ch3ep1lunchangela
            "Nothing. Sorry.":
                $ ch3ep1lunchwithangela = 2
                mc "Nothing. Sorry."
                mc "You can go get a car now."
                mc "I'll go and wait outside."
                angela "Okay....."
                scene black with dissolve
                $ renpy.pause()
                jump ch3ep1gethome
label ch3ep1lunchangela:
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene ch3ep1_63 with fade
    angela "This is one of my favorite restaurant."
    angela "It's quite near to the company. The food is also tasty."
    angela "So, I come here quite often at lunch hour."
    scene ch3ep1_62 with dissolve
    mc "Yeah? What kind of a restaurant is it?"
    angela "It's an Italian restaurant, but they also make a variety of food from different countries."
    angela "It's just... Italian food is the most delicious."
    scene ch3ep1_64 with dissolve
    mc "Alright then, let me look at the menu first."
    angela "Yeah, me too."
    mc "Do you mind recommending me a dish?"
    angela "No, not at all. I recommend you try spaghetti Bolognese. It's very delicious."
    mc "Let me see..."
    mc "Yeah, it does look tasty. I'll try it."
    scene ch3ep1_65 with dissolve
    mc "What about you?"
    mc "What are you going to have?"
    angela "Uhm... I think I'll take a Risotto for today."
    mc "Okay..."
    scene black with dissolve
    scene ch3ep1_66 with dissolve
    waitress "Hello! What'd you like to have, sir?"
    mc "Can I have a dish of spaghetti Bolognese, please?"
    waitress "Sure. Any thing else?"
    mc "And a cup of water. Thank you."
    scene ch3ep1_67 with dissolve
    waitress "What about you, miss?"
    angela "I'd like to have a dish of Risotto, please"
    angela "Oh, and please don't add any onion in it. Thank you."
    waitress "Noted that. What about a drink?"
    angela "Just a cup of water, please."
    scene ch3ep1_68 with dissolve
    waitress "Alright, let me re-check your orders and see if they're correct..."
    waitress "A dish of spaghetti Bolognese, and a dish of Risotto with no onion, and two cups of water..."
    angela "Yeah, that's correct."
    waitress "Perfect. Please, wait a moment. Your food will be ready to serve in fifteen minutes."
    angela "Thank you."
    scene black with dissolve
    scene ch3ep1_69 with dissolve
    mc "......................"
    angela "...................."
    mc "....................."
    scene ch3ep1_70 with dissolve
    angela ".... Why are you looking at me like that?"
    mc "To think about it, [maya] said that I could believe you."
    mc "I really wanted to, but in fact I still don't know you well."
    angela "Yeah... you're right."
    scene ch3ep1_71 with dissolve
    mc "I even think I made a mistake by letting you hear everything I told [maya]."
    angela "Why? Are you scared that I will rat you out?"
    mc "....................."
    mc ".... Yeah."
    scene ch3ep1_72 with dissolve
    angela "There is no way I'm going to do that."
    mc "How can I believe you?"
    angela "Believe it or not, I'm loyal to your mother."
    angela "Moreover, what is the point in doing that? What would I get?"
    angela "Think about it, it will only put me in a bad situation."
    angela "I will either get fired for that, or get killed by [victor] since I know too much about him now."
    scene ch3ep1_73 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_73.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_73_blink.jpg", 1) with dissolve
    mc "......................"
    mc "Yeah, you're right. I'm sorry."
    angela "It's fine. There is no need to be sorry. I totally understand you."
    angela "I'd be like that if I were in your position as well."
    mc "... Thank you for being understanding."
    angela "Alright, since we're talking about this now, is there any more thing you want to ask me?"
    angela "It can be anything if you think it helps you to get to know me better."
    mc "........................"
    jump ch3ep1lunchtalk
label ch3ep1lunchtalk:
    scene ch3ep1_74 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_74.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_74_blink.jpg", 1) with dissolve
    menu:
        "How old are you?":
            mc "Alright then, let's start with your age."
            mc "How old are you?"
            scene ch3ep1_73 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_73.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_73_blink.jpg", 1) with dissolve
            angela "Uhm.... To be honest I stopped counting my age for a while already. Let me think..."
            angela "Oh! I'm 26 years old now."
            $ angela_age = "26"
            mc "I see..."
            jump ch3ep1lunchtalk
        "How would you describe yourself?":
            mc "How would you describe yourself?"
            angela "Like what?"
            mc "Like... what kind of person do you think you are?"
            scene ch3ep1_73 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_73.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_73_blink.jpg", 1) with dissolve
            angela "Okay, I get it now."
            angela "Well... I see myself as a calm and loyalty person."
            angela "I don't freak out when facing a problem, but patiently deal with it instead."
            angela "I have also never betrayed anyone in my life before. Not even once."
            $ angela_perso = "Calm, Loyalty"
            jump ch3ep1lunchtalk
        "What are you favorite things?":
            mc "I want to know your favorites."
            mc "Tell me three things you like the most. It can be anything."
            scene ch3ep1_73 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_73.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_73_blink.jpg", 1) with dissolve
            angela "I think you can guess one of them. I like to eat Italian food."
            $ angela_like1 = "Italian Food"
            angela "For this one, you might not believe it. I love watching anime."
            $ angela_like2 = "Anime"
            mc "Well... I believe you. It's just... I didn't expect that from someone like you."
            mc "I mean... you don't look like a person who enjoy watching anime."
            angela "And the last one.... It's Japan. I always have a dream of going to Japan."
            $ angela_like3 = "Japan"
            mc "Now, that's not completely unexpected...."
            angela "Yeah... I want to go there so bad but, I don't have enough time to do that yet."
            jump ch3ep1lunchtalk
        "What do you hate?":
            mc "Now, let's talk about things you don't like."
            mc "Tell me three things you dislike the most."
            scene ch3ep1_73 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_73.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_73_blink.jpg", 1) with dissolve
            angela "Drugs are definitely the thing I hate the most."
            $ angela_hate1 = "Drugs"
            mc "Why...?"
            angela "It isn't anything good at all. I really don't understand why some people take it."
            angela "The second thing I dislike the most is disloyalty."
            $ angela_hate2 = "Disloyalty"
            angela "As a loyal person myself, I'd feel pretty bad if someone isn't loyal to me."
            mc "That's understandable..."
            angela "The last one would be lightning."
            $ angela_hate3 = "Lightning"
            mc "Why? Because it's loud?"
            angela ".... I'm sorry. I'm not ready to tell you that yet."
            mc "... Okay. It's fine."
            jump ch3ep1lunchtalk
        "Next":
            scene black with dissolve
            $ renpy.pause()
            jump ch3ep1lunchcontinue
label ch3ep1lunchcontinue:
    scene ch3ep1_75 with dissolve
    angela "Is there any more thing you are curious about me?"
    mc "... No, there isn't. I think that's enough for today."
    angela "Okay then..."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time having lunch with [angela] for a while...."
    scene ch3ep1_76 with dissolve
    angela "Are you full now?"
    mc "Yes, and u?"
    angela "Me, too. Alright then, let's leave here."
    mc "Sure."
    scene ch3ep1_77 with dissolve
    angela "You can go and wait me at the car first."
    angela "I'm going to pay for the bill."
    mc "You don't have to... We can just split the bill."
    angela "It's alr-"
    scene ch3ep1_78 with vpunch
    angela "*Shoulder bumps* Aw...!"
    mc "Watch out..."
    scene ch3ep1_79 with vpunch
    angela ".................."
    mc "Hey, watch where you're going..."
    unknown "Oh, I'm sorry... I didn't mean to."
    mc "Get out of my sight."
    unknown "Okay! I'm really sorry!"
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_80 with dissolve
    mc "Hey. Are you alright?"
    mc "You aren't hurt anywhere, right?"
    angela "No, I'm not. I'm completely fine."
    mc "Good to hear that."
    scene ch3ep1_81 with dissolve
    angela "Thank you, [mc]."
    angela "I'd have ended up hurting myself if it wasn't for you."
    mc "It's not a big deal, but you're welcome."
    angela "Alright then, I'm going to pay for the bill now. See you at the parking lot."
    mc "Sure thing."
    $ angela_relationship += 2
    $ angela_ch3_ep1 += 2
    scene black with dissolve
    $ renpy.pause()
    jump ch3ep1gethome

label ch3ep1gethome:
    scene ch3ep1_82 with fade
    mc "Thank you for taking me home."
    angela "No need to thank me. It's my duty to do so."
    mc "Okay then, good bye."
    angela "Good by-"
    scene ch3ep1_83 with dissolve
    mc "Hold on...."
    angela "Hm? What's wrong?"
    mc "I forgot to tell you this. Please, tell [maya] to contact me on my new phone number."
    angela "Noted that."
    mc "Thank you. See you later."
    angela "See you later, too."
    scene black with dissolve
    $ renpy.pause()
    s "Later that night............"
    scene ch3ep1_84 with fade
    u "Alright.... I've finished taking a shower."
    u "Let's find something to wear before go to bed."
    u "It's pretty late now. I'm so sleepy."
    scene ch3ep1_85 with dissolve
    s "*Ringtone sounds*............."
    u "Hm? Who's calling me at a time like this?"
    u "... That's the new phone. I guess it's either [felix] or [maya]."
    u "Let's pick it up and see...."
    scene ch3ep1_86 with dissolve
    mc "Hello...."
    scene black with dissolve
    scene ch3ep1_88 with dissolve
    maya "It's me, sweetheart."
    maya "Sorry for calling you at late night like this. Did I wake you up?"
    scene ch3ep1_86 with dissolve
    mc "No. Not at all. I just got out of a bathroom."
    mc "Why are you calling me though? What's going on?"
    scene ch3ep1_88 with dissolve
    maya "I just informed [rowan] about [victor] and you..."
    scene ch3ep1_87 with dissolve
    mc "And? What did he say after hearing everything?"
    scene ch3ep1_89 with dissolve
    maya "He seemed very shock. He was speechless for almost a full minute."
    maya "I can't blame him though. I had that same reaction, too."
    maya "But, he understood the situation so quickly after getting his sense back."
    maya "He didn't blame you for the reason you are in his company at all."
    scene ch3ep1_88 with dissolve
    maya "Instead he wanted to thank you for telling the truth."
    maya "So, he told me to ask you if you could go meet him tomorrow at 2 p.m.?"
    scene ch3ep1_87 with dissolve
    mc "Hm? Where do I have to go meet him?"
    scene ch3ep1_89 with dissolve
    maya "At his house. I'll be there, too."
    maya "I can go pick you up at one o'clock in the afternoon if you want."
    scene ch3ep1_87 with dissolve
    mc "......................"
    mc "No, I will go there by myself."
    mc "We shouldn't be seen with each other too often."
    scene ch3ep1_88 with dissolve
    maya "... Yeah, you're right about that."
    maya "That's all. See you tomorrow."
    scene ch3ep1_87 with dissolve
    mc "Sure. See you tomorrow."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_90 with dissolve
    u "Alright..."
    u "Let's get dressed and go to bed."
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    if ch2ep4hintheater == 1:
        jump ch3ep1krystaltalk
    else:
        scene black with dissolve
        $ renpy.pause()
        jump ch3ep1meetrowan
label ch3ep1krystaltalk:
    s "Next morning................"
    play music "sfx/ep4_1.mp3" fadein 3.0
    $ bgm = "Sapajou - Intención"
    scene ch3ep1_91 with dissolve
    u ".... It's already morning?"
    u "Well... That was fast. It feels like I just fell asleep not too long ago."
    u "Whatever.... Let's get up and go have some breakfast."
    scene ch3ep1_92 with dissolve
    s "*Door knocks*.............."
    u "Hm....?"
    mc "Who's it?"
    krystal "It's me, [krystal]. Can you open the door please?"
    mc "Sure. Wait a second."
    scene black with dissolve
    scene ch3ep1_93 with dissolve
    krystal "Hey..."
    mc "What's up?"
    krystal "Did you sleep well?"
    mc "Yes, I did. What about you?"
    scene ch3ep1_94 with dissolve
    krystal "I couldn't sleep well last night."
    krystal "I woke up in the middle of the night for three times."
    mc "Hm...? Why's that?"
    krystal "I have no idea..."
    krystal "May I come in, please?"
    mc "... Yeah, sure."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_95 with dissolve
    mc "So...."
    mc "What happened? Why did you wake up in the middle of the night so many times?"
    krystal "The first two times, I don't know the reason. I don't know what caused me to wake up."
    krystal "But, I remember the last time I woke up. I had a bad dream."
    scene ch3ep1_96 with dissolve
    mc "Bad dream? What was it about?"
    krystal "Do you remember me saying that I felt like we've met before?"
    mc "... Yeah, you used to say something like that."
    mc "But, what does that have to do something with your dream?"
    scene ch3ep1_97 with dissolve
    krystal "Because I saw you in my dream."
    mc "Hm...?"
    krystal "No. Actually, I don't think it was a dream. I felt like it was more likely my past memory."
    krystal "I was in somewhere that looked like an orphanage, but it also looked like a school as well."
    krystal "But, it wasn't an usual school. It felt much more different."
    scene ch3ep1_98 with dissolve
    mc "And...?"
    krystal "I remembered feeling so stress while heading to somewhere I had no idea of."
    krystal "Then, I saw a kid. He looked exactly like you."
    krystal "No, It's actually you. I'm sure."
    krystal "But when I was about to approach you, I got so much headaches that I woke up immediately."
    scene ch3ep1_99 with dissolve
    krystal "Ugh...!"
    krystal "Even for now I'm still having a headache for trying to think about it."
    krystal "I don't know what's wrong with me."
    scene ch3ep1_100 with dissolve
    u "I'm sure now that she was also adopted by [victor] just like me..."
    u "Well... this is totally unexpected. However, I'm not going to tell her the truth since it's better for her to know nothing about [victor]."
    mc "I've never met you and I've never been in such a place like that, [krystal]."
    mc "It was just a dream. I think you should just forget about it and move on."
    mc "Trying to think about it will only give you more headaches which isn't any good for you."
    scene ch3ep1_101 with dissolve
    krystal "You're right... It will only give me more headaches..."
    krystal "But, are you sure it was just a dream? It was so real that it felt like I used to be in that place before."
    mc "... Yeah, it must be just a dream. I swear I have no idea about that place at all, or maybe that kid wasn't me."
    mc "But even if it was true, what's the point in trying to remember that?"
    mc "Your life right now is perfect, isn't it? So, there is no need to remind yourself of the bad memories you wanted to forget."
    krystal "........................."
    krystal "... Yeah, you're right."
    scene ch3ep1_102 with dissolve
    mc "Alright..."
    mc "Instead of talking about that, why don't we go downstair and have some breakfast together?"
    mc "I'm so hungry right now."
    krystal "Oh, sure. Let's go then."
    scene black with dissolve
    $ renpy.pause()
    stop music fadeout 3.0
    jump ch3ep1meetrowan
label ch3ep1meetrowan:
    scene ch3ep1_103 with fade
    u "Okay...."
    u "It's about time. Let's go meet [rowan]."
    scene black with dissolve
    $ renpy.pause()
    s "*An hour later*..............."
    play music "sfx/ch1ep2.mp3"
    $ bgm = "Bensound - Little Idea"
    scene ch3ep1_104 with dissolve
    u "Alright...."
    u "I'm finally here."
    u "I saw a car parking in front of the house, I guess [maya] has also arrived as well."
    scene ch3ep1_105 with dissolve
    s "*Bell rings*............."
    rowan "Who's it?"
    mc "It's me, [mc]."
    rowan "Oh! Come on in! I've unlocked the door for you now."
    mc "Thank you."
    scene ch3ep1_106 with dissolve
    rowan "Good afternoon, [mc]."
    mc "Yeah... Good afternoon."
    scene ch3ep1_107 with dissolve
    rowan "Thank you for coming."
    mc "I should be the one saying that. Thank you for inviting me here."
    mc "Hello, [maya]. How long have you been here?"
    maya "Hi. Not that long actually. About fifteen minutes ago I guess."
    scene ch3ep1_108 with dissolve
    mc "... I'm sorry for being a little bit late."
    rowan "It's completely fine. Don't worry about that."
    mc "Thank you..."
    scene ch3ep1_109 with dissolve
    rowan "Alright, let's take a seat right over there."
    rowan "Then, we can have a talk later."
    mc "Sure thing."
    scene ch3ep1_110 with dissolve
    rowan "I heard everything from [maya] now."
    rowan "I never knew [victor] has been planning on taking the Xecon Gear's technology for so long."
    mc "Yeah, I know that. Sorry for causing you such a trouble."
    scene ch3ep1_111 with dissolve
    rowan "No. No. No. You don't have to feel sorry at all."
    rowan "Actually, I should be the one thanking you instead. For being honest and tell us the truth."
    rowan "At least we can now work together to prevent any more damage to the company."
    rowan "You've saved so many employees lives."
    mc "That still doesn't change the fact that I gave him a code of Xecon Gear."
    mc "I know that I'm able to sit here talking with you like this, because I'm [maya]'s son."
    mc "Otherwise, you'd have put me in jail already."
    rowan "........................"
    scene ch3ep1_112 with dissolve
    rowan "Well... I won't deny what you said."
    rowan "But, there is no need to overthink about that now."
    rowan "What's more important is, how are we going to do from now on."
    mc ".... Okay."
    rowan "By the way, can I ask you something?"
    rowan "I've been curious about this since I knew you were working for [victor]."
    scene ch3ep1_113 with dissolve
    mc "... Sure. Ask away."
    rowan "You know that you and [yui] got hired because two ex-employees resigned, right?"
    rowan "I wonder if those two happen to be working for [victor] now."
    mc "You have a great instinct."
    mc "Yeah, [victor] lobbied them with a higher position in order to get me in your company."
    mc "At first he tried to lobby just one person, but eventually ended up getting two."
    mc "They also brought some of Xecon codes with them."
    scene ch3ep1_114 with dissolve
    rowan "*Sighs*... I don't know what to say."
    rowan "Even though you already confirmed it, I still can't believe they betrayed me like that."
    rowan "I mean... they worked for Xecon for more than two years. I treat every employee like my own family. They were no-exception as well."
    mc "I'm sorry to say this, but it doesn't matter how well you treat them."
    mc "They went for more power and money. Easy as that."
    rowan "........................"
    scene black with dissolve
    $ renpy.pause()
    s "Some time passed..........."
    scene ch3ep1_115 with dissolve
    rowan "So...."
    rowan "You said [victor] give you a week in order to bring him the bluepring of Xecon."
    rowan "What's your plan right now?"
    scene ch3ep1_116 with dissolve
    mc "Um......."
    mc "Actually, there is a plan I've been thinking of."
    mc "But, I'm not sure if it's going to work."
    scene ch3ep1_117 with dissolve
    rowan "Hm? What's it?"
    mc "I think we should give [victor] the blueprint."
    rowan "What?! Are you serious? There is no way I'm going to give him the blueprint."
    maya "Yeah... That's not a good plan, [mc]."
    scene ch3ep1_118 with dissolve
    mc "Relax. I'm not telling you to give him the {b}real{/b} one."
    mc "I don't think one week is enough to take down [victor], so I'm asking you if it's possible to create a fake blueprint."
    mc "It must be the one that is hard to tell that it's fake."
    mc "The one that can buy us quite amount of time until he finds out that it's not real."
    maya "Oh... I think that sounds like a great idea."
    scene ch3ep1_119 with dissolve
    rowan "Umm...."
    rowan "A fake blueprint that is hard to be found out..."
    mc "What do you think?"
    scene ch3ep1_120 with dissolve
    rowan "Yeah, I also think it's a decent plan."
    rowan "But, I'm just trying to figure it out how I'm going to create it."
    rowan "We still have... five more days, right?"
    mc "Yeah..."
    scene ch3ep1_121 with dissolve
    rowan "Okay, let's stick with this plan."
    rowan "I'll try my best to make a fake blueprint for you."
    rowan "I'll give it to you once it's done."
    mc "Got it. Thank you."
    scene ch3ep1_122 with dissolve
    mc "Alright then, I guess that's it for today..."
    mc "Thank you for your time."
    rowan "Hm? Are you leaving already?"
    mc "Yeah? We're done talking now. Why?"
    scene ch3ep1_123 with dissolve
    rowan "It's almost evening now."
    mc "Yeah... And?"
    rowan "Why don't you stay and have dinner together?"
    maya "That sounds great! Let's stay for dinner before we leave, [mc]."
    mc ".... Okay."
    scene ch3ep1_124 with dissolve
    rowan "Perfect. Alright then, please wait here for a moment."
    rowan "I'm going to cook you guys dinner."
    maya "Do you need help?"
    rowan "Thanks, but it's okay. You guys are my guests."
    rowan "Please, make yourself at home."
    mc "... Thank you for your kindness."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time having dinner.............."
    scene ch3ep1_125 with dissolve
    mc "Thank you for the food, [rowan]."
    mc "It was very delicious. I never knew you were such a great chef."
    rowan "Nah... I'm still a newbie."
    maya "Such a humble young man you are..."
    maya "Anyways, I sincerely appreciate you for being kind to my son even after knowing everything."
    scene ch3ep1_126 with dissolve
    rowan "Well..."
    rowan "You gave me a helping hand when I was very hopeless."
    rowan "You showed your trust in me unconditionally when everyone else thought I was crazy."
    rowan "So, it's now time to show my trust in you and your son as well."
    maya "Thank you.... You're such a very good person."
    maya "Good bye for now, [rowan]."
    scene ch3ep1_125 with dissolve
    rowan "Yeah. Good bye for now, both of you."
    rowan "We're going through a rough time now. Please stay safe."
    mc "You, too...."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_127 with dissolve
    mc "Alright then...."
    mc "Good bye. Get home safe."
    maya "Are you going to go home by yourself?"
    maya "Do you want me to take you there?"
    scene ch3ep1_128 with dissolve
    mc "Thank you, but... we should part ways here."
    mc "Remember what I told you?"
    mc "I shouldn't be seen with each other any more often."
    maya "Oh... Okay...."
    scene ch3ep1_129 with dissolve
    mc "....................."
    mc "Good bye... ma-"
    mc "... Mom."
    maya "Hm?! W... What did you just say?! Say it again, please."
    scene ch3ep1_130 with dissolve
    mc "..................."
    mc "Good bye, mom."
    maya "*Smiles* Good bye, son! Get home safely!"
    mc ".................."
    mc "You, too."
    scene black with dissolve
    $ renpy.pause()
    if ch2ep1sexelaine == 1:
        jump ch3ep1elainedragged
    else:
        jump ch3ep1backfromrowan

label ch3ep1elainedragged:
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_131 with fade
    stop music fadeout 3.0
    u "Alright...."
    u "I've arrived at the central city."
    u "It's quite late at night now. Let's take a bus to go h-"
    scene ch3ep1_132 with dissolve
    unknown "Let me go!!"
    u "Hm....? What was that?"
    scene ch3ep1_133 with dissolve
    play music "sfx/ep2_8.mp3" fadein 3.0
    $ bgm = "Lahar - Genesis"
    elaine "I said... Let me go!!"
    elaine "How did you find me?!"
    elaine "I owe you nothing now! You can't do this!!"
    unknown "Stop being so stubborn and come with me already."
    unknown "Aren't you worried about mother?"
    elaine "You...!"
    scene black with dissolve
    scene ch3ep1_134 with dissolve
    s "*Door closed*............"
    unknown "Good girl... Listen to what I say and your mother will be fine."
    unknown "*Smirks* The night is still young. I can't wait to have fun with you all night long..."
    scene black with dissolve
    scene ch3ep1_135 with dissolve
    s "*Engine sounds*........."
    u "......................."
    scene ch3ep1_136 with dissolve
    u "Looks like [elaine] is in trouble...."
    u "What should I do?"
    menu:
        "Save her [elaine2]":
            $ ch3ep1helpelaine = 1
            $ elaine_ch3_ep1 += 2
            $ eliane_relationship += 2
            scene ch3ep1_138 with dissolve
            u "*Sighs*.............."
            u "Well, I can't ignore her just like that..."
            mc "Taxi...."
            stop music fadeout 3.0
            scene black with dissolve
            scene ch3ep1_139 with dissolve
            mc "I'll give you 300 dollars..."
            mc "Do you think you can follow the red Porsche that you just drove past?"
            dominic "It doesn't matter what's under a hood..."
            play music "sfx/ch3ep1_1.mp3" fadein 3.0
            $ bgm = "Don Omar Ft. Tego Calderon - Bandolero"
            scene ch3ep1_140 with dissolve
            dominic "The only thing that matters is who's behind the wheel."
            mc "......................."
            mc "..... Okay."
            mc "Then, don't make it suspicious. I don't want him to realise that he's being followed."
            scene ch3ep1_141 with dissolve
            dominic "I saw everything."
            dominic "The girl who was forced to get in that Porsche..."
            dominic "Is she your family?"
            mc "... No, she isn't my family. She's my friend."
            scene ch3ep1_142 with dissolve
            dominic "Friend? What is friend?"
            mc "What? Why are you asking such a question? Don't you have any friends?"
            dominic "No, I don't have friends. I have family..."
            mc "......................."
            mc "Whatever... this is not a time to talk about this. Hurry up and follow them."
            dominic "Okay...."
            scene ch3ep1_143 with dissolve
            s "*Tires sound*............."
            dominic "As you wish!"
            stop music fadeout 3.0
            scene black with dissolve
            $ renpy.pause()
            scene ch3ep1_144 with fade
            play music "sfx/ep2_8.mp3" fadein 3.0
            $ bgm = "Lahar - Genesis"
            dominic "There they are...."
            dominic "The alley he's driving in, is a dead end."
            mc "Hm? How did you know?"
            dominic "I know everything here. This is Brazil."
            mc "No, it's not...."
            scene ch3ep1_145 with dissolve
            mc "Alright...."
            mc "Thank you for taking me here."
            mc "This is 300 dollars as we agreed."
            dominic "It's alright. Just keep it back."
            scene ch3ep1_146 with dissolve
            mc "What? Why?"
            dominic "Money will come and go. We all know that. The most important thing in l-"
            mc "Okay. That's enough. I've got no time for this."
            mc "I'll leave your 300 dollars here."
            dominic "Alright then, good luck on saving your family."
            mc "Friend..."
            scene black with dissolve
            scene ch3ep1_147 with dissolve
            mc "......................."
            scene black with dissolve
            $ renpy.pause()
            scene ch3ep1_148 with fade
            elaine "Get away from me!"
            unknown "Come on.... I know you also want to do it."
            elaine "I want you to fuck me?! What the fuck are you talking about?! Are you high?!"
            unknown "*Smirks* Let's pick it up from where we left off in the past and enjoy our time together...."
            scene ch3ep1_149 with dissolve
            elaine "Stop it, [weston]."
            elaine "You can't do this to me!"
            elaine "I've paid for every cent me and my family owed you!"
            weston "No, darling. You can't escape from me..."
            scene ch3ep1_150 with dissolve
            s "*Door opened*............."
            weston "What the...?"
            scene ch3ep1_151 with dissolve
            mc "Get out of the car..."
            weston "Aw...!"
            scene ch3ep1_152 with dissolve
            weston "Ugh...!!"
            scene ch3ep1_153 with dissolve
            weston "What the fuck are you d-"
            scene ch3ep1_154 with dissolve
            weston "Hm...?"
            scene ch3ep1_155 with dissolve
            weston "Ouch...!!"
            scene ch3ep1_156 with dissolve
            weston "Who the fuck are y-"
            scene ch3ep1_157 with vpunch
            weston "Ouch...!!"
            scene ch3ep1_156 with dissolve
            weston "Why are you doing t-"
            scene ch3ep1_157 with vpunch
            weston "Ouch...!!"
            scene ch3ep1_156 with dissolve
            weston "Do you know who I-"
            scene ch3ep1_157 with vpunch
            weston "Ouch...!!"
            scene ch3ep1_156 with dissolve
            weston "You are messing with a wrong p-"
            scene ch3ep1_157 with vpunch
            weston "Ouch...!!"
            scene black with dissolve
            scene ch3ep1_158 with dissolve
            weston "....................."
            u "What...? He's passed out already...?"
            u "Well, that was fast. I was just getting started."
            scene ch3ep1_159 with dissolve
            elaine "[mc]...."
            mc "Hm...?"
            scene ch3ep1_160 with dissolve
            elaine "How did you get here?"
            mc "I was waiting for a bus to get home, then I saw you getting dragged by that guy."
            mc "It looked like you were in a trouble, so I decided to follow you here."
            mc "Sorry for sticking my nose in your business."
            scene ch3ep1_161 with dissolve
            elaine "No. No. Don't be."
            elaine "You haven't done anything wrong."
            elaine "Thank you for saving me."
            mc "You're welcome..."
            mc "By the way, are you alright?"
            scene ch3ep1_162 with dissolve
            elaine "Yes, I am."
            elaine "Fortunately, you came up right in time before he's done something to me."
            mc "Good to hear that."
            mc "Alright, let's leave here. I'm going to accompany you home."
            elaine "Okay, sure..."
            scene black with dissolve
            $ renpy.pause()
            stop music fadeout 3.0
            scene ch3ep1_163 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_163.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_163_blink.jpg", 1) with fade
            elaine "Thank you for taking me home, [mc]."
            mc "You're welcome."
            mc "Alright then, since you're safe now, I'm going to leave now."
            elaine "Hold on a sec...."
            mc "Hm...? What's wrong?"
            elaine "I'm very grateful for your help today..."
            elaine "Do you... want to have some coffee?"
            menu:
                "Yeah, sure. [elaine2]":
                    $ ch3ep1hwithelaine = 1
                    $ elaine_ch3_ep1 += 2
                    $ eliane_relationship += 2
                    scene ch3ep1_164 with dissolve
                    mc "Of course."
                    elaine "Alright then... Follow me in the house."
                    mc "Sure...."
                    jump ch3ep1elainefuck
                "Thanks, but no.":
                    $ ch3ep1hwithelaine = 2
                    scene ch3ep1_164_d with dissolve
                    mc "Thank you for inviting me in, but no I don't."
                    mc "It's very late at night now."
                    mc "I'm also very tired today."
                    mc "I should go home as soon as possible."
                    elaine "Oh... Okay then, good night."
                    mc "Bye."
                    scene black with dissolve
                    $ renpy.pause()
                    jump ch3ep1backfromrowan
        "Ignore them":
            $ ch3ep1helpelaine = 2
            scene ch3ep1_137_d with dissolve
            u "Whatever... It's none of my business."
            u "Right now, I've got a lot of things to deal with already."
            u "Let's not bring myself any more problem..."
            scene black with dissolve
            $ renpy.pause()
            jump ch3ep1backfromrowan
label ch3ep1elainefuck:
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
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_165 with fade
    elaine "*Kisses* Mhmm........."
    mc "*Kisses* W... Wait... [wendy] might see us here...."
    elaine "*Kisses* Mhhmm.... Don't worry... She's probably sleeping now...."
    elaine "*Kisses* Mhmmm.... But okay, Let's go to my room...."
    scene black with dissolve
    scene ch3ep1_166 with dissolve
    elaine "*Kisses* Mhmmm...."
    mc "*Kisses* Are you sure... you want to do it....?"
    elaine "*Kisses* Yeah, why not?"
    mc "*Kisses* I mean you just almost got...."
    scene ch3ep1_167 with dissolve
    elaine "I didn't want to do it because it was with him."
    elaine "But, if it's with you, I'm willing to."
    mc "Okay.... If you say so."
    elaine "Alright then, let's not waste any more time. Take off your clothes. I will take off mine as well."
    mc "Sure..."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_168 with dissolve
    elaine "Come. Kiss me again."
    elaine "You're the best kisser I've ever met."
    elaine "I want to feel the touch of your lips more."
    scene black with dissolve
    scene ch3ep1_169 with dissolve
    show ch3ep1_elaine1
    window hide
    elaine "*Kisses* Mhmmm.... As I said...."
    elaine "*Kisses* You really are the best kisser...."
    $ renpy.pause()
    hide ch3ep1_elaine1
    scene ch3ep1_170 with dissolve
    show ch3ep1_elaine2
    window hide
    elaine "*Kisses* Mhhmm... Your tongue.... tastes so good...."
    mc "*Kisses* So does yours...."
    $ renpy.pause()
    hide ch3ep1_elaine2
    scene black with dissolve
    scene ch3ep1_171 with dissolve
    elaine "*Giggles* Come on.... What are you waiting for...?"
    elaine "Hurry up and stick that cock of yours in my mouth already...."
    elaine "I can't wait to taste it again so badly...."
    scene ch3ep1_172 with dissolve
    mc "As you wish...."
    elaine "Mhmmm....."
    show ch3ep1_elaine3
    window hide
    elaine "*Sucks* Mhhmmm.... As expected.... Your cock is perfect...."
    elaine "*Sucks* The size.... The taste.... I love everything about it...."
    $ renpy.pause()
    mc "*Softly breathes* Suck it harder...."
    elaine "*Sucks* Mhmmm.... Hehe... Sure.... I thought you would never say that...."
    hide ch3ep1_elaine3
    scene ch3ep1_173 with dissolve
    show ch3ep1_elaine4
    window hide
    mc "*Softly breathes* Ah......"
    elaine "*Sucks* Mhmmm... Hard enough for you now...?"
    mc "*Softly breathes* Yeah.... Keep sucking it like that..."
    $ renpy.pause()
    hide ch3ep1_elaine4
    scene ch3ep1_174 with dissolve
    elaine "[mc]...."
    mc "Yes?"
    elaine "I can't hold it anymore. I want your cock inside me now."
    mc "Sure thing..."
    scene ch3ep1_175 with dissolve
    mc "Okay... I'm going to put it in now..."
    elaine "Yes, please..."
    show ch3ep1_elaine5
    $ renpy.pause(4, hard=True)
    hide ch3ep1_elaine5
    scene ch3ep1_176
    elaine "*Softly breathes* Ahh....."
    scene ch3ep1_177 with dissolve
    show ch3ep1_elaine6
    window hide
    elaine "*Softly breathes* Ahhh.... Yeah.... This is what I've been waiting for...."
    $ renpy.pause()
    elaine "*Softly breathes* Harder... [mc]. Fuck me harder...!"
    hide ch3ep1_elaine6
    scene ch3ep1_178 with dissolve
    show ch3ep1_elaine7
    window hide
    elaine "*Moans* Mhhmmm...! Yes....! Keep fucking me like that....!"
    elaine "*Moans* Ahh....! Don't stop...!!"
    $ renpy.pause()
    hide ch3ep1_elaine7
    scene ch3ep1_179 with dissolve
    show ch3ep1_elaine8
    window hide
    elaine "*Heavily breathes* Haahh...! I love you cock so much, [mc]...!"
    elaine "*Heavily breathes* Mhmmm...! I wish you could fuck me all night long...!"
    $ renpy.pause()
    hide ch3ep1_elaine8
    scene ch3ep1_180 with dissolve
    elaine "... What? Why did you stop...?"
    mc "Let's change a position..."
    elaine "Hm? How do you want to do it then?"
    mc "Turn around and lie on your stomach."
    elaine "*Giggles* As you wish, babe!"
    scene ch3ep1_181 with dissolve
    show ch3ep1_elaine9
    window hide
    mc "*Softly breathes* Ahh.... Your pussy is so tight...."
    mc "*Softly breathes* Especially in this position...."
    elaine "*Softly breathes* Arrrh.... Because your cock feels so good that I can't help, but squeeze my pussy...."
    $ renpy.pause()
    hide ch3ep1_elaine9
    scene ch3ep1_182 with dissolve
    show ch3ep1_elaine10
    window hide
    elaine "*Moans* Ahhh...!! Yes, [mc]...!!"
    elaine "*Moans* Mhhmmm.... You're driving me.... crazy with.... your cock...!!!"
    $ renpy.pause()
    hide ch3ep1_elaine10
    scene ch3ep1_183 with dissolve
    show ch3ep1_elaine11
    window hide
    elaine "*Heavily breathes* Arrh...! I've never felt this good for sooo long...!"
    elaine "*Heavily breathes* Mhmm...! Are you about to cum, [mc]...?!"
    mc "*Softly breathes*... No. not yet."
    $ renpy.pause()
    hide ch3ep1_elaine11
    scene ch3ep1_184 with dissolve
    elaine "*Softly breathes* Alright then... Let me do it."
    elaine "*Softly breathes* I'm going to cum before you if I let you continue...."
    elaine "*Softly breathes* I will take control and make us cum together."
    mc "Okay then...."
    scene black with dissolve
    scene ch3ep1_185 with dissolve
    show ch3ep1_elaine12
    window hide
    elaine "*Softly moans* Mhhm...... How does it feel?"
    mc "*Softly breathes* Great... But, it'd feel much better if you speed up a little bit...."
    $ renpy.pause()
    elaine "*Softly moans* As you wish...."
    hide ch3ep1_elaine12
    scene ch3ep1_186 with dissolve
    show ch3ep1_elaine13
    window hide
    mc "*Softly breathes* Yeah... Like that...."
    elaine "*Moans* Ahhh...!! Ahhh...!! Your cock is so long, [mc]...!"
    elaine "*Moans* It keeps touching my womb so hard right now...!"
    $ renpy.pause()
    hide ch3ep1_elaine13
    scene ch3ep1_187 with dissolve
    show ch3ep1_elaine14
    window hide
    elaine "*Heavily breathes* Mhmmm...!! I can't hold it anymore, [mc]...!"
    elaine "*Heavily breathes* I'm about to cum soon...!!"
    mc "*Softly breathes* Yeah... Almost..."
    elaine "*Heavily breathes* Go ahead...! Don't hold it...! Cum for me...!"
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch3ep1_elaine14
            jump ch3ep1elainemis1
        "Lying Doggy":
            hide ch3ep1_elaine14
            jump ch3ep1elainelying1
        "Slowest":
            hide ch3ep1_elaine14
            jump ch3ep1elainereverse1
        "Slower":
            hide ch3ep1_elaine14
            jump ch3ep1elainereverse2
        "Cum":
            jump ch3ep1elainecum
label ch3ep1elainemis1:
    scene ch3ep1_177 with dissolve
    show ch3ep1_elaine6
    window hide
    $ renpy.pause()
    menu:
        "Reverse Cowgirl":
            hide ch3ep1_elaine6
            jump ch3ep1elainereverse1
        "Lying Doggy":
            hide ch3ep1_elaine6
            jump ch3ep1elainelying1
        "Faster":
            hide ch3ep1_elaine6
            jump ch3ep1elainemis2
        "Fastest":
            hide ch3ep1_elaine6
            jump ch3ep1elainemis3
label ch3ep1elainemis2:
    scene ch3ep1_178 with dissolve
    show ch3ep1_elaine7
    window hide
    $ renpy.pause()
    menu:
        "Reverse Cowgirl":
            hide ch3ep1_elaine7
            jump ch3ep1elainereverse1
        "Lying Doggy":
            hide ch3ep1_elaine7
            jump ch3ep1elainelying1
        "Slower":
            hide ch3ep1_elaine7
            jump ch3ep1elainemis1
        "Faster":
            hide ch3ep1_elaine7
            jump ch3ep1elainemis3
label ch3ep1elainemis3:
    scene ch3ep1_179 with dissolve
    show ch3ep1_elaine8
    window hide
    $ renpy.pause()
    menu:
        "Reverse Cowgirl":
            hide ch3ep1_elaine8
            jump ch3ep1elainereverse1
        "Lying Doggy":
            hide ch3ep1_elaine8
            jump ch3ep1elainelying1
        "Slowest":
            hide ch3ep1_elaine8
            jump ch3ep1elainemis1
        "Slower":
            hide ch3ep1_elaine8
            jump ch3ep1elainemis2
label ch3ep1elainelying1:
    scene ch3ep1_181 with dissolve
    show ch3ep1_elaine9
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch3ep1_elaine9
            jump ch3ep1elainemis1
        "Reverse Cowgirl":
            hide ch3ep1_elaine9
            jump ch3ep1elainereverse1
        "Faster":
            hide ch3ep1_elaine9
            jump ch3ep1elainelying2
        "Fastest":
            hide ch3ep1_elaine9
            jump ch3ep1elainelying3
label ch3ep1elainelying2:
    scene ch3ep1_182 with dissolve
    show ch3ep1_elaine10
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch3ep1_elaine10
            jump ch3ep1elainemis1
        "Reverse Cowgirl":
            hide ch3ep1_elaine10
            jump ch3ep1elainereverse1
        "Slower":
            hide ch3ep1_elaine10
            jump ch3ep1elainelying1
        "Faster":
            hide ch3ep1_elaine10
            jump ch3ep1elainelying3
label ch3ep1elainelying3:
    scene ch3ep1_183 with dissolve
    show ch3ep1_elaine11
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch3ep1_elaine11
            jump ch3ep1elainemis1
        "Reverse Cowgirl":
            hide ch3ep1_elaine11
            jump ch3ep1elainereverse1
        "Slowest":
            hide ch3ep1_elaine11
            jump ch3ep1elainelying1
        "Slower":
            hide ch3ep1_elaine11
            jump ch3ep1elainelying2
label ch3ep1elainereverse1:
    scene ch3ep1_185 with dissolve
    show ch3ep1_elaine12
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch3ep1_elaine12
            jump ch3ep1elainemis1
        "Lying Doggy":
            hide ch3ep1_elaine12
            jump ch3ep1elainelying1
        "Faster":
            hide ch3ep1_elaine12
            jump ch3ep1elainereverse2
        "Fastest":
            hide ch3ep1_elaine12
            jump ch3ep1elainereverse3
label ch3ep1elainereverse2:
    scene ch3ep1_186 with dissolve
    show ch3ep1_elaine13
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch3ep1_elaine13
            jump ch3ep1elainemis1
        "Lying Doggy":
            hide ch3ep1_elaine13
            jump ch3ep1elainelying1
        "Slower":
            hide ch3ep1_elaine13
            jump ch3ep1elainereverse1
        "Faster":
            hide ch3ep1_elaine13
            jump ch3ep1elainereverse3
label ch3ep1elainereverse3:
    scene ch3ep1_187 with dissolve
    show ch3ep1_elaine14
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch3ep1_elaine14
            jump ch3ep1elainemis1
        "Lying Doggy":
            hide ch3ep1_elaine14
            jump ch3ep1elainelying1
        "Slowest":
            hide ch3ep1_elaine14
            jump ch3ep1elainereverse1
        "Slower":
            hide ch3ep1_elaine14
            jump ch3ep1elainereverse2
        "Cum":
            jump ch3ep1elainecum
label ch3ep1elainecum:
    mc "*Softly breathes* I'm about to cum...."
    elaine "*Heavily breathes* Inside! I want you to cum inside me!"
    menu:
        "Cum inside":
            hide ch3ep1_elaine14
            scene ch3ep1_188_in with vpunch
            mc "Ugh... I'm cumming...."
            scene ch3ep1_188_in with vpunch
            $ renpy.pause()
        "Cum outside":
            hide ch3ep1_elaine14
            scene ch3ep1_188_out with vpunch
            mc "Ugh... I'm cumming...."
            scene ch3ep1_188_out with vpunch
            $ renpy.pause()
    scene ch3ep1_189 with vpunch
    elaine "*Moans* Ahhhh~~! Me, too~~~~!!"
    elaine "*Moans* I-I have never cum so hard like this before~~!!"
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_190 with dissolve
    elaine "*Pants* Having sex with you... is always the best...."
    elaine "*Pants* I enjoyed it pretty much...."
    mc "Glad to hear that...."
    if ch2ep3caughth == 1:
        $ ch3ep1_threesome = 1
        jump ch3ep1threesome
    else:
        $ renpy.end_replay()
        jump ch3ep1leaveelainehouse
label ch3ep1threesome:
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
    scene ch3ep1_191 with dissolve
    elaine "What are you doing out there?"
    elaine "*Giggles* Stop hiding and come on in."
    u "Hm...? Who's she talking to?"
    scene ch3ep1_192 with dissolve
    elaine "There is no need to hide anymore."
    elaine "I know you've been peeking on us."
    elaine "*Giggles* Just come in and have fun together."
    mc "........................"
    scene ch3ep1_193 with dissolve
    s "*Door opens*.............."
    wendy "....................."
    wendy "How did you know....?"
    scene ch3ep1_194 with dissolve
    elaine "I saw the door was softly opened while I was riding his dick."
    elaine "That's when I knew it was you."
    wendy "I'm sorry. I didn't mean to peek on you guys. I thought you weren't home yet, then I heard a strange voice."
    wendy "So, I just came to check... I didn't know you guys were.... having a good time...."
    scene ch3ep1_195 with dissolve
    elaine "No. No. No. There is no need to be sorry about."
    elaine "I don't mind being seen by you."
    wendy "Okay then... I'm going to leave now... Enjoy your time."
    elaine "Wait. Where are you going?"
    elaine "Since you're already here, why don't we have some fun together?"
    wendy "But...."
    scene ch3ep1_196 with dissolve
    elaine "*Kisses* Say no more...."
    wendy "*Kisses* Mhmmm....?!"
    elaine "*Kisses* It's okay... Just relax.... and let yourself enjoy the moment..."
    wendy "*Kisses*......................."
    scene ch3ep1_197 with dissolve
    elaine "See? It was great, right?"
    wendy "....................."
    wendy ".... Yeah."
    elaine "Then, what are you waiting for? Take off your clothes already..."
    wendy "....................."
    elaine "Come on... Don't be shy... It's not like we haven't seen each other naked before...."
    wendy "Okay....."
    scene ch3ep1_198 with dissolve
    elaine "*Giggles* Look who's the one enjoying the most...."
    elaine "He just came not too long ago, but looks like he's ready for another round now."
    mc "Well.... You can't blame me though."
    elaine "*Giggles* Yeah, I know that."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_199 with dissolve
    elaine "Alright... Shall we start now?"
    elaine "Don't be shy. Lick it, [wendy]."
    wendy ".... Okay."
    scene ch3ep1_200 with dissolve
    show ch3ep1_threesome1
    window hide
    wendy "*Licks* It's a little bit bitter and harsh to the taste..."
    elaine "*Licks* Taste like a semen, right?"
    wendy "*Licks* Yeah... But, I guess it's because he just came..."
    $ renpy.pause()
    hide ch3ep1_threesome1
    scene ch3ep1_201 with dissolve
    show ch3ep1_threesome2
    window hide
    wendy "*Sucks* Mhmm......"
    elaine "*Licks* Arr......"
    $ renpy.pause()
    hide ch3ep1_threesome2
    scene ch3ep1_202 with dissolve
    show ch3ep1_threesome3
    $ renpy.pause(4, hard=True)
    hide ch3ep1_threesome3
    scene ch3ep1_203
    wendy "*Softly moans* Ahhhh......"
    scene ch3ep1_204 with dissolve
    show ch3ep1_threesome4
    window hide
    wendy "*Softly moans* Mhhmm.... It's so big...."
    elaine "*Softly moans* Arr... He's got such a nice dick, right?"
    elaine "*Giggles* Unlike your ex...."
    wendy "*Softly moans* Mhmmm... Stop.... I don't want to... Ahh.... hear anything about.... Mhmmm.... that asshole again..."
    $ renpy.pause()
    hide ch3ep1_threesome4
    scene ch3ep1_205 with dissolve
    show ch3ep1_threesome5
    window hide
    elaine "*Softly moans* Ahhh.... Yeah..... Keep licking my pussy just like that...."
    elaine "*Softly moans* Mhhm..... Have you ever had a threesome before, [mc]?"
    mc "*Licks*........................"
    elaine "*Softly moans* Hehe.... I bet you must feel like being in a heaven hehe...."
    $ renpy.pause()
    hide ch3ep1_threesome5
    scene ch3ep1_206 with dissolve
    show ch3ep1_threesome6
    window hide
    wendy "*Softly breathes* Ahhh.... [mc]....."
    wendy "*Softly breathes* Mhmm.... It feels so good...."
    $ renpy.pause()
    hide ch3ep1_threesome6
    scene black with dissolve
    scene ch3ep1_207 with dissolve
    elaine "*Giggles* Aw....!"
    show ch3ep1_threesome7
    window hide
    elaine "*Giggles* I never knew you had this aggressive side in you...."
    mc "*Softly breathes* Now you know...."
    $ renpy.pause()
    hide ch3ep1_threesome7
    scene ch3ep1_208 with dissolve
    show ch3ep1_threesome8
    window hide
    wendy "*Softly moans* Ahhh.... W... What's this....?"
    wendy "*Softly moans* Mhhmm.... You aren't even putting.... your cock inside my pussy, but.. why does it feel.... ahhh.... so good like this...?"
    $ renpy.pause()
    hide ch3ep1_threesome8
    scene ch3ep1_209 with dissolve
    show ch3ep1_threesome9
    window hide
    elaine "*Softly breathes* Y... Yeah.... Babe.... Don't stop....."
    wendy "*Moans* Mhhm.... S... Stop teasing me.... And put that cock of yours inside my pussy already...."
    $ renpy.pause()
    hide ch3ep1_threesome9
    scene ch3ep1_210 with dissolve
    mc "Alright.... As you wish."
    show ch3ep1_threesome10
    window hide
    wendy "*Softly breathes* Mhhhm.... Y.... Yeah.... Finally....."
    elaine "*Softly breathes* Arrrh......"
    $ renpy.pause()
    hide ch3ep1_threesome10
    scene ch3ep1_211 with dissolve
    show ch3ep1_threesome11
    window hide
    wendy "*Moans* Ahhh....! Yes...! Yes....!"
    elaine "*Softly breathes* Y... Yeah...! Mhhhm....! Deeper...! Put your finger inside my pussy deeper!"
    $ renpy.pause()
    hide ch3ep1_threesome11
    scene ch3ep1_212 with dissolve
    show ch3ep1_threesome12
    window hide
    wendy "*Heavily breathes* Haahh....! I... I'm.... getting there....!"
    elaine "*Softly breathes* Mhmmm....."
    $ renpy.pause()
    hide ch3ep1_threesome12
    scene ch3ep1_213 with dissolve
    elaine "........................"
    mc "... Why are you staring at me like that?"
    elaine "Don't fuck just her. I want you to fuck me, too...."
    mc "Alright then, swap your position...."
    scene black with dissolve
    scene ch3ep1_214 with dissolve
    show ch3ep1_threesome13
    window hide
    mc "Are you satisfied now...?"
    elaine "*Softly breathes* Mhmmm... Not yet...."
    $ renpy.pause()
    hide ch3ep1_threesome13
    scene ch3ep1_215 with dissolve
    show ch3ep1_threesome14
    window hide
    elaine "*Moans* Y... Yeah...! I like this...! Keep fucking me hard....!"
    wendy "*Moans* Mhhhmmmm~~"
    $ renpy.pause()
    hide ch3ep1_threesome14
    scene ch3ep1_216 with dissolve
    show ch3ep1_threesome15
    window hide
    elaine "*Heavily breathes* Ahh....! Mhhhmmm....! I'm about to cum soon....!"
    wendy "*Heavily breathes* Y... Yeah...! Me, too....! I can't hold it any longer....!"
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep1_threesome15
            jump ch3ep1_threesomecow1
        "Intercrural Sandwich":
            hide ch3ep1_threesome15
            jump ch3ep1_sandwich1
        "Doggy (Wendy)":
            hide ch3ep1_threesome15
            jump ch3ep1_threesomedoggywendy1
        "Slowest":
            hide ch3ep1_threesome15
            jump ch3ep1_threesomedoggy1
        "Slower":
            hide ch3ep1_threesome15
            jump ch3ep1_threesomedoggy2
        "Cum":
            jump ch3ep1threesomecum
label ch3ep1_threesomecow1:
    scene ch3ep1_204 with dissolve
    show ch3ep1_threesome4
    window hide
    $ renpy.pause()
    menu:
        "Doggy (Wendy)":
            hide ch3ep1_threesome4
            jump ch3ep1_threesomedoggywendy1
        "Doggy (Elaine)":
            hide ch3ep1_threesome4
            jump ch3ep1_threesomedoggyelaine1
        "Intercrural Sandwich":
            hide ch3ep1_threesome4
            jump ch3ep1_sandwich1
        "Faster":
            hide ch3ep1_threesome4
            jump ch3ep1_threesomecow2
        "Fastest":
            hide ch3ep1_threesome4
            jump ch3ep1_threesomecow3
label ch3ep1_threesomecow2:
    scene ch3ep1_205 with dissolve
    show ch3ep1_threesome5
    window hide
    $ renpy.pause()
    menu:
        "Doggy (Wendy)":
            hide ch3ep1_threesome5
            jump ch3ep1_threesomedoggywendy1
        "Doggy (Elaine)":
            hide ch3ep1_threesome5
            jump ch3ep1_threesomedoggyelaine1
        "Intercrural Sandwich":
            hide ch3ep1_threesome5
            jump ch3ep1_sandwich1
        "Slower":
            hide ch3ep1_threesome5
            jump ch3ep1_threesomecow1
        "Faster":
            hide ch3ep1_threesome5
            jump ch3ep1_threesomecow3
label ch3ep1_threesomecow3:
    scene ch3ep1_206 with dissolve
    show ch3ep1_threesome6
    window hide
    $ renpy.pause()
    menu:
        "Doggy (Wendy)":
            hide ch3ep1_threesome6
            jump ch3ep1_threesomedoggywendy1
        "Doggy (Elaine)":
            hide ch3ep1_threesome6
            jump ch3ep1_threesomedoggyelaine1
        "Intercrural Sandwich":
            hide ch3ep1_threesome6
            jump ch3ep1_sandwich1
        "Slowest":
            hide ch3ep1_threesome6
            jump ch3ep1_threesomecow1
        "Slower":
            hide ch3ep1_threesome6
            jump ch3ep1_threesomecow2
label ch3ep1_sandwich1:
    scene ch3ep1_207 with dissolve
    show ch3ep1_threesome7
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep1_threesome7
            jump ch3ep1_threesomecow1
        "Doggy (Wendy)":
            hide ch3ep1_threesome7
            jump ch3ep1_threesomedoggywendy1
        "Doggy (Elaine)":
            hide ch3ep1_threesome7
            jump ch3ep1_threesomedoggyelaine1
        "Faster":
            hide ch3ep1_threesome7
            jump ch3ep1_sandwich2
        "Fastest":
            hide ch3ep1_threesome7
            jump ch3ep1_sandwich3
label ch3ep1_sandwich2:
    scene ch3ep1_208 with dissolve
    show ch3ep1_threesome8
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep1_threesome8
            jump ch3ep1_threesomecow1
        "Doggy (Wendy)":
            hide ch3ep1_threesome8
            jump ch3ep1_threesomedoggywendy1
        "Doggy (Elaine)":
            hide ch3ep1_threesome8
            jump ch3ep1_threesomedoggyelaine1
        "Slower":
            hide ch3ep1_threesome8
            jump ch3ep1_sandwich1
        "Faster":
            hide ch3ep1_threesome8
            jump ch3ep1_sandwich3
label ch3ep1_sandwich3:
    scene ch3ep1_209 with dissolve
    show ch3ep1_threesome9
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep1_threesome9
            jump ch3ep1_threesomecow1
        "Doggy (Wendy)":
            hide ch3ep1_threesome9
            jump ch3ep1_threesomedoggywendy1
        "Doggy (Elaine)":
            hide ch3ep1_threesome9
            jump ch3ep1_threesomedoggyelaine1
        "Slowest":
            hide ch3ep1_threesome9
            jump ch3ep1_sandwich1
        "Slower":
            hide ch3ep1_threesome9
            jump ch3ep1_sandwich2
label ch3ep1_threesomedoggywendy1:
    scene ch3ep1_210 with dissolve
    show ch3ep1_threesome10
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep1_threesome10
            jump ch3ep1_threesomecow1
        "Intercrural Sandwich":
            hide ch3ep1_threesome10
            jump ch3ep1_sandwich1
        "Doggy (Elaine)":
            hide ch3ep1_threesome10
            jump ch3ep1_threesomedoggyelaine1
        "Faster":
            hide ch3ep1_threesome10
            jump ch3ep1_threesomedoggywendy2
        "Fastest":
            hide ch3ep1_threesome10
            jump ch3ep1_threesomedoggywendy3
label ch3ep1_threesomedoggywendy2:
    scene ch3ep1_211 with dissolve
    show ch3ep1_threesome11
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep1_threesome11
            jump ch3ep1_threesomecow1
        "Intercrural Sandwich":
            hide ch3ep1_threesome11
            jump ch3ep1_sandwich1
        "Doggy (Elaine)":
            hide ch3ep1_threesome11
            jump ch3ep1_threesomedoggyelaine1
        "Slower":
            hide ch3ep1_threesome11
            jump ch3ep1_threesomedoggywendy1
        "Faster":
            hide ch3ep1_threesome11
            jump ch3ep1_threesomedoggywendy3
label ch3ep1_threesomedoggywendy3:
    scene ch3ep1_212 with dissolve
    show ch3ep1_threesome12
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep1_threesome12
            jump ch3ep1_threesomecow1
        "Intercrural Sandwich":
            hide ch3ep1_threesome12
            jump ch3ep1_sandwich1
        "Doggy (Elaine)":
            hide ch3ep1_threesome12
            jump ch3ep1_threesomedoggyelaine1
        "Slowest":
            hide ch3ep1_threesome12
            jump ch3ep1_threesomedoggywendy1
        "Slower":
            hide ch3ep1_threesome12
            jump ch3ep1_threesomedoggywendy2
label ch3ep1_threesomedoggyelaine1:
    scene ch3ep1_214 with dissolve
    show ch3ep1_threesome13
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep1_threesome13
            jump ch3ep1_threesomecow1
        "Intercrural Sandwich":
            hide ch3ep1_threesome13
            jump ch3ep1_sandwich1
        "Doggy (Wendy)":
            hide ch3ep1_threesome13
            jump ch3ep1_threesomedoggywendy1
        "Faster":
            hide ch3ep1_threesome13
            jump ch3ep1_threesomedoggyelaine2
        "Fastest":
            hide ch3ep1_threesome13
            jump ch3ep1_threesomedoggyelaine3
label ch3ep1_threesomedoggyelaine2:
    scene ch3ep1_215 with dissolve
    show ch3ep1_threesome14
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep1_threesome14
            jump ch3ep1_threesomecow1
        "Intercrural Sandwich":
            hide ch3ep1_threesome14
            jump ch3ep1_sandwich1
        "Doggy (Wendy)":
            hide ch3ep1_threesome14
            jump ch3ep1_threesomedoggywendy1
        "Slower":
            hide ch3ep1_threesome14
            jump ch3ep1_threesomedoggyelaine1
        "Faster":
            hide ch3ep1_threesome14
            jump ch3ep1_threesomedoggyelaine3
label ch3ep1_threesomedoggyelaine3:
    scene ch3ep1_216 with dissolve
    show ch3ep1_threesome15
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch3ep1_threesome15
            jump ch3ep1_threesomecow1
        "Intercrural Sandwich":
            hide ch3ep1_threesome15
            jump ch3ep1_sandwich1
        "Doggy (Wendy)":
            hide ch3ep1_threesome15
            jump ch3ep1_threesomedoggywendy1
        "Slowest":
            hide ch3ep1_threesome15
            jump ch3ep1_threesomedoggy1
        "Slower":
            hide ch3ep1_threesome15
            jump ch3ep1_threesomedoggy2
        "Cum":
            jump ch3ep1threesomecum
label ch3ep1threesomecum:
    elaine "*Moans* Ahhh....! Let's cum together...!"
    wendy "*Moans* Y... Yeah...!"
    menu:
        "Cum on [elaine]'s butt":
            $ ch3ep1_threesomecum = 1
            hide ch3ep1_threesome15
            scene ch3ep1_217_elaine1 with vpunch
            mc "Ugh...!!"
            wendy "I'm cumming~~!!!"
            elaine "Ahhhhh~~!!"
            scene ch3ep1_217_elaine2 with dissolve
            elaine "*Pants* Hehe... That felt very good....."
            wendy "*Pants*................"
        "Cum on [wendy]'s butt":
            $ ch3ep1_threesomecum = 2
            hide ch3ep1_threesome15
            scene ch3ep1_217_wendy1 with vpunch
            mc "Ugh...!!"
            wendy "I'm cumming~~!!!"
            elaine "Ahhhhh~~!!"
            scene ch3ep1_217_wendy2 with dissolve
            elaine "*Pants* Hehe... That felt very good....."
            wendy "*Pants*................"
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*.........."
    scene ch3ep1_218 with dissolve
    elaine "*Smiles* That was the best threesome I've ever had...."
    elaine "*Smiles* It was the first time I wanted to do myself...."
    mc "I'm glad to hear that..."
    if ch3ep1_threesomecum == 1:
        scene ch3ep1_219_a with dissolve
    elif ch3ep1_threesomecum == 2:
        scene ch3ep1_219_b with dissolve
    elaine "What about you, [wendy]?"
    wendy "......................"
    elaine "[wendy]...?"
    wendy "......................"
    elaine "*Giggles* Looks like it felt so good for her that she's already passed out...."
    mc "I think so..."
    $ renpy.end_replay()
    scene black with dissolve
    $ renpy.pause()
    $ elaine_ch3_ep1 += 2
    $ eliane_relationship += 2
    $ wendy_ch3_ep1 += 4
    $ wendy_relationship += 4
    s "*Five minutes later*............"
    jump ch3ep1leaveelainehouse
label ch3ep1leaveelainehouse:
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_220 with dissolve
    mc "Alright... It's already late."
    mc "I'm going to leave now."
    elaine "Thank you for today."
    mc "... You're welcome."
    scene ch3ep1_221 with dissolve
    elaine "... Are you not going to ask me about what happened today?"
    mc "No. I'm not."
    elaine "Why's that? Are you not curious?"
    mc "It's your problem.... And if you wanted to tell me, you would've done that already."
    scene ch3ep1_222 with dissolve
    elaine "Actually, I wanted to..."
    elaine "But, I'm not ready yet...."
    mc "It's okay. Don't force yourself."
    elaine "... Thanks."
    scene ch3ep1_223 with dissolve
    mc "Alright then, good bye."
    elaine "Bye. Get home saftely."
    elaine "Have a good night."
    mc "You, too."
    scene black with dissolve
    $ renpy.pause()
    jump ch3ep1backfromrowan
label ch3ep1backfromrowan:
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    scene ch3ep1_224 with fade
    u "It's pretty late right now...."
    u "I don't feel like taking a shower tonight."
    u "Let's just go to bed..."
    scene black with dissolve
    $ renpy.pause()
    s "Next morning.........."
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene ch3ep1_225 with fade
    u "Alright....."
    u "Let's have some breakfast before going to work."
    unknown "Good morning, [mc]."
    u "Hm...?"
    scene ch3ep1_226 with dissolve
    mc "Oh... It's you."
    mc "Good morning."
    zeke "Going for breakfast, huh?"
    scene ch3ep1_227 with dissolve
    mc "Yeah. What about you?"
    zeke "I've already had it."
    mc "I see... And why are you sitting alone? Where's [mika]?"
    zeke "She has to go to a field trip with her school."
    zeke "So, she already left the house in the early morning."
    mc "I see...."
    scene ch3ep1_228 with dissolve
    zeke "Great news for you. She's not going to be around for five days."
    zeke "So, I can take you guys to the company this week."
    mc "Wow...."
    zeke "Alright, I'm not going to hold you here any longer. Go have your breakfast."
    scene ch3ep1_229 with dissolve
    u "Okay......"
    u "Let's find something to eat...."
    scene black with dissolve
    $ renpy.pause()
    jump ch3ep1part2

label ch3ep1part2:
    scene black with dissolve
    $ renpy.pause()
    s "You spent time working at the company until lunchtime...."
    scene ch3ep1_230 with fade
    play music "sfx/ch2ep2_2.mp3" fadein 3.0
    $ bgm = "Roa Music - Summer Days"
    joe "Finally! It's lunchtime guys! Let's go find something to eat!"
    leo "Sure thing! I didn't have breakfast today. I'm starving right now."
    liam "How's the work I gave you this morning, [mc]? Is it finished now?"
    mc "Almost. Just a couple things left. I will submit it to you this afternoon."
    liam "Good to know that."
    if ch2ep4takefayehome == 1:
        scene ch3ep1_231 with dissolve
        leo "Oh...?"
        faye "Hm...?"
        scene ch3ep1_232 with dissolve
        leo "Hi, [faye]! How are you?"
        joe "Hello, [faye]."
        faye "I'm good. Thanks for asking."
        leo "Why are you coming to our department?"
        scene ch3ep1_233 with dissolve
        leo "Could it be that... you are going to invite me for lunch, right?!"
        faye "......................."
        faye "No, I'm just looking for [mc]."
        u "Hm...?"
        leo "Aw...."
        scene ch3ep1_234 with dissolve
        mc "[faye]..."
        faye "Oh, there you are."
        faye "Hello, [liam]. Hi, [david]."
        liam "Hello."
        david "Hi."
        scene ch3ep1_235 with dissolve
        faye "Are you guys going for lunch together?"
        leo "Yes, we are."
        faye "I see... Can I have [mc] for a moment, please?"
        faye "It won't take long."
        liam "Sure thing. We'll be waiting in front of the elevator. Take your time."
        faye "Thank you."
        scene black with dissolve
        scene ch3ep1_236 with dissolve
        mc "How's your condition?"
        mc "Are you better now?"
        faye "Yeah, I'm completely fine now."
        faye "Thank you for taking care of me when I was sick."
        scene black with dissolve
        scene ch3ep1_237 with dissolve
        leo "*Sighs* Of course it's [mc] again...."
        leo "I don't understand why girls are going after him."
        leo "He's just a boring guy with no emotion."
        scene ch3ep1_238 with dissolve
        liam "But, I think that's what makes him different though."
        joe "*Laughs* You're just jealous of him, aren't you?"
        leo "No, I'm not! What are you talking about?"
        leo "I just feel pity for the girls for wasting their time..."
        joe "*Laughs* Yeah, you're jealous of him."
        leo "..................."
        scene black with dissolve
        scene ch3ep1_239 with dissolve
        mc "By the way....."
        mc "Why were you looking for me?"
        faye "Are you free this evening?"
        mc "... Why do you ask?"
        scene ch3ep1_240 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_240.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_240_blink.jpg", 1) with dissolve
        faye "I'd like to invite you for dinner at my house."
        mc "Your house? Why not in a restaurant?"
        faye "I appreciated your kindness from last time, so I want to cook dinner for you myself."
        faye "What do you say?"
        menu:
            "Accept her invitation. [faye1]":
                $ ch3ep1_fayeinvite = 1
                $ faye_relationship += 1
                $ faye_ch3_ep1 += 1
                mc "Sure, I'd be happy to have dinner with you."
                scene ch3ep1_241 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_241.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_241_blink.jpg", 1) with dissolve
                faye "*Smiles* I'm glad to hear that."
                faye "Wait for me at the in front of the company at ten past five."
                faye "I'll pick you up there."
                mc "Okay, sure."
                faye "Alright then, I'm not going to take any more of your time."
                faye "See you this evening."
                mc "Yeah, see you."
            "Turn down her invitation.":
                $ ch3ep1_fayeinvite = 2
                mc "Thank you for inviting me, but..."
                mc "I've been very busy lately, so I don't think I can have dinner with you today."
                scene ch3ep1_242 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_242.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_242_blink.jpg", 1) with dissolve
                faye "... Is that so?"
                mc "Yeah... I'm so sorry."
                faye "What a pity..."
                faye "Alright then, I'm going to take any more of your time."
                faye "See you later."
                mc "... Bye."
        scene black with dissolve
        scene ch3ep1_243 with dissolve
        liam "Are you guys done talking?"
        mc "Yeah. Sorry to have kept you guys waiting."
        liam "No worries at all. Shall we go now?"
        mc "Sure, let's go."
        scene black with dissolve
        $ renpy.pause()
        s "You spent your time having lunch with your colleagues....."
        scene ch3ep1_244 with fade
        leo "Alright guys... It's time for work again."
        joe "*Sighs* Yeah... Time sure flies so fast when you're having a good time."
        liam "*Laughs* I agree with you on that."
        if ch3ep1helpelaine == 1:
            scene ch3ep1_245 with dissolve
            s "*Phone rings*................"
            u "Hm...?"
            scene ch3ep1_246 with dissolve
            mc "I've got a phone call."
            mc "You guys can go first. No need to wait for me."
            liam "Okay then, see you in the department."
            mc "Yeah, sure."
            scene black with dissolve
            scene ch3ep1_247 with dissolve
            mc "Hi, [elaine]."
            mc "....................."
            mc "Right now?"
            mc "....................."
            mc "Okay. Where are you?"
            mc "....................."
            mc "Alright, got it. I'll be there soon."
            scene black with dissolve
            scene ch3ep1_248 with dissolve
            u "Her voice was shaking. She sounded nervous."
            u "Almost like she was bracing herself for something."
            u "There must be something extremely wrong on her end."
            u "Let's hurry up and get there."
            jump ch3ep1_elaineroof
        else:
            jump ch3ep1part2continue
    else:
        scene black with dissolve
        $ renpy.pause()
        s "You spent time having lunch with your colleagues...."
        scene ch3ep1_244 with fade
        leo "Alright guys... It's time for work again."
        joe "*Sighs* Yeah... Time sure flies so fast when you're having a good time."
        liam "*Laughs* I agree with you on that."
        if ch3ep1helpelaine == 1:
            scene ch3ep1_245 with dissolve
            s "*Phone rings*................"
            u "Hm...?"
            scene ch3ep1_246 with dissolve
            mc "I've got a phone call."
            mc "You guys can go first. No need to wait for me."
            liam "Okay then, see you in the department."
            mc "Yeah, sure."
            scene black with dissolve
            scene ch3ep1_247 with dissolve
            mc "Hi, [elaine]."
            mc "....................."
            mc "Right now?"
            mc "....................."
            mc "Okay. Where are you?"
            mc "....................."
            mc "Alright, got it. I'll be there soon."
            scene black with dissolve
            scene ch3ep1_248 with dissolve
            u "Her voice was shaking. She sounded nervous."
            u "Almost like she was bracing herself for something."
            u "There must be something extremely wrong on her end."
            u "Let's hurry up and get there."
            jump ch3ep1_elaineroof
        else:
            jump ch3ep1part2continue
label ch3ep1_elaineroof:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep.3/ep3_7.mp3" fadein 3.0
    $ bgm = "Jeff II - Heartfül of Kerøsene"
    scene ch3ep1_249 with fade
    mc "..................."
    u "This is the place.... She told me that she was coming to the rooftop of this building."
    u "But where is she right n-"
    scene ch3ep1_250 with dissolve
    elaine "Get away from me!!"
    u "Hm...?"
    scene ch3ep1_251 with dissolve
    elaine "No, please! Let me go!"
    weston "No one is going to save you today!"
    weston "You can't escape from me, bitch! Hahaha!"
    u "*Sighs* Here we go again...."
    u "Now I know why she sounded so shaken on the phone."
    u "Alright, let's finish this real quick."
    scene black with dissolve
    scene ch3ep1_252 with dissolve
    mc "I know that you're horny, but to try raping a girl in a place like this...."
    mc "You're very desperate..."
    weston "Fuck!? It's you again?"
    weston "How did you know that we were here?!"
    elaine "[mc]! Help me, please!"
    scene ch3ep1_253 with dissolve
    weston "Well, I half expected you to show up and save this bitch."
    weston "So, I've brought some friends for you to play with."
    weston "Guys, get that bastard out of my face. Don't let him interrupt me."
    weston "And I'll let let you have fun with this bitch after I'm done."
    marc "Got it."
    scene ch3ep1_254 with dissolve
    marc "You heard him. Get the fuck out of here, kid."
    mc "...................."
    marc "Let's make it easy for both of us."
    marc "Turn around and walk away so we don't waste our energy and you don't get hurt."
    scene ch3ep1_255 with dissolve
    mc "Get your hands off of me. I won't say it twice."
    marc "*Giggles* Shit... You scared the hell out of me."
    marc "What if I don't? What are you going to do, kid?"
    marc "Look at you... You're skinny as hell. Do you even lift, ki-"
    scene ch3ep1_256 with vpunch
    marc "Ouch...!"
    adam "Woah! What the fuck...!?"
    scene ch3ep1_257 with dissolve
    adam "You fucking asshole!"
    scene ch3ep1_258 with dissolve
    mc "................."
    adam "Wha-"
    scene ch3ep1_259 with vpunch
    adam "Ugh!!"
    scene ch3ep1_260 with dissolve
    adam "Fuck... My leg...."
    mc "....................."
    scene ch3ep1_261 with vpunch
    adam "Ouch!!!"
    scene black with dissolve
    scene ch3ep1_262 with dissolve
    mc "Now, it's your turn."
    weston "What the fuck...?!"
    weston "How did you...?! This can't be real!"
    mc "......................"
    scene ch3ep1_263 with dissolve
    weston "No! Don't get any closer!"
    weston "Stop right there!"
    mc "Get up, or I'm gonna kick your ass."
    elaine "Kick his fucking ass, [mc]!"
    weston "Okay! Okay! I will get up now!"
    scene ch3ep1_264 with dissolve
    weston "I surrender. Please don't hurt me."
    elaine "Now you're begging, huh?!"
    weston "Why are you doing this? You aren't even her boyfriend!"
    weston "How much do I have to pay you to just leave us alone? T-Tell me the number!"
    elaine "Y... You fucking piece of shit!"
    mc "Step away, [elaine]."
    elaine "Hm...? What are y-"
    scene ch3ep1_265 with vpunch
    weston "Oh, shit!!"
    elaine "!!!!!"
    scene ch3ep1_266 with dissolve
    weston "*Screams* No! No! No! No!"
    weston "*Screams* Help me! Don't let me fall!"
    elaine "[mc]...! What are you doing?!"
    elaine "I wanted your help, but this is too much! I don't want you to become a murderer!"
    scene ch3ep1_267 with dissolve
    weston "*Screams* You heard her! W-What are you waiting for?!"
    weston "*Screams* P-Pull me back in, please! I don't want to die!"
    mc "Then, vow to me that you won't threaten [elaine] again."
    weston "*Screams* S-Sure! I won't do that again!"
    scene ch3ep1_268 with dissolve
    mc "What? I didn't hear you. Say it again. Louder."
    weston "*Screams* I-I will stop bothering [elaine] from now on!!!!"
    weston "*Screams* I-I will not show my face in front of you guys anymore!!!!"
    mc "......................."
    weston "*Screams* P-Please, pull me back up!!!"
    mc "Fine..."
    scene black with dissolve
    scene ch3ep1_269 with dissolve
    weston "*Pants* Thank god......"
    elaine "Thank [mc] that he didn't decide to throw you down!"
    elaine "Now get the fuck out of my face!"
    mc "Yeah. You better run now before I change my mind..."
    scene ch3ep1_270 with dissolve
    weston "Get the fuck out of here, guys!"
    weston "That guy is a fucking maniac!!"
    elaine "Hell yeah, keep running like the bitches you are!"
    elaine "And don't ever fucking show yourself in front of me again!"
    scene black with dissolve
    $ renpy.pause()
    s "You waited until weston and his crew had left........"
    stop music fadeout 3.0
    scene ch3ep1_271 with dissolve
    play music "sfx/ch2ep3_1.mp3" fadein 4.5
    $ bgm = "RYYZN - Memories Erased"
    mc "Alright, they all left n-"
    elaine "Thank you so much, [mc]...."
    elaine "You saved me once again."
    mc "... You're welcome."
    scene ch3ep1_272 with dissolve
    elaine "... I was on the way back to the company when he showed up trying to take me with him."
    elaine "I ran as soon as I saw him. As I was running, I remembered how you saved me from him before so I decided to call you. "
    elaine "Fortunately, you arrived just in time."
    mc "You know at first I didn't want to ask you, but...."
    mc "What's actually going on between the two of you?"
    elaine "......................."
    scene ch3ep1_273 with dissolve
    mc "Do you mind telling me?"
    elaine "....................."
    scene ch3ep1_274 with dissolve
    elaine "Would you mind if I smoke first?"
    elaine "I really need one."
    mc "Of course not. You do you."
    elaine "Thank you."
    scene ch3ep1_275 with dissolve
    elaine "*Sighs*..............."
    elaine "To be honest I don't want to tell anyone about my story...."
    elaine "But since you're already a part of this, I'm going to tell you everything..."
    scene ch3ep1_276 with dissolve
    elaine "Have you ever heard of Celio?"
    mc "No, I haven't."
    elaine "It was one of the big fashion companies 10 years ago. My parents were the owner."
    elaine "So, basically my family was very rich."
    scene ch3ep1_277 with dissolve
    elaine "They were managing the company perfectly until they made the company lose a lot of its value. So much so that they were soon facing bankruptcy."
    elaine "That was when my parents decided to borrow money from their best friends, [weston]'s parents."
    elaine "They intended to use that money to save their company. However, business has never been easy."
    elaine "No matter how hard they tried, they failed to save the company."
    elaine "Then, we eventually lost everything."
    elaine "That's not the end of the story though. It's just the beginning...."
    elaine "My parents didn't have money to pay their debts to [weston]'s family. That was when their friendships tore apart."
    scene ch3ep1_278 with dissolve
    elaine "They had no choice, but to do everything [weston]'s family told them to."
    elaine "My mother became their maid, and my father became their driver."
    elaine "They didn't even get paid properly since half their wages were cut to pay their debts."
    elaine "They even got beaten up when [weston]'s family was mad at something that my mother and father didn't even do."
    elaine "And it got worse as the time past by..."
    scene ch3ep1_279 with dissolve
    elaine "I witnessed my parent getting beaten up so many times that it became my trauma."
    elaine "The fact that there was nothing I could do to help my family made me feel very useless."
    elaine "My childhood was literally ruined. I was never happy. I was always stressful. I had never smiled once during the time I was in that house."
    elaine "Then, one day I accidentally witnessed [weston]s dad having sex with his secretary."
    elaine "It made me feel horny. And that's when I learned to mastubate for the first time."
    elaine "I soon learned that I could reduce my stress by masturbating. Therefore, I started doing it more and more often."
    elaine "Unfortunately, I got caught by [weston]. He then tried to rape me, but my father came to save me in time."
    scene ch3ep1_278 with dissolve
    elaine "My family had no choice, but to send me away to live with my grandmother."
    elaine "My life became a bit better, but it was still suffering because my grandmother didn't have a lot of money as well."
    elaine "I had no choice, but to help her collect used bottles on street and sell them."
    elaine "The only way for me to feel some slight of happiness, was masturbating. As the time flew by, I became more and more obsessed with that."
    elaine "Later on, my grandmother decided to use her last savings on sending me to school."
    elaine "I didn't want her to do that for me, but she insisted. She wanted me to get an education no matter what."
    elaine "Then after a couple years in high school, a guy came to confess his feeling to me."
    elaine "I never knew what he saw in me, and why he loved me. However, he was very kind to me. So, I agreed to be his girlfriend."
    scene ch3ep1_276 with dissolve
    elaine "There was nothing I could do for him in return of his kindness, so I chose sex."
    elaine "I had sex for the first time with him, then he looked like the most happiest guy in the world."
    elaine "Seeing him like that, made me feel happy as well. It was the first time in many years that I felt valuable."
    elaine "Therefore, I had sex with him more and more often. However, it was too often that he couldn't take it."
    elaine "He said he didn't feel that my love at all. He felt that I was trying to repay his love because he confessed to me."
    elaine "Eventually, we broke up. And that was when I felt worthless again."
    elaine "My obsession with sex didn't stop as we broke up. But it kept getting stronger. Sometimes I couldn't even control myself."
    elaine "It was so bad that I had no choice, but to go see an expert. Then, I found out that I became a nymphomaniac."
    scene ch3ep1_280 with dissolve
    elaine "You might have heard everyone talking about it; hell, you have experienced it firsthand. I love having sex."
    elaine "It's not that I love it. It's just I can't control myself..."
    elaine "Even though I've gotten better, there are still times that I lose control of myself."
    elaine "However, I didn't want anyone to know about it, so I just let them think I was a slut."
    mc ".... No one thinks of you that way."
    elaine "Don't be silly, [mc]. Even though they call me Angel of whatever the name is, deep down they just see me as a slut. I know that."
    mc ".............................."
    scene ch3ep1_281 with dissolve
    elaine "Alright, just forget it. Let's get back to the main topic."
    elaine "Fortunately, I managed to get a decent job at Xecon."
    elaine "I've earned quite a lot of money and have been helping my family pay for the past three years now."
    elaine "About two weeks ago, I thought I had finally paid off everything. But it turned out that we still had to pay for the interest."
    elaine "That's why [weston] tried to take advantage of me. I have no idea how he managed to find me though."
    elaine "Fortunately, you came to help me in time..."
    scene ch3ep1_282 with dissolve
    mc "How much do you still have to pay?"
    elaine "He said it was five hundred thousand."
    mc ".... That's quite a lot of money."
    elaine "I know.... It's going to take me and my family a few more years to pay it off."
    scene ch3ep1_283 with dissolve
    elaine "I don't mind paying it, but I just don't want [weston] to come and take advantage of me."
    elaine "My family owe them money, but I'm not his sex toy."
    elaine "Even if I'm a nymphomaniac, I'm the one to choose who I'm going to have sex with."
    elaine "Thanks to you, I think from now on he will finally leave me alone."
    scene ch3ep1_284 with dissolve
    mc "Well... I might have scared him today, but there is no guarantee that he will not come back."
    mc "From what I heard, his family must be very rich. And a spoiled brat like him will always think the world revolves around him."
    elaine "... Yeah, you're right. He really thinks that."
    elaine "Then, what should we do?"
    mc "Don't worry. If he dares to show himself in front of you again. Call me immediately, and I will come help you if I can."
    elaine ".... Thank you so much. That means a lot to me."
    scene ch3ep1_285 with dissolve
    mc "You're welcome."
    elaine "Shit! It's half past one now!"
    elaine "Let's get back to the company!"
    mc "Sure."
    scene ch3ep1_286 with dissolve
    elaine "Hurry up, [mc]!"
    elaine "I can't be late again!"
    mc "Okay... Okay... I get it."
    $ elaine_ch3_ep1 += 2
    $ eliane_relationship += 2
    $ ch3ep1_saveelaine = 1
    scene black with dissolve
    $ renpy.pause()
    stop music fadeout 3.0
    jump ch3ep1part2continue
label ch3ep1part2continue:
    if ch3ep1_fayeinvite == 1:
        scene black with dissolve
        s "You spent time working until evening...."
        jump ch3ep1fayedinner
    else:
        scene black with dissolve
        s "Later that night..........."
        jump ch3ep1part2_firstnight
label ch3ep1fayedinner:
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    scene ch3ep1_287 with fade
    faye "Here we are. Welcome to my house."
    faye "Make yourself at home."
    mc "Thank you..."
    scene ch3ep1_288 with dissolve
    faye "To think about it, you're the first man that has ever come here."
    faye "Not once, but twice... or is it third?"
    mc "I don't remember that..."
    scene ch3ep1_289 with dissolve
    faye "Whatever... It doesn't matter how many times you've been here."
    faye "I'm just trying to say that you're very lucky."
    faye "I've never invited a guy in my house before."
    mc "Really...? Wow... I feel so honored."
    faye "Pff... Stop it. I know you're being sarcastic."
    scene ch3ep1_290 with dissolve
    faye "Alright, let's not waste any more time."
    faye "What would you like to eat for dinner? Any ideas?"
    mc "Um... Do you happen to have some meat left?"
    faye "Yes, I do. Why?"
    mc "I want to have steak for dinner today."
    faye "Sure thing. Let's have steak then."
    scene ch3ep1_291 with dissolve
    faye "It's going to take some time."
    faye "Why don't you go sit on the sofa first?"
    faye "You can also turn on the TV if you want. Just like I told you earlier, make yourself at home."
    mc "Sure. Thank you."
    scene black with dissolve
    $ renpy.pause()
    s "Forty five minutes later.............."
    scene ch3ep1_292 with dissolve
    mc "......................."
    faye "[mc]..."
    u "Hm...?"
    scene ch3ep1_293 with dissolve
    mc "Yeah?"
    faye "Dinner is ready. Come over here."
    mc "Oh... Okay."
    scene black with dissolve
    scene ch3ep1_294 with dissolve
    mc "Thank you for cooking me dinner."
    faye "You're welcome...."
    faye "Oh, wait a minute... I forgot to bring our knifes and forks."
    faye "I'll be back real quick."
    mc "Do you want me to go with you?"
    scene ch3ep1_295 with dissolve
    faye "Thanks, but I'm good. Just wait for me here."
    mc "Okay, if you say so."
    faye "Oh, I almost forgot. Do you want some wine?"
    mc "... Up to you. If you want to drink, I'll drink with you."
    faye "Then, I'll bring a bottle."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_296 with dissolve
    faye "Alright...."
    faye "Sorry for the wait. Shall we start eating?"
    mc "Yeah, sure."
    scene ch3ep1_297 with dissolve
    faye "But, first of all, thank you for taking care of me."
    faye "I was able to recover, and attend the meeting in the next day because of you."
    faye "Cheers..."
    mc "I'm glad I could be of help. Cheers."
    scene black with dissolve
    $ renpy.pause()
    s "About an hour later................."
    if ch2ep4takefayehome == 1 and ch2ep2suggestalice == 1 and nominatekrystal == 1:
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_298 with dissolve
        faye "[mc]."
        mc "Yeah?"
        faye "What's the thing you like or dislike the most?"
        mc ".... Why did you suddenly ask that?"
        scene ch3ep1_299 with dissolve
        faye "Even though we've known each other for some time now, I still don't know much about you."
        faye "So, I'd like to get to know you better."
        mc "Well...."
        mc "To be honest I don't know what I like the most."
        faye "What? Come on. Stop kidding me already."
        scene ch3ep1_298 with dissolve
        mc "I'm not joking. I really don't know what I like."
        faye "..................."
        mc "But, I can tell you that I don't like being alone."
        faye "... Why's that?"
        mc "I was abandoned twice when I was young."
        faye "Oh. I'm sorry, I shouldn't have asked such a sensitive question."
        scene ch3ep1_301 with dissolve
        mc "It's okay. I overcame it already."
        mc "But, if I have a choice, I wouldn't want to experience that feeling ever again."
        scene ch3ep1_300 with dissolve
        faye "Yeah, I wouldn't want to experience that as well."
        faye "You've surely come a long way, [mc]. "
        faye "I wish the best for you from now on."
        scene ch3ep1_301 with dissolve
        mc "Thank you..."
        scene ch3ep1_300 with dissolve
        faye "Alright, let's just talk about something positive."
        mc "... Like what?"
        faye "I wonder... if there's something that makes you feel happy."
        faye "Of course it doesn't have to be tangible."
        scene ch3ep1_301 with dissolve
        mc "Let me think....."
        mc "Well, I think I feel happy when I achieve my goals, or the tasks I was given."
        mc "It makes me feel useful."
        scene ch3ep1_298 with dissolve
        faye "Me, too. I also find myself being happiest when achieving my goals."
        faye "Not because it makes me feel useful though. But because it means I have the skills and talent to achieve my dreams and goals."
        mc "That makes sense. I understand you."
        scene ch3ep1_302 with dissolve
        faye "Well, it looks like we have one thing in common."
        mc "Yeah..."
        faye "Do you have a girlfriend?"
        mc "... Why did you ask that?"
        faye "Why not? I just want to know if you have one or not."
        scene ch3ep1_303 with dissolve
        mc "No, I don't have a girlfriend."
        faye "Really? That's actually quite hard to believe."
        mc "Why? Do I seem like someone who has a girlfriend?"
        faye "No, but I mean... You're smart, calm, and good looking."
        faye "So, it's a little bit surprising to hear that you are still single."
        mc "I see...."
        scene ch3ep1_302 with dissolve
        faye "Do you like older or younger women?"
        u "What kind of questions are these...?"
        u "I never expected [faye] to ask me these questions..."
        mc "If I have to date someone, her age doesn't matter."
        mc "If the feeling is right, then she is right for me."
        scene ch3ep1_304 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_304.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_304_blink.jpg", 1) with dissolve
        faye "Then, what do you think about me?"
        mc "Are you drunk? Your face is a little red."
        faye "No, I'm not. I know what I'm doing right now."
        mc "Then, why are you asking me such a question?"
        faye "You know... I'm already 26 years old. I have a house, a car, and a decent job."
        faye "I didn't think about it before, but now I think it's time for me to look for someone to be with."
        faye "You were there to stand up against my mother. You were also by my side when I was most vulnerable."
        faye "You always helped me every time you had a chance to. Why did you do all that?"
        menu:
            "I admired you. [smrec]":
                jump ch3ep1_halfconfess
            "I just wanted to help.":
                $ ch3ep1_fayequestion = 2
                scene ch3ep1_305_b1 with dissolve
                mc "I understand everything now...."
                mc "I'm sorry that I made you confused. I did of all that because I just wanted to help you."
                mc "There was no special feeling at all."
                faye "...................."
                scene ch3ep1_305_b2 with dissolve
                faye "Okay.... I get it now."
                mc "I'm sorry."
                faye "No, there is no need to be sorry. You didn't do anything wrong."
                faye "Thank you for making it clear for me."
                mc ".........................."
                faye "Well... It's getting late now. Let's finish the dinner real quick so that you won't get home too late."
                mc "Okay...."
                scene black with dissolve
                $ renpy.pause()
                stop music fadeout 3.0
                jump ch3ep1part2_firstnight

    else:
        scene black with dissolve
        stop music fadeout 3.0
        s "You spent time having lunch with dinner, then came back home...."
        jump ch3ep1part2_firstnight
label ch3ep1_halfconfess:
    $ ch3ep1_fayequestion = 1
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    scene ch3ep1_305_a1 with dissolve
    mc "Despite being so young, you have a very high position in the company."
    mc "You have a bad repution for being cold, but you don't waste your time trying to fix it."
    faye "......................"
    mc "Instead, you keep working hard to benefit the company even more."
    mc "I admired that side of you. That's why I helped you whenever you had a rough time."
    scene ch3ep1_305_a2 with dissolve
    faye "[mc]...."
    mc "... What?"
    faye "I didn't expect to hear that from you. That was so touching."
    faye "Thank you... It really means a lot."
    mc "... You're welcome. You deserve it."
    scene ch3ep1_305_a3 with dissolve
    faye "You're so sweet today..."
    faye "This is bad...."
    mc "... Why?"
    scene ch3ep1_305_a4 with dissolve
    mc "... Where are you going?"
    faye "....................."
    stop music fadeout 3.0
    scene black with dissolve
    scene ch3ep1_305_a5 with dissolve
    mc ".................."
    faye "Can I test something...?"
    faye "I want to know how I really feel..."
    mc "What are you going to t-"
    play music "sfx/ep.3/ep3_12.mp3" fadein 3.0
    $ bgm = "Brook Xiao - Fire (ft. Rachel Horter)"
    scene ch3ep1_305_a6 with dissolve
    mc "Hmmm...."
    faye "*Kisses*................"
    scene ch3ep1_305_a7 with dissolve
    mc "What was that for...?"
    faye "My heart has been beating really fast. Now you've made it beat even harder and faster."
    faye "I wanted to check if this feeling towards you is real or if it's just nothing."
    mc "... So, do you know it now?"
    faye "I'm not sure... I think I need to check even more."
    scene ch3ep1_305_a8 with dissolve
    faye "*Kisses* Mmmm......"
    mc "*Kisses*................."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_305_a9 with dissolve
    faye "*Kisses* Mmmm... Where... are you... mmmm.... taking me to....?"
    mc "*Kisses* To the sofa...."
    mc "*Kisses* You can tell me to stop if you don't want to...."
    scene ch3ep1_305_a10 with dissolve
    mc "*Kisses* Still don't know how you feel...?"
    faye "*Kisses* Hmmm... Just a... hehe. Little bit... more~ Hnng"
    mc "*Kisses* Alright then...."
    scene ch3ep1_305_a11 with dissolve
    mc "[faye]."
    faye "*Softly breathes* H... Hm?"
    mc "Get up and take off your clothes."
    faye "........................"
    faye "..... Okay."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_305_a12 with dissolve
    mc "Why are you covering your face....?"
    faye "Aw....."
    faye "Don't ask me anything.... I'm so embarrassed right now."
    faye "I haven't done this in so many years...."
    mc "Relax... It's going to be fine."
    scene black with dissolve
    scene ch3ep1_305_a13 with dissolve
    show ch3ep1_faye1
    faye "*Softly breathes* A-Ah...!"
    mc "It's so tight...."
    faye "*Softly breathes* Mhmmm... S... Stop saying... such things already..."
    $ renpy.pause()
    hide ch3ep1_faye1
    scene ch3ep1_305_a14 with dissolve
    show ch3ep1_faye2
    faye "*Softly breathes* Mhhmmm..... [mc]....."
    mc "Does it feel good?"
    faye "*Softly breathes* Y... Yeah....."
    $ renpy.pause()
    hide ch3ep1_faye2
    scene ch3ep1_305_a15 with dissolve
    show ch3ep1_faye3
    faye "*Moans* A... Ahhh...! T... That's the spot, [mc]...!"
    faye "*Moans* Mhmm... It feels.... so good right there....!"
    $ renpy.pause()
    hide ch3ep1_faye3
    scene ch3ep1_305_a16 with dissolve
    faye "*Pants* W... Why did you stop...?"
    mc "Let's do something else."
    mc "Can you go sit on the sofa and turn to me?"
    faye "Okay...."
    scene black with dissolve
    scene ch3ep1_305_a17 with dissolve
    faye "Like this...?"
    mc "Spread your legs a little bit more."
    faye "Okay....."
    mc "Good girl..."
    scene black with dissolve
    scene ch3ep1_305_a18 with dissolve
    show ch3ep1_faye4
    faye "*Softly breathes* H-Hang on a sec, [mc]...! It's dirty down there....!"
    mc "It's alright...."
    faye "*Softly breathes* A... Ahhng...."
    $ renpy.pause()
    hide ch3ep1_faye4
    scene ch3ep1_305_a19 with dissolve
    show ch3ep1_faye5
    faye "*Moans* H... Hahhh... [mc]..... It tickles...."
    mc "Relax... You'll get used to it soon enough."
    faye "*Moans* Mhhhmmmm...."
    $ renpy.pause()
    hide ch3ep1_faye5
    scene ch3ep1_305_a20 with dissolve
    show ch3ep1_faye6
    faye "*Moans* A... Ahhhh.... H... Haahhh...."
    mc "See...? I told you..."
    $ renpy.pause()
    hide ch3ep1_faye6
    scene ch3ep1_305_a21 with dissolve
    faye "... What's wrong? Why did you suddenly stand up?"
    mc "That's it. I think you're ready now."
    faye "Oh...."
    scene black with dissolve
    scene ch3ep1_305_a22 with dissolve
    faye "W-What!?"
    mc "Hm? What's wrong?"
    faye "Nothing....."
    faye "(Why is it so big....? I remember my ex from high school, it was a lot smaller than this.)"
    scene black with dissolve
    scene ch3ep1_305_a23 with dissolve
    mc "Okay...."
    mc "Are you ready now, [faye]?"
    faye "(Should I really be doing this...?)"
    mc "[faye]?"
    faye "......................"
    mc "Alright, I'm going to put it in n-"
    scene ch3ep1_305_a24 with dissolve
    faye "Wait a minute, [mc]...."
    mc "Hm? What's wrong?"
    faye "Can we stop? I don't think I'm ready yet..."
    mc "... Why?"
    scene ch3ep1_305_a25 with dissolve
    faye "Yeah, I know now that my feeling towards you is real, but..."
    faye "I think it's too fast to do it now..."
    faye "I don't want to seem easy in your eyes."
    faye "I don't want to be like my mom...."
    mc "....................."
    scene ch3ep1_305_a26 with dissolve
    mc "Okay, if you say so."
    mc "I don't want to force you to do something you don't want to either."
    faye "Thank you for understanding me."
    mc "No problem..."
    faye "Can we switch positions though?"
    mc "Hm? Why?"
    faye "Since you made me feel good, we can't just end it like this."
    faye "I will make you feel good, too."
    mc "Okay...."
    scene ch3ep1_305_a27 with dissolve
    faye "I'll use my hands if that's okay with you."
    mc "Sure thing. You do you."
    faye "Thanks. I might not be good at it, but I'll try my best."
    scene ch3ep1_305_a28 with dissolve
    show ch3ep1_faye7
    faye "How does it feel, [mc]?"
    mc "... It's okay. Your hands are also very soft."
    mc "But, it will be better if you do it faster."
    $ renpy.pause()
    hide ch3ep1_faye7
    scene ch3ep1_305_a29 with dissolve
    show ch3ep1_faye8
    faye "Like this....?"
    mc "Yeah... Keep moving your hands like that."
    faye "Okay..."
    $ renpy.pause()
    hide ch3ep1_faye8
    scene ch3ep1_305_a30 with dissolve
    show ch3ep1_faye9
    mc "Ahh...."
    faye "How do you like it? Are you feeling good right now?"
    mc "Yeah... Keep doing it. Don't stop."
    faye "As you wish...."
    $ renpy.pause()
    hide ch3ep1_faye9
    scene ch3ep1_305_a31 with dissolve
    mc "Hold on, [faye]..."
    faye "Hm? Am I doing something wrong?"
    mc "No, you're doing wonderful."
    mc "But, I don't think I will cum even if we keep doing it."
    mc "Can we try something else?"
    faye "Alright then... I've got an idea."
    scene black with dissolve
    scene ch3ep1_305_a32 with dissolve
    faye "How about this?"
    faye "I saw in a porn video that a man enjoyed it a lot when a woman did this for him."
    mc "Well, yeah you're right about that."
    faye "I've never done this before, but I'll try..."
    scene ch3ep1_305_a33 with dissolve
    show ch3ep1_faye10
    faye "Am I doing it right? How do you feel?"
    mc "Yeah, you're doing it perfectly. It feels so good."
    faye "*Smiles* Glad to know that...."
    $ renpy.pause()
    hide ch3ep1_faye10
    scene ch3ep1_305_a34 with dissolve
    show ch3ep1_faye11
    mc "Ahh...."
    $ renpy.pause()
    hide ch3ep1_faye11
    scene ch3ep1_305_a35 with dissolve
    show ch3ep1_faye12
    mc "I'm almost there, [faye]..."
    faye "*Smiles* Okay... Feel free to cum whenever you want."
    $ renpy.pause()
    menu:
        "Handjob":
            hide ch3ep1_faye12
            jump ch3ep1_fayehandjob1
        "Slowest":
            hide ch3ep1_faye12
            jump ch3ep1_fayeboobjob1
        "Slower":
            hide ch3ep1_faye12
            jump ch3ep1_fayeboobjob2
        "Cum":
            jump ch3ep1_fayeboobjobcum
label ch3ep1_fayehandjob1:
    scene ch3ep1_305_a28 with dissolve
    show ch3ep1_faye7
    window hide
    $ renpy.pause()
    menu:
        "Boobjob":
            hide ch3ep1_faye7
            jump ch3ep1_fayeboobjob1
        "Faster":
            hide ch3ep1_faye7
            jump ch3ep1_fayehandjob2
        "Fastest":
            hide ch3ep1_faye7
            jump ch3ep1_fayehandjob3
label ch3ep1_fayehandjob2:
    scene ch3ep1_305_a29 with dissolve
    show ch3ep1_faye8
    window hide
    $ renpy.pause()
    menu:
        "Boobjob":
            hide ch3ep1_faye8
            jump ch3ep1_fayeboobjob1
        "Slower":
            hide ch3ep1_faye8
            jump ch3ep1_fayehandjob1
        "Faster":
            hide ch3ep1_faye8
            jump ch3ep1_fayehandjob3
label ch3ep1_fayehandjob3:
    scene ch3ep1_305_a30 with dissolve
    show ch3ep1_faye9
    window hide
    $ renpy.pause()
    menu:
        "Boobjob":
            hide ch3ep1_faye9
            jump ch3ep1_fayeboobjob1
        "Slowest":
            hide ch3ep1_faye9
            jump ch3ep1_fayehandjob1
        "Slower":
            hide ch3ep1_faye9
            jump ch3ep1_fayehandjob2
label ch3ep1_fayeboobjob1:
    scene ch3ep1_305_a33 with dissolve
    show ch3ep1_faye10
    window hide
    $ renpy.pause()
    menu:
        "Handjob":
            hide ch3ep1_faye10
            jump ch3ep1_fayehandjob1
        "Faster":
            hide ch3ep1_faye10
            jump ch3ep1_fayeboobjob2
        "Fastest":
            hide ch3ep1_faye10
            jump ch3ep1_fayeboobjob3
label ch3ep1_fayeboobjob2:
    scene ch3ep1_305_a34 with dissolve
    show ch3ep1_faye11
    window hide
    $ renpy.pause()
    menu:
        "Handjob":
            hide ch3ep1_faye11
            jump ch3ep1_fayehandjob1
        "Slower":
            hide ch3ep1_faye11
            jump ch3ep1_fayeboobjob1
        "Faster":
            hide ch3ep1_faye11
            jump ch3ep1_fayeboobjob3
label ch3ep1_fayeboobjob3:
    scene ch3ep1_305_a35 with dissolve
    show ch3ep1_faye12
    $ renpy.pause()
    menu:
        "Handjob":
            hide ch3ep1_faye12
            jump ch3ep1_fayehandjob1
        "Slowest":
            hide ch3ep1_faye12
            jump ch3ep1_fayeboobjob1
        "Slower":
            hide ch3ep1_faye12
            jump ch3ep1_fayeboobjob2
        "Cum":
            jump ch3ep1_fayeboobjobcum
label ch3ep1_fayeboobjobcum:
    scene black with dissolve
    hide ch3ep1_faye12
    scene ch3ep1_305_a36 with vpunch
    mc "I'm cumming...!"
    scene ch3ep1_305_a36 with vpunch
    faye "*Smiles* Wow... You're shooting it out quite a lot...."
    scene ch3ep1_305_a36 with vpunch
    mc "Arrr......"
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_305_a37 with dissolve
    faye "*Pants* Did you enjoy my service?"
    mc "Of course, I did..."
    faye "*Pants* Great. It took me quite a lot of energy, so I'd have been disappointed if you said you didn't enjoy it."
    mc "... Then, just stay like this and rest for a bit."
    faye "Sounds good to me...."
    scene black with dissolve
    $ renpy.pause()
    s "*About fifteen minutes later*.............."
    stop music fadeout 3.0
    scene ch3ep1_305_a38 with dissolve
    mc "Alright, it's getting late now. I should go home before it gets any darker."
    faye "Okay... Thank you for today. I enjoyed being with you a lot."
    mc "Me, too."
    faye "Good night, [mc]."
    mc "Good night, [faye]."
    $ renpy.end_replay()
    $ faye_relationship += 3
    $ faye_ch3_ep1 += 3
    scene black with dissolve
    $ renpy.pause()
    jump ch3ep1part2_firstnight
label ch3ep1part2_firstnight:
    scene ch3ep1_306 with fade
    u "Finally, I've arrived home."
    u "It's been a pretty long day...."
    u "I feel so sweaty now. Let's go take a shower real quick."
    scene black with dissolve
    $ renpy.pause()
    s "Half an hour later............."
    play music "sfx/ep.3/ep3_4.mp3" fadein 3.0
    $ bgm = "Sarah Jansen - Moments"
    scene ch3ep1_307 with dissolve
    u "Alright...."
    u "I've finished taking a shower."
    u "I feel much more refreshing now...."
    if ch2ep4eirakiss == 1:
        scene ch3ep1_308 with dissolve
        s "*Phone vibrates*............."
        u "Hm...? I've got someone calling me now.?"
        u "Let's find out who it is..."
        scene ch3ep1_309 with dissolve
        u "Oh...."
        u "It's [eira]."
        u "I wonder why she's calling me so late at night like this..."
        scene ch3ep1_310 with dissolve
        mc "Hello, [eira]..."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_311 with fade
        eira "Hi, [mc]..."
        eira "Sorry for calling you at such a time like this. I hope I didn't wake you up."
        scene ch3ep1_310 with dissolve
        mc "No, you didn't."
        mc "I just came out of the bathroom."
        mc "How's your condition by the way?"
        scene ch3ep1_311 with dissolve
        eira "I'm relieved to hear that..."
        eira "I'm all good now. Thank you for asking."
        eira "I'll start working again tomorrow."
        scene ch3ep1_312 with dissolve
        mc "Glad to hear that."
        mc "May I ask why you're calling me now by the way?"
        mc "Is there anything you need me to help you with?"
        scene ch3ep1_313 with dissolve
        eira "Actually, I'd like to ask if you are free on tomorrow at noon."
        scene ch3ep1_313 with dissolve
        eira "[sally] and I discussed about inviting you to have lunch together."
        eira "We'll buy you a meal as a thank you gift for saving me last time."
        eira "What do you think?"
        scene ch3ep1_310 with dissolve
        mc "........................"
        menu:
            "Accept her invitation. [eira1]":
                $ ch3ep1_eirasallylunch = 1
                $ eira_relationship += 1
                $ eira_ch3_ep1 += 1
                scene ch3ep1_314 with dissolve
                mc "Sounds good to me."
                mc "I will go with you guys."
                mc "I'll meet you guys at the main elevator at lunch break."
                scene ch3ep1_315_a with dissolve
                eira "Really? Are you really going to join us?"
                eira "I'm so glad to hear that!"
                eira "Alright, I won't take any more of your time."
                eira "See you tomorrow. Have a good night."
            "Reject her invitation.":
                $ ch3ep1_eirasallylunch = 2
                scene ch3ep1_314 with dissolve
                mc "I'm sorry. I think I'll be busy tomorrow."
                mc "Thank you for inviting me though."
                mc "I appreciate your kindness."
                scene ch3ep1_315_d with dissolve
                eira "Oh... Is that so?"
                eira "What a pity.... I really wanted to do something to return your kindness."
                eira "Alright... I won't take any more of your time. Good night, [mc]."
    scene ch3ep1_316 with dissolve
    mc "....................."
    u "It's only a few days left until I have to give the fake blueprint to [victor]...."
    u "To be honest I'm still not sure if this plan is going to work...."
    scene ch3ep1_317 with dissolve
    u "I don't know how long are we going to be able to fool him."
    u "No matter how good the fake blueprint is going to be, he will find out the truth eventually."
    u "It's only just a matter of time...."
    u "I will also need to return to him once he gets the blueprint."
    u "He's going to think that I have no reason to remain at Xecon anymore."
    scene ch3ep1_318 with dissolve
    u "I hope [felix] can arrest [victor] before he finds out that the blueprint is fake."
    u "Otherwise, I'm going to be in a big trouble for sure."
    u "No... Not just only, but everyone I know. [rin], [yui], [zeke], and more..."
    u "... Do I need to tell them everything?"
    u "Or should I just disappear without telling anything?"
    u "Since the less they knows, the safer they will be, right?"
    scene ch3ep1_319 with dissolve
    u "*Sighs* This is the hardest decision I've ever had...."
    u "I need a couple more days to think about it...."
    u "I have to think about it really carefully since it's about their lives..."
    scene black with dissolve
    scene ch3ep1_320 with dissolve
    u "Well...."
    u "It's getting very late now though..."
    u "Let's go to bed and get some sleep to clear my head."
    scene black with dissolve
    $ renpy.pause()
    jump ch3ep1part2_nextday

label ch3ep1part2_nextday:
    scene black with dissolve
    s "Next morning.............."
    scene ch3ep1_321 with fade
    mc "[yui]."
    yui "Hm?"
    mc "I feel like we haven't talked for a while. How've you been recently?"
    yui "Good as always. Why?"
    mc "Nothing. I just wondered...."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time working until lunch break.........."
    if ch3ep1_eirasallylunch == 1:
        scene ch3ep1_322_a1 with fade
        sally "Oh!? Hi, [mc]!"
        eira "Hello, [mc]..."
        mc "Sorry to kept you guys waiting...."
        scene ch3ep1_322_a2 with dissolve
        eira "It's alright. We've just got down here a few minutes ago as well."
        sally "Yeah, you don't have feel sorry at all."
        mc "Thank you for saying that."
        mc "Alright, where are we going to have lunch then?"
        scene ch3ep1_322_a3 with dissolve
        sally "We agreed to go to the park nearby."
        sally "Have you ever been there?"
        mc "Hm? There is a park nearby the company?"
        eira "Yeah, it's only a ten-minute walk from here."
        mc "Alright.... Let's go then."
        scene black with dissolve
        scene ch3ep1_322_a4 with fade
        mc "Hang on a sec... What we are going to eat though?"
        mc "Is there any food restaurant at the park?"
        eira "No, there isn't..."
        sally "*Giggles* Yeah..."
        sally "But, don't worry! I've already ordered a pizza to deliver there!"
        mc "Oh... Okay then."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_322_a5 with fade
        sally "Alright, guys."
        sally "Looks like this is the only place we can sit on."
        sally "The park is crowded today. The other chairs are all unavailable."
        mc "I have no problem with that. If this is the only place available, then just sit here."
        eira "Me, too..."
        scene ch3ep1_322_a6 with dissolve
        s "*Phone vibrates*............."
        sally "Oh! Looks like the delivery boy is going to arrive here soon."
        eira "Really? That was a lot quicker that I expected."
        sally "I know, right?"
        mc "Did you buy a new phone, [sally]?"
        scene ch3ep1_322_a7 with dissolve
        sally "Hm? Oh, yeah!"
        sally "My previous one didn't work well, so I decided to buy a new one."
        sally "*Giggles* But, don't worry! I didn't change my number."
        mc "That's not what I meant...."
        sally "*Giggles* I know! I was just joking!"
        sally "Alright, I'm going to take the pizza. You guys can take a seat first."
        mc "Do you need my help?"
        sally "Thank you, but I think you better stay here with [eira]."
        mc "Alright then."
        scene ch3ep1_322_a8 with dissolve
        sally "Hello?"
        sally "Oh, you've already arrived at the entrance?"
        sally "Okay. Okay. I'm on my way."
        mc ".................."
        scene ch3ep1_322_a9 with dissolve
        mc "[eira]."
        eira "Yeah?"
        mc "Shall we take a seat?"
        eira "Oh... Sure. Let's sit and wait for [sally]."
        scene black with dissolve
        scene ch3ep1_322_a10 with dissolve
        mc "Your condition..."
        mc "Are you sure that you're really fine now?"
        eira "Yeah. The doctor told me that I've already fully recovered."
        mc "Really...? Good for you then."
        scene ch3ep1_322_a11 with dissolve
        mc "Oh... I haven't told you, right?"
        eira "Hm...?"
        mc "I've already dealt with [roxy] for you."
        mc "You don't have to worry about her now. You will not see her again."
        scene ch3ep1_322_a12 with dissolve
        eira "What?"
        eira "Are you joking?"
        mc "... Why would I joke about that?"
        eira "I mean... her father is really powerful..."
        scene ch3ep1_322_a13 with dissolve
        mc "Don't worry about that, too."
        mc "I've already dealt with her father."
        eira "......................"
        mc "He already sent [roxy] oversea."
        eira "What have you done....?"
        mc "......................"
        scene ch3ep1_322_a14 with dissolve
        eira "Well...."
        eira "Sometimes you're scary. You know that, right?"
        mc "....................."
        eira "But... I won't be scared of you. Actually, there is no reason to."
        eira "You might be scary and mysterious, but you've never done anything bad to me."
        mc "I will not that to you..."
        eira "I know... Thank you for fixing my problem, [mc]."
        mc "Anytime."
        scene black with dissolve
        scene ch3ep1_322_a15 with dissolve
        sally "Alright, guys. I'm back!"
        sally "Sorry for kept you guys waiting."
        mc "Huh?"
        scene ch3ep1_322_a16 with dissolve
        mc "Why is the box so big?"
        sally "*Giggles* Because it's a sixteen inch pizza!"
        mc "... Are you sure we can eat all that?"
        sally "*Giggles* Yes, I am! I'm so hungry right now."
        mc "......................"
        scene ch3ep1_322_a17 with dissolve
        mc "Okay then..."
        mc "Let me help you."
        eira "Me, too. I'll help you carrying these cans."
        sally "Thanks, guys."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_322_a18 with dissolve
        mc "It's really big....."
        sally "*Giggles* What are you talking about? Of course, it is!"
        sally "But hey, look. It's actually not so thick, right?"
        sally "You won't be full just by eating a piece of it."
        sally "I'd say you need to eat at least two pieces."
        mc "Okay...."
        scene ch3ep1_322_a19 with dissolve
        mc "Here you are, [eira]."
        eira "Thank you..."
        scene ch3ep1_322_a20 with dissolve
        mc "And this is yours."
        sally "Thanks!"
        sally "Don't forget to take one for yourself, too!"
        sally "I want you to try it. The pizza of this restaurant is the best in the city."
        mc "Is that so?"
        sally "Yeah! I'm not lying!"
        mc "Alright then...."
        scene black with dissolve
        $ renpy.pause()
        s "About half an hour later.............."
        scene ch3ep1_322_a21 with dissolve
        eira "I'm so full right now...."
        mc "Yeah. Me, too."
        eira "The weather is so nice today, isn't it?"
        sally "Indeed it is. Especially, when you close your eyes and feel the air..."
        sally "*Giggles* It's so nice that makes me feel like sleeping right now."
        eira "I couldn't agree more...."
        scene ch3ep1_322_a22 with dissolve
        sally "By the way, [mc]..."
        sally "We haven't hung out in a while. How have you been?"
        mc "Pretty good. What about you?"
        sally "I've been beta testing UWO so hard for the past few weeks."
        sally "It's in the last stage now."
        mc "How was it?"
        sally "Very good. I haven't found any massive bug at all. That's a very good sign."
        mc "Well...  Our department have been working so hard. So, to hear that from you, it feels very g-"
        scene ch3ep1_322_a23 with dissolve
        mc "Huh...?"
        eira "Zzzzzz......"
        sally "*Giggles* Aw...."
        sally "*Giggles* I know that the weather is so nice, but I didn't expect her to actually fall asleep."
        scene ch3ep1_322_a24 with dissolve
        sally "Please, don't wake her up."
        sally "The doctor said that she needed to take a lot of rest in order to recover."
        mc "I thought she's already recovered. She told me that herself."
        sally "Well... She has recovered for like ninety percent, so I guess she wasn't wrong though."
        mc "Alright, that's fair enough...."
        scene black with dissolve
        $ renpy.pause()
        s "About fifteen minutes later................"
        scene ch3ep1_322_a25 with dissolve
        eira "Ummm........."
        mc "......................."
        scene ch3ep1_322_a26 with dissolve
        eira "H-Huh!!??"
        mc "Oh, you're awake now?"
        eira "I'm sorry, [mc]. I didn't mean to...."
        eira "Are your shoulder okay?"
        mc "Of course. Your head isn't that heavy."
        eira "What time is it by the way...?"
        scene ch3ep1_322_a27 with dissolve
        sally "It's fifteen to one."
        eira "What? Lunch break is almost over then."
        eira "Let's go back to the company now."
        sally "Yeah, let's go."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_322_a28 with fade
        eira "It's been a while since the last time we went to that park, right?"
        sally "I think so. The last time we went there before today, was about a month ago I guess."
        eira "It was so nice actually. I wonder why we stopped going there."
        sally "I have no idea as well. Let's go again in a couple days later."
        eira "Sure..."
        scene ch3ep1_322_a29 with dissolve
        eira "Are you going to come with us, [mc]?"
        mc "......................"
        eira "[mc]...?"
        scene ch3ep1_322_a30 with dissolve
        mc "Hm? I'm sorry.... Did you say something to me?"
        eira "Yeah. Where were you looking at?"
        mc "Nothing... Can you say what you said to me again?"
        eira "I asked if you want to go to the park with us again."
        mc "Hm? When?"
        sally "In the next couple days, but we're not sure yet."
        eira "Yeah... I'll invite you again when the time comes."
        mc "Okay...."
        $ sally_relationship += 2
        $ sally_ch3_ep1 += 2
        $ eira_relationship += 2
        $ eira_ch3_ep1 += 2
        stop music fadeout 3.0
        jump ch3ep1_beingfollowed
    else:
        scene ch3ep1_322_d1 with fade
        u "Alright..."
        u "It's lunch break now."
        u "Let's go find something to eat...."
        scene black with dissolve
        scene ch3ep1_322_d2 with dissolve
        u "What am I going to eat though...?"
        u "I'll take back my word last night. That wasn't the hardest decision I've ever had."
        u "Choosing what to eat is way more harder...."
        scene black with dissolve
        $ renpy.pause()
        s "About an hour later........."
        scene ch3ep1_322_d3 with dissolve
        u "Well... I ended up eating pizza in the end. What a wonderful choice it was..."
        u "Anyway, I'm full now...."
        u "Let's go back to the company."
        mc "......................."
        stop music fadeout 3.0
        jump ch3ep1_beingfollowed

label ch3ep1_beingfollowed:
    scene black with dissolve
    $ renpy.pause()
    s "You spent your time working until five o'clock.........."
    scene ch3ep1_323 with fade
    mc "...................."
    yui "[mc]! Wait!"
    u "Hm....?"
    scene ch3ep1_324 with dissolve
    mc "[yui]?"
    yui "*Pants* Why did you walk so fast...?"
    mc "Why did you ask me to stop? Is there something you want from me?"
    yui "*Pants* Well......."
    scene ch3ep1_325 with dissolve
    yui "Where are you going?"
    yui "Didn't [zeke] tell you that he will take us home today?"
    mc "... No, he didn't."
    yui "Why's that...?"
    scene ch3ep1_326 with dissolve
    mc "I don't know. Maybe he thought that you would tell me?"
    yui "That makes sense... My bad."
    yui "Then, are you going to go home with us?"
    mc "Actually... there is something I'm going to need to do first."
    yui "Okay. Got it."
    scene ch3ep1_327 with dissolve
    mc "See you at home..."
    yui "Alright, bye."
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep2_7.mp3" fadein 3.0
    $ bgm = "AERØHEAD - The Reckoning"
    scene ch3ep1_328 with fade
    mc ".................."
    u "Alright, let's go to the bus stop."
    scene ch3ep1_329 with dissolve
    u "Okay...."
    u "I've arrived home."
    scene ch3ep1_330 with dissolve
    u "That car again...."
    if ch3ep1_eirasallylunch == 1:
        scene ch3ep1_322_a4 with flash
        $ renpy.pause(0.5, hard=True)
        scene ch3ep1_322_a28 with flash
        $ renpy.pause(0.5, hard=True)
        scene ch3ep1_328 with flash
        $ renpy.pause(0.5, hard=True)
    else:
        scene ch3ep1_322_d2 with flash
        $ renpy.pause(0.5, hard=True)
        scene ch3ep1_322_d3 with flash
        $ renpy.pause(0.5, hard=True)
        scene ch3ep1_328 with flash
        $ renpy.pause(0.5, hard=True)
    u "It keeps following me since lunch break... as far as I noticed."
    u "I wonder who is it..."
    u "Well, let's just pretend that I still have no clue."
    scene black with dissolve
    $ renpy.pause()
    s "Later that night............."
    scene ch3ep1_331 with dissolve
    u "Alright..."
    u "It's been a couple hours now."
    u "Let's check if that car is still there."
    scene ch3ep1_332 with dissolve
    u "Yeah, it's still there..."
    u "Looks like the driver is waiting for my next move."
    u "....................."
    scene ch3ep1_333 with dissolve
    u "Well...."
    u "I can't let him continue spying on me any longer."
    u "I have to find out who's in that car...."
    scene black with dissolve
    scene ch3ep1_334 with dissolve
    u "....................."
    unknown "[mc]?"
    u "Hm...?"
    scene ch3ep1_335 with dissolve
    mc "Oh... Hi, [zeke]."
    mc "What are you doing?"
    zeke "What's up, bud."
    zeke "I just finished my dinner. I was going to my room, but then I saw you first."
    zeke "It's quite dark now. Where are you going to go?"
    scene ch3ep1_336 with dissolve
    mc "Outside."
    mc "There's a thing that I have to do now."
    zeke "Hm? Right now? What are you going to do?"
    mc "......................"
    mc "I'm quite hungry, so I think I'm going to a restaurant nearby."
    scene ch3ep1_337 with dissolve
    zeke "Alone? Do you want me to go with you?"
    mc "Thank you, but it's fine. I don't want to bother you."
    mc "Just keep going to your room. Then, do your things."
    zeke "Alright then.... See you tomorrow."
    mc "Yeah, bye."
    scene black with dissolve
    scene ch3ep1_338 with fade
    u "There it is...."
    u "I'll need to trick him into following me."
    u "Let's call a taxi and go somewhere quieter."
    scene black with dissolve
    $ renpy.pause()
    s "*Half an hour later*................"
    scene ch3ep1_339 with fade
    u "Alright...."
    u "I've arrived here. This is a good place to find out who it is, the person that keeps following me."
    u "I'll get inside the building and wait for him to follow me in."
    u "I don't know if he will fall into the plan though. I hope he will."
    scene ch3ep1_340 with dissolve
    s "*Break souns*....................."
    unknown "Why is he coming to an abandoned warehouse at night like this?"
    unknown "I can already smell something fishy now...."
    scene black with dissolve
    $ renpy.pause()
    s "*About an hour later*.............."
    scene ch3ep1_341 with dissolve
    unknown "(Fuck... It's been an hour.)"
    unknown "(Why hasn't he come out yet?)"
    unknown "(I wonder what he is doing in there. I need to find it out.)"
    scene ch3ep1_342 with dissolve
    unknown "(What the fuck...?!)"
    unknown "(Why is there no one in here?)"
    unknown "(Could it be that he already knew I was following him, so he ran away?)"
    unknown "(But... he didn't even get out of the building. I watched the entrance for a whole time.)"
    unknown "(Wait?! Coult it be that there is an exit door at the back?!)"
    unknown "(Fuck! I have to check it out!)"
    scene ch3ep1_343 with dissolve
    stop music fadeout 3.0
    unknown "(What the hell...?)"
    unknown "(It's a dead end at the back...)"
    unknown "(Then, where the hell has he gone...?)"
    scene ch3ep1_344 with dissolve
    play music "sfx/ep.3/ep3_7.mp3" fadein 3.0
    $ bgm = "Jeff II - Heartfül of Kerøsene"
    mc "Are you looking for me...?"
    unknown "H-Huh!!??"
    scene ch3ep1_345 with vpunch
    unknown "Fuck off...!"
    mc "Well... We didn't meet for such a long time. Yet the first thing you do when we meet again, is kicking me?"
    mc "You make me sad, [tobi]...."
    scene ch3ep1_346 with dissolve
    mc "Hey... Where are you going?"
    mc "Are you not even going to greet me?"
    tobi "Fuck you...!"
    mc "Why are you running away from me?"
    scene ch3ep1_347 with dissolve
    mc "Come back here, [tobi]."
    tobi "Why the hell would I do that for?"
    tobi "I know I can't fight you! You're just going to beat the crap out of me!"
    tobi "I'm going to report this to [victor]!"
    mc "Well...."
    scene ch3ep1_348 with dissolve
    mc "I'm sorry, but I can't let that happen."
    tobi "Eek! Stop right there! Don't get any closer!"
    mc "Too bad... I can't do that."
    scene ch3ep1_349 with dissolve
    mc "Got you...."
    tobi "Fuck...!!!"
    scene black with dissolve
    scene ch3ep1_350 with dissolve
    tobi "Ughh...! Let go off me!"
    mc "Why did [victor] send you to spy on me?"
    mc "There's a couple days left until the day I have to give him the blueprint."
    mc "Is he planning on doing something behind my back?"
    scene ch3ep1_351 with dissolve
    tobi "Ugh...! I don't know!"
    mc "What do you mean you don't know?"
    mc "[victor] sent you here."
    tobi "Because he didn't tell me no shit! He just told me to follow you! That's it!"
    mc "Stop lying."
    scene ch3ep1_352 with dissolve
    tobi "Ugh!! I'm not fucking lying!"
    tobi "Why don't you call him and ask him yourself?!"
    u "Hm? Since when has he become so strong like this?"
    u "I've never lost to him when it comes to physical strength, but now he's slightly lifting me up."
    u "This is not getting good. I have to stop him...."
    scene ch3ep1_353 with dissolve
    tobi "*Coughs* I- I can't... breathe...."
    mc "What is [victor] planing to do?"
    tobi "*Coughs* Ugh...! I.... don't know...!"
    mc "Stop lying."
    scene ch3ep1_354 with dissolve
    tobi "*Coughs* I- I... told you.... I- I'm not lying...!"
    mc "......................"
    tobi "L-Let me... go...."
    scene ch3ep1_355 with dissolve
    u "Well... He's already passed out."
    u "It's been a while since the last time I met him."
    u "Looks like he's got stronger than before."
    u "Or could it be that... I've become weaker?"
    u "Yeah... that makes sense since I haven't been training recently."
    scene black with dissolve
    scene ch3ep1_356 with dissolve
    u "........................."
    u "What am I going to do to him now?"
    u "I can't let him run back to [victor]."
    scene ch3ep1_357 with dissolve
    u "I have to keep him somewhere he can't get out."
    u "Well... Looks like I'm going to have to take him to that place."
    u "Let's hurry up. I need to get there before he wakes up."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_358 with fade
    tobi ".................."
    scene ch3ep1_359 with dissolve
    tobi "Mmmm...."
    scene ch3ep1_360 with dissolve
    tobi "(Oh, shit!!)"
    tobi "(Where the fuck I am....?)"
    scene ch3ep1_361 with dissolve
    tobi "(Ugh...!!)"
    tobi "(Why can't I move my arms?!)"
    tobi "(What the fuck is this?! A handcuff?!)"
    scene ch3ep1_362 with dissolve
    mc "Oh... You're awake now."
    tobi "[mc]!!!"
    tobi "What the fuck is this place!!??"
    tobi "Let me go!!!"
    scene ch3ep1_363 with dissolve
    mc "Calm down, [tobi]."
    mc "Let's talk."
    tobi "Talk my ass!"
    tobi "At first I wondered why [victor] told me to spy on you, but I think I know the reason now!"
    scene ch3ep1_364 with dissolve
    tobi "You must have been doing something unrelated to the original plan."
    tobi "It must be something that you don't really want [victor] to know about."
    tobi "Otherwise, you wouldn't have lured me to that abandoned warehouse just to bring me here."
    tobi "Am I right?!"
    scene ch3ep1_365 with dissolve
    mc "Yeah, you're right."
    mc "You might not be so good at fighting, but your ability to understand things quickly can't be underestimated."
    mc "Let me ask you one thing."
    mc "Don't you want to live your own life? A life that really belongs to you, not [victor]."
    scene ch3ep1_364 with dissolve
    tobi "What the fuck?!"
    tobi "Don't tell me you're planning on betraying him?!"
    scene ch3ep1_365 with dissolve
    mc "Yes, I am."
    scene ch3ep1_366 with dissolve
    tobi "What? Are you out of your mind?"
    mc "No, I'm not. I've thought about it very carefully."
    mc "Have you not seen the way [victor] eliminates one of us when he failed his mission?"
    mc "No matter how many times you succeeded your mission, one failure and you get your throat cut."
    scene ch3ep1_367 with dissolve
    mc "If he knew that you failed to spy on me, you would have been killed already by now."
    mc "We're nothing, but a tool for him."
    mc "How long are you going to live your life like that?"
    tobi ".........................."
    scene ch3ep1_368 with dissolve
    mc "I just got some information that widely opened my eyes."
    tobi "What's it?"
    mc "I'm not going to tell you about it now."
    mc "But, I can't work for [victor] anymore. I'm going to destroy him."
    mc "Are you going to join me?"
    scene ch3ep1_369 with dissolve
    tobi "You're surely out of your mind, [mc]."
    tobi "Who's going to destroy [victor]? You?"
    tobi "Do you really think you can do that?"
    tobi "Even a police failed to do that, who do you think you are?"
    mc "........................."
    scene ch3ep1_370 with dissolve
    mc "Alright...."
    mc "I understand now that I'm just wasting my time here."
    mc "You weren't going to listen to me in the first place."
    scene ch3ep1_371 with dissolve
    mc "Too bad for you. I can't let you run back to [victor]."
    mc "So, you're going to have to be imprisoned here until everything is done."
    tobi "Hey! That's bullshit?!"
    tobi "You can't lock me up here! Release me!!"
    scene ch3ep1_372 with dissolve
    mc "Don't worry. I'm sure that you'll be fine."
    mc "This isn't the first time you are locked up."
    mc "Actually we've even gone through a lot worse."
    tobi "Hey! Come back here!"
    scene ch3ep1_373 with dissolve
    tobi "[mc]!!!"
    tobi "Don't you fucking hear me??!!"
    tobi "I said release me!!!"
    mc "Good luck...."
    tobi "Fuck you!!!"
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_374 with fade
    u "Alright, I'm back...."
    u "I still can't believe [victor] actually sent someone to spy on me."
    u "I wonder why he does that. He's never done that to me before."
    u "Well... I can't figure it out by just thinking about it."
    u "It's quite late at night now. I should go take a bath, then go to bed..."
    scene black with dissolve
    $ renpy.pause()
    s "Fifteen minutes later.............."
    play music "sfx/Nextday.mp3" fadein 4.0
    $ bgm = "Bensound - Perception"
    scene ch3ep1_375 with dissolve
    u "Alright... Let's go to b-"
    s "*Phone vibrates*...................."
    u "Hm...? Why does everyone always call me at a late night like this recently?"
    u "Let's check who it is..."
    scene ch3ep1_376 with dissolve
    u "Oh...."
    u "It's [mila]."
    u "Well... I hope it's a great news."
    scene ch3ep1_377 with dissolve
    mc "Hello...."
    scene ch3ep1_378 with fade
    mila "[mc]...."
    mila "I've heard about you now."
    mila "How could you do that...?"
    mila "I can't believe you actually did that to me..."
    scene ch3ep1_382 with dissolve
    mc "......................"
    u "What's she talking about...?"
    u "Could it be... that she already knows I'm going to betray her grandfather?"
    u "Wait... that's impossible. No one knows about this, except [tobi]."
    u "I already locked him up very well. There is no way she could have heard that from him."
    scene ch3ep1_379 with dissolve
    u "Let's try playing dumb...."
    mc "What are you talking about?"
    mc "I don't understand. What did I do to you?"
    scene ch3ep1_380 with dissolve
    mila "*Sighs* I heard that you'll have to finish your mission this Friday."
    mila "Why didn't you tell me about it?"
    mila "Don't you know how long I have been waiting for you to come back here?"
    mila "I miss you so much. You're going to come back here once you succeed your mission, right?"
    scene ch3ep1_377 with dissolve
    u "*Sighs* What a relief.... I thought I've already got caught."
    mc "I'm sorry. I've been very busy lately since I only have a few days left to finish the mission."
    mc "And yeah, I'm going to get back there after I succeed the mission. Don't worry."
    mc "There is no reason for me to stay here any longer, isn't it?"
    scene ch3ep1_381 with dissolve
    mila "*Smiles* Okay, I understand you now."
    mila "I'm sorry for being a bit paranoid earlier..."
    mila "I'm glad to hear that you're coming back soon. I can't wait to be with you again."
    scene ch3ep1_379 with dissolve
    mc ".................."
    mc "Me, too...."
    mc "[mila]. I've got to go now. I'm very tired and sleepy."
    scene ch3ep1_381 with dissolve
    mila "Oh? Okay, sure."
    mila "Have a good night, [mc]."
    mila "See you soon."
    scene ch3ep1_382 with dissolve
    mc "Yeah, see you soon."
    mc "Good night. Bye."
    scene black with dissolve
    scene ch3ep1_383 with dissolve
    u "I completely forgot about [mila]....."
    u "What am I going to do to her now?"
    u "I mean... [victor] might be evil, but [mila] is not."
    u "She's just hard to understand sometimes. However, she's the only person over there who has never looked at me as a tool."
    scene ch3ep1_384 with dissolve
    s "*Stomach grows*............"
    u "... What? I already had dinner, but I'm getting hungry again?"
    u "Well... perhaps it's because I spent quite a lot of energy tonight."
    u "What should I do?"
    menu:
        "Go to the kitchen [smrec]":
            scene ch3ep1_386 with dissolve
            u "I can't sleep while still feeling hungry like this."
            u "Let's go to the kitchen and find something to need."
            u "I hope there is still a cup noodle left...."
            if ch2ep2letyuisleep == 1:
                scene black with dissolve
                $ renpy.pause()
                scene ch3ep1_387 with dissolve
                mc "Hm...?"
                yui "Oh...?"
                scene ch3ep1_388 with dissolve
                mc "Hi, [yui]."
                mc "Are you having a supper?"
                yui "Yeah... I stayed up late tonight, and felt a little bit hungry. So..."
                mc "I see...."
                scene ch3ep1_389 with dissolve
                yui "Are you going to have a supper, too?"
                mc "Yeah. I feel a little bit hungry as well."
                mc "Is there still a cup noodle left?"
                yui "Yes, there is. Go take one and sit with me."
                mc "Sure."
                scene black with dissolve
                $ renpy.pause()
                s "You spent some time eating with [yui]......."
                scene ch3ep1_390 with dissolve
                yui "I'm full now...."
                mc "Me, too..."
                yui "To think about it, it's been quite a while since the last time we spent time together alone."
                mc "Yeah... I think so."
                yui "Since we're finally alone, why don't we....?"
                mc "Hm...?"
                scene ch3ep1_391 with dissolve
                mc "Wait... What the...?"
                mc "Why did you suddenly...?"
                yui "*Giggles* Hehe...."
                scene ch3ep1_392 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_392.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_392_blink.jpg", 1) with dissolve
                mc "What are you doing, [yui]?"
                yui "Like I said... It's really been a while."
                yui "Women get horny, too... You know?"
                mc "Are you for real? Out of sudden?"
                yui "*Giggles* Yes, I am..."
                yui "I'm going to unzip your pants now... Can I?"
                mc "......................."
                $ ch3ep1_yuisupper = 1
                jump ch3ep1part2_end
            else:
                scene black with dissolve
                $ renpy.pause()
                jump ch3ep1part2_end
        "Go to bed":
            scene ch3ep1_385 with dissolve
            u "It's so late now... I shouldn't eat any more."
            u "I will wait until morning and eat."
            u "Let's just sleep right away."
            scene black with dissolve
            $ renpy.pause()
            jump ch3ep1part2_end
label ch3ep1part2_end:
    if ch3ep1_yuisupper == 1:
        menu:
            "Go ahead. Unzip it. [yui2]":
                $ yui_ch3_ep1 += 2
                $ yui_relationship += 2
                $ ch3ep1_yuisuppersex = 1
                jump ch3ep1_yuisex
            "I'm not in a mood today.":
                scene ch3ep1_393_d1 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_393_d1.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_393_d1_blink.jpg", 1) with dissolve
                mc "Sorry, [yui]."
                mc "I'm not in a mood today."
                yui "Not even a littie bit...?"
                mc "No... I really want to go sleep now."
                yui "........................."
                yui "Alright...."
                scene black with dissolve
                scene ch3ep1_393_d2 with dissolve
                mc "I'm leaving now."
                yui "......................"
                mc "Have a good night, [yui]."
                yui "......................"
                yui ".... Good night."
                $ ch3ep1_yuisuppersex = 2
                jump ch3ep1_part3begins

    else:
        jump ch3ep1_part3begins
label ch3ep1_yuisex:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    scene ch3ep1_393_a1 at eyesblink("Ch.3/Ep.1/Scenes/ch3ep1_393_a1.jpg", "Ch.3/Ep.1/Scenes/ch3ep1_393_a1_blink.jpg", 1) with dissolve
    mc "Go ahead. Unzip it."
    yui "*Smiles* That's what I've been waiting to hear from you."
    yui "*Smiles* Alright then...."
    yui "*Smiles* I'm going to unzip your pants now."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_393_a2 with dissolve
    play music "sfx/ch2ep2_6.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - Sicked & Tired (ft. Lily Hain)"
    yui "Well... Well... Well...."
    yui "I was thinking what I should do to make you horny, but it's pointless now."
    yui "You've been ready for some time already..."
    mc "Any man gets a boner if there is a girl's face right in front of his dick this close..."
    yui "*Giggles* Nice excuse....."
    scene black with dissolve
    scene ch3ep1_393_a3 with dissolve
    yui "*Sucks* Mmmm... Let me..."
    show ch3ep1_yui1
    yui "*Sucks* Make you... Mmmmm...."
    yui "*Sucks* Feel a little bit.... better...."
    $ renpy.pause()
    hide ch3ep1_yui1
    scene ch3ep1_393_a4 with dissolve
    show ch3ep1_yui2
    yui "*Sucks* Mmmm.... This taste....."
    yui "*Sucks* Mhmmm.... It's been a while...."
    yui "*Sucks* Mmmm.... I miss it so much...."
    $ renpy.pause()
    hide ch3ep1_yui2
    scene ch3ep1_393_a5 with dissolve
    show ch3ep1_yui3
    mc "*Softly breathes* Ahhh....."
    mc "*Softly breathes* Since when did you become this good....?"
    yui "*Sucks* Hehe...."
    $ renpy.pause()
    hide ch3ep1_yui3
    scene ch3ep1_393_a6 with dissolve
    mc "Hold on a minute...."
    yui "Hm...? Why did you stop me...?"
    mc "Let me please you, too."
    mc "Get up and take off your pants."
    yui "*Giggles* As you wish...."
    scene black with dissolve
    scene ch3ep1_393_a7 with dissolve
    yui "*Smiles* Alright, I did what you said."
    yui "What do I have to do next?"
    mc "Just lean against the table and spread your legs a little bit more."
    yui "*Smiles* Alright...."
    scene ch3ep1_393_a8 with dissolve
    yui "Like this...?"
    mc "Yeah...."
    mc "Now, let me get you ready."
    yui "*Giggles* Can't wait...!"
    scene ch3ep1_393_a9 with dissolve
    show ch3ep1_yui4
    yui "*Softly breathes* A-Arrh...."
    yui "*Softly breathes* [mc]....."
    $ renpy.pause()
    hide ch3ep1_yui4
    scene ch3ep1_393_a10 with dissolve
    show ch3ep1_yui5
    yui "*Moans* Mhmmm...! Y-Yeah... That spot..."
    yui "*Moans* Ahhh.... Keep moving your tongue like that...."
    $ renpy.pause()
    hide ch3ep1_yui5
    scene ch3ep1_393_a11 with dissolve
    show ch3ep1_yui6
    yui "*Heavily breathes* A-Ahhh...! D-Don't stop...!"
    yui "*Heavily breathes* M-Mhmmm....! A-Arrr....!"
    $ renpy.pause()
    hide ch3ep1_yui6
    scene ch3ep1_393_a12 with dissolve
    yui "[mc]. S-Stop...."
    mc "Hm...? What's wrong?"
    yui "I can't hold it anymore. I want your... dick... inside me now."
    mc "Alright then...."
    scene black with dissolve
    scene ch3ep1_393_a13 with dissolve
    yui "Come on! What are you waiting for?!"
    yui "Hurry up and put it in already!"
    mc "Okay...."
    mc "... As you wish."
    scene ch3ep1_393_a14 with dissolve
    show ch3ep1_yui7
    $ renpy.pause(6, hard=True)
    scene ch3ep1_393_a15 with dissolve
    hide ch3ep1_yui7
    yui "*Softly breathes* A-Ahhhh....."
    yui "*Softly breathes* Finally...."
    yui "Go ahead. Do me however you want to...."
    mc ".... Okay."
    scene ch3ep1_393_a16 with dissolve
    show ch3ep1_yui8
    yui "*Softly breathes* Hahhhh....."
    yui "*Softly breathes* Mhmmmm..... This feeling.... I miss it so much...."
    $ renpy.pause()
    hide ch3ep1_yui8
    scene ch3ep1_393_a17 with dissolve
    show ch3ep1_yui9
    yui "*Moans* Ahhhh.... [mc]......"
    mc "*Softly breathes* Are you enjoying it now?"
    yui "*Moans* Hah..... Of course, I am...."
    $ renpy.pause()
    hide ch3ep1_yui9
    scene ch3ep1_393_a18 with dissolve
    show ch3ep1_yui10
    yui "*Heavily breathes* A-Ahhh...! A-Ahhh...!!"
    mc "*Softly breathes* Shhh... Don't moan too loud...."
    yui "*Heavily breathes* Mhhmmm....! I-I'm trying, but it feels too good....!"
    $ renpy.pause()
    hide ch3ep1_yui10
    scene ch3ep1_393_a19 with dissolve
    mc "[yui]."
    yui "Hm...? I was feeling so good.... Why did you stop...?"
    mc "I want to do it in another position."
    yui "... How do you want to do it then?"
    mc "Turn around and bend over."
    yui "Got it...."
    scene black with dissolve
    scene ch3ep1_393_a20 with dissolve
    yui "Like this....?"
    mc "Yeah...."
    yui "Then, don't waste any more time. Put it in already."
    scene ch3ep1_393_a21 with dissolve
    mc "As you wish...."
    show ch3ep1_yui11
    $ renpy.pause(4, hard=True)
    scene ch3ep1_393_a22 with dissolve
    hide ch3ep1_yui11
    yui "*Softly breathes* Arrrr......"
    scene ch3ep1_393_a23 with dissolve
    show ch3ep1_yui12
    yui "*Softly breathes* Your cock keeps touching my womb so hard in this position...."
    yui "*Softly breathes* Ahhh.... It's driving me crazy...."
    $ renpy.pause()
    hide ch3ep1_yui12
    scene ch3ep1_393_a24 with dissolve
    show ch3ep1_yui13
    mc "*Softly breathes* I never knew you were this naughty...."
    yui "*Moans* Shut up... Mhmm... You have no rights to say that."
    yui "*Moans* Hahh.... You're the one... Mhmmm.... making me this way...."
    $ renpy.pause()
    hide ch3ep1_yui13
    scene ch3ep1_393_a25 with dissolve
    show ch3ep1_yui14
    yui "*Heavily moans* A-Ahhhh....!!"
    yui "*Heavily moans* S-Sorry... I didn't mean to.... Mhhmmm.... moan that loud, but.... Ahhh.... I couldn't have controlled myself...."
    yui "*Heavily moans* I... I'm... about to cum....!!"
    mc "Me, too...."
    yui "*Heavily moans* Cum inside me.... I'm on safe days now...."
    menu:
        "Missionary":
            hide ch3ep1_yui14
            jump ch3ep1_yuimis1
        "Slowest":
            hide ch3ep1_yui14
            jump ch3ep1_yuidoggy1
        "Slower":
            hide ch3ep1_yui14
            jump ch3ep1_yuidoggy2
        "Cum":
            jump ch3ep1_yuidoggycum
label ch3ep1_yuimis1:
    scene ch3ep1_393_a16 with dissolve
    show ch3ep1_yui8
    window hide
    $ renpy.pause()
    menu:
        "Standing Doggy":
            hide ch3ep1_yui8
            jump ch3ep1_yuidoggy1
        "Faster":
            hide ch3ep1_yui8
            jump ch3ep1_yuimis2
        "Fastest":
            hide ch3ep1_yui8
            jump ch3ep1_yuimis3
label ch3ep1_yuimis2:
    scene ch3ep1_393_a17 with dissolve
    show ch3ep1_yui9
    window hide
    $ renpy.pause()
    menu:
        "Standing Doggy":
            hide ch3ep1_yui9
            jump ch3ep1_yuidoggy1
        "Slower":
            hide ch3ep1_yui9
            jump ch3ep1_yuimis1
        "Faster":
            hide ch3ep1_yui9
            jump ch3ep1_yuimis3
label ch3ep1_yuimis3:
    scene ch3ep1_393_a18 with dissolve
    show ch3ep1_yui10
    window hide
    $ renpy.pause()
    menu:
        "Standing Doggy":
            hide ch3ep1_yui10
            jump ch3ep1_yuidoggy1
        "Slowest":
            hide ch3ep1_yui10
            jump ch3ep1_yuimis1
        "Slower":
            hide ch3ep1_yui10
            jump ch3ep1_yuimis2
label ch3ep1_yuidoggy1:
    scene ch3ep1_393_a23 with dissolve
    show ch3ep1_yui12
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch3ep1_yui12
            jump ch3ep1_yuimis1
        "Faster":
            hide ch3ep1_yui12
            jump ch3ep1_yuidoggy2
        "Fastest":
            hide ch3ep1_yui12
            jump ch3ep1_yuidoggy3
label ch3ep1_yuidoggy2:
    scene ch3ep1_393_a24 with dissolve
    show ch3ep1_yui13
    window hide
    $ renpy.pause()
    menu:
        "Missionary":
            hide ch3ep1_yui13
            jump ch3ep1_yuimis1
        "Slower":
            hide ch3ep1_yui13
            jump ch3ep1_yuidoggy1
        "Faster":
            hide ch3ep1_yui13
            jump ch3ep1_yuidoggy3
label ch3ep1_yuidoggy3:
    scene ch3ep1_393_a25 with dissolve
    show ch3ep1_yui14
    window hide
    menu:
        "Missionary":
            hide ch3ep1_yui14
            jump ch3ep1_yuimis1
        "Slowest":
            hide ch3ep1_yui14
            jump ch3ep1_yuidoggy1
        "Slower":
            hide ch3ep1_yui14
            jump ch3ep1_yuidoggy2
        "Cum":
            jump ch3ep1_yuidoggycum
label ch3ep1_yuidoggycum:
    menu:
        "Cum inside":
            $ ch3ep1_yuicum = 1
        "Cum outside":
            $ ch3ep1_yuicum = 2
    scene black with dissolve
    scene ch3ep1_393_a26 with vpunch
    yui "I'm cumming.....!!!!"
    scene ch3ep1_393_a26 with vpunch
    yui "Mhmmmmm.....!!!!"
    if ch3ep1_yuicum == 1:
        scene ch3ep1_393_a26_in1 with vpunch
        mc "I'm cumming, too..."
        mc "Ugh..."
        yui "*Pants*..............."
        scene ch3ep1_393_a26_in2 with dissolve
        mc "I'm pulling it out now..."
        yui "*Pants* You came quite a lot...."
        yui "*Pants* I can tell that... hehe..."
    elif ch3ep1_yuicum == 2:
        scene ch3ep1_393_a26_out1 with vpunch
        mc "I'm cumming, too..."
        mc "Ugh..."
        yui "*Pants*..............."
        scene ch3ep1_393_a26_out2 with dissolve
        yui "*Pants* You came quite a lot...."
        yui "*Pants* I can tell that... hehe..."
        yui "*Pants* I can feel your semen on my butt...."
    scene black with dissolve
    stop music fadeout 3.0
    scene ch3ep1_393_a27 with dissolve
    yui "*Pants* I almost.... lost my breath.... the moment I had an orgasm..."
    yui "*Pants* I'm so... exhausting.... right now."
    yui "*Pants* Let me stay like this... and rest for a sec...."
    mc "Okay..."
    scene ch3ep1_393_a28 with dissolve
    unknown "*Laughs* Hahaha... This is so funny...."
    yui "!!!!"
    yui "*Whispers* Someone is coming, [mc]!"
    mc "*Whispers* Yeah, I think so."
    yui "*Whispers* Let's hurry up and get dressed! I don't want to get caught."
    mc "Either am I..."
    scene ch3ep1_393_a29 with dissolve
    rin "Oh my....!!!"
    rin "[mc]. [yui]. You almost gave me a heart attack..."
    mc "Hello, [rin]."
    scene ch3ep1_393_a30 with dissolve
    yui "H-Hi, [rin]!!"
    yui "W-Why are you up so late tonight? C-Can't sleep?"
    mc "*Whispers* Hey... You're acting so suspicious."
    yui "*Whispers* Tell me something I don't know."
    scene ch3ep1_393_a31 with dissolve
    rin "I took a nap for a couple hours after getting home."
    rin "So yeah, I'm not quite sleepy right now."
    rin "What were you guys whispering about though?"
    mc "Nothing. Don't mind us."
    mc "What brings you here by the way?"
    scene ch3ep1_393_a32 with dissolve
    rin "Oh... I just want to grab a bottle of water. What about you guys?"
    rin "What were you guys doing here at late night like this?"
    yui "We were having supper! You see these cups of noodles, right?!"
    yui "We were about to clean up, then you showed up first!"
    rin "Oh, I see..."
    scene ch3ep1_393_a33 with dissolve
    mc "Please, excuse me..."
    rin "Hm...?"
    mc "I think I should go back to my room since I'm done eating now."
    yui "Y-Yeah! It's so late now. You should go back to you room."
    mc "Have a good night, both of you."
    rin "Thank you. You, too."
    $ renpy.end_replay()
    jump ch3ep1_part3begins
label ch3ep1_part3begins:
    scene black with dissolve
    $ renpy.pause()
    s "Next morning.........."
    play music "sfx/ch1ep2.mp3"
    $ bgm = "Bensound - Little Idea"
    scene ch3ep1_394 with dissolve
    zeke "Okay, guys...."
    zeke "You haven't forgotten anything, right?"
    mc "No, I'm not."
    rin "Me, too. I've got everything I need in this bag already."
    zeke "Alright then, let's go to the company."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_395 with fade
    mc "......................"
    yui "....................."
    scene ch3ep1_396 with dissolve
    s "*Phone vibrates*..............."
    u "Hm....?"
    scene ch3ep1_397 with dissolve
    u "Oh... It's [felix]."
    u "Why is he calling me now?"
    u "I guess it must be something important."
    scene ch3ep1_398 with dissolve
    mc "[yui]."
    yui "Hm? What?"
    mc "Go in first. I've got to pick up this call."
    yui "Oh, okay."
    scene black with dissolve
    scene ch3ep1_399 with dissolve
    mc "Hello. Hang on a sec."
    mc "I can't talk with you right now."
    mc "I'll call you back in five minutes."
    scene ch3ep1_400 with dissolve
    u "This area is too open."
    u "I need to find somewhere more private."
    u "Even though I'm pretty sure there is no one working for [victor] in this company, it's better safe than sorry."
    scene black with dissolve
    scene ch3ep1_401 with dissolve
    u "Well...."
    u "This toilet would work."
    u "Let's make sure no one is here before calling him back."
    scene black with dissolve
    scene ch3ep1_402 with dissolve
    mc "Alright...."
    mc "I can talk now. What's up?"
    mc "Why did you call me?"
    scene ch3ep1_406 with fade
    felix "As expected..."
    felix "You're such a cautious person. That's good."
    felix "Well, I decided to call you because it's been a few days, and I wanted to keep you updated."
    scene ch3ep1_403 with dissolve
    mc "Keep me updated?"
    mc "About what?"
    scene ch3ep1_408 with dissolve
    felix "I've cleaned up almost ninety percent of the police department."
    felix "Most of the police that work for [victor] has already been arrested."
    felix "There are a few of them left. They're pretty big ones."
    felix "So, they're a little bit hard to deal with."
    scene ch3ep1_403 with dissolve
    u "[victor] must be having a hard time right now."
    u "No wonder why he sent [tobi] to spy on me."
    u "I guess he wanted to find out who's the person causing this mess."
    u "Other kids who are on their missions right now must have been spying on as well..."
    scene ch3ep1_404 with dissolve
    mc "That's a very good news."
    mc "Thank you for keeping me updated."
    mc "Well... since we're already talking, I also have something to inform you."
    mc "[victor] sent one of his men to spy on me"
    mc "But, you don't need to be worried. I've already got him."
    scene ch3ep1_408 with dissolve
    felix "Hm? He's suspecting you already?"
    felix "How come? I'm pretty sure that you and I have never met in a public place."
    scene ch3ep1_405 with dissolve
    mc "I dont't think he's suspecting me now."
    mc "I think he just sent his men to spy on everyone that isn't there with him."
    mc "I'm not quite sure, but the possibility is high."
    mc "He must have been so nervous. No one has ever managed to get rid of a lot of his men this quickly."
    scene ch3ep1_407 with dissolve
    felix "Well... I'm glad to hear that."
    felix "I'll everything I can to get on his nerves."
    felix "As soon as he has lost it, that will be his weakest moment."
    scene ch3ep1_403 with dissolve
    mc "...................."
    mc "I hope so."
    mc "By the way, I think I'm going to tell my friends about everything. What do you think?"
    scene ch3ep1_409 with dissolve
    felix "Are you sure you can trust them though?"
    felix "And don't you think you're only going to put them in danger?"
    scene ch3ep1_402 with dissolve
    mc "They're not involved with [victor]. I'm positive."
    mc "I think [victor]'s going to destroy everyone around me once he knows I betrayed him."
    mc "He will not care if those people know about him or not. He'll get rid of them no matter what."
    mc "So, I think it'd be better for them to know about everything."
    mc "They need to know what are coming for them so that they can prepare themselves."
    scene ch3ep1_409 with dissolve
    felix "......................"
    felix "... Yeah, you're right."
    felix "I'll find a way to keep your friends safe as well."
    scene ch3ep1_405 with dissolve
    mc "Thank you."
    mc "Alright, that'd be it for today."
    mc "I'm going to hang up now...."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_410 with dissolve
    u "Okay...."
    u "Now, I need to inform [maya] and [rowan] that I'm going to tell everyone the truth."
    u "I want to know what they think about me doing that."
    u "Let's send them a message...."
    scene ch3ep1_411 with dissolve
    u "Alright...."
    u "It's all done."
    u "Now, let's go back to the department."
    u "It's time for work now."
    scene black with dissolve
    $ renpy.pause()
    s "A few hours later........."
    scene ch3ep1_412 with fade
    mc "..................."
    s "*Phone vibrates*............."
    u "Hm...? Did I just get a new message?"
    u "Let's check it...."
    scene ch3ep1_413 with dissolve
    u "Well... This is unexpected."
    u "[maya] and [rowan] agree with me telling them the truth."
    u "I thought they were going to disagree."
    scene ch3ep1_414 with dissolve
    u "Alright, now I just have to invite everyone."
    u "Let's just send them a message and tell them to come to my house this evening."
    u "'Hey, it's me, [mc]. I have something to tell you all. It's very important. Please, come to my house this evening.'..."
    u "Alright, I think that'd work."
    scene black with dissolve
    scene ch3ep1_415 with dissolve
    yui "[mc]."
    mc "Hm, [yui]?"
    yui "I've just got a message from an unknown phone number. The message said it was you. Did you send it?"
    mc "Yes, it's really me."
    scene ch3ep1_416 with dissolve
    yui "Hm? Then, how come the number was shown as unknown?"
    yui "I thought I already had your contact."
    mc "Because it's a new number. That's why."
    mc "I just got it not so long ago."
    scene ch3ep1_417 with dissolve
    yui "What? Why did you change your number?"
    mc "I didn't change it, but...."
    mc "It's complicated. I will tell you and everyone this evening."
    yui "What's it all about? Can't you tell me now?"
    mc "Sorry. I want to tell everyone at the same time."
    yui "*Sighs* Alright then...."
    scene ch3ep1_418 with dissolve
    mc "Let's go have lunch outside. Do you want to come with me?"
    yui "Thanks, but I'm good."
    yui "I feel like having lunch at the cafeteria today."
    mc "Okay. You do you."
    mc "See you later then."
    yui "Yeah, see you later."
    scene black with dissolve
    $ renpy.pause()
    s "You went to have lunch, then came back to the company....."
    scene ch3ep1_419 with fade
    u "Alright...."
    u "Let's go back to work."
    mc "......................."
    u "Hold on...."
    u "I feel like I've forgetten something...."
    scene ch3ep1_420 with dissolve
    u ".........................."
    u "Oh, I forgot to invite [alice]."
    u "Should I tell her about everything, too?"
    u "It's true that she has nothing to do at all with the company and Xecon's gear."
    if ep3invitealice == 2:
        u "Even though we are nothing to each other, [victor] might do something bad to her."
    if ep3invitealice == 1:
        u "But, I still keep in touch with her, so [victor] might do something bad to her."
    scene ch3ep1_421 with dissolve
    if ep3invitealice == 2:
        u "I don't know if she will pick up and phone and accept my invitation, but I should try it just for her sake."
        mc ".........................."
        u "Oh? She've picked up my call."
        mc "Hello, [alice]..."
    if ep3invitealice == 1:
        u "Let's just call her. She deserves to know everything just like everyone does."
        mc ".........................."
        mc "Hello, [alice]..."
    scene ch3ep1_424 with fade
    alice "[mc]....?"
    alice "What a surprise. I didn't expect you to call me at all..."
    alice "Did you change your number by the way?"
    scene ch3ep1_422 with dissolve
    mc "It's complicated...."
    if ep3invitealice == 2:
        mc "Look. I know I was mean to you when you paid me a visit. I'm sorry for that."
        mc "I know I have no right to call you, but I need to let you know something."
    if ep3invitealice == 1:
        mc "Look. There is something I need to tell you."
    mc "It's very important."
    scene ch3ep1_425 with dissolve
    if ep3invitealice == 2:
        alice "*Smiles* It's okay. There is no need to say sorry. I've already moved on now."
        alice "Thank you for calling me though. It must have taken a lot of guts for you to do that."
        alice "What's the thing you need to let me know by the way?"
    if ep3invitealice == 1:
        alice "Hm? How important is it?"
        alice "Should we meet so that you can tell me in person?"
        alice "I think it'll be better that way."
    scene ch3ep1_423 with dissolve
    if ep3invitealice == 2:
        mc "Thank you for saying that."
        mc "The thing is... it's going to take quite a lot of time. I can't tell you now."
    if ep3invitealice == 1:
        mc "Yeah, that's what I was about to say."
    mc "Are you free this evening?"
    mc "Could you please come to my house?"
    scene ch3ep1_426 with dissolve
    alice "This evening......?"
    alice "Umm.... Yeah, I think I can go there."
    alice "What time do I need to go?"
    scene ch3ep1_421 with dissolve
    mc "I'll arrive at the house around 5.30 p.m."
    mc "So, between half past five to six o'clock is fine."
    scene ch3ep1_426 with dissolve
    alice "Okay, I get it."
    alice "See you this evening. Bye."
    scene ch3ep1_421_d with dissolve
    u "Okay, that's it..."
    u "Now, let's just go back to work..."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time working until 5 o'clock........."
    stop music fadeout 3.0
    scene ch3ep1_427 with fade
    zeke "Hey, [mc]!"
    zeke "[yui]!"
    u "Hm....?"
    scene ch3ep1_428 with dissolve
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    zeke "How was your work today, guys?"
    mc "Not as hard as a few days ago."
    mc "Why are you guys here though?"
    mc "I thought you were going to wait for us at the first floor."
    scene ch3ep1_429 with dissolve
    zeke "Because I'm so excited that I couldn't wait to see your face!"
    zeke "I've never expected you to invite someone home before!"
    zeke "If I haven't heard it wrong, you invited a lot of people today."
    zeke "How come?"
    mc "Well... I have something very important to tell you guys. So, it's better to tell you all at the same time."
    scene ch3ep1_430 with dissolve
    mc "Are you okay about that, [rin]?"
    mc "Is it too much for you that I asked you to cook for everyone?"
    rin "Not at all. It's been a while since the last time I cooked for you guys anyway."
    rin "So, I'm fine with that."
    yui "I'll help you, [rin]."
    mc "Thank you, guys..."
    zeke "Alright, let's get going then."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_431 with fade
    sally "Oh...?!"
    zeke "Oh...?!"
    u "Hm...?"
    scene ch3ep1_432 with dissolve
    sally "Hi, everyone!"
    zeke "Hello, [sally]! Hi, [eira]!"
    rin "Good evening, girls..."
    scene ch3ep1_433 with dissolve
    sally "*Giggles* We ran into you guys when we were about to go to your house. What a coincidence!"
    zeke "I know that, right?"
    sally "By the way, I'm very curious about what you're going to tell us, [mc]."
    sally "It must be something very important. Otherwise, you wouldn't have told us to gather up at your house."
    sally "Do you mind giving me a hint?"
    mc "Not now. Let's just wait until everyone is together."
    sally "Fine. If you say so. Let's hurry up and head there. Shall we?"
    zeke "Sure thing!"
    scene black with dissolve
    $ renpy.pause()
    s "*Half an hour later*................"
    scene ch3ep1_434 with fade
    rin "Okay... We've arrived here."
    rin "Make yourself home, girls."
    rin "Please, excuse me. I'm going to change my outfits first, then I'll go make dinner for you all."
    yui "I'll also go get changed, too."
    mc "Me, too."
    sally "Okay! Don't worry about us. Take your time."
    eira "Yeah..."
    scene black with dissolve
    $ renpy.pause()
    s "*A few minutes later*.............."
    scene ch3ep1_435 with dissolve
    mc "......................"
    zeke "*Laughs* Hahahaha! Really?!"
    sally "*Giggles* Yeah! That's funny, right?"
    u "They seem to be having a good time... What are they talking about...?"
    scene ch3ep1_436 with dissolve
    s "*Door bell rings*................"
    zeke "Huh...? Someone has already arrived."
    mc "Just sit there, [zeke]."
    mc "Keep accompanying [sally] and [eira]. I will go open the door."
    zeke "Got it. Thanks!"
    scene black with dissolve
    scene ch3ep1_437 with dissolve
    elaine "Good evening, [mc]."
    wendy "Hello, [mc]."
    mc "[elaine]. [wendy]. Welcome."
    scene ch3ep1_438 with dissolve
    elaine "Are we late?"
    mc "No, you guys aren't."
    mc "Everyone hasn't arrived here yet There are just [sally] and [eira]."
    elaine "Glad to know that...."
    mc "Come on in."
    wendy "Thank you."
    scene ch3ep1_439 with dissolve
    elaine "*Giggles* Look who've we got here... What's up, guys!"
    wendy "Good evening, everyone."
    zeke "What's up, girls!"
    sally "It's been a while, [elaine], [wendy]!"
    eira "Hello..."
    scene ch3ep1_440 with dissolve
    elaine "Hm? Where are [rin] and [yui]?"
    sally "They're cooking dinner for us in the kitchen."
    elaine "Oh, I see..."
    sally "Come! Take a seat first!"
    elaine "Sure thing. Thank you."
    scene ch3ep1_441 with dissolve
    elaine "To think about it, we barely meet each other at the company recently."
    sally "I know, right?!"
    zeke "Well... Your department is very far away from each other. That's why."
    wendy "I think we should meet each other more often. Let's have lunch together tomorrow."
    sally "Sure! Deal!"
    scene ch3ep1_442 with dissolve
    mc ".........................."
    u "There is no seat available for me...."
    u "Let's just find something to do while waiting for the rest...."
    scene black with dissolve
    $ renpy.pause()
    s "A few minutes later..............."
    scene ch3ep1_443 with dissolve
    mc "......................"
    unknown "What are you reading, [mc]?"
    u "Hm?"
    scene ch3ep1_444 with dissolve
    mc "[sally]..."
    sally "Why didn't you sit with us on the sofa?"
    mc "Because there was no seat available."
    sally "Is that so? I didn't realise that..."
    sally "What are you reading by the way?"
    mc "Just a simple magazine..."
    scene ch3ep1_445 with dissolve
    elaine "Hey, I'm so bored."
    elaine "Let's play some table football games."
    zeke "I was about to ask that too!"
    zeke "Do you know how to play it though?"
    scene ch3ep1_446 with dissolve
    elaine "Come on... Who do you think I am?"
    elaine "I'm a party queen. Don't you remember?"
    elaine "I've played these kind of games so many times that I've lost count."
    zeke "*Smirks* Pff... Really?"
    zeke "Do you know what? I'm good at this, too. I can't wait to beat you now!"
    elaine "*Smiles* Bring it on!"
    scene black with dissolve
    $ renpy.pause()
    s "A few minutes later..........."
    scene ch3ep1_447 with dissolve
    elaine "Well.... That was quite easy."
    zeke "Damn it...!"
    zeke "How did I lose...?!"
    elaine "I'm just better than you. It's as simple as that."
    scene ch3ep1_448 with dissolve
    sally "Hey! Hey! I want to play it, too!"
    elaine "Oh? Do you want to play it?"
    elaine "Who do you want to play with?"
    sally "*Laughs* [zeke]! His reaction when he lost was so funny! I want to see that again!"
    elaine "*Laughs* Alright then... I will pass on the stick to you."
    zeke "Hey! What do you mean by that? We haven't even started yet! Don't say things like you've already beat me!"
    scene black with dissolve
    $ renpy.pause()
    s "Half a minute later..........."
    scene ch3ep1_449 with dissolve
    sally "*Smiles* Yes! I won!"
    zeke "I-Impossible..!!!"
    zeke "Did I... just lose... in less than a minute...?!"
    eira "Wow... You're so good, [sally]."
    sally "*Giggles* Of course! If [elaine]'s a party queen, then I'm a gamer queen!"
    eira "Yeah... You really are."
    scene ch3ep1_450 with dissolve
    sally "It's your turn now, [wendy]."
    wendy "Hm? Me?"
    sally "Yeah! Come here! Take my place."
    wendy "... Okay."
    scene ch3ep1_451 with dissolve
    wendy "Please, go easy on me, [zeke]."
    zeke "I'm sorry, [wendy]. I can't do that."
    zeke "I have to salvage my dignity."
    sally "Come on... Don't be too hard on her."
    elaine "Yeah. I wouldn't say that if I were you. You will look even more worse if you lose."
    zeke "S-Shut up...!"
    elaine "*Giggles* Okay..."
    scene black with dissolve
    $ renpy.pause()
    s "A few minutes later..........."
    scene ch3ep1_452 with dissolve
    wendy "Huh...? Did I really win...?"
    sally "*Smiles* Yes, you did. Good job, [wendy]."
    zeke "*Sighs* What the hell is happening to me? Why did I always lose today?"
    zeke "I must've been cursed for sure...."
    mc "Are you okay?"
    zeke "Yeah... I'm still alive."
    scene ch3ep1_453 with dissolve
    sally "Hey, [eira]. Do you want to give it a try?"
    eira "Huh...? Me...?"
    eira "Thank you for asking, but I don't think I should..."
    sally "Hm? What made you think that?"
    eira "I don't know how to play it..."
    scene ch3ep1_454 with dissolve
    elaine "It's so easy, [eira]."
    elaine "You just need to score against him and prevent the ball from going into your goal."
    eira "But... I've never played it before..."
    elaine "Then, play it now. There is always a first time."
    elaine "Don't be too scared. He's so easy to play with."
    zeke "H-Hey! I'm not that easy!"
    eira ".... Okay then."
    scene ch3ep1_455 with dissolve
    eira "I don't really know how to play, [zeke]..."
    eira "Please, show some mercy...."
    zeke "... I really can't, [eira]."
    zeke "There is no turning back for me now. I've got to salvage my dignity."
    wendy "*Giggles* I hope you can do it this time. I'm rooting for you, [zeke]."
    scene black with dissolve
    $ renpy.pause()
    s "A few minutes later............."
    scene ch3ep1_456 with dissolve
    eira "... I-I won, [sally]! I won!"
    sally "*Smiles* Yeah! I saw it! That's my girl!!"
    wendy "Well done, [eira]!"
    zeke "Ugh... I've got beaten even by [eira]...."
    zeke "I'm so hopeless... I can't be saved anymore..."
    scene ch3ep1_457 with dissolve
    s "*Doorbell rings*........."
    sally "Huh? Was it [faye]?"
    elaine "Yeah, I think it's her since we all are already here."
    sally "Let's go open the door for her. Shall we?"
    scene ch3ep1_458 with dissolve
    zeke "No. You guys stay here."
    zeke "You are guests. I will go open the door."
    elaine "Alright, if you say so..."
    sally "*Smiles* Thank you."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_459 with dissolve
    faye "Good evening, everyone."
    sally "Hi, [faye]!"
    faye "I'm sorry I'm late. I just finished a conference with a customer at half past five."
    elaine "It's alright. No need to be sorry about that."
    elaine "By the way..."
    scene ch3ep1_460 with dissolve
    elaine "Who's this girl? I've never seen her before."
    elaine "Does she come with you, [faye]?"
    if ep3invitealice == 1 and ch2ep2suggestalice == 1:
        faye "Yes, she does. Her name is [alice]."
        alice "Hello, everyone. Nice to meet you all."
        elaine "Nice to meet you, too. I'm [elaine]."
        wendy "I'm [wendy]."
        eira "I'm [eira]..."
        sally "*Giggles* And I'm [sally]!"
        faye "She's also [mc]'s friend."
    else:
        alice "Hello, everyone. My name is [alice]."
        alice "Nice to meet you all."
        elaine "Nice to meet you, too. I'm [elaine]."
        wendy "I'm [wendy]."
        eira "I'm [eira]..."
        sally "*Giggles* And I'm [sally]!"
        alice "I'm [mc]'s friend. I come here because [mc] told me to."
    scene ch3ep1_461 with dissolve
    elaine "Hmm~? Why have you never told us about her, [mc]?"
    mc "........................"
    elaine "You should've told us that you have such a very cute girl like her as your friend."
    scene ch3ep1_462 with dissolve
    alice "C-Cute...?"
    alice "What are you talking about? No, I'm not that cute."
    elaine "*Giggles* How cute of you... Look at you trying to deny it."
    elaine "I know you're well aware that you're cute."
    scene ch3ep1_463 with dissolve
    rin "Dinner is ready, guys...."
    sally "Yes! Finally! I'm so starving right now..."
    faye "Good evening, [rin], [yui]."
    rin "Good evening, [faye]."
    yui "Hello, [faye]."
    scene ch3ep1_464 with dissolve
    rin "Hm...?"
    if ep3invitealice == 1:
        rin "Hello, [alice]. It's been a while."
        rin "I never knew you were going to come today..."
        scene ch3ep1_465 with dissolve
        alice "Yeah... It's been a while, [rin]."
        alice "[mc] invited me here. He said that he had something important to tell me."
        rin "I see...."
    else:
        rin "I've never seen you before..."
        rin "Does someone mind introducing her to me?"
        scene ch3ep1_465_a1 with dissolve
        zeke "Oh yeah, you've never met her before."
        zeke "Let me introduce her. This is [alice]."
        alice "Hi, I'm [alice]. Nice to meet you."
        scene ch3ep1_465_a2 with dissolve
        zeke "She's [mc]'s friend."
        rin "Yeah? I never knew that."
        mc "Well... I couldn't find an opportunity to introduce her to you."
        rin "Fair enough..."
    scene ch3ep1_466 with dissolve
    rin "Alright then, let's not waste any more time."
    rin "We should eat the food while it's still hot."
    yui "Looks like we also have to set a new table, [rin]."
    yui "Since there are more people than expected..."
    rin "Yeah, you're right."
    scene ch3ep1_467 with dissolve
    elaine "Let us help you guys with that."
    sally "Yeah. You've already made us dinner."
    sally "So, we should help you set a table in return!"
    rin "Thank you, guys..."
    if nominatekrystal == 1:
        scene ch3ep1_468 with dissolve
        mc "Hey. You guys head in there first. No need to wait for me."
        sally "Hm? Why's that?"
        mc "I'll go tell [krystal] to join us."
        sally "Oh! I completely forgot about her. It'll be fantastic if she joins us."
        sally "What are you waiting for? Go invite her already!"
        mc "Okay..."
        scene black with dissolve
        $ renpy.pause()
        scene ch3ep1_469 with dissolve
        s "*Door knocks*............"
        mc "[krystal]. Are you in there?"
        mc "......................."
        u "She doesn't answer me. The door is also locked. I guess she's taking a nap right now..."
        scene ch3ep1_470 with dissolve
        u "There is nothing I can do now... I also don't want to wake her up."
        u "I'll tell everything to her later."
        u "Let's just head to the kitchen...."
        jump ch3ep1telltruth
    else:
        jump ch3ep1telltruth
label ch3ep1telltruth:
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_471 with fade
    sally "*Smiles* Wow!! The food look so yummy!"
    sally "I can't wait to taste them!"
    elaine "Thank you for your hard work, [yui], [rin]."
    rin "It's actually nothing much, but... you're welcome."
    yui "I hope you all enjoy the meal."
    scene ch3ep1_472 with dissolve
    elaine "By the way... It's amazing that we all are here together, isn't it?"
    elaine "To think about it, the last time all of us were in the same place, was at the party at the president's house."
    rin "Yeah, it's been a while..."
    elaine "Hey. Why don't we all go on a trip together?"
    rin "Hm? When?"
    elaine "What about the next weekend?"
    rin "The next weekend...? Yeah, I'm down with that."
    yui "I think I'll be free by then as well."
    sally "Me, too!"
    elaine "Fantastic."
    scene ch3ep1_473 with dissolve
    elaine "What about you guys?"
    eira "Since [sally] will go, I will go as well."
    faye "I'm not sure if I'll have to work in the next weekend, but I'll join you all if I can."
    elaine "What about you, [alice]?"
    alice "Hm? I can go with you guys, too?"
    elaine "Yeah! Why not?"
    alice "*Smiles* Thank you for inviting me!"
    scene ch3ep1_474 with dissolve
    rin "But, it's only 2 days off..."
    rin "Where will we go though?"
    rin "Do you have any idea?"
    scene ch3ep1_475 with dissolve
    elaine "Umm... I haven't thought about that yet..."
    elaine "How does a beach sound? Pretty boring, right?"
    rin "Yeah, I think it's too often. We just went there last month."
    wendy "How about we go camping then?"
    scene ch3ep1_476 with dissolve
    elaine "Camping? That sounds good to me."
    sally "Me either!"
    rin "I agree with that."
    elaine "Where shall we go camping though?"
    wendy "I don't know yet, but I will search for a place to go."
    wendy "Then, I'll list the names and send to you all to decide."
    elaine "Okay. I'll leave it to you then."
    scene ch3ep1_477 with dissolve
    elaine "Are you going to join us, right?"
    mc "Hm..? Me..?"
    elaine "Yeah! [zeke]'s surely going to go with us, so who else do I have to ask?"
    mc "........................"
    scene ch3ep1_478 with dissolve
    mc "I'm not sure with that to be honest."
    zeke "Come on! Why are you not sure, bro?"
    zeke "Have you already got a plan for the next weekend?"
    mc "Yeah... Kinda...."
    scene ch3ep1_479 with dissolve
    rin "What a pity... It'd be great if you could join us..."
    sally "Right?!"
    mc "I'd love to, but I can't say for sure that I can go..."
    rin "It's alright. I understand that."
    rin "By the way, since everyone is here...."
    rin "What's that important thing you want to tell us?"
    mc ".... Let's just finish the food first, okay?"
    mc "Then, I'll tell you all."
    rin "Okay then!"
    scene black with dissolve
    $ renpy.pause()
    s "You spent time having dinner with them....."
    scene ch3ep1_480 with dissolve
    zeke "Alright, bro. We've finished eating."
    zeke "Now, tell us already."
    sally "Yeah! I can't wait to hear what it is about!"
    mc "Alright then...."
    if nominatekrystal == 1:
        scene ch3ep1_481_a1 with dissolve
        krystal "H-Huh....?!"
        elaine "Oh...?!"
        wendy "Good evening, [krystal]."
        scene ch3ep1_481_a2 with dissolve
        sally "Long time no see, [krystal]!"
        krystal "Hello, everyone..."
        sally "How are you doing?"
        krystal "I'm doing pretty good, [sally]. What about you?"
        sally "Never been better!"
        krystal "Good to hear that..."
        scene ch3ep1_481_a3 with dissolve
        krystal "Uh... By the way..."
        krystal "Why are you guys all here?"
        krystal "Have I missed out on something?"
        scene ch3ep1_481_a4 with dissolve
        rin "[mc] invited everyone here as he said he had something important to tell us."
        krystal "Hm? Why didn't you tell me that, too? [mc]?"
        mc "I went upstairs and knocked on your door, but you didn't answer..."
        krystal "Oh... I'm sorry. I guess I was sleeping."
        mc "It's alright. Since you're already here, it's better for me now."
        mc "I'll tell you all at the same time. Go bring a chair and take a seat."
        krystal "Sure. Give me a sec..."
    scene black with dissolve
    scene ch3ep1_482 with dissolve
    stop music fadeout 3.0
    mc "Are you guys ready?"
    alice "Yeah! I've been waiting for this moment for the whole day!"
    faye "Me, too. I'm curious about what you're going to tell us."
    faye "It's not usual for you to gather everyone up like this."
    scene ch3ep1_483 with dissolve
    play music "sfx/ch2ep2_7.mp3" fadein 3.0
    $ bgm = "Neutrin05 - Rain and Tears"
    mc "Okay...."
    mc "I'll tell you all everything about me since the begining..."
    mc "It all started since when I was born...."
    scene black with dissolve
    $ renpy.pause()
    s "You spent time telling everyone everything about you...."
    scene ch3ep1_484 with dissolve
    mc "That's everything I wanted to tell you all....."
    zeke "......................"
    yui "......................"
    rin "......................"
    eira "[mc]......"
    scene ch3ep1_485 with dissolve
    elaine "Wait... Hang on a sec....."
    elaine "I'm so confused... What's going on...?"
    elaine "So, you're actually the son of that lady we saw at [rowan]'s house?"
    wendy "You're the son of the main investor of our company?"
    scene ch3ep1_486 with dissolve
    faye "Hold on...."
    faye "You said you were sent here to steal the technology of Xecon's gear."
    faye "How much did you steal it and give it to... what's his name again?"
    alice "I think it's [victor]...."
    faye "Yeah, [victor]."
    scene ch3ep1_487 with dissolve
    mc "I only gave him the old version of Xecon's gear code..."
    mc "He demanded me to give him the blueprint of the current Xecon's gear."
    mc "But, I decided not to give it to him."
    faye "*Sighs* Even if it's the old version of code, but still..."
    faye "It could be developed until it actually works..."
    faye "You've caused the company such a big loss..."
    scene ch3ep1_488 with dissolve
    rin "Calm down, [faye]."
    rin "I think that's not something you should be worried about now."
    faye "Hm? If it's not for our company's sake, then what else should I be worried about?"
    rin "I understand your perspective, but...."
    scene ch3ep1_489 with dissolve
    rin "According to [mc]'s story, he had no choice, but to do what [victor] told him to."
    rin "He had to obey to [victor] if he wanted to survive."
    rin "We can't blame him for that. That's what he was taught since he was young."
    rin "But, I'm sure that he feels guity for his action now."
    rin "Plus, he found his real family now."
    rin "Now, he has no reason to obey to [victor] anymore."
    scene ch3ep1_490 with dissolve
    rin "He wants to make up for his mistakes. He also cares for us."
    rin "Otherwise, he wouldn't have decided to fully open up to us like this."
    rin "I think we should forgive him and help him as much as we can."
    eira "Yeah... I agree with that."
    faye ".... You're right."
    scene ch3ep1_491 with dissolve
    faye "I was too worried about our company that I overlook your honesty..."
    faye "I'm so sorry, [mc]."
    mc "It's okay. I completely understand you."
    mc "I'm sorry for hiding the truth from all of you."
    mc "I'm also sorry that you guys might encounter problems in the future because of me..."
    scene ch3ep1_492 with dissolve
    eira "It's okay... I don't blame you for that..."
    wendy "*Smiles* Yeah... We all are friends."
    wendy "And friends help each other through a tough time."
    rin "Well said, [wendy]."
    faye "By the way... How are you going to deal with [victor]?"
    scene ch3ep1_493 with dissolve
    mc "I'm now working with a police, his name is [felix]."
    mc "In my opinion, I think he's the one I can rely on."
    mc "We're going to take down [victor] and put him in jail."
    faye "Is there anything you want me to help...?"
    mc "Thank you, but... I don't think there is anything you can help me now."
    scene ch3ep1_494 with dissolve
    mc "Moreover, I don't want you all to get involved in this mess any deeper."
    mc "[felix] and I are trying to figure out about how to keep you guys safe."
    mc "I don't want any of you to get hurt because of [victor]."
    mc "I will try my best...."
    rin ".... Thank you, [mc]. We appreciate your kindness..."
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    s "About half an hour later.............."
    scene ch3ep1_495 with dissolve
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    rin "Alright...."
    rin "It's quite late now. The party is over."
    rin "Good bye, guys."
    elaine "Okay. See you tomorrow."
    wendy "Good bye..."
    scene ch3ep1_496 with dissolve
    sally "Thank you for dinner. It was very delicious!"
    rin "Have a good night, all of you."
    faye "Thank you. Have a good sleep, too."
    alice "See you later, [rin], [yui], [mc], [zeke]."
    mc "Get home safely, everyone...."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_497 with dissolve
    u "......................"
    u "Alright, everyone has left now."
    u "Let's go back to my room...."
    if ch2ep4hintheater == 1:
        scene ch3ep1_498 with dissolve
        krystal "[mc]."
        u "Hm...?"
        krystal "... Can we talk?"
        scene ch3ep1_499 with dissolve
        mc "Of course we can."
        mc "What do you want to talk about?"
        krystal ".... You remember the dream I told you about?"
        mc "What dream?"
        scene ch3ep1_500 with dissolve
        krystal "I told you that I saw you in my dream at the place that looked like an orphanage."
        krystal "Have you already forgot that?"
        mc "Oh... I remember it now."
        krystal "Great... You told me that it was just a dream, but after I heard everything today, I know now that it wasn't."
        krystal "We were in the same place when we were young."
        krystal "Why did you lie to me, [mc]?"
        mc "Because I didn't want you to remember it."
        scene ch3ep1_501 with dissolve
        krystal "But, that's my memories..."
        krystal "You have no idea how bad it feels when you can't remember anything from the past..."
        mc "... No, I haven't. However, I think you should focus on the present not the past."
        mc "Especially, when it was the bad past."
        mc "I'm sorry that I lied to you, but I'd do the same if I could turn back time."
        mc "You were lucky that you got out of the vicious circle caused by [victor]."
        mc "You've been shining bright.... No, you're about to shine even brighter."
        mc "So, I didn't want you to get involved with bad things again."
        scene ch3ep1_502 with dissolve
        krystal "......................."
        krystal "... I understand you now. I'm sorry for being silly."
        mc "You don't have to. I kind of understand why you were like that. So, I don't blame you."
        mc "Alright... I have to leave now. There's something I have to do soon."
        krystal "Okay... Have a good night, [mc]."
        mc "You, too."
        $ krystal_relationship += 1
        $ krystal_ch3_ep1 += 1
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_503 with dissolve
    u "I'm going to go see [tobi]."
    u "I'm going to convince him again."
    u "But, let's go to my room and change the outfit first...."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_504 with dissolve
    u "Alright, I've done changing."
    u "Now, let's go see [tobi] before it gets any dark-"
    scene ch3ep1_505 with dissolve
    u "Hm...?"
    zeke "Oh...?"
    scene ch3ep1_506 with dissolve
    mc "Where are you going to go, [zeke]?"
    zeke "Hm? What are you talking about?"
    mc "You've changed your clothes..."
    scene ch3ep1_507 with dissolve
    mc "And by the look of it, it's not the outfit to wear before going to bed."
    zeke "*Sighs* I can't really trick you by playing dumb..."
    zeke "Yeah, I'm going outside. I'm going to meet my old friends."
    mc "Hm? At a time like this?"
    scene ch3ep1_508 with dissolve
    zeke "Yeah, why not?"
    zeke "You're going to go somewhere as well, aren't you?"
    zeke "I can tell that by the look of your outfit, too."
    mc "Yeah..."
    scene ch3ep1_509 with dissolve
    mc "I'm going to convince [tobi], the guy that were spying on me, to cooperate with me."
    zeke "I see. Good luck with that then."
    mc "........................."
    mc "... Thank you."
    zeke "I'm going to leave now. Bye."
    mc "Bye."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_510 with fade
    $ renpy.pause()
    play music "sfx/ep.3/ep3_11.mp3" fadein 3.0
    $ bgm = "Day7 - Journey Home"
    mc "........................"
    scene ch3ep1_511 with dissolve
    mc "[tobi]."
    tobi "....................."
    mc "Stop pretending to be asleep already."
    mc "I know that you are awake."
    tobi "Tsk...!"
    scene ch3ep1_512 with dissolve
    tobi "Have you brought any food and drink?"
    mc "No, I haven't."
    tobi "Then, get the fuck out of my face."
    mc "......................"
    scene ch3ep1_513 with dissolve
    mc "Have you changed your mind yet?"
    mc "Don't you really want to change sides?"
    tobi "*Sighs* Stop wasting your time, bro."
    tobi "There is no way I'm going to join you."
    tobi "You're walking on the road to hell."
    tobi "Going against [victor] is just a suicide."
    scene ch3ep1_514 with dissolve
    mc "You'll never know that."
    mc "I don't think it's a complete suicide. In my opinion, it's a fifty-fifty chance."
    tobi "Pff...! Fifty-fifty? Are you high, bro?"
    mc "No, I'm not. I'm well awared that working for [victor] means my life hangs by a thread."
    mc "So, I've been preparing for this for so many years already."
    scene ch3ep1_515 with dissolve
    mc "Plus, you have no choice, but to cooperate with me now."
    mc "Even if you somehow manage to return to [victor] and tell him my plans, do you really think that he will grant you a reward?"
    mc "I can tell you that it's not going to happen."
    mc "I know him. You do know him. He's just going to focus on the fact that you failed your mission and got caught."
    mc "You've seen how someone like us, who failed his mission, ended up before."
    tobi "............................."
    scene ch3ep1_516 with dissolve
    tobi "W.. What are you doing?"
    mc "Where's your phone?"
    tobi "What are you going to do with it?"
    mc "......................."
    scene ch3ep1_517 with dissolve
    mc "Here it is...."
    mc "Well... You really took so many photos of me...."
    tobi "Hey! Didn't you hear me?!"
    tobi "What are you going to do with my phone?!"
    scene ch3ep1_518 with dissolve
    mc "Chill out..."
    mc "I'm just going to send a message to [victor] as if nothing wrong has happened."
    tobi "......................"
    mc "You can't just disappear without reporting him my situation, am I right?"
    tobi "*Sighs* Yeah.... You're right."
    scene ch3ep1_519 with dissolve
    mc "Alright...."
    mc "Have you made your decision?"
    mc "Are you going to help me take down [victor]?"
    tobi "........................"
    tobi "Can you give me more time...?"
    scene ch3ep1_520 with dissolve
    mc "Alright then..."
    mc "I'll come back tomorrow."
    tobi "What!? Are you just going to leave like that?!"
    tobi "At least give me some food and drink!"
    mc "......................."
    tobi "You fucking asshole!!!"
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_521 with fade
    u "*Sighs* What a day it was....."
    u "I'm so exhausted now."
    u "Let's go take a shower, then go to bed..."
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    s "Next morning.........."
    scene ch3ep1_522 with dissolve
    mc "Umm....."
    u "Hm? It's morning already...."
    u "I hope [tobi] decide to help me...."
    u "That'd make things a lot easier as I won't have to worry about [victor] suspecting me for now..."
    scene ch3ep1_523 with dissolve
    u "......................"
    u "Well... To think about [tobi], it reminds me of the moment he managed to push me by force."
    u "Have I become weaker...?"
    u "Let's work out for a bit before go take a shower..."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_524 with dissolve
    mc "*Pants* Ninety...."
    scene ch3ep1_525 with dissolve
    mc "*Pants* Nine...."
    scene ch3ep1_524 with dissolve
    mc "*Pants* One...."
    scene ch3ep1_525 with dissolve
    mc "*Pants* Hundred...."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_526 with dissolve
    mc "*Pants* Ninety...."
    scene ch3ep1_527 with dissolve
    mc "*Pants Nine...."
    scene ch3ep1_526 with dissolve
    mc "*Pants* One...."
    scene ch3ep1_527 with dissolve
    mc "*Pants* Hundred...."
    scene ch3ep1_528 with dissolve
    u "Alright..."
    u "A minute more, then I'm done with my exercise today..."
    s "*Door knocks*............."
    u "Hm...?"
    scene ch3ep1_529 with dissolve
    mc "Who's it?"
    rin "It's me...."
    mc "[rin]?"
    rin "Yeah. Can I come in?"
    mc "Come on in. The door is unlocked."
    rin "Okay..."
    scene black with dissolve
    scene ch3ep1_530 with dissolve
    rin "W-Wha...!?"
    rin "W-hat are you doing, [mc]?!"
    mc "Don't mind me. I'm just exercising..."
    scene ch3ep1_531 with dissolve
    rin "... Should I get out and come back again once you're done with it?"
    rin "(It's not like I have never seen him top naked before, but why does he look so hot today...?)"
    mc "It's fine. I'll finish it in a few seconds..."
    rin "Alright... I'll wait here then."
    mc "Okay."
    scene black with dissolve
    scene ch3ep1_532 with dissolve
    mc "So..."
    mc "What brings you here...?"
    rin "I wonder if... you know where [zeke] went last night after we'd finished dinner."
    mc "[zeke]? He said he was going to meet his friends."
    scene ch3ep1_533 with dissolve
    mc "Why did you ask?"
    rin "Well... I saw him returning home with a bruise on his face."
    mc "A bruise?"
    rin "Yeah. It's like a bruise you get from getting punched."
    rin "So, I'm a bit worried about what happened to him."
    mc "Why didn't you ask that from him then?"
    rin "I did ask him about that, but he didn't seem to tell me the truth."
    scene ch3ep1_534 with dissolve
    rin "He said he ran into an electric pole when walking on street with his friends."
    rin "Who would have believed that, right?"
    mc "And what do you want me to do?"
    rin "Can you go ask him? I think he will be more open to you."
    mc "I doubt that, but fine...."
    mc "I'll do you a favor."
    rin "*Smiles* Thank you."
    scene black with dissolve
    $ renpy.pause()
    s "[rin] has left your room, then you went to take a shower...."
    scene ch3ep1_535 with dissolve
    u "Alright, I'm ready now."
    u "Let's go find [zeke]."
    u "I wonder if he's in his room. Let's go find that out."
    jump ch3ep1unlockimage1
label ch3ep1unlockimage1:
    scene black with dissolve
    $ renpy.pause()
    $ ch3ep1special_image1 = True
    $ renpy.sound.play("sfx/alert.wav")
    s "You've unlocked special images......"
    jump ch3ep1special_image1
label ch3ep1unlockimage2:
    $ ch3ep1special_image2 = True
    jump ch3ep1special_image2
label ch3ep1unlockimage3:
    $ ch3ep1special_image3 = True
    jump ch3ep1special_image3
label ch3ep1unlockimage4:
    $ ch3ep1special_image4 = True
    jump ch3ep1special_image4
label ch3ep1unlockimage5:
    $ ch3ep1special_image5 = True
    jump ch3ep1special_image5
label ch3ep1_end:
    scene ch3ep1_536 with dissolve
    s "*Door knocks*..............."
    zeke "Who's it?"
    u "There he is...."
    mc "It's me. Can I come in?"
    zeke ".... [mc]?"
    zeke "Alright, you may come in."
    scene black with dissolve
    scene ch3ep1_537 with dissolve
    mc "Good morning, [zeke]..."
    zeke "... Yeah."
    zeke "What do you want?"
    mc "... What happened to your face?"
    scene ch3ep1_538 with dissolve
    zeke "Don't mind that. It's nothing serious."
    mc "I think it is. Otherwise, you wouldn't cover your right eye like that."
    zeke "I said it is not. Why do you care?"
    mc "Of course, I do. You're my friend."
    scene ch3ep1_539 with dissolve
    zeke "*Smirks* I'm your friend?"
    mc "Yes, you are."
    zeke " Really? I never knew that."
    mc "......................."
    mc "... What's wrong with you seriously?"
    zeke "If you ever thought I was your friend, you'd have told me about everything you said yesterday since a long time ago."
    scene ch3ep1_540 with dissolve
    mc "........................"
    mc "Okay, I understand now. You're mad at me because of that."
    zeke "I'm not mad at you..."
    mc "Let me ask you one thing. What would you do if you were me?"
    mc "Would you just tell your dark secrets to anyone you know for only a couple months?"
    mc "Especially when those secrets will put anyone that knows about them in danger?"
    zeke ".........................."
    scene ch3ep1_541 with dissolve
    zeke "Still..."
    zeke "What would happen if you didn't meet your mother?"
    zeke "Wouldn't you just keep obeying to [victor] and hurt us eventually?"
    mc "............................."
    mc "I'm not going to lie. Yeah, that might have happened."
    mc "But, that can't be possible now since I met my mother and found out that [victor] killed my father."
    mc "I'm not going to be on his side anymore."
    zeke "......................."
    scene ch3ep1_542 with dissolve
    zeke "*Sighs* Whatever.... Take a seat first."
    zeke "I'm going to tell you about what I did last night."
    mc "Okay..."
    scene ch3ep1_543 with dissolve
    mc "So...."
    mc "What happened to you last night? You didn't go meet your friends, right?"
    zeke "Yes, I did."
    mc "... Did you guys fight? Do you need any help?"
    scene ch3ep1_544 with dissolve
    zeke "Yeah, I did fight some of them, but it's fine now."
    mc "Why did you fight with them actually...?"
    zeke "I went to ask them for help."
    mc "What help?"
    zeke "After you told us everything last night, said that we might be in danger in the future."
    zeke "I decided that I can't just stay still doing nothing. So, I when to ask my friends to help protecting everyone around us."
    scene ch3ep1_545 with dissolve
    mc "But, [victor] and his men are cruel. Normal people can't deal them."
    mc "Why did your friends hurt you when you asked for their helps though?"
    zeke "No, they aren't normal people."
    mc "Huh...?"
    zeke "Do you still remember [rin] said that I was kind of a bad person when I was in highschool?"
    mc "Yes, I do."
    scene ch3ep1_546 with dissolve
    zeke "I know it sounds cliche, but it actually happened."
    zeke "When I was young, I used to think that I can do anything and get anything by force."
    zeke "So, I always fought with other students. Eventually, I ended up being the strongest guy in the school."
    zeke "However, that's not the end. When you brought yourself into such an environment like that, it's very hard to step out."
    zeke "No matter now many people you'd beaten, there were always other ones that wanted to take you down to prove their values."
    zeke "Not only students in my school, but there were students from other schools nearby as well."
    scene ch3ep1_547 with dissolve
    zeke "In the end, I and my friends created a gang."
    zeke "We took down our enemies. Even local mafias in the city failed to stop us."
    zeke "So, we eventually managed to own the city even though we were just highschoolers."
    zeke "However, I decided to quit and give the leader position to one of my friends."
    zeke "They were mad at me when they saw me again last night, so... we had a little fight."
    scene ch3ep1_548 with dissolve
    zeke "However, once a friend always a friend."
    zeke "Moreover, I helped them so many times when we were together, so they agreed to help me protecting everyone."
    mc "............................."
    mc "Still... [victor] and his men are more dangerous than you can imagine..."
    scene ch3ep1_549 with dissolve
    zeke "Come on! Didn't you say I'm your friend?"
    zeke "Then, have some faith in your friend!"
    zeke "I might not be as strong as I was, but I'm still good at fighting."
    zeke "Moreover, I think my friends have become even stronger and more powerful since they're the biggest gang in the city."
    zeke "So, I think they can deal with [victor] and his men."
    mc ".........................."
    scene ch3ep1_550 with dissolve
    mc "*Sighs* Fine.... More alliance is always better than less. You do you."
    zeke "So, don't worry about us. You can leave everyone's safety to me."
    zeke "And just focus on how to take down [victor] and put him in jail."
    mc "Okay, I will."
    zeke "Good.... By the way, have you had breakfast yet?"
    mc "No, I haven't."
    zeke "Me either. Why don't we go downstairs and find something to eat?"
    mc "Yeah. That sounds like a great idea...."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    s "*About two hours later*..............."
    play music "sfx/beach.mp3"
    $ bgm = "Bensound - Adventure"
    scene ch3ep1_551 with fade
    u "I'm so sleepy now...."
    u "Perhaps I'm tired because of the morning exercise."
    u "I haven't done it for quite a while, so my body doesn't remember the feeling."
    u "Let's just go grab some energy drink to keep me wake up."
    scene black with dissolve
    scene ch3ep1_552 with dissolve
    u "Hm...?"
    u "Isn't that [sally]?"
    u "Her department is on two floors above. I wonder what she is doing here."
    scene ch3ep1_553 with dissolve
    mc "[sally]."
    sally "Aw...!!"
    mc "What are you doing...?"
    scene ch3ep1_554 with dissolve
    sally "[mc]!"
    sally "Why did you sneak up on me? You almost gave me a heart attack!"
    mc "Hm? I didn't sneak up on you. I was just coming to say hi."
    sally "Still! You should've said that from far away!"
    mc "... I never knew you were such a scaredy-cat."
    scene ch3ep1_555 with dissolve
    mc "What are you doing here at this time by the way?"
    mc "Aren't you supposed to be working?"
    sally "Shh... Don't say that too loud."
    sally "I've sneaked away from my department because I don't feel like working this morning..."
    mc "Hm? You don't feel like working?"
    scene ch3ep1_556 with dissolve
    mc "I thought you enjoyed playing games so much."
    sally "Jeez... Game testing isn't just playing games, you know?"
    sally "When playing games, you just have fun and worry about nothing."
    sally "But, when testing games, you have to pay attention into a very small detail over and over again to make sure that everything is fine."
    sally "Sometimes it gets tiring and boring...."
    mc "I understand that now..."
    scene ch3ep1_557 with dissolve
    mc "By the way, are you going to use that vending machine?"
    mc "If not, can you please step aside. I'm going to use it."
    sally "Oh! I'm sorry! Yes, I am. I was about to use it before you suddenly showed up."
    sally "Let me use it first, then it's your turn."
    mc "Okay, sure."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_558 with dissolve
    mc "Hm? You're still here...?"
    mc "I thought you'd already left."
    sally "Yeah... I don't feel like going back to my department yet."
    sally "*Giggles* So, I'm going to hang around for a little bit more."
    scene ch3ep1_559 with dissolve
    mc "Alright. You do you."
    mc "I'm going to go back to my department now."
    mc "Good bye. Have a great day."
    sally "Thanks! You, too!"
    if ch2ep3_dinner == 1:
        scene ch3ep1_560_a1 with dissolve
        mc "Wait a minute...."
        sally "Hm? What's wrong?"
        mc "To think about it, didn't I make a promise to go see your mother?"
        sally "... Oh yeah! You did."
        mc "I'm sorry. I completely forgot about that."
        sally "It's alright. my mom didn't say anything about that as well."
        sally "So, I guess it's not something important."
        scene ch3ep1_560_a2 with dissolve
        mc "Glad to hear that...."
        mc "To be honest I want to go meet your mother to keep my promise now."
        mc "But, this is not the time... You understand me, right?"
        sally "Yes, I understand what you're trying to say."
        sally "It's all good! We can just go meet her after we overcome this problem."
        mc "Yeah. After we overcome this problem..."
        sally "Good luck, [mc]."
        mc "Thank you."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_561 with dissolve
    u "Okay....."
    u "Let's go back to work..."
    scene ch3ep1_562 with vpunch
    s "*Phone vibrates*............"
    u "Hm...? I'm getting a phone call?"
    u "I need to find out who it is..."
    scene ch3ep1_563 with dissolve
    u "Oh... It's [rowan]."
    u "I wonder why he calls..."
    u "Let's pick up the call and hear him out."
    scene ch3ep1_564 with dissolve
    mc "Hello...."
    scene black with dissolve
    scene ch3ep1_566 with fade
    rowan "Hi, [mc]."
    rowan "I've brought you a great news."
    scene ch3ep1_564 with dissolve
    mc "Hm? A great news?"
    mc "What is it?"
    scene ch3ep1_566 with dissolve
    rowan "It's a bit earlier than I thought, but..."
    rowan "The fake blueprint is now finished."
    scene ch3ep1_564 with dissolve
    mc "Really...?"
    mc "Well, you didn't take much time at all..."
    mc "Are you sure it is going to work?"
    scene ch3ep1_567 with dissolve
    rowan "Actually, that's why I'm calling you now."
    rowan "Do you have some time to come and take a look?"
    scene ch3ep1_565 with dissolve
    mc "Sure. How about this evening?"
    mc "I'll go to your house to check the blueprint."
    scene ch3ep1_567 with dissolve
    rowan "That'd be great."
    rowan "See you in the evening then."
    scene ch3ep1_565 with dissolve
    mc "Yeah. See you this evening."
    mc "Bye."
    scene ch3ep1_568 with dissolve
    u "It only took him a couple days..."
    u "I hope the blueprint will be good enough so that it doesn't have to be fixed."
    u "I know that there is still some time until the deadline, but..."
    u "I also need to spare some time in case of something urgent happens."
    scene black with dissolve
    $ renpy.pause()
    s "Later than evening............."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_569 with dissolve
    joe "Shawn Wick 4 is out today, guys!"
    leo "What?! Really? I thought it was going to be released tomorrow!"
    joe "No, it's today. What do you think? Shall we go to a theater?"
    leo "Of course!"
    david "Sure! I've been waiting to watch it for so long!"
    liam "I'm sorry, but I can't join you guys today...."
    scene ch3ep1_570 with dissolve
    u "Well...."
    u "There are still these people. I haven't told them about everything yet."
    u "And I think I'm not ever going to tell them since ex-employees here got lured by [victor]."
    u "There is no guarantee it's not going to happen again."
    u "If I tell everything to them, and someone among them get lured by [victor] again. My plan is just going to be ruined."
    u "So, let's just play it safe...."
    scene black with dissolve
    $ renpy.pause()
    s "You waited until they'd left...."
    scene ch3ep1_571 with dissolve
    u "Alright..."
    u "Let's go to [rowan]'s house."
    scene black with dissolve
    $ renpy.pause()
    s "About an hour later..........."
    scene ch3ep1_572 with fade
    u "Okay, I've arrived....."
    u "Did I come too early? It's five past six."
    u "... Well, forget it. I guess [rowan]'s already here."
    scene ch3ep1_573 with dissolve
    s "*Doorbell rings*............."
    rowan "[mc]...?"
    mc "Yes, it's me."
    rowan "Alright, come on in!"
    scene black with dissolve
    scene ch3ep1_574 with dissolve
    mc "Good evening, [rowan]."
    rowan "Good evening."
    rowan "Come. Let's take a seat first."
    mc "Okay..."
    scene ch3ep1_575 with dissolve
    rowan "The blueprint is in this envelope."
    rowan "Here. Take it."
    mc "Thank you."
    scene ch3ep1_576 with dissolve
    rowan "What do you think?"
    mc "......................"
    rowan "I did my best making it by using the real one as an example."
    rowan "Even I can't say it's fake in the first glance."
    mc "To be honest... I don't know what to think."
    scene ch3ep1_577 with dissolve
    mc "I haven't seen the real blueprint yet."
    mc "But if you, who's the person making both of them, can't tell their differences in the first glance."
    mc "I think it would [victor] for quite amount of time until he realises it."
    rowan "Yeah. And even though he managed to create the Xecon gear, it's not going to perform at its best."
    rowan "I've taken out a very important function out of the fake blueprint."
    mc "You're truely a genius, [rowan]. You've done a marvellous job."
    rowan "... Thank you."
    scene black with dissolve
    $ renpy.pause()
    scene ch3ep1_578 with dissolve
    mc "Alright...."
    mc "Thank you for the blueprint."
    mc "I'm going to leave now."
    rowan "So, I guess my part is done. There is no more thing I can do, right?"
    scene ch3ep1_579 with dissolve
    mc "For now. Yeah, I think so."
    rowan "Alright then, good luck."
    rowan "And also... please be safe."
    mc "Thank you. You, too."
    scene ch3ep1_580 with dissolve
    stop music fadeout 3.0
    u "Alright... I've got the fake blueprint now."
    u "Finally the plan of taking [victor] down has slightly become a reality...."
    u "However, it's just getting started. It is not going to be easy..."
    u "But, I will never give up..."
    u "... Until the day I see him collapsed."
    scene black with dissolve
    $ renpy.pause()
    hide screen smartphone
    $ episode = 9
    call screen ending

label ch3ep1special_image1:
    if _in_replay:
        scene ch3ep1special_image1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    jump ch3ep1unlockimage2
label ch3ep1special_image2:
    if _in_replay:
        scene ch3ep1special_image2 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    jump ch3ep1unlockimage3
label ch3ep1special_image3:
    if _in_replay:
        scene ch3ep1special_image3 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    jump ch3ep1unlockimage4
label ch3ep1special_image4:
    if _in_replay:
        scene ch3ep1special_image4 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    jump ch3ep1unlockimage5
label ch3ep1special_image5:
    if _in_replay:
        scene ch3ep1special_image5 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    jump ch3ep1_end
