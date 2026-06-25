label ch2ep1:
    scene black
    scene ch2 with dissolve
    $ renpy.pause(3,hard=True)
    scene ep1 with dissolve
    $ renpy.pause(3,hard=True)
    show screen smartphone
    if nominatekrystal == 1:
        play music "sfx/ep2_2.mp3" fadein 3.0
        $ bgm = "Roa - Lights"
        scene ep5_1 with fade
        u "...Alright, I'm here."
        u "This is [eira]'s house. I'm taking her with me today."
        u "I also switched cars, because the other one was too fancy."
        u "It isn't something a normal programmer like me can buy."
        u "So I don't want her to ask me about it."
        scene ep5_2 with dissolve
        u "............."
        u "Am I too early?"
        u "............."
        u "...Well, let's just call her to let her know that I'm already here."
        scene ep5_3 with dissolve
        u "............."
        scene ep5_4 with dissolve
        mc "Hello. It's me, [mc]."
        s "............."
        mc "Yes, I'm here already."
        s "............."
        mc "No worries. I'll wait for you outside."
        mc "Just come out when you're ready."
        scene black with dissolve
        $ renpy.sound.play("sfx/door opening.mp3")
        s "*Door opening*........"
        stop sound
        scene ep5_5 with dissolve
        $ renpy.sound.play("sfx/door closing.mp3")
        s "*Door closing*........"
        stop sound
        u "There she is...."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_6 with dissolve
        eira "*Softly breathes*...G-Good morning, [mc]."
        mc "Good morning."
        eira "*Softly breathes*....I'm sorry I kept you waiting."
        mc "It's okay. It's not your fault. I got here too early."
        eira "...Thanks for saying that."
        eira "...By the way, how do I look?"
        scene ep5_7 with dissolve
        $ renpy.pause()
        scene ep5_8 with dissolve
        $ renpy.pause()
        scene ep5_9 at eyesblink("Ch.2/Ep.1/Scenes/ep5_9.jpg", "Ch.2/Ep.1/Scenes/ep5_9_blink.jpg", 1) with dissolve
        mc "...Hm? Why do you ask?"
        eira "...You told me to dress formally."
        eira "This is the best I've got."
        menu:
            "You look great [eira1]":
                $ eira_ch2_ep1 += 1
                $ eira_relationship += 1
                $ eiraoutfit = 1
                scene ep5_9_a with dissolve
                mc "You look great."
                eira "...Really?"
                mc "Yeah."
                eira "*Giggles*...Thanks."
                mc "...Alright, we shouldn't waste any more time here."
                mc "Let's get going."
                eira "Sure."
            "Not bad":
                $ eiraoutfit = 2
                scene ep5_9 with dissolve
                mc "Well, it's not bad."
                eira "...You don't like it?"
                eira "Should I go inside and change to another outfit?"
                mc "No, we don't have time for that."
                mc "Let's just get going."
                eira "Oh...Okay."
        scene ep5_10 with dissolve
        eira "...By the way, I never knew you had a bad eyesight."
        mc "...Hm?"
        mc "Oh... I don't have a bad eyesight."
        eira "...Hm? Then, why are you wearing glasses?"
        mc "I'm going to need them today."
        eira "I see...."
        scene black with dissolve
        s "*About two hours later*......"
        scene ep5_11 with fade
        eira "...We've finally arrived."
        eira "...What a long trip. I almost fell asleep."
        mc "Do you still remember our plans?"
        eira "Of course I do."
        mc "Great...."
        scene ep5_12 with dissolve
        freya "When are you going to come back home, [aine]?"
        freya "Everyone is waiting for you."
        aine "No, [freya]. No."
        aine "There is no way I'm going to do that."
        aine "Didn't you see the way I was treated by mom?"
        aine "I will never ever go back home again."
        freya "But,...."
        freya "..W-Watch out!"
        scene ep5_13 with dissolve
        aine "Ouch!"
        mc "............"
        freya "[aine]!"
        eira "[mc]...."
        scene ep5_14 with dissolve
        mc "I'm sorry. Did I hurt you at all?"
        aine "No, you didn't."
        aine "And I should be the one to say sorry."
        aine "I wasn't looking where I was going."
        mc "Neither was I."
        scene ep5_15 with dissolve
        freya "Are you really okay, [aine]?"
        aine "Yes, I am..."
        aine "Alright, please excuse us. We've got to go now."
        mc "Sure...."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_16 with dissolve
        mc "Let's go, [eira]."
        eira "............"
        mc "...[eira]?"
        eira "....Isn't that..."
        scene ep5_17 with dissolve
        mc "Hm? Do you know them?"
        eira "Yes, their family is one of the richest in the city."
        eira "I heard their eldest daughter is getting married to the son of their business partner soon."
        eira "I saw it in the news recently."
        mc "So, they're well known here, in this city?"
        eira "Yes. But it seems that the daughter is against it."
        eira "And I heard some rumors that she was a bully in school as well."
        mc "I see..."
        scene ep5_18 with dissolve
        u "So... The same situation as Yui, huh?"
        u "Forcing their own daughter to do something she doesn't like."
        u "...Well, that's not my concern right now. Let's get going."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_19 with fade
        u "Okay... Here we are."
        u "This is the place where [james] and [lucy] were going to meet up."
        u "Well, she is over there..."
        unknown "Excuse me, sir."
        scene ep5_20 with dissolve
        u "....Hm?"
        driver "This place is reserved for today."
        driver "You aren't allowed to be here."
        mc "Oh...."
        driver "I'm sorry. I hope you understand."
        mc "Yeah, I do."
        scene ep5_21 with dissolve
        mc "But actually, I have an appointment with [lucy]."
        driver "Hm? What are you talking about?"
        mc "I'm a journalist from XYJ News."
        mc "Here is my business card."
        driver "Let me see...."
        scene ep5_22 with dissolve
        driver "Oh yeah, you're right."
        driver "I'm sorry. I should've known that."
        driver "But this is my first day working for her. Please, forgive me."
        mc "No worries."
        driver "Thanks! Please, come in."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_23 with dissolve
        rola "Excuse me, who are you?"
        rola "What are you doing here?"
        u "...This woman. I've seen her before."
        u "She is [lucy]'s manager."
        u "Well, let's just act friendly so she doesn't get suspicious."
        scene ep5_24 with dissolve
        mc "Hello, I'm John Doe."
        mc "I'm a journalist from XYJ News. I'm going to be interviewing [lucy] today."
        rola "Hm? Isn't [james] supposed to be doing that?"
        rola "Where is he?"
        mc "An emergency came up for him. So, he sent me instead."
        mc "Didn't you get a message from him? He told me that he was going to send it to you."
        rola "Hm... Let me check."
        scene ep5_25 with dissolve
        rola "Oh yeah, here it is."
        rola "I was pretty busy, so I didn't notice that."
        rola "Okay. He said that he was going to send you here."
        scene ep5_26 with dissolve
        mc "I already showed my business card to your bodyguard. So he let me through."
        mc "But in case you want to see it, here it is."
        rola "I see..."
        rola "But, he isn't a bodyguard. He is a driver."
        mc "Oh..."
        scene ep5_27 with dissolve
        rola "Okay. How about you go wait for us at the nearby cafe?"
        mc "Hm? Isn't it bad for [lucy] to appear in public?"
        rola "Don't worry about that. It's all reserved only for us today."
        rola "The photo session will be done soon."
        rola "I'll help [lucy] get changed and go meet you there."
        u "I'll need to tell [eira] about that, too...."
        mc "Sure. See you soon."
        rola "Yeah, see you."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_28 with fade
        cg "Welcome~!"
        u "Okay. I think this is the cafe she was talking about..."
        u "Let's find a place to sit."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_29 with dissolve
        u ".............."
        u "Well, everything went well as I expected."
        u "Now, I just need to keep the flow going."
        scene ep5_30 with dissolve
        u "[eira] is also ready to make her move as well."
        u "I wonder how she managed to get in here though."
        u "Didn't [rola] say that this cafe is reserved for their staff?"
        u "...Well, maybe some employees saw [eira] talking to me and assumed that she was a staff member."
        scene black with dissolve
        s "*Half an hour later*......."
        scene ep5_31 with dissolve
        cg "Welcome~!"
        u "Finally, there they are...."
        u "Alright, I need to let them know that I'm here."
        scene ep5_32 with dissolve
        mc "Over here!"
        lucy "Hm...?"
        rola "Feel free to go buy a drink. I'll call you when we are going to leave."
        driver "Understood!"
        scene ep5_33 with dissolve
        unknown "Excuse me, [rola]!"
        rola "Hm...?"
        scene ep5_34 with dissolve
        rola "Who are you?"
        rola "How did you get in here?"
        eira "That doesn't matter. Have you got a minute?"
        eira "I have something that I want to talk to you about."
        lucy "(Gosh... She's so beautiful. Is she an idol trainee?)"
        scene ep5_35 with dissolve
        rola "Actually, we're pretty busy right now."
        rola "Can we talk later?"
        eira "Are you sure about that?"
        eira "Look. I'm from Xecon Company."
        eira "I'm looking for someone to be the model for our upcoming project."
        eira "It's the project that is going to blow everyone's mind."
        eira "Are you sure that you don't want to hear about that?"
        rola "................."
        lucy "Can't we talk about it later? I want to hear it myself, too."
        eira "I'm sorry to say it, but I have an appointment with another candidate later."
        rola "...May I ask who you are going to meet next?"
        eira "I'm sorry. I'm not allowed to tell you that."
        rola "I see...."
        scene ep5_36 with dissolve
        rola "Can you do the interview alone, [lucy]?"
        rola "I'm going to talk with her."
        lucy "Sure. It's not like this is my first time, is it?"
        lucy "By the way, just accept the project if you think it's good, okay?"
        rola "We'll talk about it later, [lucy]."
        scene ep5_37 with dissolve
        u "Well, I told her to find a way to separate [rola] from [lucy]."
        u "But, I didn't tell her how to do it."
        u "I must say that she's doing a very good job."
        u "Well done, [eira]...."
        scene ep5_38 with dissolve
        eira "(....Hm?)"
        eira "(*Giggles*....Hehe. Thanks....)"
        scene ep5_39 with dissolve
        rola "Alright. Please, take me to your table."
        rola "I want to know more about your project."
        eira "Sure. Please follow me."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_40 with dissolve
        lucy "Hello there!"
        mc "Hello!"
        mc "Please, have a seat!"
        scene ep5_41 with dissolve
        mc "Hi, I'm John Doe."
        mc "I assume that [rola] already told you everything, right?"
        lucy "Oh! Yes, she did. You're responsible for an interview for today."
        mc "Yeah. You have no idea how happy I am right now."
        mc "I'm such a big fan of yours!"
        scene ep5_42 with dissolve
        lucy "*Giggles*...Really? You didn't say that just to make me happy, right?"
        mc "No, I didn't! It's such a pleasure to meet you today!"
        lucy "*Giggles*...Nice to meet you, too!"
        lucy "Do you want my signature? I can give it to you after we're done with the interview."
        mc "Really? Thank you!"
        scene ep5_43 with dissolve
        mc "By the way, can I record this interview?"
        mc "I'll use it later when I write the article."
        lucy "Sure! Go ahead!"
        mc "Thanks...."
        u "Okay... I won't go straight to the point. I need to catch her off guard."
        u "Well, I did a lot of research about her background story."
        u "Let's just pick the most interesting topic to begin with."
        scene ep5_44 with dissolve
        mc "First of all, I'd like to congratulate you for being chosen to play the leading female character in a movie."
        lucy "Aw... Thank you very much."
        mc "How did it feel when you knew you were chosen?"
        lucy "Umm... Well, I was very surprised back then."
        lucy "Even though I've been an idol for a few years, I'm still inexperienced in acting."
        u "Well... I doubt that."
        scene ep5_45 with dissolve
        mc "As I recall, the movie is still shooting, right?"
        lucy "Yes, it is."
        mc "What is it going to be about?"
        scene ep5_44 with dissolve
        lucy "Well, it's going to be an action movie. I can say it's going to be very fun!"
        mc "That's it? Can you tell me more about it?"
        lucy "I'm sorry, but that's all I'm allowed to tell you now."
        mc "No worries. Do you have anything to say to your fans?"
        lucy "I might not be a good actress, but I'm going to try my best!"
        lucy "Please, support me, everyone!"
        stop music fadeout 3.0
        scene black with dissolve
        s "*Half an hour later*........."
        play music "sfx/rindrowning.mp3" fadein 3.0
        $ bgm = "Mauro Somm - What You Used To Be"
        scene ep5_43 with dissolve
        mc "Alright, that's it for an interview. I've stopped recording."
        lucy "Hm? That's it?"
        mc "Yes. I've got enough information to write about."
        lucy "I see...."
        mc "Do you mind if we talk for a little bit more?"
        scene ep5_45 with dissolve
        lucy "Umm... No, I don't."
        lucy "It seems like [rola] isn't done talking with that woman."
        lucy "So, I'm basically free right now. What do you want to talk about?"
        mc ".............."
        mc "...Well, [james] told me a little bit about his secret."
        scene ep5_46 with dissolve
        mc "Like how he suddenly got so popular."
        lucy ".............."
        mc "He said that he's always been grateful to you."
        lucy "...What do you mean? I don't understand."
        u "So, you're trying to play dumb, huh?"
        mc "I mean...."
        scene ep5_47 with dissolve
        mc "...THIS!"
        james "*Video voices*....Yes, all the news about [krystal] was all made up by me."
        james "*Video voices*....But, it was [lucy] who told me to write fake news in the first place!"
        lucy "!!!!!!"
        scene ep5_48 with dissolve
        lucy "Give it to me!!"
        mc "Shhh.... I wouldn't do that if I were you."
        mc "And I suggest you lower your voice. Do you want to draw other people's attention?"
        mc "Do you have any idea how fans will react if they see this video?"
        mc "And don't even think about taking the phone from me, and deleting the video."
        mc "You can't handle me."
        mc "And even if you managed to do that, I've got so many backups uploaded on the internet."
        lucy "Ugh...!"
        scene ep5_49 with dissolve
        mc "Great...."
        lucy "What do you want?!"
        lucy "Who the hell are you?!"
        mc "You don't need to know about that."
        mc "You're not in a position to ask questions. I'm the only one who can do that."
        scene ep5_50 with dissolve
        lucy "..............."
        mc "Why did you do that to [krystal]?"
        lucy "..............."
        mc "Answer me, or I'll upload the video now."
        scene ep5_51 with dissolve
        lucy "Fuck...!"
        lucy "I did that because I hated her! Are you satisfied now?"
        lucy "That bitch stole everything from me! I fucking hated her!"
        lucy "She was nowhere near as good as I was, but those idiotic people still went crazy for her."
        mc "................."
        scene ep5_50 with dissolve
        mc "Have you ever once felt sorry for her?"
        mc "For what you did to her?"
        lucy "Why should I?"
        lucy "I did that just to take back everything that belongs to me!"
        lucy "What's wrong with that?"
        u "Alright, it's time to leave now...."
        scene ep5_52 with dissolve
        mc "I'll give you until midnight."
        lucy "For what?"
        mc "You have to upload your video where you tell everyone the truth, and apologize to [krystal]."
        lucy "And what if I don't?"
        mc "I'll upload this video on the internet. You can wait and see what happens after."
        scene ep5_53 with dissolve
        mc "It's your choice...."
        lucy "W-Wait! Where are you going?"
        lucy "We're not done talking!"
        driver "(Hm...?)"
        scene ep5_54 with dissolve
        rola "(Hm? He's leaving already?)"
        mc "..............."
        rola "(They finished the interview quicker than I thought....)"
        rola "(Well, it's actually good for us since I can just call [lucy] here to listen to this woman.)"
        rola "(The project she has been talking about is so unreal!)"
        lucy "What are you doing, you idiot!"
        rola "(Hm...? Isn't that [lucy]'s voice?)"
        scene ep5_55 with dissolve
        rola "(What's happening?!)"
        lucy "Go catch him! Don't let him get away!"
        driver "What do you mean? I'm just a driver."
        driver "That man... He is very dangerous."
        driver "I can tell that by the way he looked at me before he left."
        driver "I didn't take this job to do dangerous things like that."
        lucy "So, you prefer to lose your job instead of going after him!"
        driver "Ugh...!"
        lucy "Go catch him! If you can't bring him back to me. You're fired! Remember that!"
        scene ep5_56 with dissolve
        rola "I'm sorry! It seems like something bad just happened."
        rola "Can you give me a contact, please?!"
        rola "I'll contact you later!"
        eira "Oh! Sure."
        eira "Then, I'm leaving now. Let's talk later."
        rola "Okay!"
        scene black with dissolve
        $ renpy.pause()
        scene ep5_57 with dissolve
        rola "What happened, [lucy]?!"
        rola "Why are you so angry?"
        lucy "Ugh...!"
        rola "That journalist... What did he do?"
        rola "Why did you tell our driver to bring him back here?"
        scene ep5_58 with dissolve
        rola "Why aren't you saying anything?"
        rola "I can't help you if I don't know what's your problem."
        lucy "I don't know what I should start with..."
        rola "Is it a really big problem?"
        lucy ".....Yeah."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_59 with dissolve
        driver "*Pants*......"
        lucy "Why do you come back alone? What about him?"
        driver "I'm sorry, but I couldn't find him..."
        lucy "What?!"
        rola "How is that possible? You followed him less than a minute after he left the cafe."
        driver "I have no idea. It's like he just disappeared..."
        lucy "That's bullshit! You didn't try your best searching for him!"
        lucy "You're fired now!"
        scene ep5_60 with dissolve
        driver "W-What?! How can you do that to me?!"
        driver "This isn't even my fault!"
        lucy "I told you to bring him back here, but you failed to do it."
        lucy "So, it is your fault!"
        driver "But...!"
        lucy "Get out of my face!!"
        rola "Don't shout, [lucy]. We're drawing too much attention already."
        lucy "Ugh...!"
        rola "Let's leave here first...."
        stop music fadeout 3.0
        scene black with dissolve
        $ renpy.pause()
        play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
        $ bgm = "Roa - Fresh Time"
        scene ep5_61 with fade
        mc "Alright, we've arrived at your house."
        mc "Thank you for your help, [eira]."
        mc "Goodbye."
        eira "Wait a sec, [mc]..."
        mc "...Hm?"
        scene ep5_62 at eyesblink("Ch.2/Ep.1/Scenes/ep5_62.jpg", "Ch.2/Ep.1/Scenes/ep5_62_blink.jpg", 1) with dissolve
        eira "...Did I really do well today?"
        eira "I feel like... I didn't do anything much...."
        u "Actually, I'm not sure the result would've changed if [rola] stayed with [lucy] during the interview."
        u "But, it was a lot easier without her there."
        mc "Yes, you've done really well."
        mc "If it wasn't for you, I wouldn't have had a chance to be alone with [lucy]."
        scene ep5_63 with dissolve
        eira "...Thank you."
        eira "I feel a lot better now."
        mc "You're welcome."
        eira "...By the way, would you like to come inside?"
        eira "As I recall, we haven't eaten anything yet."
        eira "...And it's already noon. I'll cook you some lunch."
        u ".............."
        menu:
            "Join her for lunch [eira1]":
                $ eira_ch2_ep1 += 1
                $ eira_relationship += 1
                $ ch2ep1lunchateirahouse = 1
                scene ep5_64 with dissolve
                mc "Yeah, you're right."
                mc "I haven't eaten anything yet, and I'm kind of hungry now."
                mc "Thanks for inviting me in."
                eira "You're welcome."
                eira "However, you'll have to move your car."
                eira "You aren't allowed to park the car on the road for too long."
                eira "Let's park it inside."
                mc "Okay, sure."
                jump ch2ep1eirahouse
            "Turn down her offer":
                $ ch2ep1lunchateirahouse = 2
                scene ep5_64 with dissolve
                mc "Thanks for inviting me in, but I prefer to leave now."
                mc "There is something I have to do first."
                mc "I'll have lunch later."
                eira "Oh... Okay. If you say so...."
                mc "Goodbye, [eira]."
                eira "Drive safe, [mc]."
                jump ch2ep1firstnight
    else:
        scene black with dissolve
        s "Today is Saturday. You spent your whole day in the house...."
        jump ch2ep1firstnight
label ch2ep1eirahouse:
    scene black with dissolve
    $ renpy.pause()
    scene ep5_64_a1 with fade
    eira "Come inside and take a seat, [mc]."
    eira "I'll bring you some water."
    mc "Okay...."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_64_a2 with dissolve
    eira "Here you are..."
    mc "Thanks..."
    eira "Please, wait here for a sec.... I'm going to get changed."
    eira "Feel free to turn on the TV if you want..."
    mc "Okay."
    scene ep5_64_a3 with dissolve
    u ".............."
    u "....Oh, I almost forgot..."
    scene ep5_64_a4 with dissolve
    u "I don't need to use these glasses anymore."
    u "I better take them off...."
    $ renpy.sound.play("sfx/door opening.mp3")
    s "*Door opening*....."
    stop sound
    u "Hm? Was that [eira]. Is she already done changing her clothes?"
    u "...Well, that was fast..."
    unknown "*Hums*...Hmmmmm~"
    u "...Hm? That's not her voice."
    u "It must be [sally] then."
    scene ep5_64_a5 with dissolve
    sally "*Hums*....But now you're out of time~"
    u "..............."
    scene ep5_64_a6 with dissolve
    sally "*Hums*.....You'll never be enough."
    sally "*Hums*.....And people say tough luck. You just suck it up."
    sally "*Hums*.....And you think back to a time when you weren't lost~"
    u "..............."
    scene ep5_64_a7 with dissolve
    sally "Awww~! What a lovely morning!"
    u "..............."
    u "....It's noon already, [sally]..."
    scene ep5_64_a8 with dissolve
    u "She just walked past me without realising my presence."
    u "Should I let her know that I am here...?"
    u "..............."
    u "No, I shouldn't do that. I don't want to freak her out."
    u "I'll just stay quiet and wait until she leaves."
    scene ep5_64_a9 with dissolve
    sally "*Hums*....Hmmmm...{size=-10}mmm{/size}..."
    sally "................"
    scene ep5_64_a10 with dissolve
    sally "!!!!!!!?????"
    scene ep5_64_a11 with dissolve
    u "Ahh... Shit...."
    scene ep5_64_a12 with dissolve
    sally "......[mc]?!"
    scene ep5_64_a13 with dissolve
    mc "Hi, [sally]..."
    sally "*Sighs*...You almost gave me a heart attack!"
    sally "Why didn't you tell me that you were here?"
    mc "I'm sorry."
    sally "Since when did you guys get back?"
    sally "Why didn't I realise that?"
    mc "Err....[sally]..."
    sally "...Yes?"
    mc "If I were you I would cover up first..."
    sally "What are you talking abo-"
    sally "!!!!!!"
    scene ep5_64_a14 with dissolve
    sally "Aww!!!"
    sally "Don't look at me, please!"
    mc "...Relax, I've closed my eyes now."
    scene ep5_64_a15 with dissolve
    sally "I-I-I'm leaving now!"
    mc "Okay...."
    sally "(This is so embarrassing...!)"
    sally "(Ugh... I really hate my clumsiness....)"
    sally "(No matter how clumsy I am, there has to be a limit!)"
    sally "(How didn't I even realise that my bath towel slipped off...?)"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_64_a16 with dissolve
    u "*Sighs*...What an awkward situation that was...."
    u ".............."
    u "...Let's go put the cup on the table."
    scene ep5_64_a17 with dissolve
    eira "What happened, [mc]?"
    eira "I heard someone screaming..."
    mc "Well, it was [sally]..."
    eira "Hm? What happened?"
    mc "...Nothing much. She was just shocked to see me because she didn't know that we were already back."
    eira "I see...."
    eira "By the way, what would you like to eat?"
    mc "Anything."
    scene ep5_64_a18 with dissolve
    eira "Okay then, I'll start cooking now."
    eira "Can you go tell [sally] to come and have lunch with us?"
    u "It's just a normal question, but I feel like this is the hardest question ever..."
    u "I don't know if [sally] is willing to see me now. Especially after what just happened..."
    mc "Can't you do that yourself?"
    eira "...Of course, I can, but I have to cook."
    eira "I think it will save more time if you can do that for me."
    mc ".............."
    mc ".....Okay. I'll go tell her..."
    eira "Thank you."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep2_6.mp3" fadein 3.0
    $ bgm = "Onycs - Eden"
    scene ep5_64_a19 with dissolve
    u "............."
    u "What's wrong with me? There is nothing to be afraid of."
    u "Let's just do it...."
    $ renpy.sound.play("sfx/door knocking.mp3")
    s "*Knocks*........"
    stop sound
    scene ep5_64_a20 with dissolve
    mc "[sally]...."
    mc "[eira] told me to ask you if you want to come have lunch with us?"
    mc "................"
    sally "...Can you come in for a sec, [mc]?"
    mc "...Hm? Yeah, sure. If that's what you want..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_64_a21 with dissolve
    sally ".............."
    u "There she is...."
    u "Alright, let's just go and talk to her."
    scene ep5_64_a22 with dissolve
    mc "I'm sorry, [sally]."
    mc "I should've told you that I was there."
    mc "If I did that, it wouldn't have ended up the way it did."
    sally "You don't need to be sorry, [mc]."
    sally "I'm not angry at you."
    sally "You are always quiet. It's your personality. I don't blame you for that."
    mc "Then... Why do you seem so depressed?"
    scene ep5_64_a23 with dissolve
    sally "Well, it's because you saw my ugly body."
    mc "Ugly? What makes you think that?"
    sally "You know... I used to have a boyfriend."
    sally "We were dating for a year."
    sally "...And everything started on the night when we were about to have sex for the first time."
    sally "...He couldn't get hard no matter how much I tried to help him."
    sally "...In the end, we didn't have sex."
    sally "...And not too long after that night, I accidentally heard him talking with his friends."
    sally "...They asked him if we already had sex. He told them everything including the fact that he couldn't get hard."
    sally "...His friends burst into laughter after knowing that."
    scene ep5_64_a24 at eyesblink("Ch.2/Ep.1/Scenes/ep5_64_a24.jpg", "Ch.2/Ep.1/Scenes/ep5_64_a24_blink.jpg", 1) with dissolve
    sally "...Then, he told them that it wasn't his fault. It was actually mine."
    sally "...My body was so ugly that he couldn't get hard."
    sally "...He said that I had very small boobs like a 12-year-old girl with big hips like his mom."
    sally "...I was so heartbroken after hearing that, I decided to break up with him later."
    sally "...I tried to not agree with him, but I ended up thinking he was right when I looked at myself in a mirror...."
    mc "................."
    sally "What do you think? You also saw me naked."
    sally "You also agree with what he said, right?"
    menu:
        "Disagree with her [sally2]":
            jump ch2ep1complimentsally
        "Stay quiet":
            s "Are you sure that you wanted to stay quiet?"
            s "This will end the possibility of having a romantic relationship with [sally]."
            menu:
                "Yes, I am.":
                    $ ch2ep1comsally = 2
                    scene ep5_64_a25 with dissolve
                    mc "..............."
                    sally "..............."
                    scene ep5_64_a26_d with dissolve
                    sally "....See? You agree with him."
                    mc "I just...."
                    sally "It's okay. You don't need to say anything more."
                    sally "I understand that."
                    mc "................."
                    sally "Okay. You can leave first. I will join you guys after I'm done fixing my mood."
                    mc "Okay...."
                    jump ch2ep1lunch
                "On a second thought...":
                    jump ch2ep1complimentsally
label ch2ep1complimentsally:
    $ ch2ep1comsally = 1
    $ sally_ch2_ep1 += 2
    $ sally_relationship += 2
    scene ep5_64_a25 with dissolve
    mc "What are you talking about?"
    mc "You aren't ugly. Not even close."
    sally "....Thanks for saying that...."
    mc "No, [sally]. I didn't say that just to make you happy."
    mc "I don't really think your body is ugly at all."
    scene ep5_64_a26_a1 with dissolve
    sally "..............."
    sally "...Really?"
    mc "Yeah. I really meant that."
    mc "I don't know why your ex-boyfriend thought about your body like that, but for me."
    mc "You have a good looking body."
    sally "..............."
    scene ep5_64_a26_a2 with dissolve
    sally "....Thanks. That means a lot to me."
    mc "That's right. Keep your chin up. Be more confident."
    mc "Stop letting his bad words get to you."
    mc "It wasn't your fault. It was his fault in my opinion."
    mc "I believe that he couldn't get hard because he had a health problem, but he didn't want to lose face with his friends by admitting that."
    mc "So, he chose to blame you instead."
    scene ep5_64_a26_a1 with dissolve
    sally "....Hm?"
    sally "That makes sense... Why didn't I ever think of that?"
    mc "Right?"
    sally "Thank you, [mc]. I'll try to be more confident from now on."
    sally "Okay. You can go first. I will join you guys after I'm done fixing my mood."
    jump ch2ep1lunch
label ch2ep1lunch:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep.3/ep3_9.mp3" fadein 3.0
    $ bgm = "Atch - Freedom"
    scene ep5_64_a27 with fade
    mc "...[eira]."
    eira "Hm...?"
    scene ep5_64_a28 with dissolve
    eira "Oh? You're back?"
    mc "I told her. She said that she will join us soon."
    eira "Thanks, [mc]."
    scene ep5_64_a29 with dissolve
    eira "Please, take a seat. Your food is ready."
    mc "Hm? Why are there only two dishes?"
    eira "I don't feel like eating ramen now."
    eira "I will go make a salad real quick."
    mc "I see..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_64_a30 with dissolve
    eira "Chopsticks, [mc]."
    mc "Oh, thanks."
    eira "You're welcome."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_64_a31 with dissolve
    sally "Hello, guys...."
    eira "Oh, There you come."
    eira "Hi, [sally]."
    eira "Please, take a seat."
    sally "Thank you."
    scene ep5_64_a32 with dissolve
    sally "Thanks for cooking for us."
    eira "You don't need to thank me."
    eira "You often cook for me."
    eira "So, let me cook for you, too."
    scene ep5_64_a33 with dissolve
    sally "It looks so delicious. I can't wait to taste it."
    sally "Oh! By the way, how was today?"
    sally "Did everything go according to the plan?"
    eira "You should ask [mc] about that."
    scene ep5_64_a34 with dissolve
    mc "Yeah, everything went according to plan."
    sally "Oh..."
    mc "[eira] did a very good job."
    eira "Thank you, [mc]."
    sally "...A-Alright, I get it. Let's start eating!"
    scene ep5_64_a35 with dissolve
    u "..............."
    u "...Well, it seems like she hasn't fully fixed her mood yet."
    u "Let's just change the topic."
    scene ep5_64_a36 with dissolve
    mc "By the way, [eira]...."
    eira "Yes?"
    mc "I just realised that you don't seem to be shy when talking anymore."
    mc "How come?"
    scene ep5_64_a37 with dissolve
    eira "...Really?"
    eira "I didn't realise that at all..."
    sally "He's right! You've really become more confident when talking."
    eira "*Smiles*...I don't know. Have I?"
    sally "Yes, you have!"
    scene ep5_64_a38 with dissolve
    eira "I think it's maybe because I feel more comfortable being with you guys."
    eira "I feel like we've gotten closer."
    sally "Aw... I'm glad to hear that."
    sally "So, you weren't naturally shy all your life."
    scene ep5_64_a39 with dissolve
    sally "But, you're just uncomfortable when talking to someone you don't feel close with."
    eira "Yeah, I think you're right."
    eira "To think about it, I used to talk a lot when I was a kid."
    sally "....Hm? Then, when did you start to be untalkative?"
    scene ep5_64_a40 with dissolve
    eira "Do you really want to know about it?"
    sally "Of course, I want to know you better."
    eira "*Sighs*...Well..."
    scene black with dissolve
    eira "It was when I was a freshman at a senior high school...."
    scene ep5_64_a41 with dissolve
    eira "On the first day at school, I met with a group of girls."
    eira "They came to talk to me."
    eira "They asked me to be their friends because we got along very well."
    eira "But, as time went by, I started to feel like I was surrounded by people who didn't share the same interests..."
    scene ep5_64_a42 with dissolve
    sg1 "[eira]!"
    sg1 "Let's go to karaoke after school!"
    eira "Err... I'm sorry, but I have to take an extra tutorial class this evening."
    sg1 "Oh... Okay. Never mind then."
    sg2 "...................."
    scene ep5_64_a43 with dissolve
    eira "And on the next day, when I was on the way to my class...."
    scene ep5_64_a44 with dissolve
    sg3 "*Giggles*....S-Stop! That's too funny!!"
    eira "Hm...? Isn't that...?"
    scene ep5_64_a45 with dissolve
    sg1 "Do you really think that was funny?"
    sg1 "I think it's pretty annoying."
    sg2 "Yeah, I think so."
    sg3 "I think the way you were mocking her was funny."
    sg3 "'Errr...I'm sorry, but I have to take an extra tutorial class this evening.'"
    sg3 "'Errr...Why won't you do this? I'm sorry, everyone, but my mom told me smoking was bad.'"
    sg2 "'Pfff...! She's such an annoying bitch, isn't she?!'"
    scene ep5_64_a46 with dissolve
    sg1 "*Giggles*...Hahaha! Why don't you try saying that to her?!"
    sg2 "*Giggles*...I can already imagine how she will respond!"
    sg2 "*Giggles*...Don't say bad words. My mom told me that saying bad words was bad!"
    sg1 "*Giggles*...Pfff!...Hahaha!... I...can't..take it anymore...!"
    sg3 "*Giggles*....If she's only going to say something like that and disagree with us, why doesn't she just shut the hell up?"
    sg1 "*Giggles*...I know right?"
    eira "...................."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_64_a47 with dissolve
    eira "That was it. After that day, I didn't hang around with anyone anymore."
    eira "And it took me awhile to start talking with anyone again..."
    sally "..................."
    sally "I'm so sorry to hear that..."
    eira "Thank you..."
    sally "Those girls were really mean. My friends back then were really good people."
    sally "I never knew high school students could be that evil..."
    sally "But, you can trust me! If you disagree with me about something, don't hesitate to tell me!"
    sally "I'll never ever talk behind your back like that!"
    scene ep5_64_a48 with dissolve
    mc "Me, too."
    eira "Thanks, everyone..."
    eira "...Alright, I think you guys should start eating already."
    eira "The best way to eat ramen is while it's still hot."
    sally "Yeah, let's start!"
    scene black with dissolve
    s "*An hour later*......."
    scene ep5_64_a49 with dissolve
    mc "Alright, I should go now."
    mc "Thank you for the meal, [eira]."
    mc "It was very delicious."
    eira "You're welcome."
    sally "Goodbye, [mc]."
    mc "See you all later."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_65 with dissolve
    rola "*Sighs*....[lucy]...."
    rola "*Sighs*....What have you done....?"
    rola "*Sighs*....Why did you do that without asking me?"
    rola "*Sighs*....That was such a big mistake. Why did you do that?"
    scene ep5_66 with dissolve
    lucy "A big mistake?!"
    lucy "If I didn't do that, I wouldn't be so popular like I am!"
    lucy "You wouldn't be the manager of the most famous idol!"
    lucy "Yet you just told me that I made a big mistake!?"
    scene ep5_65 with dissolve
    rola "*Sighs*......."
    rola "*Sighs*....What are we supposed to do now?"
    lucy "That's your job. Can't you think of something?"
    rola "*Sighs*....I'm thinking!"
    rola "................."
    scene ep5_67 with dissolve
    rola "...You told me that he didn't record when you admitted everything, right?"
    lucy "....Yeah, he stopped recording before we talked about that."
    rola "*Sighs*...Well, first of all, let's forget about asking for help from the police."
    rola "That's only going to make things worse once reporters know about this."
    rola "Let's just wait until midnight."
    rola "And even if he uploads that video as he said, all you need to do is deny everything that [james] said."
    rola "It might be hard for people to believe, but that bastard doesn't have any evidence of you admitting your crime."
    rola "So, there will at least be people who are willing to believe you."
    scene ep5_68 with dissolve
    lucy "You're right! He doesn't have any evidence to prove [james]'s words!"
    lucy "That's a pretty good idea! Thank you, [rola]!"
    rola "Well, the result might not be as good as we hope though."
    lucy "I believe that people will trust me! Just like they did back then!"
    rola "*Sighs*...I hope so..."
    jump ch2ep1firstnight
