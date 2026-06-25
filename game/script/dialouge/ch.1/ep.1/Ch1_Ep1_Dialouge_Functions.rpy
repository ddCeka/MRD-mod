define modDoAllEp1_001 = False

label Intro:
    scene Disclaimer with dissolve
    $ renpy.pause(5,hard=True)
    scene black with dissolve
    $ renpy.pause(2,hard=True)
    scene Ch1 with dissolve
    $ renpy.pause(3,hard=True)
    scene ep1 with dissolve
    $ renpy.pause(3, hard=True)
    scene black with fade
    $ renpy.pause(2,hard=True)
    u "{b}T{/b}here is a quote, which I'm sure everyone must have heard it at least once in your life."
    u "{b}T{/b}he quote says that..."
    u "{b}Y{/b}ou've only got one life to live, so you better live it right."
    u "{b}T{/b}o talk about a good life,"
    u "{b}W{/b}e all have our own definition of it."
    u "{b}S{/b}ome people seek for wealth, because they think they could live happily if they had a lot of money."
    u "{b}S{/b}ome wish to be healthy. They believe there is nothing better than having a good health."
    u "{b}F{/b}reedom is also the thing that many people want to have too."
    u "{b}A{/b}side from that, there are also many things that people want to, have to accomplish the definition of their good life."
    u "{b}T{/b}hings such as love, friends, happiness, and many more."
    u "{b}H{/b}owever..."
    u "{b}I{/b}'ve never ever thought about all those things, even for once..."
    scene Intro1 with dissolve
    u "Hi, my name is..."
    u "Default is Isac, but you can change it if you want."
    $ mc_name = renpy.input("What's your name?", length=10)
    $ mc_name = mc_name.strip()
    if mc_name == "":
        $ mc_name = "Ceka"
    $ persistent.mc_name = mc_name
    call mod_set_vars
    play music "sfx/Moving In.mp3" fadein 3.0
    $ bgm = "Bensound - Clear Day"
    u "My name is [mc]. I'm 22 a year old guy who just graduated from a university."
    u "After graduation, there are two different choices that people usually choose."
    u "First, take a rest to heal yourself from stress and fatigue."
    u "People who take the first choice are people who want to have fun in life while they still can."
    u "They may spend their free time at home, or travel around the world for one or two years."
    u "Then, come back and apply for a job after having enough fun."
    u "Second, don't waste any of your time, and apply for a job right after graduation."
    u "People who choose this choice are people who want to become successful as fast as they can."
    u "So, instead of enjoy having fun in life when they are still young. They choose to start working right away."
    u "It's because they believe that they could have more fun later after becoming successful at work, or having a secure job."
    u "I think they're right because once you have a lot of money, you can do or buy almost anything you want."
    u "Personally, I'm also in the second group. I applied for a job right after graduation."
    u "Fortunately, they accepted my application, and tomorrow will be the first day of my working life."
    u "And since the company is located in a different city, so I have to find a new place to live in."
    u "Fortunately, I found one and I really like it, because it's not too far from the company."
    u "So, two days ago, I signed a lease agreement, and moved my personal belongings there."
    u "The contract starts today, so right now I'm leaving my current apartment,"
    u "where I've been staying since the first year at university."
    u "Well. After all I've said,..."
    u "I just want to make it clear that I didn't apply for a job because I wanted to either become successful, or earn a lot of money."
    u "I'm not like the others. I have no desire, no dream, and no ambitions."
    u "No, I said it wrong..."
    u "Actually, I do have a desire, but it is so simple that whoever knows about it will surely end up laughing at me."
    u "Well, my desire is..."
    u "..."
    alice "Hi, [mc]!"
    scene Intro2 with fade
    mc "Hm?... [alice]?"
    alice "Yeah, it's me!"
    u "This girl right in front of me, is [alice]."
    u "We've known each other for four years, because we live in the same apartment."
    u "Or to be specific, she lives next door to me. So, we happened to see each other so many times."
    scene Intro3 with dissolve
    u "Not only living in the same accommodation, we also studied in the same university as well."
    u "However, we didn't study in the same field."
    u "She studied in faculty of arts, majoring in music while I was majoring in games development."
    u "However, we still met each other a lot at the university even though our faculty buildings were on the opposite side of the campus."
    u "What a weird coincidence..."
    scene Intro4 with dissolve
    u "I said it's a weird coincidence, because I was sure that the possibility of us seeing each other at the university was very low."
    u "It couldn't even be higher than ten percent."
    u "And I've never ever been to places around her faculty building, either."
    u "So, there was no better explanation than that she's been following me around."
    u "However, since she didn't do anything bad to me, I didn't tell her to stop."
    u "Of course I knew the reason why she's been doing that. I'm not an idiot after all."
    u "Even though she's never said it, I know that she likes me."
    u "However, I don't know why she likes me though."
    u "And of course, I've never asked her either."
    u "But that doesn't matter. I'm not interested in love anyway."
    alice "[mc]!"
    scene Intro5 with fade
    mc "Hm? What?"
    alice "What's wrong? I called you so many times, but you just looked at me, and didn't answer."
    mc "Nothing. What did you want to say again?"
    alice "Oh. I took Kitty for a walk, and just came back to see if you were here."
    alice "Where are you going so early in the morning like this?"
    scene Intro6 with dissolve
    mc "I'm going to my new house."
    alice "New house? What are you talking about?"
    mc "I just got a job in a different city, so I have to move there."
    scene Intro7 with dissolve
    alice "What!? Are you for real?"
    mc "Yes, I am."
    alice "But!... What about your personal belongings? I don't see any of them."
    mc "I already brought them there two days ago."
    alice "...Friday...I went back to my hometown and just came back here yesterday night..."
    alice "...That's why I didn't know about it..."
    alice "But, why have you never told me about it though?"
    mc "Hm? Why should I?"
    alice "Yeah... You're right. Why should you?..."
    alice "You're always like this. There is nothing I can do now..."
    alice "*Sigh*... Are you in a hurry? Do you still have time left?"
    mc "Why?"
    alice "Since you're here this early, I assume that you haven't eaten anything yet, right?"
    alice "Then, let's go and find something to eat together!"
    alice "At least I can spend a little more time with you before you go..."
    menu:
        "Okay [alice1]":
            jump Beforeleaving
        "I'm not hungry yet":
            $ EatwithAlice = False
            scene Intro7_Reject1 with dissolve
            mc "I don't want to eat now. I'm not hungry yet."
            alice "... How about drinks? Do you want to have some?"
            mc "No, I'm not thirsty, either."
            alice "...Really?"
            alice "So, you are just going to leave like this?"
            mc "Yes, why?"
            alice "...Nothing."
            alice "*Sigh*... You're always putting up this wall so you don't have to talk with people or be with anyone."
            alice "Even though I understand that, and I'm the one trying to get close to you, it still..."
            scene Intro7_Reject2 with dissolve
            kitty "Meow!"
            alice "Aye!"
            alice "[kitty]! Where are you going!?"
            kitty "Meow!"
            scene Intro7_Reject3 with dissolve
            alice "Hey! Come back!"
            kitty "Meow!"
            u "..."
            u "Well, looks like I can leave now..."
            u "There are things waiting for me to arrange at the new place."
            u "So, I want to get there as fast as I can."
            u "Let's leave then..."
            scene Intro8 with dissolve
            u "To be honest I prefer living alone, but the other places nearby the company were already full."
            u "So I had no choice, but to live in a shared house."
            u "I heard that there are other people living in the house as well."
            u "I wonder if they wake up now. I hope they don't."
            u "I don't want to be the center of attention."
            u "I want to move in quietly so that nobody notices me."
            jump Movein
label Beforeleaving:
    mc "You're right. I haven't eaten anything yet. So, I'm a little bit hungry."
    alice "Then, what do you say?"
    mc "Okay, let's go."
    scene Intro7_Accept1 with dissolve
    alice "Really? You're not kidding me, right?"
    mc "What would be the point of me doing that?"
    alice "Then, wait a sec! Let me take Kitty back to my room first."
    mc "Okay."
    alice "Kitty, say goodbye to him!"
    kitty "Meow!..."
    mc "......"
    scene black with dissolve
    s "*A few minutes later*..."
    scene Intro7_Accept2 with fade
    alice "Sorry to keep you waiting. I'm back!"
    mc "Don't be. It's only been five minutes."
    alice "Hehe... Let's go!"
    scene Intro7_Accept3 with dissolve
    alice "Have you decided where we are going to eat?"
    mc "No. I think I will just walk in the first restaurant we see."
    alice "Well... Since we're heading this way, I know some good places."
    mc "Carry on."
    alice "If we keep going forward, the first restaurant we'd see will be on the right side."
    alice "It's called 'Sunrise Cafe & Restaurant'."
    alice "I think it's really a good place to chill in the morning."
    alice "They have many seats on the street outside the restaurant for customers to enjoy the wind and the sunshine."
    alice "It sounds good, right?"
    mc "Okay. Then, we'll eat there."
    alice "Hm? Don't you want to hear about the other restaurants?"
    mc "That'd be unnecessary. I'll pick the ones you just mentioned anyway."
    mc "It's the closest restaurant from here, so you won't have to walk a long way back to the apartment."
    alice "Okay. As you say."
    scene Intro7_Accept4 with dissolve
    alice "To be honest you made me a little bit angry."
    mc "Did I?"
    alice "Yes, you did!"
    alice "How could you leave without telling me anything!"
    mc "I didn't see any reason to tell you."
    mc "It wouldn't change the fact that I'm leaving anyway."
    alice "I know it wouldn't, but there were so many reasons why you should have told me!"
    alice "For example, I could have helped you finding a good place, or helped you move your personal belongings!"
    mc "But I could do it on my own. So, why did I have to bother you?"
    alice "*Sigh*... Whatever..."
    scene Intro7_Accept5 with dissolve
    alice "At least give me your new house's address."
    mc "Why?"
    alice "So that I will be able to visit you in the future."
    scene Intro7_Accept6 with dissolve
    mc "But I don't see any reason for you to do that."
    alice "Come on! Are you really going to say goodbye forever?"
    alice "I'm not going to let you do that."
    alice "If it was like we've just met, then it would be alright for us to not see each other ever again."
    alice "But it actually isn't like that! I've known you for four years!"
    mc "*Sigh*... Fine. I'll give you my new address."
    alice "Hehe..."
    alice "By the way, I guess you applied for a game developer position, right?"
    menu:
        "How did you know that?":
            mc "How did you know that?"
        "Yes":
            mc "Yes, you're right."
    scene Intro7_Accept5 with dissolve
    alice "Hehe... No wonder I've known you for a long time."
    alice "Well... let's see your new address."
    scene Intro7_Accept7 with dissolve
    alice "What? You're moving to New Town?"
    alice "That's pretty far from here..."
    alice "It will not be easy for me to visit you."
    mc "Then, you shouldn't visit me."
    scene Intro7_Accept8 with dissolve
    alice "What? How could you just say that easily?"
    mc "Instead of wasting your time visiting me..."
    mc "Why don't you spend it on following your dream?"
    mc "I heard you wanted to be a composer, didn't you?"
    alice "Hm? You knew that? How? Who told you that?"
    mc "..."
    menu:
        "Why so surprised?":
            mc "Isn't it normal for a music major student? Why so surprised?"
            alice "No, it isn't. There are also many jobs aside from a composer."
            mc "Well, I actually heard that from you..."
        "You":
            mc "Have you already forgot?"
            alice "Forgot what?"
            mc "You told me by yourself..."
    alice "What? Really?"
    alice "But when did I tell you? I can't remember."
    mc "..."
    mc "Let's finish the food. We only have an hour before the train departs."
    scene Intro7_Accept8_5 with dissolve
    alice "What? You should've have told me earlier!"
    alice "Hurry up! Finish it fast!"
    alice "I don't want you to miss your train!"
    scene black with dissolve
    $ renpy.pause()
    jump A_Good_Bye_Kiss
label A_Good_Bye_Kiss:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        else:
            $ mc_name = persistent.mc_name
    scene Intro7_Accept9 with dissolve
    mc "Hm? Are you not going back to your apartment?"
    mc "Why are you following me?"
    alice "Don't mind me. I just want to go with you to the train station."
    mc "... Whatever. It's your choice."
    scene Intro7_Accept10 with fade
    mc "We finally arrived here."
    alice "... I always thought the train station was quite far from the restaurant."
    alice "How did a ten-minute walk pass so quickly..."
    alice "...{size=-10}To be honest I don't want you to leave.{/size}"
    mc "Hm? What did you say?"
    scene Intro7_Accept11 with dissolve
    alice "..."
    u "Why is she looking at me like that?"
    scene Intro7_Accept12 with dissolve
    alice "*Kissing*... Mmm..."
    alice "I love you..."
    scene Intro7_Accept13 with dissolve
    alice "Goodbye! Take care of yourself!"
    alice "(Oh my gosh... I can't believe that I just confessed to him and kissed him!...)"
    alice "(Is he going to think that I am a crazy girl?)"
    alice "(Argh!... I shouldn't have done that....)"
    u "....."
    u "Well, it's time to get to the train."
    scene Intro8 with dissolve
    u "To be honest I prefer living alone, but the other places nearby the company were already full."
    u "So I had no choice, but to live in a shared house."
    u "I heard that there are other people living in the house as well."
    u "I wonder if they woke up now. I hope not."
    u "I don't want to be the center of attention."
    u "I want to move in quietly so that nobody notices me."
    $ renpy.end_replay()
    $ alice_ch1_ep1 += 1
    $ alice_relationship = alice_ch1_ep1
    $ EatwithAlice = True
    jump Movein

