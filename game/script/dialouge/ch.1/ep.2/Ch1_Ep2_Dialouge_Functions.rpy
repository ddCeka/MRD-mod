label Chapter2:
    call mod_set_vars
    scene ep2
    $ renpy.pause(3,hard=True)
    scene black with dissolve
    s "*A few moments later*...."
    scene ep2_01 with fade
    play music "sfx/ch1ep2.mp3"
    $ bgm = "Bensound - Little Idea"
    unknown "Alright, I have an important business meeting in half an hour."
    unknown "So, I'm going to hang up now."
    mc "....Okay."
    unknown "[mc]."
    scene ep2_02 with dissolve
    mc "...What?"
    unknown "I hope you're doing your job well."
    mc "...Yes, I am."
    unknown "Good. I have to go now. Let's talk again next time."
    unknown "Be alert. I'll be in touch with you soon."
    mc "...Got it."
    scene ep2_03 with dissolve
    u "........."
    u "So that's what he wanted to say for our first conversation in a while..."
    u "'I hope you're doing your job well'..."
    u "........."
    u "...Forget it. Let's just take a nap."
    scene black with dissolve
    s "*Two hours later*...."
    scene ep2_04 with dissolve
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Knocking*...."
    scene ep2_05 with dissolve
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Knocking*...."
    u "...Hm?"
    rin "[mc]. Are you in there?"
    u "[rin]?... Has she already come back?"
    u "I don't know what time it is now, but I assume that it's already night."
    u "By the way, what does she want from me? Why is she knocking on my door?"
    scene ep2_06 with dissolve
    u "Well... There's only one way to find out."
    mc "Yes, I am."
    rin "Can you open the door, please?"
    mc "Wait a sec..."
    scene ep2_07 with dissolve
    $ renpy.sound.play("sfx/Door opening.mp3")
    rin "Hi!"
    mc "...Hi."
    rin "I heard that you were a bit tired today. Did you get some sleep?"
    mc "... Yeah, I was sleeping until you woke me up."
    rin "Oh... I'm so sorry."
    mc "....."
    mc "....Never mind. What about you?"
    scene ep2_08 with dissolve
    rin "Hm? What about me?"
    mc "....How was the movie?"
    rin "Great. It was really enjoyable."
    mc "Good for you. By the way, what do you want from me?"
    scene ep2_09 with dissolve
    rin "Oh! Yeah, [zeke] told me that you wanted to go back home to rest."
    rin "So, I assumed that you would be hungry after waking up, and bought a hamburger for you!"
    mc "......"
    rin "What's wrong? You don't like hamburgers?"
    scene ep2_10 with dissolve
    mc "...Yes, I do."
    rin "Lovely. I'm glad to hear that."
    rin "I don't know your favorite food, so I was afraid that I bought something you don't like."
    mc "....."
    scene ep2_11 with dissolve
    rin "Come on! Don't just stand still and keep looking at me. Take it!"
    mc "....."
    u "This feeling...."
    scene black with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep2_12 with dissolve
    u "She reminds me of the old times..."
    scene black with dissolve
    $ renpy.pause(0.2, hard=True)
    scene ep2_13 with dissolve
    u "It's been so long since someone kindly gave me something..."
    u "But, I don't understand why she is so nice to me though?"
    u "We're nothing more than just housemates after all..."
    scene ep2_14 with dissolve
    rin "......."
    rin "....Are you really not going to say anything?"
    u "Why is she asking me such a question?"
    u "What am I supposed to do?"
    menu:
        "Pat her head [rin1] [smbo]":
            u "Well... I'm grateful for her kindness. Maybe I should just..."
            $ rin_ch1_ep2 += 1
            $ rin_relationship += 1
            scene ep2_14_p01 with dissolve
            mc "Thank you..."
            rin "*Giggles*...Aw... Stop it..."
            rin "Don't you remember what I told you?"
            rin "You shouldn't be doing this to a single woman."
            mc "Okay then."
            scene ep2_14_p02 with dissolve
            rin "By the way, what's your plan for tonight?"
            mc "My plan for tonight?"
            rin "Yeah."
            mc "I don't know. I don't have one."
            rin "I see... Then, would you like to come with me to the living room?"
            rin "I'm going to watch a Netflix series, so I wonder if you want to join me."
            mc "Series? Didn't you just finish watching a movie?"
            rin "Oh... Yeah, I did. Why?"
            scene ep2_14_p03 with dissolve
            mc "....Nothing."
            rin "There are so many good series. I could watch them whole day if I had enough time to do that."
            rin "...If that's what you wanted to ask me."
            u "...Since she likes netflix series so much, I'm starting to feel like I should watch one myself."
            u "It's been quite a long time since I watched anything."
            u "Moreover, I don't have plans for tonight either."
            u "So... I think I'm going to just join her."
            scene ep2_14_p04 with dissolve
            mc "Okay, let's go."
            rin "Really!? Are you really going to come with me?"
            mc "Why are you so surprised?"
            rin "It's just... I did invite you, but I didn't expect you to actually say yes."
            mc "... You can go there alone if you want."
            rin "No, let's go together."
            scene ep2_14_p05 with fade
            rin "By the way... Is there a series you want to watch?"
            mc "No, there isn't."
            rin "Really?"
            mc "Yes. Just choose the one you want to watch."
            rin "Okay then!"
            scene ep2_14_p06 with dissolve
            rin "What are you doing?"
            rin "Why are you sitting there?"
            mc "What's the problem?"
            rin "Are you going to turn your head left to the TV during the whole series?"
            rin "You're only gonna hurt your neck!"
            rin "Come and sit next to me! There are a lot of free spaces here."
            scene ep2_14_p07 with dissolve
            mc "All good now?"
            rin "Yep! It's better."
            rin "Shall we start now?"
            mc "It's up to you."
            rin "Then, let's get started!"
            scene ep2_14_p08 with dissolve
            mc "...Where's [zeke]?"
            rin "He's probably in his room now."
            rin "Why? Do you want him to join us?"
            mc "No. It's just...you guys seem to stick together."
            mc "So, I thought he was going to be here, too."
            rin "He said he had a lot of work to do."
            scene ep2_14_p10 with dissolve
            rin "By the way, how is your working life?"
            mc "Hm?..."
            scene ep2_14_p11 with dissolve
            mc "My working life?"
            rin "Yeah. How's the company? Do you like it?"
            mc "Yes, I do... The company... Has everything I was looking for..."
            rin "I'm glad to hear that."
            rin "You know what? I'm really happy that you moved here."
            mc "........"
            u "Why did she suddenly say that though?...."
            rin "In my life, I only have [zeke] as my male friend."
            scene ep2_14_p10 with dissolve
            mc "...Why? Do you also hate men?"
            rin "Also?... Oh, you're talking about [yui]."
            rin "No, I don't hate men. It's just... I've met a lot of them, and they only approached me because they wanted {b}something{/b} from me."
            mc "......."
            rin "But you're different from them."
            rin "You don't look at me {b}that{/b} way, and that makes me feel really comfortable staying with you."
            rin "Even though sometimes you seemed to not care about anything, I know that in the bottom of your heart you care about us."
            mc "......."
            scene ep2_14_p12 with dissolve
            rin "You're a very good guy. I wish you the best in your life, [mc]. I really do."
            mc "....Thank you."
            rin "You're welcome."
            scene ep2_14_p13 with dissolve
            rin "*Giggles*... But if you really appreciated it, you'd tell me more about the companies special project!"
            rin "So, I will have more time for making contents on our Facebook fanpage!"
            mc "....Don't you already know the details?"
            scene ep2_14_p12 with dissolve
            rin "No. I only know that we've been inventing the Xecon Gear for years."
            rin "I don't know what kind of game it's going to be, or when it will be released."
            rin "The company wants to keep it secret."
            rin "Only people who are involved with the development progress get a chance to know all of that."
            mc "...I see. Then, I don't think I can tell you."
            scene ep2_14_p13 with dissolve
            rin "Come on! Don't be too serious. I was just kidding!"
            mc "...Okay."
            mc "Then, what do you do at work if you don't know anything about the game?"
            rin "Well, I look after our player's community and create contents for our current game."
            mc "I see."
            scene ep2_14_p09 with dissolve
            rin "By the way, have you ever watched this series?"
            mc "...No, I haven't."
            rin "That's too bad. You missed such a good one!"
            rin "It's one of the best series on Netflix these days, in my opinion."
            mc "Yeah?...What kind of series it is?"
            rin "It's the story about a group of people who are hijacked while on board a red-eye flight from Brussels,"
            rin "which heads west in an attempt to survive a catastrophic solar event that kills all living organisms during daylight hours."
            rin "Sounds interesting, right?"
            mc "Yeah..."
            scene ep2_14_p14 with dissolve
            s "You spend your time watching the series with [rin]."
            s "Episode by episode..."
            scene black with dissolve
            s "*An hour later*...."
            scene ep2_14_p15 with dissolve
            mc "...[rin], can you pause the series for a sec?"
            rin "......"
            mc "I have to go to..."
            scene ep2_14_p16 with dissolve
            mc "Hm?..."
            rin "......."
            u "So... She just fell a sleep like this?"
            scene ep2_14_p17 with dissolve
            u "Didn't she just say that she could spend the whole day watching a series?..."
            u "...Well, maybe she's just tired."
            u "Should I wake her up?...."
            u "......."
            scene black with dissolve
            u "*A few moments later*...."
            scene ep2_14_p18 with dissolve
            rin "Zzzz...."
            scene ep2_14_p19 with dissolve
            rin "...Hm?"
            rin "....Did I just fall a sleep?..."
            mc "...You're awake?"
            scene ep2_14_p20 with dissolve
            rin "!!!!"
            rin "[mc]?"
            rin "W...was I sleeping on your lap?"
            scene ep2_14_p21 with dissolve
            mc "...Yes."
            rin "But how?..."
            mc "You were sleeping on my shoulder first... But I managed to put your head on my lap."
            rin "...Why?"
            mc "......"
            u "To be honest, I don't know why I did that either..."
            scene ep2_14_p22 with dissolve
            rin "I... I'm leaving."
            mc "Are you not going to finish the episode?"
            rin "No, I'm not. I just.... Remember that I have work to do."
            mc "....Okay."
            scene ep2_14_p23 with dissolve
            rin "(Wait.... Why do I have to run away like this?)"
            rin "(...What's this feeling?)"
            rin "(Why does my face feel so hot?...)"
            scene ep2_14_p24 with dissolve
            u "...What's wrong with her?..."
            u "...Well, forget about her. Let's just continue watching the series."
            scene ep2_14_p25 with fade
            rin "......"
            scene ep2_14_p26 with dissolve
            rin "(No, my face still feels so hot....)"
            rin "(He made me very shy. Why did he do that?)"
            rin "(That was the first time I slept on someone's lap...)"
            rin "(If he was like the other guys, I would think that he was trying to flirt with me....)"
            rin "(...Or did he really?.... No, that's impossible!)"
            scene ep2_14_p27 with dissolve
            rin "(...I should calm myself down first...)"
            rin "([mc] isn't the type of guy who flirt with every woman he sees.)"
            rin "(...It's already late at night. I should go and take a bath, then go to bed.)"
            jump rin_mas

        "Leave [rin1]":
            $ rin_ch1_ep2 += 1
            $ rin_relationship += 1
            u "Yeah, I'm grateful for her kindness, but I think that's it."
            u "I will just say thank you to her, then get back to my room."
            u "I don't want to get too close to her."
            scene ep2_14_n1 with dissolve
            mc "Thank you."
            rin "Eh?... Um, you're welcome."
            mc "You should leave now."
            rin "...Okay."
            scene ep2_14_n2 with dissolve
            u "Well... Since I've got a TV in my room..."
            u "Then, let's fine something to watch while I'm eating dinner."
            scene ep2_14_n3 with dissolve
            s "You spend your time enjoying a burger while watching a Netflix series."
            scene black with dissolve
            $ renpy.pause()
            jump Ep1Ch2_1
label rin_mas:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    scene ep2_14_p28 with dissolve
    rin "(...Aw... How relaxing...)"
    rin "(Let's clean myself up, and lie down here for a bit...)"
    scene ep2_14_p29 with dissolve
    rin "......"
    scene ep2_14_p21 with dissolve
    $ renpy.pause(0.3, hard=True)
    scene ep2_14_p30 with dissolve
    rin "(..Why can't I stop thinking about that?)"
    rin "(What was he thinking, by letting me sleep on his lap?)"
    rin "(I know that he wanted me to sleep comfortably, but he could just let me sleep on the sofa....)"
    rin "(My heart... Is beating so fast. I can't control it.)"
    scene ep2_14_p31 with dissolve
    rin "(....I'm 24 already, yet I'm still single.)"
    rin "(And it's not like I'm not interested in love, but I just haven't found a guy I like yet.)"
    rin "(...[mc]....)"
    scene black with dissolve
    show rin_mas1 with dissolve
    rin "..Mmm.... Ha....."
    rin "(...Why am I feeling so horny?...)"
    rin "(It's been... So long... Since the last time I masturbated...)"
    $ renpy.pause()
    hide rin_mas1
    show rin_mas2 with dissolve
    rin "....Ah....Ha...."
    rin "(....No... I shouldn't moan too loud... They might hear me...)"
    rin "(...Mmm.... But, this feels too good...)"
    $ renpy.pause()
    hide rin_mas2
    show rin_mas3 with dissolve
    rin "(...Ha...My pussy is so wet right now...)"
    rin "(...Ahh... Even though I'm lying in cold water, I can still feel how hot my pussy is...)"
    rin "(...Mmm...I'm...getting...there...)"
    menu:
        "Slowest":
            hide rin_mas3
            jump rin_mas_slow
        "Slower":
            hide rin_mas3
            jump rin_mas_normal
        "Cum":
            jump rin_mas_cum
label rin_mas_slow:
    scene black with dissolve
    show rin_mas1 with dissolve
    $ renpy.pause()
    menu:
        "Faster":
            hide rin_mas1
            jump rin_mas_normal
        "Fastest":
            hide rin_mas1
            jump rin_mas_fast
label rin_mas_normal:
    scene black with dissolve
    show rin_mas2 with dissolve
    $ renpy.pause()
    menu:
        "Slower":
            hide rin_mas2
            jump rin_mas_slow
        "Faster":
            hide rin_mas2
            jump rin_mas_fast
label rin_mas_fast:
    scene black with dissolve
    show rin_mas3 with dissolve
    $ renpy.pause()
    menu:
        "Slowest":
            hide rin_mas3
            jump rin_mas_slow
        "Slower":
            hide rin_mas3
            jump rin_mas_normal
        "Cum":
            jump rin_mas_cum
label rin_mas_cum:
    rin "(Mmmm!... I'm about to cum!...)"
    hide rin_mas3
    scene ep2_14_p35 with dissolve
    rin "(...Haa... I'm cumming!!...)"
    rin "(Ahhhh!!!....)"
    scene ep2_14_p36 with dissolve
    rin "*Panting*...."
    rin "(...That was the best feeling I've ever had in the past few months...)"
    rin "(I wonder how [yui] felt when she was having sex with [mc].)"
    rin "(I wish I could...)"
    scene ep2_14_p37 with dissolve
    rin "(!!!!)"
    rin "(No! What were you thinking, [rin]!)"
    rin "(He's two years younger than you!)"
    rin "(No! That's not the point! Why did I think that I wanted to do it with him?)"
    rin "(Moreover, I just masturbated myself while thinking of him!?)"
    rin "([rin], you're a crazy woman!.... I shouldn't let anyone know about this.)"
    rin "(Otherwise, they're going to think that I'm a nasty girl...)"
    $ renpy.end_replay()
    $ rin_ch1_ep2 += 2
    $ rin_relationship += 2
    $ watchtvwithrin = True
    scene black with dissolve
    $ renpy.pause()
    jump Ep1Ch2_1

label Ep1Ch2_1:
    s "Next day...."
    scene ep2_15 with fade
    u "...So, this is my work list for today."
    u "There's nothing too complicated, I just need to fix all the bugs like I've been doing for the past few days"
    u "I should do it well, so that...."
    scene ep2_16 with dissolve
    u "...Hm?"
    u "There is someone coming this way..."
    scene black with dissolve
    show faye_1 with dissolve
    $ renpy.pause(6, hard=True)
    hide faye_1
    scene black
    scene ep2_17 with dissolve
    faye "(...Hm?)"
    scene ep2_20 with dissolve
    mc "......."
    faye "......."
    faye "(Who is this man? I've never seen him around here before.)"
    u "(Who is this woman? What's she doing here?)"
    scene ep2_21 with dissolve
    u "(...Well, that's none of my business actually...)"
    faye "(Well, it doesn't matter who he is. He's probably just a new employee.)"
    faye "(I better keep going to finish my business here.)"
    scene black with dissolve
    s "*A few moments later*...."
    scene ep2_22 with fade
    u "Alright, it's time to work."
    u "...Actually, I'm a little bit thirsty..."
    u "Let's go to the water dispenser machine first."
    scene ep2_23 with dissolve
    u "...To think about that woman... She must be [faye] for sure."
    u "What did [joe] call her? An arrogant angel?"
    u "Yeah, I can tell that he was right by the way she looked at me."
    scene ep2_24 with dissolve
    u "She is working in the project management department...."
    u "Who knows? Maybe someday we might have to work together."
    if givecookies == True:
        scene ep2_24_m1 with dissolve
        sally "(Hm?... Isn't that [mc]?)"
        sally "(Yes, it's him!)"
        scene ep2_24_m2 with dissolve
        sally "(Hehehe... I'm gonna sneak up behind him.)"
        sally "(As I remember, he was kind of emotionless.)"
        sally "(Hehehe.... I can't wait to see his facial expression when I shock him!)"
        scene ep2_24_m3 with dissolve
        sally "(Hehehe... This is so exciting!)"
        sally "(...Sneaky peaky...)"
        sally "(...I need to approach him quietly...)"
        scene ep2_24_m4 with dissolve
        s "While trying to sneak up on you, [sally] accidentally trips herself."
        sally "Aw!"
        scene ep2_24_m5 with dissolve
        sally "[mc]! W-Watch out!..."
        mc "Hm?..."
        scene ep2_24_m6 with dissolve
        mc "......"
        sally "(W-What? Did he just dodge me like that?)"
        mc "[sally]?... What were you trying to do?"
        scene ep2_24_m7 with dissolve
        sally "*Screaming*...."
        sally "(No! I'm about to fall!)"
        u "She's surely going to hit the water dispenser machine..."
        u "That's going to bring a lot of attention here..."
        mc "*Sigh*...."
        scene ep2_24_m8 with dissolve
        sally "*Screaming*..Ahh! I'm falling! I'm falling!..."
        sally "This is gonna hurt!..."
        mc "......"
        sally "Ahhh!..."
        scene ep2_24_m9 with dissolve
        mc "*Sigh*...Calm down. You aren't going to fall. I've got you."
        sally "...Huh?"
        sally "...Oh yeah. You've got me."
        mc "......."
        scene ep2_24_m10 at eyesblink("Ch.1/Ep.2/Scenes/ep2_24_m10.jpg", "Ch.1/Ep.2/Scenes/ep2_24_m10_blink.jpg", 1) with dissolve
        sally "Hehe... Thanks for saving me again..."
        sally "I had no idea what to do if you didn't help me."
        mc "...So, what were you trying to do? Sneaking up behind my back like that?"
        scene ep2_24_m11 at eyesblink("Ch.1/Ep.2/Scenes/ep2_24_m11.jpg", "Ch.1/Ep.2/Scenes/ep2_24_m11_blink.jpg", 1) with dissolve
        sally "Hehe...I wanted to see your facial expression when you're shocked."
        sally "But, I accidentally tripped over myself."
        sally "How clumsy of me..."
        mc "......"
        mc "...By the way, what are you doing here?"
        sally "Oh! I tested the game, and found some bugs."
        sally "So, I come here to give my report about that."
        sally "And discuss about future plans for the game."
        mc "I see..."
        scene ep2_24_m12 with dissolve
        sally "Do you still remember the promise I made you?"
        mc "Promise?"
        sally "I promised to buy you a meal! Have you already forgot?"
        mc "Oh, you did. And?"
        sally "Well, I just want to remind you."
        sally "I'll text you the date when I'm ready."
        mc "Okay..."
        sally "Alright, let's get inside together."
        $ sally_ch1_ep2 += 1
        $ sally_relationship += 1
    elif givecookies == False:
        scene ep2_24_n1 with dissolve
        sally "Excuse me, can you move aside for a bit, please?"
        sally "I want to use the machine."
        scene ep2_24_n2 with dissolve
        if sallyatcafe == True:
            u "Hm? Isn't she the woman from the cafe on that day?"
        else:
            u "...Hm? Who's this woman?"
        mc "...Sure."
        sally "Thank you!"
        scene ep2_24_n3 with dissolve
        sally "Are you a new employee? I've never seen you around here before."
        mc "Yes, I am. I just started working here a few days ago."
        sally "Oh, that's why..."
        scene ep2_24_n4 at eyesblink("Ch.1/Ep.2/Scenes/ep2_24_n4.jpg", "Ch.1/Ep.2/Scenes/ep2_24_n4_blink.jpg", 1) with dissolve
        sally "Then, let me introduce myself."
        sally "I'm [sally]! Nice to meet you!"
        sally "I'm working in the game specialist department!"
        u "[sally]?..."
        u "Oh, she is one of the six... Wait, it's seven angels now..."
        mc "I'm [mc]. I'm a game developer."
        scene ep2_24_n5 with dissolve
        mc "By the way, what are you as a game specialist doing here?"
        sally "Oh! I tested the game, and found some bugs."
        sally "So, I come here to give my report about that."
        sally "And discuss about future plans for the game."
        mc "I see..."
        sally "Then, let's get inside together."
        scene ep2_24_n6 with dissolve
        s "While you guys are heading towards the department..."
        scene ep2_24_n7 with dissolve
        sally "Oh yeah, I just want to tell you that..."
        sally "If we happen to see each other in the company, you don't need to call me senior, okay?"
        sally "Even though I started working here before you, I'm just 20 years old!"
        mc "........"
        mc "Instead of caring about something like that, I think you should turn around and watch where you're walking."
        scene ep2_24_n8 at eyesblink("Ch.1/Ep.2/Scenes/ep2_24_n8.jpg", "Ch.1/Ep.2/Scenes/ep2_24_n8_blink.jpg", 1) with dissolve
        sally "Don't worry!"
        sally "I come here so many times that I already remember every detail here!"
        sally "But, thanks for worrying about me though."
        mc "......."
        sally "Why? Don't you believe me?"
        scene ep2_24_n9 with dissolve
        sally "Look! I can even walk with my eyes closed!"
        mc "Okay...Whatever you say."
        sally "You wanna play a game?"
        mc "What game?"
        sally "I'll walk with my eyes closed to the department room."
        sally "And if I actually do it, you have to buy me a meal!"
        mc "........"
        u "Why would I have to play it though?..."
        sally "So, what do you s-"
        scene ep2_24_n10 with dissolve
        s "While trying to walk with her eyes closed, [sally] accidentally trips herself."
        sally "Aw!!"
        scene ep2_24_n11 with dissolve
        sally "*Screaming*...."
        sally "No! I'm about to fall!..."
        u "...Well, I'm not surprised to see this at all..."
        mc "*Sigh*....."
        scene ep2_24_n12 with dissolve
        sally "*Screaming*..Ahh! I'm falling! I'm falling!..."
        sally "This is gonna hurt!..."
        mc "......"
        sally "Ahhh!..."
        scene ep2_24_n13 with dissolve
        mc "*Sigh*...Calm down. That won't happen. I've got you."
        sally "...Huh?"
        sally "...Oh yeah. You've got me."
        mc "......."
        scene ep2_24_n14 with dissolve
        mc "...Walking with your eyes closed, huh?"
        sally "Hehe... We all make mistakes, but that's what makes us human, isn't it?"
        u "...Maybe you're just clumsy..."
        sally "Maybe... Thank you for saving me."
        u "Well, it's because I don't want you to blame me for not helping..."
        scene ep2_24_n15 with dissolve
        sally "Hehe... Seems like I just lost the game..."
        sally "I'll buy you a meal! Can I have your number?"
        mc "You don't have to..."
        sally "What are you talking about? Yes, I do!"
        mc "*Sigh*...Okay then..."
        sally "Lovely. I'll text you the date and time for meeting up next time."
        sally "But now, let's go to the department room first."
        $ sally_ch1_ep2 += 2
        $ sally_relationship += 2
    scene black with dissolve
    $ renpy.pause(1,hard=True)
    scene ep2_25 with dissolve
    sally "Hello everyone!"
    david "Oh! Good morning, [sally]!"
    leo "What are you doing here, [sally]?"
    sally "I'm looking for [liam]. Where is he?"
    scene ep2_26 with dissolve
    liam "Where are you looking at, [sally]? I'm right here."
    sally "Oh, there you are!"
    sally "*Giggles*...My bad. I'm so sorry."
    scene ep2_27 with dissolve
    liam "Don't mind. Why were you looking for me?"
    sally "I was going to give you my bug report, but to think about it again..."
    sally "I think it's better for you to see it with your own eyes."
    sally "Can you come with me to the game testing room?"
    liam "Sure!"
    scene ep2_28 with dissolve
    u "...Let's go to my table..."
    scene ep2_29 with dissolve
    u "...Hm?"
    u "Isn't that the completed version of Xecon gear?"
    u "......"
    scene ep2_30 with dissolve
    u "Looking at it again, it's so amazing that we can dive into the virtual world by using this thing..."
    u "No wonder why people are going crazy about it."
    u "......."
    joe "If I were you, I would slowly put it back down."
    u "Hm?..."
    scene ep2_31 with dissolve
    joe "Be careful with what you're touching, man."
    joe "You don't want to break it, do you?"
    mc "I just..."
    scene ep2_32 with dissolve
    joe "It's alright. I know you want to play with it."
    joe "In fact, we all do..."
    joe "We're game developers, how can we not want to play with such an amazing thing like this, right?"
    mc ".....Yeah."
    joe "But you better put it down first. I don't know if the company has any backups."
    mc "Okay..."
    scene ep2_33 with dissolve
    u "Alright, let's do my work..."
    scene atoffice6 with dissolve
    s "Everyday, you spend your time working at the company..."
    scene black with dissolve
    s "Time flies so fast. Before you even realize it, it's already the weekend."
    jump Ep1Ch2_2