label ch2ep1firstnight:
    scene black with dissolve
    $ renpy.pause()
    if nominatekrystal == 1:
        scene ep5_69 with fade
        u "Finally, I am back home."
        u "What a long day it was..."
        u "Let's go to my room."
        u "................."
        u "...On second thought, I think I should tell [krystal] about today first."
        u "...Yeah, let's go find her."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_70 with dissolve
        u "I searched for her downstairs, but I didn't find her."
        u "I assume she's inside her room right now."
        u "Let's just call her...."
        mc "[krystal]...."
        krystal "Hm...? [mc]?"
        mc "Can I come in?"
        krystal "Sure."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_71 with dissolve
        krystal "Good evening, [mc]."
        mc "Good evening."
        krystal "Is there something you want?"
        mc "I have something to tell you."
        krystal "Hm? What is it?"
        scene ep5_72 with dissolve
        mc "I've got the evidence to prove that all the rumors about you are wrong."
        krystal "Really?! Can I see it?!"
        mc "Not now. You'll see it later."
        mc "I just came here to tell you that."
        mc "It's also safe to say now that you will get the modeling job."
        krystal "Aw... I know I've said it a lot, but..."
        scene ep5_73 with dissolve
        krystal "Thank you so much, [mc]."
        krystal "For everything that you've done for me."
        mc "You're welcome."
        u "Because no matter what I did, I did it for myself after all..."
        u "................."
        u "....Yeah, I did it for myself...."
        scene ep5_74 with dissolve
        krystal "....[mc]."
        mc "Hm...?"
        krystal "*Giggles*...Hehe... [mc]."
        mc "...Yes?"
        scene ep5_75 with dissolve
        krystal "I like you...."
        u "Hm? Is she trying to kiss me?"
        u "Yeah, she is...."
        u "Her face keeps getting closer to mine, and the way that she's looking at me."
        u "What should I do?"
        stop music fadeout 3.0
        menu:
            "Let it be [krystal2]":
                u "...Well, whatever happens, happens for the best..."
                jump ch2ep1krystalh
            "Push her away":
                s "Are you sure that you wanted to push her away?"
                s "This means you are going to end any possibility of having a romantic relationship with [krystal]."
                menu:
                    "Yes, I am":
                        $ ch2ep1krystalkiss = 2
                        scene ep5_75_d1 with dissolve
                        mc "I'm sorry, [krystal]."
                        krystal "...Why did you stop me?"
                        mc "I haven't been helping you because I wanted to do something like that."
                        if ep4krystalkiss2 == 1:
                            krystal "But, didn't we already...?"
                        scene ep5_75_d2 with dissolve
                        mc "I know..."
                        mc "And that was just a mistake."
                        krystal "..............."
                        mc "I'm so sorry, [krystal]."
                        scene ep5_75_d3 with dissolve
                        krystal "I thought you liked me..."
                        krystal "That's why you've been helping me."
                        mc "I do like you, [krystal]."
                        mc "You're such a sweet girl, but I like you as a friend."
                        krystal "I see...."
                        scene ep5_75_d4 with dissolve
                        mc "I'm sorry..."
                        krystal "It's alright. Thanks for telling me that."
                        krystal "...Can you leave me alone, please?"
                        mc "Sure...."
                        jump ch2ep1latenight
                    "My bad. That was a miss-click":
                        jump ch2ep1krystalh
    else:
        jump ch2ep1latenight
label ch2ep1krystalh:
    $ ch2ep1krystalkiss = 1
    $ krystal_ch2_ep1 += 2
    $ krystal_relationship += 2
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
    scene ep5_75_a1 with dissolve
    krystal "*Kisses*....Mmmmmm....."
    mc "..............."
    scene ep5_75_a2 with dissolve
    krystal "*Kisses*....Mmmmmmm...."
    mc "*Kisses*.........."
    krystal "*Kisses*...Mmmmm...[mc]...."
    scene ep5_75_a3 with dissolve
    krystal "*Softly breathes*....Can I take that as an answer...?"
    mc "....I don't know..."
    krystal "*Softly breathes*...What do you mean you don't know..?"
    mc "..................."
    mc "....I'm sorry. I shouldn't have done it."
    krystal "..............."
    mc "[krystal]."
    krystal "...Yes?"
    mc "If you like me because you think I'm a good person, you're completely wrong."
    krystal "..............."
    krystal "...No, I'm not. No matter how much you say you aren't a good person, I still believe that you are."
    krystal "You're just trying to not be one."
    mc ".................."
    krystal "It's okay. You don't have to give me an answer now."
    krystal "We still have so much time to learn about each other."
    krystal "But right now... Can we just go with the flow?"
    mc "...Are you sure that you want to do it with me?"
    krystal "Of course, I am."
    mc "................."
    scene ep5_75_a2 with dissolve
    mc "*Kisses*..........."
    krystal "*Kisses*....Mmmmmm....."
    krystal "*Softly breathes*.....[mc]...."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_75_a4 with dissolve
    krystal "*Softly breathes*.............."
    mc ".................."
    krystal "*Softly breathes*...You can pull it up if you want..."
    mc "Okay...."
    scene ep5_75_a5 with dissolve
    krystal "Do you enjoy what you're seeing?"
    mc "...Yes, I do."
    krystal "*Giggles*....I'm so shy right now...."
    mc "You look beautiful..."
    krystal "*Giggles*...Thanks. You can touch them if you want..."
    krystal "Give me a sec to take off my top..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_75_a6 with dissolve
    show ch2ep1_bm1 with dissolve
    krystal "*Softly breathes*...A-Ahh...."
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_75_a7 with dissolve
            hide ch2ep1_bm1 with dissolve
    show ch2ep1_bm2 with dissolve
    krystal "*Softly breathes*...Mmmmm...."
    krystal "*Softly breathes*...Ahhh... I like it..."
    $ renpy.pause()
    menu:
        "Next":
            scene black with dissolve
            hide ch2ep1_bm2 with dissolve
            $ renpy.pause()
    scene ep5_75_a8 with dissolve
    mc "Let me take this off..."
    krystal "...O..Okay..."
    scene ep5_75_a9 with dissolve
    krystal "...[mc]..."
    mc "...Hm?"
    krystal "Stop staring at me like that. I'm so embarrassed..."
    krystal "And are you really going to let me be naked alone?"
    krystal "Take off your clothes..."
    mc "Okay..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_75_a10 with dissolve
    krystal "*Giggles*...Hehe... This is what we call fair play..."
    krystal "Finally, we're both naked."
    mc "Let's do something else."
    krystal "Hm? What do you want to do?"
    mc "...Can you lick it?"
    krystal "....Okay, sure."
    scene black with dissolve
    scene ep5_75_a11 with dissolve
    mc "Wait a sec."
    krystal "...Hm? What's wrong?"
    mc "I don't want to be pleased alone. It's not fair."
    mc "Let me please you, too."
    krystal "But, how are we going to do it?"
    mc "Let's do 69. Do you know what it is?"
    krystal "*Giggles*...Yeah, I know. I've seen it from videos..."
    krystal "Alright, let's do it then!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_75_a12 with dissolve
    show ch2ep1_69_1 with dissolve
    krystal "*Licks*....A-Ah...[mc]..."
    mc "*Licks*...Hm?"
    krystal "*Softly breathes*...It feels so weird down there..."
    mc "Do you want me to stop?"
    krystal "*Softly breathes*...N..No... It's okay... I think I'll get used to it soon..."
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_75_a13 with dissolve
            hide ch2ep1_69_1 with dissolve
    show ch2ep1_69_2 with dissolve
    krystal "*Sucks*....Mmmmmm...."
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_75_a14 with dissolve
            hide ch2ep1_69_2 with dissolve
    mc "I think that's enough, [krystal]."
    krystal "Yeah...?"
    mc "Yes."
    mc "By the way, are you sure that you want to go to the next step?"
    krystal "It's not like we can just stop now and act like nothing has happened."
    krystal "Let's do it..."
    mc "I almost forgot... I don't have a condom with me now."
    krystal "...It's okay. Just shoot it outside...."
    mc "If you say so..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_75_a15 with dissolve
    mc "This is your first time, right?"
    krystal "Y..Yeah... I've masturbated, but I have never put anything inside..."
    krystal "So, can you put it in slowly, please...?"
    mc "Sure... Tell me if it hurts too much."
    scene black with dissolve
    scene ep5_75_a16 with dissolve
    krystal "U-Ugh...!"
    mc "Are you alright?"
    krystal "*Softly breathes*...Y-Yeah... Don't worry about me..."
    krystal "*Softly breathes*...Please, continue..."
    mc "Okay... Then, I'm going to start moving now."
    scene ep5_75_a17 with dissolve
    show ch2ep1_legup1 with dissolve
    krystal "*Softly breathes*...Ahh...."
    mc "...Does it still hurt?"
    krystal "*Softly breathes*...A little bit... But, it feels much better now..."
    $ renpy.pause()
    krystal "*Softly breathes*...Arr... You can do it faster if you want..."
    mc "...Okay."
    menu:
        "Next":
            scene ep5_75_a18 with dissolve
            hide ch2ep1_legup1 with dissolve
    show ch2ep1_legup2 with dissolve
    krystal "*Moans*...Mmmmm...."
    krystal "*Moans*...Arrr... K...Keep moving like that....I like it..."
    krystal "*Softly breathes*....Mmmmmm....."
    $ renpy.pause()
    mc "Can I do it a little bit faster?"
    krystal "*Moans*...Y..Yeah... Go ahead..."
    menu:
        "Next":
            scene ep5_75_a19 with dissolve
            hide ch2ep1_legup2 with dissolve
    show ch2ep1_legup3 with dissolve
    krystal "*Moans*....Ahhh!...."
    krystal "*Softly breathes*...A-Ah... [mc]!... This feels so good...!"
    krystal "*Moans*....D...Don't stop...!"
    $ renpy.pause()
    mc "Can we change into a different position?"
    krystal "*Softly breathes*...H..Hm?... How do you want to do it...?"
    mc "I want to do it from behind..."
    krystal "*Softly breathes*...Mmmm... Okay..."
    menu:
        "Next":
            scene ep5_75_a20 with dissolve
            hide ch2ep1_legup3 with dissolve
    $ renpy.pause()
    scene ep5_75_a21 with dissolve
    show ch2ep1_behind1 with dissolve
    krystal "*Softly breathes*....A-Arrr....."
    krystal "*Moans*....Mmmm.... This is too much..."
    krystal "*Moans*...Ahhhh.... It goes in even deeper in this position.... I think I'm going to cum soon!"
    mc "...Hang in there for a little bit more..."
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_75_a22 with dissolve
            hide ch2ep1_behind1 with dissolve
    show ch2ep1_behind2 with dissolve
    krystal "*Moans*....Ahhhh!...Ahhhh!...."
    mc "Shhh.... Lower your voice..."
    krystal "*Softly breathes*...Mmmmmm... How can I...?"
    krystal "*Heavily breathes*...Ahhhh.... Not yet, [mc]?... I'm about to cum!"
    mc "...Just a little bit more..."
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_75_a23 with dissolve
            hide ch2ep1_behind2 with dissolve
    show ch2ep1_behind3 with dissolve
    krystal "*Heavily breathes*...Mmmm!....Mmmmm!...."
    mc "Almost there...."
    krystal "*Heavily breathes*....Mmmmm!...."
    $ renpy.pause()
    menu:
        "Legup Missionary":
            hide ch2ep1_behind3
            jump krystallegup1
        "Slowest":
            hide ch2ep1_behind3
            jump krystalbehind1
        "Slower":
            hide ch2ep1_behind3
            jump krystalbehind2
        "Cum":
            jump krystalbehindcum
label krystallegup1:
    scene ep5_75_a17 with dissolve
    show ch2ep1_legup1 with dissolve
    $ renpy.pause()
    menu:
        "Lying Behind":
            hide ch2ep1_legup1
            jump krystalbehind1
        "Faster":
            hide ch2ep1_legup1
            jump krystallegup2
        "Fastest":
            hide ch2ep1_legup1
            jump krystallegup3
label krystallegup2:
    scene ep5_75_a18 with dissolve
    show ch2ep1_legup2 with dissolve
    $ renpy.pause()
    menu:
        "Lying Behind":
            hide ch2ep1_legup2
            jump krystalbehind1
        "Slower":
            hide ch2ep1_legup2
            jump krystallegup1
        "Faster":
            hide ch2ep1_legup2
            jump krystallegup3
label krystallegup3:
    scene ep5_75_a19 with dissolve
    show ch2ep1_legup3 with dissolve
    $ renpy.pause()
    menu:
        "Lying Behind":
            hide ch2ep1_legup3
            jump krystalbehind1
        "Slowest":
            hide ch2ep1_legup3
            jump krystallegup1
        "Slower":
            hide ch2ep1_legup3
            jump krystallegup2
label krystalbehind1:
    scene ep5_75_a21 with dissolve
    show ch2ep1_behind1 with dissolve
    $ renpy.pause()
    menu:
        "Legup Missionary":
            hide ch2ep1_behind1
            jump krystallegup1
        "Faster":
            hide ch2ep1_behind1
            jump krystalbehind2
        "Fastest":
            hide ch2ep1_behind1
            jump krystalbehind3
label krystalbehind2:
    scene ep5_75_a22 with dissolve
    show ch2ep1_behind2 with dissolve
    $ renpy.pause()
    menu:
        "Legup Missionary":
            hide ch2ep1_behind2
            jump krystallegup1
        "Slower":
            hide ch2ep1_behind2
            jump krystalbehind1
        "Faster":
            hide ch2ep1_behind2
            jump krystalbehind3
label krystalbehind3:
    scene ep5_75_a23 with dissolve
    show ch2ep1_behind3 with dissolve
    $ renpy.pause()
    menu:
        "Legup Missionary":
            hide ch2ep1_behind3
            jump krystallegup1
        "Slowest":
            hide ch2ep1_behind3
            jump krystalbehind1
        "Slower":
            hide ch2ep1_behind3
            jump krystalbehind2
        "Cum":
            jump krystalbehindcum
label krystalbehindcum:
    mc "I..I'm about to cum!"
    krystal "*Heavily breathes*...Y-Yes, please cum!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_75_a24 with vpunch
    mc "Ahh...."
    krystal "*Moans*....I'm cumming, too!...Mmmmmm...!!!"
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    scene ep5_75_a25 with dissolve
    krystal "*Pants*....T...That...was...so good...."
    mc "Yeah...."
    krystal "*Pants*...I..I can't...move..anymore, [mc]..."
    krystal "*Pants*...Let me....rest for....a sec..."
    mc "Sure..."
    scene black with dissolve
    s "*About five minutes later*......."
    scene ep5_75_a26 with dissolve
    krystal "*Giggles*...I just took a shower an hour ago, but it seems like I'm going to need another one..."
    krystal "...All because of you."
    mc "I'm sorry."
    krystal "*Giggles*...Just kidding! You don't need to be sorry at all."
    krystal "I'm happy that I did it with you. That was a great first time."
    scene ep5_75_a27 with dissolve
    mc "Yeah, that was really great."
    mc "Okay. I think I should leave now."
    mc "I also have to take a shower, too."
    krystal "Hm? Then how about we take a shower together?"
    mc "...Are you for real?"
    scene ep5_75_a28 with dissolve
    krystal "Pff!...No, I'm not!"
    krystal "*Giggles*...I was just teasing you!"
    krystal "*Giggles*...That was funny! You looked surprised to hear that for real."
    krystal "*Giggles*...I've never seen you like that before!"
    mc "............."
    krystal "Don't be so disappointed that I'm not taking a shower with you!"
    mc "...I'm not..."
    scene ep5_75_a29 with dissolve
    krystal "Not today, but maybe we'll do it later!"
    mc "Stop teasing me already..."
    krystal "*Giggles*...Okay. Okay. I will stop it now."
    krystal "Alright, you should leave now."
    mc "Okay. Goodnight, [krystal]."
    krystal "Goodnight...."
    krystal "Hey...."
    mc "Hm...?"
    krystal "You look good when you're smiling."
    mc "Hm? Am I smiling now?"
    krystal "Yes, you are...."
    krystal "I hope I can see you smile for me more."
    mc "..............."
    krystal "*Giggles*...Goodnight for real, [mc]."
    mc "Bye...."
    stop music fadeout 3.0
    $ renpy.end_replay()
    $ krystal_ch2_ep1 += 2
    $ krystal_relationship += 2
    scene black with dissolve
    s "*Half an hour later*....."
    jump ch2ep1latenight
label ch2ep1latenight:
    play music "sfx/ch1ep2.mp3" fadein 3.0
    $ bgm = "Bensound - Little Idea"
    scene ep5_76 with dissolve
    if ch2ep1krystalkiss == 1:
        u "Okay... I'm done taking a shower..."
        u "It's half past eleven."
        u "I've given [lucy] until midnight."
        u "Let's find something to do to kill time..."
    else:
        u "It's already late..."
        u "Let's go to bed...."
    if ep3invitealice == 1:
        scene ep5_77 with dissolve
        $ renpy.sound.play("sfx/phone vibrating.mp3")
        s "*Phone rings*........."
        u "Hm...?"
        u "Someone is calling me?"
        u "Let me see who it is..."
        scene ep5_78 with dissolve
        u "Hm...? It's [alice]."
        u "I wonder why she is calling me now."
        u "Let's hear her out..."
        stop sound
        scene ep5_79 with dissolve
        mc "Hello...."
        scene ep5_80 with dissolve
        alice "Hello, [mc]."
        alice "Did I wake you up?"
        scene ep5_79 with dissolve
        mc "No. I've just finished taking a shower."
        mc "Why are you calling?"
        scene ep5_81 with dissolve
        alice "Look. I already told you that I was going to move there, right?"
        mc "Yeah, you texted me about that."
        alice "It's tomorrow. I'm going to move my personal belongings around 11 a.m."
        alice "So, I decided to call you to ask if you want to come and help me..."
        scene ep5_82 with dissolve
        mc "..............."
        mc "You're going to move out tomorrow morning, but you ask for my help just now?"
        alice "I know... At first, I didn't want to bother you, but I thought it wouldn't hurt to ask."
        alice "That's why...."
        scene ep5_81 with dissolve
        alice "If you don't want to come, it's okay. I understand that."
        mc ".............."
        alice "...What do you say?"
        scene ep5_82 with dissolve
        if nominatekrystal == 1:
            u "Actually, I'm going to release [james] tomorrow morning..."
            u "But, I can do that early and go to [alice] after I'm done with him."
        else:
            u "Actually, I don't have any specific plan for tomorrow..."
        u "What should I answer?"
        menu:
            "Agree to help [alice2]":
                $ ch2ep1helpalice = 1
                $ alice_ch2_ep1 += 2
                $ alice_relationship += 2
                scene ep5_83 with dissolve
                mc "................"
                mc "Okay. I'll meet you there at 11 a.m."
                alice "Really?! Are you really going to come?!"
                mc "Yeah..."
                scene ep5_83_a with dissolve
                alice "*Giggles*...Hehe... I'm so happy to hear that!"
                alice "Alright, I won't bother you anymore. See you tomorrow!"
                mc "Okay. See you tomorrow."
                alice "Goodnight, [mc]."
                mc "You, too."
            "Refuse to help":
                $ ch2ep1helpalice = 2
                scene ep5_83 with dissolve
                mc "................"
                mc "I'm sorry, but it's too short notice."
                mc "I might've gone if you asked me earlier."
                scene ep5_83_d with dissolve
                alice "It's okay. I understand you."
                alice "I'll just call a taxi then."
                alice "Alright, I won't bother you anymore."
                alice "Goodnight, [mc]."
                mc "You, too."
    else:
        scene black with dissolve
        $ renpy.pause()
    if nominatekrystal == 1:
        scene ep5_84 with dissolve
        stop music fadeout 3.0
        u "..............."
        u "Let's just wait until midnight..."
        scene black with dissolve
        play music "sfx/rindrowning.mp3" fadein 3.0
        $ bgm = "Mauro Somm - What You Used To Be"
        $ renpy.pause()
        scene ep5_85 with fade
        lucy ".............."
        lucy "(Ugh...! The time is running....)"
        lucy "(I've only got five minutes left...)"
        lucy "(Did I make the right choice to not do what he told me to?)"
        lucy "(Arghh! That bastard! He's driving me nuts!)"
        scene ep5_86 with dissolve
        rola "Stop biting your nails already, [lucy]!"
        rola "It will get to be a bad habit."
        lucy "But-!"
        rola "Just relax. Why are you so scared?"
        rola "Everything is going to be fine..."
        lucy "Tsk...!"
        scene ep5_87 with dissolve
        $ renpy.sound.play("sfx/phone vibrating.mp3")
        s "*Alarm sounds*....."
        stop sound
        lucy "It's already midnight!"
        lucy "Look on your phone and help me see if the video was leaked anywhere!"
        scene ep5_88 with dissolve
        lucy ".............."
        lucy ".............."
        lucy "....I don't find any videos about that."
        lucy "What about you, [rola]?"
        scene ep5_89 with dissolve
        rola "Me, too...."
        rola "I also didn't find it. Youtube, Twitter, Facebook, etc."
        rola "None of them. No such a video was uploaded."
        scene ep5_90 with dissolve
        lucy "*Sighs*....What a relief!"
        lucy "That bastard... He was just all talk!"
        lucy "Just you wait... I'm going to make you pay for threatening me!"
        lucy "I can finally sleep now!"
        scene ep5_91 with dissolve
        rola "Don't let your guard down just yet."
        rola "He might post it later."
        rola "We need to be alert until we're sure that he is going to do nothing."
        lucy "Jeez... Okay...."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_92 with fade
        u "Okay... So, she chose to ignore me, huh?"
        u "...Well, I gave her the chance because I wanted to see if she will ever regret her guilt."
        u "Then, admit it and tell everyone about the truth."
        u "But she just threw away her last chance..."
        u "Alright then, let's just continue the plan..."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_93 with dissolve
        u "............."
        u "....These glasses. I didn't wear them today because I wanted to disguise myself."
        u "I would be stupid if I believed that no one would recognize me just because I wore them."
        u "Plus, there was no need for me to disguise myself anyway...."
        u "The only reason I wore these glasses was that because they have a spy camera."
        u "Moreover, it records audio, too."
        scene ep5_94 with dissolve
        u "There it is...."
        u "I pretended to stop recording so that she would let her guard down."
        u "Then, I showed the video of [james] to provoke her."
        u "And it was a lot easier than I thought."
        u "She immediately got angry and showed her true colors because she thought that I wasn't recording."
        u "But, she was wrong...."
        u "I've got the video of [lucy] admitting everything herself."
        scene ep5_95 with dissolve
        u "I knew from the beginning that the video of [james] wasn't enough to prove that [krystal] was a victim."
        u "[lucy] might just play dumb, and tell everyone that she was slandered. That everything [james] said was a lie."
        u "So, I decided not to post it on the internet yet, but use it to threaten [lucy]."
        scene ep5_96 with dissolve
        u "Now, I'm going to edit the video, and make it a little bit shorter."
        u "I also need to create a fake account and fake my ip address."
        u "Just in case anything out of control happens..."
        scene black with dissolve
        s "*A few moments later*....."
        scene ep5_97 with dissolve
        u "Okay... Everything is done."
        u "But, I haven't uploaded the video yet."
        u "I just set a release schedule. It's going to be released at 6 a.m."
        u "Alright, everything that I needed to do was done."
        u "I'm so tired today. Let's go to bed..."
        jump ch2ep1nextday
    else:
        scene ep5_84 with dissolve
        u "Alright, there is nothing for me to do anymore."
        u "Let's just sleep..."
        jump ch2ep1nextday
label ch2ep1nextday:
    stop music fadeout 3.0
    scene ep5_98 with dissolve
    $ renpy.sound.play("sfx/Clock alarm.mp3")
    s "*Alarm sounds*........."
    stop sound
    play music "sfx/ep2_2.mp3" fadein 3.0
    $ bgm = "Roa - Lights"
    u "................."
    scene ep5_99 with dissolve
    u "It's already morning...?"
    u "That was fast..."
    scene ep5_100 with dissolve
    u "Okay. Let's go take a shower..."
    if nominatekrystal == 1:
        u "So, the plan for today is to release [james]."
        u "There is no need to hold him there any longer."
        if ch2ep1helpalice == 1:
            u "Then, I will go to see [alice] at her place."
            u "I have to be there at 11 a.m."
            u "Well, I'll be pretty busy today, won't I?"
        else:
            u "Then, let's see what I should do after releasing him..."
    else:
        u "Then, I'll have breakfast and think about what to do for today..."
    scene black with dissolve
    $ renpy.pause()
    if nominatekrystal == 1:
        jump ch2ep1releasejames
    elif nominatekrystal != 2 and ch2ep1helpalice == 1:
        scene ep5_101 with dissolve
        u "Alright, let's have breakfast, then go to see [alice]...."
        jump ch2ep1alicemovingin
    else:
        jump ch2ep1freeday
label ch2ep1releasejames:
    scene ep5_101 with dissolve
    u "The video should've been released by now."
    u "Poor [lucy]. Today is going to be a very tough day for her."
    scene ep5_101_a1 with dissolve
    s "*Voices from distance*....Holy shit!"
    u "Hm...? Wasn't that [zeke]'s voice?"
    u "Today is Sunday, but he woke up very early. I didn't expect that."
    scene ep5_101_a2 with dissolve
    mika "What's wrong, [zeke]? Why did you suddenly swear?"
    zeke "Look at this video, [mika]!"
    s "*Voices from the video*.....That bitch stole everything from me! I fucking hated her!"
    mika "!!!!!"
    krystal "Hm? What are you guys watching?"
    krystal "Why do you look so shocked?"
    scene ep5_101_a3 with dissolve
    zeke "[krystal]! Look!"
    krystal "!!!!!"
    scene ep5_101_a4 with dissolve
    s "*Voices from the video*.....I did that just to take back everything that belongs to me!"
    zeke "This is so amazing, [krystal]!"
    zeke "[lucy] finally showed her true colors to the world!"
    zeke "Everyone is going to stop hating you for no reason now!"
    mika "Yeah... This video proves that all the rumors about you weren't true."
    mika "I'm so happy for you now, [krystal]."
    scene ep5_101_a5 with dissolve
    krystal "Err... Thank you, guys."
    zeke "Damn... I don't know who did this, but I'm very thankful for that person!"
    zeke "Hahaha! Look at her face! I can tell how angry she was!"
    zeke "Wait. Let me share this video first..."
    zeke "The world deserves to know about what she did!"
    scene ep5_101_a6 with dissolve
    krystal "(....Hm?)"
    krystal "(...Isn't that [mc]?)"
    krystal "(That video must've been the evidence he told me about yesterday.)"
    scene ep5_101_a7 with dissolve
    krystal "(I need to talk to him...)"
    zeke "Let's go to the shopping mall, [mika]!"
    mika "Hm? Why so sudden?"
    zeke "This will be the most dramatic topic today! I want to go buy some popcorn!"
    mika "*Giggles*...Alright, let's go then."
    scene ep5_101_a8 with dissolve
    krystal "...Good morning, [mc]."
    mc "Hello."
    krystal "Are you going to go somewhere?"
    mc "Yeah. I have something to finish up."
    krystal "..............."
    mc "What's wrong?"
    scene ep5_101_a9 with dissolve
    krystal "That video... It was you, right?"
    mc "Yeah, why?"
    krystal "I'm very grateful for your help, [mc]."
    krystal "But, I don't know... I can't describe my feelings right now."
    krystal "I knew that she didn't like me, but I never knew she hated me so much that she could do something like that to me."
    krystal "If I only knew that before...."
    mc "There was nothing you could do, [krystal]. Haters are gonna hate."
    krystal "..............."
    scene ep5_101_a10 with dissolve
    krystal "But, did we really have to do it this way?"
    krystal "I know I shouldn't be, but somehow I feel sorry for her."
    mc ".................."
    krystal "No matter how much she hated me, she still used to be a friend."
    krystal "Now, her career will be destroyed...."
    mc "You're too kind, [krystal]."
    krystal "....I know, right?"
    scene ep5_101_a11 with dissolve
    mc "I'm not saying that being kind is bad. Oppositely, it's actually good."
    mc "But, it will become your weakness if you are too kind."
    mc "Also, she doesn't deserve your kindness, especially after what she did behind your back..."
    mc "And yes, we had to do this. The evidence is really important for your rehabilitation."
    mc "People were blinded. Without that video, no one would believe you."
    mc "I know it's very cruel for [lucy], but what she did to you was very cruel, too."
    mc "There are some kind of people who are willing to harm you no matter how good you are towards them."
    mc "[lucy] is that type of person. Don't ever feel sorry for her. She deserves what is coming for her."
    krystal "................."
    scene ep5_101_a12 with dissolve
    krystal "*Sighs*...Well, you're right."
    krystal "I shouldn't really be sorry for her. She was the one destroying my career."
    krystal "Now, it's time for me to take it back."
    mc "Yeah, that's right."
    mc "Alright, I've got to leave now."
    krystal "Oh... Okay."
    mc "See you later, [krystal]."
    krystal "See you."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause(2,hard=True)
    play music "sfx/ep2_8.mp3" fadein 3.0
    $ bgm = "Lahar - Genesis"
    scene ep5_106 with fade
    u ".............."
    u "Alright, let's get this done real quick..."
    scene ep5_107 with dissolve
    mc ".............."
    mc "Hey. Wake up."
    james "..............."
    mc "Wake up!"
    james "!!!!!!"
    scene ep5_108 with dissolve
    james "MMmmmm!!!!"
    mc "Shut up and listen carefully."
    james ".............."
    mc "I'm not going to keep you here any longer."
    mc "Thanks for your cooperation for the past few days."
    mc "I'm going to take the handcuff off for you soon."
    james "MMMmmm!! MMmmmm!!"
    scene ep5_109 with dissolve
    mc "Stay still...."
    mc "Don't even think about doing something stupid."
    mc "I'm not going to harm you. You will be going home unharmed."
    mc "Just stand up after I take this handcuff off and walk by according to my commands."
    james "................"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_110 with dissolve
    james "Mmmmmm!!!!!"
    mc "................"
    james "Mmmmmmm!!!!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_111 with dissolve
    james "Mmmmm.....!"
    mc "*Sighs*......."
    mc "...Are you stupid?"
    mc "Did you really think of running away with your legs tied, and your eyes blindfolded?"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_112 with dissolve
    mc "...Well, I was going to free you up a bit."
    mc "But, since you tried to run away. I have no choice but to cuff your hands again."
    james "Mmmmmm!!!!"
    mc "Now, stand up and don't try to do anything stupid again."
    james "Mmmmmm!!!!"
    mc "Stop trying my patience...."
    james "............."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_113 with dissolve
    mc "....Go forward."
    james ".............."
    mc "Stay still. I'm going to take the handcuff off."
    james ".............."
    mc "Okay. Done."
    james "..............."
    mc "Hang on a sec...."
    scene black with dissolve
    scene ep5_114 with dissolve
    james "!!!!!!!!!"
    mc "Can you feel it?"
    james "MMmmmm!!! Mmmmm!!!"
    mc "Good. Now, listen carefully."
    mc "I'm going to leave you here."
    mc "Wait until the sound of my car has gone, then you're free to do whatever you want."
    mc "You got it?"
    james "Mmmmm!!!"
    scene ep5_115 with dissolve
    mc "Good. Now, walk forward...."
    mc "I don't need to remind you to not do anything stupid, right?"
    james "Mmmmm...!!"
    mc "Great. Keep walking. Slowly."
    u "Yeah. I'll let him leave just like that."
    u "I've got everything I needed from him. The video I just posted was already enough to make him suffer."
    u "He is surely going to lose his job, and people will keep bashing him nonstop."
    u "He'll probably end up in court if [krystal] wants to sue him."
    u "There is no need to do anything crazy. That would only make things more complicated."
    scene ep5_116 with dissolve
    u "Hm...?"
    u "Oh...."
    scene ep5_117 with dissolve
    u "Looks like he just pissed himself...."
    u "....Well, I don't blame him for that."
    mc "Alright, I'm going to leave now."
    mc "And don't ever think about looking for me later."
    mc "I might let you leave unharmed today, but if you keep going against me. I'll have no choice..."
    james "Mmmmmm!!!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_118 with dissolve
    james ".............."
    james ".............."
    scene ep5_119 with dissolve
    james "*Pants*....He really left me here...."
    james "*Pants*...That was so fucking scary... I thought I was going to be killed!"
    james "*Pants*...Where the hell am I...?"
    james "*Pants*...Fuck....He also took my phone...."
    scene ep5_120 with dissolve
    james "I don't know anymore!"
    james "Let's just leave this place first!"
    james "He might change his mind and come back to kill me!"
    james "I don't want to die!"
    stop music fadeout 3.0
    if ch2ep1helpalice == 1:
        jump ch2ep1alicemovingin
    else:
        scene black with dissolve
        u "...Alright, let's clean up everything..."
        jump ch2ep1sunnight