label Movein:
    scene Movein1 with fade
    rin "*Yawning*... What a lovely morning!"
    scene Movein2 with dissolve
    rin "Hm?"
    scene Movein3 with dissolve
    rin "Wow... To see you waking up so early in the weekend like this is very crazy."
    rin "It must be the apocalypse today then."
    scene Movein4 with dissolve
    zeke "Haha... That's very funny."
    zeke "I woke up because I had to pee, and couldn't sleep again."
    rin "That's it?"
    zeke "Yeah, that's it."
    rin "Well, I thought today was a special day or something."
    zeke "Oh, actually it is."
    rin "Hm?"
    zeke "Did you know that our new housemate is coming today?"
    rin "Really? I never knew that. A man or a woman?"
    scene Movein3 with dissolve
    zeke "I heard it's a man."
    rin "Well, that's good news for you, isn't it?. {w}You are the only man in this house."
    zeke "Yeah, I'm going to be his friend!"
    rin "And when will he arrive?"
    zeke "I don't know. The landlord didn't tell me that."
    rin "I see..."
    rin "By the way, what are you watching?"
    rin "May I join?"
    zeke "Sure!"
    scene Movein5 with dissolve
    rin "What is this movie about?"
    zeke "Actually, it isn't a movie. It's a television series."
    zeke "It's about a high school student who has been bullied after transfering to a new school."
    zeke "Then, he decided to train himself. He wanted to stop the bullies, and have a peaceful life at school."
    rin "That sounds interesting. Is it fun?"
    zeke "It's the first project of a new director, so there are some scenes that don't make sense."
    zeke "But it's not all that bad. You can watch it just to kill time."
    rin "I see..."
    scene Movein6 with fade
    u "What a long trip... I almost went to sleep on the train."
    u "To think that I get to live here from now on, it feels a bit exciting..."
    u "...Only just a bit."
    u "I spent four years living in the city I've just left, and now I'm suddenly here..."
    u "{b}{i}Everyday is a new adventure{/i}{/b}... Someone used to tell me that."
    scene Movein7 with dissolve
    u "Well, let's get inside, and go to my room."
    scene Movein8 with dissolve
    rin "I'm kinda hungry. I will go grab some snacks from the kitchen."
    rin "Do you want anything to eat?"
    zeke "Umm... Let me think..."
    #--------Insert door opening sound here--------#
    s "*Entrance door opening*...."
    scene Movein9 with dissolve
    rin "Hm? Who's that?"
    rin "Has [yui] just come back from being outside?"
    zeke "I don't think it's her. I didn't notice her going outside."
    zeke "Let's go and have a look."
    scene Movein10 with dissolve
    zeke "Wait... I think he's our new housemate!"
    rin "Oh, yeah. I almost forgot we just talked about him."
    rin "Let's give him a warm welcome."
    zeke "Hey, do you need help?"
    u "Hm?..."
    scene Movein11 with dissolve
    zeke "You must be our new housemate, right?"
    zeke "Hi, I'm [zeke]. Nice to meet you."
    u "...Seems like my plan to sneak in quietly has just failed..."
    u "Well..."
    menu:
        "Shake hand [rin1][smec] & [zeke1]":
            scene Movein11_Shake1 with dissolve
            $ Shakehand = True
            $ zeke_ch1_ep1 += 1
            $ rin_ch1_ep1 += 1
            $ zeke_relationship = zeke_ch1_ep1
            $ rin_relationship = rin_ch1_ep1
            mc "My name is [mc]. Nice to meet you."
            zeke "How are you?"
            mc "Good."
            scene Movein11_Shake2 with dissolve
            zeke "I'm good, too!"
            u "I didn't even ask... Why did he tell me that...?"
        "Ignore":
            scene Movein11_NoShake1 with dissolve
            mc "My name is [mc]. Nice to meet you."
            zeke "Er... How are you?"
            mc "Good."
            scene Movein11_NoShake2 with dissolve
            zeke "Oh..."
            zeke "I'm sorry. You don't like to shake hands, do you?"
            zeke "Did I make you uncomfortable?"
            mc "No, you didn't."
    scene Movein12 with dissolve
    zeke "Oh! I almost forget."
    zeke "This is [rin]. She also lives here."
    rin "Hello, nice to meet you!"
    mc "Nice to meet you, too."
    scene Movein13 with dissolve
    zeke "You must be tired moving here."
    zeke "Have you eaten anything yet?"
    zeke "We're about to have breakfast."
    zeke "Do you want to join us?"
    rin "You should come with us, so we can get to know each other better."
    rin "Don't be shy."
    scene Movein14 with dissolve
    u "What's wrong with this guy?..."
    u "Does he always ask too many questions like this?"
    u "Seems like I got an annoying housemate..."
    menu:
        "No, I don't":
            scene Movein16 with dissolve
            mc "No, I don't."
            rin "Oh..."
            mc "There are many things in my room waiting for me to tidy up."
            zeke "...I'm sorry. I forgot that..."
            zeke "By the way, is there anything you want me to help?"
            mc "No, there isn't."
        "I already had it.":
            u "Well, I don't want to cause a problem."
            u "I'll just nicely reject them."
            mc "I already had breakfast."
            mc "And there are many things in my room I need to fix."
            scene Movein15 with dissolve
            zeke "I'm sorry. I completely forgot that."
            zeke "Is there anything you want me to help with?"
            mc "No, there isn't."
    scene Movein17 with dissolve
    zeke "Are you sure that you don't want my help?"
    mc "Yes, I am."
    mc "Aren't you guys going for a breakfast?"
    zeke "Oh... We are."
    mc "Then, see you later."
    scene Movein18 with dissolve
    zeke "I think he doesn't like me..."
    rin "You're overthinking. How can he not like you? You're a good man."
    zeke "But I think I just made him uncomfortable."
    zeke "You saw his expression, and the way he talked, didn't you?"
    zeke "He seemed annoyed."
    rin "You can't judge him yet. Maybe he's just an introverted guy."
    rin "Come on, stop being so sad. Let's go to the kitchen."
    zeke "Okay..."
    scene Movein24 with dissolve
    u "There are a lot of boxes..."
    u "Alright, let's get started."
    scene Movein19 with fade
    rin "Well, I think I've just gotten more hungry."
    rin "Only snacks won't be enough to make me full."
    rin "So, I'm going to cook something to eat."
    rin "Do you want me to cook for you, too?"
    zeke "Yes, please."
    rin "Then, what'd you like to eat?"
    zeke "Can you cook me an omelette rice?"
    rin "Sure."
    zeke "Thanks."
    zeke "I have no idea how I would survive if you weren't living in this house."
    zeke "You're the only one person who can cook."
    scene Movein20 with dissolve
    rin "*Giggles*...Then, you better find yourself a girlfriend who is good at cooking!"
    rin "That woman... How is your relationship with her going?"
    zeke "W-What are you talking about!?"
    zeke "We're just friends!"
    scene Movein19 with dissolve
    rin "Come on. Stop lying already. How long have we known each other?"
    rin "I know you love her."
    zeke "That doesn't matter. She already has a boyfriend..."
    rin "She has a boyfriend. Then what?"
    rin "They are just dating, not married."
    rin "Even though they might become a married couple some day, {w}that doesn't mean they will love each other until the last day of their lives."
    rin "There are a lot of married couples divorcing nowadays."
    rin "You'll never know what could happen in the future. You still have a chance!"
    scene Movein20_1 with dissolve
    zeke "Oops! Hahaha!!"
    rin "Why is it so funny?"
    zeke "*Panting*...I'm sorry. I know that you tried to cheer me up, but..."
    rin "But what?"
    zeke "You said like you are really good at relationships. I almost believed you."
    zeke "But... As I remember... {w}You've never had a boyfriend, haven't you?"
    zeke "You have been single for 24 years..."
    rin "W-What did you want to eat again!?"
    zeke "Hahaha!"
    rin "Stop laughing! Otherwise, there will be no food for you!"
    zeke "Ha.. Oops! Okay... I'm sorry."
    scene black with dissolve
    $ renpy.pause()
    scene Movein21 with dissolve
    rin "Okay, finished. Here is your omelette rice."
    zeke "Thanks a lot."
    scene Movein22 with dissolve
    rin "Speaking of [mc]..."
    rin "Don't you think he is similar to someone we know?"
    zeke "Hm? Who?"
    rin "[yui]."
    zeke "Oh... Yeah! They are so similar!"
    rin "*Giggles*.... Right?"
    zeke "Hey."
    rin "Hm?"
    zeke "Since he has become our new housemate, should we arrange a welcoming party tonight?"
    rin "That's a pretty good idea!"
    rin "I'm sure it's going to help us improve our relationship with him."
    scene Movein23 with dissolve
    rin "But..."
    zeke "But what?"
    rin "Are you sure that he will join us? You know he seems to be introverted."
    zeke "Oh... You're right..."
    zeke "What should we do?..."
    scene Movein25 with fade
    u "*Sigh*... Finally, it's all done..."
    u "What time is it?"
    u "Hm?... Already noon? Did I take that long to fix up my room?"
    u "I didn't notice it because I don't feel hungry at all."
    u "But, I'm a little tried. I think I should take a nap."
    scene Movein26 with dissolve
    u "Last time I came here, I didn't think about it."
    u "But I wonder if there is any good restaurants around here."
    u "I need to find something to eat after waking up..."
    u "...."
    scene Movein27 with dissolve
    u "Zzzz...."
    scene black with dissolve
    #--------Insert door being knocked sound here-------#
    play sound "sfx/Door knocking.mp3"
    play music "sfx/Main_menu.mp3" fadein 4.0
    $ bgm = "Bensound - Creative Minds"
    s "*Knocking*...."
    menu:
        "Wake up":
            scene Firstdinner1 with dissolve
            play sound "sfx/Door knocking.mp3"
            s "*Knocking*....."
            u "Uhm.... What's happening?..."
    scene Firstdinner2 with dissolve
    play sound "sfx/Door knocking.mp3"
    s "*Knocking*....."
    u "Ah... There is someone knocking on my door."
    scene Firstdinner3 with dissolve
    play sound "sfx/Door knocking.mp3"
    s "*Knocking*...."
    zeke "[mc]. Are you in there?"
    mc "Yes, I am."
    zeke "Can you open the door for me? I have something to tell you."
    scene Firstdinner4 with dissolve
    mc "Wait... I'm coming."
    scene Firstdinner5 with dissolve
    zeke "Hi! Did I interrupt you while sleeping?"
    mc "...To be honest you did."
    zeke "Oops! I'm sorry then. I didn't know that."
    scene Firstdinner6 with dissolve
    mc "*Sigh*...Then, what did you want to tell me?"
    zeke "Oh! We're about to have a welcome party for you!"
    zeke "So, I am here to ask you frankly if you want to come down and have a dinner together."
    zeke "(...Actually, I'm going to take you there no matter what.)"
    u "...Well... I'm kinda hungry..."
    menu:
        "Okay":
            mc "Okay."
            scene Firstdinner6_Accept with dissolve
            zeke "Really? Are you really going to join us?"
            mc "Why are you so happy?"
            zeke "I thought you were introverted, so I expected you to reject."
            mc "Introverted? I'm not."
            zeke "Great! Then, let's go down stairs."
        "No, thanks":
            mc "Thanks, but I'm gonna find something to eat by myself."
            scene Firstdinner6_Reject with dissolve
            zeke "Come on, man."
            zeke "I know that you're introverted..."
            mc "Introverted?"
            zeke "But you can't live alone by yourself in this world."
            zeke "Join us, man. You should make some friends!"
            mc "*Sigh*...Fine."
    scene Firstdinner7 with dissolve
    zeke "We didn't know what's your favorite food, so I let [rin] handle it."
    zeke "Is that okay for you?"
    mc "I can eat everything. Don't worry."
    zeke "I'm glad to hear that!"
    mc "Your arm."
    zeke "Hm? Why?"
    mc "Aren't you going to take it off me?"
    zeke "What's the problem? We're already friends!"
    mc "*Sigh*...."
    scene Firstdinner8 with fade
    zeke "There they are!..."
    scene Firstdinner9 with dissolve
    zeke "Girls! Look who I've got..."
    mc "...Hi."
    u "Hm?..."
    scene Firstdinner10 with dissolve
    rin "I'm glad to see you joining us, [mc]."
    rin "What are you guys waiting for? Take a seat!"
    zeke "Sure!"
    scene Firstdinner11 with dissolve
    rin "Oh, you guys haven't met, right?"
    rin "Let me introduce..."
    scene Firstdinner12 with dissolve
    rin "[mc], this is [yui]."
    rin "[yui], this is [mc]."
    mc "...."
    yui "...."
    scene Firstdinner13 with dissolve
    rin "[yui]?"
    rin "Don't be so rude. Say something!"
    yui "*Sigh*...."
    scene Firstdinner14 with dissolve
    yui "Hi."
    yui "I'm [yui], and I don't like you."
    yui "Are you satisfied?"
    mc "...."
    scene Firstdinner15 with dissolve
    rin "Err... She was just kidding!"
    zeke "Yeah! She's always like this!"
    zeke "Do you feel like you're watching a mirror now?"
    mc "...."
    rin "Please, don't mind her."
    mc "I don't..."
    rin "Thanks"
    u "Actually, I don't even care about her..."
    scene Firstdinner16 with dissolve
    rin "By the way, do you mind telling us more about yourself?"
    rin "Like how old are you? where are you from? Why did you move here?"
    rin "We'd like to know you better."
    u "I think I better tell them what they want to know."
    u "So, they won't have to keep asking me, and make me annoyed any longer..."
    scene Firstdinner17 with dissolve
    mc "I'm from East Town."
    rin "East Town? Hm?... You came a long way here."
    mc "Yes."
    rin "How old are you?"
    mc "I'm 22."
    rin "Oh, you're two years younger than us."
    mc "Us?"
    rin "[zeke] and I."
    rin "But [yui] is also 22 like you."
    scene Firstdinner18 with dissolve
    zeke "So, why did you move here?"
    mc "I just got a job in this city."
    zeke "Did you? Congrats!"
    zeke "When will you start working?"
    mc "Tomorrow."
    zeke "That's pretty hasty... You just moved here today."
    rin "Yeah, I think so."
    zeke "What company are you going to work for?"
    mc "Xecon."
    scene Firstdinner19 with dissolve
    rin "Wait... What!?"
    mc "Hm?"
    rin "What a coincidence. We also work for Xecon, too!"
    mc "...Really?"
    scene Firstdinner20 with dissolve
    rin "Yeah, I'm working in the community management team."
    rin "You know... Planning and creating contents."
    rin "Then, post them on social medias to inform our customers, and many more."
    scene Firstdinner21 with dissolve
    rin "[zeke] is a graphic designer."
    rin "Although he looks like this, he is actually one of the best."
    zeke "Hey! What did you mean by 'Although he looks like this'?"
    rin "*Giggles*... Nothing. Just kidding."
    scene Firstdinner22 with dissolve
    rin "[yui] is going to start her first day tomorrow, too!"
    rin "She is going to be in the game developer department."
    scene Firstdinner23 with dissolve
    rin "What about you?"
    rin "What position are you going to work?"
    zeke "Let me guess! A graphic designer, right!?"
    mc "....."
    zeke "I knew it! You look like someone who's really good at making pictures, and vid-"
    mc "A game developer."
    scene Firstdinner24 with dissolve
    yui "...What?"
    yui "What did you just say?"
    mc "I'm going to work with you."
    scene Firstdinner25 with dissolve
    yui "That's impossible!"
    yui "I heard that they only accepted one position!"
    mc "Then, I think you heard it wrong."
    yui "But!..."
    scene Firstdinner26 with dissolve
    rin "Calm down. Why are you so mad at him?"
    rin "The executive board must discussed it already before hiring someone."
    zeke "Yeah, this isn't his fault."
    zeke "I think you should actually be happy to work with a friend."
    yui "He isn't my friend!"
    mc "....You aren't mine either..."
    yui "W-what!?"
    scene Firstdinner26_1 with dissolve
    rin "[zeke]! Have you eaten the pizza? How was it?"
    zeke "O-Oh, yeah! It's so delicious!"
    zeke "Come on, guys! Stop talking, and start eating already..."
    yui "Tch!..."
    scene black with dissolve
    s "*Almost an hour later*...."
    scene Firstdinner27 with dissolve
    u "*Sigh*...I'm full."
    u "It's been quite long since I've been here. I need to go to the toilet..."
    scene Firstdinner28 with dissolve
    zeke "Hey, where are you going?"
    mc "....Toilet."
    zeke "Okay then."
    scene Firstdinner29 with dissolve
    u "I was thinking about going to the toilet at the second floor, {w}but there is also the bathroom in the hallway."
    u "Which one should I go?"
    menu:
        "Hallway [krystal1]":
            scene Firstdinner30 with dissolve
            u "I think I'll go to the bathroom in the hallway."
            jump Krystalinbathroom
        "Second floor":
            scene Firstdinner30 with dissolve
            u "I think I'll go to the toilet at the second floor."
            jump Yuiatsecondfloor
label Krystalinbathroom:
    if _in_replay:
        $ _game_menu_screen = "scenegallery"
        if persistent.mc_name == None:
            $ mc_name = "MC"
        elif persistent.krystal_name == None:
            $ krystal_name = "Unknown Girl"
        else:
            $ mc_name = persistent.mc_name
            $ krystal_name = persistent.krystal_name
    scene Firstdinner30_Hall1 with fade
    u "There it is..."
    u "Let's get inside."
    $ renpy.sound.play("sfx/Door opening.mp3")
    s "*Opening the door*...."
    scene Firstdinner30_Hall2 with dissolve
    u "....."
    krystal "(Wait... Wasn't that the sound of someone opening the door?)"
    krystal "(But I remember that I already locked the door...)"
    krystal "(Maybe someone just opened her bedroom's door...)"
    scene Firstdinner30_Hall3 with dissolve
    mc "Er... I'm sorry. I didn't know you were in here."
    krystal "!!!!!"
    krystal "G...G..."
    scene Firstdinner30_Hall4 with dissolve
    mc "Don't scream. I'm closing my eyes. I didn't see anything."
    mc "I'm leaving..."
    krystal "G...G..."
    mc "Don't turn back."
    scene Firstdinner30_Hall5 with dissolve
    krystal "Stop talking, and close the door already!!!"
    mc "Okay."
    $ renpy.sound.play("sfx/Door closing.mp3")
    s "*Closing the door*...."
    scene Firstdinner30_Hall6 with dissolve
    mc "I already closed the door."
    mc "Don't worry. I won't tell anyone about it."
    u "Seems like I have to use the toilet in my bedroom."
    scene Firstdinner30_Hall7 with dissolve
    krystal "Just get lost!!"
    mc "...Sure."
    krystal "(What should I do? Did he see my face?)"
    krystal "(What if he tells everyone?)"
    scene Firstdinner30_Hall8 with dissolve
    krystal "(Argh! Why does the shower in my bedroom have to be broken today!?)"
    krystal "(What am I supposed to do now?)"
    scene Firstdinner30_Own1 with dissolve
    u "Okay, there is nobody using this one..."
    scene Firstdinner30_Own2 with dissolve
    u "...I should've come here in the first place..."
    u "I hope she will forget what just happened."
    u "I don't want to have a problem."
    scene Firstdinner30_Own3 with dissolve
    u "Alright, let's get back to the kitchen."
    scene Firstdinner30_Own4 with dissolve
    mc "...."
    yui "Hm?"
    scene Firstdinner30_Own5 with dissolve
    mc "....."
    yui "If you aren't going to say anything, then get out of my way."
    menu:
        "Toilet?":
            mc "Are you also going to the bathroom?"
            yui "No, I'm going back to my room."
        "Leaving already?":
            mc "Are you leaving already?"
            yui "Yes, I'm already full. There is no reason for me to stay."
    mc "I see."
    yui "Then, can you move aside now?"
    mc "Sure."
    $ renpy.end_replay()
    $ krystal_ch1_ep1 += 1
    $ krystal_relationship = krystal_ch1_ep1
    $ Krystalintoilet = True
    jump A_strange_woman
label Yuiatsecondfloor:
    scene Firstdinner30_Own6 with dissolve
    u "....Hm?"
    scene Firstdinner30_Own7 with dissolve
    u "Who's that?"
    u "Well, I better keep going to the toilet."
    scene Firstdinner30_Own1 with dissolve
    u "Okay, let's go pee..."
    scene Firstdinner30_Own2 with dissolve
    u "I'm not sure what time it is. But, it's getting late."
    u "I think I will stay in the kitchen for a bit more."
    u "Then, I'll go back to my room."
    scene Firstdinner30_Own3 with dissolve
    u "Alright, let's get back to the kitchen."
    scene Firstdinner30_Own4 with dissolve
    mc "...."
    yui "Hm?"
    scene Firstdinner30_Own5 with dissolve
    mc "....."
    yui "If you aren't going to say anything, then get out of my way."
    menu:
        "Toilet?":
            mc "Are you also coming to the toilet?"
            yui "No, I'm going back to my room."
        "Leaving already?":
            mc "Are you leaving already?"
            yui "Yes, I'm already full. There is no reason for me to stay."
    mc "I see."
    yui "Then, can you move aside now?"
    mc "Sure."
    jump A_strange_woman