label Ep1Ch2_2:
    scene ep2_34 with fade
    play music "sfx/beach.mp3"
    $ bgm = "Bensound - Adventure"
    rin "Do you have any plans for this weekend, [zeke]?"
    zeke "........"
    rin "[zeke]!"
    scene ep2_35 with dissolve
    zeke "What? Why did you shout my name all of sudden?"
    rin "It's because you didn't answer my question."
    zeke "Oh, I'm sorry. I didn't hear you calling me."
    zeke "I was paying attention to the game I'm playing."
    zeke "What did you want to ask me again?"
    scene ep2_34 with dissolve
    rin "I want to know your plans for this weekend."
    zeke "Oh, I don't have any plans. Just staying home maybe?"
    rin "I'm a little bit bored though..."
    rin "Should we..."
    s "*Foot step coming*...."
    scene ep2_36 with dissolve
    rin "Hm?..."
    scene ep2_37 with dissolve
    rin "Good morning, [mc]!"
    mc "...Morning."
    rin "Did you sleep well last night?"
    mc "Yes."
    scene ep2_38 at eyesblink("Ch.1/Ep.2/Scenes/ep2_38.jpg", "Ch.1/Ep.2/Scenes/ep2_38_blink.jpg", 1) with dissolve
    rin "So, this is your first weekend after becoming a developer."
    rin "How do you feel?"
    mc "What do you mean?"
    rin "You get days off after working for the whole week. How does it feel?"
    mc "Nothing...."
    mc "Am I supposed to feel anything special?"
    scene ep2_39 at eyesblink("Ch.1/Ep.2/Scenes/ep2_39.jpg", "Ch.1/Ep.2/Scenes/ep2_39_blink.jpg", 1) with dissolve
    zeke "Of course, you are!"
    zeke "Man, you don't get many days off once you start your working life"
    zeke "I miss the good old days when I was a student. I had a lot of free time back then..."
    zeke "I could just skip the university when I didn't want to go!"
    zeke "But I can't do that now. Otherwise, I'll have my salary cut..."
    mc "...But I've never missed a single class though."
    scene ep2_38 at eyesblink("Ch.1/Ep.2/Scenes/ep2_38.jpg", "Ch.1/Ep.2/Scenes/ep2_38_blink.jpg", 1) with dissolve
    rin "Heh... We've got a former outstanding student here..."
    rin "Don't listen to [zeke]. He was a very bad student!"
    zeke "Hey! I've changed now, okay?"
    rin "*Giggles*...You should take [mc] as the role model of your life, [zeke]!"
    zeke "Come on..."
    mc "........"
    rin "By the way, what are you doing here, [mc]?"
    scene ep2_40 with dissolve
    mc "I'm going to grab a water bottle."
    zeke "Just a water bottle? What about breakfast?"
    mc "I'm not hungry yet."
    rin "Well, then we won't hold you down here any longer."
    mc "Okay."
    scene ep2_41 with dissolve
    u "Hm?..."
    scene ep2_42 with dissolve
    yui "!!!"
    mc "....."
    yui "......"
    yui "...I'm..."
    scene ep2_43 with dissolve
    s "[yui] was about to say something, but she decided to stop and walked past you instead."
    u "What was she trying to say?"
    scene ep2_44 with dissolve
    u "...Forget it. She just probably wanted to apologize to me."
    u "Let's just go and take a water bottle, then go back to my room."
    scene ep2_45 with dissolve
    rin "......"
    rin "(*Sigh*...These guys....)"
    scene ep2_46 with dissolve
    rin "Don't you feel uncomfortable, [zeke]?"
    zeke "Uncomfortable? No, I don't."
    zeke "Why? Are you uncomfortable?"
    zeke "Oh! Of course, you are. I told you that sofa isn't so comfy, didn't I?"
    rin "I'm not talking about the sofa, dumbass!"
    scene ep2_47 with dissolve
    zeke "Hm? Then, what are you talking about?"
    rin "I'm talking about them! [mc] and [yui]."
    zeke "Oh... Yeah, they still don't talk to each other."
    rin "Right? I know that this is none of my business, but the atmosphere between them..."
    rin "I couldn't help but feel uncomfortable."
    zeke "But what can we do though?"
    rin "Let me think..."
    scene ep2_48 with dissolve
    rin "Oh! Why don't we bring them to somewhere tomorrow?"
    zeke "Hm? Where?"
    rin "The beach! Let's bring them to the beach!"
    zeke "What beach?"
    rin "The nearest one, of course! It's only an hour's drive from here."
    scene ep2_49 with dissolve
    zeke "Sounds good to me."
    zeke "Moreover, we haven't gone there for a while."
    rin "Right? I still can't believe that we haven't gone to such a beautiful beach like that for a while either."
    scene ep2_50 with dissolve
    zeke "However, I think there is a problem..."
    rin "What problem?"
    zeke "I'm sure that we can convince [yui] to go with us, but...what about [mc]?"
    scene ep2_51 with dissolve
    rin "...Oh. Yeah, you're right."
    rin "It won't be easy to convince him..."
    zeke "Right?"
    rin "......"
    scene ep2_52 with dissolve
    rin "Don't worry! I'll convince him myself!"
    zeke "Are you sure that you can do it?"
    rin "I don't know, but let me try at least!"
    zeke "Well then. I'm counting on you!"
    scene ep2_53 with fade
    mc "......"
    scene ep2_54 with dissolve
    $ renpy.sound.play("sfx/Door knocking.mp3")
    rin "[mc], are you in there?"
    scene ep2_55 with dissolve
    mc "...Yes."
    rin "Er...Can we talk for a bit?"
    mc "......."
    scene ep2_56 with dissolve
    u "I wonder what she wants to talk about..."
    u "*Sigh*...But that doesn't matter..."
    u "She's already out there anyway, I can't just ignore her..."
    scene ep2_57 with dissolve
    $ renpy.sound.play("sfx/Door opening.mp3")
    rin "Hey!"
    u "What's up with that strange smile...."
    u "I can already tell that this conversation will not be any good for me..."
    scene ep2_58 with dissolve
    mc "What do you want? "
    rin "I want to know if you're free tomorrow."
    mc "....Yes, I am. Why?"
    rin "Well... The thing is... [zeke] and I are going to the beach tomorrow."
    mc "And?"
    scene ep2_59 at eyesblink("Ch.1/Ep.2/Scenes/ep2_59.jpg", "Ch.1/Ep.2/Scenes/ep2_59_blink.jpg", 1) with dissolve
    rin "Okay. To be frank, I want you to come with us."
    u "And that's what I was talking about..."
    rin "Look. Since you're new to the city, I would like to take this chance to take you to one of the most beautiful places, in my opinion!"
    mc "......."
    scene ep2_60 at eyesblink("Ch.1/Ep.2/Scenes/ep2_60.jpg", "Ch.1/Ep.2/Scenes/ep2_60_blink.jpg", 1) with dissolve
    rin "What do you say? You will go with us, right?"
    rin "You do remember that I helped you last time, right?"
    rin "You owe me one, so I'd like to ask you to do me a favor by going to the beach with us tomorrow."
    mc "......"
    scene ep2_61 with dissolve
    u "Well, I think it isn't so bad for me to go with them."
    u "I also don't have any plans for tomorrow. Then..."
    mc "Okay..."
    rin "Huh? What did you say?"
    mc "I'll go with you guys."
    rin "(Oh... To be honest he surprised me. I didn't expect him to say it this easy.)"
    scene ep2_62 with dissolve
    rin "Lovely. Then, let's meet up tomorrow at 8 a.m."
    rin "Are you okay with that?"
    mc "Yeah. No problem."
    rin "Good. See you tomorrow!"
    scene ep2_63 with dissolve
    u "....To think about it, I don't know if I made a right choice."
    u "I don't think I should get too close to them..."
    u "Since there is only one reason that brought me here..."
    scene sunday with dissolve
    $ renpy.pause()
    scene ep2_64 with fade
    zeke "...It's five to eight already."
    zeke "Are you sure that he will come, [rin]?"
    scene ep2_65 with dissolve
    rin "Don't worry! He said that he'll go with us. So, he'll definitely come."
    rin "I'm sure that he's a man of his word!"
    zeke "If you say so..."
    scene ep2_66 with dissolve
    yui "What are you guys waiting for?"
    yui "Aren't we going?"
    scene ep2_67 with dissolve
    zeke "Of course, we are!"
    yui "Then, let's go! Why are we wasting time here?"
    zeke "Er...."
    yui "Wait!... Don't tell me that you're waiting for...."
    scene ep2_68 with dissolve
    $ renpy.sound.play("sfx/Door opening.mp3")
    rin "There he is!"
    $ renpy.sound.play("sfx/Door closing.mp3")
    zeke "Speaking of the devil!"
    yui "Ugh!..."
    scene ep2_69 with dissolve
    zeke "Man. I thought you wouldn't come!"
    mc "....What made you think that?"
    zeke "It's because you didn't show up until now."
    mc "[rin] told me to meet up at eight..."
    rin "*Giggles*...Oh. Yes, I did."
    zeke "Dude! You're so..."
    zeke "*Sigh*...I don't know what to say."
    rin "Alright, we've got everyone here. Let's go."
    scene ep2_70 with dissolve
    rin "What are you waiting for, [yui]?"
    rin "Get inside the car."
    yui "...You didn't tell me that he would come with us."
    rin "Yeah? I thought I already did."
    rin "(To be honest, I didn't. Otherwise, you would reject when I invited you for sure.)"
    scene ep2_71 with dissolve
    zeke "Come on, [yui]!"
    zeke "Hop in! We should get there as fast as we can so that we can reserve a good spot!"
    yui "......"
    rin "Let's go, [yui]."
    yui "*Sigh*...Fine."
    scene ep2_72 with dissolve
    zeke "Alright, let's go guys!"
    rin "I'm gonna take a quick nap."
    rin "Don't drive too fast, okay?"
    scene black with dissolve
    s "*An hour later*......"
    scene ep2_73 with fade
    zeke "Those chairs seem available!"
    rin "Yeah, let's go and put all of our stuff there."
    zeke "Sure!"
    scene ep2_74 with dissolve
    zeke "Wooooh! Sunny bay, I am here!"
    mc "Sunny bay?"
    zeke "Yeah! It's the name of the beach."
    mc "I see..."
    rin "Guys."
    scene ep2_75 with dissolve
    zeke "What?"
    rin "Can you take care of our stuff?"
    rin "We're going to get changed."
    zeke "No problem!"
    rin "Thanks. Let's go, [yui]."
    yui "Okay."
    scene ep2_76 with dissolve
    zeke "Ahh... The sun... The wind... The smell of the sea..."
    zeke "This is such a wonderful place to visit on the weekend...."
    u "Well, I totally agree..."
    scene ep2_77 with dissolve
    zeke "Are you going to swim in the sea?"
    mc "....No."
    zeke "Come on, man..."
    zeke "We come to the beach for a reason. Don't waste such an opportunity!"
    zeke "I'm sure the girls will be very happy if you do that."
    mc "......."
    scene ep2_78 with dissolve
    zeke "Well, speaking of the devils..."
    zeke "There they are."
    mc "......."
    show beach with dissolve
    $ renpy.pause(6.5, hard=True)
    scene black
    hide beach
    scene ep2_80 with dissolve
    rin "Aw... The weather is great today!"
    yui "Yeah, we're so lucky."
    rin "Hm? Why?"
    yui "It was forcasted that today it will be rainy."
    rin "Oh... Then, I hope they're wrong."
    yui "Yeah, I hope so..."
    scene ep2_79 at eyesblink("Ch.1/Ep.2/Scenes/ep2_79.jpg", "Ch.1/Ep.2/Scenes/ep2_79_blink.jpg", 1) with dissolve
    rin "What are you waiting for, guys?"
    rin "Let's go swimming!"
    show screen smartphone
    scene ep2_81 with dissolve
    play music "sfx/beach.mp3" fadein 3.0
    $ bgm = "Bensound - Adventure"
    $ visitbeach = True
    $ sally_contact = True
    yui "Now?"
    rin "Yeah, why not?"
    yui "I actually think it's too hot to swim right now."
    yui "Let's just wait for a bit."
    rin "Um..."
    rin "Yeah, I think you're right."
    scene ep2_82 with dissolve
    rin "Guys, can you share us a chair, please?"
    mc "...Sure."
    rin "Thank you, [mc]."
    mc "No worries..."
    scene ep2_83 with dissolve
    zeke "You guys look fantastic!"
    rin "Hehe... We already knew that."
    zeke "I'm going to buy drinks. Do you guys want some?"
    rin "Of course, I do."
    zeke "What about you, [yui]?"
    yui "Yes."
    zeke "What do you guys want?"
    yui "Just buy me anything."
    rin "Yeah."
    zeke "Okay then..."
    scene ep2_84 with dissolve
    zeke "...."
    scene ep2_85 with dissolve
    rin "...Hm? What?"
    zeke "*Whispers*...Shh! Don't talk too loud."
    rin "*Whispers*....Okay."
    zeke "*Whispers*...You should go buy drinks with me and let [mc] stay here."
    scene ep2_86 with dissolve
    rin "*Whispers*...Hehe... I think I know what you're trying to do now."
    rin "*Whispers*...That's such a great idea!"
    zeke "*Whispers*...Right?"
    rin "*Whispers*...Okay. Then, let's go."
    scene ep2_87 with dissolve
    zeke "[mc], wait."
    u "...Hm?"
    scene ep2_88 with dissolve
    mc "What's wrong?"
    zeke "Ahem!... I think you don't need to go with me now."
    zeke "[rin] is going with me instead."
    mc "......"
    zeke "W-Why are you looking at me like that? S-She just wants to go to a toilet!"
    rin "Y-Yeah!"
    mc "I didn't even say anything..."
    zeke "...I-I just want to let you know that I didn't plan to do something suspicious!"
    rin "Hehe...[zeke]."
    zeke "What?"
    rin "*Whispers*...Shut up."
    scene ep2_89 with dissolve
    u "....."
    u "Were they really trying to trick me?"
    u "It was really obvious that they wanted to set me up with [yui] alone..."
    u "*Sigh*...Do they think that I'm stupid?"
    u "Forget it. Let's just go back to the chairs."
    scene ep2_90 with dissolve
    u "......."
    yui "[rin], can you put sunscreen on my back, please?"
    mc "......."
    yui "Are you there, [rin]?"
    scene ep2_91 with dissolve
    mc "I'm not [rin]."
    yui "......."
    yui "([mc]?...I thought he already went to buy drinks with [zeke].)"
    scene ep2_92 with dissolve
    yui "([zeke] and [rin] were the ones setting this up for sure!)"
    mc "......."
    yui "......."
    scene black with dissolve
    s "*A few moments later*...."
    scene ep2_93 with dissolve
    yui "(Ugh!... This is so awkward...)"
    yui "(How can he stay quiet after knowing the truth?)"
    yui "(I mean... At least he should blame me for misunderstanding and scolding him!)"
    yui "(If he did that, it would be a lot easier for me to...)"
    yui "(.......)"
    yui "(.....Apologize to him.)"
    scene ep2_94 with dissolve
    yui "(Argh!...I can't take this awkward silence anymore!)"
    yui "(Let's just do it! Apologize to him, and end all these guilty feelings I have!)"
    scene ep2_95 with dissolve
    yui "........"
    mc "........"
    yui "....I'm sorry."
    scene ep2_96 with dissolve
    mc "Hm? What did you just say?"
    yui "........"
    yui "....I said that I'm sorry."
    mc "........"
    mc "Actually... You don't have to apologize to me."
    scene ep2_97 with dissolve
    yui "What are you talking about? Yes, I do!"
    mc "......."
    yui "I know that I've been rude towards you because of my prejudice against men."
    yui "...But what happened that night was actually my fault."
    yui "I shouldn't have treated you like that before knowing the truth."
    yui "...{size=-10}I will try my best to be nice to you from now on.{/size}"
    mc "Hm? What did you say?"
    yui "N-Nothing!"
    scene ep2_96 with dissolve
    yui "...Can you... Forgive me?"
    yui "...I want to end this awkward atmosphere between us."
    u "How should I respond?"
    menu:
        "I forgive you. [yui2]":
            $ yui_ch1_ep2 += 2
            $ yui_relationship += 2
            mc "Okay. I forgive you."
            yui "Really? Then, are we good now?"
            mc "Yeah."
            mc "...I actually think that you did nothing wrong."
            mc "Most women would act like you did if they were in such a situation like that."
            yui "......."
            yui "Thanks for understanding me."
            if sexwithyui == 1:
                mc "I'm also sorry. I thought you knew it was me, and I guess I was drunk, so I went along..."
                yui "... It's okay... We both made a mistake..."
            scene ep2_98 with dissolve
            mc "You like [pete]?"
            yui "W-What!? How did you know that!?"
            mc "After hearing the truth from [rin], I started to remember what happened that night."
            yui "!!!!"
            mc "At first, I wonder why you made a move on me, but it turned out you misunderstood me for [pete]."
            yui "S-Shut up!"
            scene ep2_99 with dissolve
            mc "That made me know that you like him..."
            yui "S-Stop!"
            mc "You said you chose to work at Xecon because you followed someone there."
            yui "!!!!"
            mc "That must be [pete] then."
            scene ep2_100 with dissolve
            yui "I told you to {b}SHUT UP!!{/b}"
            mc "......"
            scene black with dissolve
            $ renpy.pause(0.5, hard=True)
            scene ep2_101 with dissolve
            yui "If you say something more, I swear I'll kill you!"
            mc "......."
            yui "*Sigh*...You've always been quiet like you were so afraid to talk."
            yui "Why did you suddenly talk too much like that. How come?"
            scene ep2_102 with dissolve
            mc "......"
            yui "I'll release you, but you have to swear to me that you won't tell anyone about that, okay?"
            mc "*Nodding head*...."
            yui "Good. And if I see you telling people that I like..."
            yui "Uhm..."
            yui "Screw it! Just keep your promise. Otherwise, I'll kill you for real!"
            u "I don't think you can actually kill me though..."
            scene ep2_103 with dissolve
            rin "Heh...?"
            rin "I must say that I didn't expect this outcome."
            yui "!!!!"
            zeke "Guys... You shouldn't do something like that in a public area like this."
            scene ep2_104 with dissolve
            yui "W-What do you think we're doing!?"
            zeke "I don't know. You tell me."
            yui "Screw you!"
            scene ep2_105 with dissolve
            rin "Come on, [zeke]. Stop teasing her already."
            zeke "Hahaha. Okay."
            zeke "I was just kidding. I'm sorry, [yui]."
            yui "That wasn't funny!"
        "Stay quiet [yui1]":
            $ yui_ch1_ep2 += 1
            $ yui_relationship += 1
            scene ep2_97 with dissolve
            mc "........"
            yui "Why aren't you saying anything?"
            mc "What do you want me to say?"
            yui "Maybe say something like 'I forgive you'."
            scene ep2_98 with dissolve
            mc "I don't feel like you did something wrong."
            mc "So, you don't have to ask for my forgiveness."
            yui "Really?"
            mc "Yes."
            if sexwithyui == 1:
                mc "I should be the one saying sorry. I thought you knew it was me, and I guess I was drunk, so I went along..."
                yui "... It's okay... We both made a mistake..."
            yui "So... Are we good now?"
            mc "Up to you."
            yui "Then, we're good!"
            scene black with dissolve
            $ renpy.pause(0.5,hard=True)
            scene ep2_105 with dissolve
            zeke "We're back, guys!"
            rin "Here! Take your drink!"
    scene black with dissolve
    $ renpy.pause(0.5, hard=True)
    scene ep2_106 with dissolve
    rin "So......"
    rin "Everything is all good now?"
    yui "Yeah."
    zeke "Your drink, man."
    mc "Thank you."
    scene ep2_107 with dissolve
    rin "I'm glad to hear that."
    rin "You know...I really want to see you guys get along."
    yui "....."
    rin "We're housemates after all. We have to live together for a long time."
    rin "At least six months for the minimum length of the tenancy agreement."
    rin "So, we should be nice to each other."
    scene ep2_108 with dissolve
    rin "But on the other hand, I also think it's good that you guys fought."
    yui "Hm? Why do you think like that?"
    rin "You know... I think that people tend to become good friends after making up for their fights."
    rin "To be honest, before [zeke] and I became friends, we hated and fought each other a lot, too!"
    yui "Really? I can't imagine that."
    scene ep2_109 with dissolve
    zeke "Hm? Did you just mention my name?"
    rin "Oh! Yeah, I did."
    rin "I told [yui] about how much we hated each other before becoming friends!"
    zeke "Oh yeah! I really hated you back then!"
    scene ep2_110 with dissolve
    zeke "I still remember your facial expression at the first time we met!"
    zeke "You looked at me as if I was a piece of trash!"
    rin "Weren't you?"
    zeke "Hahaha. Yeah, I was! I admit it!"
    rin "Yeah, you were a really bad student back then."
    yui "Are you kidding? I can't think of him being a bad student."
    yui "I mean... I'm pretty sure that he was a noisy nerd."
    rin "Oh, girl...."
    rin "You have no idea..."
    zeke "Hey! Can we just stop talking about my past already, okay?"
    rin "*Giggles*...If that's what you want..."
    scene ep2_111 with dissolve
    rin "Alright, I'm going to swim now. Let's finish our drinks."
    rin "[yui], can you apply sunscreen for me, please?"
    yui "Sure. I need you to do it for me as well."
    rin "Okay."
    scene black with dissolve
    s "*A few minutes later*...."
    play music "sfx/beach3.mp3" fadein 3.0
    $ bgm = "MusicbyAden & Atch - Sunrise"
    scene ep2_112 with fade
    rin "Let's go guys! It's time to enjoy!"
    zeke "Yeahhh!"
    scene ep2_113 with dissolve
    zeke "Hm?..."
    zeke "Wait a sec..."
    scene ep2_114 with dissolve
    zeke "What are you doing, man?"
    zeke "Get up! Come with us!"
    rin "Yeah, let's just forget about everything, and enjoy swimming!"
    mc "No, I'm good. I'd rather stay here."
    scene ep2_115 with dissolve
    zeke "Come on, man!"
    zeke "....Oh, I got it!"
    zeke "You're worrying about our stuff, right?"
    zeke "Don't worry, man! This place is very safe."
    zeke "No one is gonna steal our stuff around here."
    rin "Yeah."
    mc "...I'm not worrying about that."
    zeke "Then, what's the problem?"
    scene ep2_116 with dissolve
    zeke "If you aren't going to swim in the sea, then what's the point to come here?"
    mc "Not everyone comes to beach to swim, okay?"
    mc "Look around you, those guys are singing while playing a guitar."
    mc "Those kids are building a sand castle."
    mc "So, I just want to lie down here, and enjoy the atmosphere."
    zeke "...Oh."
    scene ep2_117 with dissolve
    rin "It's okay. If he insists to stay here, then we should listen to him."
    rin "We shouldn't force people to do something they don't want, right?"
    zeke "Yeah... To think about that, you're right."
    rin "Then, let's just leave him here, and go swimming."
    zeke "Okay!"
    scene ep2_118 with fade
    zeke "Let's go!!"
    rin "*Giggles*.....Yay!"
    scene ep2_119 with dissolve
    zeke "Woooh!!!"
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_120 with dissolve
    yui "Arr... So cold!"
    zeke "This feels so good...."
    zeke "It's been... Err... Three months since I felt relaxed like this!"
    rin "Right?"
    scene ep2_121 with dissolve
    rin "Haaa... I wish we could spend a night staying at a hotel around here."
    rin "Have some good seafood for dinner..."
    rin "Alongside with a good wine so that I can sleep well..."
    rin "Then, wake up tomorrow to see the sunrise..."
    zeke "That sounds really awesome."
    rin "Yes, it does."
    rin "But....."
    scene ep2_122 with dissolve
    rin "Unfortunately, it's Monday tomorrow...."
    scene ep2_124 with dissolve
    zeke "Ugh!..."
    zeke "You just woke me up from a really good dream..."
    zeke "*Sigh*...Well... Yeah, tomorrow is Monday...."
    zeke "Damn! We should've come here yesterday..."
    scene ep2_122 with dissolve
    rin "*Sigh*...Yeah. Too bad, we didn't prepare to come here in the first place."
    rin "This is such an urgent trip."
    scene ep2_123 with dissolve
    zeke "We can't change the past though... But we can change the future into a better past!!"
    zeke "We still have a lot of chances to come back here in the future. Let's think about that later."
    scene ep2_124 with dissolve
    zeke "What you need to do now, is just cheer up!"
    zeke "You should just enjoy and have fun so you won't regret this short trip!"
    rin "Yeah, you're right."
    scene ep2_125 with fade
    u "They seem to really have fun out there...."
    scene ep2_126 with dissolve
    mc "......"
    u "Well... To be honest I'm feeling a little bit hot here..."
    u "......."
    u "...Perhaps, I should...."
    $ renpy.sound.play("sfx/phone vibrating.mp3")
    scene ep2_126 with vpunch
    stop sound fadeout 2.0
    $ newmessage = True
    $ alice_messages_show = True
    $ alice_newmessage = True
    $ phone_alert = True
    $ alicemessage = True
    s "*Vibrates*...."
    scene ep2_126_1 with dissolve
    u "Hm?..."
    u "Did someone just send me a message?"
    scene ep2_126_2 with dissolve
    u "Well..."
    u "Let's have a look."
    jump messagefromalice
label messagefromalice:
    if reply_alice2 == False:
        scene ep2_126_2 with vpunch
        u "I should reply to the message first!"
        jump messagefromalice
    elif reply_alice2 == True:
        jump goswimming