label ch2ep1alicemovingin:
    play music "sfx/Nextday.mp3" fadein 3.0
    $ bgm = "Bensound - Perception"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_121 with fade
    alice "[mc]!!!"
    mc "Hi, [alice]."
    kitty "Meow~!"
    mc "Have you finished packing-"
    scene ep5_122 with dissolve
    mc "-Ouch...!!"
    alice "*Giggles*...You really came!!"
    mc "Why are you so surprised?"
    mc "I told you, didn't I?"
    scene ep5_123 with dissolve
    alice "*Giggles*...Hehe... Yeah, you did."
    alice "*Giggles*...But, I'm still so happy to see you here!"
    alice "*Giggles*...It's been awhile since you moved out. Do you miss this place?"
    mc "...A little bit."
    alice "And yeah, I've finished packing my personal belongings."
    mc "I see..."
    scene ep5_124 with dissolve
    alice "But, I'm going to need your help carrying them down here."
    alice "Some of them are quite heavy."
    mc "Yeah, sure."
    mc "Let's take them down and put them in my car."
    alice "*Giggles*...Okay. Thanks!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_125 with dissolve
    mc "This box is the last one, right?"
    alice "Yeah, you're right."
    mc "Okay then. Let's get going."
    alice "Actually, can you wait for me here for a sec?"
    alice "I need to return my room key to the owner first."
    mc "Sure."
    alice "Can you also take [kitty] and put her in your car, please?"
    mc "Okay. Give her to me."
    alice "Thanks!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_126 with dissolve
    alice "I'm back!"
    alice "Let's go, [mc]!"
    mc "Wait... Did you forget something?"
    alice "Hm? What did I forget?"
    mc "I don't know. I'm checking."
    alice "I don't think so. I'm sure that I already put everything in the boxes."
    mc "Alright, let's go then..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_127 with dissolve
    mc "It's going to be a long trip."
    mc "You can take a nap if you want."
    alice "Thanks, but I've already had enough sleep."
    alice "I'll stay awake until we get there!"
    mc "Alright, that's your choice..."
    scene black with dissolve
    s "*A few hours later*........"
    scene ep5_128 with fade
    mc "Alright, I think this is it."
    alice "Yeah... I think so."
    u "Well, I can tell that [alice] is pretty well off."
    u "This room looks very good. I'm sure the rent is quite high."
    scene ep5_129 with dissolve
    alice "Thank you so much, [mc]."
    alice "At first, my parents were supposed to come help me, but they called me last night."
    alice "They told me that there was an emergency case last night."
    alice "And they had to prepare for an operation immediately."
    alice "It was going to be a very hard case, so they weren't sure if they could come help me or not."
    mc "I see... So that's why you called me so late last night."
    alice "Yeah..."
    scene ep5_130 with dissolve
    alice "It would be a very tough day for me if you weren't here."
    alice "I can't imagine carrying these boxes here all by myself."
    mc "...You're welcome."
    mc "Alright, I think I should leave now."
    scene ep5_131 with dissolve
    alice "Hm? Why so sudden?"
    mc "...Well, everything is all done. You don't need my help anymore."
    mc "So...."
    alice "Wait. I've just realised that we haven't eaten anything yet."
    alice "How about you eat something first before you leave?"
    scene ep5_130 with dissolve
    mc "..............."
    alice "I'll order food. It won't take long."
    mc "...Alright, if you say so."
    alice "*Giggles*...Lovely! I'll order a pizza. Is that okay for you?"
    mc "Yeah, pizza is fine."
    scene black with dissolve
    s "*An hour later*.........."
    scene ep5_132 with dissolve
    alice "Arrr... That was very delicious!"
    alice "I'm so full~"
    mc "Yeah, you should be full."
    mc "It was the largest size pizza, yet you took 4 pieces of it..."
    alice "*Giggles*...Hehe..."
    scene ep5_133 with dissolve
    alice "[mc]."
    mc "....Hm?"
    alice "I want to spend a little bit more time with you."
    alice "Let's watch a show together!"
    mc ".....Okay."
    alice "*Giggles*...Lovely!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_134 with dissolve
    alice "Is there a specific show that you want to watch?"
    mc "No, there isn't."
    alice "Okay then... How about we watch Fate: The Winx Saga?"
    alice "I saw its cover on Netflix yesterday. And it looked pretty interesting."
    mc "Yeah, let's watch it then."
    alice "*Giggles*...Okay!"
    scene ep5_135 with dissolve
    alice "Can I sit with you?"
    mc "Sure, but you don't have to ask me that."
    mc "This is your house. You can sit anywhere you want."
    alice "*Giggles*... Is that so?"
    scene ep5_136 with dissolve
    alice "Wow... She is very beautiful, isn't she?"
    alice "She must be the main character for sure."
    mc "I think so...."
    scene black with dissolve
    s "You spent your time watching it until the end of the first episode...."
    scene ep5_137 with dissolve
    alice "Well, that was such a very good first episode!"
    alice "Do you agree?"
    alice "I wish I could have magic power like them! That would be so cool!"
    mc "...Yeah, but the main character was a little bit annoying to me."
    alice "Really?! I thought I was the only one thinking that!"
    scene ep5_138 with dissolve
    kitty "Meow~!!"
    mc "!!!!"
    alice "Aw! [kitty]!"
    scene ep5_139 with dissolve
    alice "*Giggles*...She likes you, [mc]."
    mc "...But, how come?"
    mc "I didn't do anything to make her like me at all."
    alice "Hm...? What are you talking about?"
    alice "You did! Don't you remember?"
    scene ep5_140 with dissolve
    mc "Yeah? Since when did I do anything?"
    alice "Wow... You completely forgot about that."
    alice "Alright, let me remind you."
    mc "...Okay."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_141 with dissolve
    alice "It was one night during the first semester when we were freshmen..."
    alice "There was a very heavy rain that day."
    alice "I was on the way back to my room. Then, I heard a strange voice..."
    s "....Meow!"
    scene ep5_142 with dissolve
    alice "Then, I saw you standing still while carrying an umbrella."
    alice "You looked at the box at your feet."
    s "....Meow!"
    alice "I knew there was a cat inside that box after hearing its sound the second time."
    scene ep5_143 with dissolve
    alice "You kept standing still for some time."
    alice "You seemed to be talking with the cat because I heard your voice."
    alice "However, it was raining very hard so I couldn't hear everything you said."
    alice "But, I heard you say something like...'You're just like me when I was a kid.'"
    scene ep5_144 with dissolve
    alice "You left your umbrella on the ground to cover the box from the rain."
    alice "Then, you walked away just like that."
    alice "I was going to talk to you, but you walked too fast so that I couldn't catch up to you."
    scene ep5_145 with dissolve
    alice "So, I decided to go look at the box instead."
    alice "Then, I saw a kitten inside the box."
    alice "Yeah, it was [kitty]. She looked very sad back then."
    alice "I didn't know who left her like that. It was such a very bad thing to do."
    alice "Then, I decided to bring [kitty] back home with me."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_146 with dissolve
    alice "That's it. Do you remember it all now?"
    mc "...Yeah, I recall it."
    alice "Yeah, that's why she looks very happy every time she sees you."
    alice "I know it might sound exaggerated, but I think she remembers that you gave her your umbrella."
    scene ep5_147 with dissolve
    kitty "Meow!!"
    mc ".................."
    alice "*Giggles*...She can't stay still, right?"
    alice "Usually cats prefer to do nothing, and sleep almost the whole day."
    alice "But I'd say [kitty] is quite different. She is so playful."
    mc "Yeah, I can tell that..."
    alice ".............."
    scene ep5_148 with dissolve
    mc "...Hm? Why did you suddenly stand up?"
    alice "...[mc]."
    mc "...Yeah?"
    scene ep5_149 at eyesblink("Ch.2/Ep.1/Scenes/ep5_149.jpg", "Ch.2/Ep.1/Scenes/ep5_149_blink.jpg", 1) with dissolve
    alice "Since I just told you about how you met [kitty]..."
    alice "I also want you to know that that was the first time I met you as well."
    mc "I see...."
    alice "What you did for [kitty] was very heartwarming."
    alice "Not everyone would be willing to leave an umbrella for an abandoned cat in a situation like that."
    alice "Then later I was very happy to find out that we lived next door to each other."
    alice "....[mc]."
    mc "...Yes?"
    alice "I love you. I fell in love with you since that day...."
    mc "..................."
    alice "What do you think of me?"
    stop music fadeout 3.0
    menu:
        "I don't know. [alice2]":
            jump ch2ep1aliceh
        "You're my friend.":
            s "Are you sure that you want to do this?"
            s "This means you and [alice] will stay as friends only."
            menu:
                "Yes, I am.":
                    $ ch2ep1answeralice = 2
                    scene ep5_150_d1 at eyesblink("Ch.2/Ep.1/Scenes/ep5_150_d1.jpg", "Ch.2/Ep.1/Scenes/ep5_150_d1_blink.jpg", 1) with dissolve
                    mc "You're...."
                    mc "....my friend."
                    alice ".............."
                    alice "...Really?"
                    mc "Yeah..."
                    alice "....Am I nothing more than just a friend for you...?"
                    scene ep5_150_d2 with dissolve
                    mc "Yes, you understand it, right [alice]."
                    mc "I only think of you as a friend."
                    alice "................"
                    alice "...I thought you at least liked me a bit..."
                    alice "Since you took me to the theatre, and helped me move..."
                    mc "I did that because you asked me to..."
                    alice "...Alright, I understand it now...."
                    alice "You can leave now if you want. I won't take any more of your time here."
                    mc "Okay then...."
                    scene ep5_150_d3 with dissolve
                    mc "See you later, [alice]."
                    mc "Goodbye."
                    alice "................"
                    jump ch2ep1sunnight
                "On second thought":
                    jump ch2ep1aliceh
label ch2ep1aliceh:
    $ ch2ep1answeralice = 1
    $ alice_ch2_ep1 += 2
    $ alice_relationship += 2
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
    scene ep5_150_a1 at eyesblink("Ch.2/Ep.1/Scenes/ep5_150_a1.jpg", "Ch.2/Ep.1/Scenes/ep5_150_a1_blink.jpg", 1) with dissolve
    mc "............."
    alice "...Hm?"
    mc "....I don't know."
    alice "...What do you mean you don't know?"
    mc "...I can't think about something like that yet."
    mc "I'm doing something important right n-"
    scene ep5_150_a2 with dissolve
    alice "Shhh...."
    alice "Say nothing more...."
    mc "Hm...?"
    scene ep5_150_a3 with dissolve
    alice "*Kisses*....Mmmmmm....."
    alice "*Kisses*...Mmmm... It doesn't matter what... You think of me right now."
    alice "*Kisses*....You're surrounded by beautiful girls in that house."
    alice "*Kisses*....Mmmm... I can't just... Sit still doing nothing..."
    alice "*Kisses*....I've got to make my move..."
    mc ".............."
    scene ep5_150_a4 with dissolve
    alice "Hold on a sec...."
    scene ep5_150_a5 with dissolve
    alice "...Let's do it, [mc]."
    mc "...Do what?"
    alice "Do the things that women and men do when they're together alone...."
    mc "...Are you sure about that?"
    alice "Yeah. I've been waiting for this moment for a long time."
    mc "...Alright, if you say so."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_150_a6 with dissolve
    alice "*Giggles*...Hehe..."
    alice "*Giggles*....I can't believe this is actually happening..."
    mc ".............."
    alice "Alright, let's start by...."
    scene ep5_150_a7 with dissolve
    alice "...pleasing you first."
    alice "...Can I lick it?"
    mc "Sure..."
    scene ep5_150_a8 with dissolve
    show ch2ep1_lick with dissolve
    alice "*Licks*...So, this is how it tastes..."
    alice "*Licks*...Ahh... I like it...."
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_150_a9 with dissolve
            hide ch2ep1_lick with dissolve
    show ch2ep1_hj with dissolve
    alice "I think it's too big for my mouth. So, Let me use my hand instead...."
    alice "*Giggles*...To be honest, I wanted to suck it."
    alice "I've been practicing with a dildo, but yours is bigger than I expected."
    mc "Hm? You've been practicing with it?"
    alice "*Giggles*...Yeah, I used it when I was masturbating while thinking about you..."
    mc "...I never knew you were this nasty..."
    alice "*Giggles*...I know, right?"
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_150_a10 with dissolve
            hide ch2ep1_hj with dissolve
    alice "...Alright, I think you're ready."
    alice "Let's do it..."
    mc "...What about you?"
    alice "*Giggles*...Yeah, I'm ready. I'm already wet..."
    mc "Okay then..."
    scene ep5_150_a11 with dissolve
    alice "...Alright, I'm going to sit on your cock..."
    alice "Even though I've tried to do it with a dildo before, I'm going to do it slowly..."
    alice "Because you're really big..."
    scene ep5_150_a12 with dissolve
    alice "A...Ah!"
    alice "*Giggles*...Hehe... Finally, it went in..."
    mc "Only half way though...."
    alice "*Giggles*...Hehe... I'm going to start moving now."
    show ch2ep1_sit1 with dissolve
    alice "*Softly breathes*....Mmmmmm...."
    alice "*Softly breathes*....It feels so good...."
    alice "*Softly breathes*...Ahhh... Keep touching my boobs like that..."
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_150_a13 with dissolve
            hide ch2ep1_sit1 with dissolve
    show ch2ep1_sit2 with dissolve
    alice "*Moans*...Ahhh....Ahhh...."
    alice "*Moans*...This is so much better than a dildo...!"
    alice "*Moans*...Mmmm.... F...Faster... Faster, please!"
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_150_a14 with dissolve
            hide ch2ep1_sit2 with dissolve
    show ch2ep1_sit3 with dissolve
    alice "*Heavily breathes*....This is so good...!"
    alice "*Heavily breathes*...I can feel it keeps touching my womb...!"
    alice "*Heavily breathes*....Mmmm.... D...Don't stop...!"
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_150_a15 with dissolve
            hide ch2ep1_sit3 with dissolve
    mc "...Do you want to change positions?"
    alice "*Softly breathes*....Hm? What do you have in mind?"
    mc "Let's see...."
    scene black with dissolve
    alice "*Giggles*...Aw!"
    scene ep5_150_a16 with dissolve
    alice "*Giggles*.....Hehe... You want to do it like this?"
    mc "...Yeah. I have much more control in this position."
    alice "*Giggles*...Okay then, as you wish!"
    scene ep5_150_a17 with dissolve
    alice "*Giggles*...Ahh!"
    show ch2ep1_hold1 with dissolve
    alice "*Softly breathes*....Mmmmm....."
    alice "*Softly breathes*...Ahhh.... It feels so weird to do it like this..."
    mc "...You want to change back?"
    alice "*Softly breathes*...Mmmmm....No, it's okay. I'll get used to it soon..."
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_150_a18 with dissolve
            hide ch2ep1_hold1 with dissolve
    show ch2ep1_hold2 with dissolve
    alice "*Moans*....Ahhhh!....Ahhhh!"
    alice "*Moans*...Y..Yeah, keep moving your hips like that...!"
    $ renpy.pause()
    menu:
        "Next":
            scene ep5_150_a19 with dissolve
            hide ch2ep1_hold2 with dissolve
    show ch2ep1_hold3 with dissolve
    alice "*Heavily breathes*...Mmmmm!....Mmmmm!...."
    alice "*Heavily breathes*....I'm getting there...!"
    alice "*Heavily breathes*....Ahhh!...D..Don't stop..!"
    mc "I'm about to cum...."
    alice "*Heavily breathes*...Mmmmm...Me, too!"
    mc "Where do you want me to cum?"
    alice "*Heavily breathes*...Arrr... You can cum inside if you want. I'll take pills later...!"
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2ep1_hold3 with dissolve
            jump ch2ep1alicesit1
        "Slowest":
            hide ch2ep1_hold3 with dissolve
            jump ch2ep1alicehold1
        "Slower":
            hide ch2ep1_hold3 with dissolve
            jump ch2ep1alicehold2
        "Cum":
            jump ch2ep1aliceholdcum
label ch2ep1alicesit1:
    scene ep5_150_a12 with dissolve
    show ch2ep1_sit1 with dissolve
    $ renpy.pause()
    menu:
        "Hugging":
            hide ch2ep1_sit1 with dissolve
            jump ch2ep1alicehold1
        "Faster":
            hide ch2ep1_sit1 with dissolve
            jump ch2ep1alicesit2
        "Fastest":
            hide ch2ep1_sit1 with dissolve
            jump ch2ep1alicesit3
label ch2ep1alicesit2:
    scene ep5_150_a13 with dissolve
    show ch2ep1_sit2 with dissolve
    $ renpy.pause()
    menu:
        "Hugging":
            hide ch2ep1_sit2 with dissolve
            jump ch2ep1alicehold1
        "Slower":
            hide ch2ep1_sit2 with dissolve
            jump ch2ep1alicesit1
        "Faster":
            hide ch2ep1_sit2 with dissolve
            jump ch2ep1alicesit3
label ch2ep1alicesit3:
    scene ep5_150_a14 with dissolve
    show ch2ep1_sit3 with dissolve
    $ renpy.pause()
    menu:
        "Hugging":
            hide ch2ep1_sit3 with dissolve
            jump ch2ep1alicehold1
        "Slowest":
            hide ch2ep1_sit3 with dissolve
            jump ch2ep1alicesit1
        "Slower":
            hide ch2ep1_sit3 with dissolve
            jump ch2ep1alicesit2
label ch2ep1alicehold1:
    scene ep5_150_a17 with dissolve
    show ch2ep1_hold1 with dissolve
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2ep1_hold1 with dissolve
            jump ch2ep1alicesit1
        "Faster":
            hide ch2ep1_hold1 with dissolve
            jump ch2ep1alicehold2
        "Fastest":
            hide ch2ep1_hold1 with dissolve
            jump ch2ep1alicehold3
label ch2ep1alicehold2:
    scene ep5_150_a18 with dissolve
    show ch2ep1_hold2 with dissolve
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2ep1_hold2 with dissolve
            jump ch2ep1alicesit1
        "Faster":
            hide ch2ep1_hold2 with dissolve
            jump ch2ep1alicehold1
        "Fastest":
            hide ch2ep1_hold2 with dissolve
            jump ch2ep1alicehold3
label ch2ep1alicehold3:
    scene ep5_150_a19 with dissolve
    show ch2ep1_hold3 with dissolve
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2ep1_hold3 with dissolve
            jump ch2ep1alicesit1
        "Slowest":
            hide ch2ep1_hold3 with dissolve
            jump ch2ep1alicehold1
        "Slower":
            hide ch2ep1_hold3 with dissolve
            jump ch2ep1alicehold2
        "Cum":
            jump ch2ep1aliceholdcum
label ch2ep1aliceholdcum:
    mc "...I'm about to cum!"
    alice "*Heavily breathes*...Ahhh!...Me, too! Please, cum for me!"
    menu:
        "Cum inside":
            scene black with dissolve
            hide ch2ep1_hold3 with dissolve
            $ renpy.pause()
            scene ep5_150_a19_in1 with vpunch
            alice "Mmmmmm!! I'm cumming~!!"
            mc "Ugh..!"
            alice "Mmmmmm!!!!"
            scene black with dissolve
            $ renpy.pause()
            scene ep5_150_a19_in2 with dissolve
            mc "I'm pulling it out..."
            alice "*Pants*....Okay..."
        "Cum outside":
            scene black with dissolve
            hide ch2ep1_hold3 with dissolve
            $ renpy.pause()
            scene ep5_150_a19_out1 with vpunch
            alice "Mmmmmm!! I'm cumming~!!"
            mc "Ugh..!"
            scene ep5_150_a19_out2 with dissolve
            alice "Ahhhhh!!!!"
            mc "....Alright, you can get down now..."
            alice "*Pants*...Okay..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_150_a20 with dissolve
    alice "*Pants*....T..That was so good..."
    alice "*Pants*...I've never cum like that before..."
    mc "That's good for you..."
    alice "*Pants*...Hehe..."
    mc "...Alright, I think I should leave now."
    mc "I've already been here so long..."
    alice "*Pants*...Alright, if you say so..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_150_a21 with dissolve
    alice "Thanks again for today, [mc]!"
    mc "You're welcome."
    alice "Get home safe! Let's hang out together again!"
    mc "Sure..."
    alice "Goodbye~!"
    mc "Goodbye, [alice]."
    stop music fadeout 3.0
    $ renpy.end_replay()
    $ alice_ch2_ep1 += 2
    $ alice_relationship += 2
    jump ch2ep1sunnight
label ch2ep1freeday:
    scene black with dissolve
    s "You spent a whole day doing nothing special...."
    jump ch2ep1sunlatenight
label ch2ep1sunnight:
    scene black with dissolve
    $ renpy.pause()
    if nominatekrystal == 1 or ch2ep1helpalice == 1:
        u "Let's clean up everything before going back home..."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_151 with fade
        u "Okay... I'm home."
        u "Let's get inside..."
        scene black with dissolve
        $ renpy.pause()
        jump ch2ep1gethome
    else:
        scene black with dissolve
        $ renpy.pause()
        scene ep5_151 with fade
        u "Okay... I'm home."
        u "Let's get inside..."
        scene black with dissolve
        $ renpy.pause()
        jump ch2ep1gethome
label ch2ep1gethome:
    if nominatekrystal == 1:
        jump ch2ep1dinnerforkrystal
    else:
        jump ch2ep1sunlatenight
label ch2ep1dinnerforkrystal:
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_152 at eyesblink("Ch.2/Ep.1/Scenes/ep5_152.jpg", "Ch.2/Ep.1/Scenes/ep5_152_blink.jpg", 1) with dissolve
    rin "Finally! You're back!"
    mc "...Hm? What's happening?"
    rin "Hm? Didn't you read my message?"
    rin "We were waiting for you to come back so that we can have a dinner party!"
    mc "..Hm? For what occasion?"
    rin "What?! Didn't you hear the news today?"
    rin "Someone uploaded video of [lucy] admitting that she was the one behind all of [krystal]'s bad rumors."
    rin "So, [krystal] is all clean now! That's why we're having a party to congratulate her!"
    mc "Oh... I get it now..."
    scene ep5_153 with dissolve
    rin "Then, what are you waiting for?!"
    rin "Let's go!"
    rin "Everyone is waiting for you!"
    mc "But, I've already had dinner..."
    rin "It's alright! You don't have to eat if you don't want to."
    rin "You just need to be there for her. Come on! It won't take long!"
    mc "...Alright, if you say so..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_154 with dissolve
    rin "Guys! Look who is finally here~!"
    zeke "Oh! Where have you been dude! Hurry up, and take a seat already!"
    zeke "I'm starving to death right now..."
    krystal "*Smiles*... Please, take a seat, [mc]."
    scene ep5_155 with dissolve
    mc "You guys should've started eating without me."
    mc "You didn't have to wait for me, to be honest..."
    mc "What if I came back really late...?"
    krystal "Well, we might keep waiting for you until you got back."
    krystal "Everyone agreed to do that. They wanted all of us to have dinner together."
    zeke "Yeah... This is such a special occasion! How could we leave you out!?"
    mc "....Okay."
    scene ep5_156 with dissolve
    zeke "Okay then! Let's get started!"
    zeke "Congratulations, [krystal]!"
    zeke "You've been through a lot. But what happened in the past, stays in the past."
    zeke "I wish you all the best from now on!"
    mika "Me, too! I believe that you're going to shine brighter than before!"
    scene ep5_157 with dissolve
    rin "Congrats, [krystal]."
    rin "You're finally going to get what belongs to you back."
    yui "Well, you guys said everything I wanted to say..."
    yui "There is nothing left for me to say now, but congrats, [krystal]!"
    mc "...Congratulations."
    scene ep5_158 with dissolve
    krystal "*Giggles*...Hehe... Thank you very much, everyone."
    krystal "I don't know what to say..."
    krystal "Words can't describe how happy I am right now."
    krystal "I'm so lucky to have you guys here..."
    zeke "Alright, everyone! Cheers!"
    rin "Cheers!"
    scene black with dissolve
    s "*A few hours later*.........."
    scene ep5_159 with dissolve
    u "...Okay. It's getting late."
    u "Let's go take a shower, then go to bed..."
    $ renpy.sound.play("sfx/phone vibrating.mp3")
    s "*Phone vibrates*........"
    stop sound
    u "Hm...?"
    scene ep5_160 with dissolve
    $ faye_contact = True
    $ ch2ep1fayemessage = True
    $ newmessage = True
    $ faye_messages_show = True
    $ faye_newmessage = True
    $ phone_alert = True
    u "...I've got a new message. Let's see who sent it to me..."
    jump ch2ep1checkmessage
label ch2ep1checkmessage:
    if faye_newmessage == True:
        scene ep5_160 with vpunch
        u "I should check the message first."
        jump ch2ep1checkmessage
    elif faye_newmessage == False:
        scene ep5_159 with dissolve
        u "Alright, let's go take a shower..."
        jump ch2ep1sunlatenight
label ch2ep1sunlatenight:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    u "After finishing a shower, you went to bed straight away...."
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep4_3.mp3" fadein 3.0
    $ bgm = "LiQWYD - Birthday"
    scene ep5_161 with fade
    rin "Your outfit looks really cute today, [yui]."
    rin "I like it!"
    yui "Really? Thank you."
    rin "Where did you buy it?"
    yui "I bought it online from a shop on Instagram."
    yui "I can send you the link if you want."
    rin "Yes, please send it to me!"
    scene ep5_162 with dissolve
    zeke "Dude!!"
    mc "Hm...?"
    zeke "What a lovely morning, isn't it?!"
    mc "Arr... Yes, it is."
    zeke "Right?! The weather is so nice that I want to go jogging right now!"
    mc "............"
    scene ep5_163 with dissolve
    mc "....What's wrong with you, [zeke]?"
    zeke "Hm? What do you mean? I don't understand."
    mc "You look happier than ever..."
    zeke "Hahaha! Really?! I didn't know!"
    mc ".............."
    zeke "...Well, actually I think it's because [mika] finally accepted my feelings last night. Hehehe.."
    rin "W-What?!"
    scene ep5_164 with dissolve
    rin "What did you just say?! Can you say it again?"
    zeke "Err... I confessed to [mika] last night."
    rin "Really?!!"
    zeke "Hehehe... Yeah."
    zeke "At first she hesitated to accept my feelings, but I gave her my promise that I won't treat her the way that asshole did."
    zeke "Then, she was silent for a while, but she finally accepted my feelings."
    zeke "Today is our Day 1. Hehehe..."
    scene ep5_165 with dissolve
    rin "Congratulations!"
    rin "Wow! I'm so happy for you right now!"
    rin "Finally, your one-sided love story has finally ended!"
    rin "Mommy is so proud of you, son!"
    zeke "Hahaha! Thanks, mommy!"
    rin "It's been how many years now?"
    rin "Seven, right? You fell in love with her when you were at high school."
    scene ep5_166 with dissolve
    yui "Hm? Did all of you study together at the same high school?"
    rin "Hm? Didn't we already tell you guys about that?"
    yui "No, you didn't. As I can recall, right, [mc]?"
    mc "Yes, [yui] is right."
    rin "*Giggles*...Sorry. My bad."
    yui "No, you don't have to."
    yui "By the way, congrats, [zeke]."
    zeke "Hehehe... Thank you, [yui]."
    yui "It must feel really good to have someone you love who loves you back...."
    scene ep5_167 with dissolve
    rin "Alright, the elevator is here."
    rin "Let's go!"
    zeke "Sure!"
    jump ch2ep1part1end
label ch2ep1part1end:
    if nominatekrystal == 1:
        unknown "[mc]!"
        u "Hm....?"
        scene ep5_168 with dissolve
        mc "Oh... Hi, [faye]."
        faye "Good morning."
        scene ep5_169 with dissolve
        zeke "Good morning, [faye]."
        rin "Hello, [faye]!"
        yui "Er... Good morning."
        faye "Hi, everyone."
        faye "Can I borrow [mc] for a sec?"
        zeke "Oh! Sure!"
        faye "Thank you."
        scene ep5_170 with dissolve
        mc "...Is there something that you want from me?"
        faye "Have you already forgotten about that? It's about the advertising thing."
        faye "I want to talk about it with you."
        mc "...Right now? I thought we were going to talk about it with [eira], too."
        faye "That's right. We'll go see her together."
        mc "I see..."
        scene ep5_171 at eyesblink("Ch.2/Ep.1/Scenes/ep5_171.jpg", "Ch.2/Ep.1/Scenes/ep5_171_blink.jpg", 1) with dissolve
        faye "By the way,...."
        faye "...[mc]."
        mc "....Yeah?"
        faye "................."
        faye "Who are you exactly?"
        mc "................"
        scene ep5_172 with dissolve
        mc "...I don't understand your question."
        faye ".............."
        faye "The thing you just did... I don't think a mere programmer could have done it."
        faye "How did you manage to do it?"
        mc "...Well, by chance I have a friend who is good at things like that."
        mc "So, I asked him for some advice. Fortunately, it worked out well."
        scene ep5_173 with dissolve
        faye "Is that so?"
        mc "...Yeah."
        u "That was complete bullshit. I don't think she is really buying it."
        u "I can tell that by the way she's looking at me right now."
        faye "................."
        faye "*Sighs*....."
        scene ep5_174 with dissolve
        faye "...Well, let's just forget about it."
        faye "I don't care how you managed to get the video, or who you are."
        faye "As long as it's good for the sake of our company."
        mc "................."
        faye "Alright, let's get going."
        mc "Sure."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_175 with fade
        u "*Sighs*.... I was too careless. That was close."
        u "I should've expected her to suspect me. I mean... she was right."
        u "No ordinary programmer could have done what I did."
        scene ep5_176 with dissolve
        u "Well, I've got to give her some credit though."
        u "No one else suspected me at all. Everyone was busy feeling happy for [krystal]."
        u "[faye] was the only person who noticed."
        u "No doubt that's why she is the leader of this project..."
        u "Fortunately, she didn't insist on busting me."
        s "*Door opens*......."
        scene ep5_177 with dissolve
        eira "*Softly breathes*... I'm sorry. Am I late?"
        faye "No. You're actually right on time."
        faye "Please, take a seat."
        eira "*Softly breathes*... Thanks."
        scene ep5_178 with dissolve
        faye "Alright...."
        faye "First of all, I'd like to thank both of you."
        faye "You guys have done a very good job."
        eira "I give all the credit to [mc]. He was the one doing the most."
        scene ep5_179 with dissolve
        mc "Then, I have to give all the credit to you."
        mc "It would have been a lot harder without your help."
        faye "Yeah, [mc] already told me about what you did while we were on the way here."
        faye "Well done, [eira]."
        eira "...Thank you."
        scene ep5_180 with dissolve
        faye "Look. I just checked on social media."
        faye "People are now completely on [krystal]'s side."
        faye "They're asking for [lucy] to apologise to [krystal]."
        faye "And they're also shouting for [krystal] to come back on screen, too."
        faye "This is a very good sign for us."
        scene ep5_181 with dissolve
        eira "That means we can now hire [krystal] as our model, right?"
        faye "Of course."
        eira "Good. I was just asking in case you already found someone else."
        faye "*Sighs*... Well, actually I did."
        faye "I was on the verge of contacting [lucy] to take the job."
        eira "...Are you for real?"
        faye "I mean... even though she isn't as popular as [krystal] was, she is still more famous than anyone else on my list."
        faye "But, thanks to you guys, you just saved my life."
        faye "I don't want to imagine what would happen if the truth about her was revealed after she'd already become the model for our company."
        faye "I might have ended up losing my job."
        eira "...That would be really bad..."
        scene ep5_182 with dissolve
        faye "... Alright, [mc]."
        mc "...Yes?"
        faye "As I recall... you said that you know [krystal] personally, right?"
        mc "To be exact, we live in the same house."
        faye "...Really?"
        mc "Yeah, [rin], [yui], and [zeke] also live there, too."
        faye "I see... Can you give me her phone number?"
        faye "I'm going to call her right now."
        mc "Sure...."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_183 with dissolve
        faye "................"
        faye "She isn't answer my call..."
        mc "Maybe she doesn't pick up a call from a stranger?"
        mc "Do you want to use my phone instead?"
        faye "Well then, can you hand me your ph-"
        faye "-Oh wait. She's picking it up now."
        scene ep5_184 with dissolve
        faye "Hello. Is this [krystal]?"
        krystal "..............."
        krystal "...Yes, it is. Who are you?"
        faye "My name is [faye]. I'm the head of the Project management department of Xecon."
        krystal "....Xecon?"
        scene ep5_185 with dissolve
        krystal "*Mumbles to herself*...Isn't that the company everyone is working for?"
        mc "...[krystal]."
        krystal "Hm? That voice? Is that you, [mc]?"
        mc "Yeah, it's me."
        krystal "Oh... I understand the situation now."
        krystal "Is this about the modeling job that you told me about earlier?"
        scene ep5_186 with dissolve
        faye "Yes, you got it right."
        faye "I'm calling to ask if you would like to be the model for our upcoming project?"
        krystal "I would love to, but..."
        krystal "...Are you sure that you want me to do it?"
        krystal "I can tell how important this photo session is."
        krystal "Wouldn't it be better for you to find someone who is better than me?"
        krystal "I mean... it's been awhile since my last photo session..."
        krystal "I'm not sure if I can do it well."
        scene ep5_187 with dissolve
        faye "You don't need to worry about that. We've already chosen you."
        faye "There is no one who is as perfect for the job as you are."
        eira "Yeah..."
        krystal "Aw...."
        faye "So... What do you say?"
        krystal "If you put it like that....."
        krystal "...Okay. I'll do my best."
        faye "Great. You made the right choice, [krystal]."
        krystal "May I ask when the session is going to start?"
        faye "I know it's too hasty, but could you come to our offices tomorrow morning?"
        krystal "...Sure, I can do that."
        faye "Lovely. See you tomorrow, [krystal]."
        krystal "Okay. See you tomorrow."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_188 with dissolve
        faye "Alright, that's all for today."
        faye "Thank you for your help, [mc]."
        mc "You're welcome."
        faye "Are you guys busy this evening?"
        scene ep5_189 with dissolve
        mc "No, I'm not."
        eira "Me, neither. Why do you ask?"
        faye "Well, since everything is going pretty well, let me take you to dinner."
        faye "What do you say?"
        scene ep5_190 with dissolve
        mc "I'm fine with that."
        eira "Sure, [faye]."
        eira "Where are we going, then?"
        faye "Let's just think about that later."
        faye "Can we meet up in front of the building after work?"
        mc "Sure."
        eira "Anything you say."
        faye "Alright, see you guys this evening then. Goodbye."
        eira "See you, [faye]."
        $ ch2ep1fayeinvite = 1
        scene black with dissolve
        $ renpy.pause()
        if ep4wendylunch == 1:
            jump ch2ep1wendylunch
        else:
            jump ch2ep1part2evening

    else:
        scene black with dissolve
        s "You spent time working until lunch time..."
        scene black with dissolve
        $ renpy.pause()
        if ep4wendylunch == 1:
            jump ch2ep1wendylunch
        else:
            jump ch2ep1part2evening
label ch2ep1wendylunch:
    scene ep5_191 with fade
    u "Okay..."
    u "What am I going to eat today?"
    u "..............."
    u "...Hm?"
    scene ep5_192 with dissolve
    u "...Isn't that [wendy]?"
    u "Is she going for lunch alone?"
    u "...Well, I haven't decided what to eat yet."
    u "Let's just go ask her what she is up to."
    scene ep5_193 with dissolve
    mc "Hi, [wendy]."
    wendy "Eyaa!!!"
    mc "..............."
    mc "...Relax. It's me."
    scene ep5_194 with dissolve
    wendy ".............."
    wendy "...[mc]?"
    mc "...Yes. What was that reaction?"
    scene ep5_195 with dissolve
    wendy "N-Nothing! Hehehe...."
    mc "............."
    wendy "By the way, is there something that you want from me?"
    mc "Hm? Why do you ask that?"
    wendy "You know... usually, you would have ignored me and walked by."
    scene ep5_196 with dissolve
    wendy "But, you decided to come greet me first, so..."
    mc "...I saw you walking alone, so I decided to say hi. It's nothing special."
    mc "But, I think you're right. I do have something to ask."
    wendy "...Yeah? Ask away."
    mc "Where are you going to have lunch?"
    scene ep5_197 at eyesblink("Ch.2/Ep.1/Scenes/ep5_197.jpg", "Ch.2/Ep.1/Scenes/ep5_197_blink.jpg", 1) with dissolve
    wendy "................"
    mc "...What?"
    wendy "Nothing. You just asked a simpler question than I expected."
    wendy "I'm going to a cafe. I feel like having some bread and a cup of coffee for today's lunch."
    mc "Where's [elaine] by the way? Why are you going alone?"
    wendy "She's busy dealing with a troublesome customer now."
    mc "I see..."
    wendy "................."
    wendy "....[mc]."
    mc "...Yeah?"
    wendy "Would you like to come with me?"
    menu:
        "Go with her [wendy2]":
            $ ch2ep1wendylunch = 1
            $ wendy_ch2_ep1 += 2
            $ wendy_relationship += 2
            scene ep5_198_a1 at eyesblink("Ch.2/Ep.1/Scenes/ep5_198_a1.jpg", "Ch.2/Ep.1/Scenes/ep5_198_a1_blink.jpg", 1) with dissolve
            mc "Okay. I'll come with you."
            wendy "Really?!"
            mc "...Yeah."
            wendy "Alright, let's go then!"
            scene ep5_198_a2 with dissolve
            mc "....Why do you seem so happy?"
            wendy "*Giggles*...Nothing. I'm just happy to have some company."
            mc "...Is that so?"
            wendy "*Giggles*...Yep!"
            scene black with dissolve
            $ renpy.pause()
            scene ep5_198_a3 with fade
            wendy "Alright, here we are."
            wendy "Let's go in."
            mc "Yeah, let's go..."
            scene black with dissolve
            $ renpy.pause()
            scene ep5_198_a4 with fade
            wendy "This cake looks so delicious..."
            wendy "Let's see how it tastes..."
            wendy "................"
            scene ep5_198_a5 with dissolve
            wendy "....Hm?"
            scene ep5_198_a6 with dissolve
            wendy "What's wrong?"
            wendy "Why do you keep staring at me like that?"
            mc "Nothing..."
            mc "You really love eating dessert, don't you?"
            wendy "*Giggles*...Yeah! Eating desserts really helps boost my mood."
            $ wendy_like2 = "Desserts"
            mc "That means you were unhappy then? That's why you came here..."
            scene ep5_198_a7 with dissolve
            wendy "*Sighs*...Well, actually yes I was."
            mc "Why? What's wrong?"
            wendy "I don't know..."
            wendy "I feel like I've been followed recently, but every time I turned around to see who it was, I don't see anyone."
            wendy "That's why I was startled when you touched my shoulder from behind."
            mc "I see...."
            scene ep5_198_a8 with dissolve
            mc "...By the way, do you think it has something to do with that {b}thing{/b} you're doing?"
            wendy "....I don't think so."
            wendy "I always wear makeup and a wig to look like someone else."
            wendy "Plus, I've never told my personal information to anyone."
            mc "...Well, if you say so."
            mc "Then, do you have any enemies?"
            wendy "Enemies?"
            scene ep5_198_a9 with dissolve
            mc "I mean... is there anyone who wants to harm you."
            mc "Can you think of someone who would do something like that."
            wendy "...I don't know."
            wendy "I don't think I've ever done anything bad to anyone."
            wendy "...Yeah, I've never done that."
            scene ep5_198_a10 with dissolve
            wendy "Let's just stop talking about it."
            wendy "I might just be overthinking it. No one has been following me at all."
            mc "...Well, you might be right."
            mc "By the way, may I ask why you decided to do that stuff on twitter?"
            wendy "Why not? I love to take photos of myself."
            scene ep5_198_a11 with dissolve
            wendy "I'm just like everyone else, the only difference is that I prefer to reveal my body a little bit more."
            wendy "I think of it as a kind of art."
            wendy "But, I also have my standards..."
            wendy "Even though I show too much of my skin, it's still considered a non-nude photograph."
            wendy "However, there is no way I would go all naked for a photograph. That's unacceptable for me."
            menu:
                "Respect her hobby [wendy2]":
                    $ ch2ep1wendyhobby = 1
                    $ wendy_ch2_ep1 += 2
                    $ wendy_relationship += 2
                    scene ep5_198_a12 with dissolve
                    mc "That's good for you."
                    mc "I know that I'm not in a position to judge, so I respect your hobby."
                    mc "We all have different personal taste."
                    mc "You can do whatever you want as long as it doesn't harm anyone."
                    scene ep5_198_a12_a with dissolve
                    wendy "Right?!"
                    wendy "Wow... to be honest, I never expected you to understand me."
                    wendy "You impressed me, [mc]."
                    scene black with dissolve
                    $ renpy.pause()
                "I don't want to judge, but...":
                    $ ch2ep1wendyhobby = 2
                    scene ep5_198_a12 with dissolve
                    mc "I don't want to judge, but..."
                    mc "I don't think it's good for you to do things like that."
                    mc "I know that your hobby doesn't harm anyone, but it might harm yourself one day."
                    scene ep5_198_a12_d with dissolve
                    wendy "...How?"
                    mc "Social media is very dangerous nowadays, [wendy]. There are a lot of weird people using it."
                    mc "You never know what those crazy bastards are going to do."
                    mc "Plus, let's say you have kids in the future, what would they think about you when they know everything."
                    wendy ".............."
                    scene black with dissolve
                    $ renpy.pause()
            scene black with dissolve
            s "*About half an hour later*......."
            scene ep5_198_a13 with dissolve
            u "Alright, we've finished our lunch."
            u "Let's go back to the office...."
            scene black with dissolve
            $ renpy.pause()
            scene ep5_198_a14 with fade
            wendy "Okay... We're back!"
            wendy "Thank you for accompanying me today, [mc]."
            mc "You're welcome."
            wendy "We have about 15 minutes left. What are you going to do?"
            scene ep5_198_a15 with dissolve
            mc "I think I'll go right back to my department."
            mc "What about you?"
            wendy "I'll go to the library."
            mc "I see..."
            wendy "Alright, goodbye then. See you around, [mc]."
            mc "Okay. Bye."
            jump ch2ep1part2evening
        "Have lunch alone":
            $ ch2ep1wendylunch = 2
            scene ep5_198_d1 at eyesblink("Ch.2/Ep.1/Scenes/ep5_198_d1.jpg", "Ch.2/Ep.1/Scenes/ep5_198_d1_blink.jpg", 1) with dissolve
            mc "I'm sorry, but I don't feel like going to a cafe today."
            mc "I'm going to find something else to eat."
            wendy "Oh... Okay. Never mind then."
            mc "Alright then, please excuse me."
            scene ep5_198_d2 with dissolve
            mc "See you later, [wendy]."
            mc "Enjoy your lunch break."
            wendy "....You, too."
            jump ch2ep1part2evening