label A_strange_woman:
    scene Firstdinner31 with fade
    rin "Well, I told you, didn't I?"
    rin "He didn't hate you."
    zeke "Yeah, sometimes he seems annoyed, but I think he is a good person."
    scene Firstdinner32 with dissolve
    rin "Oh, you're back?"
    mc "Yes."
    scene Firstdinner33 with dissolve
    if Krystalintoilet == True:
        zeke "What happened? I think I heard a screaming voice coming from the hallway."
        zeke "Did you fight with [yui]?"
        mc "No, I didn't."
        mc "It's another person. A woman with pink hair."
        scene Firstdinner34 with dissolve
        rin "What? Did you see Ms. Ghost?"
    elif Krystalintoilet == False:
        mc "Is there also another person in this house?"
        zeke "Who?"
        mc "I don't know. A woman with pink hair."
        scene Firstdinner34 with dissolve
        rin "What? Did you see Ms. Ghost?"
    $ krystal_name = "Ms. Ghost"
    $ persistent.krystal_name = krystal_name
    mc "Ms. Ghost? What are you talking about?"
    mc "She died in this house?"
    scene Firstdinner35 with dissolve
    zeke "No, it isn't what you think. She is also our housemate."
    zeke "Actually, she was the first person living in this house."
    mc "Then, why do you guys call her Ms. Ghost?"
    zeke "Because we've been living here for two years, but we've never met her even once!"
    zeke "You know... It's like she exists, but we can't see her."
    mc "Two years living here, yet you've never met her."
    mc "How is that even possible?"
    scene Firstdinner36 with dissolve
    zeke "Oh... Wait!"
    zeke "Actually, I think I've met her once."
    zeke "Let me review my memory..."
    zeke "Uhm... It happened a half year ago... I guess?"
    scene black with fade
    $ renpy.pause(1,hard=True)
    scene Firstdinner37 with fade
    zeke "While the sun was setting down, I sat on the sofa in the living room to read a book."
    zeke "Then, I heard foot steps passing behind my back."
    zeke "I was so scared because I was sure that I was the only person in the house at that time."
    zeke "I thought it was a ghost, but then I braced myself up, and turned towards the direction of foot steps."
    zeke "Guess what?"
    mc "...."
    scene Firstdinner38 with dissolve
    zeke "I saw a woman wearing a black hoodie!"
    zeke "I didn't see her face because she put the hood on."
    zeke "I think that was Ms. Ghost for sure!"
    scene Firstdinner39 with dissolve
    zeke "Do you know why she have to hide herself all the time?"
    mc "No, I don't."
    zeke "Well, I guess it's because she's very ugly!"
    mc "Ugly?... I don't think so."
    zeke "No, it has to be that reason. Otherwise, why?"
    scene Firstdinner40 with dissolve
    rin "Wait..."
    rin "Why did you think she's not ugly?"
    mc "Like I said before. I just saw her."
    mc "Even though I only saw her from the back, I can tell that she's really a beautiful woman."
    scene Firstdinner41 with dissolve
    rin "Hmmmm?...."
    rin "That was the longest sentence you've ever said since we met. {w}Do you realise that?"
    mc "Was it?"
    rin "I thought you weren't interested in women, but seems like I was wrong."
    rin "*Giggles*.... She must be really beautiful as you said."
    rin "Then, what about me?"
    mc "What about you?"
    rin "Who is more beautiful?"
    zeke "Wait. Are you drunk, [rin]?"
    rin "No, I'm not. Just tipsy."
    rin "Why don't you answer?"
    mc "...."
    rin "Tell me who is more beautiful~?"
    menu:
        "You [rin1]":
            $ Rin_Compliment = True
            $ rin_ch1_ep1 += 1
            $ rin_relationship = rin_ch1_ep1
            mc "...You."
            scene Firstdinner41_Yes with dissolve
            rin "Really? Do you really think I'm more beautiful?"
            mc "Yes, I do."
            rin "*Giggles*...You're so sweet!"
        "Her":
            mc "I don't want to lie. She is more beautiful."
            scene Firstdinner41_No with dissolve
            rin "Oh..."
            rin "I'm such an idiot to ask you that question..."
        "I can't choose [rin1]":
            mc "You're both beautiful. I can't choose."
            $ Rin_Compliment = True
            $ rin_ch1_ep1 += 1
            $ rin_relationship = rin_ch1_ep1
            scene Firstdinner41_Yes with dissolve
            rin "I know that you think she's more beautiful."
            rin "But you just don't want me to feel sad, do you?"
            mc "....."
            rin "*Giggles*... You're so kind..."
    scene black with dissolve
    u "*A fews moment later*...."
    scene Firstdinner42 with dissolve
    mc "I'm leaving now."
    zeke "Oh... Okay!"
    rin "Goodnight~"
    u "She's already drunk..."
    mc "What about the dishes?"
    zeke "Don't worry. We'll wash them."
    mc "If you say so..."
    scene black with dissolve
    $ renpy.pause()
    scene Firstdinner43 with dissolve
    u "I have to wake up early. Let's go to sleep."
    scene Firstdinner44 with dissolve
    u "Just forget about taking a bath. I'm gonna do it tomorrow morning."
    u "Right now, I just want to lie down and fall a sleep..."
    scene black with dissolve
    $ renpy.pause()
    jump Firstdayatoffice