label goswimming:
    scene black with dissolve
    $ renpy.pause()
    scene ep2_126_j1 with dissolve
    u "Okay..."
    u "Since it's getting hotter up here, I think I'll just go there and put my feet in the water."
    u "Maybe, I'll walk on the beach for a bit, too..."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j2 with dissolve
    zeke "Come on, [rin]!"
    zeke "You don't need that swim ring. It's actually shallow here."
    zeke "You aren't going to drown."
    rin "No, I'd rather stay up here."
    zeke "Come on... You can't be good at swimming without practicing..."
    scene ep2_126_j3 with dissolve
    zeke "...Hm?"
    rin "What's wrong?"
    scene ep2_126_j4 with dissolve
    zeke "It's [mc]! He's coming this way!"
    rin "W-What? Are you joking?"
    zeke "No, I'm not! Just turn around and look for yourself!"
    rin "O-Oh!"
    scene ep2_126_j5 with dissolve
    zeke "What's up, man?"
    zeke "You changed your mind after seeing us having fun, huh?"
    scene ep2_126_j6 with dissolve
    mc "....."
    mc "Yes."
    scene ep2_126_j7 with dissolve
    zeke "What!? You aren't kidding me, right?"
    scene ep2_126_j6 with dissolve
    mc "Yes, I was just kidding."
    zeke "Damn you!"
    scene ep2_126_j7 with dissolve
    zeke "I know that it's pretty hot up there..."
    zeke "Are you sure that you don't want to come down here?"
    zeke "You know... This cold water makes you feel really comfortable."
    rin "Yeah, come and enjoy it with us!"
    scene ep2_126_j8 with dissolve
    mc "No, thanks."
    zeke "*Whispers*...[rin]!"
    rin "*Whispers*...What?"
    zeke "*Whispers*...You said that we shouldn't force people to do something they don't want."
    rin "*Whispers*...Yes, I did!"
    zeke "*Whispers*...But the fact that he actually walked here, I think he secretly wanted to join us."
    zeke "*Whispers*...So... Let's go and get him!"
    rin "*Whispers*...Okay!"
    play music "sfx/beach2.mp3" fadein 3.0
    $ bgm = "Galaxy Voices - Cauzmonote"
    scene ep2_126_j9 with dissolve
    u "....Hm?"
    zeke "Hahaha...I got y-"
    scene ep2_126_j10 with dissolve
    zeke "W-What!?..."
    zeke "How did you dodge that!?"
    mc "......"
    zeke "Hmmm? I see..."
    zeke "So, you've got some skills, huh?"
    zeke "But..."
    scene ep2_126_j11 with dissolve
    zeke "I also have my moves, too!"
    zeke "Got y-"
    scene ep2_126_j12 with dissolve
    zeke "!!!!"
    rin "(Wow... I never knew he had such a really fast reaction like this.)"
    rin "(I have to be quiet... I can't let him know that I'm right behind him...)"
    scene ep2_126_j13 with dissolve
    zeke "(Damn... This guy is no joke.)"
    zeke "(I can't believe that he actually caught my arm like that.)"
    zeke "(I thought I was fast enough, but obviously I was wrong...)"
    scene ep2_126_j14 with dissolve
    rin "Ha! I got you!"
    mc "Aw..."
    zeke "Nice catch, [rin]!"
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j15 with dissolve
    rin "*Giggles*...Hehe... You can't escape now..."
    rin "What are you going to do, hm~?"
    mc "......."
    u "*Sigh*...These people..."
    scene ep2_126_j16 with dissolve
    rin "Stay still, okay?"
    mc "...Okay."
    rin "Good boy~"
    scene ep2_126_j17 with dissolve
    zeke "Nice one."
    rin "*Giggles*...Hehe.. Thanks!"
    scene ep2_126_j18 with dissolve
    zeke "Well, I must say that you really impressed me, man."
    zeke "I didn't expect you to move that quick."
    rin "Me too!"
    mc "......"
    zeke "Those movements....."
    zeke "You must've gone through some trainings, huh?"
    mc "....Can you let me go now?"
    scene ep2_126_j19 with dissolve
    zeke "We'll let you go if you promise to join us!"
    mc "You leave me no choice at all."
    rin "*Giggles*...Isn't it good for you? You don't even need to think about the answer!"
    mc "*Sigh*...Fine."
    zeke "That's right, my dude!"
    scene ep2_126_j20 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j20.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j20_rinblink.jpg", 1) with dissolve
    rin "Please, don't be angry at us."
    mc "......."
    rin "I don't know why you always look so emotionless..."
    rin "but I really want you to be happy and have fun."
    u "Happy? Fun?...."
    u "I almost forgot these words...."
    u "I can't remember the last time I felt that...."
    scene ep2_126_j20 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j20.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j20_zekeblink.jpg", 1) with dissolve
    zeke "Yeah! You can't be like this for your entire life!"
    zeke "We have feelings, that's why we're humans!"
    mc "....Animals also have feeling though..."
    scene ep2_126_j21 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j21.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j21_rinblink.jpg", 1) with dissolve
    rin "*Giggles*...Hahaha. That's funny!"
    zeke "......."
    scene ep2_126_j21 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j21.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j21_zekeblink.jpg", 1) with dissolve
    zeke "Okay, I'm sorry!"
    zeke "I was just trying to tell you that you should show your emotions more!"
    zeke "Smile when you're happy."
    zeke "Laugh when you hear something funny."
    zeke "Cry when you feel sad."
    zeke "You're a human, not a robot!"
    mc "...Okay. That's enough."
    mc "I will join you guys, but I'm going to need to take my top off first."
    mc "I only have one outfit, so I don't want it to get soaked."
    scene ep2_126_j22 with dissolve
    zeke "Alright, I'll go with you!"
    mc "....Don't touch me. Your body is so wet."
    zeke "What's the matter? You're going to get soaked soon, too!"
    scene ep2_126_j23 with dissolve
    zeke "Okay. You can take your top off now."
    mc "...You sound just like a pervert to say that to me."
    zeke "W-What?"
    zeke "No! I didn't mean in that way!"
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j24 with dissolve
    zeke "Hmmmm?...."
    mc "......"
    zeke "Last time I was in a hurry shutting the door."
    zeke "So, I haven't noticed until now, but you're pretty fit, aren't you?"
    scene ep2_126_j25 with dissolve
    zeke "You have some muscles, but not too big as bodybuilders."
    zeke "You also did some fighting training, didn't you?"
    mc "...Yes, I did."
    zeke "No wonder why you could move that fast. I get it now."
    mc "Can we go swimming now?"
    scene ep2_126_j26 with dissolve
    zeke "Sure!"
    zeke "Let's go!!"
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j27 with dissolve
    rin "*Giggles*...[zeke]..."
    zeke "What?"
    rin "If I were you, I wouldn't dare to stand near [mc]."
    rin "Especially, when both of you are topless!"
    zeke "S-Shut up!"
    rin "*Giggles*...Hahaha..."
    zeke "I used to have muscles, too! Okay!?"
    zeke "Actually, I still have some of them left! Come and watch!"
    rin "*Giggles*...No, thanks."
    scene ep2_126_j28 with dissolve
    zeke "Look... So beautiful, right?"
    zeke "You made a right choice to join us."
    u "...You guys actually gave me no choice."
    scene ep2_126_j29 with dissolve
    rin "Usually, a lot of people will come here on the weekend."
    rin "But, seems like we're lucky today. There are only a few people here."
    scene ep2_126_j30 with dissolve
    rin "(Hm?...)"
    scene ep2_126_j31 with dissolve
    $ renpy.pause()
    scene ep2_126_j32 with dissolve
    rin "(Heh...)"
    rin "(You want to throw him into the water, right?)"
    scene ep2_126_j33 with dissolve
    rin "(Okay! I got it!)"
    u "*Sigh*...Look at them sending signals behind my back..."
    u "....They're planning to do something again."
    u "*Sigh*...I'm going to pretend that I don't know then..."
    scene ep2_126_j34 with dissolve
    zeke "Ha! I've got him!"
    mc "....Ah."
    zeke "Hurry up! You need to lift up his legs!"
    rin "Okay!"
    scene ep2_126_j35 with dissolve
    zeke "[yui]!"
    zeke "Come here, and help [rin] do it!"
    scene ep2_126_j36 with dissolve
    yui "Jeez... You guys are playing like kids..."
    zeke "Stop complaining, and come here already!"
    zeke "I can't hold him for long!"
    yui "Okay... Okay!"
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j37 with dissolve
    yui "Ugh!...He's so heavy..."
    zeke "Alright, I'm gonna count to three..."
    mc "......."
    zeke "One..."
    zeke "Two..."
    scene ep2_126_j38 with dissolve
    zeke "THREE!!!"
    rin "Yay!"
    $ renpy.sound.play("sfx/splash.mp3", loop=False)
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j39 with dissolve
    zeke "Hahaha... You're all soaked, man!"
    zeke "Argh...I wish I had my phone with me now...."
    zeke "I want to take a photo of you now, hahaha."
    yui "Hey, don't look at me like that."
    yui "They told me to do it, okay?"
    mc "...Whatever."
    scene black with dissolve
    s "*A few moments later*....."
    scene ep2_126_j40 with dissolve
    rin "*Giggles*...How do you feel?"
    scene ep2_126_j41 with dissolve
    mc "....Cold."
    rin "*Giggles*...But it's better than feeling hot, right?"
    mc "Yeah...."
    u "Alright. I've learned something new."
    u "In order to make them stop bothering me, I should just let them do what they want."
    u "Yeah, I can do that unless it's too much for me."
    scene ep2_126_j42 with dissolve
    rin "(Hm?...)"
    rin "[mc]..."
    mc "What?"
    scene ep2_126_j43 with dissolve
    rin "Nice tattoo."
    mc "...Thanks."
    zeke "Oh? He has a tattoo?"
    rin "Yeah."
    zeke "I didn't notice that...."
    rin "Actually, I saw it before because when you wore a t-shirt, the shirt didn't cover all of it."
    rin "But, this is the first time I've seen your whole tattoo."
    rin "I wonder if it has any meaning...."
    scene ep2_126_j44 with dissolve
    mc "....Meaning?"
    rin "Yeah. Do you mind telling me?"
    mc "Well... That's a long story..."
    scene ep2_12 with fade
    u "I was an orphan since the first day I was born, because my parents left me at a church in Romford."
    u "When I was 6 years old, I was adopted by a married couple."
    u "They adopted me because it was hard for them to have children."
    u "I was excited that I finally have parents. Everything was good. It looked like they really loved me and took cared of me very well."
    u "But my happiness didn't last that long...."
    u "A year later, my adoptive mother got pregnant. So, they didn't want me anymore."
    u "But, instead of sending me back to the church. They abandoned me in some slum area that I had no idea where it was."
    scene ep2_126_j45 with dissolve
    u "I did everything I could to survive."
    u "I stole food from nearby stores so that I could have something to eat."
    u "But, in a very dangerous area like the slums, you often got beat up for ridiculous reasons."
    u "And I got beat up so many times. It got so bad that I sometimes wanted to kill myself to end all of my pain."
    u "Until that day..."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j46 with dissolve
    butler "Be careful, sir."
    butler "There are so many thieves here."
    unknown "Why do I have to be careful when I've got you around?"
    unknown "There is no way you will let them touch me, right?"
    butler "No, sir."
    scene ep2_126_j47 with dissolve
    unknown "...Hm?"
    butler "What's wrong, sir?"
    scene ep2_126_j48 with dissolve
    unknown "That kid..."
    butler "Oh, poor kid. He's injured."
    unknown "....."
    scene ep2_126_j49 with dissolve
    unknown "Take him back with us."
    butler "...Pardon?"
    unknown "I said take him back with us."
    butler "Err... May I ask for your reason, sir?"
    unknown "......."
    butler "Understood. I'll bring him back with us."
    unknown "Good."
    scene ep2_126_j48 with dissolve
    unknown "Hey, kid."
    unknown "Tell me your name...."
    unknown "Actually, forget it."
    unknown "From now on, your name is [mc]."
    mc "...[mc]?"
    unknown "Yes, [mc]."
    unknown "Listen. I'll give you a new life, a life that is a hundred times better than this."
    unknown "You'll have a place to sleep, you'll have a fireplace that keeps you warm on a cold night."
    unknown "You'll no longer have to either beg, or steal for food and money."
    unknown "But..."
    mc "....What do I have to do for that?"
    unknown "...Oh! You're quite smart, aren't you?"
    scene ep2_126_j50 with dissolve
    unknown "No, there is nothing I want from you....."
    unknown ".....Now."
    unknown "All you need to do is just get up, and follow me."
    unknown "Do you want to have a new life, or stay here trying so hard to survive?"
    unknown "Your choice...."
    mc "......"
    scene black with dissolve
    rin "......[mc]!"
    mc "......."
    scene ep2_126_j51 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j51.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j51_blink.jpg", 1) with dissolve
    rin "[mc]!"
    mc "...What?"
    rin "Are you okay? You went blank for almost a minute!"
    scene ep2_126_j52 with dissolve
    mc "I'm fine...."
    mc "I was just thinking about my past..."
    scene ep2_126_j53 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j53.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j53_blink.jpg", 1) with dissolve
    zeke "Your past!?"
    zeke "Tell me more! I want to know you more!"
    scene ep2_126_j51 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j51.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j51_blink.jpg", 1) with dissolve
    rin "Me, too!"
    rin "I only know that you're 22 and you lived in East Town before."
    rin "You became my housemate, and now we're working for the same company."
    rin "Umm.... That's all I know!"
    mc "......"
    mc "What do you want to know then?"
    scene ep2_126_j51_1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j51_1.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j51_1_blink.jpg", 1) with dissolve
    rin "You still didn't answer my previous question, so I'm going to ask it again."
    rin "Your tattoo. Does it have any meaning?"
    menu:
        "Yes":
            mc "Yes, it does."
            rin "Really? What is it?"
            mc "Well... I can't tell you about that."
        "I can't tell":
            mc "Well... I can't tell you about that."
    scene ep2_126_j51 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j51.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j51_blink.jpg", 1) with dissolve
    rin "Come on..."
    rin "Trying to be mysterious, huh?"
    mc "No, I'm not..."
    rin "*Sigh*...Okay. How about this?..."
    scene ep2_126_j51_1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j51_1.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j51_1_blink.jpg", 1) with dissolve
    rin "Have you ever had a girlfriend?"
    zeke "Wait! Why are you asking him such a question?"
    rin "I'm just curious, okay!?"
    rin "He's always emotionless like this, so I wonder if he ever went out with someone."
    mc "......"
    menu:
        "Answer":
            mc "No. I never had a girlfriend."
            rin "*Giggles*....That was pretty obvious though..."
            mc "......"
        "Pass":
            mc "Next question."
            rin "*Giggles*....Are you too shy to say that you never had a girlfriend?"
            mc "......"
    scene ep2_126_j53 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j53.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j53_blink.jpg", 1) with dissolve
    zeke "My turn! Let me ask him, too!"
    rin "Okay."
    zeke "You moved quite far away from your old city."
    zeke "Do you miss your parents?"
    menu:
        "No":
            mc "No, I don't."
            zeke "Really? You don't miss them at all?"
            mc "I don't have parents."
        "I'm an orphan":
            mc "No, I don't."
            zeke "Really? You don't miss them at all?"
            mc "I'm an orphan."
            mc "So, I don't have parents."
    scene ep2_126_j54 with dissolve
    zeke "......"
    rin "*Mouths*...You idiot! Why did you ask him such a question?"
    zeke "Err... I'm sorry, man."
    mc "It's okay."
    scene ep2_126_j55 with dissolve
    zeke "Anyway, I'm so proud of you, man!"
    mc "......."
    zeke "Even though you didn't say it, I'm pretty sure that you've been through a lot of things."
    zeke "So, to see that you got a job at our company, I'm really proud of you..."
    mc "...Okay."
    zeke "Let's find something fun to do to cheer you up!"
    zeke "Um... How about riding a jet ski? Can you ride it?"
    mc "No. I'd like to stay here."
    zeke "Okay. Then, I guess I'll have to ride it alone."
    jump Helprin