label ch2ep1part2evening:
    stop music fadeout 3.0
    scene black with dissolve
    s "You worked all afternoon until 5 p.m."
    scene ep5_199 with fade
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    mc "..............."
    yui "What are you looking at, [mc]?"
    mc "...Hm?"
    scene ep5_200 with dissolve
    yui "Let's go home. What are you waiting for?"
    if ch2ep1fayeinvite == 1:
        mc "Don't worry about me. You can leave first."
        yui "Hm? Why? Are you going somewhere?"
        mc "Yes, I'm going to have dinner with [faye] and [eira]."
        mc "[faye] wanted to buy us a meal for helping her out."
        yui "Okay. See you at home then."
        scene ep5_200_a1 with dissolve
        leo "[liam], do you have plans this weekend?"
        liam "...No, I don't. Why do you ask?"
        leo "I went on a blind date yesterday. There was a girl asking me to suggest someone to her."
        leo "So, I showed her your photo. She told me that she wanted to meet you."
        liam "Err... She really said that?"
        leo "Yeah. She was eager to meet you. What do you say?"
        liam "...If she really wanted to meet me, I can do that..."
        leo "Perfect!"
        joe "Hey! What about me?!"
        leo "I'm sorry, [joe]..."
        u "Alright, let's go meet up with [faye] and [eira]..."
        jump ch2ep1part2dinner
    else:
        mc "Oh... Okay."
        scene ep5_200_d1 with dissolve
        leo "[liam], do you have any plans this weekend?"
        liam "...No, I don't. Why do you ask?"
        leo "I went on a blind date yesterday. There was a girl asking me to suggest someone to her."
        leo "So, I showed her your photo. She told me that she wanted to meet you."
        liam "Err... She really said that?"
        leo "Yeah. She was eager to meet you. What do you say?"
        liam "...If she really wanted to meet me, I can do that..."
        leo "Perfect!"
        joe "Hey! What about me?!"
        leo "I'm sorry, [joe]..."
        jump ch2ep1part2night
label ch2ep1part2dinner:
    scene black with dissolve
    $ renpy.pause()
    scene ep5_200_a2 with dissolve
    faye "Okay... We're all here now."
    faye "Let's get going, then."
    eira "So, where are we going to go?"
    faye "Let's go to Secret Spot."
    u "...Hm? What secret spot is she talking about?"
    eira "Oh... I know that restaurant. Lovely, it's not too far from here."
    u "I see now... It's the name of the restaurant."
    faye "Yeah, we can easily walk there."
    scene black with dissolve
    s "About ten minutes later*........"
    scene ep5_200_a3 with dissolve
    faye "Okay. Here we are."
    faye "Please, take a seat and get comfortable."
    u "I remember this restaurant. I've been here twice."
    u "It's really crazy that I never knew its name until today..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_200_a4 with dissolve
    faye "You can order anything you want."
    eira "Anything?"
    faye "Yeah. Don't you remember? I told you this is my treat."
    eira "Oh... Yeah, you said that."
    scene ep5_200_a5 with dissolve
    faye "What about you, [mc]?"
    faye "What do you want to eat?"
    mc "A glass of beer and a basket of chicken wings will do."
    faye "Heh~ I can see that you have good taste in food."
    faye "A glass of beer and chicken wings are the best combination."
    mc "Absolutely..."
    scene black with dissolve
    s "*An hour and a half later*......"
    scene ep5_200_a6 with dissolve
    faye "Hm? Things that I like?"
    eira "Yeah. I've just realised that I know a very little about you despite working in the same company for more than a year."
    faye "Yeah... To think about that, you're right."
    faye "Um... I like working out. I always go to the gym whenever I have free time."
    $ faye_like1 = "Workouts"
    eira "I knew it! You look like someone who exercises a lot."
    eira "I mean... your legs look so slim."
    scene ep5_200_a7 with dissolve
    faye "*Giggles*...They don't look that good, to be honest. I still have a long way to go."
    eira "They already look perfect to me, [faye]. I really want my legs to look like that."
    faye "Would you like to join me at the gym, then?"
    eira "I don't know... I get tired very easily."
    eira "I mean... I can't even run for more than 10 minutes."
    faye "I know. It's hard at the beginning. Everyone has to start somewhere."
    faye "But, if you can break through it, the result is worth the effort."
    scene ep5_200_a6 with dissolve
    eira "...How old are you if I may ask...?"
    faye "I'm 26."
    $ faye_age = "26"
    eira "W-What?! Are you for real?"
    faye "Yes, I am. Why do you seem so surprised to know that?"
    eira "It's because you look a lot younger than your age...."
    faye "Aw... Thank you."
    eira "I thought you were younger than me, but you're actually a year ahead of me."
    faye "You still look so young, too."
    scene ep5_200_a8 with dissolve
    faye "What about you, [mc]?"
    mc "Hm...? what about me?"
    faye "I know very little about you as well."
    faye "Would you mind letting us know more about yourself?"
    mc "...Do I really have to?"
    eira "Yeah. I also want to know it, too."
    mc "................."
    scene ep5_200_a9 with dissolve
    mc "...Well, there is nothing much to tell..."
    mc "I graduated with a Bachelor's degree from a university in East Town."
    mc "Then, I moved here to work."
    faye "East Town, huh? I've been there once. It's a pretty good city."
    mc "Indeed it is..."
    faye "Then, how about your parents? How often do you go back to see them?"
    mc "I don't have any parents. I'm an orphan."
    faye ".............."
    eira "....[mc]...."
    faye "I'm so sorry."
    mc "Don't say that. It's not a big deal."
    scene ep5_200_a10 with dissolve
    eira "Hm...? Where are you going?"
    mc "Toilet. I'll be right back."
    eira "Oh... Wait a sec. I also need to go, too."
    eira "What about you, [faye]?"
    faye "I'm good. I'll wait here for you guys."
    eira "Okay..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_200_a11 with dissolve
    eira "...I'm sorry, [mc]."
    mc "Hm? For what?"
    eira "For earlier... It must've been so hard for you to answer such a question."
    mc "It's alright, [eira]. As I said, it wasn't a big deal."
    mc "It's quite a general question to ask someone. I don't blame [faye] for that."
    eira "How mature of you..."
    scene black with dissolve
    s "*A few minutes later*........."
    scene ep5_200_a12 with dissolve
    mc "Alright, let's get back to [faye]..."
    eira "[mc], wait..."
    mc "Hm? What's wrong?"
    eira "Look at our table."
    scene ep5_200_a13 with dissolve
    mc "Oh, I see now..."
    eira "What are those guys doing there?"
    mc "...I think they're trying to hit on [faye]."
    eira "Oh yeah, you're right..."
    scene ep5_200_a14 with dissolve
    man1 "Hey, beauty. What's your name?"
    man1 "Are you lonely? I saw your friend leaving. Do you want to hangout with us?"
    man2 "Yeah, it will be fun. We can have a couple of beers together."
    faye "................"
    man1 "Come on... Are you really not going to talk to us?"
    scene ep5_200_a15 with dissolve
    eira "What should we do, [mc]?"
    mc "..............."
    menu:
        "Interrupt them [faye2]":
            $ ch2ep1helpfaye = 1
            $ faye_ch2_ep1 += 2
            $ faye_relationship += 2
            mc "Wait for me here. I'll be right back."
            eira "Please, be careful, [mc]."
            eira "There are two of them."
            mc "Okay. I get it."
            scene black with dissolve
            $ renpy.pause()
            scene ep5_200_a15_a1 with dissolve
            mc "...Let's go, [faye]."
            man1 "(Hm...?)"
            man1 "(Why is this man here? I thought he had already left.)"
            faye "...Hang on a sec."
            scene ep5_200_a15_a2 with dissolve
            faye "Well, as you can see, I'm leaving now."
            faye "So, I can't hangout with you guys."
            faye "You should find another girl."
            man1 "It's alright. I understand that."
            man1 "Is he your boyfriend? I thought the other girl was his girlfriend, no?"
            scene ep5_200_a15_a3 with dissolve
            faye "Yeah, you got it right. He's my boyfriend."
            faye "I'm starting to feel sleepy, honey."
            faye "Let's leave."
            mc "..............."
            mc "....Okay."
            scene ep5_200_a15_a4 with dissolve
            man2 "Why did you let her go so easy, man?"
            man2 "It was so obvious that they weren't a real couple."
            man1 "Yeah, I know that."
            man1 "But, it's also obvious that she doesn't want to play with us, too."
            man1 "If a girl doesn't want to play with us, there is nothing you can do."
            man1 "Just better to let her go, and find another one."
            man2 "I see..."
            scene ep5_200_a15_a5 with dissolve
            faye "Sorry for earlier, [mc]."
            faye "Thank you for playing along with me."
            mc "It's all right. I'm happy to help."
            faye "*Sighs*...This kind of stuff will never stop happening to me."
            faye "I'm so sick of it."
            faye "Alright, can you please wait here for a sec."
            faye "I'm going to pay the check."
            eira "Yeah, sure. Go ahead."
        "Let [faye] deal with the situation":
            $ ch2ep1helpfaye = 2
            mc "I think [faye] can deal with them by herself."
            mc "Let's just wait for her here."
            eira "Are you sure that we don't need to help her?"
            mc "Yeah, I believe that she can take care of herself."
            eira "...Alright, but you need to help her if things go bad, okay?"
            mc "Of course, I will."
            scene ep5_200_a15_d1 with dissolve
            faye "*Sighs*............"
            man2 "Hm? Why did you sigh? What's wrong?"
            man2 "We're ready to listen to you. You can tell us everything."
            faye "(...Hm? [mc] and [eira] are back.)"
            scene ep5_200_a15_d2 with dissolve
            man1 "Hm...? Where are you going?"
            faye "I'm leaving. You better find another girl."
            man1 "Oh... Okay."
            scene ep5_200_a15_d3 with dissolve
            faye "Should we go now?"
            eira "Yeah, if that's what you want."
            faye "Alright, can you please wait here for a sec."
            faye "I'm going to pay the check."
            eira "Yeah, sure. Go ahead."
    scene ep5_200_a15_a6 with dissolve
    faye "By the way, how are you guys going to go home?"
    mc "I will take a bus."
    eira "There is no bus stop in front of my house. I can't go back home by bus."
    eira "So, I'm going to call an uber."
    faye "I can drive you home if you want."
    eira "Thank you, but I will just call an uber."
    eira "I don't want to bother you."
    faye "Alright, if you say so."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_201 with fade
    u "Alright, I'm home..."
    u "It's getting late. Let's go take a shower, then go to bed."
    unknown "Oh? You're finally back?"
    u "Hm...?"
    scene ep5_202 with dissolve
    mc "[krystal]? What are you doing down here so late at night?"
    krystal "I'm looking for something to eat. I'm kind of hungry now."
    mc "Hm? Didn't you have dinner yet?"
    krystal "I already had it, but I didn't eat much."
    scene ep5_203 with dissolve
    mc "I see..."
    krystal "Do you want to join me?"
    mc "No, thanks. I'm still full."
    mc "I'm also feeling a little bit sticky. I want to go take a shower."
    krystal "All good. I'll see you tomorrow then!"
    krystal "Goodnight, [mc]."
    mc "You, too."
    scene black with dissolve
    $ renpy.pause()
    s "*Half an hour later*........."
    jump ch2ep1part2night
label ch2ep1part2night:
    scene ep5_204 with fade
    u "Alright, my shower is done."
    u "Let's go to bed. I'm starting to feel sleepy now."
    if ep4rinkiss == 1:
        $ renpy.sound.play("sfx/door knocking.mp3")
        s "*Door knocks*......."
        u "Hm...?"
        scene ep5_205 with dissolve
        mc "Who's it?"
        rin "It's me. Can you open the door, please?"
        mc "[rin]?"
        mc "....Alright, hang on a sec."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_206 with dissolve
        mc "Hi."
        rin "Hey. How was your dinner?"
        rin "I heard that you went out to eat with [eira] and [faye]."
        mc "Well, it wasn't bad."
        rin "I see..."
        mc "By the way, what are you doing here this late at night?"
        scene ep5_207 at eyesblink("Ch.2/Ep.1/Scenes/ep5_207.jpg", "Ch.2/Ep.1/Scenes/ep5_207_blink.jpg", 1) with dissolve
        rin "Well....."
        rin "You know... It's been awhile since we spent time together."
        mc "And...?"
        rin "So, I want to ask if I can sleep here with you tonight..."
        menu:
            "Let her in [rin1]":
                $ ch2ep1rinvisit = 1
                $ rin_ch2_ep1 += 1
                $ rin_relationship += 1
                scene ep5_208_a1 at eyesblink("Ch.2/Ep.1/Scenes/ep5_208_a1.jpg", "Ch.2/Ep.1/Scenes/ep5_208_a1_blink.jpg", 1) with dissolve
                mc "Alright, come on in then."
                rin "Really? Can I really sleep here?"
                mc "Yeah, why not?"
                rin "*Giggles*...Lovely! Let's get inside then!"
                scene black with dissolve
                $ renpy.pause()
                scene ep5_208_a2 with dissolve
                mc "Goodnight, [rin]."
                rin "..............."
                rin "...You, too. Goodnight."
                scene ep5_208_a3 with dissolve
                mc "................"
                rin "................"
                mc "................"
                scene ep5_208_a4 with dissolve
                rin "..............."
                mc "..............."
                rin ".....[mc]. Are you still awake?"
                mc ".............."
                scene ep5_208_a5 with dissolve
                mc "....Yeah. Why?"
                rin "I know that I asked to sleep here with you."
                rin "But,...."
                scene ep5_208_a6 with dissolve
                rin "I don't want to sleep only..."
                rin "....You know what I'm saying, right...?"
                u "There is no way I didn't know that. She's clearly up to something."
                u "What should I do?"
                menu:
                    "[smgr2]Kiss her":
                        jump ch2ep1sexrin
                    "I'm really tired":
                        scene ep5_208_a6_d with dissolve
                        mc "I'm sorry, [rin]."
                        mc "I'm very tired today. I want to sleep."
                        rin "....Okay. I get it."
                        rin "Let's just sleep then..."
                        $ ch2ep1rinsex = 2
                        jump ch2ep1part2nextmorning
            "Not today":
                scene ep5_208_d at eyesblink("Ch.2/Ep.1/Scenes/ep5_208_d.jpg", "Ch.2/Ep.1/Scenes/ep5_208_d_blink.jpg", 1) with dissolve
                mc "Not today, [rin]."
                rin "Why....?"
                mc "I'm very tired. I want to rest."
                rin "Oh, okay... I get it."
                mc "Sorry."
                rin "It's okay. You don't have to feel sorry."
                rin "Alright, I won't bother you anymore then."
                rin "Have a good rest, [mc]."
                mc "Goodnight, [rin]."
                $ ch2ep1rinvisit = 2
                jump ch2ep1part2nextmorning
    else:
        jump ch2ep1part2nextmorning
label ch2ep1sexrin:
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
    scene ep5_208_a6_a1 with dissolve
    rin "!!!!!"
    play music "sfx/ep4_2.mp3" fadein 3.0
    $ bgm = "Leonell Cassio - Woho, I Thought It Be Me & You (ft. Lily Hain)"
    mc "*Kisses*....."
    rin "(...I didn't expect him to suddenly kiss me like this...)"
    rin "*Kisses*....Mmmm... [mc]...."
    scene ep5_208_a6_a2 with dissolve
    rin "(...Hm? Is he trying to pull my top up?)"
    rin "(...I've never seen him like this. He's more aggressive than ever.)"
    rin "(But, this is good. I like it.)"
    rin "(His thing... I can feel it's starting to get hard...)"
    scene ep5_208_a6_a3 with dissolve
    rin "*Kisses*....[mc]....Mmmm..."
    rin "*Kisses*...Mmmm... Wait a sec..."
    mc "*Kisses*....Hm?"
    rin "*Kisses*....Let me take everything off..."
    mc "*Kisses*....Okay."
    scene black with dissolve
    $ renpy.pause()
    rin "...Okay. I'm ready."
    scene ep5_208_a6_a4 with dissolve
    rin "...Could you please lick it for me?"
    rin "I want you to make me feel good."
    mc "...Alright."
    scene ep5_208_a6_a5 with dissolve
    show ch2_lick_rin1 with dissolve
    window hide
    rin "*Softly breathes*....Arrr....."
    $ renpy.pause()
    menu:
        "Next":
            rin "*Softly breathes*....Mmmm....Faster..."
            rin "*Softly breathes*....Arrr....Do it faster, please."
    scene ep5_208_a6_a6 with dissolve
    hide ch2_lick_rin1
    show ch2_lick_rin2 with dissolve
    window hide
    rin "*Softly breathes*....Mmmm... Y..Yeah... Keep licking it like that...."
    $ renpy.pause()
    menu:
        "Next":
            rin "*Softly breathes*....Arrr... That's enough, [mc]."
            rin "*Softly breathes*....Let me make you feel good, too."
            mc "*Licks*....Okay."
    scene black with dissolve
    hide ch2_lick_rin2
    $ renpy.pause()
    scene ep5_208_a6_a7 with dissolve
    rin "*Smiles*....As I remember, It's been awhile since I sucked it for you last time, right?"
    mc "...I guess so."
    rin "*Smiles*...Let me do it today then!"
    scene ep5_208_a6_a8 with dissolve
    show ch2_bj_rin1 with dissolve
    window hide
    rin "*Sucks*....Mmmmm... It's so...big...."
    $ renpy.pause()
    menu:
        "Next":
            rin "*Sucks*....Mmmm... Is it okay if I go faster?"
            mc "....Sure. Go ahead."
    scene ep5_208_a6_a9 with dissolve
    hide ch2_bj_rin1
    show ch2_bj_rin2 with dissolve
    window hide
    rin "*Sucks*.....Mmmmm..... It tastes so good...."
    $ renpy.pause()
    menu:
        "Next":
            rin "*Sucks*.....Mmmmmm....Mmmmmm....."
    scene ep5_208_a6_a10 with dissolve
    hide ch2_bj_rin2
    show ch2_bj_rin3 with dissolve
    window hide
    rin "*Sucks*....Mmmmm!...Mmmmmm!"
    mc "...Yeah, keep sucking it like that..."
    $ renpy.pause()
    menu:
        "Next":
            rin "*Sucks*.....Mmmmm.... It's going...in so deep...in my mouth."
            mc "...Hang on a sec."
    scene black with dissolve
    hide ch2_bj1_rin3
    scene ep5_208_a6_a11 with dissolve
    rin "What's wrong? Why did you tell me to stop?"
    mc "I'm ready. Let's do it."
    rin "*Giggles*...Okay. How do you want to do it?"
    mc "I want you to get up, and sit on my lap."
    rin "As you wish!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_208_a6_a12 with dissolve
    rin "*Smiles*....Like this?"
    mc "...Yeah, that's right."
    mc "Now, I want you to slowly put it in."
    rin "*Giggles*....Okay."
    scene ep5_208_a6_a13 with dissolve
    rin "*Softly breathes*....Arrr...It's in..."
    mc "You can start moving now."
    rin "*Softly breathes*...Okay..."
    show ch2_sit_rin1 with dissolve
    window hide
    rin "*Softly breathes*....Arrrr... It's so big inside me..."
    $ renpy.pause()
    menu:
        "Next":
            rin "*Softly breathes*...Mmmm... How is it? Am I doing good?"
            mc "...You should go a little bit faster."
            rin "*Softly breathes*....Whatever you say..."
    scene ep5_208_a6_a14 with dissolve
    hide ch2_sit_rin1
    show ch2_sit_rin2 with dissolve
    window hide
    rin "*Softly breathes*....Mmmmm.... Like this?"
    mc "Yeah, keep moving your hips like that."
    $ renpy.pause()
    menu:
        "Next":
            rin "*Moans*....Ahhh!... This feels so good!"
            mc "Shhhh....."
            rin "*Softly breathes*....Mmmmm... S-Sorry..."
    scene ep5_208_a6_a15 with dissolve
    hide ch2_sit_rin2
    show ch2_sit_rin3 with dissolve
    window hide
    rin "*Heavily breathes*....Mmmmm....Mmmmmm...."
    $ renpy.pause()
    menu:
        "Next":
            rin "*Heavily breathes*....I...I'm starting to feel tired, [mc]..."
            mc "Okay then, let's change position."
            mc "I will be the one doing it now."
            rin "*Heavily breathes*....O...Okay."
    scene black with dissolve
    hide ch2_sit_rin3
    scene ep5_208_a6_a16 with dissolve
    mc "Alright,.... I'm going to put it in."
    scene ep5_208_a6_a17 with dissolve
    rin "*Softly breathes*...A-Ah~!"
    show ch2_doggy_rin1 with dissolve
    window hide
    rin "*Softly breathes*...Mmmm....[mc]..."
    mc "...Yeah?"
    rin "*Softly breathes*....Ahhh... Do we really...need to do it like this...?"
    rin "*Softly breathes*....Mmmmm..... I feel so...embarrassed..."
    mc "...Do you want to change to another position then?"
    rin "*Softly breathes*......It's...alright.... Let's just keep doing it this way..."
    mc "...Okay."
    $ renpy.pause()
    menu:
        "Next":
            mc "I'm going to move faster...."
    scene ep5_208_a6_a18 with dissolve
    hide ch2_doggy_rin1
    show ch2_doggy_rin2 with dissolve
    window hide
    rin "*Softly breathes*....Mmmmm!....Mmmmm...!"
    rin "*Softly breathes*....Ahhh... This feels too...good...!"
    rin "*Softly breathes*...Mmmmm... You're...driving me crazy, [mc]..."
    $ renpy.pause()
    menu:
        "Next":
            rin "*Softly breathes*....Ahhhh... F..Faster... Faster, please!"
    scene ep5_208_a6_a19 with dissolve
    hide ch2_doggy_rin2
    show ch2_doggy_rin3 with dissolve
    window hide
    rin "*Heavily breathes*....Mmmmmm!!... Yeah, that's right...!"
    mc "Shhh... Lower your voice."
    rin "*Heavily breathes*....Mmmmm.... B-But, it's hard to...!"
    rin "*Heavily breathes*....Mmmmm!... I...I'm about to cum soon!"
    mc "...Me, too."
    menu:
        "Sitting":
            hide ch2_doggy_rin3
            jump ch2rinsit1
        "Slowest":
            hide ch2_doggy_rin3
            jump ch2rindoggy1
        "Slower":
            hide ch2_doggy_rin3
            jump ch2rindoggy2
        "Cum":
            jump ch2rindoggybeforecum
label ch2rinsit1:
    scene ep5_208_a6_a13 with dissolve
    show ch2_sit_rin1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Legup doggy":
            hide ch2_sit_rin1
            jump ch2rindoggy1
        "Faster":
            hide ch2_sit_rin1
            jump ch2rinsit2
        "Fastest":
            hide ch2_sit_rin1
            jump ch2rinsit3
label ch2rinsit2:
    scene ep5_208_a6_a14 with dissolve
    show ch2_sit_rin2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Legup doggy":
            hide ch2_sit_rin2
            jump ch2rindoggy1
        "Slower":
            hide ch2_sit_rin2
            jump ch2rinsit1
        "Faster":
            hide ch2_sit_rin2
            jump ch2rinsit3
label ch2rinsit3:
    scene ep5_208_a6_a15 with dissolve
    show ch2_sit_rin3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Legup doggy":
            hide ch2_sit_rin3
            jump ch2rindoggy1
        "Slowest":
            hide ch2_sit_rin3
            jump ch2rinsit1
        "Slower":
            hide ch2_sit_rin3
            jump ch2rinsit2
label ch2rindoggy1:
    scene ep5_208_a6_a17 with dissolve
    show ch2_doggy_rin1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2_doggy_rin1
            jump ch2rinsit1
        "Faster":
            hide ch2_doggy_rin1
            jump ch2rindoggy2
        "Fastest":
            hide ch2_doggy_rin1
            jump ch2rindoggy3
label ch2rindoggy2:
    scene ep5_208_a6_a18 with dissolve
    show ch2_doggy_rin2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Sitting":
            hide ch2_doggy_rin2
            jump ch2rinsit1
        "Slower":
            hide ch2_doggy_rin2
            jump ch2rindoggy1
        "Faster":
            hide ch2_doggy_rin2
            jump ch2rindoggy3
label ch2rindoggy3:
    scene ep5_208_a6_a19 with dissolve
    show ch2_doggy_rin3 with dissolve
    window hide
    menu:
        "Sitting":
            hide ch2_doggy_rin3
            jump ch2rinsit1
        "Slowest":
            hide ch2_doggy_rin3
            jump ch2rindoggy1
        "Slower":
            hide ch2_doggy_rin3
            jump ch2rindoggy2
        "Cum":
            jump ch2rindoggybeforecum
label ch2rindoggybeforecum:
    mc "...I'm almost there."
    rin "*Heavily breathes*...Mmmm... Me, too! Let's cum together!"
    mc "...Where do you want me to cum?"
    rin "*Heavily breathes*....A...Anywhere you want...!"
    if ch2ep1fayeinvite == 1:
        menu:
            "Cum inside":
                $ ch2ep1rincum = 1
                jump ch2krystalpeek
            "Cum outside":
                $ ch2ep1rincum = 2
                jump ch2krystalpeek
    else:
        menu:
            "Cum inside":
                $ ch2ep1rincum = 1
                jump ch2rindoggycum
            "Cum outside":
                $ ch2ep1rincum = 2
                jump ch2rindoggycum
label ch2krystalpeek:
    scene black with dissolve
    hide ch2_doggy_rin3
    $ renpy.pause(3, hard=True)
    scene ep5_208_a6_a20 with dissolve
    krystal "(To think about it, I still have no clue about what to do tomorrow...)"
    krystal "(I'll go talk to [mc] about it.)"
    krystal "(But, it's pretty late at night already. I hope he's still awake.)"
    scene ep5_208_a6_a21 with dissolve
    krystal "(Hm...? The door isn't fully closed?)"
    krystal "(I guess he's still awake then.)"
    krystal "(Also, I can even hear some voices coming from there.)"
    scene ep5_208_a6_a22 with dissolve
    krystal "(I don't know what that sound is though, I can't hear it very clearly...)"
    krystal "(Let's just knock on the door before going i-)"
    scene ep5_208_a6_a23 with dissolve
    krystal "(!!!!)"
    krystal "(Oh my god...!)"
    scene ep5_208_a6_a24 with dissolve
    show ch2_doggy_rin4 with dissolve
    rin "*Heavily breathes*...Mmmm....Almost there...!"
    krystal "(...Isn't that [rin]?!)"
    krystal "(I can't believe my eyes...! They're really having sex!)"
    krystal "(I never knew they were dating...!)"
    jump ch2rindoggycum
label ch2rindoggycum:
    if ch2ep1rincum == 1:
        scene black with dissolve
        hide ch2_doggy_rin3
        hide ch2_doggy_rin4
        scene ep5_208_a6_a25_in1 with vpunch
        mc "I'm cumming!"
        rin "*Heavily breathes*...M-Me, too. I can't hold it anymore!"
        rin "*Heavily breathes*....Mmmmmmmm!!!!"
        scene ep5_208_a6_a25_in2 with dissolve
        rin "*Pants*....Ahh...Hehe... I can feel...your hot semen inside me..."
        rin "*Pants*....You came...quite a lot... I can't take it all..."
        mc "*Pants*....Yeah, I can tell..."
    elif ch2ep1rincum == 2:
        scene black with dissolve
        hide ch2_doggy_rin3
        hide ch2_doggy_rin4
        scene ep5_208_a6_a25_out1 with vpunch
        mc "I'm cumming!"
        rin "*Heavily breathes*...I can't hold it anymore!"
        rin "*Heavily breathes*....Mmmmmmmm!!!!"
        scene ep5_208_a6_a25_out2 with vpunch
        rin "*Pants*...Hehe... You came...all over me..."
        mc "*Pants*...My bad."
        rin "*Pants*...All good. I don't...blame you...for that..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_208_a6_a26 with dissolve
    rin "*Giggles*...There is still some of your semen left..."
    mc "...Yeah."
    rin "*Licks*...Let me clean it for you."
    scene ep5_208_a6_a27 at eyesblink("Ch.2/Ep.1/Scenes/ep5_208_a6_a27.jpg", "Ch.2/Ep.1/Scenes/ep5_208_a6_a27_blink.jpg", 1) with dissolve
    rin "*Giggles*...Hehe... It tastes quite good. I like it."
    mc "Really?"
    rin "*Giggles*...Yeah! It tastes a lot better than I thought."
    mc "Good for you then."
    rin "*Giggles*.... By the way, that was very good, [mc]."
    rin "*Giggles*...Hehe... Let's do it again soon!"
    mc "...Sure."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_208_a6_a28 with dissolve
    mc "...Hm? Where are you going?"
    rin "I need to clean myself up. I'm going to take a shower real quick."
    rin "Don't fall asleep just yet, okay? I'll be back."
    mc "...Alright."
    if ch2ep1fayeinvite == 1:
        scene ep5_208_a6_a29 with dissolve
        krystal "(She's about to come out!)"
        krystal "(I need to go back to my room ASAP!)"
        krystal "(I can't let them know that I saw what they were doing.)"
        scene ep5_208_a6_a30 with dissolve
        s "*Door opens*......"
        rin "(Hm...? I didn't know that the door wasn't completely closed.)"
        rin "(I forgot to check it when I followed [mc] into the room...)"
        rin "(I hope no one saw what [mc] and I did....)"
        scene black with dissolve
        $ renpy.pause()
        scene ep5_208_a6_a31 with dissolve
        krystal "(*Sighs*...That was close.)"
        krystal "(I almost got caught watching them.)"
        krystal "(Things would be so messed up if I did.)"
        scene ep5_208_a6_a32 with dissolve
        krystal "(Anyway, I still can't believe what I just witnessed.)"
        krystal "(I always thought that [mc] was single, but I was obviously wrong.)"
        krystal "(Wait....)"
        scene ep5_208_a6_a33 with dissolve
        if ch2ep1krystalkiss == 1:
            krystal "(If he's dating [rin], then why did he do that with me...?)"
            krystal "(I know that I was the one who made the first move, but still...)"
            krystal "(Why didn't he reject me?)"
            krystal "(I'm so confused now....)"
        else:
            krystal "(Everything is crystal clear now.)"
            krystal "(He's dating [rin]. That's why he rejected me last time....)"
            krystal "(When I think about it carefully, the way [rin] looks at [mc] was different from when she looked at [zeke]."
            krystal "(I should've noticed that earlier...)"
    scene black with dissolve
    $ renpy.pause()
    $ renpy.end_replay()
    $ ch2ep1rinsex = 1
    $ rin_ch2_ep1 += 3
    $ rin_relationship += 3
    jump ch2ep1part2nextmorning