label Firstdayatoffice:
    play music "sfx/Nextday.mp3" fadein 4.0
    $ bgm = "Bensound - Perception"
    scene black with dissolve
    play sound "sfx/Clock alarm.mp3"
    s "*Alarm clock sound*....."
    scene Firsttimeatoffice1 with dissolve
    play sound "sfx/Clock alarm.mp3"
    s "*Alarm clock sound*....."
    mc "U...Ummm...."
    scene Firsttimeatoffice2 with dissolve
    u "What?... It's already morning?"
    u "Well, time passed so fast."
    u "I feel like I just fell a sleep not too long ago."
    scene Firsttimeatoffice3 with dissolve
    u "Alright, stop thinking nonsense."
    u "It's time to wake up and go to work."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Firsttimeatoffice4 with dissolve
    u "Let's take a shower...."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Firsttimeatoffice5 with dissolve
    zeke "*Humming a song*...Mmmmmm...."
    zeke "(Hm?...)"
    scene Firsttimeatoffice6 with dissolve
    zeke "[mc]!"
    mc "...."
    scene Firsttimeatoffice7 with dissolve
    zeke "Wow..."
    zeke "This is the first time I see a male housemate after opening my room's door."
    zeke "To be honest I'm still not getting used to it."
    zeke "Wait... Why are you dressed too formal."
    mc "What's wrong with my outfit?"
    zeke "No, there is nothing wrong with it, but you know... You can actually dress however you want."
    zeke "Our company doesn't mind that. Unless, you're going to work while naked."
    mc "Then, this is the outfit I want to wear."
    zeke "Okay then."
    zeke "By the way, you seem in a hurry. Where are you going?"
    mc "The office."
    zeke "Why are you in such hurry? We still have an hour left."
    zeke "Let's have a breakfast first!"
    zeke "Come on! Follow me."
    mc "....Fine."
    scene Firsttimeatoffice8 with dissolve
    zeke "Heh? You guys are also here?"
    zeke "Morning, everyone!"
    zeke "How are you doing?"
    scene Firsttimeatoffice9 with dissolve
    rin "Lovely. We're having a breakfast."
    rin "You guys want some?"
    zeke "Of course. Have you never heard this?"
    zeke "{b}The army marches on its stomach!{/b}"
    rin "*Giggles*...Take a seat then."
    scene Firsttimeatoffice10 with dissolve
    zeke "[mc], you sit right there, and wait for me."
    zeke "I'll grab you some bread."
    mc "Thank you."
    yui "Wait... Why did you tell him to sit next to me?"
    zeke "Because I want to sit here! Where else do you want him to sit?"
    yui ".....Whatever."
    scene Firsttimeatoffice11 with dissolve
    rin "Did you sleep well, [mc]?"
    rin "I know sometimes people have a problem when sleeping in an unfamiliar place."
    mc "I'm good. Don't worry."
    rin "Great."
    scene Firsttimeatoffice12 with dissolve
    rin "*Giggles*.... To look at you guys again..."
    rin "An office worker couple, huh?"
    yui "W-What!?"
    rin "You guys look like a couple! Your outfits suit each other very well!"
    scene Firsttimeatoffice13 with dissolve
    yui "....."
    mc "What are you looking at?"
    yui "Why don't you go back to your room to change the outfit?"
    mc "Then, why don't you?"
    yui "Y-You!...."
    scene Firsttimeatoffice14 with dissolve
    zeke "Come on guys. You shouldn't pick a fight in a lovely morning like this."
    zeke "Moreover, since you guys are going to work in the same department,"
    zeke "you should get along. Otherwise, how will you work together?"
    yui "Tch!..."
    mc "I get it."
    u "Actually, I'm not the one having a problem..."
    scene Firsttimeatoffice15 with dissolve
    zeke "By the way, how will you guys go to the company?"
    menu:
        "Bus":
            scene Firsttimeatoffice13 with dissolve
            mc "I'm going to take a bus."
            yui "Then, I'm going to take a taxi."
        "Taxi":
            scene Firsttimeatoffice13 with dissolve
            mc "I'm going to take a taxi."
            yui "Then, I'm going to take a bus."
    mc "...."
    scene Firsttimeatoffice15 with dissolve
    zeke "Well, since we have to go to the same place, why don't you guys come with me?"
    zeke "I have a car."
    scene Firsttimeatoffice14 with dissolve
    mc "Are you sure?"
    zeke "Yeah, [rin] is also coming with me, too."
    rin "Yes, just let him drive you guys there. Why bother paying extra money?"
    u "She's right..."
    mc "Okay."
    zeke "Then, let's finish the breakfast."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Firsttimeatoffice16 with dissolve
    zeke "Alright, we have half an hour left."
    zeke "Let's go guys!"
    rin "Sure!"
    scene Firsttimeatoffice17 with dissolve
    zeke "You have never seen my car, right!?"
    zeke "Yeah, I'm sure you haven't!"
    mc "Why are you so excited?"
    zeke "Because you are going to meet my child!"
    scene Firsttimeatoffice18 with dissolve
    yui "Wait... He has a baby?"
    rin "*Giggles*... No, he doesn't."
    yui "Then, why...?"
    rin "It's his car. He takes care of it as if it was his baby."
    yui "... I don't really understand him..."
    rin "*Giggles*... That's the way boys are."
    scene Firsttimeatoffice19 with dissolve
    zeke "Ladies and gentlemen! The time has come!"
    zeke "Let me introduce you!..."
    stop music fadeout 3.0
    scene Firsttimeatoffice20 with dissolve
    play music "sfx/zeke vehicle.mp3" fadein 3.0
    $ bgm = "Teriyaki boyz - Tokyo Drift"
    zeke "Anyone! Anytime! Anywhere!"
    scene Firsttimeatoffice21 with dissolve
    zeke "It corners faster than electricity!"
    zeke "It exists for one reason, and that one reason is only to kill supercars!"
    zeke "You don't have to like it. You just have to stay the hell out of its way."
    scene Firsttimeatoffice22 with dissolve
    zeke "if it would be a person, it would be Adrian Neuwy!"
    scene Firsttimeatoffice24 with dissolve
    zeke "Look at how gorgeous it is!"
    zeke "Welcome to my..."
    scene Firsttimeatoffice23 with dissolve
    stop music fadeout 3.0
    zeke "Nissan GT-R!!!!"
    scene Firsttimeatoffice25 with dissolve
    play music "sfx/Nextday.mp3" fadein 3.0
    $ bgm = "Bensound - Perception"
    zeke "What do you think? Beautiful, isn't it?"
    zeke "Even an angle can't compete with how beautiful it is."
    scene Firsttimeatoffice26 with dissolve
    mc "......."
    u "I usually don't talk much, but he just made me lost of words..."
    yui "......."
    rin "Hahaha... You're always overreacting!"
    rin "I remember the first time you showed it to me!"
    scene Firsttimeatoffice27 with dissolve
    yui "It's just a car, isn't it?"
    yui "I don't understand why he is so excited about it."
    rin "Well, it's always been his favorite car since he was in high school."
    rin "He worked so hard to earn money so that he could buy it."
    rin "Please, try to understand him."
    yui "....Okay."
    scene Firsttimeatoffice28 with dissolve
    zeke "Hm? What do you think, [mc]?"
    menu:
        "Compliment [zeke1]":
            $ Car_Compliment = True
            $ zeke_ch1_ep1 += 1
            $ zeke_relationship = zeke_ch1_ep1
            u "Well, I think it's better to say something nice."
            mc "Yeah, it's really beautiful."
            scene Firsttimeatoffice28_1 with dissolve
            zeke "Right!? I knew we would have something in common!"
            mc "..... Do we?"
        "Just a car":
            zeke "Hm? What do you think?"
            mc ".... It's just a car."
            scene Firsttimeatoffice28_2 with dissolve
            zeke "Oh...."
            zeke "I thought we have something in common, but seems like I was wrong."
    scene Firsttimeatoffice28 with dissolve
    zeke "...Alright, we wasted so much more time than we should have."
    yui "Because of whom!?"
    zeke "Hahaha. I'm sorry."
    zeke "Come on, hop in!"
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Firsttimeatoffice29 with dissolve
    mc "We only have twenty minutes left..."
    zeke "Don't worry! I will take you there in time."
    zeke "Mark my word!"
    zeke "Woooh! Let's go boys!"
    scene Firsttimeatoffice30 with dissolve
    rin "Hey! Don't drive too fast!"
    rin "You're going to cause an accident!"
    zeke "Hahaha. You know that I'm not!"
    rin "You!..."
    scene Firsttimeatoffice31 with fade
    zeke "Alright, guys! We've arrived here!"
    zeke "Welcome to Xecon!"
    zeke "See? I told you that I would get you here in time."
    mc "Yes, you did."
    zeke "Okay, let me park my baby first."
    scene Firsttimeatoffice32 with dissolve
    rin "Why is the parking lot so dark today though?..."
    zeke "I don't know. Maybe they just want to save electricity."
    zeke "Alright, let's get inside the building."
    scene Firsttimeatoffice33 with dissolve
    rin "To be honest I wanted to ask you a question since yesterday..."
    mc "...."
    yui "Who are you talking to, [rin]?"
    rin "You and [mc]."
    yui "Oh. What did you want to know?"
    rin "Why did you choose this company?"
    rin "You know... Actually our company was just established two years ago."
    rin "It isn't considered as one of the best companies."
    rin "Why didn't you guys choose a better one?"
    scene Firsttimeatoffice34 with dissolve
    mc "... This company has something I want."
    rin "Hm? What do you want?"
    mc "The thing that you guys have been inventing..."
    zeke "Hm?... How did you know that? It isn't well known yet."
    mc ".... From someone I know."
    mc "I want to be a part of the new future, that's why."
    rin "*Giggles*... I wonder if there is someone who doesn't want to..."
    scene Firsttimeatoffice35 with dissolve
    yui "Is there something on my face?"
    mc "No."
    yui "Then, stop staring at me!"
    mc "Are you not going to give [rin] an answer?"
    yui "Tch! I chose to work here because I followed someone here."
    rin "Hm?.... A man?"
    yui "I'm sorry. Even though I like you, there is no way I'm going to tell that."
    rin "*Giggles... Relax."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Firsttimeatoffice36 with fade
    s "*Walking out of the elevator*...."
    zeke "Finally, we are here!"
    scene Firsttimeatoffice37 with dissolve
    zeke "I'd like to take this chance to give you an official welcome again!"
    zeke "Congratulations! And welcome to Xecon!"
    rin "I wish you guys good luck and hope you are successful in your working life!"
    zeke "If you have any problems and want us to help..."
    zeke "Don't be shy, we're willing to help!"
    scene Firsttimeatoffice39 with dissolve
    mc "Thank you."
    yui "....Understood."
    scene Firsttimeatoffice38 with dissolve
    rin "Alright, seems like we have to say goodbye here."
    rin "I have to go to my department."
    zeke "Me too."
    zeke "Do you still remember the way to get to your department?"
    scene Firsttimeatoffice40 with dissolve
    yui "I don't know about him, but I do."
    mc "....."
    scene Firsttimeatoffice41 with dissolve
    rin "Good to hear that. Then, good luck!"
    zeke "Call us when you get off work. I'll drive you guys back home."
    zeke "See you later!"
    scene Firsttimeatoffice42 with dissolve
    s "*[rin] and [zeke] are walking away*..."
    scene Firsttimeatoffice43 with dissolve
    yui "Hey!"
    mc "What?"
    yui "Let's pretend that we don't know each other."
    mc "....Why?"
    yui "And don't try to talk to me! Do you understand!"
    mc "...."
    scene Firsttimeatoffice44 with dissolve
    u "What's wrong with this girl?"
    u "Well, you didn't even have to tell me that. I also planned to do it myself."
    u "However, I have to follow her first. I also have to meet the department head, too."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Firsttimeatoffice45 with dissolve
    yui "(There he is!)"
    u "...There he is."
    scene Firsttimeatoffice46 with dissolve
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Knocking*...."
    pete "Come in!"
    scene Firsttimeatoffice47 with dissolve
    pete "Oh, there you guys are!"
    pete "Please, come here!"
    scene Firsttimeatoffice48 with dissolve
    pete "How are you? Are you ready to start working?"
    mc "Yes, chief."
    pete "Hahaha.... Chief?"
    pete "Just relax and call me by my name."
    pete "We don't call people by their position in this company."
    pete "But make sure that you show your respect to other people."
    scene Firsttimeatoffice49 with dissolve
    yui "As you wish, [pete]."
    u "Hm?... She is smiling...?"
    u "What's going on? I've never seen her smile..."
    pete "Well, since you guys came here together,"
    pete "I assume that you've already introduced yourself."
    scene Firsttimeatoffice50 with dissolve
    yui "Yes. We live in the same shared house."
    u "Wait. Didn't you just tell me to pretend that we don't know each other..."
    pete "Really? Good for you guys then."
    pete "I hope to see both of you get along and work together."
    yui "I'll make sure of it!"
    u "What a liar... You just told me not to talk to you."
    scene Firsttimeatoffice51 with dissolve
    pete "Alright then. I'll show you guys where to work."
    pete "Follow me."
    mc "Okay."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Firsttimeatoffice52 with dissolve
    pete "We, the game developer department, work in this room."
    pete "We start working at 9 a.m. and get off work at 5 p.m."
    pete "But don't be too worry. The schedule isn't actually strict."
    pete "We want our employees to have fun working here, so you can basically do whatever you want."
    pete "However, you'll need to make sure that it will not affect your work."
    scene Firsttimeatoffice53 with dissolve
    pete "Alright, everyone! Attention, please!"
    scene Firsttimeatoffice54 with dissolve
    pete "As you may have already known it. Our former members resigned."
    pete "After the board meeting, they decided to hire people to fill up the gap."
    pete "So, the company has been recruiting employees for a while."
    scene Firsttimeatoffice55 with dissolve
    pete "Let me introduce you guys two new members to our team."
    leo "(Hm?... A woman?)"
    pete "Here is [mc] and [yui]."
    mc "*Nodding head*...[mc]."
    yui "I'm [yui]. Nice to meet you guys."
    scene Firsttimeatoffice56 with dissolve
    pete "This is [liam]. He is the leader of the team."
    liam "Nice to meet you. I'm [liam]."
    liam "If there is something you don't understand. Feel free to ask."
    scene Firsttimeatoffice57 with dissolve
    pete "The guy sitting over there is [joe].... Wait."
    pete "I told you to cut your hair, didn't I?"
    pete "It looks so untidy!"
    joe "Hahaha. I'm sorry. I was too busy to get it done."
    joe "By the way, nice to meet you guys."
    pete "*Sigh*..."
    scene Firsttimeatoffice58 with dissolve
    pete "And there is our big guy, [david]."
    david "Good morning. Do you want something to drink?"
    pete "Don't be afraid of him just because of his appearance."
    pete "He's really a kind person."
    mc "Got it."
    scene Firsttimeatoffice59 with dissolve
    pete "The last person is [leo]."
    leo "Hi, there."
    pete "He's handsome, right?"
    pete "He's the remarkable man for our department."
    pete "I mean both appearance, and ability."
    scene Firsttimeatoffice60 with dissolve
    pete "You must think that there are so few people, right?"
    pete "But don't worry. We actually have a lot more."
    pete "People working in this room are employees who were considered one of the best!"
    scene Firsttimeatoffice60_1 with dissolve
    mc "Then, why are we here?"
    pete "Maybe the board saw your portfolio, and thought that you guys were good enough, and had potentials."
    pete "After meeting you guys, I think they were right. I can tell if someone has the ability to work."
    yui "I see..."
    scene Firsttimeatoffice60 with dissolve
    pete "Alright, your seats are right there."
    pete "Feel free to have a look."
    mc "Okay."
    scene Firsttimeatoffice61 with dissolve
    pete "Okay guys! There are ten more minutes before the meeting."
    pete "Please, prepare yourself, and be on time."
    pete "I'll be waiting in the meeting room."
    u "Hm? What meeting is he talking about?"
    liam "Understood."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Firsttimeatoffice62 with dissolve
    liam "[mc]. Let's go."
    mc "Do I have to go, too?"
    liam "Of course. You're already a part of the team."
    mc "I get it."
    scene Firsttimeatoffice63 with dissolve
    liam "I know it's your first day here."
    liam "But, don't be too worried."
    liam "You just have to sit there and listen to us talking."
    liam "It's going to help you know what you have to do in the future."
    mc "Okay."
    scene Firsttimeatoffice64 with dissolve
    leo "We should go, too. [yui]."
    yui "....."
    leo "Hm? What's wrong?"
    yui "I don't need you to tell me that. I know what I should do."
    scene Firsttimeatoffice65 with dissolve
    leo "What? Why are you talking to me like that?"
    leo "Have I done something to upset you?"
    yui "You're doing it right know."
    yui "I'm already an adult! Don't tell me what to do or not."
    leo "....Okay. I'm sorry."
    leo "(I didn't expect her personality to be like this...)"
    leo "(But... This isn't that bad. She is kinda cute... Haha...)"
    scene Firsttimeatoffice66 with dissolve
    liam "Are you guys ready?"
    david "Yes."
    liam "[leo], Where is your presentation file?"
    leo "It's with me now."
    liam "Great. Let's go then."
    scene Firsttimeatoffice67 with dissolve
    $ renpy.sound.play("sfx/Door knocking.mp3")
    s "*Knocking*..."
    pete "Come in!"
    scene Firsttimeatoffice68 with dissolve
    leo "(I wanted [yui] to sit right next to me.)"
    leo "(But, why did it turn out to be him....)"
    scene Firsttimeatoffice69 with dissolve
    pete "Alright, shall we start now?"
    liam "Sure."
    scene Firsttimeatoffice70 with dissolve
    pete "It's been more than two years since our president started building this company."
    pete "At first, nobody wanted to invest money in our company because they thought our project was too fancy, and impossible."
    pete "Moreover, the president had just graduated with a phd from the university by that time."
    pete "So, they thought he was too young to establish a company."
    pete "He didn't give up, and managed to overcome all obstacles..."
    pete "After working hard for so long...."
    pete "I'd like to inform you guys that our special project is about to be announced to the public soon!"
    joe "Yes! Finally!"
    pete "I know you guys has been testing {b}it{/b} for two years, so I'd like to show you..."
    scene Firsttimeatoffice71 with dissolve
    pete "The completed version of {b}Xecon Gear!{/b}"
    u "There it is..."
    david "A completed version? Is it for real?"
    pete "Yeah, it's already been tested and confirmed that it does no harm to anyone."
    pete "Thanks to all of you, every single one."
    pete "Without any of you, we wouldn't be able to create this amazing thing."
    scene Firsttimeatoffice72 with dissolve
    liam "Wow... It looks fantastic."
    joe "I couldn't agree more."
    pete "I remembered the day that the japanese light novel came out."
    pete "In that novel, there was the technology that helped people diving into the game as if it was a real world."
    pete "People were so hyped about it, and wanted to make it real."
    scene Firsttimeatoffice73 with dissolve
    pete "Unfortunately, nobody could do it..."
    pete "The best we've got was just the VR headset which it technically didn't bring us into the game world."
    pete "We thought that it would take atleast twenty years to be able to do it."
    pete "However, we won't have to wait that long because there was one person..."
    pete "Yes, it was our president."
    pete "He was so passionate in Virtual MMORPG that he tried to create this technology 24/7 for many years since he was still a university student."
    pete "Finally, here we come..."
    pete "I'm really proud to say that Virtual MMMORPG world is no longer a dream!"
    u "....."
    joe "Wooh!!"
    scene Firsttimeatoffice74 with dissolve
    pete "Alright, let's get back to the reason why we are here now."
    pete "[liam]."
    liam "Got it."
    scene Firsttimeatoffice75 with dissolve
    $ renpy.pause()
    scene Firsttimeatoffice76 with dissolve
    liam "Okay, allow me to start the presentation."
    pete "You may start now."
    liam "Thank you."
    scene Firsttimeatoffice77 with dissolve
    liam "After hearing good news from you. I also have good news for you, too."
    liam "The game is also in the final testing process."
    liam "If everything goes according to the plan, we'd be able to release it in the next three months!"
    pete "I'm glad to hear that."
    scene Firsttimeatoffice78 with dissolve
    liam "Moreover, I discussed with the medical department, and decided that"
    liam "It'd be great if there was a system to check the player's brainwave, and heart rate."
    scene Firsttimeatoffice79 with dissolve
    liam "So, [david] and I added it into the game."
    liam "If the player's brainwave, and heart rate go beyond limits,"
    liam "it'd force him out of the game to prevent any bad circumstances."
    scene Firsttimeatoffice80 with dissolve
    pete "Phenomenal! Well done."
    liam "Thank you."
    pete "But you tested it with the older version of Xecon Gear, right?"
    liam "Yes."
    pete "How long would it take you to test if it works with the completed ones."
    scene Firsttimeatoffice81 with dissolve
    liam "Ummm... I'm not sure."
    liam "I have to check the code of the completed version first."
    liam "Then, compare it with the ones I tested."
    liam "If it's changed a lot, then it'd take at least two weeks to make it work together."
    scene Firsttimeatoffice82 with dissolve
    liam "However, if it's exactly the same, then it wouldn't take so long."
    pete "Got it. Then, report to me again later."
    liam "Understood."
    liam "That's all I wanted to present you today."
    scene Firsttimeatoffice83 with dissolve
    pete "Well done, [liam]."
    pete "No wonder why you're the leader."
    liam "Thanks to everyone. They helped me out a lot."
    scene Firsttimeatoffice84 with dissolve
    pete "Alright, what about you, [leo]?"
    pete "How is everything going?"
    scene Firsttimeatoffice85 with dissolve
    leo "Well, there are only few CGs that have to be done."
    leo "But, don't worry. They will be ready soon."
    pete "Good. Can you show me some?"
    leo "Sure."
    scene Firsttimeatoffice86 with dissolve
    $ renpy.pause()
    scene Firsttimeatoffice87 with dissolve
    leo "As you already knew, {b}Unlimited World Online{/b} or {b}UWO{/b} is going to be the first Virtual MMORPG online game ever."
    leo "According to its name, there are a lot of things going on in the game."
    leo "There are a lot of races that player can choose."
    leo "For example, Demon, God, Angel, Human, or even Robot."
    leo "Of course, a lot of kingdoms, too."
    scene Firsttimeatoffice88 with dissolve
    leo "It may not sound any different from many MMORPG games we've seen nowadays."
    leo "But, the game has its own unique stories, and hidden quests."
    leo "And since the game is going to be an open world game,"
    scene Firsttimeatoffice89 with dissolve
    leo "To see a demon race walking in the City of God, is something that can always happen."
    leo "But I'm not sure if that Demon race player can actually {b}{i}wander{/i}{/b} in the city without having a problem."
    leo "Of course, since it's the first Virtual MMORPG game in the theme of fantasy world,"
    scene Firsttimeatoffice90 with dissolve
    leo "The CGs is going to play a crucial role in getting customers attention."
    leo "We have to make sure that our players will feel like it's actually a real world, not just a game."
    leo "So, I've been going all out to make sure that every single one looks as good as it can."
    scene Firsttimeatoffice91 with dissolve
    leo "Unfortunately, my sidekick was one of the two guys handing in a resignation letter."
    leo "I couldn't do anything, but to see the work speed dropping."
    leo "However, since we've already got new faces here, and if I'm not mistaken..."
    leo "I'm sure that [yui] can help me out a lot."
    leo "So, you don't need to worry. Everything will be ready before the dead line."
    scene Firsttimeatoffice92 with dissolve
    pete "I'm glad to hear that."
    pete "Thanks for your presentation, [leo]."
    leo "Your welcome. It's my duty to do it."
    scene Firsttimeatoffice93 with dissolve
    pete "Alright, before we finish this meeting..."
    pete "Is there anyone who wants to talk?"
    pete "Any ideas on how we should improve our game before it's announced to public."
    scene Firsttimeatoffice94 with dissolve
    joe "I think we should improve on game mechanics."
    pete "I'm listening..."
    joe "In my opinion, what is the most important thing in getting customers attention..."
    joe "isn't graphics, but game mechanics."
    joe "No offense, [leo]. I'm just saying my opinion."
    leo "It's okay. I understand your point of view."
    pete "Ummm... Yeah, I understand what you're trying to say."
    scene Firsttimeatoffice95 with dissolve
    pete "Then... What about both of you?"
    pete "You guys have not said a single word since you came in here."
    pete "What do you think?"
    scene Firsttimeatoffice96 with dissolve
    yui "I think we should focus more on graphics."
    yui "No matter how good the game mechanics are, the first thing our customers are going to see is the graphics."
    yui "It is going to play a crucial role as [leo] just said."
    yui "And I'm sure I can even make it better."
    yui "You know first impression is very important, right?"
    scene Firsttimeatoffice97 with dissolve
    joe "Alright, let's assume that I agree with you."
    joe "But do you realise that there are many people who chose to stop playing the game because it had nothing good, except the graphics?"
    joe "What are we going to do if that happens?"
    joe "{size=-15}*Sigh*...I don't understand why the board sent a woman to our department...{/size}"
    scene Firsttimeatoffice98 with dissolve
    yui "Wait? What did you just say!?"
    joe "Hm? What did I say?"
    yui "I don't understand why this company lets someone who doesn't even take care of himself work here either!"
    scene Firsttimeatoffice99 with dissolve
    joe "What!?"
    liam "Hey, be careful before you talk..."
    yui "Why don't you tell that to him? Didn't you hear what he said?"
    pete "Okay, guys. That's enough."
    pete "Stop arguing already. We're a team."
    yui "But I was just saying my opinion...."
    scene Firsttimeatoffice100 with dissolve
    pete "Thanks for your opinion, [yui]."
    pete "Now, I'd like to hear [mc]'s opinion."
    scene Firsttimeatoffice101 with dissolve
    mc "Hm? Me?"
    pete "Yes. What do you think?"
    pete "Who do you agree with?"
    u "Well..."
    menu:
        "Agree with [joe]":
            $ Agreewithjoe = True
            scene Firsttimeatoffice101_Disagree1 with dissolve
            mc "I think [joe] was right."
            yui "What!?"
            mc "If I were a player, instead of having very beautiful graphics, but there is nothing to do,"
            mc "I'd want to enjoy the game mechanics and small details."
            yui "But!..."
            scene Firsttimeatoffice101_Disagree2 with dissolve
            pete "[yui]. I told you to stop, didn't I?"
            pete "This is the working place. You have to listen to other people, too."
            pete "The world doesn't revolve around you."
            yui "....I'm sorry."
        "Agree with [yui] [yui1]\n[smbo]":
            $ Agreewithyui = True
            $ yui_ch1_ep1 += 1
            $ yui_relationship = yui_ch1_ep1
            scene Firsttimeatoffice101_Agree1 with dissolve
            mc "I agree with [yui]."
            mc "There are a lot of people nowadays who don't care about game mechanics and small details."
            mc "Moreover, since they are going to dive into the game as if it was a real world,"
            mc "They might just want to travel around the world to admire its beauty than fighting with monsters."
            yui "That's what I was talking about!"
            scene Firsttimeatoffice101_Agree2 with dissolve
            pete "Ummm... You've got a point."
            pete "I might actually be one of those people who just want to travel around the world as well."
            pete "You know... I don't like fighting."
        "Why can't we do both? [yui1]":
            $ Agreewithboth = True
            $ yui_ch1_ep1 += 1
            $ yui_relationship = yui_ch1_ep1
            scene Firsttimeatoffice101_Agree1 with dissolve
            mc "I think both graphics and game mechanics are equally important."
            mc "Why don't we focus on both of them?"
            yui "Well, at least you know what you should say."
            scene Firsttimeatoffice101_Agree2 with dissolve
            mc "There are a lot of people nowadays who don't care about game mechanics and small details."
            mc "Moreover, since they are going to dive in the game as if it was a real world,"
            mc "They might just want to travel around the world to admire its beauty than fighting with monsters."
            mc "And there are also hardcore gamers who enjoy both PvE, and PvP."
            mc "That's when the game mechanics is going to be involved."
            pete "Yeah, you're right."
    scene Firsttimeatoffice102 with dissolve
    pete "Alright, thank you for your opinion."
    pete "Actually, I agree with both."
    pete "Since we are going to revolutionize the gaming industry, let's make this game the best game of a century!"
    scene Firsttimeatoffice103 with dissolve
    pete "Alright, that's all for today."
    pete "You guys may leave, and get back to work now."
    liam "We get it."
    pete "Oh... Wait a sec."
    pete "Since we got new members here today, let's make a welcome party after work!"
    joe "Yes! A party!"
    u "*Sigh*... Again?..."
    scene black with dissolve
    $ renpy.sound.play("sfx/Door opening.mp3")
    s "*Everone left the room*...."
    if yui_relationship == 1:
        scene Firsttimeatoffice104_Agree1 with dissolve
        yui "Well, you're better than I thought."
        scene Firsttimeatoffice104_Agree2 with dissolve
        mc "What?..."
        yui "Nothing."
    elif yui_relationship == 0:
        scene Firsttimeatoffice104_Disagree1 with dissolve
        yui "Why didn't you agree with me!?"
        yui "You're just like him!"
        scene Firsttimeatoffice104_Disagree2 with dissolve
        mc "What's wrong with you? I just told my opinion."
        mc "The world doesn't revolve around you. Don't you remember?"
        yui "Y-You!..."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Firsttimeatoffice105 with dissolve
    u "Alright, it's time to work..."
    liam "[mc]!"
    u "Hm?"
    scene Firsttimeatoffice106 with dissolve
    liam "Come here."
    mc "Okay."
    scene Firsttimeatoffice107 with dissolve
    mc "Is there something you want from me?"
    liam "I heard that coding is your strength, right?"
    scene Firsttimeatoffice108 with dissolve
    mc "Yes. I can write in any languages."
    liam "Fantastic."
    mc "But, I'm not sure about writing codes for the Virtual MMORPG game."
    mc "It's quite new for me. Actually, for the world."
    liam "Don't worry. The code in the headgear plays a crucial role, not the code in the game."
    liam "You will have a chance to play with the headgear in the future, but for now I want you to do something."
    mc "What is it?"
    scene Firsttimeatoffice109 with dissolve
    liam "There are some game mechanics I think should be improved."
    liam "After the meeting, I assume that you already knew that I'm quite busy to do it myself."
    liam "Can you do it?"
    mc "Sure."
    liam "Great. Then, I'll give you a source code file..."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Firsttimeatoffice110 with dissolve
    u "Okay. I've got a file."
    u "Let's do my best..."
    scene black with dissolve
    $ renpy.pause()
    scene Firsttimeatoffice111 with dissolve
    liam "How are you doing?"
    mc "Great. I agree with what you said."
    mc "The amount of damage that the dark wolf could do was a little bit lower than it should be."
    mc "The boss monster of the city in the beginning shouldn't be that weak."
    mc "So, I fixed the numbers a little bit."
    liam "I'm glad to hear that."
    liam "By the way, you should stop working now."
    scene Firsttimeatoffice112 with dissolve
    mc "Why?"
    liam "It's already 5 p.m."
    mc "Oh..."
    liam "Come on. Let's go."
    mc "Hm? Where?"
    liam "The welcoming party. Did you already forget that?"
    mc "....Do I really need to go?"
    liam "Of course you do! You and [yui] are the main attractions today!"
    mc "*Sigh*...Okay."
    scene Firsttimeatoffice113 with fade
    pete "Alright, guys! Let's go!"
    pete "We're going to party all night til the sun comes up!"
    david "Hahaha.... That's not going to happen."
    pete "Hm? Why?"
    leo "Because you're going to get drunk before anyone else!"
    leo "Don't you remember the last time?"
    liam "Hahahaha...."
    scene Firsttimeatoffice114 with dissolve
    mc "What's wrong?"
    mc "Don't you want to go to the party?"
    yui "....."
    scene Firsttimeatoffice115 with dissolve
    yui "You already knew the answer, why are you still asking?"
    mc "......"
    mc "Did you tell [rin] and [zeke]?"
    yui "No, I didn't."
    mc "Then, you should tell them so that they won't have to wait for us."
    scene Firsttimeatoffice116 with dissolve
    yui "Why me?"
    yui "Why don't you call them by yourself?"
    mc "I don't have their numbers."
    yui "Tsk! Stop looking at me like that!"
    scene Firsttimeatoffice117 with dissolve
    mc "Like what?"
    yui "Stop doing that lifeless-looking eyes!"
    mc "Lifeless-looking eyes? Since when did I do that?"
    yui "Your eyes have been looking like that since the first time I saw you!"
    mc "I di-"
    joe "Hey! What are you guys doing?"
    joe "Aren't you coming with us!?"
    scene Firsttimeatoffice118 with dissolve
    mc "Sorry. I'm going."
    yui "....I don't like him."
    u "...I've never seen you like anyone expect [rin]."
    mc "Be careful. He might hear you."
    yui "Who cares?"
    scene Welcomeparty1 with fade
    pete "Alright, just order anything you guys want to eat."
    pete "I'll pay for the food!"
    david "Yes! That's what I've been wanting to hear."
    joe "Hahaha... Be careful not to order too much, bro."
    scene Welcomeparty2 with dissolve
    pete "And of course, since this is the party, alcoholic drinks will be needed."
    pete "[mc] and [yui]."
    yui "Yes?"
    pete "Can you guys drink? A beer would be okay, right?"
    scene Welcomeparty3 with dissolve
    yui "A beer?"
    yui "(No... I can drink everything, but not a beer...)"
    yui "(But I don't want to disappoint him.... What should I do?)"
    mc "I don't-"
    yui "!!!"
    scene Welcomeparty4 with dissolve
    yui "*Whispering*.. Shut your mouth!"
    scene Welcomeparty5 with dissolve
    pete "Hm? What did you say, [mc]?"
    yui "Nothing! A beer would be excellent!"
    mc "Mmm..."
    yui "*Whispering*...Shut up! Were you really going to reject?"
    yui "*Whispering*...Don't you know how rude that was?"
    leo "(What are they whispering about? What's wrong with this guy?)"
    leo "(Why does [yui] seem to be so close to him?)"
    scene Welcomeparty6 with dissolve
    pete "Great!"
    pete "I can't wait to see how much you guys can drink!"
    liam "I'm sure that they can drink more than you..."
    pete "H-Hey! I was just sick last time, okay?"
    pete "Otherwise, there was no way I'd get drunk that easily!"
    liam "Hahaha... Okay. Whatever you say."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Welcomeparty7 with dissolve
    pete "Guys... Grab your beer. Then, stand up."
    scene Welcomeparty8 with dissolve
    pete "Okay...."
    pete "[mc], [yui]. Welcome to the team!"
    pete "Hopefully, we can get along together!"
    mc "...Sure."
    scene Welcomeparty9 with dissolve
    pete "And... For you guys..."
    pete "Thanks a lot for working so hard, and helping the company step closer to being successful."
    liam "Thanks for being such a good boss, too."
    pete "Let's forget about what happened in the meeting room today, okay?"
    pete "We're a team. We need to be united."
    joe "Agreed."
    pete "Cheers!"
    scene Welcomeparty10 with dissolve
    u "Hm? I've never had alcohol, because I didn't see any reason to drink it."
    u "But, it's much more delicious than I expected it to be..."
    scene black with dissolve
    u "*More than an hour later*...."
    scene Welcomeparty11 with dissolve
    pete "Hahahahaha... That's funny!"
    liam "Was it for real?"
    david "Yeah! He didn't believe me when I told him that I wasn't the hulk!"
    david "No matter what I did, he insisted that he wanted my signature...."
    pete "Hahahahaha..."
    scene Welcomeparty12 with dissolve
    mc "......"
    u "I don't... Understand. What's so funny?"
    u "Hm?"
    scene Welcomeparty13 with dissolve
    mc "Are you okay?"
    yui "U....Um..."
    u "I don't think so..."
    david "It's good to see [yui] in our department."
    scene Welcomeparty14 with dissolve
    mc "Hm?"
    scene Welcomeparty15 with dissolve
    david "You know... We're all guys here, except [yui]."
    david "So, we were the only department that didn't have a female worker."
    david "And our workplace looks a bit dull and boring, but we can't blame anyone for that."
    david "The company has to invest most of the money into the project."
    scene Welcomeparty16 with dissolve
    david "However, since we've got [yui], the environment has become better now."
    david "Moreover, our youngest sister is so beautiful."
    david "I can proudly say that she's as beautiful as {b}Six Angels{/b}!"
    scene Welcomeparty17 with dissolve
    mc "Six Angels. What is that?"
    leo "Let me tell you."
    leo "{b}Six Angels{/b} is the group name of the most beautiful women in our company."
    leo "They are all in a different department."
    scene Welcomeparty18 with dissolve
    leo "Cold as ice, even her hair is also white."
    leo "The angel of the Marketing department."
    scene Eira_Introduce1
    $ renpy.pause(0.3, hard=True)
    scene Eira_Introduce2
    $ renpy.pause(0.3, hard=True)
    scene Eira_Introduce3
    $ renpy.pause(0.3, hard=True)
    scene Eira_Introduce4
    $ renpy.pause(0.3, hard=True)
    leo "Her name is [eira]!"
    scene Welcomeparty19 with dissolve
    leo "The angel of the customer support department."
    scene Eliane_Introduce1
    $ renpy.pause(0.3, hard=True)
    scene Eliane_Introduce2
    $ renpy.pause(0.3, hard=True)
    scene Eliane_Introduce3
    $ renpy.pause(0.3, hard=True)
    scene Eliane_Introduce4
    $ renpy.pause(0.3, hard=True)
    scene Eliane_Introduce5
    $ renpy.pause(0.3, hard=True)
    scene Eliane_Introduce6
    $ renpy.pause(0.3, hard=True)
    leo "The party queen, [elaine]!"
    leo "If [eira] was as cold as ice, then [elaine] would be as hot as fire!"
    scene Welcomeparty20 with dissolve
    leo "Sometimes, she is just an ordinary girl, but sometimes she isn't."
    leo "The bookworm angel of the Language quality assurance department."
    scene Wendy_Introduce1
    $ renpy.pause(0.3, hard=True)
    scene Wendy_Introduce2
    $ renpy.pause(0.3, hard=True)
    scene Wendy_Introduce3
    $ renpy.pause(0.3, hard=True)
    scene Wendy_Introduce4
    $ renpy.pause(0.3, hard=True)
    scene Wendy_Introduce5
    $ renpy.pause(0.3, hard=True)
    leo "Her name is [wendy]!"
    scene Welcomeparty21 with dissolve
    leo "Legend has it that it doesn't matter how bright the sun can shine."
    leo "It can't be as bright as her gorgeous smile!"
    leo "The very kind, and friendly angel of the community management department."
    leo "Let me hear you shout her sweet name..."
    scene Rin_Introduce1
    $ renpy.pause(0.3, hard=True)
    scene Rin_Introduce2
    $ renpy.pause(0.3, hard=True)
    scene Rin_Introduce3
    $ renpy.pause(0.3, hard=True)
    leo "[rin]!!"
    scene Welcomeparty22 with dissolve
    leo "Where there is light, there must be shadow."
    leo "The arrogant angel of the Project management department."
    leo "The woman who doesn't seem to care about anyone in the world..."
    scene Faye_Introduce1
    $ renpy.pause(0.3, hard=True)
    scene Faye_Introduce2
    $ renpy.pause(0.3, hard=True)
    scene Faye_Introduce3
    $ renpy.pause(0.3, hard=True)
    scene Faye_Introduce4
    $ renpy.pause(0.3, hard=True)
    leo "[faye]!"
    scene Welcomeparty41 with dissolve
    leo "And the last angel is..."
    scene Sally_Introduce1
    $ renpy.pause(0.3, hard=True)
    scene Sally_Introduce2
    $ renpy.pause(0.3, hard=True)
    scene Sally_Introduce3
    $ renpy.pause(0.3, hard=True)
    scene Sally_Introduce4
    $ renpy.pause(0.3, hard=True)
    scene Sally_Introduce5
    $ renpy.pause(0.3, hard=True)
    leo "...[sally]!"
    leo "The angel of the Game specialist department."
    leo "She's well known for her playful personality!"
    scene black with dissolve
    $ renpy.pause()
    scene Welcomeparty23 with dissolve
    liam "But...."
    liam "You guys said that [yui] is as beautiful as the six Angels, then I assume that we can't call them Six Angels anymore."
    liam "How could we call them that when there are actually seven people?"
    u "....I don't actually care about it, anyway."
    scene Welcomeparty24 with dissolve
    liam "By the way, seems like our angel has just gone back to heaven!"
    liam "She is such a lightweight, just like our boss, hahaha."
    mc "......"
    scene Welcomeparty25 with dissolve
    mc "Hey, are you drunk?"
    leo "Stop bothering her, man! Let her sleep."
    scene Welcomeparty26 with dissolve
    yui "Who said that I'm drunk!"
    leo "Oh.. Shit! You shocked me, [yui]!"
    yui "....."
    scene Welcomeparty27 with dissolve
    yui "Look. I'm....not drunkkk..I'm just a...lil bit...tipsy..."
    yui "I can understand your conversation, okayyy~?"
    mc "....."
    scene Welcomeparty28 with dissolve
    yui "Why don't you... Answer meee!?"
    yui "'You're not drunk'. Say it!"
    david "Hahaha. She's so cute...."
    mc "......"
    yui "Say! It!"
    mc "*Sigh*..... You're not drunk."
    scene Welcomeparty29 with dissolve
    yui "Good!"
    yui "Ummm... Your shoulder... feels so comfortable...."
    mc "... When will we finish?"
    leo "Why? You want to leave already?"
    mc ".... Yes."
    scene black with dissolve
    s "*One more hour later*....."
    scene Welcomeparty30 with dissolve
    david "Ahhh... I'm so full!"
    leo "Me, too!"
    liam "Of course you guys are. Do you realise that you've been eating nonstop for two hours?"
    liam "Look... Our boss and the others are already drunk."
    david "Then, let's pay the bill, and leave."
    scene Welcomeparty31 with dissolve
    liam "[mc]! [leo]!"
    mc "..... Hm?"
    liam "We're leaving now. Let's go!"
    leo "S...Sure..."
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Welcomeparty32 with dissolve
    mc "....Stand still."
    yui "...Ummmm..."
    leo "[yui]!... Do you want me... To take you.... Hom-!"
    scene Welcomeparty33 with dissolve
    leo "Ouch!"
    leo "What are you doing, [david]!? Release meeee!...."
    david "Are you sure that you're okay, [mc]?"
    mc "....Yes."
    david "Do you know where [yui] lives?"
    mc "Yes. We live in the same shared house."
    leo "W-What!?..."
    david "Okay. Then, get home safely."
    scene Welcomeparty34 with fade
    yui "...What... Are you doing?"
    yui "....Take your...hands off...me. I...can walk...by...my own."
    u "I don't know why am I doing this either."
    u "Maybe it's because of alcohol..."
    mc ".... You can't even stand straight..."
    yui "I told you to..."
    scene Welcomeparty35 with dissolve
    yui "Take your hands off me!"
    mc "Ouch!..."
    mc "Stop!... It hurts!"
    scene Welcomeparty36 with dissolve
    yui "....."
    mc "....."
    yui "Well... since you... think I'm drunk... then, I'll...act like one."
    u "...You're actually drunk..."
    yui "...On your knees."
    mc "....."
    scene Welcomeparty37 with dissolve
    yui "I said... On your knees!"
    mc "But why?"
    yui "I'm...drunk. You have to give me...a piggy back ride."
    yui "Otherwise... I'm not going...home with you!"
    mc "......"
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Welcomeparty38 with dissolve
    u ".... I could just leave her there alone easily..."
    u "But why did I not do that?..."
    yui "You know... I hate you."
    mc "......"
    yui "[leo]... [david].... [liam] and every guy..."
    yui "I hate all of them..."
    yui "Every guy I've met has always said that girls shouldn't be dreaming about being a game developer..."
    yui "'It's a man job', 'Why don't you choose to be a secretary?'"
    yui "'Girls know nothing about games'. Who were you to say that!?"
    yui "You guys are biased, and abusing my ability, except [pete]..."
    u "......."
    menu:
        "Not everyone is the same [yui1]":
            $ Yuireason = True
            $ yui_ch1_ep1 += 1
            $ yui_relationship = yui_ch1_ep1
            scene Welcomeparty39 with dissolve
            mc "You're also being biased, too."
            yui "....W-What!?..."
            mc "I don't know who you met, but not all guys are the same."
            mc "At least I'm sure I've never said something like that."
            yui "....."
            scene Welcomeparty40 with dissolve
            yui "....Who are you to say that!"
            mc "Ouch...."
            yui "I don't.... Need you to... comfort me!..."
            mc "........"
            jump Nextday
        "Stay quiet":
            $ Yuireason = True
            scene Welcomeparty39 with dissolve
            mc "......"
            yui "See?... Even you also look down on me..."
            mc "What? I didn't even say anything."
            scene Welcomeparty40 with dissolve
            yui "Yes! You just kept being quiet!"
            mc "Ouch...."
            yui "And It means you agreed with them!"
            mc "Wait? How come did you think like that?"
            yui "...Shut up!"
            jump Nextday