label Helprin:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        else:
            $ mc_name = persistent.mc_name
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j56 with dissolve
    rin "Aww... So relaxing..."
    rin "It's so nice out today..."
    rin "The waves aren't too strong today, too. Nice."
    mc "......"
    scene ep2_126_j57 with dissolve
    mc "You can't swim?"
    scene ep2_126_j58 with dissolve
    rin "Hm?..."
    rin "Oh! No, I can actually."
    mc "Then, why..."
    rin "I can swim, but I'm not quite good at it."
    rin "So, I feel more safe to use this swim ring."
    mc "I see..."
    scene ep2_126_j59 with dissolve
    zeke "*Yelling in the distance*....Watch out!..."
    rin "W-Wait! No! Don't come this way!"
    mc "......"
    scene ep2_126_j60 with dissolve
    zeke "Hahahahaha!...."
    rin "[zeke]!...You bastard!"
    scene ep2_126_j61 with dissolve
    s "*Noisy scream*...."
    scene ep2_126_j62 with dissolve
    yui "(That's [rin]'s voice.)"
    yui "(Why is she screami-)"
    scene ep2_126_j63 with dissolve
    yui "(!!!!)"
    scene ep2_126_j64 with dissolve
    yui "Oh...S-"
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/rindrowning.mp3" fadein 3.0
    $ bgm = "Mauro Somm - What You Used To Be"
    scene ep2_126_j65 with dissolve
    yui "*Cough*...Are you trying to kill us!?"
    yui "Come back here! I swear I'm going to kick your ass!"
    scene ep2_126_j66 with dissolve
    zeke "Hahahaha... I'm sorry!"
    zeke "I couldn't control the jet ski, it was more powerful that I thought!"
    mc "*Cough*...Are you okay, [rin]?"
    s "........"
    scene ep2_126_j67 with dissolve
    mc "[rin]?"
    yui "That's bullshit!"
    mc ".....Shit."
    menu:
        "Help her":
            scene ep2_126_j68 with dissolve
            yui "Hm?"
            s "Once you realise that [rin] is drowning, you immediately dive in the sea seaching for her."
    scene ep2_126_j65 with dissolve
    yui "Hey!! [rin]'s drowning!"
    zeke "W-What!? Is she for real!?"
    yui "There is no way I'm joking about her life, okay!?"
    zeke "E-Er... Wait a sec! I'm coming!!"
    scene black with dissolve
    $ renpy.pause()
    scene ep2_126_j69 with dissolve
    rin "*Cough*....."
    mc "Relax. Take a deep breath."
    rin "*Cough*...I...I...."
    s "[rin]'s shaking in fear while trying to say something."
    mc "It's okay. Don't be scared. I've got you."
    rin "O-Okay..."
    scene black with dissolve
    $ renpy.pause(0.1,hard=True)
    scene ep2_126_j70 with dissolve
    rin "......."
    rin "Thank you. You saved my life."
    mc "...Anytime."
    rin "I must've been dead already if it wasn't for you..."
    mc "You're alright now."
    rin "Yeah, that's because of you."
    scene ep2_126_j71 with dissolve
    mc "By the way, if I were you, I would cover your chest."
    rin "My chest?..."
    mc "Yeah."
    rin "What are you..."
    scene ep2_126_j72 with dissolve
    rin "....talking abo-"
    scene ep2_126_j73 with dissolve
    rin "!!!"
    rin "Err....."
    rin "Thanks for telling me."
    mc "You're welcome."
    scene ep2_126_j74 with dissolve
    yui "Are you okay, [rin]!"
    zeke "[rin]!! I'm sorry!"
    zeke "I...I...didn't want that to happen!"
    scene ep2_126_j75 with dissolve
    rin "I-I'm good.... Thank you."
    yui "Are you sure? Why is your cheek red like that?"
    rin "N-Nothing!"
    mc "...She lost her top when drowning."
    mc "Look after her. I'm going to find it."
    yui "Okay."
    scene black with dissolve
    s "*Half a minute later*...."
    scene ep2_126_j76 at eyesblink("Ch.1/Ep.2/Scenes/ep2_126_j76.jpg", "Ch.1/Ep.2/Scenes/ep2_126_j76_rin_zeke.jpg", 1) with dissolve
    rin "......"
    rin "Have you found it?"
    mc "Yes."
    scene ep2_126_j77 with dissolve
    rin "Really?"
    mc "Here you are."
    rin "Thank you!"
    $ renpy.end_replay()
    $ helprin = True
    $ rin_ch1_ep2 += 2
    $ rin_relationship += 2
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/beach4.mp3" fadein 3.0
    $ bgm = "Metro Vice - Voices"
    scene ep2_126_j78 with dissolve
    s "After that accident, we decided to stop swimming and got back to the chairs."
    yui "*Mumbles*...Yes! Eat that!"
    rin "What are you doing, [yui]?"
    scene ep2_126_j79 with dissolve
    yui "I'm playing the game called {b}Black Desert{/b}."
    yui "Have you ever heard it?"
    rin "Of course, I have."
    rin "It would be a shame for people working in a game company like us if we don't know it."
    rin "It's an Korean MMORPG game, right?"
    yui "Yeah, one of the best MMORPG games in the world right now, in my opinion."
    rin "I agree..."
    rin "It has a really good combat system that the other games can hardly compete with!"
    yui "I know right!"
    scene ep2_126_j80 with dissolve
    yui "By the way..."
    yui "...[rin]."
    rin "Hm?..."
    scene ep2_126_j81 with dissolve
    yui "Are you going to ignore him like that?"
    rin "Yeah. He deserves it."
    zeke "[rin]....."
    zeke "I knew that I was wrong."
    zeke "I'm so sorry. I shouldn't have done that."
    zeke "Please, forgive me...."
    scene ep2_126_j80 with dissolve
    rin "If you knew that you were wrong, why'd you do that in the first place?"
    zeke "I...I...."
    rin "I almost died because of you."
    rin "You know that, right?"
    scene ep2_126_j81 with dissolve
    zeke "Yeah, that's why I'm feeling so guilty now..."
    rin "You aren't expecting me to easily forgive you, right?"
    zeke "....No, I'm not."
    rin "Then, keep staying like that until I feel like forgiving you."
    zeke "......"
    scene ep2_126_j82 with dissolve
    zeke "[mc]. Help me, dude."
    rin "Hey! Leave him alone."
    rin "Don't ask him to help you take responsibility for your crazy action."
    mc "......."
    unknown "Ehh...!?"
    scene ep2_126_j83 with dissolve
    u "Hm?..."
    unknown "[zeke]?...[rin]?..."
    rin "Oh?"
    scene ep2_126_j84 with dissolve
    elaine "Yeah, it's really you guys!"
    elaine "What a coincidence! I didn't expect to see you guys here!"
    wendy "Hello, everyone."
    scene ep2_126_j85 with dissolve
    rin "Aw! What a surprise!"
    rin "I'm so happy to see you and [wendy] here, too!"
    elaine "Pff! Don't say that!"
    elaine "Actually, I'm a little bit angry now!"
    elaine "How could you come here without inviting us!?"
    scene ep2_126_j92 with dissolve
    rin "...I'm sorry."
    rin "I thought you guys were busy."
    elaine "*Giggles*...Aw! Don't be sad."
    elaine "I was just kidding!"
    wendy "Jeez... You really like to tease [rin], do you?"
    scene ep2_126_j85 with dissolve
    rin "Aw! You got me again!"
    elaine "Hehe..."
    rin "Jeez... When are you going to stop teasing me?..."
    zeke "What's up, girls!"
    elaine "Hey! How's everything, [zeke]?"
    scene ep2_126_j86 with dissolve
    rin "Since when did I tell you to get up!?"
    zeke "Er-"
    rin "Kneel down on the ground right now!"
    zeke "......"
    scene ep2_126_j87 with dissolve
    zeke "Okay...."
    elaine "*Giggles*...Did you do something stupid again, [zeke]?"
    rin "*Sigh*...He almost killed me."
    wendy "What!?"
    elaine "Are you serious?"
    rin "Yes, I am."
    wendy "Oh... Then, he deserves it."
    scene ep2_126_j88 with dissolve
    elaine "By the way...."
    elaine "Who are those guys?"
    rin "Oh! They are new employees at our company, and also my housemates, too."
    elaine "I see..."
    scene ep2_126_j89 with dissolve
    rin "That woman is [yui]."
    yui "Hi, nice to meet you."
    elaine "Nice to meet you, too!"
    scene ep2_126_j90 with dissolve
    rin "That man is [mc]."
    mc "........"
    mc "*Nodding head*....Hello."
    scene ep2_126_j91 with dissolve
    elaine "(Heh...? He's quite handsome, isn't he?)"
    rin "*Giggles*...Please, don't mind him. He doesn't talk much."
    elaine "Hi~!"
    wendy "Nice to meet you."
    $ girlsintroduce = True
    $ wendy_ch1_ep2 += 1
    $ eliane_ch1_ep2 += 1
    $ wendy_relationship += 1
    $ eliane_relationship += 1
    scene ep2_126_j92 with dissolve
    elaine "Oh! I almost forget why we are here."
    rin "Hm? What do you mean?"
    elaine "We were about to play beach volleyball, but we didn't have enough people to play."
    elaine "So, we're looking for people to join us. Are you guys interested?"
    rin "Umm...beach volleyball..."
    rin "I'd love to join, but I'm not good at it..."
    elaine "It's okay! You don't have to worry about that."
    elaine "We just play it for fun. So, it doesn't matter if you're good or not."
    scene ep2_126_j93 with dissolve
    zeke "Let's play! I want to play it!"
    elaine "That's such a very good spirit right there!"
    zeke "I know, right!?"
    rin "Shut up."
    scene ep2_126_j87 with dissolve
    zeke "O-Oh..."
    wendy "*Giggles*..Hehe."
    rin "How about you, [yui]?"
    scene ep2_126_j89 with dissolve
    yui "Beach volleyball?"
    yui "Sounds good. Count me in."
    rin "Okay."
    scene ep2_126_j90 with dissolve
    rin "[mc]?"
    mc "Do I have a choice?"
    rin "*Giggles*...I don't know."
    mc "*Sigh*...I'll play then."
    scene ep2_126_j92 with dissolve
    elaine "Fantastic! We've got enough people now."
    rin "Already?"
    wendy "Yeah, we already have eight people including you guys."
    wendy "So, it's going to be a 4 on 4 match."
    rin "Hm? But I'm only seeing six of us right now."
    elaine "They're waiting for us at the court."
    rin "Oh, I see..."
    elaine "Let's go! Follow me!"
    scene ep2_126_j94 with fade
    elaine "There they are!"
    rin "Hm?"
    scene ep2_126_j95 with dissolve
    rin "So, you guys are double dating, huh?"
    rin "Who are those guys? I've never seen them before."
    elaine "Hehe... No, we're not double dating."
    elaine "We just met them here."
    elaine "They invited us to play with them."
    rin "*Giggles*...No doubt. You guys are really hot."
    rin "I would be more surprised if they didn't invite you."
    elaine "*Giggles*...Who knows... They might fall for you instead of us."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j96 with dissolve
    elaine "These people are my friends. We work for the same company."
    elaine "They're going to play with us."
    $ ethan_name = "Dude A"
    $ persistent.ethan_name = ethan_name
    $ ben_name = "Dude B"
    $ persistent.ben_name = ben_name
    ben "That's nice!"
    ethan "I never knew you had such beautiful friends."
    yui "(Ew... Another flirty guy who thinks it's cool to say cheesy lines like that.)"
    scene ep2_126_j97 with dissolve
    elaine "Let me introduce you guys first."
    elaine "This is [rin]."
    scene ep2_126_j98 with dissolve
    rin "Hello, I'm [rin]."
    rin "I'm not so good at beach volleyball, but I'll try my best!"
    ethan "It's my pleasure to meet you."
    ethan "You can call me Ethan."
    $ ethan_name = "Ethan"
    $ persistent.ethan_name = ethan_name
    rin "Nice to meet you, [ethan]."
    ethan "I never believed that an angel really exists..."
    scene ep2_126_j99 with dissolve
    ethan "....Until I met you."
    rin "!!!"
    yui "(Ew!...)"
    elaine "Hmm? See?"
    elaine "What did I just say to you, [rin]?"
    ben "Stop it, dude. You're making her scared."
    ben "I'm sorry for my friend. He's always like this when meeting such a very beautiful woman like you."
    rin "Err... Thanks?"
    ben "Oh! I'm Benjamin by the way."
    $ ben_name = "Benjamin"
    $ persistent.ben_name = ben_name
    scene ep2_126_j100 with dissolve
    ethan "And who is this cute woman?"
    ethan "May I know your name, please?"
    yui "......"
    scene ep2_126_j101 with dissolve
    yui "There is no way I'm going to tell you my name."
    yui "I'm here to play beach volleyball, not to listen to your cheesy lines."
    ethan "...Er..."
    rin "Please, don't mind her!"
    rin "S-She just isn't in a good mood right now!"
    scene ep2_126_j102 with dissolve
    rin "Let me introduce you those guys instead."
    ethan "Oh? We've also got dudes here?"
    rin "Of course, they come with me."
    scene ep2_126_j103 with dissolve
    rin "The guy with a shaggy orange-colored hairstyle, is [zeke]."
    rin "And the another one, is [mc]."
    zeke "Nice to meet you guys!"
    zeke "Let's have fun together!"
    scene ep2_126_j104 with dissolve
    ethan "Err... Nice to meet you."
    ben "Okay, man. Let's have a good game!"
    zeke "Sure!"
    scene ep2_126_j105 with dissolve
    ethan "Alright. Before we get started..."
    ethan "How are we going to team up?"
    elaine "Ummm? How about drawing straws?"
    rin "That's a pretty good idea!"
    wendy "Yeah, let's do it!"
    scene black with dissolve
    s "*A few moments later*...."
    scene ep2_126_j106 with dissolve
    zeke "Hahahahaha! Look at your team!"
    zeke "Poor girls... We've got all guys here except [mc]!"
    scene ep2_126_j107 with dissolve
    mc "......."
    rin "Hehe... Seems like it's going to be a hard match for us."
    scene ep2_126_j106 with dissolve
    ben "Well... I feel sorry for you girls, but we got the lineups from drawing straws."
    ben "So...."
    zeke "Hahaha! This is going to be an easy match for us!"
    wendy "....I'm not sure about that though."
    zeke "Hm? What did you say?"
    wendy "...Nothing."
    scene ep2_126_j107 with dissolve
    yui "Ugh!...Don't be overconfident!"
    yui "You'll never know what'll happen next!"
    scene ep2_126_j106 with dissolve
    ethan "Look... I think it's a bit boring to play it just for fun."
    ethan "How about the losers have to obey the winners?"
    zeke "That sounds great! I love it!"
    ethan "What do you say, girls?"
    scene ep2_126_j107 with dissolve
    yui "Ugh!..."
    rin "That's so unfair..."
    elaine "Don't worry! We aren't going to lose."
    mc "......."
    scene ep2_126_j108 with dissolve
    ethan "Are you ready?"
    ethan "I'm going to serve now!"
    elaine "Go ahead! We're ready!"
    ethan "Okay..."
    scene ep2_126_j109 with dissolve
    ben "Nice serve!"
    zeke "Nice serve!"
    ethan "Oh!"
    scene ep2_126_j110 with dissolve
    elaine "Relax, guys."
    elaine "Just try to receive the ball, and pass to me."
    rin "O...Okay!"
    scene ep2_126_j111 with dissolve
    rin "Let's do our best, [mc]!"
    mc "...Sure."
    scene ep2_126_j112 with dissolve
    ethan "Take that!"
    elaine "The ball is going to your direction, [mc]."
    mc "...Okay."
    scene ep2_126_j113 with dissolve
    mc "I got it."
    rin "Good!"
    elaine "Nice one!"
    scene ep2_126_j114 with dissolve
    elaine "Set the ball to me, [yui]!"
    yui "O-Okay!"
    zeke "Heh? You guys are quite good, aren't you?"
    yui "That's why..."
    scene ep2_126_j115 with dissolve
    yui "...I told you to not be so overconfident!"
    elaine "Excellent! You're a pretty good setter, [yui]!"
    elaine "Your ball setting is very impressive!"
    ben "Damn! She's flying!"
    elaine "Now, just leave everything to me!"
    zeke "There is no way I'm going to let you do that!"
    zeke "Yahhhhh!"
    scene ep2_126_j116 with dissolve
    elaine "Take that!"
    zeke "S-Shit!..."
    rin "Wow!"
    ethan "......."
    ben "........"
    ben "Hey... Hey..."
    ben "Dude.... What the hell just happened?"
    ethan "...I... Don't know man."
    ethan "That was... So fast."
    ethan "She spiked the ball, and in the blink of an eye, the ball landed here."
    wendy "....That's why I said I wasn't sure about us winning this match...."
    scene ep2_126_j110 with dissolve
    elaine "Do you still think that it's an easy match for you guys, hmmm?"
    rin "You're amazing, [elaine]!"
    rin "I never knew you were very good at beach volleyball like this."
    elaine "Thanks."
    elaine "It's because I was a former volleyball player when I was in high school."
    rin "*Sigh*...I used to learn how to play volleyball when I was in high school, too."
    rin "But, I'm not half as good as you..."
    scene ep2_126_j117 with dissolve
    elaine "Okay, it's our turn to serve now."
    elaine "Nice serve, [mc]!"
    rin "Nice serve!"
    u "....The loser team will have to obey to the winner team..."
    u "That isn't going to be good for me...."
    scene ep2_126_j118 with dissolve
    u "*Sigh*...Well"
    u "There is only one way to stop it from happening."
    scene ep2_126_j119 with dissolve
    ethan "....Hm?"
    scene ep2_126_j121 with dissolve
    ethan "H-H-Holy...shit!!"
    ben "W-Woah!....Woah! What the fuck, dude!?"
    scene ep2_126_j120 with dissolve
    ethan "H-He's fucking flying!"
    zeke "I knew it! You really aren't human, are you!"
    scene ep2_126_j122 with dissolve
    rin "[mc]!?..."
    elaine "Hm? What's up with these guys reactions?"
    elaine "I kinda wonder what [mc] is doing now."
    scene ep2_126_j123 with dissolve
    elaine "Heh?... I didn't expect him to do a jump serve."
    elaine "Impressive...."
    zeke "C-Chill out, dude!"
    zeke "Are you going to kill us!?"
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j124 with dissolve
    wendy "*Screams*...!!!..."
    ethan "F-Fuck! I'm outta here!"
    ethan "There's no way I'm going to receive that fucking ball!"
    ethan "It's fucking far stronger than her spike!"
    ben "Damn!... I don't wanna get slapped by this guy!"
    zeke "Seriously, dude! Are you {b}Tooru OIKAWA!?{/b}"
    zeke "Am I playing in inter high!?"
    scene ep2_126_j125 with dissolve
    elaine "*Giggles*...Oops!... You guys are so funny!"
    elaine "*Giggles*...Hahaha... Look at you guys running away from the ball!"
    elaine "How are you going to win then?"
    rin "That was amaaaaazing, [mc]!"
    rin "How did you do that!?"
    yui "Hey! What if it hit my head!?"
    mc "....No, it won't."
    scene ep2_126_j126 with dissolve
    ethan "*Ahem*...Sir..."
    ethan "This is just a friendly, not a competitive match..."
    ethan "Can you stop doing a jump serve like that?"
    yui "Hey! What!?"
    yui "Didn't you just talk about a reward for the winner?"
    ethan "Yeah, I did. But..."
    yui "Then, it has already become a competitive match!"
    ethan "I know, but..."
    ethan "...At least give us a chance to play, please?"
    scene black with dissolve
    s "*A few moments later*...."
    scene ep2_126_j127 with dissolve
    rin "Yes! I got it!"
    elaine "Nice receive, [rin]!"
    scene ep2_126_j128 with dissolve
    ethan "F-Fuck!...."
    zeke "Don't mind!"
    scene ep2_126_j130 with dissolve
    wendy "Here you go!"
    ben "Nice setting, girl!"
    scene ep2_126_j132 with dissolve
    yui "Ugh!..."
    yui "I'm sorry. I should've received it."
    elaine "No worries! We're still leading."
    scene ep2_126_j129 with dissolve
    ben "A-Argh!..."
    ben "Sorry guys. I couldn't reach it."
    zeke "Don't mind!"
    scene ep2_126_j130 with dissolve
    wendy "Spike it, [zeke]!"
    zeke "Sure! Leave it to me!"
    scene ep2_126_j131 with dissolve
    rin "Wow! You actually received it?"
    zeke "W-What the...!?"
    elaine "I've already lost count of how many times you impressed me today, [mc]!"
    scene ep2_126_j133 with dissolve
    rin "Aw!..."
    elaine "Don't mind! Don't mind!"
    scene black with dissolve
    $ renpy.pause()
    scene ep2_126_j134 with dissolve
    rin "Yes! We won!!"
    yui "Well, that's no doubt."
    yui "After seeing what [elaine] and [mc] could do, I was so sure that we were going to win."
    elaine "You're really really good, [mc]."
    mc "...Thanks."
    scene ep2_126_j135 with dissolve
    rin "Come on, [mc]!"
    rin "Give me a high five!"
    mc "......"
    scene ep2_126_j136 with dissolve
    rin "*Giggles*...Yeah! That's right!"
    rin "I've never thought that a beach volleyball game would be so much fun until today!"
    elaine "It's very fun because we are the winners."
    elaine "You might've changed your mind if you were on the loser side."
    rin "*Giggles*...Maybe!"
    elaine "Well... Talking about losers..."
    scene ep2_126_j137 with dissolve
    elaine "Losing to girls..."
    elaine "How do you feel, guys?"
    zeke "*Pants*...That... Doesn't count! You had [mc] on your team!"
    ben "*Heavily breaths*...Y..Yeah...."
    elaine "*Giggles*...I don't care. A deal is a deal."
    elaine "Get up, and follow us."
    ben "*Pants*...[ethan], you fucking piece of shit!"
    ben "....Why did you have to mention anything about a punishment!!"
    ethan "*Heavily breaths*...F-Fuck! I didn't expect us to lose, okay!?"
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene ep2_126_j138 with dissolve
    rin "So...."
    rin "What should we tell them to do, [elaine]?"
    zeke "Come on... Do you really have to do this?"
    yui "Of course, we do!"
    yui "You guys set the rule by yourself, so just deal with it."
    scene ep2_126_j139 with dissolve
    elaine "How about this?"
    elaine "I want you guys to dance."
    wendy "D-Dance...?"
    elaine "Yes."
    elaine "Try to impress us by your dancing skills until we're satisfied."
    scene ep2_126_j138 with dissolve
    rin "Heh? That sounds good!"
    yui "Yeah, I'm okay with that."
    elaine "What's about you, [mc]?"
    mc "...Okay."
    scene ep2_126_j139 with dissolve
    wendy "Ugh!...You knew that I'm not good at dancing..."
    elaine "I'm sorry, [wendy]."
    elaine "Just try your best, okay!?"
    elaine "*Mouths*...Don't worry. I'll go easy on you."
    zeke "H-Hey! Do you think that I don't know what you just said!?"
    elaine "Hm? What did I say?"
    zeke "You sai-!"
    elaine "You're losers. You aren't allowed to argue!"
    elaine "Just start dancing already!"
    play music "sfx/dance.mp3" fadein 3.0
    $ bgm = "Peyruis - Intense"
    scene black with dissolve
    show dance
    elaine "Hahahaha! What are you doing, [zeke]?"
    rin "Oops!... You call that a dance!?"
    yui "Ugh! I can't bare to watch..."
    zeke "S-Shut up!..."
    elaine "Aw! You're so cute when dancing, [wendy]..."
    elaine "I like that!"
    zeke "Hey! Stop being biased, please!"
    zeke "She's doing nothing, but clapping her hands!"
    ethan "Girls? What about me?"
    elaine "Err...."
    elaine "You're doing okay..."
    ethan "Right!? I knew that!"
    rin "......."
    elaine "But, I think [ben]'s the best right now though..."
    ben "Then, can I stop now?"
    elaine "No, keep dancing!"
    $ renpy.pause()
    hide dance
    scene ep2_126_j141 with dissolve
    u "......"
    u "Seems like they're having fun."
    u "......"
    scene ep2_126_j142 with dissolve
    rin "Hm?..."
    rin "Where are you going, [mc]?"
    mc "...I'm gonna go for a walk."
    scene ep2_126_j143 with dissolve
    elaine "(......)"
    scene ep2_126_j144 with dissolve
    elaine "I'm going to get some water."
    rin "Oh? Do you want me to go with you?"
    elaine "*Giggles*...No. I think you better stay here to judge these dancers."
    rin "If you say so."
    scene ep2_126_j145 with dissolve
    elaine "*Giggles*...."
    jump elianeact
label elianeact:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        else:
            $ mc_name = persistent.mc_name
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/witheliane.mp3" fadein 3.0
    $ bgm = "MBB - Sax"
    scene ep2_126_j146 with dissolve
    elaine "Boo!!"
    mc "......"
    mc "Ahh...."
    elaine "Oops!...Haha!..."
    elaine "*Laughs*...What was that!?"
    elaine "Are you trying to pretend that you're shocked?"
    mc "......."
    scene ep2_126_j147 with dissolve
    elaine "Heh? You're ignoring me?"
    mc "No."
    elaine "Then, why didn't you answer me?"
    mc "You knew the answer already. So, I chose to not answer."
    elaine "Interesting..."
    elaine "You have talents, but you don't brag about it..."
    elaine "You don't talk much which is pretty nice."
    elaine "I don't like guys who are all talk."
    $ elaine_hate1 = "Boasters"
    elaine "You're kind of handsome, too."
    scene ep2_126_j148 with dissolve
    elaine "*Giggles*...Actually... To be honest you're really my type!"
    mc "...What are you trying to say exactly?"
    elaine "Nothing! I just want to tell you that."
    mc "...I'm sorry, but I'm not interested in women."
    scene ep2_126_j149 with dissolve
    elaine "Hehh? Are you interested in men then?"
    mc "No."
    elaine "I knew it. I can tell if someone's a real man or not."
    elaine "Then, what's the thing you're interested in?"
    mc "...Nothing."
    elaine "Really?"
    mc "......."
    scene ep2_126_j150 with dissolve
    elaine "Hmmm~?"
    elaine "Are you really not interested in women?"
    elaine "I mean... Are you really not interested in me?"
    elaine "Am I not beautiful~?"
    mc "......."
    scene ep2_126_j151 with dissolve
    show kiss
    $ renpy.pause(7, hard=True)
    scene ep2_126_j152
    hide kiss
    u "......"
    scene ep2_126_j153 with dissolve
    elaine "*Kissing*...Mmmm...."
    s "[elaine] keeps kissing you while putting her tongue inside of your mouth."
    s "You can taste how sweet her tongue is once both of your tongues start touching each other."
    s "She keeps kissing you for almost a full minute."
    $ renpy.pause()
    scene ep2_126_j154 with dissolve
    elaine "If you aren't really interested in women, why didn't you push me away?"
    elaine "Hmmm?....."
    mc "......."
    u "....She's right. Why didn't I push her away?"
    scene ep2_126_j155 with dissolve
    elaine "Well... Well... Well..."
    elaine "Look who've we got down there...."
    elaine "You're having an erection, aren't you?"
    scene ep2_126_j156 with dissolve
    elaine "Not interested in women, huh?"
    elaine "How are you going to explain this?"
    mc "...It's just a normal thing."
    mc "Men usually have an erection when sexually aroused."
    elaine "Yeah, you're right."
    elaine "So, what are you going to do now?"
    elaine "*Giggles*...Do you need help?"
    if _in_replay:
        jump elainehjreplay
    menu:
        "Stay quiet [elaine2]":
            mc "........"
            elaine "Still don't answer me, hm?"
            elaine "Never mind. I'll take it as a yes then!"
            scene ep2_126_j157 with dissolve
            elaine "Wow...."
            elaine "I must say that you've got such a very good cock."
            elaine "It's better than the other ones I used to see."
            elaine "Look at the size and length..."
            elaine "Wait...Actually, I think that you're the best!"
            scene ep2_126_j158 with dissolve
            elaine "*Giggles*...Hey, look at my boobs."
            mc "........"
            elaine "Do you like them?..."
            elaine "It's actually unfair for you to be naked alone."
            elaine "So, I took my top off, hehe!"
            elaine "Alright, I'm gonna start jerking you off now."
            show stand_hj1 with dissolve
            elaine "How do you feel, hmmm?"
            elaine "Do you like my hand?"
            elaine "All the guys I gave them a handjob, nobody could last longer than two minutes!"
            elaine "I wonder how long you can last...."
            $ renpy.pause()
            hide stand_hj1
            scene ep2_126_j159 with dissolve
            elaine "Well......"
            elaine "I think I underestimated you a little bit..."
            elaine "Let's do it faster!"
            show stand_hj2 with dissolve
            mc "....A...h..."
            elaine "Hmm~? Did you just moan?"
            elaine "So, you aren't completely emotionless, huh?"
            mc ".....No, I didn't moan."
            elaine "*Giggles*...You liar..."
            elaine "You know... It's fine to moan if you feel good, okay?"
            $ renpy.pause()
            elaine "You can still hold it?"
            elaine "Impressive..."
            hide stand_hj2
            scene ep2_126_j160 with dissolve
            elaine "Then, How about this?"
            show sit_hj1 with dissolve
            elaine "Well..."
            elaine "I want to make it clear, just in case you're misunderstanding me."
            elaine "I don't do this to every guy I meet, okay?"
            elaine "*Giggles*...You're the exception, hehe..."
            $ renpy.pause()
            hide sit_hj1
            scene ep2_126_j161 with dissolve
            show sit_hj2 with dissolve
            elaine "...You're about too cum, right?"
            mc "*Softly breaths*....How do you know that?"
            elaine "It's because your cock is getting hotter, and hotter."
            elaine "As if it's going to explode in my hand, hehe..."
            $ renpy.pause()
            menu:
                "Standing handjob":
                    hide sit_hj2
                    jump standhjslow
                "Slower":
                    hide sit_hj2
                    jump sithjslow
                "Cum":
                    jump sithjcum
        "Push her away [elaine1]":
            scene ep2_126_j156_n1 with dissolve
            mc "No, I don't want your help."
            elaine "Hehh?...Are you sure?"
            mc "Yeah. Just leave it like that."
            mc "It'll eventually get down by itself."
            scene ep2_126_j156_n2 with dissolve
            elaine "(Well...)"
            elaine "(No one has ever refused me before...)"
            elaine "(I'm getting even more interested in him now...)"
            scene ep2_126_j156_n3 with dissolve
            mc "......"
            elaine "What?"
            mc "Why are you still following me?"
            elaine "*Giggles*...Since when've I been following you?"
            elaine "I'm just going to get some water for the rest of us!"
            mc "Okay then..."
            $ renpy.end_replay()
            $ refuseeliane = True
            $ eliane_ch1_ep2 += 1
            $ eliane_relationship += 1
            jump endofthetrip
label elainehjreplay:
    mc "........"
    elaine "Still don't answer me, hm?"
    elaine "Never mind. I'll take it as a yes then!"
    scene ep2_126_j157 with dissolve
    elaine "Wow...."
    elaine "I must say that you've got such a very good cock."
    elaine "It's better than the other ones I used to see."
    elaine "Look at the size and length..."
    elaine "Wait...Actually, I think that you're the best!"
    scene ep2_126_j158 with dissolve
    elaine "*Giggles*...Hey, look at my boobs."
    mc "........"
    elaine "Do you like them?..."
    elaine "It's actually unfair for you to be naked alone."
    elaine "So, I took my top off, hehe!"
    elaine "Alright, I'm gonna start jerking you off now."
    show stand_hj1 with dissolve
    elaine "How do you feel, hmmm?"
    elaine "Do you like my hand?"
    elaine "All the guys I gave them a handjob, nobody could last longer than two minutes!"
    elaine "I wonder how long you can last...."
    $ renpy.pause()
    hide stand_hj1
    scene ep2_126_j159 with dissolve
    elaine "Well......"
    elaine "I think I underestimated you a little bit..."
    elaine "Let's do it faster!"
    show stand_hj2 with dissolve
    mc "....A...h..."
    elaine "Hmm~? Did you just moan?"
    elaine "So, you aren't completely emotionless, huh?"
    mc ".....No, I didn't moan."
    elaine "*Giggles*...You liar..."
    elaine "You know... It's fine to moan if you feel good, okay?"
    $ renpy.pause()
    elaine "You can still hold it?"
    elaine "Impressive..."
    hide stand_hj2
    scene ep2_126_j160 with dissolve
    elaine "Then, How about this?"
    show sit_hj1 with dissolve
    elaine "Well..."
    elaine "I want to make it clear, just in case you're misunderstanding me."
    elaine "I don't do this to every guy I meet, okay?"
    elaine "*Giggles*...You're the exception, hehe..."
    $ renpy.pause()
    hide sit_hj1
    scene ep2_126_j161 with dissolve
    show sit_hj2 with dissolve
    elaine "...You're about too cum, right?"
    mc "*Softly breaths*....How do you know that?"
    elaine "It's because your cock is getting hotter, and hotter."
    elaine "As if it's going to explode in my hand, hehe..."
    $ renpy.pause()
    menu:
        "Standing handjob":
            hide sit_hj2
            jump standhjslow
        "Slower":
            hide sit_hj2
            jump sithjslow
        "Cum":
            jump sithjcum
label standhjslow:
    scene black with dissolve
    scene ep2_126_j158 with dissolve
    show stand_hj1 with dissolve
    $ renpy.pause()
    menu:
        "Sitting handjob":
            hide stand_hj1
            jump sithjslow
        "Faster":
            hide stand_hj1
            jump standhjfast
label standhjfast:
    scene black with dissolve
    scene ep2_126_j159 with dissolve
    show stand_hj2 with dissolve
    $ renpy.pause()
    menu:
        "Sitting handjob":
            hide stand_hj2
            jump sithjslow
        "Slower":
            hide stand_hj2
            jump standhjslow
label sithjslow:
    scene black with dissolve
    scene ep2_126_j160 with dissolve
    show sit_hj1 with dissolve
    $ renpy.pause()
    menu:
        "Standing handjob":
            hide sit_hj1
            jump standhjslow
        "Faster":
            hide sit_hj1
            jump sithjfast
label sithjfast:
    scene black with dissolve
    scene ep2_126_j161 with dissolve
    show sit_hj2 with dissolve
    $ renpy.pause()
    menu:
        "Standing handjob":
            hide sit_hj2
            jump standhjslow
        "Slower":
            hide sit_hj2
            jump sithjslow
        "Cum":
            jump sithjcum
label sithjcum:
    mc "......."
    mc "....I'm about to cum."
    elaine "Yeah?"
    scene black with dissolve
    hide sit_hj2
    scene ep2_126_j162 with dissolve
    elaine "Don't cum just yet."
    elaine "Hold it for a little bit longer."
    mc "......."
    scene ep2_126_j163 with dissolve
    elaine "Okay! You can cum now~!"
    scene ep2_126_j164 with dissolve
    mc "*Softly breaths*...!!"
    elaine "Wow! You're cumming a lot!"
    elaine "You make me wonder, when was the last time you got off..."
    scene ep2_126_j165 with dissolve
    elaine "Aw..."
    elaine "My face is covered by all of your semen..."
    elaine "I wonder if it tastes good..."
    mc "Are you going to...?"
    scene ep2_126_j166 with dissolve
    elaine "*Swallows*...Mmmm..."
    elaine "Not bad... I like it."
    mc "......"
    elaine "Alright, I think that's it for now."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_126_j167 with dissolve
    elaine "Hey, come with me!"
    elaine "Let's go and get some water for the rest of us!"
    mc "...Okay, but don't hold my arm like that."
    elaine "Why? What's the problem?"
    elaine "*Giggles*...I've already touched your dick!"
    mc "....Fine."
    $ renpy.end_replay()
    $ elianehj = True
    $ eliane_ch1_ep2 += 2
    $ eliane_relationship += 2
    jump endofthetrip