label ch2ep1part2nextmorning:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ch1ep2.mp3" fadein 3.0
    $ bgm = "Bensound - Little Idea"
    s "*Many hours later*........."
    scene ep5_209 with dissolve
    $ renpy.sound.play("sfx/Clock alarm.mp3")
    s "*Alarm clock*............"
    stop sound
    scene ep5_210 with dissolve
    u "....Hm? It's morning already?"
    u "................"
    if ch2ep1rinsex == 1:
        scene ep5_211 with dissolve
        u "[rin] has already left..."
        u "I guess she left very early in the morning, so no-one would see her."
    u "...Alright, let's get up and go take a shower."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_212 with dissolve
    u "Okay. I've finished dressing."
    u "Let's go have breakfast in the kitchen."
    u "I wonder if everyone is there..."
    if ch2ep1fayeinvite == 1:
        unknown "...Yes!"
        u "Hm...?"
        scene ep5_213 with dissolve
        zeke "That's what you deserve, you crazy bitch!"
        mika "Hey. Language."
        zeke "Haha... I'm sorry. I was too excited."
        mika "*Sighs*... Well, I can't blame you for that though."
        zeke "Right?"
        u "Oh. It's [zeke] and [mika]. They're watching the news."
        u "I wonder what news it is..."
        scene ep5_214 with dissolve
        u "Oh... It's about [lucy]."
        rp "It's been a couple of days since [lucy] locked herself in the house."
        rp "People are now very angry at her. They're yelling and shouting for her to come out."
        rp "We also still haven't heard anything from her company."
        rp "Plenty of people are thinking that the company has already abandoned [lucy]."
        rp "That's it for today. Thank you for watching."
        scene ep5_215 with dissolve
        rp "And don't forget to hit the like and subscribe buttons to stay updated with us, FCK News."
        zeke "Hm...?"
        scene ep5_216 with dissolve
        zeke "Good morning, [mc]."
        mc "What's up."
        mika "Hello, [mc]."
        zeke "Since when have you been here? I didn't notice you at all."
        mc "I just got here a moment ago."
        zeke "I see...."
        scene ep5_217 with dissolve
        mc "Have you already finished your breakfast?"
        zeke "Yeah. We had it pretty early today."
        zeke "Are you heading to the kitchen?"
        mc "Yes, I'm going to get a cup of coffee."
        zeke "[rin] and [yui] are also there. They're having breakfast, too."
        mc "I see...."
        zeke "Oh-!"
        scene ep5_218 with dissolve
        zeke "Hello, [krystal]."
        mika "Good morning, [krystal]."
        krystal "Good morning, everyone!"
        zeke "Are you going somewhere? You're dressed nicely today."
        krystal "Oh? Didn't [mc] already tell you guys about it?"
        zeke "Hm? What do you mean?"
        krystal "I'm going with you guys to your company today."
        krystal "I was asked to be a model for a photo shoot."
        zeke "Really? Wow! Good for you!"
        if ch2ep1rinsex == 1:
            scene ep5_219_a1 with dissolve
            mc "Good morning, [krystal]."
            krystal "!!!!"
            krystal "G-Good morning, [mc]..."
            mc "Are you ready for today?"
            krystal "Y-Yes, I am...."
            scene ep5_219_a2 with dissolve
            mc "Hm...? Where are you hurrying off to?"
            krystal "I-I'm very hungry. L-Let's talk later, okay?!"
            krystal "(Argh... This is not good! I keep thinking about last night. I need to calm myself ASAP...)"
            mc "Oh... Okay."
            u "What's wrong with her? She's acting so weird today."
            u "I feel like she's trying to avoid me. Very hungry, huh? No one will believe that."
            scene ep5_219_a3 with dissolve
            zeke "Hahahaha! Look at her running!"
            zeke "She must be really hungry like she said. I believe it!"
            mika "*Giggles*....She's so cute..."
            u "...................."
            u "*Sighs* These people...."
        else:
            scene ep5_219_d1 with dissolve
            mc "Good morning, [krystal]."
            krystal "Oh! I didn't realise you were here, too."
            krystal "Good morning, [mc]."
            mc "Are you ready for today?"
            krystal "Of course, I am!"
            mc "That's good...."
            krystal "Did you have breakfast yet?"
            mc "Not yet. I'm about to go have it."
            scene ep5_219_d2 with dissolve
            krystal "Then, let's go together. I'm going to the kitchen, too."
            mc "Sure."
            zeke "Enjoy your breakfast."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_220_a1 with fade
        rin "Good luck on the photo shoot, [krystal]."
        yui "I was very happy to hear that you were going to come with us today."
        yui "You deserve this opportunity. I wish you all the best, [krystal]."
        zeke "If you need help, don't hesitate to call any of us, okay?"
        krystal "Aw... Thank you, everyone. You're so nice to me."
        scene ep5_220_a2 with dissolve
        mc "Let's go, [krystal]."
        mc "It's about time. They are probably waiting for us."
        krystal "Oh! Okay!"
        scene ep5_220_a3 with dissolve
        krystal "Goodbye, everyone."
        krystal "See you around."
        rin "Good luck!"
        yui "*Sighs* I wish I could go with you, but never mind."
        yui "Do your best, [krystal]! Fighting!"
        scene black with dissolve
        $ renpy.pause()
        scene ep5_220_a4 with fade
        sally "O-Oh! Here they come!"
        mc "There they are..."
        krystal "There are quite a lot of people..."
        mc "Yeah, all of them are involved in what we're going to do."
        mc "Don't worry. They're all nice people."
        scene ep5_220_a5 with dissolve
        mc "Alright, I've brought her here."
        faye "Well done, [mc]. Good morning, [krystal]."
        faye "Welcome to Xecon."
        krystal "Thank you. You are...?"
        scene ep5_220_a6 with dissolve
        faye "I'm [faye]. I'm the one who called you yesterday."
        krystal "Oh. I remember that."
        krystal "Hello, [faye]. I'm [krystal]. Nice to meet you."
        faye "Nice to meet you, too."
        faye "You can take off that mask and hat if you want."
        faye "It's safe to do so. There are no reporters here."
        krystal "Okay. Hang on a sec..."
        scene ep5_220_a7 with dissolve
        krystal "*Smiles* This is much more comfortable!"
        krystal "I'm sorry. I have to wear them to avoid being noticed."
        faye "There is no need to apologize. We understand."
        krystal "*Giggles* Thank you."
        scene ep5_220_a8 with dissolve
        faye "Alright, let me introduce everyone."
        faye "This is [eira] and [sally]."
        eira "I'm [eira]. It's my pleasure to meet you."
        sally "You look as beautiful as you've always been, [krystal]!"
        sally "Oh! I'm [sally], by the way."
        krystal "*Giggles* Thanks, [sally]. Nice to meet you, too, [eira]."
        scene ep5_220_a9 with dissolve
        faye "[eira] is an expert in marketing."
        faye "She was the one who suggested your name to me."
        krystal "Aw... Thank you for giving me this opportunity, [eira]."
        eira "...You deserve it. You don't have to thank me."
        u "I already saw her when I walked into the room, but..."
        u "Who is this woman? I can't recall ever seeing her at the company before."
        scene ep5_220_a10 with dissolve
        u "Hm...?"
        u "Oh, she's looking back at me."
        scene ep5_220_a11 with dissolve
        unknown "*Winks*.........."
        u "Wait... What? Why did she do that?"
        faye "There is one more person I'd like to introduce."
        scene ep5_220_a12 with dissolve
        faye "This is [allison]. She's our photographer for today."
        allison "Let's do our best, [krystal]."
        krystal "Nice to meet you, [allison]. Please, take care of me."
        faye "You guys might never have seen her before, because she never shows herself in public."
        faye "But, don't worry. She's a very good photographer."
        faye "She usually doesn't accept any projects, but fortunately, I'm her close friend."
        faye "{b}Wisteria{/b} is her artistic name."
        scene ep5_220_a13 with dissolve
        krystal "W-What?! Really?!"
        krystal "Are you really that Wisteria?"
        allison "*Smiles* Yes, I really am."
        krystal "Wow! I'm such a big fan of yours!"
        allison "*Giggles* Thanks! I'm a big fan of you, too!"
        u "Hm? Even [krystal] is a fan of her. I never knew she was that famous..."
        scene ep5_220_a14 with dissolve
        faye "Alright, let's not waste anymore time."
        faye "Can you take everyone inside to get ready, [sally]?"
        sally "Sure. Leave it to me!"
        faye "You can go with [sally] too, [eira]."
        faye "There is something I need to talk to [krystal] about for a sec."
        eira "Okay, I get it."
        scene black with dissolve
        scene ep5_220_a15 with dissolve
        faye "Alright, before we start, let's go sit and talk for a bit."
        faye "It's about the contract. I want you to look at it first."
        krystal "Oh. Okay!"
        mc "What about me?"
        scene ep5_220_a16 with dissolve
        faye "You can come with us if you want."
        faye "I mean... You're looking after [krystal], right?"
        faye "You can help her look over the contract."
        krystal "Yes, please. I need your help, [mc]."
        mc "Okay. If you say so."
        scene black with dissolve
        scene ep5_220_a17 with dissolve
        faye "Alright, here is the contract."
        faye "I wrote it for you last night. Feel free to check it."
        faye "And if there is something you want to change, don't be afraid to tell me."
        krystal "Thank you."
        scene ep5_220_a18 with dissolve
        krystal "W-What?!"
        krystal "You're going to pay me $1,000,000!?"
        faye "Yeah. What's wrong?"
        faye "Do you want more? How much do you want? We can talk it over."
        scene ep5_220_a19 with dissolve
        krystal "No, it's nothing like that."
        krystal "It's just that I didn't expect you to pay me that kind of money."
        krystal "So, I was shocked when I saw the amount."
        faye "I see..."
        faye "Well, to be honest I wanted to give you more, because I believe you're worth more than a million."
        krystal "Aw... I'm so grateful to hear that."
        faye "But, the board didn't agree with me. They thought it would be risky to invest more than a million in you for now."
        scene ep5_220_a20 with dissolve
        krystal "They have their right to think that. I understand them."
        krystal "I've been inactive for quite a long time, there is nothing to guarantee that I will be doing well again."
        krystal "That's why I was shocked to see you're going to hire me for that much money."
        faye "I believe in you, [krystal]. It doesn't matter that you've been inactive for how long."
        faye "Judging from your performances in the past, I can tell that you're very talented."
        faye "So, I believe that you're going to shine bright again. You're born to be a star."
        krystal "Aw... You're exaggerating..."
        krystal "I'm just an ordinary person like everyone else..."
        scene black with dissolve
        s "*A few moments later*........."
        scene ep5_220_a21 with dissolve
        faye "Alright, we've reached an agreement."
        faye "Let's not waste anymore time here."
        faye "It's time to start working now."
        krystal "Okay, sure!"
        scene black with dissolve
        $ renpy.pause()
        scene ep5_220_a22 with dissolve
        sally "Take this, [krystal]."
        krystal "Hm? What is this thing...?"
        faye "It's called Xecon Gear. It's the product that we will be introducing it to the world soon."
        krystal "I see... Then, what am I supposed to do with it?"
        sally "Just wear it, then lie down on a chaise longue over there."
        sally "And... Boom! Magic will happen. You will be so amazed. I promise you."
        krystal "*Giggles* Okay..."
        scene ep5_220_a23 with dissolve
        sally "This is yours, [mc]."
        mc "Thanks."
        sally "*Giggles* You already know how to use it, right?"
        mc "Of course I do."
        sally "*Giggles* Hehe... Good!"
        faye "What about the others?"
        eira "They've already dived into the game."
        faye "Okay, great."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_220_a24 with dissolve
        krystal "I need to wear it like this, right?"
        krystal "*Giggles* This is so weird. I've never done anything like this before."
        krystal "What am I supposed to do next, [mc]?"
        scene ep5_220_a25 with dissolve
        mc "Yeah, that's right."
        mc "All you need to do is press on the start button."
        mc "It's on the right side of the gear."
        krystal "Oh! I think I've found it."
        mc "Yeah, press it. Then, wait for a few seconds."
        scene ep5_220_a26 with dissolve
        mc "See you soon, [krystal]."
        krystal "Hm? What are you talking ab..."
        krystal "................"
        scene black with dissolve
        $ renpy.pause()
        u "................"
        scene ep5_220_a27 with dissolve
        u "................"
        scene ep5_220_a28 with dissolve
        krystal "E-Eh?! What is happening?!"
        mc "Hi, [krystal]."
        scene ep5_220_a29 with dissolve
        krystal "Oh!?"
        krystal "What is this, [mc]?!"
        krystal "Where are we now? What is this place?"
        krystal "And what are these outfits we are wearing?"
        krystal "Wait... Your company is a game company."
        krystal "Is this the next level of VR technology?"
        scene ep5_220_a30 with dissolve
        mc "Calm down. I'll answer one question at a time..."
        mc "Let's start with your last question. No, this is nothing like VR technology."
        mc "We're actually inside a game now."
        krystal "What?! Really?! Is it even possible?!"
        mc "Of course, it is. This is the project that the company has been working towards."
        krystal "Wow... I knew that it was going to be a photo shoot to advertise a game."
        krystal "I thought it would be taken in the real world. I never knew that we were going to do it in-game like this..."
        s "*Spawning effects*........."
        krystal "Hm...?"
        scene ep5_220_a31 with dissolve
        krystal "Oh... I completely believe you now."
        krystal "We're actually inside a game."
        mc "I told you...."
        scene ep5_220_a32 with dissolve
        faye "Well... I've been a part of this project for years, but this is my first time diving in here."
        faye "I'm impressed. I can't tell any difference between the real world and this world."
        eira "Yeah... Me, too."
        sally "*Giggles* Hehe... I know, right?"
        faye "By the way, what am I wearing...?"
        faye "Hm? Wait..."
        scene ep5_220_a33 with dissolve
        faye "Is that a tail?"
        faye "Wait... I have a tail? How?"
        faye "Hm? I can even move it, too!"
        sally "Wow! You're so lucky, [faye]!"
        faye "Me? Lucky? How?"
        sally "It's a fairy fox race! It's one of the rarest races in the game."
        sally "You can't create a fairy fox character, you need to find the secret quest that allows you to become one."
        scene ep5_220_a32 with dissolve
        sally "But, this is just a beta testing, so our characters are automatically created at random."
        sally "However, the chance is still very, very low. This is the first time I've seen a fairy fox spawn as well."
        sally "We mostly got human race characters."
        eira "I guess I'm a human then."
        faye "Hmmm... I see."
        faye "By the way, don't you think my outfit is a little bit too revealing?"
        scene ep5_220_a34 with dissolve
        sally "That's the default costume for a fairy fox."
        sally "Since this is a beta testing account, you can change it if you want."
        sally "But, you'll need to open a system control."
        faye "Is that so...?"
        sally "Yeah. Do you want me to teach you how to do it?"
        faye "....No, forget it. I don't want to waste time doing it."
        faye "The photo shoot is more important right now."
        scene black with dissolve
        scene ep5_220_a35 with dissolve
        krystal "Hello, everyone."
        sally "Wow... You look good in that outfit, [krystal]."
        faye "Yeah, I couldn't agree more."
        faye "Seeing you like this, I feel even more like I made the right choice to choose you."
        eira "Me, too."
        krystal "*Giggles* Thanks..."
        scene ep5_220_a36 with dissolve
        faye "Alright, let's start working."
        faye "Where is everyone else?"
        sally "I told them to wait for us here."
        sally "So, I think they're somewhere in this village."
        faye "Alright, let's go look for them."
        scene ep5_220_a37 with dissolve
        allison "Hey, everyone!"
        sally "Oh! There she is!"
        faye "What are you doing down there, [allison]?"
        scene ep5_220_a38 with dissolve
        allison "I went to scout some good places for the session!"
        faye "Then, did you find one yet?"
        allison "Of course! Follow me. My staff members are waiting for us right there!"
        faye "Alright, let's get going, guys."
        mc "Okay..."
        scene ep5_220_a39 with dissolve
        allison "There they are..."
        u "Hm...? There is something strange."
        u "I thought [allison] was taller than everyone."
        u "But now, she looks the same size as [krystal]."
        u "...Well, I guess she was wearing high heels when we first met."
        scene ep5_220_a40 with dissolve
        allison "Alright, I think this place has the best view in this village."
        allison "So, we're going to take photos of [krystal] here."
        allison "What do you guys think?"
        faye "You're an expert in photography. If you think this is the best place, then it is the best."
        krystal "Yeah, I agree with [faye]."
        eira "Me, too."
        u "Well, to think about [allison], she looks somehow familiar..."
        u "This is so weird. I'm sure that I've never seen her before, but her face looks very familiar to me."
        scene ep5_220_a41 with dissolve
        allison "By the way, how are we going to take photos?"
        allison "I don't have any cameras here. I couldn't bring one from the real world either."
        sally "Oh! You don't need a camera in the game."
        sally "There is a system that allows you to take a picture of anything you're seeing."
        sally "You just need to open the menu by moving either of your hands like this."
        sally "Then, the system window will be shown in front of you."
        sally "Click on an icon that looks like a camera. Then, you're ready to go."
        sally "You can also adjust lights and shadows if you want."
        allison "*Smiles* That's a lot more convenient than real life, isn't it?"
        sally "*Giggles* I know, right?!"
        scene ep5_220_a42 with dissolve
        allison "Alright then, let's get started."
        allison "Could you please go stand over there, [krystal]?"
        krystal "Yeah, sure."
        allison "Thank you."
        scene ep5_220_a43 with dissolve
        allison "Lovely. That's what I was talking about."
        krystal "[allison]."
        allison "Yes?"
        krystal "How am I supposed to pose?"
        allison "Ummm... This is your first photo shoot after a long time, right?"
        allison "Let's start with easy poses first. Then, just follow your feelings."
        allison "Don't worry about it. No matter what pose you take, you will look absolutely beautiful."
        krystal "*Giggles* Stop flattering me already. You're making me shy."
        krystal "*Sighs* Alright, let's get started."
        scene ep5_220_a44 with dissolve
        krystal "How about this?"
        allison "Yeah, that looks great."
        allison "You can try changing to another pose."
        scene ep5_220_a45 with dissolve
        krystal "Okay...."
        allison "Lovely, but please smile a little bit more."
        krystal "Sure. I get it."
        scene ep5_220_a46 with dissolve
        allison "Perfect. Next pose, please."
        eira "[faye]."
        faye "Yes, [eira]?"
        eira "Those fox ears... I wanted to ask you for awhile."
        eira "Can you feel them the way you felt your tail?"
        sally "*Giggles* Why are you asking her that, [eira]?"
        eira "I'm just curious..."
        scene ep5_220_a47 with dissolve
        faye "Umm... I don't know. I can't feel them."
        sally "No way! You are supposed to be able to feel them, too."
        sally "That's one of the strong points of this game, isn't it?"
        sally "You can feel animal ears and tails as if they were real."
        sally "Am I right, [mc]?"
        mc "I have no idea...."
        scene ep5_220_a48 with dissolve
        faye "Oh, wait! I think I'm starting to feel them."
        faye "I'm going to try to control them...."
        faye "Oh, I can feel them moving now. Do you guys see that?"
        sally "Yeah, they're really moving!"
        eira "Aw... So cute."
        u "To think about it, I wonder if she can feel when someone touches those ears..."
        menu:
            "Touch those ears [faye2]":
                $ ch2ep1touchears = 1
                $ faye_ch2_ep1 += 2
                $ faye_relationship += 2
                scene ep5_220_a49 with dissolve
                faye "A-Aw! W-What are you doing, [mc]?!"
                sally "!!!!!"
                eira "Why are you doing that, [mc]?"
                mc "How does that feel, [faye]?"
                mc "I want to test if the sensory system is working."
                faye "Y-Yes, it's actually working. So, s-stop it already!"
                scene ep5_220_a50 with dissolve
                faye "*Softly breathes* E-Eyah!"
                sally "That's enough, [mc]. You've gotten your answer."
                sally "Please, take your hands off already."
                mc "....Oh, my bad. I forgot."
                scene black with dissolve
                scene ep5_220_a51 with dissolve
                faye "Y-You...!"
                sally "Calm down, [faye]."
                sally "He didn't do it on purpose. He was just testing the system."
                faye "Tsk...!"
                scene ep5_220_a52 with dissolve
                faye "*Sighs* Since you've been very helpful recently, I'll forgive you this time!"
                faye "But, don't you ever do that again, got it?!"
                mc "Yeah, I get it."
                sally "Well done, [faye]."
                scene black with dissolve
                $ renpy.pause()
            "Do nothing":
                $ ch2ep1touchears = 2
                u "Forget it. I shouldn't try testing it with her."
                u "We're not close enough to do something like that."
                scene black with dissolve
                $ renpy.pause()
        scene ep5_220_a53 with dissolve
        if ch2ep1touchears == 1:
            allison "What happened? Were you guys fighting?"
            sally "N-No, we weren't! Don't worry about us. Everything is all good!"
            allison "I see... By the way, we're done taking photos in this area."
        else:
            allison "Hey, guys. We're done taking photos in this area."
        allison "Can we move somewhere else?"
        faye "Yeah, sure."
        allison "Lovely. Can you suggest any beautiful places to go, [sally]?"
        sally "Of course I can!"
        scene black with dissolve
        $ renpy.pause()
        scene ep5_220_a54 with dissolve
        allison "Yeah, hold that pose, [krystal]."
        allison "Don't smile too much. I want this picture to look a little bit serious."
        allison "Keep your head that direction, but look right here."
        allison "Yeah, that's right. Perfect!"
        scene black with dissolve
        $ renpy.pause()
        scene ep5_220_a55 with dissolve
        allison "Great! Keep smiling at the camera like that."
        allison "You can try winking if you want. It will look very cute."
        krystal "Like this?"
        allison "Lovely! that's what I was talking about."
        scene black with dissolve
        $ renpy.pause()
        s "You guys spend a couple hours on the photo shoot...."
        scene ep5_220_a56 with dissolve
        allison "Alright, thank you, everyone, for your hard work today."
        allison "Especially you, [krystal]. You've done very well."
        krystal "Thank you for looking after me, [allison]."
        allison "No worries. I was just doing my job."
        scene ep5_220_a57 with dissolve
        faye "By the way, when can you send us the photos?"
        allison "Um... I'd say next week."
        allison "I want every one of them to look perfect."
        allison "So, I need some time for editing."
        faye "Okay. Noted that."
        scene ep5_220_a58 with dissolve
        allison "Alright, I've got to leave now."
        allison "It was an honor to work with you guys, especially you, [krystal]."
        krystal "Thank you. I was very happy to work with you, too."
        allison "*Smiles* I'm glad to hear that."
        allison "Goodbye, everyone."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_220_a59 with dissolve
        eira "I've got to leave, too."
        eira "I have an appointment with a customer in an hour."
        faye "Oh, okay. Thank you for today."
        eira "See you guys later."
        sally "See you, [eira]!"
        scene ep5_220_a60 with dissolve
        krystal "Did I do well, [mc]?"
        mc "Of course you did. You looked very professional when working."
        mc "You looked nothing like someone who has been inactive for years."
        krystal "*Smiles* Really? Thank you."
        krystal "Hearing that from you, I feel more confident now."
        scene ep5_220_a61 with dissolve
        krystal "By the way, would you mind taking me home?"
        mc "Hm? Do you want to leave now?"
        mc "It's almost noon. Why don't you have lunch before going?"
        krystal "Thanks, but I don't want to draw any more attention now."
        mc "If you say so, but I'll have to ask [zeke] for his car keys first."
        krystal "Oh yeah... You're right. I almost forgot that [zeke] was the one who brought us here."
        faye "I have a car. I can take you home."
        scene ep5_220_a62 with dissolve
        krystal "Thank you, [faye]...."
        krystal "But, I don't want to bother you..."
        faye "Don't worry about that. I don't think that you're bothering me at all."
        faye "Plus, I have an errand to run anyway. Taking you to your home isn't a big deal."
        krystal "Are you sure...?"
        faye "Of course! We're already work partners. We should help each other."
        sally "Yeah, she's right!"
        scene ep5_220_a63 with dissolve
        mc "Thank you, [faye]."
        faye "You're welcome."
        mc "Be careful not to let anyone see her."
        faye "I'm well aware of that."
        mc "Good..."
        krystal "Alright then, goodbye, [mc]."
        krystal "I'll see you this evening."
        mc "Sure."
        scene black with dissolve
        $ ch2ep1photosession = 1
        $ renpy.pause()
        jump ch2ep1elaine
    else:
        scene black with dissolve
        $ renpy.pause()
        s "You spent time having breakfast, then headed out to the company..."
        scene ep5_220_d1 with fade
        s "While waiting for an elevator...."
        crowd "Hold on! Isn't that...!?"
        crowd "Oh my god! What is she doing here?!"
        scene ep5_220_d2 with dissolve
        u "Hm...?"
        rin "What's happening....?"
        scene ep5_220_d3 with dissolve
        rin "Isn't that [lucy]?"
        rin "What is she doing here?"
        u "................"
        leo "Can you let us in, please?"
        leo "I'd like to ask her for a selfie. It will be very quick."
        joe "[lucy]! [lucy]! Can I get your autograph, please?!"
        scene ep5_220_d4 with dissolve
        faye "This way."
        lucy "Yeah, sure!"
        scene ep5_220_d5 with dissolve
        yui "I don't like her...."
        zeke "Neither do I..."
        zeke "She's so fake. I can sense it."
        yui "I know right?"
        rin "Alright, the elevator is here. Let's go guys..."
        jump ch2ep1elaine
label ch2ep1elaine:
    if ep3_quickfun == 1 or ep3_quickfundoggy == 1:
        scene ep5_220_a64 with fade
        u "................."
        u "...Alright, let's go back to the department."
        scene ep5_221 with dissolve
        elaine "Oh...!"
        u "Hm? [elaine]?"
        scene ep5_222 at eyesblink("Ch.2/Ep.1/Scenes/ep5_222.jpg", "Ch.2/Ep.1/Scenes/ep5_222_blink.jpg", 1) with dissolve
        elaine "There you are. Where have you been?"
        elaine "I was looking for you, but you weren't in your department."
        if ch2ep1photosession == 1:
            mc "I was in the game testing room."
        else:
            mc "I went to the toilet."
        mc "What were you looking for me for?"
        elaine "Can you come with me for a sec?"
        u "................"
        menu:
            "Follow her [elaine1]":
                $ ch2ep1followelaine = 1
                $ elaine_ch2_ep1 += 1
                $ eliane_relationship += 1
                scene ep5_223_a1 with dissolve
                mc "Yes, I can."
                mc "But, where are we going to go?"
                elaine "Follow me, and you'll see."
                mc "....Okay."
                scene black with dissolve
                $ renpy.pause()
                scene ep5_223_a2 with dissolve
                elaine "Okay... This place will do."
                mc "................"
                scene ep5_223_a3 with dissolve
                mc "What do you want from me?"
                mc "Why do we need to come up this far?"
                mc "By the way, aren't you supposed to be working now?"
                elaine "Shh... Can we just stop talking about work for now, okay?"
                elaine "I'm so sick of it already. I've been dealing with retarded customers for a few days."
                mc "Then, why did you bring me here?"
                elaine "Well...."
                scene black with dissolve
                mc "Hm...?"
                scene ep5_223_a4 with dissolve
                u "Okay. Now I know what she wants..."
                elaine "I just need to relax."
                elaine "And by relax, I mean sex."
                scene black with dissolve
                scene ep5_223_a5 at eyesblink("Ch.2/Ep.1/Scenes/ep5_223_a5.jpg", "Ch.2/Ep.1/Scenes/ep5_223_a5_blink.jpg", 1) with dissolve
                elaine "Come on. Let's fuck."
                elaine "I want to have fun with you."
                mc "...Someone might come up here."
                elaine "Don't worry. This is my secret place."
                elaine "I come here regularly, but I've never seen anyone up here before."
                elaine "There is also no security camera as well. There is no need to be worry about being seen."
                mc ".................."
                scene ep5_223_a6 with dissolve
                elaine "What are you waiting for?"
                elaine "Take your cock out and fuck me already..."
                menu:
                    "I've got another idea":
                        mc "Well, I've got another idea..."
                        elaine "Hm? What do you mea-"
                        jump ch2fuckelaine
                    "Leave":
                        $ ch2ep1sexelaine = 2
                        scene ep5_223_a6_d with dissolve
                        elaine "W-Wait? Where are you going?"
                        mc "I'm sorry, but I'm not in a mood to play with you today."
                        elaine "[mc], please...."
                        mc "No, [elaine]. Not today."
                        elaine "*Sighs* You're so boring..."
                        scene black with dissolve
                        s "You spent your day working until evening....."
                        jump ch2ep1part2end
            "I need to work":
                $ ch2ep1followelaine = 2
                scene ep5_223_d with dissolve
                mc "Sorry, but I can't."
                mc "I've been out here for too long. I need to go back to work."
                elaine "................"
                elaine "...Alright, never mind then."
                elaine "Good luck on your boring day. Bye."
                scene black with dissolve
                s "You spent your day working until evening....."
                jump ch2ep1part2end
    else:
        scene black with dissolve
        s "You spent your day working until evening....."
        jump ch2ep1part2end
label ch2fuckelaine:
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
    scene ep5_223_a7 with dissolve
    show ch2_elaine_spank with dissolve
    play music "sfx/ep4_4.mp3" fadein 3.0
    $ bgm = "Le Gang - Bad Intentions"
    elaine "-Ahhh?!"
    elaine "*Softly breathes* W-What are you doing?!"
    mc "I'm punishing a bad girl."
    elaine "*Softly breathes* A-Ahh..! I'm...not...a bad girl!"
    mc "Yeah? You're supposed to be working now, but not only did you skip the work, you wanted me to do naughty things with you here."
    elaine "*Softly breathes* A-Ahh..! I just...Mmmm!... Want to enjoy...Mmmm!... Myself!"
    $ renpy.pause()
    menu:
        "Next":
            elaine "*Softly breathes* Mmmmm! Please, stop teasing me already...!"
            mc ".................."
    scene ep5_223_a8 with dissolve
    hide ch2_elaine_spank
    mc "Alright then..."
    elaine "You made me really horny."
    elaine "Take your cock out and put it inside my pussy, please."
    mc "Fine. If you want it that much..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_223_a9 with dissolve
    mc "Okay, I'm going to put it in now...."
    elaine "Hurry up. I can't wait to feel it anymore!"
    mc "Alright then...."
    scene ep5_223_a10 with dissolve
    show ch2_elaine_doggy1 with dissolve
    window hide
    mc "Take that!"
    elaine "*Softly breathes* A-Ah...! Mmmm...Finally....!"
    $ renpy.pause()
    menu:
        "Next":
            elaine "*Softly breathes* Mmmm.... F-Faster... I want you to fuck me faster!"
            mc "Alright...."
    scene ep5_223_a11 with dissolve
    hide ch2_elaine_doggy1
    show ch2_elaine_doggy2 with dissolve
    window hide
    elaine "*Moans* Y-Yeah, that's right...!"
    elaine "*Moans* Mmmm..... Keep fucking me good like that...."
    $ renpy.pause()
    menu:
        "Next":
            elaine "*Moans* A-Ahh... M-More...! I want more...!"
    scene ep5_223_a12 with dissolve
    hide ch2_elaine_doggy2
    show ch2_elaine_doggy3 with dissolve
    window hide
    elaine "*Heavily breathes* Mmmmm!...Ahhhh!... [mc]...!"
    elaine "*Heavily breathes* A-Ahhh!...Mmmm... You're so good...!"
    $ renpy.pause()
    menu:
        "Next":
            elaine "*Heavily breathes* Mmmmm...! Hold on a sec...!"
            mc "...Hm? Why?"
            elaine "*Heavily breathes* Ahhh...! I want to do something else...!"
            mc "Okay..."
    scene black with dissolve
    hide ch2_elaine_doggy3
    scene ep5_223_a13 at eyesblink("Ch.2/Ep.1/Scenes/ep5_223_a13.jpg", "Ch.2/Ep.1/Scenes/ep5_223_a13_blink.jpg", 1) with dissolve
    mc "So, you want to do it in this position?"
    elaine "*Smiles* Yeah, but not in my pussy."
    elaine "*Smiles* I want you to fuck my ass."
    mc "................."
    elaine "What are you waiting for? Put your cock inside my ass already."
    mc "I've never fucked someone in the ass before..."
    elaine "*Smiles* Then, try it. I promise you. It will feel as good as fucking a pussy."
    elaine "Or maybe it will feel even better..."
    mc "................."
    elaine "*Smiles* Don't worry, I already cleaned it."
    mc "....Alright then."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_223_a14 with dissolve
    elaine "*Softly breathes* A-Ahhhh...!"
    mc "Ugh! It's so tight..."
    elaine "*Softly breathes* Of course, it is. This is my first time being fucked in the ass, too."
    mc "Wait. I thought you did it often. Judging from the way you talked earlier."
    elaine "*Giggles* I was just pretending. I needed to convince you to agree to it."
    elaine "*Softly breathes* Y-You can start moving your hips now..."
    show ch2_elaine_ass1 with dissolve
    window hide
    elaine "*Softly breathes* Mmmmm...! This feels so good...!"
    elaine "*Softly breathes* Ahhhh...! How about you? Feels good, right?"
    mc "...Yeah, I think so."
    $ renpy.pause()
    menu:
        "Next":
            elaine "*Softly breathes* Mmmmm...! F-Faster, please...!"
            mc "Okay...."
    scene ep5_223_a15 with dissolve
    hide ch2_elaine_ass1
    show ch2_elaine_ass2
    window hide
    elaine "*Moans* A-Ahhh...! A-Ahhh...!"
    elaine "*Moans* Mmmmmm....! [mc]....!"
    $ renpy.pause()
    menu:
        "Next":
            elaine "*Moans* Ahhhh...! You're driving me crazy...!"
            mc "*Softly breathes* Ahh...."
    scene ep5_223_a16 with dissolve
    hide ch2_elaine_ass2
    show ch2_elaine_ass3
    window hide
    elaine "*Heavily breathes* Ahhhh...! Ahhhh....!"
    elaine "*Heavily breathes* Mmmmm....! I-I'm about to cum...!"
    mc "*Softly breathes* Ahhh... Me, too..."
    $ renpy.pause()
    menu:
        "Pussy":
            hide ch2_elaine_ass3
            jump ch2elainedoggy1
        "Slowest":
            hide ch2_elaine_ass3
            jump ch2elaineass1
        "Slower":
            hide ch2_elaine_ass3
            jump ch2elaineass2
        "Cum":
            jump ch2elaineasscum
label ch2elainedoggy1:
    scene ep5_223_a10 with dissolve
    show ch2_elaine_doggy1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Ass":
            hide ch2_elaine_doggy1
            jump ch2elaineass1
        "Faster":
            hide ch2_elaine_doggy1
            jump ch2elainedoggy2
        "Fastest":
            hide ch2_elaine_doggy1
            jump ch2elainedoggy3
label ch2elainedoggy2:
    scene ep5_223_a11 with dissolve
    show ch2_elaine_doggy2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Ass":
            hide ch2_elaine_doggy2
            jump ch2elaineass1
        "Slower":
            hide ch2_elaine_doggy2
            jump ch2elainedoggy1
        "Faster":
            hide ch2_elaine_doggy2
            jump ch2elainedoggy3
label ch2elainedoggy3:
    scene ep5_223_a12 with dissolve
    show ch2_elaine_doggy3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Ass":
            hide ch2_elaine_doggy3
            jump ch2elaineass1
        "Slowest":
            hide ch2_elaine_doggy3
            jump ch2elainedoggy1
        "Slower":
            hide ch2_elaine_doggy3
            jump ch2elainedoggy2
label ch2elaineass1:
    scene ep5_223_a14 with dissolve
    show ch2_elaine_ass1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Pussy":
            hide ch2_elaine_ass1
            jump ch2elainedoggy1
        "Faster":
            hide ch2_elaine_ass1
            jump ch2elaineass2
        "Fastest":
            hide ch2_elaine_ass1
            jump ch2elaineass3
label ch2elaineass2:
    scene ep5_223_a15 with dissolve
    show ch2_elaine_ass2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Pussy":
            hide ch2_elaine_ass2
            jump ch2elainedoggy1
        "Slower":
            hide ch2_elaine_ass2
            jump ch2elaineass1
        "Faster":
            hide ch2_elaine_ass2
            jump ch2elaineass3
label ch2elaineass3:
    scene ep5_223_a16 with dissolve
    show ch2_elaine_ass3
    window hide
    $ renpy.pause()
    menu:
        "Pussy":
            hide ch2_elaine_ass3
            jump ch2elainedoggy1
        "Slowest":
            hide ch2_elaine_ass3
            jump ch2elaineass1
        "Slower":
            hide ch2_elaine_ass3
            jump ch2elaineass2
        "Cum":
            jump ch2elaineasscum