label Nextday:
    scene black with dissolve
    $ renpy.pause(0.5,hard=True)
    scene Nextday1 with dissolve
    u "......."
    yui "......."
    u "....Wait.... What just happened?..."
    scene Nextday2 with dissolve
    u "Is this her room? No, it's mine."
    u "Why is she sleeping here? Moreover, why are we naked?"
    u "What should I do?"
    menu:
        "Wake her up":
            u "Well, it's my room. I have no reason to run away."
            scene Nextday3_Wake1 with dissolve
            mc "[yui]..."
            yui "Ummmmm...."
            mc "Wake up."
            yui "Five more minutes, Mom..."
            mc "[yui]."
            scene Nextday3_Wake2 with dissolve
            yui "Mom! I said give me five..."
            yui "....."
            scene Nextday3_Wake3 with dissolve
            yui "!!!!!"
            mc "Are you awake?"
        "Try to leave quietly":
            u "I think I should leave quietly."
            u "I'm too lazy to hear her yelling at me after she's awake."
            scene Nextday3_Leave1 with dissolve
            u "How am I supposed to leave though?"
            u "She's sleeping on top of my right arm..."
            u "If I move my arm, she is going to wake up for sure."
            scene Nextday3_Leave2 with dissolve
            yui "Ummmm...."
            u "That's what I was talking about...."
            u "Three..."
            u "Two..."
            u "One..."
            scene Nextday3_Leave3 with dissolve
            yui "!!!!!"
            u "....I'm screwed...."
    scene Nextday4 with dissolve
    yui "*Screaming*....."
    u "Ouch... My ear..."
    scene Nextday5 with dissolve
    yui "You asshole! W-What did you do to me last night!?"
    mc "I can't remember. I just woke up and saw you in my room."
    yui "You can't remember!? That's the worst excuse I've ever heard!"
    scene Nextday6 with dissolve
    mc "Hey. Calm down.... I'm not l-"
    yui "Calm down!? Are you serious!?"
    yui "Do you realise what you took from me!?"
    $ renpy.sound.play("sfx/Door opening.mp3")
    s "*Door opening in a hurry*...."
    scene Nextday7 with dissolve
    zeke "Are you okay, [mc]? I heard someone screaming..."
    scene Nextday8 with dissolve
    zeke "Oh shit!"
    scene Nextday10 with dissolve
    mc "....It's not what you..."
    zeke "It's okay. Don't mind me."
    zeke "I'm sorry for interrupting you guys!"
    scene Nextday11 with dissolve
    $ renpy.sound.play("sfx/Door closing.mp3")
    s "*Door closing in a hurry*...."
    mc "......"
    scene Nextday12 with dissolve
    mc "Hey. I'm sor-"
    yui "Shut up! I don't want to hear your ugly voice!"
    yui "Don't you dare talk to me ever again!"
    scene black with dissolve
    $ renpy.sound.play("sfx/Door slamming.mp3")
    u "*Door slamming*...."
    scene Nextday13 with dissolve
    u "....What a headache situation...."
    u "What actually happened last night?"
    u "She might think I'm a pervert by now."
    u "But I'm sure that I didn't do something like that."
    u "I'm not interested in love and sex, there was no reason for me to do it."
    u "I should find some evidence to redeem myself..."
    stop sound fadeout 3.0
    play music "sfx/After party.mp3" fadein 3.0
    $ bgm = "Bensound - Elevate"
    $ area = "MCRoom"
    $ yui_sex += 1
    $ newmessage = True
    $ alice_messages_show = True
    $ alice_newmessage = True
    $ Yuifirstsex = True
    $ phone_alert = True
    modsnote2 "There are 5 Special Images to collect as you Roam which I have marked."
    modsnote2 "You can ignore going to see Yui until after you have spoken to both Zeke & Rin about what happened last night."
    modsnote2 "Be sure to choose all their converstion Options, as well as get their phone numbers. [smpu]\[Next click goes to free roam\]"
    jump House
label House:
    show screen smartphone
    if area == "YuiRoom":
        scene black
        scene Misunderstand1 with dissolve
        if Whathappenedlastnight == False:
            menu:
                "Knock":
                    play sound "sfx/Door knocking.mp3"
                    s "*Knocking*...."
                    mc "We need to talk."
                    yui "Leave me alone!"
                    u "I shouldn't bother her without the evidence to redeem myself."
                    $ area = "Second floor1"
                    jump House
                "Leave":
                    u "I shouldn't bother her without the evidence to redeem myself."
                    $ area = "Second floor1"
                    jump House
        elif Whathappenedlastnight == True:
            if reply_alice1 == False:
                scene black
                scene black with vpunch
                s "You need to answer [alice]'s message first!!"
                $ area = "Second floor1"
                jump House
            else:
                menu:
                    "Knock [yui1]":
                        play sound "sfx/Door knocking.mp3"
                        s "*Knocking*...."
                        mc "We need to talk."
                        yui "Leave me alone!"
                        mc "...."
                        jump Misunderstand
                    "Leave":
                        u "I have the witness now, but I don't think it's the right time to talk."
                        $ area = "Second floor1"
                        jump House
    elif area == "KrystalRoom":
        scene SecondFloor2
        $ renpy.sound.play("sfx/Locked door.mp3")
        u "I can't go in there."
        $ area = "Second floor2"
        jump House
    else:
        call screen HouseEp1Ch1