label endofthetrip:
    scene black with dissolve
    $ renpy.pause()
    scene ep2_126_j168 with dissolve
    elaine "We're back, guys!"
    zeke "Oh!"
    scene ep2_126_j169 with dissolve
    elaine "Here you are, [yui]."
    elaine "Take this water bottle."
    yui "Thank you."
    elaine "No worries."
    rin "Thanks, [mc]."
    mc "You're welcome."
    scene black with dissolve
    s "*Ten minutes later*...."
    scene ep2_126_j170 with dissolve
    ben "Come on, guys!"
    ben "Let's play one more match!"
    ethan "But, we'll have to draw straws again, okay?"
    elaine "I'm okay with that."
    scene ep2_126_j171 with dissolve
    rin "Hurry up, [yui]!"
    rin "We don't have much time left. It's almost evening."
    yui "O-Okay! I'm coming!"
    elaine "[wendy]! Come here!"
    wendy "No. I'm already tired."
    wendy "I'll just stay here reading the book."
    wendy "Please go ahead without me."
    scene ep2_126_j173 with dissolve
    elaine "We'll be lacking of people then..."
    elaine "It's going to be 4 vs 3."
    scene ep2_126_j172 with dissolve
    mc "Don't worry about that."
    mc "I'm also not going to play."
    scene ep2_126_j173 with dissolve
    elaine "Okay..."
    elaine "Then, it's 3 vs 3 match."
    ethan "You made a right choice, man!"
    ethan "You're too good. We can't compete with you if you play!"
    mc "......"
    scene ep2_126_j174 with dissolve
    u "I've spent a lot of energy for today."
    u "I'm feeling a little bit tired..."
    u "Let's take a seat. Then, rest for a bit."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_126_j175 with dissolve
    mc "......."
    wendy "......."
    s "Even though you guys are alone together, no one starts the conversation."
    s "[wendy] just keeps reading her book while you're trying to take a nap."
    s "But just a few seconds before you fall a sleep..."
    scene ep2_126_j176 with dissolve
    wendy "......."
    wendy "You did it with [elaine], right?"
    mc "........"
    scene ep2_126_j177 with dissolve
    mc "....What?"
    scene ep2_126_j176 with dissolve
    wendy "I asked if you did it with [elaine]."
    wendy "And I think you know what I mean."
    scene ep2_150 with dissolve
    mc "Why do you want to know?"
    wendy "So, you did it with her."
    if elianehj == True:
        mc "Yes, I did."
    elif refuseeliane == True:
        mc "No, I didn't."
    scene ep2_151 with dissolve
    if elianehj == True:
        wendy "So, you're one of them."
        wendy "That's pretty predictable. Not surprised at all."
        mc "One of them? What do you mean?"
        wendy "One of the guys who have never refused to do something like that with her."
        mc "......"
        wendy "She's always been the one rejecting others."
        wendy "I really wish to see someone who doesn't fall for her."
    elif refuseeliane == True:
        wendy "Really?"
        mc "Yes."
        wendy "I must say that I didn't expect to hear that answer."
        wendy "So, you're the first person I guess."
        mc "First person for what?"
        wendy "For denying her. You know... Nobody has never refused to do something like that with her before."
        wendy "She's always been the ones rejecting others."
    scene ep2_150 with dissolve
    mc "Why are you telling me this?"
    wendy "It's because I'm worrying about you."
    mc "You're worrying about me?"
    wendy "Yes. She's a playgirl."
    wendy "You can have fun with her, but you must not fall for her."
    wendy "Otherwise, you're only going to get yourself hurt."
    mc "Why's that?"
    scene ep2_151 with dissolve
    wendy "It's like you're playing with fire."
    wendy "She'd disappear from your life if she found out that you have feelings for her."
    mc "......."
    mc "Aren't you her friend?"
    mc "Why are you talking so bad about her."
    scene ep2_150 with dissolve
    wendy "Of course, I'm her friend."
    wendy "But, I'm not talking bad about her behind her back."
    wendy "It's the truth. She's always been like that."
    mc "......."
    wendy "However, don't misunderstand her."
    wendy "She's a really good person. I like her."
    scene ep2_151 with dissolve
    wendy "She's someone who can be a really good friend."
    wendy "But not a good girlfriend because of her personality for now. She still likes to flirt around."
    wendy "She's interested in you now, but she'd throw you away if she became bored of you."
    wendy "That's all I want to say. It's your choice now."
    menu:
        "Thanks for warning [wendy1]":
            scene ep2_150 with dissolve
            mc "Even though I don't think I'll fall for her..."
            mc "Thanks for warning."
            wendy "You're welcome."
            $ wendywarning = 1
            $ wendy_ch1_ep2 += 1
            $ wendy_relationship += 1
        "You're exaggerating":
            scene ep2_150 with dissolve
            mc "...You're exaggerating."
            wendy "......."
            mc "I don't want to judge her by hearing that from you."
            wendy "Whatever...."
            wendy "It's none of my business anymore. I already warned you."
            $ wendywarning = 2
    scene black with dissolve
    $ renpy.pause()
    scene ep2_152 with fade
    elaine "Alright, guys! It's time to say goodbye."
    elaine "It was pretty much fun today!"
    zeke "I couldn't agree more!"
    ben "Yeah, let's hang out again in the future!"
    scene ep2_153 with dissolve
    ethan "*Ahem*...[rin]..."
    ethan "Can we talk?"
    scene ep2_154 with dissolve
    rin "Hm?"
    rin "What do you want to talk about, [ethan]?"
    scene ep2_155 with dissolve
    ethan "You know... I'm really happy to meet you."
    ethan "You're really beautiful, and lovely."
    rin "Er.... Thanks."
    ethan "I think I like you."
    ethan "I want to go out with you."
    ethan "Can I have your phone number, please?"
    scene ep2_156 with dissolve
    rin "Err... I'm sorry to say this..."
    rin "But I don't want to give you my phone number."
    ethan "Come on... Don't be like that."
    ethan "You're single, aren't you?"
    ethan "At least give me a chance. I'm sure that I can make you love me."
    rin "Err..."
    scene ep2_157 with dissolve
    rin "No, I'm not single. He is my boyfriend."
    mc "...What?"
    ethan "Really? Are you guys really dating?"
    rin "*Whispers*...[mc]. Please, help me."
    mc "*Sigh*...Yeah, we're dating."
    yui "(Hehh... That's pretty funny to see [mc] play along.)"
    scene ep2_158 with dissolve
    ethan "Err...I'm sorry, man."
    ethan "I didn't know she's your girlfriend."
    mc "It's alright."
    rin "Then, we're leaving. Please, excuse us."
    ethan "Sure..."
    scene ep2_159 with dissolve
    zeke "*Whispers*...Heh... Are you guys really dating!?"
    zeke "*Whispers*...So, you secretly have feelings for [mc], hm?"
    zeke "*Whispers*...You know... You could just use me instead of him."
    rin "*Whispers*...Shut up, [zeke]!"
    zeke "*Whispers*...Hahaha..."
    mc "......."
    scene ep2_160 with dissolve
    ethan "Err... Can I have your phone number, [elaine]?"
    elaine "Hmm? So you want my number because [rin] didn't give you hers?"
    ethan "Hehe... Yeah."
    ben "Actually, I think you should really give us your number so that we can invite you to hang out next time!"
    ethan "Yeah, he's right. How could we meet again if none of you gave us your number?"
    elaine "*Giggles*...Okay. Hand me your phone."
    ethan "Sure!"
    scene ep2_161 with dissolve
    s "While [elaine]'s typing her phone number, [wendy] notices there's something wrong."
    wendy "(Hm?... Whose phone number is she typing?)"
    wendy "(That is neither her phone number nor mine.)"
    elaine "Okay, here you are."
    scene ep2_162 with dissolve
    elaine "Alright, I think we should leave before it's getting darker."
    ben "I think so. We're going to leave soon, too."
    elaine "See you later then."
    ethan "See you!"
    scene ep2_163 with dissolve
    wendy "....."
    elaine "Stop looking at me like that. What do you want to say?"
    wendy "You didn't give them your number. Whose phone number was it?"
    elaine "I don't know. I made it up."
    wendy "Hm? Why? You've never done this."
    elaine "Well...no matter how much I love to flirt around, I'm not going to hang out with losers like them."
    wendy "Losers?"
    elaine "Don't you think so?"
    elaine "They didn't even call me to check if I really gave them my number."
    wendy "Well, you're right."
    elaine "Moreover, there was nothing special about them."
    elaine "They're just dudes trying their luck to get girls."
    elaine "[ben] might be better than the another one, but still... I'm not interested in them at all."
    elaine "{size=-15}Perhaps it's because I've already found someone really interesting....{/size}"
    wendy "Hm? What did you say?"
    elaine "*Giggles*...Nothing!"
    scene black with dissolve
    $ renpy.pause()
    scene ep2_164 with fade
    elaine "Hm? I thought you guys already left."
    elaine "Why are you guys still here?"
    scene ep2_165 with dissolve
    rin "Well, we want to ask if you want to stop by our house."
    rin "Let's hang out for a bit. Maybe we can have a party, too!"
    zeke "That sounds fun to me! What do you guys think!?"
    scene ep2_166 with dissolve
    elaine "I'm really pleased to go with you guys."
    wendy "Yeah, it's been a while since we visited you guys there."
    zeke "Then, what are you waiting for? Let's go!"
    elaine "Usually, there's no way I would say no to having a party."
    elaine "But..."
    scene ep2_167 with dissolve
    elaine "I think I have to say no today since we still have some works to finish."
    wendy "Yeah..."
    elaine "Actually, we thought about coming here for only one or two hours to relax, then leave."
    elaine "But, it turned out that we stayed here longer than we expected too."
    rin "It's alright. Just visit us next time when you guys aren't busy."
    wendy "We surely will."
    $ yui_ch1_ep2_1 += 1
    $ rin_ch1_ep2 += 1
    $ zeke_ch1_ep2 += 1
    $ yui_relationship += 1
    $ rin_relationship += 1
    $ zeke_relationship += 1
    scene black with dissolve
    s "You've gained 1 relationship point with [yui]!"
    s "You've gained 1 relationship point with [rin]!"
    s "You've gained 1 relationship point with [zeke]!"
    s "*One hour later*...."
    play music "sfx/ep2_1.mp3" fadein 3.0
    $ bgm = "Vendredi - Te Amo"
    #-------------music here-------------#
    scene ep2_168 with fade
    zeke "Alright, guys! We've arrived home!"
    rin "*Yawns*...That was fast..."
    yui "Ugh...I feel so sticky. I can't wait to take a bath..."
    scene ep2_169 with dissolve
    zeke "Wait a sec, guys!"
    scene ep2_170 with dissolve
    rin "Hm? Is there something you want to say?"
    zeke "Let's clean ourselves up, then have dinner together!"
    scene ep2_171 with dissolve
    rin "Umm..."
    rin "I thought about having dinner at first when I invited [elaine] and Wendy to come over."
    rin "But to think about it again..."
    scene ep2_172 with dissolve
    rin "It's weird that I should be hungry right now after spending all of that energy today, but I'm not really hungry right now."
    rin "So, I think I'm not going to have dinner today."
    yui "Me, too. I'm on a diet now."
    zeke "What!?"
    zeke "You're already slim! Why are you on diet?"
    zeke "*Sigh*...What about you, [mc]?"
    mc "I'll take a bath first. Then, go to the kitchen to find something to eat."
    zeke "Okay. Then, find me when you're ready. I'll be waiting here."
    mc "Okay."
    scene ep2_173 with fade
    u "I feel so sticky..."
    u "Let's take a bath..."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_174 with dissolve
    u "*Sigh*...I feel a lot better after cleaning myself up."
    u "Let's go to have dinner."
    $ backhome = True
    $ newmessage = True
    $ sally_messages_show = True
    $ sally_newmessage = True
    $ phone_alert = True
    $ area = "mcroom"
    jump house_ep2
label house_ep2:
    if ep2hiddenimages_count == 7:
        $ ep2hiddenimages = True
    if area == "hallway":
        if reply_sally1 == False:
            s "I should reply the message first!"
            jump house_ep2
        elif reply_sally1 == True:
            jump dinnerwithzeke
    if area == "rinroom" and ep2rinroom == False:
        jump ep2rinroom
    if rin_like2 == "Movies" and rin_like3 == "Games" and rin_hate2 == "Liars" and rin_hate3 == "Bad people" and rinpathead == True:
        $ ep2rintalk = True
    if yui_like1 == "Success" and yui_hate1 == "Being insulted" and yuihair == True and yui_contact == True:
        $ ep2yuitalk = True
    if area == "yuiroom" and ep2yuiroom == False:
        jump ep2yuiroom
    call screen ep2house
label dinnerwithzeke:
    #-----------Music here-----------#
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    scene black
    $ renpy.pause()
    scene ep2_175 with fade
    u "Let's go find [zeke]."
    scene ep2_176 with dissolve
    u "Where did Zeke go?"
    zeke "[mc]!"
    scene ep2_177 with dissolve
    zeke "Come here!"
    scene ep2_178 with dissolve
    zeke "Have you ever played this?"
    mc "No. What's that?"
    zeke "It's called foosball."
    zeke "I'm telling you. I'm really good at this game!"
    zeke "I've never lost to anybody in the house!"
    scene ep2_179 with dissolve
    mc "Congrats..."
    zeke "Hehe... Thanks."
    zeke "Well... You're really lucky today!"
    mc "Hm? Lucky?"
    zeke "Yeah! I'm giving you a chance to compete with me!"
    mc "Er..... Thanks."
    mc "But I don't want to. I'd rather go find something to eat."
    zeke "Come on! Don't be like that!"
    zeke "Let's play a couple more games before we eat dinner!"
    mc "......"
    menu:
        "Okay [zeke1]":
            scene ep2_179_a1 with dissolve
            $ foosball = 1
            $ zeke_ch1_ep2 += 1
            $ zeke_relationship += 1
            mc "*Sigh*...Just a couple games, okay?"
            zeke "Yes! That's my boy!"
            mc "So... How do we play?"
            scene ep2_179_a2 with dissolve
            zeke "It's really simple! It's just like a real football."
            zeke "You need to score goals to win the game."
            zeke "You see those bars, right?"
            mc "Yeah."
            zeke "There are four bars on each side of the table."
            zeke "You'll have two bars in your defensive zone, one bar in your midfield zone, and another one in your striker zone."
            zeke "You just need to control those bars to prevent the ball from going in your goal, and trying to score a goal."
            mc "......."
            scene ep2_179_a3 with dissolve
            zeke "Well, I think we better start playing."
            zeke "I'm sure that you can learn during the game."
            mc "Okay."
            scene ep2_179_a4 with dissolve
            zeke "I just want to let you know this before we start playing..."
            mc "Know what?"
            zeke "I'm not going to go easy on you even though you're my friend!"
            zeke "Be ready!"
            mc "......"
            zeke "Take that!"
            scene ep2_179_a5 with dissolve
            zeke "Hehhh... What are you doing man?"
            zeke "You'll never score against me if you keep playing like that!"
            mc "We'll see..."
            scene ep2_179_a4 with dissolve
            zeke "I'm so sorry, but I'm going to take the lead!"
            mc "There is no way..."
            zeke "Watch out! Watch out! Watch out!"
            scene ep2_179_a6 with dissolve
            zeke "Eat that!"
            mc "Ugh!...."
            scene ep2_179_a7 with dissolve
            zeke "Yes! I scored a goal!!"
            zeke "Hahahaha! What did I tell you!?"
            zeke "What did I fucking tell you!?"
            mc "......"
            zeke "I'm the best!"
            scene ep2_179_a8 with dissolve
            zeke "Hahaha! I've finally found something you aren't good at!"
            mc "This is my first time playing it, okay?"
            zeke "Yeah... Yeah... I know."
            zeke "However, I don't think you'll be able to beat me anytime soon."
            scene ep2_179_a9 with dissolve
            mc "Tsk...."
            mc "Are you really gonna keep bragging? Or are you going to play?"
            zeke "......"
            scene ep2_179_a10 with dissolve
            zeke "......."
            mc "What?"
            scene ep2_179_a11 with dissolve
            zeke "......"
            scene ep2_179_a10 with dissolve
            zeke "I can't believe my eyes..."
            zeke "I can't believe that I'm witnessing you showing your emotion!"
            mc "......."
            zeke "This is the first time ever! I thought you were completely emotionless."
            mc "Shut up! I'm going to beat you badly."
            zeke "Ha! Seems like someone hates losing, hm?"
            zeke "Come on! Show me how you are going to do that!"
            scene black with dissolve
            s "*A few moments later*......"
            scene ep2_179_a12 with dissolve
            zeke "No! No! No!"
            zeke "This can't be happening....!"
            zeke "How can you play so much better in such a very shot time like this!?"
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep2_179_a13 with dissolve
            mc "That's 1-1"
            zeke "Ugh!..."
            zeke "...There is no way I'm going to lose!"
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep2_179_a14 with dissolve
            mc "Now, I'm leading."
            zeke "Damn it!"
            zeke "Am I dreaming right now!?"
            zeke "I can't believe this is really happening!"
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep2_179_a15 with dissolve
            mc "Another one."
            zeke "Fuck!..."
            zeke "Come on, [zeke]! You can do it! You can still bounce back!"
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep2_179_a6 with dissolve
            zeke "Yes! That's what I'm talking about!"
            mc "Don't be too happy. I'm still leading."
            zeke "You'll never know that...!"
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep2_179_a13 with dissolve
            mc "That's it. I won."
            zeke "Ugh!..."
            mc "Well played."
            scene ep2_179_a16 with dissolve
            zeke "No! I don't accept it!"
            zeke "You lied to me, right?"
            zeke "There is no way this is your first time playing foosball."
            mc "*Sigh*...It's really my first time...."
            zeke "I don't b-"
            mc "I'm just a fast learner, okay?"
            zeke "Let's play one more game! I'm going to win it!"
            mc "*Sigh*....Okay."
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep2_179_a13 with dissolve
            zeke "Ugh!..."
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep2_179_a14 with dissolve
            zeke "Ouch!..."
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep2_179_a15 with dissolve
            zeke "No!...."
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene black with dissolve
            s "*A few moments later*...."
            scene ep2_179_a17 with dissolve
            zeke "Ugh...I lost again..."
            zeke "I'm such a loser..."
            mc "Hey, it's just a game..."
            zeke "You don't get it...."
            zeke "It's the only thing I thought I was better at than you..."
            zeke "I shouldn't have invited you to play in the first place..."
            mc "......."
            zeke "*Sigh*...I'm sorry. I shouldn't have said that."
            mc "It's alright."
            zeke "...Don't mind me. I'll get better soon."
            zeke "Let's go find something to eat."
            mc "Okay."
            jump dinnerwithzeke2
        "No, thanks":
            scene ep2_179_r1 with dissolve
            $ foosball = 2
            mc "No, I don't want to play. I'm hungry now."
            zeke "Come on, man...."
            mc "....."
            zeke "*Sigh*...Okay. Let's go to the kitchen."
            jump dinnerwithzeke2
label dinnerwithzeke2:
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep2_179_a18 with fade
    zeke "Ahh... This smell..."
    zeke "Damn... It looks so yummy."
    zeke "I can't wait to taste it."
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep2_179_a19 with dissolve
    rin "*Hums*......"
    rin "(Let's grab a beer~)"
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep2_179_a20 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a20.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a20_blink.jpg", 1) with dissolve
    mc "Don't we have something else to eat than these cup noodles?"
    zeke "I don't think so, why?"
    zeke "You don't like to eat cup noodles?"
    zeke "Should we order out?"
    scene ep2_179_a22 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a22.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a22_blink.jpg", 1) with dissolve
    mc "No, it's okay."
    mc "I'm just wondering what you would eat if [rin] didn't cook."
    scene ep2_179_a20 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a20.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a20_blink.jpg", 1) with dissolve
    zeke "I usually order out, but I feel like having a cup of noodles today"
    zeke "So..."
    mc "I see...."
    scene ep2_179_a23 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a23.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a23_blink.jpg", 1) with dissolve
    zeke "By the way..."
    zeke "Since we were talking about [rin], what do you think of her?"
    mc "What do you mean?"
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep2_179_a21 with dissolve
    rin "(*Sigh*...[zeke]. I can't believe you.)"
    rin "(Why are you asking him such a question?)"
    rin "(Should I go in and let them know my presence?)"
    rin "(........)"
    rin "(But, I kind of want to hear [mc]'s answer though...)"
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep2_179_a23 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a23.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a23_blink.jpg", 1) with dissolve
    zeke "I mean...She's a very nice girl..."
    zeke "She's also very beautiful."
    zeke "She's a woman many guys would kill to get a chance to date her"
    zeke "For example, that guy we met today."
    zeke "However, I'm not going to give her to those guys because I don't think they're good enough for her."
    zeke "But, I'd be okay if it was you..."
    zeke "What do you think?"
    menu:
        "Agree [rin1][smec] & [zeke1]":
            scene ep2_179_a24 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a24.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a24_blink.jpg", 1) with dissolve
            mc "Yes, you're right."
            mc "She's a very beautiful, and a very nice woman."
            mc "I also feel comfortable everytime I'm around her."
            scene ep2_179_a25 with dissolve
            zeke "Then, what are you waiting for?"
            zeke "Just ask her out!"
            zeke "I'm sure that she also has some feelings for you, too!"
            scene ep2_179_a24 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a24.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a24_blink.jpg", 1) with dissolve
            mc "......"
            u "...I don't know what to say."
            u "For the circumstances I've been living through, I've never thought about having a deep relationship with someone."
            u "Because everyone is going to leave in the end anyway..."
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep2_179_a26 with dissolve
            rin "([mc] just said that I'm beautiful...)"
            rin "(I already knew it though, because I've been told that I'm beautiful so many times.)"
            rin "(But, to hear that coming from [mc]....)"
            rin "(Aw.... My heart is beating so hard...)"
            $ agreezeke = 1
            $ zeke_ch1_ep2 += 2
            $ zeke_relationship += 2
            $ rin_ch1_ep2 += 2
            $ rin_relationship += 2
            jump afterdinner
        "I'm not interested":
            scene ep2_179_a24 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a24.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a24_blink.jpg", 1) with dissolve
            mc "I don't know."
            mc "I feel comfortable everytimes when being with her."
            mc "But, I'm not interested in dating her."
            scene ep2_179_a25_r with dissolve
            zeke "Oh?..."
            zeke "But why?"
            zeke "Is she not good enough for you?"
            scene ep2_179_a24 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a24.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a24_blink.jpg", 1) with dissolve
            mc "Yes, she is."
            mc "Actually, she is too good for me."
            mc "So, I'm not going to ask her out on a date."
            u "To be honest, I can't do it. I'm not allowed to do it...."
            scene black with dissolve
            $ renpy.pause(0.2,hard=True)
            scene ep2_179_a26_1 with dissolve
            rin "......."
            rin "(Why am I so sad after hearing what he said...?)"
            rin "(Does it mean that I wish he was going to ask me out?)"
            rin "(I should leave....)"
            $ agreezeke = 2
            jump afterdinner
label afterdinner:
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep2_179_a27 with fade
    zeke "Arrr... I'm so full~"
    zeke "I can't eat anymore!"
    scene ep2_179_a28 with dissolve
    zeke "Hm? Are you going to leave already?"
    mc "Yes, why?"
    zeke "Why don't you stay here for a bit longer?"
    zeke "I wanna talk to you some more."
    scene ep2_179_a29 with dissolve
    $ renpy.sound.play("sfx/doorbell.mp3")
    s "*Doorbell rings*....."
    zeke "Hm? We've got a guest?"
    zeke "Who's coming here at this time?"
    zeke "Did you invite someone here?"
    mc "No, I didn't."
    scene ep2_179_a30 with dissolve
    zeke "Dude, can you do the clean up for me?"
    zeke "I'm going to open the door."
    mc "Okay."
    zeke "Cheers, man."
    scene ep2_179_a31 with dissolve
    $ renpy.pause()
    scene ep2_179_a32 with dissolve
    $ renpy.sound.play("sfx/doorbell.mp3")
    s "*Doorbell rings*....."
    zeke "Wait a sec! I'm coming!"
    scene black with dissolve
    $ renpy.sound.play("sfx/Door opening.mp3")
    zeke "Who's th-?"
    $ renpy.sound.play("sfx/Door closing.mp3")
    scene ep2_179_a33 with dissolve
    zeke "!!!!"
    zeke "[mika]?"
    mika "*Hics*...[zeke]...."
    scene ep2_179_a34 with dissolve
    zeke "What's happening? Who hurt you?"
    mika "*Hics*...I...I..."
    zeke "Please, don't cry."
    zeke "It really hurts me to see you cry."
    zeke "Relax. Take a deep breath."
    mika "*Hics*....."
    scene ep2_179_a35 with dissolve
    mika "...Can I...sleep over here tonight?"
    zeke "....Of course, you can if that's what you want."
    zeke "Come here. Follow me."
    mika "*Hics*...Thank you."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_179_a36 with dissolve
    zeke "Here. Take this handkerchief."
    zeke "You'll need it to wipe away your tears."
    mika "Thank you..."
    scene ep2_179_a37 with dissolve
    mika "....Do you have beers?"
    mika "*Hics*...I want to get drunk so that I can forget... What I just saw...."
    zeke "Er... Sure."
    zeke "I'll go grab them for you."
    scene ep2_179_a38 with dissolve
    zeke "(I wonder what she saw....)"
    zeke "(She's never been like this before.)"
    zeke "(I'm really worried about her...)"
    zeke "(I'm going to take care of her tonight.)"
    scene ep2_179_a39 with dissolve
    mc "What's going on?"
    zeke "Oh... That's my friend, [mika]."
    scene ep2_179_a40 with dissolve
    zeke "She's kind of... Sad now."
    mc "I see..."
    zeke "Are you going back to your room?"
    scene ep2_179_a39 with dissolve
    mc "Yeah."
    zeke "Okay. See you tomorrow."
    mc "See you."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_179_a41 with dissolve
    $ renpy.pause()
    scene ep2_179_a42 with dissolve
    u "Hm?..."
    u "That's [rin]."
    u "What's she doing in front of [yui]'s room?"
    scene ep2_179_a43 with dissolve
    $ renpy.pause()
    scene ep2_179_a44 with dissolve
    rin "[mc]!?"
    mc "Yes, it's me..."
    scene ep2_179_a45 with dissolve
    mc "Why are you so shocked to see me?"
    rin "You came out of no where. How can I not be shocked?"
    rin "At least you should've said something so that I knew you were behind me."
    mc "I'm sorry."
    if agreezeke == 1:
        scene ep2_179_a46 with dissolve
        rin "It's alright..."
        rin "You don't have to be sorry..."
        rin "(Aw...I can't stop thinking about what he said to [zeke]...)"
        scene ep2_179_a47 with dissolve
        mc "Do you have a fever? Your face looks red."
        rin "N-No, I'm fine!"
        mc "Okay."
        mc "Anyway, what are you doing here?"
        scene ep2_179_a48 with dissolve
        rin "Oh! I came here to ask [yui] if she wanted to watch TV with me."
        rin "But, she told me that she has to work."
        mc "I see..."
        rin "By the way, I heard the doorbell ringing."
        rin "Do we have a guest now?"
        scene ep2_179_a49 with dissolve
        mc "It's [zeke]'s friend."
        rin "[mika]?"
        mc "Yes, it's her."
        rin "Why is she here?"
        mc "I don't know. She seemed to be crying."
        mc "[zeke]'s probably taking care of her now."
        mc "And I don't think you can watch the TV now since they are down there."
        scene ep2_179_a50 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a50.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a50_blink.jpg", 1) with dissolve
        rin "Is that so...?"
        mc "Yeah."
        rin "Poor me...."
        rin "I wish I had a TV in my bedroom."
        rin "I really want to watch some series before going to bed...."
        menu:
            "I have one in my room [rin1]":
                $ inviterin = 1
                $ rin_ch1_ep2 += 1
                $ rin_relationship += 1
                u "That's a pretty good idea..."
                mc "There's a TV in my room, but it's not as large as the one in the hallway."
                mc "I'm going to find something to watch as well."
                mc "Do you want to join?"
                scene ep2_179_a51 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a51.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a51_blink.jpg", 1) with dissolve
                rin "W-What!?"
                rin "What did you just say?"
                mc "Do you want to come in my room?"
                rin "......."
                mc "Seems like you d-"
                scene ep2_180 with dissolve
                rin "Yes, I do!"
                rin "*Giggles*...Let's go to your room!"
                mc "Er...Actually, you don't have to be so hasty..."
                mc "The TV isn't going to disappear..."
                rin "*Giggles*...You're funny!"
                jump withrin
            "Watch on your phone":
                $ inviterin = 2
                mc "Why don't you watch it on your phone?"
                mc "You know that there's a Netflix app on the phone, right?"
                scene ep2_179_a52 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a52.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a52_blink.jpg", 1) with dissolve
                rin "....Yeah, I know that."
                rin "But I prefer to watch the series on a TV. The screen is much more bigger than my phone."
                rin "Thanks for your suggestion though."
                rin "I'm leaving now. See you later."
                mc "Okay. See you."
                scene black with dissolve
                $ renpy.pause()
                scene ep2_218_5 with dissolve
                s "You spend your time watching a series on Netflix..."
                scene black with dissolve
                $ renpy.pause()
                jump krystalkitchen
    elif agreezeke == 2:
        scene ep2_179_a45 with dissolve
        mc "What are you doing here by the way?"
        rin "Er..."
        rin "Oh! I came here to ask [yui] if she wanted to watch a TV with me."
        rin "But, she told me that she has to work."
        mc "I see..."
        rin "By the way, I heard the doorbell ringing."
        rin "Do we have a guest now?"
        scene ep2_179_a49 with dissolve
        mc "It's [zeke]'s friend."
        rin "[mika]?"
        mc "Yes, it's her."
        rin "Why is she here?"
        mc "I don't know. She seemed to be crying."
        mc "[zeke]'s probably taking care of her now."
        mc "And I don't think you can watch the TV now since they are down there."
        scene ep2_179_a52 at eyesblink("Ch.1/Ep.2/Scenes/ep2_179_a52.jpg", "Ch.1/Ep.2/Scenes/ep2_179_a52_blink.jpg", 1) with dissolve
        rin "Is that so...?"
        mc "Yeah."
        rin "Poor me...."
        rin "I wish I had a TV in my bedroom."
        rin "I really want to watch some series before going to bed...."
        scene black with dissolve
        $ renpy.pause()
        scene ep2_218_5 with dissolve
        s "You spend your time watching a series on Netflix..."
        scene black with dissolve
        $ renpy.pause()
        jump krystalkitchen