label ch2elaineasscum:
    mc "*Softly breathes* I'm about to cum..."
    elaine "*Heavily breathes* Mmmmm...! M-Me, too...!"
    elaine "*Heavily breathes* Y-You can cum inside my ass if you want...!"
    menu:
        "Cum inside":
            hide ch2_elaine_ass3
            scene black with dissolve
            scene ep5_223_a16_in1 with vpunch
            elaine "*Moans* I-I'm cumming...! Mmmmm....!!!"
            mc "*Softly breathes* Arrr...."
            mc "I'm going to pull it out now."
            scene ep5_223_a16_in2 with dissolve
        "Pull out":
            hide ch2_elaine_ass3
            scene black with dissolve
            scene ep5_223_a16_out1 with vpunch
            elaine "*Moans* I-I'm cumming...! Mmmmm....!!!"
            mc "*Softly breathes* Arrr...."
            scene ep5_223_a16_out2 with dissolve
    elaine "*Pants* Hehe... That...was...great...."
    elaine "*Pants* T-Thank you, [mc]. I feel much...happier now..."
    mc "You're welcome."
    elaine "*Pants* L-Let me take a deep breath for a sec, okay...?"
    mc "Okay..."
    scene black with dissolve
    s "*A few moments later*..........."
    scene ep5_223_a17 with dissolve
    elaine "*Smiles* You felt so good, [mc]."
    elaine "I've never felt so good when having sex with anyone before, except you."
    elaine "*Giggles* What should I do? I guess I'm addicted to you now."
    elaine "We also seem to get along well. Should we start dating?"
    mc "................"
    scene ep5_223_a18 with dissolve
    elaine "*Giggles* Relax. I was just kidding!"
    elaine "You want some?"
    mc "No, thanks. I don't smoke."
    elaine "Okay. That's good for you."
    scene ep5_223_a19 with dissolve
    elaine "What I said earlier... Don't take it too serious, okay?"
    elaine "There is no way I'm going to date anyone."
    elaine "I'll just keep enjoying my life like this."
    mc "..............."
    mc "May I ask why you want to live like that?"
    elaine ".............."
    scene ep5_223_a20 with dissolve
    elaine "*Sighs* It's a long story, [mc]."
    elaine "And I don't want to talk about it."
    elaine "I just don't want to remind myself of the old me again...."
    mc "Okay, I'm sorry."
    elaine "All good. There is nothing for you to be sorry for."
    elaine "My life right now is pretty good. I like it."
    elaine "I don't have to rely on anyone anymore."
    mc "................"
    scene ep5_223_a21 with dissolve
    mc "It must be awesome to be able to live the life you want to live..."
    elaine "Hm? What's wrong?"
    mc ".....Nothing."
    elaine "..............."
    elaine "You can also do that, too. You know it, right?"
    elaine "It won't be easy at first, but the result is worth the effort."
    mc "..............."
    scene ep5_223_a22 with dissolve
    mc "...Alright, I think it's time for me to leave now."
    mc "I've been away from my workstation for too long. I need to get back to work."
    elaine "Oh, okay. Feel free to go."
    elaine "I'll leave, too, after I finish smoking."
    elaine "See you around, [mc]."
    mc "See you, [elaine]."
    $ renpy.end_replay()
    $ ch2ep1sexelaine = 1
    $ elaine_ch2_ep1 += 3
    $ eliane_relationship += 3
    scene black with dissolve
    s "You went back to the department and worked until evening....."
    jump ch2ep1part2end
label ch2ep1part2end:
    scene black with dissolve
    $ renpy.pause()
    scene ep5_224 with dissolve
    stop music fadeout 3.0
    yui "Let's go home, [mc]."
    mc "Hm...?"
    yui "It's already 5 p.m."
    mc "Oh..."
    scene ep5_225 with dissolve
    mc "Don't worry about me. You can go first."
    mc "I still have some more work to finish."
    mc "I'll be working overtime today."
    yui "Is that so? Alright then, see you at home."
    mc "Yeah, see you."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_226 with dissolve
    s "You spend a couple more hours working..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_227 with dissolve
    u "Alright, I've finished..."
    u "Fortunately, I'm done earlier than I expected."
    u "Let's leave and go home."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_228 with fade
    u "Okay... I'm at the bus stop."
    u "I'll take a seat, and wait for the bu-"
    scene ep5_229 with vpunch
    u "Ouch...!"
    scene ep5_230 at eyesblink("Ch.2/Ep.1/Scenes/ep5_230.jpg", "Ch.2/Ep.1/Scenes/ep5_230_blink.jpg", 1) with dissolve
    mc "....[wendy]?"
    wendy "P-Please, help me, [mc]...."
    scene ep5_231 with dissolve
    mc "Hm? Help you?"
    $ faye_age = "26"
    play music "sfx/ep4_5.mp3" fadein 3.0
    $ bgm = "RYYZN - Waited (instrumental)"
    wendy ".....Yeah."
    mc "What do you want me to help you with?"
    scene ep5_232 with dissolve
    wendy "I-I've been followed by {b}him{/b}!"
    wendy "H-He waited for me in front of the company."
    wendy "I already told him that I didn't want to talk, b-but he keeps following me!"
    wendy "Help me, please!"
    mc "Hang on, [wendy]. Who was that {b}he{/b} you were talking about?"
    scene ep5_233 with dissolve
    unknown "There you are, [wendy]..."
    wendy "!!!!!"
    mc "Hm...?"
    scene ep5_234 with dissolve
    unknown "*Softly breathes*... You ran so fast, [wendy]. I almost couldn't catch up with you."
    unknown "But, why did you run away from me in the first place?"
    unknown "We didn't finish talking yet."
    wendy "Yes, we did! I already told you that I don't want to talk to you, didn't I?!"
    wendy "There is nothing to talk about between us!"
    u "Hm? I thought she was followed by a random perverted subscriber..."
    u "But, it seems like they know each other."
    scene ep5_235 with dissolve
    unknown "Come on... Don't be like that."
    unknown "We still have plenty to talk about."
    unknown "I miss you, and I know that you miss me, too."
    wendy "Don't come near me!!"
    u "*Sighs*...Well, looks like I have no choice."
    scene ep5_236 with dissolve
    mc "Stop it."
    unknown "Hm....? What are you doing?"
    unknown "Who are you by the way?"
    unknown "Why are you doing this to me? I just want to talk to her."
    mc "Step back."
    scene ep5_237 with dissolve
    mc "Didn't you hear what she said?"
    mc "She said that she didn't want to talk to you."
    unknown "Chill, bro. I just wanted to clear things up with her. That's it."
    unknown "It's not like I was going to hurt her, wasn't it? Don't be so serious."
    unknown "Wait... Did I actually have to explain that to you?"
    unknown "This is our business. Who are you to intervene? You have no right to."
    mc ".............."
    menu:
        "I'm her boyfriend. [wendy3]":
            jump ch2ep1answer1
        "I'm her colleague. [wendy1]":
            $ ch2ep1helpwendy = 2
            $ wendy_relationship += 1
            $ wendy_ch2_ep1 += 1
            scene ep5_237_d1 with dissolve
            mc "I'm her colleague."
            unknown "................."
            mc ".................."
            scene ep5_237_d2 with dissolve
            unknown "What the fuck, man? Then, you really have no right to interrupt."
            mc "Of course I have the right to. It's obvious that you're bothering her."
            unknown "What? Since when am I bothering her? I just want to talk."
            mc "But, she doesn't want to talk to you. Don't you understand that?"
            unknown "*Sighs*.....You're the one who doesn't understand things here."
            scene ep5_237_d3 with dissolve
            unknown "She still loves me! I'm a hundred percent sure!"
            unknown "She even posts her sexy images just for me!"
            mc "Just for you?"
            unknown "I'm her boyfriend! Don't you understand that!?"
            wendy "No! What are you talking about!? You aren't my boyfriend! Not anymore!"
            jump ch2ep1helpwendyend
label ch2ep1answer1:
    $ ch2ep1helpwendy = 1
    $ wendy_relationship += 3
    $ wendy_ch2_ep1 += 3
    scene ep5_237_a1 with dissolve
    mc "Of course I do. I'm her boyfriend."
    wendy "Hm...?!"
    unknown "W-What did you just say?!"
    mc "Are you deaf? I said that I'm her boyfriend."
    unknown "Y-You...!"
    scene ep5_237_a2 with dissolve
    unknown "You're lying!"
    unknown "I've been following her for sometimes already."
    unknown "Yeah, I saw you with her a couple of times, but there is no way you're her boyfriend!"
    unknown "So stop bullshitting around, and get lost!"
    mc "Bullshitting around?"
    unknown "Yeah! What you said was obviously a lie. You need to learn how to lie better!"
    scene ep5_237_a3 with dissolve
    mc "Well then...."
    mc "Since you leave me no choice, I will prove it to you."
    mc "*Whispers* I'm sorry, [wendy]...."
    wendy "H-Hm, what are you sorry f-"
    scene ep5_237_a4 with dissolve
    wendy "!!!!!!!"
    unknown "W-What are you doing!!??"
    unknown "S-Stop it already!!"
    mc "*Kisses*........."
    scene ep5_237_a5 with dissolve
    wendy "*Kisses* Mmmm...."
    wendy "(W-What is happening...?!)"
    wendy "(I know that he needed to do something to trick that bastard into believing him.)"
    wendy "(But, I didn't expect him to actually kiss me like this...)"
    scene ep5_237_a6 with dissolve
    mc "Was that enough?"
    mc "Do you believe that we're dating now?"
    unknown "Y-You...!!"
    wendy "..............."
    scene ep5_237_a7 with dissolve
    unknown "No! I still don't believe you!"
    unknown "There is no way she is dating you!"
    unknown "She still loves me! I'm a hundred percent sure!"
    unknown "She even posts her sexy images just for me!"
    jump ch2ep1helpwendyend
label ch2ep1helpwendyend:
    scene ep5_238 with dissolve
    unknown "Let's just find somewhere quiet to talk, [wendy]..."
    wendy "No! I don't want to go with you!"
    wendy "Get lost! I don't want to see you! Don't you show up ever again!"
    unknown "Come on... Don't be like that. I miss you so bad!"
    u "*Sighs* This guy is a complete psycho..."
    u "He is also very annoying. I can't take it anymore."
    mc "Didn't she tell you to......"
    scene ep5_239 with dissolve
    mc "{b}....GET LOST?!{/b}"
    unknown "Ouch!!!"
    wendy "!!!!!"
    scene ep5_240 with dissolve
    unknown "...Ouch!!"
    unknown "D-Did you just kick me?!"
    unknown "I-I'm going to call the police!"
    crowd "Hm? What's happening right there?"
    mc "..............."
    scene ep5_241 with dissolve
    mc "Then, what are you waiting for?"
    mc "Go ahead. Pick up your phone, and call the police already."
    mc "I can pay for the call, but I'm pretty sure you will be the one ending up in jail."
    unknown "W-What are you talking about? There is no way it's going to happen!"
    mc "Really? Don't you realize what you've been doing is called stalking?"
    mc "And as I remember...."
    mc "the penalty for stalking is imprisonment. Up to 10 years."
    unknown "!!!!!!"
    scene ep5_242 with dissolve
    mc "So, stop stalking her already, you fucking pervert."
    unknown "O-Ouch!! I-It hurts...!"
    mc "Since I'm not the one having a problem with you, I'll let you go for today."
    mc "But, don't you dare show your face to me ever again."
    mc "Otherwise, I'm going to make sure that you end up in jail."
    unknown "O-Okay!! I promise that I won't show up around you again!"
    unknown "P-Please, let me go! It hurts...!"
    mc "Well then..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_243 with dissolve
    wendy "Get lost, you piece of shit!"
    unknown "(Shit! I never knew [wendy] had a gangster as a friend.)"
    unknown "(Let's just back off for now...)"
    unknown "(I'll find another opportunity when that fucking piece of shit isn't with her!)"
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ch1ep2.mp3"
    $ bgm = "Bensound - Little Idea"
    scene ep5_244 with dissolve
    wendy "....[mc]."
    mc "Yeah...?"
    wendy "Thank you so much for helping me out."
    mc "You're welcome."
    scene ep5_245 with dissolve
    mc "By the way, is he your ex-boyfriend?"
    wendy "...Yeah, he is."
    wendy "I dated him back in university."
    mc "I see..."
    wendy "Let's just stop talking about him, okay?"
    wendy "I don't want to talk about that piece of shit."
    mc "Alright, if you say so."
    scene ep5_246 with dissolve
    mc "By the way, I think you should report it to the police."
    mc "I know that I threatened him to not show up again, but we'll never know..."
    mc "So, it's better to let the police handle him."
    wendy "I agree with you, but I'm not sure if I want to make a tempest in a teacup from this."
    wendy "I need some time to think about it..."
    mc "Fine. I have no problem with that."
    if ch2ep1helpwendy == 1:
        mc "By the way, I'm sorry about earlier."
        wendy "Hm? What are you talking about?"
        mc "About that kiss."
        scene ep5_246_a with dissolve
        wendy "O-Oh! You don't need to be sorry at all!"
        wendy "I understand why you decided to kiss me."
        wendy "You just wanted to trick him to believe that we're really dating."
        wendy "So, I'm not mad at you at all!"
        mc "Thank you for understanding."
    scene black with dissolve
    scene ep5_247 with dissolve
    mc "By the way, why are you going home this late?"
    mc "Did you work overtime, too?"
    wendy "Too? You worked overtime, then?"
    mc "Yeah, I did."
    wendy "But, actually no, I didn't work overtime. I spent some time at the library after work."
    mc "I see..."
    scene ep5_248 with dissolve
    wendy "Oh! The bus is here!"
    mc "Hm...?"
    wendy "You're waiting for another line, right?"
    mc "Yeah, I am."
    wendy "Alright, I'm leaving now. See you tomorrow, [mc]."
    mc "............."
    scene ep5_249 with dissolve
    mc "Hang on a sec, [wendy]...."
    wendy "Hm...?"
    mc "I'll take this bus, too."
    wendy "But, why? This bus doesn't stop at your house."
    mc "It's okay. I just want to go with you and make sure that you get home safely."
    wendy "Aw... How sweet of you."
    wendy "Alright, let's go then."
    mc "Okay...."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_250 with fade
    wendy "Okay, we're here. This is my home."
    wendy "Thank you for taking me here, [mc]."
    mc "You're welcome."
    scene ep5_251 with dissolve
    mc "Alright then, since you're safe now, I'm going to take a leave."
    mc "Get inside, [wendy]."
    wendy "Are you going to leave now?"
    mc "Yeah, I just wanted to make sure that your ex-boyfriend wasn't waiting for you here."
    wendy "I see..."
    scene ep5_252 at eyesblink("Ch.2/Ep.1/Scenes/ep5_252.jpg", "Ch.2/Ep.1/Scenes/ep5_252_blink.jpg", 1) with dissolve
    wendy "But, since you're already here, and there is still time before the last bus..."
    wendy "Why don't you come inside first?"
    wendy "Let's relax for a little while."
    wendy "I'd also like to do something to thank you for helping me out."
    wendy "How about a meal? I'll make you dinner tonight."
    u "..................."
    menu:
        "Accept [wendy1]":
            $ ch2ep1wendyinvite = 1
            $ wendy_ch2_ep1 += 1
            $ wendy_relationship += 1
            scene ep5_253 with dissolve
            mc "Okay, if you say so."
            wendy "*Giggles* Alright, let's get inside then!"
            mc "Sure."
            scene black with dissolve
            $ renpy.pause()
            scene ep5_254_a1 with dissolve
            wendy "By the way, I'm warning you. My house might look a little bit untidy."
            wendy "I've been pretty busy. It's been a while since I cleaned it last time."
            mc "All good. I don't mind that."
            wendy "*Giggles* Thanks. Alright, come in. Make yourself at home."
            scene ep5_254_a2 with dissolve
            elaine "Welcome home, [wendy]."
            wendy "Oh? You're still here?"
            wendy "I thought you were going to go party tonight."
            elaine "Well, I just changed my mind. I don't feel like going out tonight."
            elaine "Hm...?"
            scene ep5_254_a3 with dissolve
            elaine "[mc]?"
            mc "Hello..."
            elaine "Why are you guys arriving together?"
            wendy "We met at the bus stop, so I invited him home."
            elaine "I see..."
            scene ep5_254_a4 with dissolve
            wendy "[mc]."
            mc "Yeah?"
            wendy "You can go take a seat with [elaine] first."
            wendy "I'm going to change my outfit."
            mc "Okay. Got it."
            scene ep5_254_a5 with dissolve
            elaine "What's up?"
            mc "Do you mind moving inside for a bit?"
            elaine "Oh... Okay!"
            mc "Thank you."
            scene ep5_254_a6 with dissolve
            elaine "...Hm? Why do you keep staring at me like that?"
            mc "Oh, sorry. I've just never seen you wear glasses before."
            mc "I never knew that you were short-sighted."
            elaine "Oh, I always wear contact lenses when I'm outside. That's why."
            elaine "Wearing glasses leaves marks on my nose. I don't like that."
            elaine "Moreover, my eyesight isn't that bad, so I only wear them when watching TV, or working in front of a computer."
            mc "I see..."
            scene ep5_254_a7 with dissolve
            mc "By the way, what were you watching?"
            elaine "Justice League."
            mc "Hm? You haven't watched it yet? It was released in 2017, wasn't it?"
            elaine "Yes, I did. That version was a mess."
            mc "I agree with that."
            elaine "This is Zack Snyder's Justice League."
            elaine "It was just released a few days ago."
            mc "I see..."
            scene ep5_254_a8 with dissolve
            wendy "Okay..."
            wendy "...I'm done changing."
            wendy "What'd you like to have for dinner, guys?"
            scene ep5_254_a9 with dissolve
            elaine "I feel like having a salmon steak today."
            wendy "Okay, salmon steak for [elaine]."
            wendy "What about you, [mc]?"
            mc "Me, too."
            wendy "Okay then, salmon steak for both of you."
            elaine "Hang on a sec...."
            scene ep5_254_a10 with dissolve
            elaine "Let me help you cook."
            elaine "Is there something you need me to help with?"
            wendy "Umm... I'll let you prepare vegetable dishes then."
            elaine "Okay, leave it to me."
            scene ep5_254_a11 with dissolve
            u "Well, I could be useful if it was something else, but cooking."
            u "There is nothing I can do...."
            u "Let's just keep watching TV then."
            scene black with dissolve
            s "*Half an hour later*...."
            scene ep5_254_a12 with dissolve
            wendy "[mc]."
            mc "Yes...?"
            wendy "Come. Dinner is ready."
            mc "Oh, okay. Let me turn off the TV."
            scene black with dissolve
            s "*About an hour later*...."
            scene ep5_254_a13 with dissolve
            elaine "Ah... I'm so full~!"
            elaine "That was very delicious."
            elaine "Your food is as delicious as always, [wendy]."
            wendy "*Giggles* Thank you."
            scene ep5_254_a14 with dissolve
            elaine "What about you, [mc]?"
            elaine "Did you enjoy the dinner?"
            wendy "*Smiles*...."
            scene ep5_254_a15 with dissolve
            mc "Yes, I did. It was delicious."
            mc "Your cooking skill is as good as [rin]."
            wendy "*Giggles* Aw... Thank you."
            wendy "But, she is far better than me. I'm still learning."
            scene ep5_254_a16 with dissolve
            elaine "By the way, I'm still surprised at how you managed to invite [mc] here."
            elaine "You know... I don't think he is a type of guy who accepts any invitation easily."
            elaine "How did you do it?"
            wendy "................"
            scene ep5_254_a17 with dissolve
            wendy "*Sighs* Well, do you remember [luke]?"
            elaine "[luke]...?"
            wendy "My ex-boyfriend."
            elaine "Oh... Yeah, I remember him."
            wendy "He appeared out of nowhere in front of the company."
            scene ep5_254_a18 with dissolve
            elaine "W-What?!"
            wendy "Yeah, he really freaked me out. He said that he wanted to talk with me."
            wendy "But, I ran away till I met [mc] at the bus stop."
            wendy "Then, I asked [mc] to help me."
            scene ep5_254_a19 with dissolve
            elaine "*Bangs her fist down on the table* That jerk!"
            wendy "C-Calm down, [elaine]..."
            elaine "Talking about him reminds me of his face, and that makes me so angry right now!"
            elaine "How dare he show up in front of you again?!"
            scene ep5_254_a20 with dissolve
            elaine "I wish I'd been there with you."
            elaine "If I was, I could slap him in the face!"
            wendy "Calm down, [elaine]."
            wendy "[mc] already helped me deal with him."
            wendy "I think he won't dare to show up to me again."
            u "[elaine] looks very pissed. She must really hate that guy."
            u "Hearing about him now, I wonder what he did to make her so pissed off."
            menu:
                "Ask [wendy1]":
                    $ ch2ep1askwendy = 1
                    $ wendy_ch2_ep1 += 1
                    $ wendy_relationship += 1
                    scene ep5_254_a20_a1 with dissolve
                    mc "Why are you so angry after hearing about him, [elaine]?"
                    mc "What did he do?"
                    scene ep5_254_a20_a2 with dissolve
                    elaine "*Sighs* I'm sorry, [mc]."
                    elaine "I just don't want to talk about that jerk. It really makes me disgusted."
                    mc "Oh..."
                    wendy "It's alright. I will tell you everything, [mc]."
                    mc "Okay."
                    scene black with dissolve
                    wendy "Back when I was at the university...."
                    scene ep5_254_a20_a3 with fade
                    wendy "[luke]... He and I were in the same field."
                    wendy "We met each other in almost every class."
                    wendy "So, we became friends at first."
                    scene ep5_254_a20_a4 with dissolve
                    wendy "We shared a lot of things in common, so we got along really well."
                    wendy "We spent time hanging out together a lot."
                    wendy "I thought he was a good person back then. So, I was a little bit interested in him."
                    scene ep5_254_a20_a5 with dissolve
                    wendy "Then, a friendship turned into a relationship."
                    wendy "I really loved him, and he was my first boyfriend."
                    wendy "So, I did everything to make him happy."
                    scene ep5_254_a20_a6 with dissolve
                    wendy "At first, everything was really good. I was so happy in our relationship."
                    wendy "But as time flew by, he started to become less interested in me."
                    wendy "He always looked at his phone every time we were together."
                    scene ep5_254_a20_a7 with dissolve
                    wendy "So, I started to feel unhappy at our relationship."
                    wendy "But, I tried my best to not overthink it."
                    wendy "It was coming up to the final exam, so I thought he was distracted by that."
                    scene ep5_254_a20_a8 with dissolve
                    wendy "Later that night, I decided to surprise him by going to his place."
                    wendy "I thought I was going to study for the exam with him."
                    scene ep5_254_a20_a9 with dissolve
                    wendy "But..."
                    scene ep5_254_a20_a10 with dissolve
                    wendy "I saw him with another girl."
                    wendy "They were about to walk into his place."
                    wendy "He hugged her shoulder while walking, and it made me suddenly realize that they weren't just friends."
                    scene ep5_254_a20_a11 with dissolve
                    wendy "I was so heartbroken to see that."
                    wendy "And when I came back to my senses again, I was already crying with [elaine]."
                    wendy "I immediately told her everything."
                    scene ep5_254_a20_a12 with dissolve
                    wendy "She was so angry that she immediately rushed into his place."
                    wendy "She slapped him right in the face."
                    wendy "He was so confused why she did that to him, and he denied her calling him a cheater."
                    scene ep5_254_a20_a13 with dissolve
                    wendy "You know what he said? He told us that he didn't cheat on me."
                    wendy "That girl was just a hooker. He said that he felt bored having sex with me."
                    wendy "He said he wanted to feel excited. He wanted to have different feelings. That's why he decided to hire her."
                    wendy "His excuse didn't help anything, it only made [elaine] more pissed off."
                    wendy "So, she kicked him in the balls real hard."
                    scene ep5_254_a20_a14 with dissolve
                    wendy "At first, I was about to hurt him myself as well."
                    wendy "But, after seeing what [elaine] did to him, I already felt satisfied."
                    wendy "Then, she yelled at him, telling him to not contact me again and he promised that."
                    scene black with dissolve
                    $ renpy.pause()
                    scene ep5_254_a20_a15 with dissolve
                    wendy "That's it."
                    wendy "He kept his promise for years. I don't know why he suddenly showed up again."
                    elaine "I bet he wanted to come up with typical bullshit like..."
                    elaine "'I'm sorry, I know that I was wrong. Could you give me a second chance, please? I know now that the only person I love is you.'"
                    elaine "Don't you ever fall for jerk, [wendy]."
                    scene ep5_254_a20_a16 with dissolve
                    wendy "That isn't going to happen, [elaine]."
                    wendy "There is no way I'm going to forgive him."
                    elaine "That's right, my girl. That fucking jerk doesn't deserved to be in your life."
                    elaine "To be honest I don't even need to warn you about it. You're smart."
                    elaine "{size=-15}Don't be stupid like I was...{/size}"
                    mc "Hm....?"
                "Stay quiet":
                    $ ch2ep1askwendy = 2
                    scene ep5_254_a20_d with dissolve
                    u "Well, I think it's better not to ask anything."
                    u "I don't find myself getting anything good for being involved in this."
                    u "And, this is none of my business after all...."
                    u "Let's just stay quiet until she calms herself down."
            scene black with dissolve
            s "*A few moments later*........"
            scene ep5_254_a21 with dissolve
            mc "...Thank you for dinner, [wendy]."
            wendy "You're welcome."
            wendy "Feel free to come hang out with us again."
            mc "Okay, sure."
            scene ep5_254_a22 with dissolve
            mc "Alright, it's about time for the last bus to come."
            mc "See you tomorrow."
            wendy "See you, [mc]."
            elaine "Get home safely. Goodnight."
            mc "Goodnight."
            jump ch2ep1nightbeforeparty
        "Decline":
            $ ch2ep1wendyinvite = 2
            scene ep5_253 with dissolve
            mc "Thanks for inviting me in. I appreciate that."
            mc "But, I better leave now. There is something else I need to do."
            wendy "Oh... Okay, never mind then!"
            scene ep5_254_d1 with dissolve
            wendy "Goodbye. Get home safely, [mc]."
            mc "See you tomorrow."
            jump ch2ep1nightbeforeparty
label ch2ep1nightbeforeparty:
    $ elaine_contact = True
    $ wendy_contact = True
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ch2ep1_1.mp3" fadein 3.0
    $ bgm = "Roa - Winter Magic"
    scene ep5_255 with fade
    u "Alright, I'm back home..."
    u "Let's go upstairs to my room."
    unknown "Oh! You're back, [mc]?!"
    u "...Hm?"
    scene ep5_256 with dissolve
    u "Oh, it's [zeke] and... [yui]?"
    u "What are they doing there?"
    u "Why are they dressed like that?"
    scene ep5_257 with dissolve
    zeke "Long day, huh?"
    mc "Yeah..."
    mc "You guys are going somewhere?"
    zeke "Hm...?"
    scene ep5_258 with dissolve
    zeke "Oh, hahaha. No, we aren't!"
    zeke "We're just trying outfits for tomorrow's party."
    mc "Tomorrow's party?"
    scene ep5_259 with dissolve
    zeke "Yeah. Can you come here for a sec?"
    zeke "The girls might want to know your opinion."
    mc "................"
    mc "...Okay, sure."
    scene ep5_260 at eyesblink("Ch.2/Ep.1/Scenes/ep5_260.jpg", "Ch.2/Ep.1/Scenes/ep5_260_blink.jpg", 1) with dissolve
    rin "Hi, [mc]."
    rin "Will you give me your opinion?"
    mc "What do you want to ask me?"
    yui "How do we look in these dresses?"
    menu:
        "Gorgeous":
            scene ep5_261_a at eyesblink("Ch.2/Ep.1/Scenes/ep5_261_a.jpg", "Ch.2/Ep.1/Scenes/ep5_261_a_blink.jpg", 1) with dissolve
            mc "You both look gorgeous."
            rin "Really? Do you really think that?"
            mc "Yeah..."
            yui "Alright then, I'll wear this dress for tomorrow's party."
        "Okay":
            scene ep5_261_d at eyesblink("Ch.2/Ep.1/Scenes/ep5_261_d.jpg", "Ch.2/Ep.1/Scenes/ep5_261_d_blink.jpg", 1) with dissolve
            mc "You both look okay."
            rin "...That's it?"
            mc "Yeah..."
            yui "Okay. Thank you for your opinion."
            yui "I guess I'll wear this dress for tomorrow's party then."
    scene ep5_262 with dissolve
    mc "By the way, what party are you guys talking about?"
    mc "Am I missing something?"
    zeke "Hm? You haven't heard about it yet?"
    zeke "[rowan], our president, is throwing a party tomorrow night."
    mc "For what?"
    scene ep5_263 with dissolve
    rin "He just bought a new house. So, it's a housewarming party."
    mc "I see..."
    mc "Well, no one ever told me about that."
    rin "I'm sorry. I forgot to tell you just now..."
    zeke "Me, too. My bad, bro."
    yui "I thought you wouldn't be interested, so..."
    rin "By the way, will you come with us?"
    scene ep5_264 with dissolve
    mc "..............."
    u "Well, I'm not a party person..."
    u "But, it's going to be held at [rowan]'s house."
    u "I might find some useful information there."
    scene ep5_265 with dissolve
    mc "Alright, you can count me in."
    rin "Lovely! Then, you're going to need a good looking suit."
    rin "Have you got one?"
    mc "Hm? Can I just wear my work outfit?"
    scene ep5_266 with dissolve
    zeke "Of course not! We're talking about a party at our president's house!"
    zeke "Everyone has been waiting for it."
    zeke "You'll need to dress properly, bro."
    mc "Alright, got it."
    scene ep5_267 with dissolve
    mc "I'm really tired. Please, let me go."
    zeke "Sure. Rest well, bro."
    zeke "See you tomorrow."
    rin "Goodnight, [mc]."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_268 with fade
    u "Okay. I'm done with my shower."
    u "It's getting late. Let's go to bed."
    scene ep5_269 with dissolve
    u "By the way, I've been thinking about it for awhile..."
    u "This bed is a bit uncomfortable. It's quite hard for me to fall asleep."
    u "I might need to buy a new one soon..."
    if ep4yuiplananswer == 1:
        scene ep5_269_a1 with dissolve
        s "*Door knocks*......."
        u "...Hm? Who's it?"
        yui "It's me, [yui]. Can we talk for a sec?"
        u "...Okay."
        scene ep5_269_a2 at eyesblink("Ch.2/Ep.1/Scenes/ep5_269_a2.jpg", "Ch.2/Ep.1/Scenes/ep5_269_a2_blink.jpg", 1) with dissolve
        yui "Hi again, [mc]."
        mc "Hi."
        yui "Did I wake you up?"
        mc "No, you didn't."
        yui "Phew, that's a relief!"
        scene ep5_269_a3 with dissolve
        mc "By the way, what did you want to talk about?"
        yui "Not right here, [mc]."
        yui "Can we talk inside?"
        mc "................."
        mc "....Okay. Come on in then."
        yui "Thank you."
        scene ep5_269_a4 with dissolve
        mc "You can sit on that chair if you want."
        yui "Oh yeah, that's lovely. Thanks."
        mc "You're welcome."
        scene ep5_269_a5 with dissolve
        mc "....Alright then, what was it that you wanted to talk about."
        yui "Well, I came here to prepare some Q&A with you."
        mc "Q&A? About what?"
        yui "About me, of course! Did you already forget that you promised to go meet my parents with me?"
        mc "No, I didn't. I just don't understand why we need to prepare this Q&A thing."
        scene ep5_269_a6 with dissolve
        yui "Alright, listen. We're going to meet them this Saturday, right?"
        mc "...Yeah, that's right."
        yui "What do you think we're going to do after meeting them?"
        yui "Did you think that we will just go say hi to them, and then leave?"
        mc "...No, I didn't."
        yui "Right?! At the very least, we're going to have to eat with my parents."
        yui "And I'm a hundred percent sure that they will ask you plenty of questions about me."
        yui "That's why I'm asking you to prepare some Q&A now so that you can answer them questions and trick them to believe that we're really dating."
        mc "...................."
        scene ep5_269_a7 with dissolve
        mc "...Alright, I understand it now."
        yui "Lovely. Alright, let's get started then. Are you ready?"
        mc "...I think so."
        yui "Alright, let's start with the first question...."
        scene black with dissolve
        s "*About half an hour later*.........."
        scene ep5_269_a7 with dissolve
        yui "Okay. That was the last question."
        yui "Do you remember everything now?"
        mc "Yes, I do."
        yui "...Are you positive?"
        mc "Yeah..."
        yui "What high school did I go to?"
        mc "Hm...?"
        yui "What are you waiting for? Answer me."
        scene ep5_269_a8 with dissolve
        mc "{b}Rose Marie.{/b}"
        yui "What kind of place do I prefer to go on a vacation? Beach, or mountains?"
        mc "You prefer the {b}beach{/b} over mountains."
        yui "What is my favorite type of music?"
        mc "Your favorite type of music is {b}classical music.{/b}"
        yui "And what song do I like the most?"
        mc "{b}Ombra mai fù by Handel.{/b}"
        scene ep5_269_a9 with dissolve
        yui "Wow! To be honest I didn't expect you to remember everything in the first try."
        yui "But, you did it! I'm so impressed."
        mc "Well, I'm quite good at memorizing, so..."
        yui "That's good for you, then. Also, for me, too."
        yui "Alright, I'm sure that I can count on you now. I'm going to leave."
        mc "...Okay."
        scene ep5_269_a10 with dissolve
        yui "Oh! By the way, please don't forget to wear a good-looking suit, okay?"
        yui "It's not just for tomorrow's party. You'll need to wear one on Saturday, too."
        mc "Got it. You don't need to worry about that."
        yui "Lovely. Goodnight then, [mc]."
        mc "You, too."
        scene black with dissolve
        $ renpy.pause()
        scene ep5_269_a11 with dissolve
        u "....Alright, I think that's it for today."
        u "It's getting very late. Let's get to bed."
        $ ch2ep1qa = 1
        $ yui_ch2_ep1 += 2
        $ yui_relationship += 2
    else:
        $ ch2ep1qa = 2
        u "*Sighs* Well, let's just forget about it for now..."
    u "Let's just go to bed."
    scene ep5_270 with dissolve
    u ".................."
    u "*Sighs* Well, it's really uncomfortable to fall asleep on this bed."
    u "I'm going to need to find some time to look for a new one."
    scene black with dissolve
    $ renpy.pause()
    jump ch2ep1spycctv