label ZekeTalk:
    if Whathappenedlastnight == False:
        scene Zeke_Room
        scene ZekeTalk1 at eyesblink("Ch.1/Ep.1/Scenes/ZekeTalk1.jpg", "Ch.1/Ep.1/Scenes/ZekeTalk1_blink.jpg", 1) with dissolve
        zeke "What are you doing here, playboy?"
        mc "I'm not a playboy...."
        zeke "Did you finish your business with [yui] already?"
        zeke "You are more wicked than I thought, haha!"
        mc "....Stop it."
        mc "I want to..."
        jump ZekeTalkEp1Ch1
    elif Whathappenedlastnight == True:
        scene Zeke_Room
        scene ZekeTalk1 at eyesblink("Ch.1/Ep.1/Scenes/ZekeTalk1.jpg", "Ch.1/Ep.1/Scenes/ZekeTalk1_blink.jpg", 1) with dissolve
        zeke "Hm? Is there something you want to talk?"
        jump ZekeTalkEp1Ch1
label ZekeTalkEp1Ch1:
    menu:
        "Talk":
            mc "Talk."
            zeke "Hm? What do you want to talk about?"
            if zeke_contact == False:
                menu:
                    "About you":
                        mc "You."
                        zeke "What do you want to know?"
                        menu:
                            "Favorites":
                                mc "I want to know your favorite things."
                                if zeke_like1 == "Cars":
                                    zeke "Hm? I already told you that, didn't I?"
                                    mc "Yeah... sorry."
                                    jump ZekeTalkEp1Ch1
                                elif zeke_like1 == "???":
                                    zeke "Cars! Of course!"
                                    mc "No doubt..."
                                    $ zeke_like1 = "Cars"
                                    jump ZekeTalkEp1Ch1

                            "Dislikes":
                                mc "Do you have something that you dislike?"
                                if zeke_hate1 == "Liars":
                                    zeke "Hm? I already told you that, didn't I?"
                                    mc "Yeah... sorry."
                                    jump ZekeTalkEp1Ch1
                                elif zeke_hate1 == "???":
                                    zeke "Um... Let me think..."
                                    scene ZekeTalk2 at eyesblink("Ch.1/Ep.1/Scenes/ZekeTalk2.jpg", "Ch.1/Ep.1/Scenes/ZekeTalk2_blink.jpg", 1) with dissolve
                                    zeke "Oh! I hate liars."
                                    zeke "I don't understand how someone can tell so many lies and never feel bad about it."
                                    mc "I see..."
                                    scene ZekeTalk1 at eyesblink("Ch.1/Ep.1/Scenes/ZekeTalk1.jpg", "Ch.1/Ep.1/Scenes/ZekeTalk1_blink.jpg", 1) with dissolve
                                    $ zeke_hate1 = "Liars"
                                    jump ZekeTalkEp1Ch1
                            "Nothing":
                                mc "Forget it."
                                zeke "Hm? Are you going to leave just like that?"
                                mc "Yes."
                                jump House
                    "Your phone number [zeke1]":
                        mc "Can I have your number?"
                        scene ZekeTalk2 at eyesblink("Ch.1/Ep.1/Scenes/ZekeTalk2.jpg", "Ch.1/Ep.1/Scenes/ZekeTalk2_blink.jpg", 1) with dissolve
                        zeke "Oh? Did I forget to give it to you?"
                        mc "Yes."
                        zeke "Okay, then here you are!"
                        mc "Thank you."
                        scene ZekeTalk1 at eyesblink("Ch.1/Ep.1/Scenes/ZekeTalk1.jpg", "Ch.1/Ep.1/Scenes/ZekeTalk1_blink.jpg", 1) with dissolve
                        $ zeke_ch1_ep1 += 1
                        $ zeke_relationship = zeke_ch1_ep1
                        $ zeke_contact = True
                        jump ZekeTalkEp1Ch1
                    "What happened last night?":
                        mc "Do you know what happened last night?"
                        zeke "Hm? What do you mean?"
                        mc "Do you know why [yui] was in my bedroom?"
                        scene ZekeTalk2 at eyesblink("Ch.1/Ep.1/Scenes/ZekeTalk2.jpg", "Ch.1/Ep.1/Scenes/ZekeTalk2_blink.jpg", 1) with dissolve
                        zeke "Hm? I don't know that, but...."
                        mc "But?"
                        zeke "Didn't you take her there by yourself?"
                        mc "....Forget it."
                        zeke "Hm? Are you going to leave just like that?"
                        mc "Yes."
                        jump House
                    "Leave":
                        mc "Forget it."
                        zeke "Hm? Are you going to leave just like that?"
                        mc "Yes."
                        jump House
            else:
                menu:
                    "About you":
                        mc "You."
                        zeke "What do you want to know?"
                        menu:
                            "Favorites":
                                mc "I want to know your favorite things."
                                if zeke_like1 == "Cars":
                                    zeke "Hm? I already told you that, didn't I?"
                                    mc "Yeah... sorry."
                                    jump ZekeTalkEp1Ch1
                                elif zeke_like1 == "???":
                                    zeke "Cars! Of course!"
                                    mc "No doubt..."
                                    $ zeke_like1 = "Cars"
                                    jump ZekeTalkEp1Ch1
                            "Dislikes":
                                mc "Do you have something that you dislike?"
                                if zeke_hate1 == "Liars":
                                    zeke "Hm? I already told you that, didn't I?"
                                    mc "Yeah... sorry."
                                    jump ZekeTalkEp1Ch1
                                elif zeke_hate1 == "???":
                                    zeke "Um... Let me think..."
                                    scene ZekeTalk2 at eyesblink("Ch.1/Ep.1/Scenes/ZekeTalk2.jpg", "Ch.1/Ep.1/Scenes/ZekeTalk2_blink.jpg", 1) with dissolve
                                    zeke "Oh! I hate liars."
                                    zeke "I don't understand how someone can tell so many lies and never feel bad about it."
                                    mc "I see..."
                                    scene ZekeTalk1 at eyesblink("Ch.1/Ep.1/Scenes/ZekeTalk1.jpg", "Ch.1/Ep.1/Scenes/ZekeTalk1_blink.jpg", 1) with dissolve
                                    $ zeke_hate1 = "Liars"
                                    jump ZekeTalkEp1Ch1
                            "Nothing":
                                mc "Forget it."
                                zeke "Hm? Are you going to leave just like that?"
                                mc "Yes."
                                jump House
                    "What happened last night?":
                        mc "Do you know what happened last night?"
                        zeke "Hm? What do you mean?"
                        mc "Do you know why [yui] was in my bedroom?"
                        scene ZekeTalk2 at eyesblink("Ch.1/Ep.1/Scenes/ZekeTalk2.jpg", "Ch.1/Ep.1/Scenes/ZekeTalk2_blink.jpg", 1) with dissolve
                        zeke "Hm? I don't know that, but...."
                        mc "But?"
                        zeke "Didn't you take her there by yourself?"
                        mc "....Forget it."
                        zeke "Hm? Are you going to leave just like that?"
                        mc "Yes."
                        jump House
                    "Leave":
                        mc "Forget it."
                        zeke "Hm? Are you going to leave just like that?"
                        mc "Yes."
                        jump House
        "Leave":
            mc "Forget it."
            zeke "Hm? Are you going to leave just like that?"
            mc "Yes."
            jump House
label RinTalk:
    if Whathappenedlastnight == False:
        if Rininunderwear == False:
            $ Rininunderwear = True
            scene RinRoom
            mc "[rin]."
            scene RinTalk1 with dissolve
            rin "Hm... [mc]?"
            mc "Oh... I'm sorry."
            mc "I'll wait for you outside."
            scene RinTalk2 with dissolve
            rin "Wait. You don't have to."
            rin "It's not like you saw me full naked, right?"
            rin "I don't mind being seen in an underwear..."
            rin "In my opinion, it's the same as being seen in a bikini."
            mc "Okay then..."
            scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
            rin "Alright, I assume that you came here for a reason."
            rin "What is it?"
            mc "I want to..."
            jump RinTalkEp1Ch1
        elif Rininunderwear == True:
            scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
            rin "Good morning, [mc]."
            rin "What makes you come here?"
            mc "I want to..."
            jump RinTalkEp1Ch1
    elif Whathappenedlastnight == True:
        scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
        rin "Good morning, [mc]."
        rin "What makes you come here?"
        mc "I want to..."
        jump RinTalkEp1Ch1