label withrin:
    scene black with dissolve
    $ renpy.sound.play("sfx/Door opening.mp3")
    $ renpy.pause()
    $ renpy.sound.play("sfx/Door closing.mp3")
    scene ep2_181 with dissolve
    #----------Music here-----------#
    play music "sfx/ep2_3.mp3" fadein 3.0
    $ bgm = "Mike Leite - Vacaciones"
    $ renpy.pause()
    scene ep2_182 with dissolve
    mc "There it is..."
    rin "Aw... Look at that cute little thing..."
    mc "........"
    scene ep2_183 with dissolve
    rin "Oh! Please, don't get me wrong!"
    rin "I didn't mean it in a bad way."
    mc "I didn't even say anything..."
    rin "*Giggles*...I'm sorry. I was a bit overthinking..."
    scene ep2_184 with dissolve
    rin "Alright, what do you want to watch?"
    mc "Any suggestions?"
    rin "Uhmm...."
    scene ep2_185 with dissolve
    rin "Oh! I saw people talking about the series called Money Heist on social medias."
    rin "It's the story about a criminal mastermind who goes by {b}The Professor{/b} has a plan to pull off the biggest heist in recorded history."
    rin "He plans to print billions of euros in the Royal Mint of Spain with the help of his crew."
    rin "I watched the trailer, and it was very interesting."
    rin "I was also surprised to know that it has four seasons already."
    rin "I have no clue how I have never watched a single episode of it."
    scene ep2_184 with dissolve
    rin "What do you think? Should we watch it?"
    mc "That sounds interesting enough for me."
    mc "Let's watch it."
    rin "Okay!"
    scene black with dissolve
    $ renpy.pause()
    scene ep2_186 with dissolve
    s "[rin] and you start watching the series..."
    scene ep2_187 with dissolve
    mc "......."
    rin "(Look at him...)"
    rin "(I really like the way he's focusing on the series...)"
    rin "......."
    scene ep2_188 with dissolve
    rin "Don't you feel uncomfortable to sit and watch like this?"
    mc "Hm?"
    rin "I mean... There is nothing behind us."
    rin "We can't lean back to get into a more comfortable position."
    mc "You can sit on the chair if you want."
    rin "But, to think about it...."
    rin "......."
    rin "....Can I lie on your lap instead?"
    scene ep2_189 with dissolve
    rin "(Argh!...Why did I say that!?)"
    mc "Why do you want to lie on my lap?"
    rin "I-It's just... I feel comfortable when lying on your lap!"
    rin "That's it!"
    mc "........"
    scene ep2_190 with dissolve
    rin "(Ugh!...What did you just say, [rin]!?)"
    rin "(That was such a very stupid excuse...)"
    scene ep2_191 with dissolve
    rin "(There is no way he's going to....)"
    mc "Okay."
    rin "(...Let me...)"
    rin "Hm!?..."
    scene ep2_192 with dissolve
    rin "What did you just say!?"
    rin "I didn't hear it clearly. Can you say it again, please?"
    mc "You can lie on my lap if you want...."
    rin "........"
    u "Look at her facial expression..."
    u "I can tell that she didn't expect to hear what I said."
    u "Actually, even I'm a little bit surprised as well...."
    u "Why did I decide to say that?...."
    rin "Okay then...."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_193 with dissolve
    rin "(*Giggles*...I can't believe that I'm actually lying on his lap again...)"
    scene ep2_194 with dissolve
    rin "So, what do you think about the series?"
    rin "Is it good?"
    scene ep2_195 with dissolve
    mc "I think it's pretty good."
    mc "I like the way they took so many months to prepare for the heist."
    rin "Me too. It shows that they're not just normal thieves."
    mc "Yeah."
    scene ep2_196 with dissolve
    rin "!!!!"
    mc "......."
    scene ep2_197 with dissolve
    rin "Er....."
    rin "I never knew that it had a scene like this...."
    mc "..But I find it pretty normal nowadays though..."
    scene ep2_198 with dissolve
    rin "I'll be right back."
    mc "Hm? Where are you going?"
    rin "...I-I'm going to get a beer."
    rin "D-Do you want some?"
    mc "No, I don't."
    rin "Okay then."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_199 with dissolve
    rin "(*Sigh*....That was so dangerous...)"
    rin "(I know that I was being a little bit exaggerating. It's just a nude scene for a few seconds.)"
    rin "(But I've never watched nude scenes with a man before!)"
    rin "(*Sigh*...I need to clear up my mind....)"
    scene ep2_200 with dissolve
    rin "(Hm?...)"
    rin "(That's [zeke], and [mika].)"
    rin "(I wonder what they are talking about.)"
    scene ep2_201 with dissolve
    zeke "{b}YOU SAID WHAT!?{/b}"
    zeke "Where is he now?"
    zeke "I'm going to punch him in the fucking face!!"
    mika "C-Calm down, [zeke]..."
    mika "He isn't worth it."
    zeke "........"
    scene ep2_202 with dissolve
    zeke "Argh!...I'm so mad right now."
    mika "I'm sorry..."
    zeke "You don't have to!"
    zeke "It's not your fault!"
    scene ep2_203 with dissolve
    rin "What's happening, guys?"
    mika "...[rin]?"
    rin "Yep."
    rin "What's happening, [zeke]?"
    rin "Why are you so mad?"
    scene ep2_204 with dissolve
    zeke "That bastard just cheated on her!"
    zeke "Can you believe it!? How could he do that to her!?"
    rin "W-What!?"
    rin "Did he really...?"
    mika ".....Yeah."
    mika "I saw it with my own eyes..."
    rin "I'm sorry to hear that..."
    scene ep2_205 with dissolve
    zeke "Listen! You need to break up with that asshole ASAP!"
    zeke "Just go see him and yell at him in the face that you know what he did."
    mika "....I get it."
    zeke "See? I told you so many times that any girl like you deserves a better man!"
    rin "Wait. That sounds familiar...."
    scene ep2_206 with dissolve
    mika "*Giggles*...Did you just try to comfort me by saying Shawn Mendes's song lyrics?"
    rin "Right? That's why it sounds so familiar...."
    zeke "........"
    zeke "No. I changed it a little bit...."
    mika "*Giggles*....That's not how it works!"
    mika "*Giggles*....But, thanks, [zeke]. You made me feel better now."
    scene ep2_207 with dissolve
    rin "(I think there's nothing left for me to say anymore.)"
    rin "([zeke]'s doing his job very well.)"
    rin "(I can leave her with him here.)"
    scene black with dissolve
    $ renpy.pause()
    scene ep2_208 with fade
    rin "I'm back."
    mc "Welcome."
    scene ep2_209 with dissolve
    rin "Are you sure that you don't want this?"
    rin "I grabbed one for you."
    mc "No, I'm fine. Thanks."
    scene ep2_210 with dissolve
    rin "Oh, I almost forget that you're a lightweight."
    rin "So, you shouldn't drink it."
    mc "......."
    rin "Nevermind, I'm going to put it there then."
    scene ep2_211 with dissolve
    s "[rin] and you start watching the series again..."
    scene ep2_212 with dissolve
    rin "She's very beautiful...."
    mc "......"
    rin "Don't you think so?"
    mc "Hm? I don't know."
    scene ep2_213 with dissolve
    u "Well, I forgot to ask her to grab a water bottle for me."
    u "I'm kind of thirsty now..."
    u "......"
    u "....Let's just drink this beer instead."
    scene ep2_214 with dissolve
    rin "Hm?....."
    mc "I'm thirsty, and there is no water here."
    mc "So...."
    rin "*Giggles*...Relax. I didn't even say anything."
    mc "......."
    rin "Can I lie on your lap again?"
    mc "...Up to you."
    scene black with dissolve
    s "*About an hour later*....."
    scene ep2_215 with dissolve
    rin "........"
    rin "(...Here we go again...)"
    rin "(Fortunately, they aren't completely naked this time.)"
    mc "........"
    scene ep2_216 with dissolve
    rin "(...But why am I getting turned on...?)"
    rin "*Softly breathes*....."
    mc "......."
    rin "(Hm?....)"
    rin "(I can feel something pushing the back of my head...)"
    rin "(....Is he also getting turned on?)"
    scene ep2_217 with dissolve
    rin "*Softly breathes*....."
    if rin_relationship >= 13:
        rin "(...W...What are you doing, [rin]!?)"
        rin "(...Why am I doing this?)"
        rin "(...But why is he not saying anything?)"
        rin "(...Does he not know that I'm touching his thing...?)"
        rin "(...I'm already 24, but I've never seen a real one...)"
        rin "(.........)"
        scene ep2_218 with dissolve
        rin "...I want to... See it."
        rin ".....Can you show it to me, please?"
        rin "(Argh!...I can't believe that I actually said that...)"
        rin "(*Sigh*...I don't care anymore. I'm so horny right now.)"
        rin "(...I don't know what'd happen, but I'm sure that I'd be okay if I did it with him.)"
        menu:
            "Take your shorts off [rin3]":
                u "Even though I said that I'm not interested in sex, it doesn't mean that I have no feelings at all."
                u "And the sex with [yui]... That wasn't my first time..."
                u "I also get horny sometimes, too."
                u "I usually choose to ignore it, but this time..."
                mc "...Okay."
                jump rinhandjob
            "Push her away":
                scene ep2_218_r1 with dissolve
                mc "Okay. That's enough."
                rin "W-Wait! What are you doing?"
                rin "The episode isn't finished yet!"
                mc "I'm sleepy. I'm going to sleep now."
                scene black with dissolve
                $ renpy.pause()
                scene ep2_218_r2 with dissolve
                u "*Sigh*...That was close..."
                u "I almost let her do it..."
                scene ep2_218_a24 with dissolve
                u "Let's finish this episode..."
                scene black with dissolve
                $ sexwithrin = 2
                $ renpy.pause()
                jump krystalkitchen
    elif rin_relationship < 13:
        scene ep2_218_r1 with dissolve
        mc "Okay. That's enough."
        rin "W-Wait! What are you doing?"
        rin "The episode isn't finished yet!"
        mc "I'm sleepy. I'm going to sleep now."
        scene black with dissolve
        $ renpy.pause()
        scene ep2_218_r2 with dissolve
        u "*Sigh*...That was close..."
        u "I almost let her do it..."
        s "You need at least 13 relationship points with [rin] to unlock the scene."
        scene ep2_218_a24 with dissolve
        u "Let's finish this episode..."
        scene black with dissolve
        $ renpy.pause()
        jump krystalkitchen
label rinhandjob:
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
    play music "sfx/ep2_4.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - Out of Time"
    scene ep2_218_a1 with dissolve
    rin "Oh my...."
    rin "So, this is a real...dick."
    mc "......."
    rin "...Can I...touch it?"
    mc "Go ahead."
    show rin_hj1 with dissolve
    window hide
    rin "....It's really big..."
    rin "...I can barely fit my hand around it."
    $ renpy.pause()
    rin "...Do you mind if I move faster?"
    mc "No, I don't"
    scene black
    hide rin_hj1
    show rin_hj2 with dissolve
    window hide
    rin "...It feels so hot..."
    rin "How do you feel...?"
    mc "Good."
    $ renpy.pause()
    rin "Are you about to cum?"
    mc "No. You need to put more effort in."
    scene black
    hide rin_hj2
    show rin_hj3 with dissolve
    window hide
    rin "Then, how about this?"
    mc "Yeah, keep moving like that."
    $ renpy.pause()
    menu:
        "Slowest":
            scene black
            hide rin_hj3
            jump rinhj1
        "Slower":
            scene black
            hide rin_hj3
            jump rinhj2
        "Next":
            jump rinfinger
label rinhj1:
    show rin_hj1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            scene black
            hide rin_hj1
            jump rinhj2
        "Fastest":
            scene black
            hide rin_hj1
            jump rinhj3
        "Next":
            jump rinfinger
label rinhj2:
    show rin_hj2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            scene black
            hide rin_hj2
            jump rinhj1
        "Faster":
            scene black
            hide rin_hj2
            jump rinhj3
        "Next":
            jump rinfinger
label rinhj3:
    show rin_hj3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slowest":
            scene black
            hide rin_hj3
            jump rinhj1
        "Slower":
            scene black
            hide rin_hj3
            jump rinhj2
        "Next":
            jump rinfinger
label rinfinger:
    scene black
    hide rin_hj3
    scene ep2_218_a5 with dissolve
    rin "...I'm so horny, too..."
    rin "...Can you help me, please?"
    mc "Okay."
    scene ep2_218_a6 with dissolve
    rin "...Are you going to finger my... Pussy?"
    mc "Yes. Why?"
    rin "......"
    scene ep2_218_a7 with dissolve
    rin "It's just... Nobody has done that to me before..."
    rin "So... Can you please be gentle?"
    mc "...Okay."
    scene ep2_218_a8 with dissolve
    rin "...This is so embarassing..."
    show rin_fin1 with dissolve
    window hide
    rin "*Softly breathes*...Mmmm..."
    rin "*Softly breathes*...It feels a bit weird having someone else's fingers touching my pussy..."
    $ renpy.pause()
    rin "*Softly breathes*...Mmmm... Faster, please."
    scene black
    hide rin_fin1
    show rin_fin2 with dissolve
    window hide
    rin "Ahhh....Ahhh...."
    mc "Your pussy is very wet...."
    rin "Mmmm... Because it feels so good."
    $ renpy.pause()
    menu:
        "Slower":
            scene black
            hide rin_fin2
            jump rinfing1
        "Next":
            scene black
            hide rin_fin2
            jump rinmis
label rinfing1:
    show rin_fin1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            scene black
            hide rin_fin1
            jump rinfing2
        "Next":
            scene black
            hide rin_fin1
            jump rinmis
label rinfing2:
    show rin_fin2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            scene black
            hide rin_fin2
            jump rinfing1
        "Next":
            scene black
            hide rin_fin2
            jump rinmis
label rinmis:
    scene ep2_218_a10 with dissolve
    rin "*Softly breathes*...S... Stop..."
    mc "Hm? Why?"
    rin "*Softly breathes*...I want you to put...{b}it{/b} in..."
    mc "Are you sure?"
    rin "*Softly breathes*...Yeah, we already went too far..."
    rin "*Softly breathes*....There is no going back now...."
    mc "Okay then."
    scene ep2_218_a11 with dissolve
    rin "Do it slowly, please..."
    mc "Tell me if it hurts."
    rin "...Sure."
    scene ep2_218_a12 with dissolve
    rin "Ugh!...."
    mc "Are you okay?"
    rin "Yeah... Don't mind me."
    scene ep2_218_a13 with dissolve
    mc "Okay then, I'm gonna start moving now."
    show rin_mis1 with dissolve
    window hide
    rin "*Softly breathes*...Mmmm...."
    mc "How do you feel?"
    rin "*Softly breathes*...Mmmm... It's so hot... And weird..."
    $ renpy.pause()
    mc "Can I move faster?"
    rin "*Softly Moans*...Ye...Yeah."
    scene black
    hide rin_mis1
    show rin_mis2 with dissolve
    window hide
    rin "*Moans*...Ahhh..."
    rin "*Moans*...Mmmm... You're so big inside me..."
    $ renpy.pause()
    mc "I'm going faster..."
    rin "*Moans*..Mmmm.... Yeah, please go faster!"
    scene black
    hide rin_mis2
    show rin_mis3 with dissolve
    window hide
    rin "*Heavily moans*...Ahhh!...Ahhh!..."
    mc "Shh!...Don't moan too loud. Someone might hear you."
    rin "*Heavily breathes*...Mmmm...I can't control...it..."
    $ renpy.pause()
    menu:
        "Slowest":
            scene black
            hide rin_mis3
            jump rinmis1
        "Slower":
            scene black
            hide rin_mis3
            jump rinmis2
        "Next":
            scene black
            hide rin_mis3
            scene ep2_218_a15 with dissolve
            mc "Let's change position..."
            rin "....What do you have in mind?"
            mc "Get up and bend over here."
            jump rin_behind
label rinmis1:
    show rin_mis1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Faster":
            scene black
            hide rin_mis1
            jump rinmis2
        "Fastest":
            scene black
            hide rin_mis1
            jump rinmis3
        "Next":
            scene black
            hide rin_mis3
            if poschange == False:
                scene ep2_218_a13 with dissolve
                mc "Let's change position..."
                rin "....What do you have in mind?"
                mc "Get up and bend over here."
                jump rin_behind
            elif poschange == True:
                jump rinbehind1
label rinmis2:
    show rin_mis2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slower":
            scene black
            hide rin_mis2
            jump rinmis1
        "Faster":
            scene black
            hide rin_mis2
            jump rinmis3
        "Next":
            scene black
            hide rin_mis3
            if poschange == False:
                scene ep2_218_a14 with dissolve
                mc "Let's change position..."
                rin "....What do you have in mind?"
                mc "Get up and bend over here."
                jump rin_behind
            elif poschange == True:
                jump rinbehind1
label rinmis3:
    show rin_mis3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Slowest":
            scene black
            hide rin_mis3
            jump rinmis1
        "Slower":
            scene black
            hide rin_mis3
            jump rinmis2
        "Next":
            scene black
            hide rin_mis3
            if poschange == False:
                scene ep2_218_a15 with dissolve
                mc "Let's change position..."
                rin "....What do you have in mind?"
                mc "Get up and bend over here."
                jump rin_behind
            elif poschange == True:
                jump rinbehind1
label rin_behind:
    $ poschange = True
    scene black with dissolve
    $ renpy.pause()
    scene ep2_218_a16 with dissolve
    rin "Like this?"
    mc "Yeah..."
    show rin_behind1 with dissolve
    window hide
    rin "Ah!...You should've told me before moving your hips..."
    rin "Mmmm...I wasn't prepared for that..."
    $ renpy.pause()
    rin "*Softly breathes*...Move faster, please..."
    mc "As you wish..."
    scene black
    hide rin_behind1
    show rin_behind2 with dissolve
    window hide
    rin "*Moans*...Ahhh...Your dick is going inside me deeper in this position..."
    rin "*Moans*..Mmmm....I can feel it touching my womb..."
    $ renpy.pause()
    scene black
    hide rin_behind2
    show rin_behind3 with dissolve
    window hide
    rin "*Heavily breathes*...Ahh!... You're suddenly moving...Mmmm... Faster without telling me again!"
    rin "*Heavily breathes*...Mmm!!... You're driving me crazy!"
    $ renpy.pause()
    menu:
        "Back":
            scene black
            hide rin_behind3
            jump rinmis1
        "Slowest":
            scene black
            hide rin_behind3
            jump rinbehind1
        "Slower":
            scene black
            hide rin_behind3
            jump rinbehind2
        "Cum":
            jump rincum
label rinbehind1:
    show rin_behind1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Back":
            scene black
            hide rin_behind1
            jump rinmis1
        "Faster":
            scene black
            hide rin_behind1
            jump rinbehind2
        "Fastest":
            scene black
            hide rin_behind1
            jump rinbehind3
label rinbehind2:
    show rin_behind2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Back":
            scene black
            hide rin_behind2
            jump rinmis1
        "Slower":
            scene black
            hide rin_behind2
            jump rinbehind1
        "Faster":
            scene black
            hide rin_behind2
            jump rinbehind3
label rinbehind3:
    show rin_behind3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Back":
            scene black
            hide rin_behind3
            jump rinmis1
        "Slowest":
            scene black
            hide rin_behind3
            jump rinbehind1
        "Slower":
            scene black
            hide rin_behind3
            jump rinbehind2
        "Cum":
            jump rincum
label rincum:
    rin "*Heavily breathes*...I'm about to cum!"
    mc "...Me, too!"
    mc "Where do you want me to cum?"
    rin "*Heavily breathes*...Just cum inside. It's safe for me."
    mc "*Softly breathes*...Okay..."
    scene black
    hide rin_behind3
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep2_218_a19 with dissolve
    rin "I'm cumming!!"
    mc "Argh...."
    rin "*Pants*...Haaa..."
    mc "I'm going to pull out."
    rin "*Pants*...O..Okay..."
    scene ep2_218_a20 with dissolve
    rin "*Pants*...That...was...so good..."
    $ renpy.pause()
    scene ep2_218_a21 with dissolve
    mc "[rin]."
    rin "Hmmm?..."
    mc "Do you still want to finish the episode?"
    scene ep2_218_a22 with dissolve
    rin "I'm too tired now..."
    rin "So, I think I should go back to my room."
    mc "Okay then, see you tomorrow."
    rin "Goodnight, [mc]."
    scene ep2_218_a23 with dissolve
    rin "(Awww... I can't believe I actually had sex!)"
    rin "(And I think that was such a great first time for me)"
    rin "(But, it actually feels a bit weird looking at him after we just had sex though.)"
    rin "(So, I had no choice, but to leave first...)"
    $ renpy.end_replay()
    $ sexwithrin = 1
    $ rin_ch1_ep2 += 3
    $ rin_relationship += 3
    scene black with dissolve
    $ renpy.sound.play("sfx/Door closing.mp3")
    $ renpy.pause()
    scene ep2_218_a24 with dissolve
    u "Okay, let's finish this episode..."
    scene black with dissolve
    $ renpy.pause()
    jump krystalkitchen