label ch2ep1spycctv:
    scene black with dissolve
    $ renpy.pause()
    scene ep5_271 with dissolve
    zeke "Wooh, what a lovely day!"
    zeke "Let's go to work on our beloved job, guys!"
    mika "*Giggles* Yeah, let's go!"
    mc "................"
    scene black with dissolve
    $ renpy.pause()
    if ch2ep1qa == 1:
        scene ep5_272_a with fade
        yui "[mc]."
        mc "...Hm?"
        yui "What was my first pet? Was it a dog or a cat? And, what was its name?"
        mc "It was {b}a dog named Cooper.{/b}"
        yui "*Giggles* Wow! I totally believe now that you're good at memorizing."
    else:
        scene ep5_272_d with fade
        yui ".............."
        mc ".............."
    scene ep5_273 with dissolve
    liam "Oh?!"
    mc "Hm?"
    liam "Good morning, guys."
    liam "You guys are quite early today, huh?"
    scene ep5_274 with dissolve
    yui "Good morning, [liam]."
    yui "Are you going somewhere?"
    liam "Oh! I was going to meet [pete]. I have to talk to him about work."
    yui "I see... Alright then, we'll let you go, then."
    scene ep5_275 with dissolve
    liam "Oh! By the way, have you heard about tonight, [mc]?"
    liam "I was about to tell you so many times, but I kept forgetting to."
    liam "Our president is arranging a housewarming party tonight."
    mc "Yeah, [rin] and [yui] already told me about that."
    scene ep5_276 with dissolve
    liam "Really? That's great then. Are you coming?"
    mc "Yes, I am."
    liam "Perfect! Alright, please excuse me."
    liam "[pete] is probably waiting for me."
    mc "Yeah, sure. Go ahead."
    liam "Thanks. Let's talk later, okay?"
    scene ep5_277 with dissolve
    joe "What's up, [mc]!"
    mc "...Good morning, [joe]."
    leo "Hello, [yui]~!"
    yui "...Hi, [leo]."
    scene black with dissolve
    s "You worked until lunch time...."
    scene ep5_278 with dissolve
    liam "We're going for an Italian food today."
    liam "Do you want to come with us, [mc]?"
    joe "You better join us, man. The food is really delicious!"
    u "I know that I've turned them down many times already, but..."
    scene ep5_279 with dissolve
    u "There is something more important that I want to do now."
    mc "I'm sorry, guys."
    liam "....It's alright. Don't worry about that."
    liam "Let's go, [joe]."
    joe "Yeah, sure."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_280 with dissolve
    u "I've been working here for awhile, but I haven't paid much attention to that thing yet..."
    u "Let's just go see where they are at in the building..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_281 with dissolve
    u "................."
    u "....There is one right there."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_282 with dissolve
    u "................."
    u "...That's another one."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_283 with dissolve
    u "................."
    u "...It's up there."
    u "Well, this building actually has more security cameras than I thought."
    u "I know that I can just get rid of any evidence, but it will be better if I don't get caught by these cameras."
    scene ep5_284 with dissolve
    wendy "*Song hums*....Hmmmm~"
    scene ep5_285 with dissolve
    wendy "(....Hm? Isn't that [mc]?)"
    wendy "(Why does he keep staring at the security camera like that?)"
    wendy "................."
    scene ep5_286 with dissolve
    wendy "What were you doing, [mc]?"
    mc "Hm? [wendy]?"
    wendy "Yeah. Why did you keep staring at that security camera?"
    wendy "What's wrong?"
    mc "................"
    scene ep5_287 with dissolve
    mc "Nothing. I was just wondering if it's working."
    wendy "....Is that so?"
    mc "....[wendy]."
    wendy "...O-Okay. I get it."
    mc "By the way, is an elevator broken?"
    mc "Why were you walking instead of taking one?"
    scene ep5_288 at eyesblink("Ch.2/Ep.1/Scenes/ep5_288.jpg", "Ch.2/Ep.1/Scenes/ep5_288_blink.jpg", 1) with dissolve
    wendy "...Well, I like walking. It keeps me healthy."
    wendy "So, I sometimes walk downstairs instead of taking an elevator."
    mc "I see..."
    wendy "By the way, have you heard about tonight's party yet?"
    mc "Yes, I have."
    wendy "That's great then. I'm going to buy a dress for tonight and find something to eat."
    wendy "Have you eaten anything yet? Would you like to come with me?"
    menu:
        "Sure, let's go. [wendy1]":
            $ ch2ep1gowithwendy = 1
            $ wendy_ch2_ep1 += 1
            $ wendy_relationship += 1
            scene ep5_289_a at eyesblink("Ch.2/Ep.1/Scenes/ep5_289_a.jpg", "Ch.2/Ep.1/Scenes/ep5_289_a_blink.jpg", 1) with dissolve
            mc "Sure, let's go then."
            wendy "Really? Are you really going to come with me?"
            mc "Yeah, why are you so surprised?"
            wendy "*Giggles* Nothing. You seemed busy doing something, so I was just asking without expecting you to say yes."
            mc "I'm starting to feel hungry, so..."
            wendy "Alright then, let's not waste any more time here. Let's go."
            mc "Sure."
            scene black with dissolve
            $ renpy.pause()
            scene black with dissolve
            s "*A few moments later*............"
            scene ep5_290 with fade
            cg "Welcome, customers~!"
            cg "Feel free to look around, and ask if you need help."
            scene ep5_291 with dissolve
            wendy "Umm... What should I wear for tonight...?"
            wendy "This one looks good, but so does the other."
            mc "..............."
            scene ep5_292 with dissolve
            wendy "Hey, [mc]."
            mc "Yeah...?"
            wendy "Can you help me pick?"
            mc "Why me? I'm not the one who is going to wear it."
            wendy "You're right, but you can help me decide which one looks good on me."
            wendy "Come on! Just pick the best-looking one in your opinion."
            mc ".................."
            scene ep5_293 with dissolve
            mc "Alright, there it is then."
            wendy "Hm? Which one?"
            mc "This one."
            wendy "That one?"
            mc "...Yeah."
            wendy "I see... Alright, let me try it then."
            scene black with dissolve
            $ renpy.pause()
            scene ep5_294 with dissolve
            mc "................"
            if ch2ep1answeralice == 1:
                $ ch2ep1alicemessage = True
                $ newmessage = True
                $ alice_messages_show = True
                $ alice_newmessage = True
                $ phone_alert = True
                $ renpy.sound.play("sfx/phone vibrating.mp3")
                s "*Phone vibrates*..........."
                stop sound
                u "Hm....? Did someone send me a message?"
                scene ep5_295 with dissolve
                u "Let's check the message...."
                u "Okay, it's from [alice]. She's asking if she can come see me tonight."
                u "Well, I already have a plan for tonight. Let's just tell her that."
            else:
                scene black with dissolve
                $ renpy.pause()
            scene ep5_296 with dissolve
            u "................."
            u "...Why is she taking so long?"
            if ch2ep1helpwendy == 1:
                scene black with dissolve
                $ renpy.pause()
                scene ep5_296_a1 with dissolve
                wendy "*Hums* Hmmm~"
                wendy "(Well, I think this dress suits me very well.)"
                wendy "(I can't wait to show it to [mc].)"
                scene ep5_296_a2 with dissolve
                wendy "(Hm...?)"
                wendy "(*Sighs* Here comes a problem. I can't reach my hands behind my back.)"
                wendy "(What should I do? I can't zip my dress up....)"
                wendy "(..................)"
                wendy "(...Well, there is no other way.)"
                scene black with dissolve
                $ renpy.pause()
                scene ep5_297 with dissolve
                wendy "[mc]."
                mc "...Yeah?"
                wendy "I need your help. Can you come in here for a sec?"
                mc ".............."
                mc "...Okay."
                scene black with dissolve
                $ renpy.pause()
                scene ep5_297_a1 with dissolve
                mc "What's wrong?"
                wendy "I can't zip my dress up. I can't reach my hands there."
                wendy "Could you zip it up for me, please?"
                mc "Yeah, sure."
                scene ep5_297_a2 with dissolve
                mc "Like this?"
                wendy "Yeah, that's right."
                scene ep5_297_a3 with dissolve
                mc "Alright, done."
                wendy "Thanks a lot."
                mc "You're welcome. Is there anything else you want me to help with?"
                wendy "No, thanks."
                mc "Alright, I'll wait for you outside, then."
                wendy "Sure, I'll follow you real soon."
                scene black with dissolve
                s "*A few more minutes later*........"
            else:
                scene black with dissolve
                s "*A few more minutes later*........"
            scene ep5_297 with dissolve
            wendy "...[mc]."
            mc "Hm....?"
            scene ep5_298 at eyesblink("Ch.2/Ep.1/Scenes/ep5_298.jpg", "Ch.2/Ep.1/Scenes/ep5_298_blink.jpg", 1) with dissolve
            wendy "I've finished changing..."
            wendy "What do you think?"
            wendy "Do I look good in this dress?"
            mc "..............."
            menu:
                "You look perfect. [wendy2]":
                    $ ch2ep1wendydress = 1
                    $ wendy_ch2_ep1 += 2
                    $ wendy_relationship += 2
                    scene ep5_299_a at eyesblink("Ch.2/Ep.1/Scenes/ep5_299_a.jpg", "Ch.2/Ep.1/Scenes/ep5_299_a_blink.jpg", 1) with dissolve
                    mc "You look perfect."
                    wendy "Really? You didn't just say it to make me happy, right?"
                    mc "No, I didn't. I really think that."
                    wendy "*Giggles* Hehe... You've got a good taste, [mc]."
                    wendy "I also like this dress, too."
                    wendy "Alright, I'll take this one."
                "Not bad.":
                    $ ch2ep1wendydress = 2
                    scene ep5_299_d at eyesblink("Ch.2/Ep.1/Scenes/ep5_299_d.jpg", "Ch.2/Ep.1/Scenes/ep5_299_d_blink.jpg", 1) with dissolve
                    mc "Well, you look not bad."
                    wendy "Hm? That's it?"
                    mc "Yeah..."
                    wendy "Well, I really like this dress. I'll take it, then."
            scene black with dissolve
            s "*A few more minutes later*........."
            scene ep5_300 with dissolve
            cg "Thank you, customers!"
            cg "Please, come back again next time!"
            scene black with dissolve
            $ renpy.pause()
            scene ep5_301 with dissolve
            wendy "Wait a sec, [mc]."
            mc "Hm? What's wrong?"
            wendy "I forgot to ask if you wanted to buy yours, too."
            wendy "Should we go back?"
            mc "Don't worry about that. I've already got one."
            wendy "Okay then, let's just go find something to eat!"
            mc "Sure."
            if ch2ep1helpwendy == 1:
                scene ep5_301_a with dissolve
                wendy "By the way... It looks like we're dating, don't you think?"
                mc "Hm? What made you think that?"
                wendy "Well, we went to buy my dress together, and now we're about to eat together..."
                mc "Well, you invited me for help you, so...."
                wendy "*Giggles* I know! I was just kidding!"
            scene black with dissolve
            s "*About half an hour later*........."
            scene ep5_302 with dissolve
            wendy "Alright, thank you for helping me."
            wendy "I'm going back to my department now."
            wendy "See you tonight."
            mc "Yeah, see you."
            scene black with dissolve
            s "*Many hours later*............"
        "I have something else to do.":
            $ ch2ep1gowithwendy = 2
            scene ep5_289_d at eyesblink("Ch.2/Ep.1/Scenes/ep5_289_d.jpg", "Ch.2/Ep.1/Scenes/ep5_289_d_blink.jpg", 1) with dissolve
            mc "Sorry. I still have something really important to do."
            wendy "Oh... It's alright. I was just asking as a formality."
            wendy "It's obvious that you're in the middle of doing something."
            mc "................."
            wendy "Don't mind me. I'm leaving now. You can keep doing your thing now."
            mc "See you later then."
            wendy "Yeah, see you later."
            scene black with dissolve
            s "*Many hours later*............"
    jump ch2ep1getready
label ch2ep1getready:
    scene ep5_303 with dissolve
    stop music fadeout 3.0
    yui "Alright, it's time to get off work."
    yui "Let's go, [mc]. [zeke] and [rin] are waiting for us."
    mc "Yeah, sure."
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep4_3.mp3" fadein 3.0
    $ bgm = "LiQWYD - Birthday"
    scene ep5_304 with fade
    rin "Okay, we're home."
    rin "Now, let's just go get ready for tonight."
    rin "Wait right here when you guys are ready, okay?"
    zeke "Got it."
    yui "Yeah, sure."
    scene black with dissolve
    scene ep5_305 with dissolve
    u "Alright, let's go take a shower, and get myself ready..."
    scene black with dissolve
    s "*Twenty minutes later*......."
    scene ep5_306 with dissolve
    u "Okay... I think I look good enough for the party."
    u "Let's go downstairs and see if everyone is ready."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_307 with dissolve
    u "Hm...? No one is here?"
    u "Am I the first person who is ready?"
    unknown "Yes, that's right!!"
    scene ep5_308 with dissolve
    u "Hm...?"
    scene ep5_309 with dissolve
    u "Oh... They're right there."
    u "But, [rin] is nowhere to be seen."
    u "I guess she's still in her room, then."
    scene ep5_310 with dissolve
    yui "Come! Show me what you can do, [mika]!"
    u "Well, it seems like they're having fun..."
    zeke "Fight, [mika]!"
    mika "N-N-No...!!"
    scene ep5_311 with dissolve
    yui "Yes! I won!"
    yui "Hehehehe!"
    mika "*Sighs* I'm so bad...."
    zeke "Don't think like that. Everyone has to start somewhere."
    zeke "You can't just be good at something on the first try."
    scene ep5_312 with dissolve
    zeke "Leave it to me. I'll beat her for you!"
    mika "Thank you..."
    yui "*Giggles* What did you say? You? Beat me?"
    yui "*Giggles* That's such a nice joke, [zeke]!"
    zeke "Oh... What an innocent young brat. You have no idea who I am."
    scene ep5_313 with dissolve
    yui "Why? Are you a world champion of foosball or what?"
    zeke "No, I'm not, but just you wait, [yui]...."
    yui "Duh! I'm not afraid of you. Come on, try me!"
    mika "Fight, [zeke]..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_314 with dissolve
    mika "Wow! You really won, [zeke]!"
    zeke "See?! What did I say?! I told you that I would beat her for you!"
    mika "And you really did. Well done!"
    zeke "Hahahaha!"
    yui "H-How is this even possible? H-How did I lose?"
    yui "I've played this game since I was a kid, and I'm pretty sure that I'm really good at it..."
    scene ep5_315 with dissolve
    zeke "Yes, [yui]. You're really good at this game, but..."
    yui "...But what?"
    zeke "I'm just better than you! Hahahaha!"
    yui "Tsk! You can't stop bragging, can you?"
    yui "Come! Let's play one more round. I want to see if that win was just a fluke!"
    zeke "Bring it on!"
    scene black with dissolve
    s "*A few minutes later*.........."
    scene ep5_316 with dissolve
    zeke "Fufu... Hahahaha!!"
    yui "Ugh...!"
    zeke "What do you say now, [yui]? Was it just a fluke, or not?"
    zeke "We can play another round if you want more proof, but the result will still be the same!"
    zeke "Hahahahaha!"
    mika "*Giggles* Stop that, [zeke]. I'm starting to feel scared of you."
    u "Well, it seems like they're done playing. Let's just join them."
    scene ep5_317 with dissolve
    mc "Hey, guys..."
    zeke "Oh...?!"
    mika "Hello, [mc]."
    scene ep5_318 with dissolve
    zeke "You look good in that suit, man."
    mika "I couldn't agree more. You look like a completely different person than I know."
    mc "Thank you, I guess?"
    yui "Hey, [mc]!"
    scene ep5_319 with dissolve
    mc "Hm? What's wrong, [yui]?"
    yui "Can you come here for a sec?"
    mc "But why?"
    yui "Come on! Just come right here, then I will tell you."
    mc "...Alright, if you say so."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_320 with dissolve
    yui "Do you know how to play foosball?"
    if foosball == 1:
        mc "...Yeah, I do."
        yui "Are you good at it?"
        mc "...I think so, why?"
        yui "That's perfect! I want you to play against [zeke] and beat him for me."
    else:
        mc "...I've never played it before, why?"
        yui "That sucks..."
        yui "But, you're very multi-talented and a fast learner, aren't you?"
        yui "I'll teach you how to play it. Can you play against [zeke] and beat him for me, please?"
        scene black with dissolve
        s "*A few minutes later*........"
        scene ep5_320 with dissolve
        yui "Do you understand it now?"
    mc "....But, why do I need to do that?"
    yui "Come on, please. If you beat him, I will do anything you want me to."
    mc "..................."
    mc "...Alright then."
    scene ep5_321 with dissolve
    zeke "What was that? What were you guys whispering about?"
    yui "Ha! You volunteered to play for [mika], right?"
    yui "I've also got someone to play for me, too!"
    zeke "W-What?!"
    mc "................."
    scene ep5_322 with dissolve
    yui "Why? Are you scared that you will lose?"
    zeke "Duh! Who's scared? Me?"
    zeke "You asked [mc] to play for you, then what?"
    zeke "I'm not scared of him. I'm the best!"
    mika "What a good fighting spirit you have!"
    scene ep5_323 with dissolve
    zeke "Are you ready, [mc]?"
    mc "...Yeah."
    if foosball == 1:
        zeke "I lost to you last time, but I won't lose again!"
    yui "Beat him up, [mc]!"
    mika "Fighting, [zeke]!"
    scene ep5_324 with dissolve
    zeke "Come! Bring it on, [mc]!"
    mc "................"
    scene black with dissolve
    s "*A few minutes later*........"
    scene ep5_325 with dissolve
    yui "Ha! That was quite easy."
    yui "You aren't as good as you bragged about, are you?"
    zeke "T-That was impossible! H-How did I lose?"
    mc "................"
    mika "[zeke]....."
    zeke "O-One more round!"
    scene black with dissolve
    s "*A few minutes later*........"
    scene ep5_326 with dissolve
    yui "Hahahaha! You lost again!"
    yui "*Giggles* How does it taste, [zeke]? The taste of defeat!"
    zeke "Ugh...!"
    if foosball == 1:
        zeke "...Again. I lost to you again, [mc]."
    mc "..................."
    mika "Don't be so sad. It's just a game, [zeke]...."
    scene ep5_327 with dissolve
    rin "Guys..."
    zeke "Hm...?"
    yui "Oh, [rin]..."
    scene ep5_328 with dissolve
    rin "Sorry for keeping you waiting. I'm ready now."
    yui "*Giggles* It's alright! We were having pretty good fun while waiting for you!"
    zeke "Ugh...."
    rin "Wow! You look so handsome today, [mc]."
    mc "...Thank you."
    scene ep5_329 with dissolve
    rin "Alright then, let's not waste any more time here."
    rin "We should get going now."
    zeke "Yeah, I agree."
    mika "Have fun, [zeke]."
    scene ep5_330 with dissolve
    zeke "Alright, let's go, guys!"
    mc "..............."
    mika "Enjoy the party, everyone."
    rin "Of course, we will!"
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    s "*About an hour later*.........."
    scene ep5_331 with fade
    rin "Okay, here we are..."
    yui "Wow... This house looks very good."
    zeke "I know, right? I wish I could have a house like this someday."
    rin "Me, too."
    scene ep5_332 with dissolve
    rin "Alright, let's go inside."
    yui "Yeah, sure."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_333 with dissolve
    rowan "Oh! Welcome, everyone."
    rowan "Thank you for coming here tonight."
    rin "We should be the ones thanking you. It's our honor to be here."
    yui "Yeah, she's right."
    yui "There aren't many company owners out there who are friendly enough to invite their employees to their house like you."
    scene ep5_334 with dissolve
    rowan "*Smiles* Well, it's because I don't see you guys as my employees, but family members."
    rin "Aw..."
    rowan "Alright, please excuse me. I've got to meet other people, too."
    rowan "Feel free to drink and eat anything you want. Make yourself at home, okay?!"
    zeke "Yeah, sure!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_335 with dissolve
    rin "Alright then, we should say goodbye here for now."
    rin "I'm sure you guys have something you want to do, too."
    rin "We'll meet here again when the party is over. How does that sound?"
    zeke "I agree with that."
    yui "Me, too."
    mc "....Yeah."
    rin "Great. Then, see you guys later!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_336 with dissolve
    stop music fadeout 3.0
    u ".................."
    u "...Alright, I'm free now. What should I do?"
    u "Well, I came here to look for some information about the blueprint of the latest version of Xecon gear."
    u "It's pretty hard to go into the lab in the company building."
    u "However, the blueprint is something very important. I'm pretty sure that he keeps the original one himself."
    u "It might be in his room. I need to sneak there."
    scene black with dissolve
    play music "sfx/ch2ep1_2.mp3" fadein 3.0
    $ bgm = "Tokyo Music Walker - Your Little Wings"
    $ renpy.pause()
    $ ch2ep1freeroam = True
    $ area = "entrance"
    jump ch2ep1_freeroam
label ch2ep1_freeroam:
    if ep5hiddenimages_count == 5:
        $ ep5hiddenimages = True
    if area == "bedroom":
        jump ch2ep1_endfreeroam
    call screen ch2ep1house
label ep5_entrance_talk:
    if ep5entrance_pic == False:
        scene ep5_entrance_photo
    else:
        scene ep5_entrance
    u "[liam], [joe], and [david] are right there."
    u "What should I do?"
    menu:
        "[smgr]Approach them":
            if ch2ep1entrancetalk == False:
                u "Well, I don't want to be a dick. Let's just go say hi."
                scene black with dissolve
                scene ep5_337 with dissolve
                mc "Hey, guys..."
                liam "Hm...?"
                scene ep5_338 at eyesblink("Ch.2/Ep.1/Scenes/ep5_338.jpg", "Ch.2/Ep.1/Scenes/ep5_338_blink.jpg", 1) with dissolve
                liam "Oh! Hello, [mc]!"
                joe "Wait? Are you actually [mc]?"
                david "You look like a completely different person wearing that suit, man."
                joe "I know, right?!"
                liam "Have you been here for awhile?"
                mc "No, I just got here."
                mc "Alright, I just came to say hi. Enjoy the party, guys."
                joe "Sure. You, too!"
                scene black with dissolve
                $ ch2ep1entrancetalk = True
            else:
                u "I've already talked to them."
            jump ch2ep1_freeroam
        "Leave":
            u "Forget it."
            jump ch2ep1_freeroam
label ep5_livingroom_es:
    if ep5livingroom_pic == False:
        scene ep5_livingroom_photo
    else:
        scene ep5_livingroom
    u "That's [sally] and [eira]...."
    menu:
        "Go greet them\n[eira1][smec] & [sally1]":
            if ch2ep1livingroomes == False:
                u "Well, let's just go greet them for a bit."
                scene black with dissolve
                scene ep5_339 with dissolve
                mc "Hey, girls..."
                scene ep5_340 with dissolve
                eira "...Hm?"
                scene ep5_341 at eyesblink("Ch.2/Ep.1/Scenes/ep5_341.jpg", "Ch.2/Ep.1/Scenes/ep5_341_blink.jpg", 1) with dissolve
                eira "Hello, [mc]."
                sally "Wow! You look very handsome today, [mc]!"
                mc "Thank you. Both of you look beautiful, too."
                eira "Aw..."
                sally "*Smiles* Hehe. Thanks!"
                mc "What were you guys doing?"
                sally "Nothing special. We were just talking."
                mc "I see..."
                scene ep5_342 with dissolve
                mc "Alright, I won't bother you guys anymore. Please, continue."
                mc "I just wanted to say hi."
                eira "Have fun, [mc]."
                mc "Thanks. You, too."
                scene black with dissolve
                $ ch2ep1livingroomes = True
                $ sally_ch2_ep1 += 1
                $ sally_relationship += 1
                $ eira_ch2_ep1 += 1
                $ eira_relationship += 1
            else:
                u "I've already talked to them."
            jump ch2ep1_freeroam
        "Leave":
            u "Forget it."
            jump ch2ep1_freeroam
label ep5_livingroom_leo:
    if ep5livingroom_pic == False:
        scene ep5_livingroom_photo
    else:
        scene ep5_livingroom
    u "That's [leo] and... I don't know who that woman is."
    menu:
        "[smgr]Get closer":
            if ch2ep1livingroomleo == False:
                scene black with dissolve
                scene ep5_343 with dissolve
                leo "Oh... I think I'm the luckiest person here today."
                unknown "*Giggles* What made you think that?"
                leo "Because I've met such a beautiful angel like you."
                unknown "*Giggles* Aww..! Thank you. You're so sweet!"
                u ".................."
                u "...Well, [leo] is doing [leo]'s thing as usual. I should leave them alone."
                scene black with dissolve
                $ ch2ep1livingroomleo = True
            else:
                u "I should leave them alone."
            jump ch2ep1_freeroam
        "Leave":
            u "Forget it. Just leave them alone."
            jump ch2ep1_freeroam
label ep5_kitchen_zeke:
    if ep5kitchen_pic == False:
        scene ep5_kitchen_photo
    else:
        scene ep5_kitchen
    u "I wonder what [zeke] is doing there..."
    menu:
        "[smgr]Get closer":
            if ch2ep1kitchenzeke == False:
                scene black with dissolve
                scene ep5_344 with dissolve
                zeke "Hahahaha! Is that so?"
                u "It seems like [zeke] is having a great time talking with his co-workers."
                u "I think I shouldn't bother them. Let's just leave them alone."
                scene black with dissolve
                $ ch2ep1kitchenzeke = True
            else:
                u "I should leave them alone."
            jump ch2ep1_freeroam
        "Leave":
            u "Forget it. Let's just leave them alone."
            jump ch2ep1_freeroam

label ep5_kitchen_pete:
    if ep5kitchen_pic == False:
        scene ep5_kitchen_photo
    else:
        scene ep5_kitchen
    u "That's [pete] and... What is her name again?"
    u "...San...dra? Yeah, that's right. [sandra]."
    menu:
        "[smgr]Approach them":
            if ch2ep1kitchenpete == False:
                scene black with dissolve
                scene ep5_345 with dissolve
                pete "What do you think? How does it sound?"
                sandra "This Saturday?"
                pete "Yeah..."
                scene ep5_346 with dissolve
                pete "...Hm?"
                scene ep5_347 at eyesblink("Ch.2/Ep.1/Scenes/ep5_347.jpg", "Ch.2/Ep.1/Scenes/ep5_347_blink.jpg", 1) with dissolve
                pete "Oh! Is that you, [mc]?"
                mc "Hi, [pete]. Hello, [sandra]."
                sandra "Hello, [mc]."
                pete "Wow. I almost didn't recognize you."
                pete "You look so good today, man."
                mc "Thank you."
                pete "Do you want to drink with us for a bit?"
                mc "Thanks, but I'm good. Don't worry about me."
                mc "You guys seemed to be in the middle of something. Please, carry on."
                mc "I just came to say hi."
                pete "Oh, okay then. Have fun, [mc]."
                scene black with dissolve
                $ ch2ep1kitchenpete = True
            else:
                u "I've already talked to them."
            jump ch2ep1_freeroam
        "Leave":
            u "Forget it."
            jump ch2ep1_freeroam
label ep5_kitchen_faye:
    if ep5kitchen_pic == False:
        scene ep5_kitchen_photo
    else:
        scene ep5_kitchen
    u "Hm...? Isn't that [faye]"
    u "I wonder what she is doing there alone."
    menu:
        "Go talk to her [faye1]":
            if ch2ep1kitchenfaye == False:
                scene black with dissolve
                scene ep5_348 with dissolve
                faye "................"
                scene ep5_349 with dissolve
                faye "Hm...?"
                scene ep5_350 with dissolve
                faye "Hey, [mc]. That suit looks good on you."
                mc "Thank you. That dress looks good on you, too."
                faye "*Smiles* Thanks. This is one of my favorite dresses."
                mc "I see..."
                scene ep5_351 with dissolve
                mc "What were you doing just now? Why are you here alone?"
                faye "Oh... I was checking an email."
                if ch2ep1photosession == 1:
                    faye "[allison]. Do you remember her?"
                    mc "Yeah, the photographer from that day."
                    faye "Yeah, she just sent me a set of in-game photos that we took."
                else:
                    faye "The photographer just sent me a set of in-game photos that will be used for advertising."
                mc "I see...."
                faye "Wanna hang out for a bit?"
                mc "...Okay. That sounds great."
                scene black with dissolve
                scene ep5_352 with dissolve
                s "You spent some time chatting with [faye] for awhile..."
                $ ch2ep1kitchenfaye = True
                $ faye_ch2_ep1 += 1
                $ faye_relationship += 1
                scene black with dissolve
            else:
                u "I've already talked to her."
            jump ch2ep1_freeroam
        "Leave":
            u "Forget it. She seems to be busy right now."
            jump ch2ep1_freeroam
label ep5_pool_yui:
    if ep5pool_pic == False:
        scene ep5_pool_photo
    else:
        scene ep5_pool
    u "That's [yui]. I wonder what she is doing there..."
    menu:
        "Approach her [yui1]":
            if ch2ep1poolyui == False:
                scene black with dissolve
                scene ep5_353 with dissolve
                mc "Hey..."
                yui "...Hm?"
                scene ep5_354 at eyesblink("Ch.2/Ep.1/Scenes/ep5_354.jpg", "Ch.2/Ep.1/Scenes/ep5_354_blink.jpg", 1) with dissolve
                yui "Oh, [mc]?"
                yui "What are you doing here?"
                mc "I was just roaming around, then I saw you."
                mc "What were you doing?"
                yui "I'm kind of hungry. So, I'm waiting for the barbecue."
                mc "Well, listening to you makes me hungry, too."
                mc "I'll just grab some then."
                scene black with dissolve
                scene ep5_355 with dissolve
                s "You spent some time eating barbecue with [yui]..."
                $ ch2ep1poolyui = True
                $ yui_ch2_ep1 += 1
                $ yui_relationship += 1
                scene black with dissolve
            else:
                u "I've already talked to her."
            jump ch2ep1_freeroam
        "Leave":
            u "Forget it. Let's leave her alone."
            jump ch2ep1_freeroam
label ep5_pool_re:
    if ep5pool_pic == False:
        scene ep5_pool_photo
    else:
        scene ep5_pool
    u "[rin] is with [elaine] right there. What should I do?"
    menu:
        "Approach them\n[elaine1][smec] & [rin1]":
            if ch2ep1poolre == False:
                scene black with dissolve
                scene ep5_356 with dissolve
                elaine "*Giggles* Really? That's very interesting..."
                rin "*Giggles* I know, right?"
                mc "Hi..."
                scene ep5_357 with dissolve
                elaine "Hm? Oh! Hello, [mc]."
                elaine "Wow... Can I take a photo of you today?"
                elaine "*Giggles* I don't think I'll ever see you dressed like this again."
                mc "................"
                elaine "*Giggles* Chill! I was just kidding!"
                mc "I know that..."
                scene ep5_358 at eyesblink("Ch.2/Ep.1/Scenes/ep5_358.jpg", "Ch.2/Ep.1/Scenes/ep5_358_blink.jpg", 1) with dissolve
                mc "By the way, what were you guys doing?"
                mc "Why did you guys come out here?"
                rin "Well, I saw the pool right here. I wanted to see it close, so I came here."
                rin "[elaine] was already here before me, so we decided to take a seat and chat for a bit."
                mc "I see..."
                rin "Would you like to join us?"
                mc "......Okay."
                scene black with dissolve
                scene ep5_359 with dissolve
                s "You spent time chatting with [rin] and [elaine] for awhile...."
                scene black with dissolve
                $ ch2ep1poolre = True
                $ elaine_ch2_ep1 += 1
                $ eliane_relationship += 1
                $ rin_ch2_ep1 += 1
                $ rin_relationship += 1
            else:
                u "I've already talked to them."
            jump ch2ep1_freeroam
        "Leave":
            u "Forget it. Let's leave her alone."
            jump ch2ep1_freeroam
label ep5_balcony_wendy:
    if ep5balcony_pic == False:
        scene ep5_balcony_photo
    else:
        scene ep5_balcony
    u "Hm...? Isn't that [wendy]?"
    u "I wonder what she is doing here alone."
    menu:
        "Approach her [wendy1]":
            if ch2ep1balconywendy == False:
                scene black with dissolve
                scene ep5_360 with dissolve
                mc "Hi...."
                wendy "....Hm?"
                scene ep5_361 at eyesblink("Ch.2/Ep.1/Scenes/ep5_361.jpg", "Ch.2/Ep.1/Scenes/ep5_361_blink.jpg", 1) with dissolve
                wendy "Oh! Hello, [mc]."
                wendy "You look very handsome tonight."
                mc "Thanks."
                wendy "Is there something that you want?"
                mc "I was just walking around, then I saw you here alone."
                mc "So, I decided to come greet you."
                wendy "I see..."
                mc "By the way, what are you doing here alone?"
                wendy "...Well, I don't like being inside the house now. It's too noisy."
                mc "Oh..."
                scene ep5_362 with dissolve
                wendy "Out of the other places in this house, I like this place the most."
                wendy "Can you feel the wind and smell the sea?"
                wendy "Look at the sky, you can also see a lot of beautiful stars up there."
                wendy "This place is so peaceful..."
                mc "Yeah, I agree with that..."
                scene black with dissolve
                scene ep5_363 with dissolve
                s "You spent time hanging out with [wendy] for awhile..."
                scene black with dissolve
                $ ch2ep1balconywendy = True
                $ wendy_ch2_ep1 += 1
                $ wendy_relationship += 1
            else:
                u "I've already talked to her."
            jump ch2ep1_freeroam
        "Leave":
            u "Forget it. Let's just leave her alone."
            jump ch2ep1_freeroam
label ch2ep1_endfreeroam:
    stop music fadeout 3.0
    $ ch2ep1endfreeroam = True
    scene black
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/rindrowning.mp3" fadein 3.0
    $ bgm = "Mauro Somm - What You Used To Be"
    scene ep5_364 with dissolve
    u ".................."
    u "...Okay. This is the opportunity."
    u "Everyone seems to be busy. No one is paying attention to me."
    scene ep5_365 with dissolve
    u "[rowan]'s room isn't on the first floor."
    u "Let's go upstairs and look for it..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_366 with dissolve
    u "It isn't on the second floor, either."
    u "There is the only floor left."
    u "I'm sure that his room must be up there, on the third floor."
    u "Let's not waste any more time here then..."
    scene black with dissolve
    scene ep5_367 with dissolve
    u "There it is...."
    u "Look at that bunch of screens. This must be his room for sure."
    u "Now, I just need to search for the blueprint."
    u "Where could he possibly keep it...?"
    scene ep5_368 with dissolve
    unknown "What are you doing up here?"
    u "Hm...?!"
    scene ep5_369 with dissolve
    u "Oh shit... If I recall correctly, that woman is [rowan]'s secretary."
    u "I thought no one was up here. How come she is up here?"
    u "Actually, why is she in his room?"
    ana "Hello? What are you doing up here?"
    scene ep5_370 with dissolve
    mc "O-Oh! I'm just looking for the bathroom."
    ana "The bathroom? There is one on the first floor."
    mc "Really? I didn't see it when I was looking for it. My bad."
    u "...This is bad. Only if I knew she was up here, I would just sneak up behind her, and put her to sleep."
    u "But, she already saw my face. I can't do anything now."
    scene ep5_371 with dissolve
    ana "................."
    mc "...Can you please show me where the bathroom is?"
    mc "I'm pretty bad at directions."
    ana "................."
    scene ep5_372 with dissolve
    ana "...Okay. Follow me."
    mc "Thank you very much. You're so kind."
    ana "You're welcome. By the way, can you do me a favor?"
    mc "Yes, sure. What do you want me to do?"
    ana "Don't come up here again. No one is allowed to come up here, except the president."
    mc "....Okay. I won't."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ep.3/ep3_1.mp3" fadein 3.0
    $ bgm = "Roa - Fresh Time"
    scene ep5_373 with dissolve
    u "By the way, she said no one is allowed to go up there, except [rowan]."
    u "But, she was also up there, wasn't she?"
    u "I wonder what relationship she has with [rowan]."
    u "Is she just his secretary, or is she more than that...?"
    scene ep5_374 with dissolve
    u "...Hm?"
    u "That's [rowan] and... Who are those women?"
    u "I've never seen them before."
    scene ep5_375 with dissolve
    unknown "What's wrong, [rowan]?"
    unknown "What are you looking at?"
    rowan "Please, wait a second, Ms. Taylor."
    scene ep5_376 with dissolve
    ana "Sir...."
    rowan "What happened, [ana]? Why did he come down here with you?"
    ana "I found him in your room. He said that he was just looking for the bathroom."
    ana "So, I was on the way to show him the bathroom."
    rowan "Is that so? You don't need to go up there, [mc]."
    rowan "There is one down here."
    mc "I'm sorry. I didn't know that."
    rowan "It's alright! I don't blame you. You're just here for the first time."
    mc "Thank you, president."
    scene ep5_377 with dissolve
    unknown "Excuse me, [rowan]. Who is this young man?"
    unknown "I've never seen him before."
    rowan "Oh! He's a new employee, Ms. Taylor."
    unknown "Jeez... You keep telling your employees to stop calling you by your position, but your name."
    maya "Yet you keep calling me by my surname? I've told so many times to just call me, [maya]."
    maya "It's not like we just met, is it?"
    rowan "I'm sorry..."
    scene ep5_378 with dissolve
    maya "So, he is one of the new employees that you hired."
    maya "Would you mind introducing him to me?"
    rowan "Of course not! Come here, [mc]."
    u "....Hm? His hand...."
    scene ep5_379 with dissolve
    rowan "Introduce yourself, [mc]."
    u "Judging from the way [rowan] talked to her. She must be someone very important..."
    rowan "This woman is an investor in our company."
    u "Okay, I'm right..."
    mc "Nice to meet you, madam. My name is [mc]."
    mc "I'm working in the game development department."
    maya "Nice to meet you, too. I'm [maya] and this is my daughter, [skylar]."
    skylar "I'm [skylar]. Nice to meet you, [mc]."
    scene ep5_380 with dissolve
    rowan "Please, look after him, [maya]."
    rowan "He's a very talented lad. I have very high expectations for him!"
    maya "Hm? Is he really that good?"
    rowan "Yeah, I'm sure that he will soon become one of our best employees!"
    mc ".................."
    scene ep5_381 with dissolve
    rowan "Oh! I almost forgot that you were looking for the bathroom, right?"
    mc "...Yeah, I was."
    rowan "My bad. I won't hold you here any longer then!"
    rowan "[ana]. Show him the way to the bathroom."
    ana "Understood."
    scene ep5_382 with dissolve
    ana "This way...."
    mc "Thank you."
    scene ep5_383 with dissolve
    ana "Here it is...."
    mc "...Oh, this is the bathroom?"
    mc "I thought it wasn't."
    ana ".....Yes, it is."
    mc "Okay then. Thank you very much for bringing me here."
    ana "...You're welcome."
    scene black with dissolve
    s "*A few minutes later*.........."
    scene ep5_384 with dissolve
    u "*Sighs* Well, that was close..."
    u "[ana] seemed to suspect something, but fortunately, she didn't say it out loud."
    u "Perhaps, it was also because she didn't have anything to prove her words."
    u "...I still got what I wanted though. However, I think I'll have to be more careful than before."
    u "Now, let's act like usual and blend in with people at the party."
    scene ep5_385 with dissolve
    u "Hm...?"
    u "What's going on? Why is everyone gathered there?"
    rowan "Thank you for coming here tonight, everyone."
    rowan "This shows that you guys care about me and the company."
    rowan "Also, thank you all for all of your hard work."
    scene ep5_386 with dissolve
    wendy "Hi, [mc]."
    mc "Hm...? Oh, hi again, [wendy]."
    wendy "Where have you been?"
    mc "I just came back from the bathroom."
    wendy "I see..."
    scene ep5_387 with dissolve
    rowan "I have some good news to inform you guys."
    rowan "Though some of you might already know about this, there are still some people who don't."
    rowan "But, we're now ready to tell you about the project we've been working on!"
    wendy "...N-No!!"
    scene ep5_388 with dissolve
    mc "Hm...?"
    elaine "What's wrong, [wendy]?"
    wendy "...It's [luke]. He sent me this video."
    elaine "W-What?! That fucking asshole! What does he want?"
    wendy "He told me to go meet him alone. Otherwise, he said that he will spread the video on the internet..."
    elaine "That fucking piece of shit! Let's go meet him then. I'll go with you."
    wendy "B-But..."
    elaine "Don't worry. I won't let him do what he said."
    elaine "I'll slap his ugly face, and delete the video before he even has a chance to upload it."
    scene ep5_389 with dissolve
    elaine "Let's go, [wendy]!"
    wendy "Okay!"
    u "So, that guy still dares to bother [wendy] despite me telling him not to?"
    u "What should I do?"
    menu:
        "[smgr]Go with them":
            mc "Wait a sec."
            scene ep5_390_a1 with dissolve
            wendy "Hm? What's wrong, [mc]?"
            mc "I told him to not bother you anymore, but it's obvious that he didn't take my words seriously."
            mc "So, I'll go with you guys, too."
            wendy "Really?! Do you really want to come with us?!"
            mc "Yes, I do."
            elaine "That's very good news. You're coming with us. That asshole is surely a dead man."
            scene ep5_390_a2 with dissolve
            stop music fadeout 3.0
            elaine "Alright, let's not waste any more time here."
            elaine "We better get going now."
            wendy "Sure!"
            jump ch2ep1followwendy
        "Let them go alone":
            s "Are you sure that you want to stop her?"
            s "This means you will end any possibility of having a relationship with [wendy]."
            menu:
                "Yes, I am":
                    $ ch2ep1_followwendy = 2
                    scene ep5_390_d with dissolve
                    u "...Well, I think I've helped her enough."
                    u "This is her problem after all."
                    u "I will let her fix the problem by herself."
                    u "Plus, [elaine] is already going with her. I think she should be fine."
                    scene black with dissolve
                    s "*A few hours later*..........."
                    jump ch2ep1end
                "On a second thought":
                    jump ch2ep1followwendy