label RinTalkEp1Ch1:
    menu:
        "Talk":
            mc "Talk."
            rin "Talk?"
            rin "Okay, I'm a bit surprised to see you wanted to talk first."
            rin "Well, what do you want to talk about?"
            if rin_contact == False:
                menu:
                    "About you":
                        mc "You."
                        rin "What do you want to know?"
                        menu:
                            "Favorites":
                                mc "What are the things you like?"
                                if rin_like1 == "Shopping":
                                    scene RinTalk4 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                                    rin "Hm? Didn't I already told you that?"
                                    mc "Oh... You did. I'm sorry."
                                    scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
                                    jump RinTalkEp1Ch1
                                elif rin_like1 == "???":
                                    scene RinTalk4 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                                    rin "Heh... You want to know my favorite things?"
                                    rin "Um... For now. Let's say I like shopping."
                                    mc "Only shopping?"
                                    rin "I'll tell you about others when I think we're close enough."
                                    mc "Okay."
                                    scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
                                    $ rin_like1 = "Shopping"
                                    jump RinTalkEp1Ch1
                            "Dislikes":
                                mc "What are the things you hate?"
                                if rin_hate1 == "Money":
                                    scene RinTalk4 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                                    rin "Hm? Didn't I already told you that?"
                                    mc "Oh... You did. I'm sorry."
                                    scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
                                    jump RinTalkEp1Ch1
                                elif rin_hate1 == "???":
                                    rin "I hate you."
                                    mc "What?"
                                    scene RinTalk4 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                                    rin "*Giggles*... Just kidding."
                                    rin "Uhmm.... I hate money."
                                    rin "It can change people. Turning someone from good to evil."
                                    mc "I agree with you."
                                    scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
                                    $ rin_hate1 = "Money"
                                    jump RinTalkEp1Ch1
                            "Nothing":
                                mc "Forget it."
                                rin "Hm? Are you going to leave just like that?"
                                mc "Yes."
                                jump House
                    "Your phone number [rin1]":
                        mc "Can I have your number?"
                        rin "Hm?..."
                        mc "What?"
                        rin "Are you trying to hit on me?"
                        mc "...."
                        mc "It's just for an emergency case..."
                        scene RinTalk4 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                        rin "*Giggles*... Just kidding! Don't be so serious."
                        mc "Oh..."
                        rin "May I ask why you have to keep your emotionless face all the time?"
                        mc "Emotionless?"
                        rin "Yes."
                        mc "I don't understand your question. {w}My face is just always like this."
                        scene RinTalk3 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
                        rin "I noticed that you've never smiled even once since you've been here."
                        mc "....."
                        rin "That's a pity..."
                        rin "I'm sure you'd look really great if you smile."
                        mc "There is no reason for me to smile."
                        rin "....."
                        rin "You're really weird..."
                        rin "But never mind. Here is my number!"
                        mc "Thank you."
                        $ phone_alert = True
                        $ newmessage = True
                        $ rin_messages_show = True
                        $ rin_newmessage = True
                        $ rin_ch1_ep1 += 1
                        $ rin_relationship = rin_ch1_ep1
                        $ rin_contact = True
                        jump RinTalkEp1Ch1
                    "What happened last night?":
                        if Whathappenedlastnight == False:
                            mc "Do you know what happened last night?"
                            rin "Hm? What happened?"
                            mc "Did you see me getting home last night?"
                            scene RinTalk4 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                            rin "Oh, yeah. I saw you."
                            mc "Can you tell me more about it?"
                            rin "Sure."
                            jump TrueStoryFromTheWitness
                        elif Whathappenedlastnight == True:
                            mc "Do you know what happened last night?"
                            rin "Hm? I already told you that, didn't I?"
                            mc "Oh... Yes, you did."
                            jump House
                    "Leave":
                        mc "Forget it."
                        rin "Hm? Are you going to leave just like that?"
                        mc "Yes."
                        jump House
            else:
                menu:
                    "About you":
                        mc "You."
                        rin "What do you want to know?"
                        menu:
                            "Favorites":
                                mc "What are the things you like?"
                                if rin_like1 == "Shopping":
                                    scene RinTalk4 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                                    rin "Hm? Didn't I already told you that?"
                                    mc "Oh... You did. I'm sorry."
                                    scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
                                    jump RinTalkEp1Ch1
                                elif rin_like1 == "???":
                                    scene RinTalk4 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                                    rin "Heh... You want to know my favorite things?"
                                    rin "Um... For now. Let's say I like shopping."
                                    mc "Only shopping?"
                                    rin "I'll tell you about others when I think we're close enough."
                                    mc "Okay."
                                    scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
                                    $ rin_like1 = "Shopping"
                                    jump RinTalkEp1Ch1
                            "Dislikes":
                                mc "What are the things you hate?"
                                if rin_hate1 == "Money":
                                    scene RinTalk4 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                                    rin "Hm? Didn't I already told you that?"
                                    mc "Oh...you did. I'm sorry."
                                    scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
                                    jump RinTalkEp1Ch1
                                elif rin_hate1 == "???":
                                    rin "I hate you."
                                    mc "What?"
                                    scene RinTalk4 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                                    rin "*Giggles*... Just kidding."
                                    rin "Uhmm.... I hate money."
                                    rin "It can change people. Turning someone from good to evil."
                                    mc "I agree with you."
                                    scene RinTalk3 at eyesblink ("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
                                    $ rin_hate1 = "Money"
                                    jump RinTalkEp1Ch1
                            "Nothing":
                                mc "Forget it."
                                rin "Hm? Are you going to leave just like that?"
                                mc "Yes."
                                jump House
                    "What happened last night?":
                        if Whathappenedlastnight == False:
                            mc "Do you know what happened last night?"
                            rin "Hm? What happened?"
                            mc "Did you see me getting home last night?"
                            scene RinTalk4 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with dissolve
                            rin "Oh, yeah. I saw you."
                            mc "Can you tell me more about it?"
                            rin "Sure."
                            jump TrueStoryFromTheWitness
                        elif Whathappenedlastnight == True:
                            mc "Do you know what happened last night?"
                            rin "Hm? I already told you that, didn't I?"
                            mc "Oh... Yes, you did."
                            jump House
                    "Leave":
                        mc "Forget it."
                        rin "Hm? Are you going to leave just like that?"
                        mc "Yes."
                        jump House
        "Leave":
            mc "Nothing...."
            rin "Hm? Are you sure?"
            mc "Yes."
            jump House
label TrueStoryFromTheWitness:
    scene Witness1 with fade
    rin "Well, it was already dark outside. I'm not sure what time it was."
    rin "But you guys got home pretty late."
    mc "Keep telling."
    scene Witness2 with dissolve
    rin "Fortunately, I didn't go to sleep yet, because I was watching TV in the main hall."
    rin "I didn't hear you opening the main door because of the TV's sound."
    scene Witness3 with dissolve
    rin "So, while I was enjoying the movie, you suddenly appeared out of nowhere."
    rin "To be honest you almost gave me a heart attack!"
    mc ".....Did I?"
    scene Witness4 with dissolve
    rin "You both seemed drunk, especially [yui]."
    rin "She slept on your back while you were giving her a piggyback ride."
    rin "So, I asked you if there was someone trying to get her drunk, but you didn't answer me."
    scene Witness5 with dissolve
    rin "Actually, you didn't say anything at all..."
    rin "The only thing you did was just stare at me."
    rin "But that's enough to let me know what you wanted."
    scene Witness6 with dissolve
    rin "So, I told you where her room was."
    rin "Then, you suddenly walked towards there."
    scene Witness7 with dissolve
    rin "Fortunately for us, she didn't lock the room."
    rin "Otherwise, it would have been a bit difficult, because we'd have to find the key."
    rin "Then, I opened the door for you."
    scene Witness8 with dissolve
    rin "I thought there was nothing I could help with."
    rin "So, I just watched you walk into her room."
    scene Witness9 with dissolve
    rin "You slowly crouched down and carefully put [yui] down on her bed as if you were afraid that she might wake up."
    rin "To be honest I was a bit surprised. I never knew you were such a caring person."
    mc "......"
    scene Witness10 with dissolve
    rin "After putting her down on her bed, I didn't know what you were thinking,"
    rin "but you stood still and watched her sleeping for a while."
    scene Witness11 with dissolve
    rin "Then, you just went back to your room."
    rin "After seeing you closing the door, I went back to the main hall to continue watching TV."
    scene RinTalk4 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk4.jpg", "Ch.1/Ep.1/Scenes/RinTalk4_blink.jpg", 1) with fade
    rin "That's it."
    mc "......"
    rin "Why do you look so confused?"
    mc "If what you said is true..."
    mc "Then why?..."
    rin "Hm, why what? What are you talking about?"
    mc "......"
    mc "I woke up and saw [yui] sleeping naked with me in my bedroom."
    scene RinTalk5 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk5.jpg", "Ch.1/Ep.1/Scenes/RinTalk5_blink.jpg", 1) with dissolve
    rin "W-What!? Are you kidding me?"
    mc "....."
    mc "Do I look like I'm joking?"
    rin "No, you don't... But... How?"
    mc "I don't know either."
    rin "Did you guys....?"
    mc ".....I'm not sure."
    scene RinTalk5 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk5.jpg", "Ch.1/Ep.1/Scenes/RinTalk5_blink.jpg", 1) with dissolve
    mc "But, [yui] is so angry at me now."
    rin "That's understandable..."
    mc "Can you help me talk to her?"
    scene RinTalk3 at eyesblink("Ch.1/Ep.1/Scenes/RinTalk3.jpg", "Ch.1/Ep.1/Scenes/RinTalk3_blink.jpg", 1) with dissolve
    rin "Sure. It's unfair te be angry at you for something you didn't actually do."
    rin "But... You didn't go back to her room and take her to yours, right?"
    mc "....No."
    rin "Okay. Then, let's go to her room!"
    $ rin_ch1_ep1 += 1
    $ rin_relationship = rin_ch1_ep1
    $ Whathappenedlastnight = True
    jump House
label Misunderstand:
    play music "sfx/Nextday.mp3" fadein 3.0
    $ bgm = "Bensound - Perception"
    scene Misunderstand2 with dissolve
    rin "Let me try. She'll listen to me."
    mc "Okay."
    rin "Don't worry too much. Leave it to me!"
    scene Misunderstand3 with dissolve
    play sound "sfx/Door knocking.mp3"
    s "*Knocking*...."
    yui "I said...{b}LEAVE ME ALONE!{/b}"
    rin "It's me, [rin]."
    yui "....."
    rin "Can I come in?"
    yui "....."
    scene Misunderstand4 with dissolve
    play sound "sfx/Door opening.mp3"
    s "*Door opening*...."
    scene Misunderstand5 with dissolve
    rin "See? I told you."
    mc "....."
    rin "Alright, I'm going in."
    mc "What about me?"
    rin "Wait here."
    scene Misunderstand6 with dissolve
    rin "*Eyes winking*....Don't worry."
    rin "I'll make sure that she will no longer misunderstand you."
    mc "If you say so..."
    scene Misunderstand7 with dissolve
    rin "...."
    rin "Are you okay?"
    yui "....No, I'm not okay."
    scene Misunderstand8 with dissolve
    rin "What happened?"
    yui "...I've just lost the most valuable thing in my life...."
    rin "....."
    yui "That asshole just took it from me...."
    yui "I can no longer get married."
    rin "What makes you think like that?"
    yui "...Nobody would be crazy enough to marry a dirty woman."
    scene Misunderstand9 with dissolve
    rin "Poor kid..."
    rin "You won't become dirty just because you lost your virginity."
    rin "I don't know about other people,..."
    rin "But for me, we as women, shouldn't value ourselves from that."
    rin "There are many more things that can make us valuable."
    rin "Things such as ability, intelligence, and aptitude."
    rin "In my opinion, you're already perfect. You've got it all!"
    rin "I know it isn't that long since we met, but I can tell that."
    yui "......"
    scene Misunderstand10 with dissolve
    yui "....But, I wanted to save it for the man I love..."
    yui "I can't go see him anymore... I'm afraid that he will hate me."
    scene Misunderstand11 with dissolve
    rin "Listen. If he really loves you for real, your virginity wouldn't be a problem for him."
    rin "But if he knew that you aren't a virgin, and he suddenly hated you."
    rin "Then, just ditch him. He is just an idiot."
    rin "And that idiot doesn't deserve a really good woman like you."
    rin "You surely deserve someone better."
    scene Misunderstand10 with dissolve
    yui "...Thank you."
    rin "Your welcome."
    rin "Are you better now?"
    yui "I need more time... You understand me, right?"
    rin "Sure, you can take as much as you want."
    yui "Thanks."
    scene Misunderstand12 with dissolve
    rin "However!"
    yui "....Hm?"
    rin "There is something you must know."
    yui "......"
    rin "You're misunderstanding [mc]."
    scene Misunderstand10 with dissolve
    yui "What!? How can you s-?"
    rin "Calm down. I know that you're angry at him, {w}and it's because you think that he took advantage of you."
    rin "But he really didn't do it."
    yui "You're lying!"
    rin "No, I'm not. I saw you guys last night. He didn't bring you to his room."
    yui "How do you know that?"
    scene Misunderstand13 with dissolve
    rin "Because I was the one opening your bedroom's door for him."
    yui "......"
    rin "He gently put you down on this bed. Then he just went back to his room."
    yui "....Who knows? He might have just come back here and took me there..."
    rin "Do you really think he's that kind of person?"
    yui "......"
    rin "See? You already have the answer."
    rin "Alright, I'll leave you alone now..."
    rin "However, make sure that you get to the company in time. You don't want to clock in late, right?"
    yui "....Yeah, I get it."
    scene black with dissolve
    $ renpy.pause()
    scene Misunderstand14 with dissolve
    mc "How was she?"
    rin "Relax. She's fine now."
    rin "I also told her what actually happened last night,..."
    rin "so I assume that it's clear to say that she's no longer misunderstanding you now."
    mc "Thank you."
    rin "Your welcome."
    scene Misunderstand15 with dissolve
    rin "*Giggles*...By the way, I never knew you were such a lightweight!"
    mc "....It wasn't my fault. I never had booze before."
    rin "Oh, that's why I didn't see you drinking the wine last time."
    mc "Yeah, and I will never drink again."
    scene Misunderstand14 with dissolve
    rin "Well, that's such a pity..."
    mc "Why?"
    rin "You're kinda cute when you're drunk. I won't have a chance to see that again."
    mc "......"
    scene black with dissolve
    $ renpy.pause()
    scene Misunderstand16 with dissolve
    yui "(What [rin] just told me... Was it real?)"
    yui "(If he wasn't the one who took me to his room, then who did...?)"
    yui "(Wait.... I'm starting to remember something....)"
    jump Truth

label Truth:
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
    $ renpy.pause(1, hard=True)
    scene Truth1 with fade
    yui "Ahh... What a relief..."
    scene Truth2 with dissolve
    yui "It's so dark... I can't see anything."
    yui "Let's get back to my room..."
    scene Truth3 with dissolve
    $ renpy.pause()
    scene Truth4 with dissolve
    $ renpy.pause()
    scene Truth5 with dissolve
    yui "Mmm... So comfortable..."
    yui "...Hm?"
    scene Truth6 with dissolve
    yui "[pete]...?"
    yui "Why are you here in my bedroom? How...?"
    yui "This is a dream, right?"
    yui "Well, it doesn't matter."
    scene Truth7 with dissolve
    mc "Ummm.... Hm...? [yui]...?"
    mc "What are you doing my bedroom?"
    yui "Do you know how long I have been waiting to see you?"
    yui "It's been three years."
    yui "But, you don't even remember me."
    mc "I don't remember you...?"
    yui "...I love you..."
    scene Truth9 with dissolve
    yui "I often dreamed about doing this so many times..."
    yui "But this time is the most realistic..."
    yui "Let me take off my clothes..."
    scene Truth10 with dissolve
    $ renpy.pause()
    scene Truth11 with dissolve
    $ renpy.pause()
    scene Truth12 with dissolve
    yui "Look I've grown up now, right?"
    yui "Am I as beautiful as that woman?"
    scene Truth13 with dissolve
    yui "Why don't you answer me...?"
    yui "Never mind...."
    scene Truth14 with dissolve
    yui "Let me take off your clothes..."
    scene Truth15 with dissolve
    yui "Hehe your body is sexier than ever..."
    scene Truth16 with dissolve
    yui "Don't misunderstand me..."
    yui "I'm not a lewd girl..."
    yui "It's just this is a dream...."
    yui "It isn't real that's why I'm doing this..."
    menu:
        "Let her do it.":
            $ sexwithyui = 1
            scene Truth17 with dissolve
            show Drunk_Blowjob1 with dissolve
            yui "Mmmm...."
            yui "How is it....?"
            mc "It feels so good..."
            yui "I'm glad to hear that..."
            menu:
                "Faster":
                    hide Drunk_Blowjob1
                    scene Truth18 with dissolve
                    show Drunk_Blowjob2 with dissolve
                    yui "Mmmm I've been practicing this a lot..."
                    yui "I wanted to impress you..."
                    yui "Of course not in a dream like this..."
                    yui "I mean in real life..."
                    menu:
                        "Next":
                            hide Drunk_Blowjob2
                            scene black with dissolve
                            $ renpy.pause(0.3, hard=True)
            scene Truth19 with dissolve
            yui "Now, it's... Time..."
            yui "I want to be yours..."
            yui "And I want you... To be mine, too..."
            scene Truth20 with dissolve
            yui "Nothing has ever been inside my private area before..."
            yui "Even though I dreamed about doing lewd things... With you,..."
            yui "We've never gone to this step..."
            yui "But I can't... Hold it...."
            scene Truth21 with dissolve
            yui "...Anymore!"
            yui "Urgh! It hurts!...."
            yui "But, I don't want to stop..."
            yui "I have to endure it...."
            scene Truth22 with dissolve
            yui "Argh! It's in!...."
            mc "Ugh... You're so tight... [yui]..."
            yui "Oh my... Why does it... Feel so painful... In a dream... Like this?"
            u "Dream? Am I dreaming right now...?"
            u "Whatever... Just forget it...."
            yui "I'm... Gonna... Start moving... Now..."
            show Drunk_Cowgirl1 with dissolve
            yui "Mmmm....."
            yui "So... This is what... Sex feels like..."
            yui "It hurt at first... But it's starting... To feel good now..."
            yui "It feels so good even in a dream."
            yui "I have no idea how'd it feel in real life..."
            menu:
                "Faster":
                    hide Drunk_Cowgirl1
                    scene Truth23 with dissolve
                    show Drunk_Cowgirl2 with dissolve
                    yui "*Giggles* Hehe... We belong to each other now..."
                    yui "I hope this... Is actually real..."
                    yui "Ahhh...."
                    menu:
                        "Faster":
                            hide Drunk_Cowgirl2
                            scene Truth24 with dissolve
                            show Drunk_Cowgirl3 with dissolve
                            yui "Ahh! Ahh! Mmm...!"
                            yui "Mmmm...... I can... Feel there is something... About... To come out!..."
                            yui "Ahh! Mmm! Almost there...!"
                            menu:
                                "Slowest":
                                    hide Drunk_Cowgirl3
                                    jump DrunkCowgirl1
                                "Slower":
                                    hide Drunk_Cowgirl3
                                    jump DrunkCowgirl2
                                "Cum":
                                    jump DrunkCowgirlCum
        "Stop her.":
            $ sexwithyui = 2
            scene Truth16_d1 with dissolve
            mc "Wait... We can't do it."
            yui "Why....? Don't you want to do it with me?"
            mc "This isn't right."
            mc "Let's stop it here."
            scene Truth16_d2 with dissolve
            yui "Okay... If that's what you want, [pete]..."
            u "Hm...? Did I hear it wrong...?"
            yui "I'm so sleepy now... It's a good dream after all... I'm happy."
            u "Whatever... Let's just sleep..."
            scene Misunderstand17 with fade
            yui "Argh!!... You idiot!"
            yui "Have you gone crazy, [yui]!? Were you out of your mind!?"
            yui "How did you think it was a dream!?"
            yui "What's even worse is, how were you so delusional that you misunderstood that [mc] was [pete]!?"
            yui "They are so different!"
            yui "You idiot! You idiot!..."
            yui "But fortunately, he stopped me..."
            yui "....What am I supposed to do when we meet now!?"
            $ yui_ch1_ep1 += 1
            $ yui_relationship = yui_ch1_ep1
            $ Truth = True
            jump Truth2
label DrunkCowgirl1:
    scene black with dissolve
    show Drunk_Cowgirl1 with dissolve
    $ renpy.pause()
    menu:
        "Faster":
            hide Drunk_Cowgirl1
            jump DrunkCowgirl2
        "Fastest":
            hide Drunk_Cowgirl1
            jump DrunkCowgirl3
label DrunkCowgirl2:
    scene black with dissolve
    show Drunk_Cowgirl2 with dissolve
    $ renpy.pause()
    menu:
        "Slower":
            hide Drunk_Cowgirl2
            jump DrunkCowgirl1
        "Faster":
            hide Drunk_Cowgirl2
            jump DrunkCowgirl3
label DrunkCowgirl3:
    scene black with dissolve
    show Drunk_Cowgirl3 with dissolve
    $ renpy.pause()
    menu:
        "Slowest":
            hide Drunk_Cowgirl3
            jump DrunkCowgirl1
        "Slower":
            hide Drunk_Cowgirl3
            jump DrunkCowgirl2
        "Cum":
            jump DrunkCowgirlCum
label DrunkCowgirlCum:
    yui "Mmm.....! I'm about to... Cum....!"
    mc "Me, too..."
    hide Drunk_Cowgirl3
    scene black with dissolve
    scene Truth25 with dissolve
    yui "Ahhhh....!"
    yui "This is... The... Best dream... Ever...!"
    scene black with dissolve
    $ renpy.pause(0.2, hard=True)
    scene Truth26 with dissolve
    yui "Time to sleep....."
    yui "Goodnight, [pete]...."
    u "What...? Did she just say [pete]...?"
    u "I might heard it wrong.... I'm so tired and sleepy now. Let's just sleep."
    scene Misunderstand17 with fade
    yui "Argh!!... You idiot!"
    yui "Have you gone crazy, [yui]!? Were you out of your mind!?"
    yui "How did you think it was a dream!?"
    yui "What's even worse is, how were you so delusional that you misunderstood that [mc] was [pete]!?"
    yui "They are so different!"
    yui "...And you just blamed him for your own mistake!"
    yui "...He must have thought I wanted to do it with him...!"
    yui "You idiot! You idiot!..."
    yui "....What am I supposed to do when we meet now!?"
    $ renpy.end_replay()
    $ yui_ch1_ep1 += 1
    $ yui_relationship = yui_ch1_ep1
    $ Truth = True
    jump Truth2
label Truth2:
    scene Misunderstand14 with fade
    rin "Alright, let's go and have a breakfast."
    menu:
        "Pat her head [rin1]":
            $ rin_ch1_ep1 += 1
            $ rin_relationship = rin_ch1_ep1
            scene Misunderstand18 with dissolve
            rin "W-What are you doing!?"
            mc "I don't know. I just feel like doing it."
            mc "Maybe it's because I'm grateful for your help."
            rin "{size=-15}....You shouldn't be doing this to a single woman...{/size}"
            mc "Hm? What?"
            rin "Nothing. Let's go..."
            mc "Okay."
        "Okay":
            mc "Okay."
            jump atoffice
    if Krystalintoilet == True:
        scene krystal_decision1 with dissolve
        rin "By the way, I suggest you to give her some time."
        rin "Don't just go to talk to her straight away."
        rin "It's better for you to wait until she approaches you first."
        scene krystal_decision2 with dissolve
        rin "Well, to think about it. Actually, I didn't even have to tell you that."
        rin "Judging from your personality, you're less likely going to talk with her first."
        scene krystal_decision3 with dissolve
        rin "Are you listening to..."
        scene krystal_decision4 with dissolve
        rin "...Hm?"
        scene krystal_decision5 with dissolve
        rin "(Where has he gone?)"
        rin "(Did he not follow me after agreeing to have breakfast?)"
        rin "(Whatever....)"
        rin "(I'm so hungry. Let's find something to eat.)"
        scene krystal_decision6 with fade
        mc "....."
        krystal "......"
        mc "[krystal]?"
        scene krystal_decision7 at eyesblink("Ch.1/Ep.1/Scenes/krystal_decision7.jpg", "Ch.1/Ep.1/Scenes/krystal_decision7_blink.jpg", 1) with dissolve
        krystal "[krystal]? Who?"
        mc "You."
        krystal "That isn't my name!"
        mc "Then, what's your name?"
        krystal "You don't have to know it."
        mc "Then, why did you bring me here?"
        krystal "We need to talk."
        scene krystal_decision6 with dissolve
        mc "If it was about last time. I'm so sorry. I didn't mean to..."
        krystal "That isn't what I want us to talk about."
        mc "Then?"
        krystal "Did you see my face?"
        krystal "Do you know who I am?"
        mc "...Yeah, you turned back to yell at me, so I saw your face."
        mc "But who are you? Am I supposed to know you?"
        scene krystal_decision8 at eyesblink("Ch.1/Ep.1/Scenes/krystal_decision8.jpg", "Ch.1/Ep.1/Scenes/krystal_decision8_blink.jpg", 1) with dissolve
        krystal "....."
        krystal "You don't really know me?"
        mc "No, I don't."
        krystal "(...He seems to be not lying.)"
        krystal "(But it might be because he saw my face only for a very few seconds...)"
        krystal "(I want to make sure...)"
        scene krystal_decision9 with dissolve
        krystal "(I know this is a risky move, but it's worth trying.)"
        scene krystal_decision10 at eyesblink("Ch.1/Ep.1/Scenes/krystal_decision10.jpg", "Ch.1/Ep.1/Scenes/krystal_decision10_blink.jpg", 1) with dissolve
        krystal "How about now?"
        krystal "Do you recognize me?"
        scene krystal_decision11 with dissolve
        mc "....No, I don't."
        mc "Should I know you?"
        scene krystal_decision12 at eyesblink("Ch.1/Ep.1/Scenes/krystal_decision12.jpg", "Ch.1/Ep.1/Scenes/krystal_decision12_blink.jpg", 1) with dissolve
        krystal "....."
        krystal "(I can't believe there is a guy who doesn't know me...)"
        krystal "Nevermind... You may leave now."
        mc "Okay."
        scene krystal_decision13 at eyesblink("Ch.1/Ep.1/Scenes/krystal_decision13.jpg", "Ch.1/Ep.1/Scenes/krystal_decision13_blink.jpg", 1) with dissolve
        krystal "Wait!"
        mc "....."
        krystal "Don't tell anyone that I live here."
        mc "How could I? I don't even know your real name."
        mc "They're gonna ask me back something like..."
        mc "...[krystal]? Who?"
        scene krystal_decision12 at eyesblink("Ch.1/Ep.1/Scenes/krystal_decision12.jpg", "Ch.1/Ep.1/Scenes/krystal_decision12_blink.jpg", 1) with dissolve
        krystal "You're right."
        krystal "(To be honest I'm really lonely....)"
        krystal "(I've been hiding, and living alone for more than two years.)"
        krystal "(...Can I trust this guy?)"
        krystal "(He doesn't look like he has a big mouth...)"
        krystal "(......)"
        krystal "(Well... I think I can tell him my real name)"
        scene krystal_decision14 at eyesblink("Ch.1/Ep.1/Scenes/krystal_decision14.jpg", "Ch.1/Ep.1/Scenes/krystal_decision14_blink.jpg", 1) with dissolve
        krystal "Okay. I will let you know my real name."
        $ krystal_name = "Krystal"
        $ persistent.krystal_name = krystal_name
        krystal "You can call me [krystal]. What's your name?"
        mc "[mc]."
        krystal "[mc]...? You've got such a good name."
        krystal "Come. Let's do a pinky swear that you won't tell anyone about me."
        mc "......"
        menu:
            "Do it [krystal1]":
                scene krystal_decision15 at eyesblink("Ch.1/Ep.1/Scenes/krystal_decision15.jpg", "Ch.1/Ep.1/Scenes/krystal_decision15_blink.jpg", 1) with dissolve
                mc "Okay. I promise."
                krystal "Great!"
                krystal "Alright... Let's forget about our weird first meet up, nice to meet you, [mc]."
                mc "...Nice to meet you, too."
                mc "May I leave now? I have to go to work."
                krystal "Oh, sure!"
                mc "Thanks."
                $ pinkyswear = True
                $ krystal_ch1_ep1 += 1
                $ krystal_relationship = krystal_ch1_ep1
                jump atoffice
            "Don't do it.":
                scene krystal_decision16 with dissolve
                mc "I don't want to do it, but I give you my promise."
                krystal "......"
                mc "May I leave now? I have to go to work."
                krystal "...Oh... Yes, you can leave now."
                krystal "I'm sorry to keep you here."
                mc "Bye."
                krystal "....."
                jump atoffice
    elif Krystalintoilet == False:
        scene krystal_decision1 with dissolve
        rin "By the way, I suggest you to give her sometimes."
        rin "Don't just go to talk to her straight away."
        rin "It's better for you to wait until she approaches you first."
        scene Breakfastwithrin with dissolve
        rin "Well, to think about it. Actually, I didn't even have to tell you that."
        rin "Judging from your personality, you're less likely going to talk with her first."
        mc "...Yeah. You know me well."
        rin "*Giggles*... Do I?"
        jump atoffice

label atoffice:
    play music "sfx/atoffice.mp3" fadein 3.0
    $ bgm = "B3NJ4M1N - Rainy Days"
    scene black with dissolve
    $ renpy.pause()
    scene atoffice1 with fade
    u "I wonder if there will be anyone here at this time."
    u "I remember last night [pete] and [leo] were also drunk."
    scene atoffice2 at eyesblink("Ch.1/Ep.1/Scenes/atoffice2.jpg", "Ch.1/Ep.1/Scenes/atoffice2_blink.jpg", 1) with dissolve
    liam "Morning, [mc]."
    mc "....Hi."
    u "You almost gave me a heart attack..."
    liam "You manage to get here on time even though we had a party last night."
    liam "Great. I like your spirit!"
    david "[liam], can you come here for a sec?"
    scene atoffice3 with dissolve
    liam "Oh, okay! I'm coming."
    u "Hm? That was [david]'s voice. So, I assume that everyone is already here."
    scene atoffice4 at eyesblink("Ch.1/Ep.1/Scenes/atoffice4.jpg", "Ch.1/Ep.1/Scenes/atoffice4_blink.jpg", 1) with dissolve
    liam "Well... Before I leave, I want to tell you that I already gave you, your work for today."
    liam "It's in a folder on the bottom right of your desktop."
    liam "You can check it. If you need help, just call me."
    mc "Okay."
    liam "Good."
    scene atoffice5 with dissolve
    u "Well... Let's see what I have to do for today."
    u "Umm... There are a few bug reports..."
    u "Players don't get the experiences after killing monsters in red desert."
    u "The high priest of holy light church disappeared after a player finished his quest...."
    u "Well... Let's see what I can do about it..."
    scene black with dissolve
    s "*A few hours later*...."
    scene atoffice6 with dissolve
    u "*Sigh*... Time flies so fast..."
    u "It's already noon. I'm starting to get hungry."
    scene atoffice7 with dissolve
    u "Let's go and find something to eat..."
    david "[mc]. Wait!"
    u "Hm?"
    scene atoffice8 with dissolve
    mc "What do you want from me?"
    david "Let's have lunch together!"
    liam "Yeah, we're going to the cafeteria."
    liam "You should come with us."
    u "...What should I say?"
    menu:
        "Okay [smpi]\[Eira Route\]":
            scene atoffice8_okay with dissolve
            mc "Okay. I will go with you guys."
            david "Great! I'm happy to hear that."
            david "We're a team, so we should build up our relationship."
            liam "Let's go guys."
            jump cafeteria
        "Thanks, but... [smpi]\[Sally Route\]":
            scene atoffice8_reject with dissolve
            mc "Thanks, but I think I'm gonna eat somewhere else."
            david "...Are you sure you don't want to come with us?"
            mc "Yes. I want to look for the places around here."
            liam "Okay, if that's what you want..."
            liam "Alright, guys. We should go now."
            jump cafe
        "[smgr2]MOD: Both":
            $ modDoAllEp1_001 = True
            jump cafeteria
label cafeteria:
    scene lunch1 with dissolve
    $ renpy.pause()
    scene lunch2 with dissolve
    $ eiraatcafeteria = True
    u "Hm...?"
    scene lunch3 with dissolve
    u "[yui] is going for lunch, too."
    u "I wonder where she will go. Of course, it can't be the cafeteria."
    u "There is no way she will join us."
    scene lunch4 with dissolve
    yui "...!!"
    mc "...."
    yui "Err...."
    scene lunch5 with dissolve
    yui "To think about it again, I'm not quite hungry today..."
    yui "....Let's find something else to do."
    mc "...."
    scene cafeteria1 with fade
    u "Alright... Here we are."
    u "So, this is the company's cafeteria."
    u "Well, it looks like...."
    scene cafeteria2 with dissolve
    joe "Our company's cafeteria looks just like the ones in a high school or university, right?"
    mc "...Yeah, kinda."
    joe "Haha... Don't be too worried!"
    joe "Even though they look the same, but food here taste so much more delicious!"
    joe "Of course, it's cheaper than having lunch outside, too!"
    mc "...Okay."
    scene cafeteria3 with dissolve
    u "Umm... What do they have here...?"
    u "There are five lunch sets from set A to set E..."
    u "Well, set D looks good..."
    mc "Can I have set D, please?"
    unknown "*Speaking almost at the same time*...I'd like to have set D, please."
    u "Hm...?"
    scene cafeteria4 with dissolve
    mc "....."
    eira "....."
    s "Set D? There is only one left."
    menu:
        "Then, I'll... [eira1]":
            scene cafeteria4_giveher1 with dissolve
            mc "Give it to her. I'll have set B instead."
            eira "....."
            s "Sure. Here you are!"
            scene cafeteria4_giveher2 with dissolve
            eira "... Thank you."
            s "You're welcome!"
            $ eira_ch1_ep1 += 1
            $ eira_relationship = eira_ch1_ep1
            $ givelunchset = True
        "I said it first":
            scene cafeteria4_take1 with dissolve
            mc "I was the ones saying it first."
            eira "....."
            s "Yeah, you're right...."
            s "I'm sorry, miss. Can you choose another set?"
            scene cafeteria4_take2 with dissolve
            eira "....."
    scene cafeteria5 with dissolve
    $ renpy.pause()
    scene cafeteria6 with dissolve
    u "....."
    u "Hm?"
    scene cafeteria7 with dissolve
    mc "Why are you guys looking at me?"
    joe "Dude!"
    joe "Do you have any idea who you've just met?"
    mc "Hm? Who?"
    joe "That's [eira]!"
    mc "And?"
    joe "What did you say to her?"
    joe "We saw her staring at you while you were walking here."
    mc "I said nothing."
    scene cafeteria8 with dissolve
    leo "You must be kidding, right?"
    mc "No, I'm not."
    leo "Then, why did she look at you?"
    mc "Maybe she just looked at you guys."
    scene cafeteria9 with dissolve
    leo "No, that's impossible."
    mc "...."
    leo "Someone from her department said something like..."
    leo "'You will get her attention only when talking about work.'"
    mc "You are exaggerating."
    scene cafeteria10 with dissolve
    leo "No, I'm not!"
    leo "You don't believe me? Then, look at her."
    mc "....."
    scene cafeteria11 at eyesblink("Ch.1/Ep.1/Scenes/cafeteria11.jpg", "Ch.1/Ep.1/Scenes/cafeteria11_blink.jpg", 1) with dissolve
    leo "Do you know why she's having lunch alone?"
    leo "It's because she doesn't have any friends!"
    joe "Yeah, she is so cold that nobody dares to talk to her first."
    joe "She must be lonely. I feel bad for her."
    mc "....."
    u "I'm only seeing her back, but I can say that she doesn't look lonely at all."
    u "I understand her though."
    u "She is someone who doesn't have to have friends in her life."
    scene cafeteria12 with dissolve
    liam "Let's stop talking about her."
    liam "You better eat your food while it's hot."
    leo "You don't seem interested, [liam]."
    liam "What will I get from being interested?"
    liam "Who would want to date programmers like us?"
    liam "Of course, you're the exception because you're handsome."
    leo "Do you want me to arrange you a blind date?"
    liam "Thanks, but I don't."
    liam "I'm already so busy that I don't have time to think about women."
    scene black with dissolve
    if modDoAllEp1_001:
        jump modAllScenesEp1_001
    s "*Four hours passed*...."
    scene atoffice6 with dissolve
    u "Alright, it's time to leave work."
    jump ep1_ch1_ending

label cafe:
    scene lunch1 with dissolve
    $ renpy.pause()
    scene lunch2 with dissolve
    $ sallyatcafe = True
    u "Hm...?"
    scene lunch3 with dissolve
    u "[yui] is going for lunch, too."
    u "I wonder where she will go. Of course, it can't be the cafeteria."
    u "There is no way she will join them."
    scene lunch4 with dissolve
    yui "...!!"
    mc "...."
    yui "Err...."
    scene lunch5 with dissolve
    yui "To think about it again, I'm not quite hungry today..."
    yui "....Let's find something else to do."
    mc "...."
    label modAllScenesEp1_001:
    scene cafe1 with fade
    u "Hm? This place looks good."
    u "I think I will have lunch here for today."
    scene cafe2 with dissolve
    s "Welcome to the cafe!"
    u "It's quite smaller than looking from the outside, but it's still a good cafe."
    scene cafe3 with dissolve
    s "What'd you like to have, sir?"
    mc "I'd like to have a cup of hot coffee, and a piece of chocolate cake."
    s "A cup of hot coffee, and a piece of chocolate cake..."
    s "Anything else?"
    mc "Cookies, too."
    s "Understood. I'll bring them to your table when ready."
    scene cafe4 with dissolve
    u "Well... There is only one table available."
    scene cafe5 with dissolve
    u "To think of it..."
    u "I can foresee that people will go really crazy when the Xecon Gear is released to public."
    u "Who would have thought Virtual MMORPG could actually become true in this decade."
    u "......"
    scene cafe6 with dissolve
    u ".... I can feel someone staring at me..."
    scene cafe7 with dissolve
    mc "....."
    sally "......"
    scene cafe8 with dissolve
    u "Did I do something weird?"
    u "Why is she staring at me like that?"
    scene cafe9 with dissolve
    u "Oh... She didn't stare at me, but the cup of coffee."
    u "I think I know what her problem is now."
    u "What should I do?"
    menu:
        "Talk to her [sally1]":
            scene cafe9_invite1 with dissolve
            mc "....."
            mc "You want some?"
            scene cafe9_invite2 at eyesblink("Ch.1/Ep.1/Scenes/cafe9_invite2.jpg", "Ch.1/Ep.1/Scenes/cafe9_invite2_blink.jpg", 1) with dissolve
            sally "What did you just say?"
            mc "....Do you want to have my food?"
            sally "Really? Can I have it?"
            mc "Yes, you can."
            sally "You aren't kidding me, right?"
            mc "Do you want it or not?"
            scene cafe9_invite3 with dissolve
            sally "Yes!"
            scene cafe9_invite4 at eyesblink("Ch.1/Ep.1/Scenes/cafe9_invite4.jpg", "Ch.1/Ep.1/Scenes/cafe9_invite4_blink.jpg", 1) with dissolve
            sally "Thanks for your kindness. I'm [sally]."
            sally "Nice to meet you!"
            sally "I was so starving to death. You're my life saver!"
            u "Yeah, I know that..."
            sally "May I know your name?"
            mc "Call me [mc]."
            sally "Thanks again, [mc]!"
            scene cafe9_invite5 with dissolve
            mc "Here. You can have these cookies."
            sally "Hehe... They look so yummy!"
            scene cafe9_invite6 at eyesblink("Ch.1/Ep.1/Scenes/cafe9_invite6.jpg", "Ch.1/Ep.1/Scenes/cafe9_invite6_blink.jpg", 1) with dissolve
            sally "Awww... So good!"
            mc "What happened to you?"
            sally "I forgot my backpack at home. My wallet and phone are inside it."
            mc "I see..."
            scene cafe9_invite7 at eyesblink("Ch.1/Ep.1/Scenes/cafe9_invite7.jpg", "Ch.1/Ep.1/Scenes/cafe9_invite7_blink.jpg", 1) with dissolve
            sally "I'm so lucky that you're here. You just saved my life."
            mc "You're exaggerating..."
            sally "No, I'm not!"
            sally "I was about to clock in late, so I was in such a hurry that I didn't have time for breakfast either!"
            mc "....."
            scene cafe9_invite6 at eyesblink("Ch.1/Ep.1/Scenes/cafe9_invite6.jpg", "Ch.1/Ep.1/Scenes/cafe9_invite6_blink.jpg", 1) with dissolve
            sally "I'll buy you a meal later! Can I have your number?"
            mc "You don't have to. I just helped a little."
            sally "What are you talking about? Help is help!"
            sally "I owe you one, so I have to repay you a favor."
            mc "Okay then..."
            scene cafe9_invite7 at eyesblink("Ch.1/Ep.1/Scenes/cafe9_invite7.jpg", "Ch.1/Ep.1/Scenes/cafe9_invite7_blink.jpg", 1) with dissolve
            sally "Are you working somewhere around here?"
            mc "Yes, I'm working at Xecon company."
            scene cafe9_invite8 at eyesblink("Ch.1/Ep.1/Scenes/cafe9_invite8.jpg", "Ch.1/Ep.1/Scenes/cafe9_invite8_blink.jpg", 1) with dissolve
            sally "What a coincidence! I also work there, too!"
            mc "Really?"
            sally "Yeah! I'm a game specialist of the company!"
            u "So, she is one of... Six Angels [leo] talked about."
            scene cafe9_invite7 at eyesblink("Ch.1/Ep.1/Scenes/cafe9_invite7.jpg", "Ch.1/Ep.1/Scenes/cafe9_invite7_blink.jpg", 1) with dissolve
            sally "What about you?"
            mc "I'm a game developer. You're my senior. I've only been working there for two days."
            sally "Oh... That's why you don't look familiar."
            scene cafe9_invite9 at eyesblink("Ch.1/Ep.1/Scenes/cafe9_invite9.jpg", "Ch.1/Ep.1/Scenes/cafe9_invite9_blink.jpg", 1) with dissolve
            sally "But please don't call me senior!"
            sally "Even though I started working there before you,"
            sally "I'm just twenty years old!"
            mc "... Okay."
            scene black with dissolve
            $ renpy.pause()
            scene cafe9_invite10 with dissolve
            sally "I'll text you the date and time for meeting up next time."
            sally "Don't forget to check it out!"
            scene black with dissolve
            s "*Four hours passed*...."
            scene atoffice6 with dissolve
            u "Alright, it's time to get off work."
            $ sally_age = "20"
            $ sally_ch1_ep1 += 1
            $ sally_relationship = sally_ch1_ep1
            $ givecookies = True
            jump ep1_ch1_ending
        "Ignore her":
            scene cafe9_ignore1 with dissolve
            u "Why should I care?"
            u "I don't even know her."
            scene cafe9_ignore2 with dissolve
            sally "....."
            u "Let's finish this lunch quick and go back to the company."
            scene black with dissolve
            s "*Four hours passed*...."
            scene atoffice6 with dissolve
            u "Alright, it's time to get off work."
            jump ep1_ch1_ending


label ep1_ch1_ending:
    play music "sfx/ep1_ch1_ending.mp3" fadein 3.0
    $ bgm = "OMIIN - Long Journey"
    scene ch1_ending1 with fade
    u "Let's go back home..."
    zeke "[mc]!"
    u "[zeke]?"
    scene ch1_ending2 with dissolve
    zeke "Are you going back home?"
    mc "Yes, I am. Why?"
    zeke "[rin] and I are going for a movie. {w}Do you want to come with us?"
    scene ch1_ending3 with dissolve
    mc "...No, thanks."
    mc "I'm tired today. I want to just rest."
    zeke "It's okay. Let's go together next time!"
    mc "Yeah, next time."
    scene black with dissolve
    $ renpy.pause()
    scene ch1_ending4 with dissolve
    u "Let's take a nap, then find something to eat later."
    u "I don't know why I feel so sleepy today."
    scene ch1_ending5 with dissolve
    u "Could it be because there is still some alcohol left in my body?"
    $ renpy.sound.play("sfx/phone vibrating.mp3")
    s "*Phone vibrating*...."
    scene ch1_ending6 with dissolve
    u "...Hm?"
    u "Who's calling me at this time?"
    scene ch1_ending7 with dissolve
    u "...."
    scene ch1_ending8 with dissolve
    mc "...."
    mc "... Hello?"
    scene ch1_ending9 with fade
    mc "... Hello?"
    mc "Whom am I talking to?"
    unknown "....."
    scene ch1_ending10 with dissolve
    unknown "Hello."
    unknown "Long time no talk, [mc]."
    stop music fadeout 3.0
    $ episode = 1
    call screen ending




label MCRoom_Pic1:
    if _in_replay:
        scene McRoomPic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene MCRoom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ MCRoom_Pic1 = True
    jump House

label Mainhall_Pic1:
    if _in_replay:
        scene MainhallPic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene Mainhall
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ Mainhall_Pic1 = True
    jump House

label Livingroom_Pic1:
    if _in_replay:
        scene LivingroomPic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene Livingroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ Livingroom_Pic1 = True
    jump House

label BeforeRinRoom_Pic1:
    if _in_replay:
        scene BeforeRinRoomPic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene Before_Rinroom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ BeforeRinRoom_Pic1 = True
    jump House

label RinRoom_Pic1:
    if _in_replay:
        scene RinRoomPic1 with dissolve
        $ renpy.pause()
        $ renpy.end_replay()
    scene RinRoom
    $ renpy.sound.play("sfx/alert.wav")
    s "You've received a special image!"
    $ RinRoom_Pic1 = True
    jump House