label krystalkitchen:
    #---------Music here-----------#
    scene ep2_219 with dissolve
    play music "sfx/ep2_5.mp3" fadein 3.0
    $ bgm = "Mike Leite - Fiesta Loca"
    u "........."
    u "As I thought, a cup of noodles isn't enough to get me full all night..."
    u "It's already late though, I can't order out."
    u "Looks like I have to go to the kitchen and find something to eat."
    u "It's probably going to be just a cup of noodles again."
    scene ep2_220 with fade
    $ renpy.pause()
    scene ep2_221 with dissolve
    $ renpy.sound.play("sfx/snoring.mp3")
    s "*Snoring sounds*......"
    scene ep2_222 with dissolve
    u "Hm? Who's that?"
    u "......"
    scene ep2_223 with dissolve
    u "That's [zeke]."
    u "Why is he sleeping here?"
    zeke "*Snores*....Mmm...Don't worry, [mika]..."
    zeke "*Snores*...I...will...always...take care of...you..."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_224 with fade
    stop sound
    krystal "*Sigh*...I was almost shocked to death, because of that guy's snoring..."
    krystal "Now, everyone went to sleep."
    krystal "Finally, it's time for my dinner..."
    krystal "Hehe... Yummy Yummy..."
    scene ep2_225 with dissolve
    $ renpy.pause()
    scene ep2_226 with dissolve
    u "Hm?..."
    if Krystalintoilet == True:
        u "Isn't that [krystal]?"
        u "Is she always having dinner this late?"
        u "Well, I guess it's because she doesn't want to be seen..."
    elif Krystalintoilet == False:
        u "Who's that?"
        u "...[krystal]?"
        u "I know why nobody has ever seen her now. She only comes out of her room when everyone's asleep."
    scene ep2_227 with dissolve
    krystal "Awww!... So good!"
    krystal "There is no way I'll get bored of eating sushi!"
    scene ep2_228 with dissolve
    krystal "....Hm?"
    krystal "......"
    $ latedinner = True
    if Krystalintoilet == True:
        scene ep2_228_a1 with dissolve
        krystal "No!!"
        krystal "Don't look at me!"
        mc "......."
        mc "Relax. It's me."
        krystal "......."
        scene ep2_228_a2 with dissolve
        krystal "...[mc]?"
        mc "Yep."
        krystal "...It's you!!"
        mc "What?"
        krystal "......"
        scene ep2_228_a3 with dissolve
        krystal "*Sigh*...Why didn't you call me before walking in?"
        krystal "Yeah, you should've done that."
        krystal "You almost gave me a heart attack."
        krystal "I'd be in trouble if you were someone else...."
        scene ep2_228_a4 with dissolve
        mc "I'm sorry then."
        mc "I thought you wanted to be alone, so I was just going to ignore you."
        krystal "You could do that only if we didn't know each other!"
        mc "Got it."
        scene black with dissolve
        $ renpy.pause(0.2,hard=True)
        scene ep2_228_a5 with dissolve
        krystal "I thought you went to sleep already."
        krystal "Why are you having such a late dinner today?"
        krystal "Didn't you eat anything before?"
        scene ep2_228_a6 with dissolve
        mc "Yes, I did."
        mc "But, I've gotten hungry again."
        krystal "I see..."
    elif Krystalintoilet == False:
        scene ep2_228_b1 with dissolve
        krystal "No!!"
        krystal "Don't look at me!"
        mc "......."
        scene ep2_228_b2 with dissolve
        krystal "........"
        krystal "(...Is he still there?)"
        krystal "(Why didn't he say anything?)"
        scene ep2_228_b3 with dissolve
        krystal "(What...?)"
        krystal "(He isn't there....)"
        krystal "(Where has he gone?)"
        scene ep2_228_b4 with dissolve
        krystal "(Oh! There he is!)"
        krystal "(He must be a new tenant for sure. I've never seen him before.)"
        krystal "(What is he doing?)"
        scene ep2_228_b5 with dissolve
        krystal "(...Does he not notice that I'm here?)"
        krystal "(No, that's impossible. There is no way he didn't see me before walking in.)"
        krystal "(Can it be... That he is ignoring me?)"
        scene black with dissolve
        $ renpy.pause()
        scene ep2_228_b6 with dissolve
        krystal "......."
        mc "......."
        krystal "(This guy....!)"
        scene ep2_228_b7 with dissolve
        krystal "Hey!"
        mc "What?"
        krystal "What...?"
        krystal "Don't you think that it's rude to ignore someone?"
        krystal "I'm sitting right here!"
        scene ep2_228_b8 with dissolve
        mc "...Why are you so mad?"
        mc "I heard your story. You've been hiding from everyone."
        mc "So, I assume that you don't want to be noticed."
        mc "But, I have to eat here, so I chose to ignore you."
        mc "Isn't it what you want?"
        krystal "........"
        krystal "*Sigh*...Yeah, you're right. I'm sorry."
        scene ep2_228_b9 with dissolve
        krystal "But, to think that you came up with such an idea..."
        krystal "*Giggles*...you're really weird."
        mc "......."
        krystal "(Moreover, he saw my face, but he doesn't seem to know who I am...)"
        krystal "(Should I ask him to make it sure?)"
        krystal "(.......)"
        scene ep2_228_b10 with dissolve
        krystal "...Do you know who I am?"
        mc "No. Am I supposed to know you?"
        krystal "......."
        krystal "(He doesn't seem to be lying....)"
        krystal "(This is my first time meeting a guy who doesn't know me...)"
        scene ep2_228_b8 with dissolve
        krystal "(To be honest I'm really lonely....)"
        krystal "(I've been hiding, and living alone for more than two years.)"
        krystal "(Can I be friends with him...?)"
        krystal "What's your name?"
        mc "[mc]."
        scene ep2_228_b10 with dissolve
        krystal "[mc]...You've got such a good name"
        mc "Thanks."
        $ krystal_name = "Krystal"
        $ persistent.krystal_name = krystal_name
        krystal "I'm [krystal]. Nice to meet you."
        mc "Nice to meet you."
        krystal "Can you promise me one thing?"
        mc "Promise?"
        krystal "Yeah, don't tell anyone about me, okay?"
        mc "........"
        mc "Okay....."
        $ firstmeet == True
        $ krystal_ch1_ep2 += 2
        $ krystal_relationship += 2
        krystal "Great. Then, let's have our dinner."
    mc "By the way, where did you get that sushi from?"
    mc "You ordered it?"
    scene ep2_228_a8 with dissolve
    krystal "It looks good, right?"
    mc "To be honest... Yes, it does."
    scene ep2_228_a7 with dissolve
    krystal "*Giggles*...Thanks."
    mc "You made it?"
    krystal "Yeah, I made it by myself."
    mc "...You're so good at cooking."
    scene ep2_228_a9 with dissolve
    krystal "*Giggles*...No, I'm not. It's just sushi."
    krystal "It isn't that hard to make sushi actually."
    mc "Well, it's still hard to make it look so good."
    mc "If I was the one making it, it would look really bad and no where near as good as the sushi you made."
    scene ep2_228_a8 with dissolve
    krystal "*Giggles*...I can imagine that."
    krystal "I can teach you later when we have an opportunity if you want."
    mc "I don't know. Let's see..."
    if Krystalintoilet == True:
        scene ep2_228_a9 with dissolve
        mc "By the way, what's going on?"
        krystal "Hm? What do you mean?"
        mc "I think you look a bit different from last time."
        krystal "....Do I?"
        mc "Yeah."
        scene ep2_228_a10 with dissolve
        krystal "Maybe it's because I applied makeup for a natural look today!"
        mc "...Oh yeah, you're right."
        krystal "Not many guys can notice the difference, but you can."
        krystal "I must say that I'm impressed!"
    scene black with dissolve
    $ renpy.pause()
    scene ep2_228_a11 with dissolve
    krystal "*Sucks*...Mmmm..."
    krystal "The salmon is so fresh today."
    krystal "......."
    scene ep2_228_a12 at eyesblink("Ch.1/Ep.2/Scenes/ep2_228_a12.jpg", "Ch.1/Ep.2/Scenes/ep2_228_a12_blink.jpg", 1) with dissolve
    krystal "You know what?"
    krystal "This is my first time in about two years that I'm having dinner with someone."
    mc "Judging from the way you live, I'm not surprised at all."
    krystal "*Giggles*...Right?"
    mc "Why do you have to live like this though?"
    krystal "Well...that's a long story..."
    krystal "I don't want to talk about it."
    mc "...Okay."
    scene ep2_228_a13 at eyesblink("Ch.1/Ep.2/Scenes/ep2_228_a13.jpg", "Ch.1/Ep.2/Scenes/ep2_228_a13_blink.jpg", 1) with dissolve
    krystal "By the way...."
    krystal "Are you sure that cup of noodle is going to make you full?"
    mc "No, it's not."
    mc "But, it's the only thing I've got though."
    mc "Moreover, I'm going to sleep soon. So, I think I'll be fine."
    krystal "Ummm...."
    scene ep2_228_a14 with dissolve
    krystal "You're lucky that I'm such a very kind person."
    krystal "Here you are."
    krystal "You can have some of my sushi. Just pick the ones you want."
    mc "Are you sure?"
    krystal "Yes!"
    menu:
        "Take it [krystal2]":
            scene ep2_228_a14_a with dissolve
            mc "Then, I'll take this one..."
            mc "Thank you."
            krystal "Anytime!"
            krystal "*Giggles*..I'm glad that you took it. I don't think I can eat them all anyway."
            $ getsushi = 1
            $ krystal_ch1_ep2 += 2
            $ krystal_relationship += 2
        "Refuse":
            scene ep2_228_a14_d with dissolve
            mc "Thanks for your kindness, but I don't want to bother you."
            krystal "It's okay! Don't hesitate to take one."
            krystal "I don't think I can eat them all anyway."
            mc "I'm really fine."
            krystal ".....Okay then."
            $ getsushi = 2
    scene black with dissolve
    $ renpy.pause()
    scene ep2_228_a15 with dissolve
    krystal "*Sigh*...I'm so full..."
    mc "Me, too."
    if getsushi == 1:
        mc "Your sushi is so good."
        krystal "*Giggles*...Hehe...Thanks."
    scene ep2_228_a16 with dissolve
    krystal "Alright, I think it's time to leave now."
    krystal "I hope we can have dinner together again soon."
    krystal "Goodnight, [mc]."
    mc "Goodnight."
    jump dream
label dream:
    scene black with dissolve
    u "It's time to sleep."
    $ renpy.pause()
    #---------Music here----------#
    play music "sfx/ep2_6.mp3" fadein 3.0
    $ bgm = "Onycs - Eden"
    scene ep2_d1 with fade
    butler "From now on, this is your bed, kid."
    mc "........"
    butler "You should be thankful for my master's kindness."
    mc "...Thank you."
    butler "That's right."
    butler "Alright, I'll leave you here for tonight."
    butler "I'll be back tomorrow morning."
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep2_d2 with dissolve
    mc "......."
    unknown "Hey!"
    mc "(...Hm?)"
    scene ep2_d3 with dissolve
    mc "...What?"
    scene ep2_d4 with dissolve
    unknown "You moved here today?"
    mc "Yes."
    unknown "Me, too!"
    unknown "Wow... Look at this place..."
    unknown "This is far better than where I lived."
    unknown "It's like an upgraded version of the orphanage!"
    unknown "Oh! My name is [tom]. What's your name?"
    mc "[mc]."
    tom "Nice to meet you, [mc]!"
    tom "Let's be friends!"
    scene black with dissolve
    $ renpy.pause()
    scene ep2_d5 with dissolve
    s "After moving into the new place, your life became so much better."
    s "You didn't have to live in fear anymore."
    s "You also got an education like normal children."
    tom "Watch out!"
    scene ep2_d6 with dissolve
    mc "Ouch!"
    tom "Hahaha! I told you to watch out, didn't I?"
    teacher "*Ahem*...Stop playing, please."
    mc "*Sigh*...[tom]...."
    mc "You should pay attention to the teacher..."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_d7 with dissolve
    butler "Listen! Nobody can protect you better than yourself."
    butler "That's why you have to learn how to fight, kids."
    butler "Watch me carefully, any try to remember every movement."
    butler "Then, you'll have to pair up with your friend to practice."
    scene ep2_d8 with dissolve
    tom "[mc]."
    mc "Hm?"
    tom "Let's pair up!"
    mc "...Okay."
    tom "But you'll have to go easy on me, okay?"
    tom "I'm not really good at fighting."
    scene black with dissolve
    s "*About a month later*....."
    scene ep2_d9 with dissolve
    mc "......"
    tom "[mc]!"
    mc "......"
    tom "[mc]!!!"
    scene ep2_d10 with dissolve
    mc "*Sigh*...Stop yelling already."
    tom "Let's go play!"
    mc "Play what?"
    tom "Football! The other kids are waiting for you!"
    mc "You realise that there will be an exam tomorrow, right?"
    mc "You should review the lessons instead of playing."
    scene ep2_d11 with dissolve
    tom "It's too hard for me. There is no way I'm going to pass anyway."
    tom "So, I don't care about it!"
    tom "Let's go play!"
    mc "But I've never played football before..."
    tom "Don't worry. You just need to go on the field, and leave the rest to me."
    tom "I'm going to carry our team!"
    mc "Carry our team? Are you that good?"
    tom "Hey! Hey! Don't you know who are you talking to?"
    tom "I'll be the best football player in the future!"
    tom "I'm going to be even better than Messi and Ronaldo!"
    scene ep2_d12 with dissolve
    mc "Haha... Stop dreaming already."
    tom "Come on! Come play with me!"
    mc "*Sigh*...Fine. Let's go."
    tom "Yeah! Let's go!!"
    scene black with dissolve
    s "You went to play football with [tom]."
    s "By that time, you had no idea that the next day was going to be the last day you saw him."
    #---------Music here----------#
    play music "sfx/ep2_7.mp3" fadein 3.0
    $ bgm = "AERØHEAD - The Reckoning"
    scene ep2_d13 with dissolve
    u "Where's [tom]?"
    u "I haven't seen him since we finished taking the exam."
    u "Did something happen to him?"
    u "I think I should go ask Mr. [butler]."
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep2_d14 with dissolve
    kids "Mr. [butler]."
    kids "Do you know where Julia is?"
    butler "Julia?"
    kids "Yes. A girl with pink short hair. She's our friend."
    kids "She disappeared yesterday."
    butler "Oh...You're talking about that girl..."
    butler "I'm sorry, but she wasn't qualified."
    kids "..W...What do you mean?"
    butler "She didn't pass our expectations. So, we sent her away."
    kids "...Sent her away? To where?"
    butler "To the place she came from."
    scene ep2_d15 with dissolve
    kids "What!? Then, how's she going to live!?"
    butler "......."
    kids "How could you do that to her!?"
    butler "Listen carefully, kids."
    butler "We are not a charity for children! {w}We adopted you for reasons."
    butler "We provide you a place to sleep, food, water, education and much more."
    butler "But as I said before, we are not a charity for children. {w}We don't do it for free."
    butler "You guys aren't here to make friends either."
    butler "So, instead of caring about your friend, you better care about yourself."
    butler "If you don't want to go back to where you came from, {w}you'll have to prove that you're worth our investment."
    butler "You got it?"
    kids "*Hics*....Y...Yes..."
    u "........."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_d16 with dissolve
    $ renpy.sound.play("sfx/Clock alarm.mp3")
    s "*Clock alarms*......."
    scene ep2_d17 with dissolve
    mc "......."
    u "It's been so long since the last time I dreamed about my past..."
    u "Anyway, I need to get up and take a shower."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_d18 with dissolve
    u "Alright, it's time to go to work."
    $ renpy.sound.play("sfx/phone vibrating.mp3")
    s "*Phone vibrates*......."
    u "Hm?..."
    scene ep2_d19 with dissolve
    stop sound fadeout 3.0
    mc "...Hello?"
    scene ep2_d20 with dissolve
    unknown "Good morning, [mc]."
    mc "Good morning, sir."
    unknown "Why haven't I recieved anything from you yet?"
    mc "......."
    unknown "Are you slacking off?"
    mc "No, I'm not."
    unknown "Then, today is the deadline."
    unknown "Understood?"
    scene ep2_d19 with dissolve
    mc "Understood, sir."
    unknown "[mc]."
    mc "Yes?"
    unknown "You're well aware of what'd happen if you became useless, right?"
    mc "Yes, I am."
    unknown "Good."
    stop music fadeout 3.0
    jump mcact

label mcact:
    scene black with dissolve
    $ renpy.pause()
    scene ep2_229 with fade
    liam "[mc]!"
    liam "Stop working already. Let's go have lunch."
    mc "....."
    scene ep2_230 with dissolve
    mc "Thanks for inviting me, but I'm not hungry today."
    liam "Are you sure?"
    mc "Yes, I am. I'll just keep working here."
    liam "Okay then."
    leo "[yui], do you want to have lunch with me?"
    yui "No, thanks."
    leo "Ugh!...It's okay!"
    leo "I'll invite you again tomorrow!"
    scene black with dissolve
    $ renpy.pause(0.2,hard=True)
    scene ep2_231 with dissolve
    #------------Music here-------------#
    play music "sfx/ep2_8.mp3" fadein 3.0
    $ bgm = "Lahar - Genesis"
    u "Okay...."
    u "Now, everyone has left."
    u "This is my chance."
    scene ep2_232 with dissolve
    u "........"
    scene ep2_233 with dissolve
    u "[liam]...."
    u "He is really smart, but he's also careless at the same time."
    u "How did he leave such an important thing like this here...?"
    u "....He didn't even lock the computer, too."
    u "........."
    u "Here it is...."
    scene black with dissolve
    s "*A few moments later*......"
    scene ep2_234 with dissolve
    u "Okay, I've got it."
    u "Now, there is a thing I need to deal with."
    scene ep2_235 with dissolve
    u "There it is..."
    scene ep2_236 with dissolve
    u "That's a CCTV."
    u "I'm sure that it captured everything I did."
    u "I can't leave it just like that."
    u "I need to get rid of the video."
    scene ep2_237 with fade
    sec "Everyone already went to have lunch..."
    sec "Why am I always the one left behind?"
    sec "*Sigh*...Well, it's just another day of the working life..."
    scene ep2_238 with dissolve
    sec "*Yawns*...But, it's kind of boring though."
    sec "All I have to do here everyday, is just keep watching the cameras..."
    sec "I mean...who would be stupid enough to cause a problem in a company like this?"
    scene ep2_239 with dissolve
    $ renpy.sound.play("sfx/Door opening.mp3")
    s "*Door opening*....."
    sec "*Hums*...Hit you with that ddu-du ddu-du du!"
    sec "*Hums*...Oh yeah! Oh yeah~!"
    $ renpy.sound.play("sfx/Door closing.mp3")
    scene ep2_240 with dissolve
    mc "Er...."
    sec "*Hums*...Black Pink!"
    u "*Sigh*...What kind of security guard is this...?"
    u "He doesn't even notice me standing behind him..."
    scene ep2_241 with dissolve
    mc "Hey!!"
    sec "Huh!? W-What!?"
    sec "Was that a gun shot!?"
    scene ep2_242 with dissolve
    sec "Oh! Did you call me?"
    mc "Yes, I did."
    sec "Is there something you want?"
    mc "I bought a hot chocolate, and I got one more cup from the one plus one promotion."
    mc "I don't know whom I'm going to give it to."
    scene ep2_243 with dissolve
    mc "So, I want to give it to you guys, the security team."
    mc "Let's say it's a thank you gift for keeping us safe."
    sec "O-Oh...How sweet of you."
    sec "Thank you very much."
    mc "No worries. Then, I'll leave now."
    sec "Okay man!"
    scene black with dissolve
    $ renpy.pause()
    scene ep2_244 with dissolve
    sec "What a nice person..."
    sec "Actually, I was a little bit sleepy. I hope this is going to give me a little bit more energy."
    sec "Mmmm...a hot chocolate in a cold day like this...."
    sec "Arr...This is going to keep me full for a while until my co-workers come back."
    scene black with dissolve
    $ renpy.sound.play("sfx/Door opening.mp3")
    s "*Door opening*......"
    $ renpy.sound.play("sfx/Door closing.mp3")
    scene ep2_245 with dissolve
    $ renpy.sound.play("sfx/snoring.mp3")
    sec "*Snores*....Zzzz...."
    scene ep2_246 with dissolve
    u "Have a good sleep..."
    sec "*Snores*....Zzzz...."
    scene ep2_247 with dissolve
    u "*Sigh*...Okay..."
    u "Let's get rid of the evidence..."
    u "I can't let anyone know what I did."
    stop sound
    jump aftermeeting
label aftermeeting:
    scene black with dissolve
    stop music fadeout 3.0
    $ renpy.pause()
    scene ep2_248 with fade
    play music "sfx/ep2_1.mp3" fadein 3.0
    $ bgm = "Vendredi - Te Amo"
    pete "Alright, that's enough for our meeting today."
    pete "Thank you everyone!"
    pete "You guys can leave now."
    scene ep2_249 with dissolve
    leo "Wooh! It's time to leave work!"
    david "You look a little bit too happy, [leo]."
    joe "Yeah, why? You have a date after work?"
    if sally_reply1_choice == 1:
        leo "Hehe...I have an appointment with a girl on tin-"
        scene ep2_250 with dissolve
        unknown "[mc]!!"
        mc "Hm?"
    elif sally_reply1_choice == 2:
        leo "Hehe...I have an appointment with a girl on tinder."
        joe "Really!? Is she pretty?"
        leo "Of course she is!"
        joe "Man...I'm very jealous of you..."
        scene black with dissolve
        $ renpy.pause()
        jump endofep2
    leo "That voice...!"
    leo "It can't be...!"
    scene ep2_251 at eyesblink("Ch.1/Ep.2/Scenes/ep2_251.jpg", "Ch.1/Ep.2/Scenes/ep2_251_blink.jpg", 1) with dissolve
    sally "What's up!"
    sally "Are you ready!?"
    mc "You got here too fast..."
    mc "You'll have to wait for a bit. I need to get my stuff, and turn off the computer first."
    scene ep2_252 with dissolve
    sally "Sure! No problem!"
    leo "(Damn!...Isn't that [sally], the angel of the game specialist department!)"
    leo "(I saw them together last time, but I thought they didn't know each other.)"
    leo "(But, I was obviously wrong! They know each other for sure!)"
    scene ep2_253 with dissolve
    david "What are you doing, [leo]?"
    david "Hurry up and get everything done already."
    david "So, we can lea-"
    scene ep2_254 with dissolve
    leo "Shh! Be quiet!"
    leo "Shut up, and come take a look over here!"
    leo "[mc] is talking to [sally]!"
    scene ep2_255 with dissolve
    david "Is this what you want me to see?"
    david "That's very normal. They're just talking."
    david "[sally] usually talks with everyone."
    leo "No, it isn't that normal!"
    leo "Don't you see the way she's looking at him?"
    leo "It's a lot different from when she talked with us!"
    joe "What are you guys talking about? I want to see it, too!"
    scene ep2_256 with dissolve
    sally "What are you waiting for?"
    sally "Go get your stuff, so we can leave now."
    mc "Okay."
    yui "(Hm?... Who's that girl [mc]'s talking to?)"
    yui "(Does he know any other girls besides [rin], and me?)"
    scene ep2_257 with dissolve
    leo "Oh shit! He's coming here!"
    leo "Hurry up! We need to hide!"
    david "...Why do we need to hide though?"
    leo "....Yeah, you're right. Why?"
    scene ep2_258 with dissolve
    leo "Wait a second, man."
    mc "Hm?..."
    mc "Is there something you want from me?"
    leo "Let's talk."
    scene ep2_259 with dissolve
    mc "What do you want to talk about?"
    leo "Do you know that woman, [sally]?"
    mc "Yes, I do. Why?"
    david "[leo] probably just wants to know why she is here, {w}and what she said to you."
    scene ep2_260 with dissolve
    mc "She comes to pick me up, {w}then we're going to find something for lunch together."
    leo "What!? Really!?"
    leo "Are you guys a couple?"
    mc "...No, we aren't."
    mc "She just want to return a favor by buying me lunch."
    mc "Can I go now? She's waiting for me."
    leo "Err...Sure, man."
    scene ep2_261 with dissolve
    mc "......."
    leo "(Damn... I'm so jealous of him...)"
    leo "([sally] makes the girl I'm going to meet look like an average girl...)"
    scene black with dissolve
    $ renpy.pause()
    scene ep2_262 with dissolve
    mc "Alright, let's go."
    sally "Yeah, let's go!"
    scene ep2_263 with dissolve
    mc "Where are you going to take me to?"
    sally "I don't know..."
    sally "Let's just walk along the street first."
    mc "You invited me, but you didn't plan for it?"
    sally "Well... It's because I don't know what you can or can't eat!"
    mc "I can eat everything, but you actually could've just asked...."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_264 with fade
    sally "Alright...."
    sally "Let's eat here!"
    mc "Here?"
    scene ep2_265 with dissolve
    sally "Yep. This is my favorite burger restaurant."
    sally "The burgers here are very, very good!"
    sally "Let's get in the line!"
    mc "Okay."
    scene black with dissolve
    s "*A fews moment later*....."
    scene ep2_266 with dissolve
    girl "Good evening, customers!"
    girl "What'd you like to have?"
    sally "Umm... I'd like to have a double cheese burger value meal, please."
    girl "How about this gentleman?"
    scene ep2_267 with dissolve
    sally "What do you want to eat, [mc]?"
    mc "I want the same thing she just ordered, please."
    girl "Alright. Then, it's going to be two double cheese burger value meals..."
    girl "Is that correct?"
    mc "Yes, it is."
    scene black with dissolve
    $ renpy.pause()
    scene ep2_268 with dissolve
    sally "Alright, let's take a seat here."
    mc "Okay..."
    sally "I'm telling you. the cheese burger is the best burger here!"
    sally "You made the right choice!"
    scene ep2_270 with dissolve
    mc "Aren't you a little bit over exaggerating?"
    sally "No, I'm not!"
    sally "Just try it yourself if you don't believe me."
    mc "Okay..."
    scene ep2_269 at eyesblink("Ch.1/Ep.2/Scenes/ep2_269.jpg", "Ch.1/Ep.2/Scenes/ep2_269_blink.jpg", 1) with dissolve
    sally "Do you believe me now?"
    sally "I wasn't just exaggerating, right!?"
    mc "Yeah.... You're right. It's very good."
    scene ep2_271 at eyesblink("Ch.1/Ep.2/Scenes/ep2_271.jpg", "Ch.1/Ep.2/Scenes/ep2_271_blink.jpg", 1) with dissolve
    sally "See? What did I tell you!?"
    sally "I wouldn't bring you here if it wasn't good."
    mc "That makes sense..."
    scene ep2_269 at eyesblink("Ch.1/Ep.2/Scenes/ep2_269.jpg", "Ch.1/Ep.2/Scenes/ep2_269_blink.jpg", 1) with dissolve
    sally "Anyway, can I ask how old you are?"
    mc "Hm? Why do you want to know my age?"
    sally "No reason. I just want to know it."
    mc "Why don't you guess it?"
    scene ep2_271 at eyesblink("Ch.1/Ep.2/Scenes/ep2_271.jpg", "Ch.1/Ep.2/Scenes/ep2_271_blink.jpg", 1) with dissolve
    sally "Ha! You wanna play it like this, right?"
    sally "Well... Judging from how you look, {w}and the fact that you just started working here last week...."
    sally "You're probably just a new graduate..."
    sally "So, I'm going to say... Umm... 22!"
    mc "......."
    sally "Am I right?"
    mc "Seriously?..."
    mc "I think you should just quit the job, and become a detective...."
    scene ep2_271_5 at eyesblink("Ch.1/Ep.2/Scenes/ep2_271_5.jpg", "Ch.1/Ep.2/Scenes/ep2_271_5_blink.jpg", 1) with dissolve
    sally "*Giggles*...Hahaha... That's funny!"
    mc "I'm sure you can be a very great detective."
    sally "Heh...?"
    sally "Then, should I hand in a resignation letter tomorrow?"
    mc "Wait... I was just kidding..."
    sally "*Giggles*...I was just kidding, too!"
    scene ep2_269 at eyesblink("Ch.1/Ep.2/Scenes/ep2_269.jpg", "Ch.1/Ep.2/Scenes/ep2_269_blink.jpg", 1) with dissolve
    sally "By the way, if there's something you wanna ask me, don't hesitate to ask."
    mc "Okay then...."
    jump sally_talkchoice