label ch2ep1followwendy:
    $ ch2ep1_followwendy = 1
    $ wendy_ch2_ep1 += 2
    $ wendy_relationship += 2
    $ elaine_ch2_ep1 += 2
    $ eliane_relationship += 2
    scene black with dissolve
    $ renpy.pause()
    scene ep5_390_a3 with fade
    play music "sfx/ep2_8.mp3" fadein 3.0
    $ bgm = "Lahar - Genesis"
    elaine "Okay. It seems like we've arrived."
    elaine "Are you sure that this is his house?"
    wendy "Yeah, I'm pretty sure. He sent me a location, and it led us here."
    elaine "Okay then, go knock on the door, [wendy]."
    elaine "We'll hide ourselves until he opens it up."
    wendy "Sure."
    scene ep5_390_a4 with dissolve
    wendy "*Knocks*.........."
    unknown "Who's it?"
    wendy "...It's me, [wendy]."
    unknown "Okay. Wait a sec."
    scene ep5_390_a5 with dissolve
    luke "Hello, my sweetheart~!"
    luke "You're finally...."
    scene ep5_390_a6 with dissolve
    luke "...Hm?"
    elaine "You son of a..."
    scene ep5_390_a7 with dissolve
    elaine "Bitch!"
    luke "Ouch...!!"
    scene ep5_390_a8 with dissolve
    luke "Ha! Nice shot, [elaine]."
    elaine "Then, how about you get another one?!"
    luke "Come on! Do it! I'm not scared of you! Not anymore!"
    luke "But, don't blame me if I hit you back then! I'm not as weak as you think I was, [elaine]."
    luke "You can't do anything to me now."
    scene ep5_390_a9 with dissolve
    mc "Then, what about me...?"
    luke "!!!!"
    mc "Didn't I tell you to stop bothering [wendy]."
    mc "But, what's this?"
    luke "F-Fuck..!"
    scene ep5_390_a10 with dissolve
    luke "[wendy]! What the hell is this?"
    luke "Didn't I tell you to come here alone?"
    luke "Why did you have to bring this bitch and that asshole with you?!"
    luke "Why is it so hard for you to listen to me?"
    luke "I just wanted to talk with you."
    scene ep5_390_a11 with dissolve
    elaine "Huh! Why is it so hard for you to understand that she doesn't want to talk to you?!"
    wendy "Yes! Let alone talking, I don't even want to see your face!"
    elaine "Delete that video now! Otherwise, I'm going to kick your ass!"
    scene ep5_390_a12 with dissolve
    luke "Huh! As if I'm going to listen to you, bitch!"
    luke "You know what? I saw this coming from a mile away."
    luke "So, I prepared some presents for you!"
    scene ep5_390_a13 with dissolve
    luke "Come here, guys!"
    elaine "W-What?! Who the fuck are they?!"
    luke "Just you wait. You'll know that soon enough!"
    scene ep5_390_a14 with dissolve
    man1 "Hello, hotties~!"
    wendy "!!!!!"
    luke "Bring me that orange-haired woman."
    luke "And get that red haired bitch and that asshole out of my house!"
    luke "But, be careful of that asshole right there. He's a pretty good fighter."
    man2 "What about this chick?"
    luke "I don't care about that bitch. You can do anything you want with her."
    man1 "Wew~! That's what I wanted to hear~!"
    scene ep5_390_a15 with dissolve
    elaine "Run, [wendy]!"
    wendy "What about you?!"
    elaine "Don't worry about me! I can take care of myself!"
    wendy "B-But...!"
    elaine "Run!!"
    luke "Don't let her run away!"
    scene ep5_390_a16 with dissolve
    mc "Did you forget about me?"
    elaine "...Oh, [mc]?"
    mc "So, you did forget about me."
    mc "Well, let me take care of them. You go wait for me with [wendy] outside."
    elaine "But, there are three of them..."
    mc "Don't worry about that. I'll be fine."
    elaine "O-Okay..."
    scene ep5_390_a17 with dissolve
    man2 "Wow! This man has got some guts!"
    man1 "If I were you, I'd get the hell out of here as fast as I could, man."
    man2 "Yeah, don't you know who we are? We're members of the black tiger gang!"
    mc "I don't care about that."
    man1 "Wew~!"
    luke "What are you guys waiting for?! Beat him up!"
    scene ep5_390_a18 with dissolve
    man1 "I'll make you regret standing up against us!"
    wendy "W-Watch out, [mc]!"
    mc "..............."
    scene ep5_390_a19 with dissolve
    man1 "O-Ouch..!!!!"
    luke "W-What?!!"
    scene ep5_390_a20 with dissolve
    mc "*Sighs* So weak..."
    mc "Well, at first I was just about to ask you nicely, but it looks like it's too late..."
    man2 "H-Ha?! You've got some skills, huh?!"
    luke "You idiot! I told you to be careful of him, didn't I?!"
    scene ep5_390_a21 with dissolve
    mc "Why did you pull a knife up?"
    mc "That thing isn't going to help you at all."
    man2 "Really!? Then, come closer and we'll see if it helps me or not!"
    mc "*Sighs*.............."
    man2 "What's wrong? Are you scared now?!"
    man2 "I don't know how you managed to knock him out, but..."
    scene ep5_390_a22 with dissolve
    man2 "I'm not as weak as him!!! Yahhhh!"
    wendy "[mc]!!!"
    mc "..................."
    mc "A knife will be useful if it's in the right hands, but..."
    scene ep5_390_a23 with dissolve
    man2 "Arghhhh!!!!"
    mc "If it's in your hands, it is nothing more than a chopstick."
    scene ep5_390_a24 with dissolve
    man2 "Ouch!!!!!"
    luke "F-Fuck!!! Why are you guys so weak!"
    luke "I didn't pay you for this!!"
    scene ep5_390_a25 with dissolve
    mc "Listen. I have nothing to do with you guys here."
    mc "I come here for that man behind you."
    mc "So, piss off."
    mc "And don't you dare to come back again. Otherwise, that knife will be in your body instead of on the floor."
    man2 "O-Okay! I-I get it! I-I won't!"
    scene black with dissolve
    $ renpy.pause()
    scene ep5_390_a26 with dissolve
    mc "Now, it's your turn..."
    luke "P-Please, don't hurt me!! I'm sorry!"
    luke "Please, let me go! I'll never show my face to any of you again! I'll do whatever you want!"
    scene ep5_390_a27 with dissolve
    mc "*Sighs* Well then, unlock your phone and give it to me."
    luke "O-Okay! I'll give it to you!"
    mc "[wendy], [elaine], come here."
    wendy "Y-Yeah, we're coming."
    scene ep5_390_a28 with dissolve
    mc "Here you are."
    mc "Find the video and delete it."
    wendy "Thank you so much, [mc]."
    elaine "Well, I can't really let him leave like this."
    elaine "If you aren't going to hurt him, let me do it then!"
    luke "P-Please! I already did what you guys wanted me to!"
    elaine "Well, that's not enough to pay for everything you've tried to do!"
    elaine "And what happened to big brave guy [luke] back then?"
    elaine "Didn't you say you weren't scared of me? Why are you acting like this now?"
    luke "P-Please, d-"
    scene black with dissolve
    luke "Ouch...!"
    luke "Ugh...!"
    luke "Arghh...!"
    scene ep5_390_a29 with dissolve
    wendy "Okay, I deleted the video."
    luke "Ugh... W-Why did you hurt me? I-I promised!"
    elaine "You've got what you deserved!"
    mc "That's it? Was that the only video you had?"
    luke "..................."
    mc "I won't ask you twice..."
    luke "There are more, but they're in my laptop..."
    elaine "You piece of shit!!"
    mc "Where is your laptop?"
    luke "It's in my bedroom...."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_390_a30 with dissolve
    elaine "Ugh...! There are a ton of them!"
    elaine "There are also videos of other girls, too!"
    elaine "You're so disgusting, [luke]."
    wendy "I'm going to delete them all!"
    elaine "Yeah, do it, [wendy]!"
    scene ep5_390_a31 with dissolve
    s "*Phone vibrates*........."
    u "Hm...? There's someone calling me now."
    u "I wonder who it is...."
    scene ep5_390_a32 with dissolve
    u "Oh, it's [rin]..."
    mc "Hello..."
    mc "..................."
    mc "I left with [elaine] and [wendy]."
    mc "................."
    mc "Yeah, I'm sorry. I should've told you guys before."
    mc "................."
    mc "Nothing. You don't need to worry about me."
    mc "................."
    mc "Okay, bye."
    scene ep5_390_a33 with dissolve
    u "...Hm?!"
    scene ep5_390_a34 with dissolve
    mc "Watch out!!"
    wendy "!!!!!!"
    luke "I tried to be as calm as I could, but you keep making me pissed!"
    luke "Die! Both of you, bitches! Yahhhh!!"
    scene black with dissolve
    scene ep5_390_a35 with dissolve
    mc "Move back! Ugh..!"
    wendy "[mc]!!"
    elaine "[mc]!!"
    luke "Y-You!"
    scene ep5_390_a36 with dissolve
    luke "Ugh...!!"
    scene ep5_390_a37 with dissolve
    mc "*Pants*............"
    wendy "T-That's blood! [mc], are you alright?!"
    elaine "L-Let's go to a hospital, [mc]!"
    unknown "Everyone, don't move!!"
    mc "Hm...?"
    scene ep5_390_a38 with dissolve
    elaine "Oh! Finally, you came!"
    police "Hello! We've been reported that there was a crime scene here!"
    wendy "That's right. We were the ones calling you."
    wendy "Please, arrest the guy behind us. He blackmailed and threatened me to come see him here alone."
    wendy "I can show you my inbox messages as evidence."
    wendy "He also tried to stab us with a knife."
    police "Understood!"
    u "I thought it was just in the movies that the police were always the one to come last."
    u "But, it seems like it's the same in real life, too...."
    scene black with dissolve
    s "*A few moments later*............."
    scene ep5_390_a39 with dissolve
    police "Walk!"
    luke "..............."
    wendy "Thank you, officers."
    police "You're welcome. It's our duty to arrest bad people."
    police "However, you might need to go to the police station, too. We'll call you soon."
    wendy "No problem. I'll give you my full cooperation."
    police "Thank you. That will be very helpful."
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    play music "sfx/ch2ep1_1.mp3" fadein 3.0
    $ bgm = "Roa - Winter Magic"
    scene ep5_390_a40 with dissolve
    wendy "Thank you for helping us and saving our lives, [mc]."
    elaine "Yeah, we would've been badly hurt if it wasn't for you."
    mc "You're welcome."
    wendy "By the way, are you sure that you don't need to go to a hospital?"
    mc "Yeah, I didn't get stabbed. It's just a scratch."
    wendy "..................."
    scene ep5_390_a41 with dissolve
    wendy "But, I feel so bad to take you home like this."
    wendy "After all, it was because of me that you got hurt."
    wendy "Our house is on the way to yours. Let's stop by there, and I will dress your wound."
    elaine "Yeah, let's do that. You helped us, so let us help you, too. Okay?"
    mc "................."
    mc "Alright, if you say so..."
    wendy "Lovely! Let's go then!"
    scene black with dissolve
    $ renpy.pause()
    scene black with dissolve
    scene ep5_390_a42 with fade
    elaine "Alright, I don't know how to dress a wound, so I'll get out of the way."
    elaine "But, don't you worry, [wendy] is pretty good at it."
    elaine "Come call me when you guys are done. I'll be waiting in my room."
    wendy "Yeah, sure."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_390_a43 with dissolve
    wendy "Alright then..."
    wendy "Take off your shirt, [mc]."
    mc "...What?"
    wendy "*Giggles* Why are you looking at me like that?"
    wendy "I'm going to dress your wound, but I can't do that unless you take your shirt off."
    mc "...Okay."
    scene black with dissolve
    s "*A few minutes later*.........."
    scene ep5_390_a44 with dissolve
    wendy "*Smiles* Okay, Finished!"
    wendy "You're so lucky the cut isn't very deep. Otherwise, you'd really have to go to a hospital."
    mc "Thank you, [wendy]."
    wendy "*Smiles* You're welcome!"
    scene black with dissolve
    scene ep5_390_a45 with dissolve
    wendy "I know that I already said it a lot, but..."
    wendy "Thank you, [mc]. You're my savior."
    mc "Anytime. If you need my help, just tell me."
    wendy "Aw... You're very sweet."
    wendy "................."
    scene ep5_390_a46 with dissolve
    wendy "[mc]....."
    u "Hm...? What is she trying to..."
    scene black with dissolve
    $ renpy.pause(0.5, hard=True)
    scene ep5_390_a47 at eyesblink("Ch.2/Ep.1/Scenes/ep5_390_a47.jpg", "Ch.2/Ep.1/Scenes/ep5_390_a47_blink.jpg", 1) with dissolve
    u "...do?"
    wendy ".................."
    mc "...What are you doing, [wendy]?"
    wendy "I don't know. I don't even know why I'm doing this, either..."
    mc "...Are you drunk?"
    wendy "No, I'm not. I didn't drink much."
    wendy "Also, since I broke up with [luke], I've never done {b}that{/b} with anyone before..."
    wendy "But, I don't know what is happening now. You look so handsome tonight."
    wendy "And I want you so bad..."
    u "Hm...? Her face is starting to get closer..."
    menu:
        "[smgr]Let it be":
            jump ch2ep1sexwendy
        "Stop her":
            s "Are you sure that you want to stop her?"
            s "This means you will end any possibility of having a relationship with [wendy]."
            menu:
                "Yes, I am.":
                    scene ep5_391_d1 with dissolve
                    mc "No, [wendy]."
                    wendy "...Why?"
                    mc "I helped you because we work in the same company."
                    mc "I've never thought about you in a different way."
                    wendy "................"
                    scene ep5_391_d2 with dissolve
                    wendy "Okay. I get it."
                    mc "...Are you okay?"
                    wendy "*Giggles* Yeah! Don't mind me. I was just out of my mind."
                    wendy "Alright, I'm going to tell [elaine] that we're done."
                    wendy "Then, we'll take you back home."
                    mc "Okay. Thank you."
                    wendy "All good!"
                    $ ch2ep1sexwithwendy = 2
                    jump ch2ep1end
                "On a second thought...":
                    jump ch2ep1sexwendy
label ch2ep1sexwendy:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    play music "sfx/ch2ep1_3.mp3" fadein 3.0
    $ bgm = "Raymouton - Used To Be (feat. Ramonna Abdul & Conner Kazie)"
    scene black with dissolve
    u "...Well, go with it."
    scene ep5_391_a1 with dissolve
    wendy "*Kisses* Mmmmm....[mc]...."
    mc "*Kisses*........"
    u "I never knew her lips were so soft like this..."
    u "She might have the softest lips of any girl I've ever kissed."
    scene ep5_391_a2 with dissolve
    wendy "*Kisses* Mmmmm....."
    mc "*Kisses*..........."
    wendy "(...The way he's kissing feels so nice....)"
    wendy "(...I never knew he was this good at kissing.)"
    scene ep5_391_a3 with dissolve
    wendy "*Smiles* Hehe... I can't hold it anymore."
    wendy "Let's do it."
    mc "Are you sure about that? [elaine] might hear us."
    wendy "*Giggles* Don't worry! I will be quiet."
    mc "Oh...."
    wendy "*Smiles* Let me take this dress off..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_391_a4 with dissolve
    wendy "D-Don't stare at me like that..."
    mc "Sorry...."
    wendy "*Giggles* Just kidding! It's not like I can blame you for that."
    wendy "Alright, let me take off your pants, too..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_391_a5 with dissolve
    wendy "Wow... It's so big."
    wendy "It's almost 3 times bigger than that asshole."
    wendy "Now I know why [elaine] seemed to be so interested in you."
    mc "................."
    wendy "Can I taste it?"
    mc "...Sure."
    wendy "*Giggles* Lovely..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_391_a6 with dissolve
    show ch2ep1_wendy_bj1 with dissolve
    window hide
    wendy "*Sucks* Mmmm... It's really big..."
    wendy "*Sucks* Mmmm... But, it tastes so good..."
    $ renpy.pause()
    menu:
        "Next":
            mc "Can you do it faster?"
            wendy "*Sucks* Mmmm... Yeah, sure."
    scene ep5_391_a7 with dissolve
    hide ch2ep1_wendy_bj1
    show ch2ep1_wendy_bj2 with dissolve
    window hide
    wendy "*Sucks* Mmmmmm..... Like this?"
    mc "...Yeah."
    $ renpy.pause()
    menu:
        "Next":
            wendy "*Sucks* Mmmm... Do you want me suck it a little bit faster?"
            mc "Yes, please."
            wendy "*Sucks* Mmmm... As you wish then!"
    scene ep5_391_a8 with dissolve
    hide ch2ep1_wendy_bj2
    show ch2ep1_wendy_bj3 with dissolve
    window hide
    wendy "*Sucks* Mmmmm....."
    mc "...That's right. Keep sucking it like that."
    $ renpy.pause()
    menu:
        "Next":
            scene black with dissolve
            $ renpy.pause()
            scene ep5_391_a5 with dissolve
            hide ch2ep1_wendy_bj3
            wendy "Okay... I think it's ready now."
            wendy "Can you lie down, please? I want to ride it..."
            mc "...Okay. Wait a sec."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_391_a9 with dissolve
    wendy "Alright... I'm going to put it in now..."
    scene ep5_391_a10 with dissolve
    wendy "U-Ugh...! I-It's so big...!"
    mc "Are you okay..?"
    wendy "Y-Yeah... Don't worry about me."
    wendy "I-I'm going to start moving now..."
    scene black with dissolve
    scene ep5_391_a11 with dissolve
    show ch2ep1_wendy_cow1 with dissolve
    window hide
    wendy "*Softly breathes* Mmmmm....."
    wendy "*Softly breathes* Ahhh.... [mc]...."
    $ renpy.pause()
    menu:
        "Next":
            wendy "*Softly breathes* Mmmm... Okay, I've gotten used to it now..."
            wendy "*Softly breathes* I'm going to move faster..."
    scene ep5_391_a12 with dissolve
    hide ch2ep1_wendy_cow1
    show ch2ep1_wendy_cow2 with dissolve
    window hide
    wendy "*Softly breathes* Mmmmmm.....!"
    wendy "*Softly breathes* Ahhh... Yes! This feels so good...!"
    mc "Shhh..."
    wendy "*Softly breathes* S-Sorry..."
    menu:
        "Next":
            mc "...Can you do it a little bit faster?"
            wendy "*Softly breathes* Mmmm... Yeah, sure...!"
    scene ep5_391_a13 with dissolve
    hide ch2ep1_wendy_cow2
    show ch2ep1_wendy_cow3 with dissolve
    window hide
    wendy "*Heavily breathes* Mmmmmmm....!"
    wendy "*Heavily breathes* Y-Your cock! It keeps touching my womb..."
    wendy "*Heavily breathes* Mmmmm... I thought I would be able to do it quietly, b-but your cock is driving me crazy...!"
    menu:
        "Next":
            scene black with dissolve
            hide ch2ep1_wendy_cow3
            $ renpy.pause()
            scene ep5_391_a14 with dissolve
            mc "Let's change position, [wendy]."
            wendy "*Softly breathes* Hm...? How do you want to do it?"
            mc "Can you lie down on your right side?"
            wendy "Okay, I'll try that..."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_391_a15 with dissolve
    wendy "...Like this?"
    mc "Yes, that's right."
    mc "I'll be the one doing it now...."
    wendy "*Giggles* Whatever you want!"
    scene ep5_391_a16 with dissolve
    wendy "Ahhh..!!"
    mc "Shhh...."
    wendy "I'm sorry, but it's not my fault, though..."
    wendy "I wasn't ready for it. You should've warned me before putting it in..."
    mc "Yeah, you're right. My bad."
    wendy "*Giggles* Yeah, you should know that."
    mc "I'm going to start moving now..."
    wendy "Yes, please..."
    scene black with dissolve
    scene ep5_391_a17 with dissolve
    show ch2ep1_wendy_side1 with dissolve
    window hide
    wendy "*Softly breathes* Ahhhh....."
    wendy "*Softly breathes* Mmmm... I've never done this position before, but I like it. It feels so good..."
    $ renpy.pause()
    menu:
        "Next":
            mc "Can I move a bit faster?"
            wendy "*Softly breathes* Mmmm... Yeah, go ahead...!"
    scene ep5_391_a18 with dissolve
    hide ch2ep1_wendy_side1
    show ch2ep1_wendy_side2 with dissolve
    window hide
    wendy "*Softly breathes* Mmmmm... Ahhh... [mc]...."
    mc "...Hm?"
    wendy "*Softly breathes* Mmmm... Why...are you so good at this...?"
    mc "I don't know."
    menu:
        "Next":
            mc "I'm almost there."
            wendy "*Softly breathes* Ahhh... Me, too..!"
    scene ep5_391_a19 with dissolve
    hide ch2ep1_wendy_side2
    show ch2ep1_wendy_side3 with dissolve
    window hide
    wendy "*Heavily breathes* A-Ahhh...! Y-Yes, that's spot..!"
    mc "Keep your voice down..."
    wendy "*Heavily breathes* Mmmm... I don't care anymore!"
    wendy "*Heavily breathes* Ahhh... Don't stop! Keep fucking me like that...!"
    menu:
        "Blowjob":
            hide ch2ep1_wendy_side3
            jump ch2ep1wendybj1
        "Cowgirl":
            hide ch2ep1_wendy_side3
            jump ch2ep1wendycow1
        "Slowest":
            hide ch2ep1_wendy_side3
            jump ch2ep1wendyside1
        "Slower":
            hide ch2ep1_wendy_side3
            jump ch2ep1wendyside2
        "Cum":
            jump ch2ep1wendysidecum
label ch2ep1wendybj1:
    scene ep5_391_a6 with dissolve
    show ch2ep1_wendy_bj1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch2ep1_wendy_bj1
            jump ch2ep1wendycow1
        "Side":
            hide ch2ep1_wendy_bj1
            jump ch2ep1wendyside1
        "Faster":
            hide ch2ep1_wendy_bj1
            jump ch2ep1wendybj2
        "Fastest":
            hide ch2ep1_wendy_bj1
            jump ch2ep1wendybj3
label ch2ep1wendybj2:
    scene ep5_391_a7 with dissolve
    show ch2ep1_wendy_bj2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch2ep1_wendy_bj2
            jump ch2ep1wendycow1
        "Side":
            hide ch2ep1_wendy_bj2
            jump ch2ep1wendyside1
        "Slower":
            hide ch2ep1_wendy_bj2
            jump ch2ep1wendybj1
        "Faster":
            hide ch2ep1_wendy_bj2
            jump ch2ep1wendybj3
label ch2ep1wendybj3:
    scene ep5_391_a8 with dissolve
    show ch2ep1_wendy_bj3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Cowgirl":
            hide ch2ep1_wendy_bj3
            jump ch2ep1wendycow1
        "Side":
            hide ch2ep1_wendy_bj3
            jump ch2ep1wendyside1
        "Slowest":
            hide ch2ep1_wendy_bj3
            jump ch2ep1wendybj1
        "Slower":
            hide ch2ep1_wendy_bj3
            jump ch2ep1wendybj2
label ch2ep1wendycow1:
    scene ep5_391_a11 with dissolve
    show ch2ep1_wendy_cow1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch2ep1_wendy_cow1
            jump ch2ep1wendybj1
        "Side":
            hide ch2ep1_wendy_cow1
            jump ch2ep1wendyside1
        "Faster":
            hide ch2ep1_wendy_cow1
            jump ch2ep1wendycow2
        "Fastest":
            hide ch2ep1_wendy_cow1
            jump ch2ep1wendycow3
label ch2ep1wendycow2:
    scene ep5_391_a12 with dissolve
    show ch2ep1_wendy_cow2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch2ep1_wendy_cow2
            jump ch2ep1wendybj1
        "Side":
            hide ch2ep1_wendy_cow2
            jump ch2ep1wendyside1
        "Slower":
            hide ch2ep1_wendy_cow2
            jump ch2ep1wendycow1
        "Faster":
            hide ch2ep1_wendy_cow2
            jump ch2ep1wendycow3
label ch2ep1wendycow3:
    scene ep5_391_a13 with dissolve
    show ch2ep1_wendy_cow3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch2ep1_wendy_cow3
            jump ch2ep1wendybj1
        "Side":
            hide ch2ep1_wendy_cow3
            jump ch2ep1wendyside1
        "Slowest":
            hide ch2ep1_wendy_cow3
            jump ch2ep1wendycow1
        "Slower":
            hide ch2ep1_wendy_cow3
            jump ch2ep1wendycow2
label ch2ep1wendyside1:
    scene ep5_391_a17 with dissolve
    show ch2ep1_wendy_side1 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch2ep1_wendy_side1
            jump ch2ep1wendybj1
        "Cowgirl":
            hide ch2ep1_wendy_side1
            jump ch2ep1wendycow1
        "Faster":
            hide ch2ep1_wendy_side1
            jump ch2ep1wendyside2
        "Fastest":
            hide ch2ep1_wendy_side1
            jump ch2ep1wendyside3
label ch2ep1wendyside2:
    scene ep5_391_a18 with dissolve
    show ch2ep1_wendy_side2 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch2ep1_wendy_side2
            jump ch2ep1wendybj1
        "Cowgirl":
            hide ch2ep1_wendy_side2
            jump ch2ep1wendycow1
        "Slower":
            hide ch2ep1_wendy_side2
            jump ch2ep1wendyside1
        "Faster":
            hide ch2ep1_wendy_side2
            jump ch2ep1wendyside3
label ch2ep1wendyside3:
    scene ep5_391_a19 with dissolve
    show ch2ep1_wendy_side3 with dissolve
    window hide
    $ renpy.pause()
    menu:
        "Blowjob":
            hide ch2ep1_wendy_side3
            jump ch2ep1wendybj1
        "Cowgirl":
            hide ch2ep1_wendy_side3
            jump ch2ep1wendycow1
        "Slowest":
            hide ch2ep1_wendy_side3
            jump ch2ep1wendyside1
        "Slower":
            hide ch2ep1_wendy_side3
            jump ch2ep1wendyside2
        "Cum":
            jump ch2ep1wendysidecum
label ch2ep1wendysidecum:
    wendy "*Heavily breathes* Mmmmm... I-I can't hold it anymore!"
    wendy "*Heavily breathes* Mmmmm... A-Are you about to cum, [mc]?!"
    mc "....Yeah. Where do you want me to cum?"
    wendy "*Heavily breathes* Mmmm... A-Anywhere you want! You can cum inside me. It's my safe day today!"
    menu:
        "Cum inside":
            scene black with dissolve
            hide ch2ep1_wendy_side3
            $ renpy.pause()
            scene ep5_391_a19_in1 with vpunch
            mc "I'm cumming!!"
            wendy "A-Ahhhh~~!!"
            wendy "*Pants*...That was...the best sex...I've ever...had..."
            mc "I'm going to pull it out now..."
            wendy "*Pants*...O-Okay..."
            scene ep5_391_a19_in2 with dissolve
            wendy "*Pants*....You...came quite a lot. I...can feel it inside my stomach..."
            mc "*Softly breathes*.....Yeah..."
            wendy "*Pants*....I can't...stand up now. Can...I...rest for a sec?"
            mc "*Softly breathes*...Yeah, sure."
        "Cum in her mouth":
            mc "Get up. I want to cum inside your mouth."
            wendy "*Heavily breathes* O-Okay...!"
            scene black with dissolve
            hide ch2ep1_wendy_side3
            $ renpy.pause()
            scene ep5_391_a19_out1 with vpunch
            mc "I'm cumming!!"
            wendy "Mmmmmm~!!!!"
            wendy "*Sucks* Mmmmm....."
            scene black with dissolve
            scene ep5_391_a19_out2 with dissolve
            wendy "*Pants*...That was...the best sex...I've ever...had..."
            wendy "*Licks*...Your cum...also tastes so good..."
            wendy "*Pants*...Let's take...a rest for a bit...before dressing up, okay?"
            mc "*Softly breathes*...Yeah, sure."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_391_a20 with dissolve
    wendy "Okay... I'm dressed now."
    wendy "Wait here for a sec, [mc]. I'm going to tell [elaine]."
    mc "Okay, sure."
    scene ep5_391_a21 with dissolve
    elaine "Are you done, guys?"
    wendy "[elaine]!!??"
    elaine "Hm? What's wrong, [wendy]?"
    elaine "Why are you so shocked to see me?"
    wendy "N-Nothing! O-Oh! You changed your outfit already?"
    elaine "Yeah, I wanted to feel more comfortable, so..."
    wendy "Okay then, let me change mine, too. After that, we'll take [mc] back home together."
    elaine "Sure. Take your time."
    $ renpy.end_replay()
    $ ch2ep1sexwithwendy = 1
    $ wendy_ch2_ep1 += 4
    $ wendy_relationship += 4
    jump ch2ep1end
label ch2ep1end:
    stop music fadeout 3.0
    scene black with dissolve
    $ renpy.pause()
    scene ep5_392 with fade
    u "Alright, I'm back home."
    u "It's already very late at night."
    u "Let's go take a shower. Then, to bed...."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_393 with fade
    maya "Alright, it's time to go take a shower, my dear."
    skylar "Oh, you already took yours, mom?"
    maya "Yeah, I did."
    skylar "Okay then..."
    scene ep5_394 with dissolve
    maya "Oh! By the way, I got some warm milk for you."
    maya "It's on the table in the kitchen. Don't forget to drink it before going to bed."
    skylar "Thank you, mom. I love you."
    maya "I love you, too."
    skylar "Don't stay up too late. You should get to bed soon, too."
    maya "Sure. I'll just sit here for a bit. Then, I'll go to bed soon."
    skylar "Alright then, goodnight, mom."
    maya "Goodnight, my dear."
    scene black with dissolve
    $ renpy.pause()
    scene ep5_395 with dissolve
    maya "(*Sighs* It's been a very long day. I'm so tired...)"
    maya "(To think about [rowan], it's been so long since he came to me the first time.)"
    maya "(To be honest I didn't really expect that the project, which sounded very far from reality back then, would really happen.)"
    maya "(I only helped him because he seemed very determined despite struggling.)"
    maya "(I know the feeling of struggling really well, so I decided to help him.)"
    maya "(By the way, the stars are so beautiful today...)"
    maya "(..................)"
    maya "(I wonder if {b}he{/b} is also watching these beautiful stars somewhere...)"
    scene ep5_396 with dissolve
    s "*Ringtone sounds*..................."
    maya "(...Hm? It's very late at night now. Who's calling me at this time?)"
    maya "(Oh... It's secretary [angela], and it's a FaceTime call.)"
    maya "(It must be something very important.)"
    scene ep5_397 with dissolve
    maya "Yes, [angela]?"
    angela "President. I'm sorry for calling you so late at night like this."
    maya "It's alright. I'm still awake."
    maya "There must be something really important. Otherwise, I know you wouldn't have called me now."
    angela "Yes, you're right. I've got very, very good news for you."
    maya "Hm...? What is it?"
    angela "I've found him, president."
    scene ep5_398 with dissolve
    maya "W-What did you just say?!"
    scene black with dissolve
    $ renpy.pause()
    hide screen smartphone
    $ rin_ch2_ep1 = 5
    $ episode = 5
    call screen ending
label ep5_entrance_pic:
    if _in_replay:
        scene ep5_entrancepic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep5_entrance
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep5entrance_pic = True
    $ ep5hiddenimages_count += 1
    jump ch2ep1_freeroam
label ep5_livingroom_pic:
    if _in_replay:
        scene ep5_livingroompic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep5_livingroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep5livingroom_pic = True
    $ ep5hiddenimages_count += 1
    jump ch2ep1_freeroam
label ep5_kitchen_pic:
    if _in_replay:
        scene ep5_kitchenpic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep5_kitchen
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep5kitchen_pic = True
    $ ep5hiddenimages_count += 1
    jump ch2ep1_freeroam
label ep5_pool_pic:
    if _in_replay:
        scene ep5_poolpic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep5_pool
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep5pool_pic = True
    $ ep5hiddenimages_count += 1
    jump ch2ep1_freeroam
label ep5_balcony_pic:
    if _in_replay:
        scene ep5_balconypic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene ep5_balcony
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ ep5balcony_pic = True
    $ ep5hiddenimages_count += 1
    jump ch2ep1_freeroam