label sally_talkchoice:
    menu:
        "Your age":
            mc "Since you mentioned about age, it makes me wonder how you ended up working despite being so young."
            mc "Aren't you supposed to be studying at a university?"
            scene ep2_271 at eyesblink("Ch.1/Ep.2/Scenes/ep2_271.jpg", "Ch.1/Ep.2/Scenes/ep2_271_blink.jpg", 1) with dissolve
            sally "Well...."
            sally "To be honest It wasn't something I'm proud of, but it was what made me who I am."
            sally "Just forget about a university. I didn't even finish high school."
            sally "It's because I was so addicted to games that I often skipped school just to have more time to play games."
            sally "Finally, I ended up quitting the school..."
            sally "Then, I decided to start streaming."
            sally "Luckily, I got a lot of subscribers."
            sally "I think it's because I'm a girl, yet I was always one of the top players at every game I played."
            sally "I was streaming for about two years..."
            sally "Then, one day I got an email from the company asking if I wanted to become a game tester for them."
            mc "I see..."
            scene ep2_269 at eyesblink("Ch.1/Ep.2/Scenes/ep2_269.jpg", "Ch.1/Ep.2/Scenes/ep2_269_blink.jpg", 1) with dissolve
            jump sally_talkchoice
        "Favorites":
            mc "Can you tell me what are your favorite things to do?"
            sally "My favorite things to do?"
            mc "Yeah. Give me three things you like the most."
            if sally_like1 == "???" and sally_like2 == "???":
                scene ep2_271_5 at eyesblink("Ch.1/Ep.2/Scenes/ep2_271_5.jpg", "Ch.1/Ep.2/Scenes/ep2_271_5_blink.jpg", 1) with dissolve
                sally "Of course, it has to be games!"
                sally "I really like playing games! I've never got bored of playing!"
                $ sally_like1 = "Games"
                mc "Yeah, I can tell that..."
                mc "What else?"
                scene ep2_271 at eyesblink("Ch.1/Ep.2/Scenes/ep2_271.jpg", "Ch.1/Ep.2/Scenes/ep2_271_blink.jpg", 1) with dissolve
                sally "What are we eating right now?"
                mc "A cheese burger?"
                sally "Yep! A cheese burger!"
                sally "It comes second on the list!"
                $ sally_like2 = "Cheese burger"
                mc "What about the last one?"
                scene ep2_269 at eyesblink("Ch.1/Ep.2/Scenes/ep2_269.jpg", "Ch.1/Ep.2/Scenes/ep2_269_blink.jpg", 1) with dissolve
                sally "Ummm......"
                sally "I don't know.... I can't think of it now."
                mc "It's okay."
                sally "Can I tell you next time?"
                mc "Sure."
                jump sally_talkchoice
            else:
                sally "Hm...?"
                sally "Didn't we already talk about it?"
                mc "Yes, we did. I'm sorry I forgot it."
                sally "No worries."
                jump sally_talkchoice
        "Dislikes":
            mc "What about things you dislike?"
            sally "Things I dislike?"
            mc "Yeah. Tell me three things you dislike the most."
            sally "Ummm....."
            if sally_hate1 == "???" and sally_hate2 == "???":
                scene ep2_269_5 at eyesblink("Ch.1/Ep.2/Scenes/ep2_269_5.jpg", "Ch.1/Ep.2/Scenes/ep2_269_5_blink.jpg", 1) with dissolve
                sally "Cockroaches come first. That's no doubt."
                sally "I really hate it! Especially, when it flies!"
                $ sally_hate1 = "Cockroach"
                sally "It's so disguting!"
                mc "I agree."
                mc "What else?"
                scene ep2_271 at eyesblink("Ch.1/Ep.2/Scenes/ep2_271.jpg", "Ch.1/Ep.2/Scenes/ep2_271_blink.jpg", 1) with dissolve
                sally "Violence."
                sally "I just don't understand why some people like to use violence."
                $ sally_hate2 = "Violence"
                mc "But, there is also violence in a lot of games, too."
                mc "Are you okay with that?"
                sally "Yes, I am."
                sally "Because, they're just games! Nobody's going to get hurt."
                sally "But, we shouldn't use violence in real life."
                mc "I see..."
                mc "What else?"
                scene ep2_269 at eyesblink("Ch.1/Ep.2/Scenes/ep2_269.jpg", "Ch.1/Ep.2/Scenes/ep2_269_blink.jpg", 1) with dissolve
                sally "Ummm......"
                sally "I don't know.... I can't think of it now."
                mc "It's okay."
                sally "Can I tell you next time?"
                mc "Sure."
                jump sally_talkchoice
            else:
                sally "Hm...?"
                sally "Didn't we already talk about it?"
                mc "Yes, we did. I'm sorry I forgot it."
                sally "No worries."
                jump sally_talkchoice
        "End conversation [sally2] [smgr2](Last)":
            mc "I think that's enough for now."
            mc "We should finish our food before it gets too late."
            sally "I think so!"
            scene black with dissolve
            s "*Twenty minutes later*....."
            scene ep2_272 with dissolve
            mc "Alright, let's leave here."
            sally "Okay!"
            girl "Thank you! Please come again!"
            $ buyameal = True
            $ sally_ch1_ep2_1 += 2
            $ sally_relationship += 2
            scene ep2_273 with fade
            s "While [sally] and you are on the way back to the company, she notices something..."
            scene ep2_274 with dissolve
            sally "Hm!?..."
            sally "[mc]!"
            mc "What?"
            scene ep2_275 with dissolve
            sally "Can you wait for me here real quick?"
            sally "I'm going to buy an ice cream right there!"
            mc "Okay."
            sally "Do you want me to buy you one?"
            mc "No, I'm good."
            scene black with dissolve
            s "*A few moments later*......"
            scene ep2_276 with dissolve
            sally "Alright, we can keep walking now!"
            mc "Okay..."
            scene ep2_277 with dissolve
            sally "*lick*...Aw... So good..."
            sally "An ice cream after a meal...."
            sally "What a perfect combination!"
            mc "......"
            scene ep2_278 with dissolve
            mc "Since you look like you're really enjoying it..."
            mc "I think I can say that eating ice cream is one of your favorite things to do."
            sally "Oh yeah! You're right!"
            sally "*Giggles*...I always eat ice cream once a day!"
            $ sally_like3 = "Ice cream"
            scene ep2_279 with dissolve
            sally "By the way, how are you going to get home?"
            mc "My housemate, [zeke], has a car. So, I usually get home with him."
            mc "But, I think I'll have to take a bus in front of the company building today."
            sally "No, you don't have to do that. I have a car."
            sally "Since I brought you here with me, then let me drive you home."
            mc "........"
            mc "Okay then."
            scene black with dissolve
            $ renpy.pause()
            scene ep2_280 with dissolve
            sally "Wait a sec, let me unlock the door for you first."
            mc "......."
            sally "Alright, you're good now."
            mc "Thanks."
            scene ep2_281 with dissolve
            mc "You've got such a good car."
            sally "Thanks!"
            mc "It still looks new. When did you buy it?"
            scene ep2_282 with dissolve
            sally "Yeah, I just bought it."
            sally "About four months ago I guess?"
            sally "*Giggles*...I spent half of my money on it!"
            mc "That's a lot..."
            jump endofep2

label endofep2:
    play music "sfx/ep2_6.mp3" fadein 3.0
    $ bgm = "Onycs - Eden"
    if sally_reply1_choice == 1:
        scene black with dissolve
        s "*A few moments later*....."
        scene ep2_283 with fade
        mc "Okay, this is my house."
        sally "Alright then, we've arrived here."
        mc "Thank you for driving me here."
        sally "Anytime!"
        scene ep2_284 with dissolve
        u "Alright, let's get in the house and go to my room."
        u "I have something really important to do."
    elif sally_reply1_choice == 2:
        scene black with dissolve
        s "Since there is something you need to do,"
        s "you decided to go straight to your house after work..."
    scene ep2_285 with dissolve
    u "......."
    u "Okay, that's it."
    scene ep2_286 with dissolve
    u "Now, I just have to call him."
    scene ep2_287 with dissolve
    mc "...Hello."
    mc "I've sent you the code of Xecon gear."
    $ yui_ch1_ep2_sum = yui_ch1_ep2 + yui_ch1_ep2_1
    $ sally_ch1_ep2_sum = sally_ch1_ep2 + sally_ch1_ep2_1
    scene black with dissolve
    $ renpy.pause()
    $ rin_sex += 1
    $ dinnerwithzeke = True
    hide screen smartphone
    $ episode = 2
    call screen ending

label ep2yuiroom:
    scene black
    scene ep2_yui1 with fade
    yui "*Hums*...Let's check my work again and see if there is something more I can do to improve it."
    yui "(I'm going to need to turn the computer on first.)"
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Knocking*..."
    yui "(Hm?...)"
    scene ep2_yui2 with dissolve
    yui "Is that you, [rin]?"
    mc "No. It's me, [mc]."
    yui "Is there something you want from me?"
    yui "Why did you knock on my door?"
    mc "May I come in, please?"
    yui "......"
    yui "Sure."
    $ ep2yuiroom = True
    jump house_ep2
label ep2rinroom:
    scene black
    scene ep2_rin1 with fade
    rin "Aww... So refreshing.."
    rin "What a tiring day..."
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Knocking*...."
    rin "(Hm?...)"
    scene ep2_rin2 with dissolve
    rin "Who is it?"
    mc "It's me."
    rin "[mc]?"
    mc "Yes."
    rin "What do you want?"
    mc "May I come in?"
    rin "W-Wait a second!"
    scene ep2_rin3 with dissolve
    rin "(I need to find something to wear...)"
    scene black with dissolve
    $ renpy.pause()
    scene ep2_rin4 with dissolve
    rin "Alright, you may come in now."
    mc "Okay."
    $ ep2rinroom = True
    jump house_ep2
label ep2_yuiroom_talk:
    scene black
    scene ep2_yuitalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_yuitalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_yuitalk1_blink.jpg", 1) with dissolve
    yui "What do you want?"
    jump ep2_yuiroom_talkchoice
label ep2_yuiroom_talkchoice:
    menu:
        "Talk":
            menu:
                "What were you doing?":
                    mc "What were you doing?"
                    yui "I was about to work."
                    mc "I see."
                    jump ep2_yuiroom_talkchoice
                "Dinner":
                    mc "Are you really not going to have dinner?"
                    yui "No. I'm on a diet just like I said before."
                    mc "Okay."
                    jump ep2_yuiroom_talkchoice
                "Phone number":
                    if yui_contact == False:
                        mc "Can I have your phone number?"
                        yui "Why do you want my phone number?"
                        mc "You know... Just in case we need to talk about work."
                        yui "That makes sense..."
                        scene ep2_yuitalk2 at eyesblink("Ch.1/Ep.2/Scenes/ep2_yuitalk2.jpg", "Ch.1/Ep.2/Scenes/ep2_yuitalk2_blink.jpg", 1) with dissolve
                        yui "Alright, I'll give it to you then."
                        mc "Thanks."
                        scene ep2_yuitalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_yuitalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_yuitalk1_blink.jpg", 1) with dissolve
                        $ yui_contact = True
                        jump ep2_yuiroom_talkchoice
                    elif yui_contact == True:
                        mc "Can I have your phone number?"
                        yui "Hm? Didn't I already give it to you?"
                        mc "Oh yeah, actually you did."
                        mc "My bad."
                        jump ep2_yuiroom_talkchoice
                "Favorites":
                    mc "Can I ask what your favorite things to do are?"
                    yui "My favorites to do?"
                    mc "What are the things you like the most?"
                    if yui_relationship >= 3:
                        if yui_like1 == "???":
                            yui "Does it have to be tangible?"
                            mc "No."
                            scene ep2_yuitalk2 at eyesblink("Ch.1/Ep.2/Scenes/ep2_yuitalk2.jpg", "Ch.1/Ep.2/Scenes/ep2_yuitalk2_blink.jpg", 1) with dissolve
                            yui "Then, I'll say I like success the most."
                            yui "I want to be successful at everything I do."
                            $ yui_like1 = "Success"
                            mc "Well, that sounds pretty much like you."
                            yui "Right?"
                            mc "What else?"
                            yui "......"
                            yui "I don't want to tell you now. I don't think we're close enough."
                            mc "Okay."
                            scene ep2_yuitalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_yuitalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_yuitalk1_blink.jpg", 1) with dissolve
                            jump ep2_yuiroom_talkchoice
                        elif yui_like1 == "Success":
                            yui "Didn't we already talk about it?"
                            mc "Yeah, we did."
                            yui "Then, I'm not going to say it again."
                            jump ep2_yuiroom_talkchoice
                    elif yui_relationship < 3:
                        yui "I told you that I will try to be nice to you."
                        yui "But, I don't think we're close enough to talk about this."
                        mc "Okay."
                        jump ep2_yuiroom_talkchoice
                "Dislikes":
                    mc "What about things you don't like?"
                    if yui_relationship >= 3:
                        if yui_hate1 == "???":
                            scene ep2_yuitalk2 at eyesblink("Ch.1/Ep.2/Scenes/ep2_yuitalk2.jpg", "Ch.1/Ep.2/Scenes/ep2_yuitalk2_blink.jpg", 1) with dissolve
                            yui "I didn't like guys, but I learned that not all guys are the same."
                            yui "So, let's say I hate being insulted."
                            mc "I see..."
                            mc "What else?"
                            yui "I don't want to tell you now. I don't think we're close enough."
                            mc "Okay."
                            $ yui_hate1 = "Being insulted"
                            scene ep2_yuitalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_yuitalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_yuitalk1_blink.jpg", 1) with dissolve
                            jump ep2_yuiroom_talkchoice
                        elif yui_hate1 == "Being insulted":
                            yui "Didn't we already talked about it?"
                            mc "Yeah, we did."
                            yui "Then, I'm not going to say it again."
                            jump ep2_yuiroom_talkchoice
                    elif yui_relationship < 3:
                        yui "I told you that I will try to be nice to you."
                        yui "But, I don't think we're close enough to talk about this."
                        mc "Okay."
                        jump ep2_yuiroom_talkchoice
                "Your look [yui1]":
                    if yuihair == False:
                        mc "You look a little bit different."
                        scene ep2_yuitalk3 at eyesblink("Ch.1/Ep.2/Scenes/ep2_yuitalk3.jpg", "Ch.1/Ep.2/Scenes/ep2_yuitalk3_blink.jpg", 1) with dissolve
                        yui "Hm? Maybe it's because I put my hair up?"
                        mc "Oh yeah. You're right."
                        mc "You look quite a bit more mature with this hairstyle."
                        yui "Do I?"
                        mc "Yeah."
                        yui "...Thanks."
                        scene ep2_yuitalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_yuitalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_yuitalk1_blink.jpg", 1) with dissolve
                        $ yui_ch1_ep2_1 += 1
                        $ yui_relationship += 1
                        $ yuihair = True
                        jump ep2_yuiroom_talkchoice
                    else:
                        mc "I already talked about it."
                        mc "I don't think it's a good idea to talk about it again."
                        jump ep2_yuiroom_talkchoice
                "Back":
                    jump ep2_yuiroom_talkchoice
        "Leave":
            mc "Nothing. I'm leaving now."
            yui "Okay."
            jump house_ep2
label ep2_rinroom_talk:
    scene black
    scene ep2_rintalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk1_blink.jpg", 1) with dissolve
    rin "What's up, [mc]."
    rin "What brings you here?"
    jump ep2_rinroom_talkchoice
label ep2_rinroom_talkchoice:
    menu:
        "Talk":
            menu:
                "What were you doing?":
                    mc "What were you doing?"
                    scene ep2_rintalk2 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk2.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk2_blink.jpg", 1) with dissolve
                    rin "Nothing. I was just getting dressed."
                    mc "I see."
                    scene ep2_rintalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk1_blink.jpg", 1) with dissolve
                    jump ep2_rinroom_talkchoice
                "Dinner":
                    mc "Are you really not going to have dinner?"
                    scene ep2_rintalk2 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk2.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk2_blink.jpg", 1) with dissolve
                    rin "Well, I was about to change my mind when taking a bath."
                    rin "However, I'm still not hungry at all."
                    rin "So yeah, I'm not going to have dinner today."
                    mc "Okay."
                    scene ep2_rintalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk1_blink.jpg", 1) with dissolve
                    jump ep2_rinroom_talkchoice
                "Favorites":
                    if rin_like1 == "Shopping":
                        mc "You said you'll tell me more about your favorite things to do when you think we're close enough."
                        rin "Yes, I did."
                        mc "So, are we close enough now?"
                        if rin_relationship >= 10:
                            scene ep2_rintalk2 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk2.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk2_blink.jpg", 1) with dissolve
                            rin "Of course, we are!"
                            mc "Then, can I know what your favorite things are besides shopping?"
                            if rin_like2 == "???" and rin_like3 == "???":
                                scene ep2_rintalk3 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk3.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk3_blink.jpg", 1) with dissolve
                                rin "I was going to say movies, but I think you already knew that since it's very obvious."
                                mc "Yep, it is."
                                $ rin_like2 = "Movies"
                                rin "Then, I will tell you another one."
                                rin "Even though it's at the bottom of my list, it's still my favorite thing."
                                mc "What is it?"
                                rin "Games!"
                                mc "Oh... Yeah, that's no doubt."
                                rin "Right? I'd never work at our company if I didn't like games!"
                                scene ep2_rintalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk1_blink.jpg", 1) with dissolve
                                $ rin_like3 = "Games"
                                jump ep2_rinroom_talkchoice
                            if rin_like2 == "Movies" and rin_like3 == "Games":
                                rin "Hm? Didn't I already tell you about it?"
                                mc "Of course, you did."
                                mc "My bad..."
                                rin "It's alright!"
                                scene ep2_rintalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk1_blink.jpg", 1) with dissolve
                                jump ep2_rinroom_talkchoice
                        elif rin_relationship < 10:
                            rin "I'm sorry, but I don't think so."
                            mc "...Okay."
                            s "You need to have 10 relationship points with her to do it."
                            jump ep2_rinroom_talkchoice
                    elif rin_like1 == "???":
                        mc "What are the things you like?"
                        mc "Give me the top 3 of your favorite things."
                        scene ep2_rintalk2 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk2.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk2_blink.jpg", 1) with dissolve
                        rin "I like to go shopping the most."
                        mc "Why?"
                        rin "I don't know. I just feel happy everytime I go shopping."
                        $ rin_like1 = "Shopping"
                        mc "I see..."
                        mc "What else?"
                        if rin_relationship >= 10:
                            scene ep2_rintalk3 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk3.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk3_blink.jpg", 1) with dissolve
                            rin "I was going to say movies, but I think you already knew that since it's very obvious."
                            mc "Yep, it is."
                            $ rin_like2 = "Movies"
                            rin "Then, I will tell you another one."
                            rin "Even though it's at the bottom of my list, it's still my favorite thing."
                            mc "What is it?"
                            rin "Games!"
                            mc "Oh...Yeah, that's no doubt."
                            rin "Right? I'd never work at our company if I didn't like games!"
                            scene ep2_rintalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk1_blink.jpg", 1) with dissolve
                            $ rin_like3 = "Games"
                            jump ep2_rinroom_talkchoice
                        elif rin_relationship < 10:
                            rin "I don't know if I should tell you. I don't think we're close enough."
                            rin "Let's wait until we get a little bit closer. Then, I'll tell you."
                            mc "...Okay."
                            s "You need to have 10 relationship points with her to do it."
                            scene ep2_rintalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk1_blink.jpg", 1) with dissolve
                            jump ep2_rinroom_talkchoice
                "Dislikes":
                    mc "Let's talk about things you don't like."
                    if rin_hate2 == "???" and rin_hate3 == "???":
                        rin "Umm...I already told you that I hate money, right?"
                        if rin_hate1 == "Money":
                            mc "Yes, you did."
                        elif rin_hate1 == "???":
                            mc "No, you didn't."
                            rin "Didn't I?"
                            mc "Why do you hate money?"
                            rin "It can change people. Turning someone from good to evil."
                            $ rin_hate1 = "Money"
                        rin "However, I hate it, but I still need it in my life."
                        rin "You get it, right?"
                        mc "Yes. It's such an important thing in this world."
                        rin "Yeah, it surely is."
                        mc "What else?"
                        rin "Umm..."
                        scene ep2_rintalk3 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk3.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk3_blink.jpg", 1) with dissolve
                        rin "Liars."
                        rin "I hate when someone lies to me, especially if that person is really close to me."
                        if zeke_hate1 == "Liars":
                            mc "No wonder why [zeke] is your best friend."
                            mc "You guys have something in common."
                            mc "I see... You both hate liars."
                            rin "Yeah."
                        $ rin_hate2 = "Liars"
                        rin "*Giggles*...But, I'm okay if it's a white lie though."
                        rin "Because I also lie sometimes, too!"
                        mc "That's the part of us being human, isn't it?"
                        mc "I don't think there're people who have never ever lied in their whole life."
                        rin "Yeah, you're right."
                        mc "What else? Tell me more."
                        scene ep2_rintalk2 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk2.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk2_blink.jpg", 1) with dissolve
                        rin "Umm..."
                        rin "I also don't like bad people."
                        rin "They're harmful to other people."
                        mc "I see..."
                        scene ep2_rintalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk1_blink.jpg", 1) with dissolve
                        $ rin_hate3 = "Bad people"
                        jump ep2_rinroom_talkchoice

                    elif rin_hate2 == "Liars" and rin_hate3 == "Bad people":
                        rin "Hm? Didn't we already talked about it?"
                        mc "Yes, we did."
                        mc "My bad..."
                        rin "It's alright!"
                        scene ep2_rintalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk1_blink.jpg", 1) with dissolve
                        jump ep2_rinroom_talkchoice
                "Pat her head [rin1]":
                    if rinpathead == False:
                        scene ep2_rinpat with dissolve
                        rin "Aww... What are you doing~?"
                        rin "..S-Stop it. You can't do this. I'm older than you..."
                        mc "Well, it's not my fault. Your hair is so soft that I want to keep touching it."
                        rin "....Is it?"
                        $ rin_ch1_ep2 += 1
                        $ rin_relationship += 1
                        $ rinpathead = True
                        scene ep2_rintalk1 at eyesblink("Ch.1/Ep.2/Scenes/ep2_rintalk1.jpg", "Ch.1/Ep.2/Scenes/ep2_rintalk1_blink.jpg", 1) with dissolve
                        jump ep2_rinroom_talkchoice
                    elif rinpathead == True:
                        u "I already did it once. I don't think I should do it again."
                        jump ep2_rinroom_talkchoice
                "Back":
                    jump ep2_rinroom_talkchoice
        "Leave":
            mc "Nothing. I'm leaving now."
            rin "Okay."
            jump house_ep2
label mcbed:
    if ep2mcroom_pic == False:
        scene ep2_mcroom_photo
    elif ep2mcroom_pic == True:
        scene ep2_mcroom
    s "It's my bed."
    jump house_ep2
label zeke_bookshelf:
    scene ep2_zekeroom
    s "It's just a bookshelf."
    jump house_ep2
label ep2_rinroom_closet:
    if ep2rinroom_pic1 == False and ep2rinroom_pic2 == False:
        scene ep2_rinroom_photos
    if ep2rinroom_pic1 == True and ep2rinroom_pic2 == False:
        scene ep2_rinroom_photo2
    if ep2rinroom_pic1 == False and ep2rinroom_pic2 == True:
        scene ep2_rinroom_photo1
    elif ep2rinroom_pic1 == True and ep2rinroom_pic2 == True:
        scene ep2_rinroom
    s "That's [rin]'s closet."
    jump house_ep2
label ep2_livroom_sofa:
    if ep2livroom_pic == False:
        scene ep2_livingroom_photo
    elif ep2livroom_pic == True:
        scene ep2_livingroom
    s "That's the most comfortable sofa in the house in my opinion."
    jump house_ep2
label ep2_kitchen_microwave:
    if ep2kitchen_pic == False:
        scene ep2_kitchen_photo
    elif ep2kitchen_pic == True:
        scene ep2_kitchen
    s "It's just a microwave."
    jump house_ep2
label ep2_garage_car:
    if ep2garage_pic == False:
        scene ep2_garage_photo
    elif ep2garage_pic == True:
        scene ep2_garage
    s "It's a Nissan GTR, [zeke]'s car."
    jump house_ep2
label ep2_mcroom_pic:
    if _in_replay:
        scene ep2_mcroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep2_mcroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep2mcroom_pic = True
    $ ep2hiddenimages_count += 1
    jump house_ep2
label ep2_yuiroom_pic:
    if _in_replay:
        scene ep2_yuiroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep2_yuiroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep2yuiroom_pic = True
    $ ep2hiddenimages_count += 1
    jump house_ep2
label ep2_rinroom_pic1:
    if _in_replay:
        scene ep2_rinroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    if ep2rinroom_pic2 == False:
        scene ep2_rinroom_photo2
    else:
        scene ep2_rinroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep2rinroom_pic1 = True
    $ ep2hiddenimages_count += 1
    jump house_ep2
label ep2_rinroom_pic2:
    if _in_replay:
        scene ep2_rinroompic2 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    if ep2rinroom_pic1 == False:
        scene ep2_rinroom_photo1
    else:
        scene ep2_rinroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep2rinroom_pic2 = True
    $ ep2hiddenimages_count += 1
    jump house_ep2
label ep2_livroom_pic:
    if _in_replay:
        scene ep2_livingroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep2_livingroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep2livroom_pic = True
    $ ep2hiddenimages_count += 1
    jump house_ep2
label ep2_kitchen_pic:
    if _in_replay:
        scene ep2_kitchenpic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep2_kitchen
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep2kitchen_pic = True
    $ ep2hiddenimages_count += 1
    jump house_ep2
label ep2_garage_pic:
    if _in_replay:
        scene ep2_garagepic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep2_garage
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep2garage_pic = True
    $ ep2hiddenimages_count += 1
    jump house_ep2
