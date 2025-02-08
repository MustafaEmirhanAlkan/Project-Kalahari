# WickedTawernStudios. All rights are served. Coded by Crane.

#TODO Speaking charachters stay bright, other charachters shown slighty darker. +4 !!!!
#TODO Clickable portal. Az sayıda bazı yerlerde. !!!!

#TODO Map. Need map image!
#TODO Add sound effects. +4
#TODO Dialog text box style. BOX AND MEDI AVEL.
#TODO Screen changes with health in wars.
#TODO TPS TO FPS War Scenes.

#Gallery
image gallerymc = "images/mann.png"
image gallerymelina = "images/melina.png"
image gallerydiana = "images/diana.png"
image gallerycasy = "images/warrior.png"
image collectcamp = "images/camp1.jpg"
image collectcave = "images/caveinside.jpg"
image collectjungle = "images/jungle1.jpg"
image collectchurch = "images/church.jpg"
image collectarena = "images/arena.jpg"

#MainCharachter
#image mann = At('mann', sprite_highlight('mcname'))
define man = Character('Me', color = "#2640ff") #, image='mann', callback = name_callback, cb_name='mcname')
define pov = Character("[mcname]", color = "#2640ff")
default mc_armor = 0
default mc_atk = 0
default mc_hp = 0
default mc_crit = (mc_atk * 2)
default hitchance = 0 # 4 - 6 - 8 
default mc_dodge = 0
default weapon = 0
default armor = 0
#Charachters;
define casy = Character("Captain Casy", color = "#ff9100")
default casy_armor = 0
default casy_atk = 0
default casy_hp = 0
default casy_krit = 0
default casy_dodge = 0
define melina = Character("Melina", color = "#591397")
define diana = Character("Diana", color = "#ff37d4")
define bartender = Character("Bartender", color = "#6b0000")
define triss = Character("Triss", color = "#00854d")
#Enemies;
define goblin = Character("Goblin1", color= "#00ff15")
define goblin1 = Character("Goblin1", color= "#00ff15")
define goblin2 = Character("Goblin2", color= "#00ff15")
define hobgoblin = Character("Hobgoblin", color= "#005707")

screen bg_idle:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.3
        auto "bg_%s.jpg"
        action [Hide("WickedTavernStudios"), jump("end")]


        hovered Show("WickedTavernStudios", 
            displayText = "WTS PRESENTS! (Click to end)")
        unhovered Hide("WickedTavernStudios")

#Wicked Tavern Logo and Music.
image splash = "images/token.png"
label splashscreen:
    scene black
    with Pause(1)
    show splash with dissolve:
        xalign 0.5
        yalign 0.4
        zoom 2
    with Pause(3)
    show text "WICKED TAVERN PRESENTS" with dissolve:
        xalign 0.5
        yalign 0.8
        zoom 2
    with Pause(3)
    hide text with dissolve
    with Pause(1)
    hide splash with dissolve
    with Pause(1)
    return


#Game Start.
label start:
    scene church
    pause(2.0)
    show melina at left
    with moveinleft
    pause(2.0)
    melina "Hope this portal works and summons a {b}hero{/b}, sister." #Bold.
    show diana at right
    with moveinright
    diana "I hope so!"
    
    show teleport with vpunch: #vpunch = Shakes the screen.
        xalign 0.5
        yalign 0.5
    "{i}(Magical Portal Sounds){/i}" #Italic = Text type.
    "{size=+3}AA{size=+5}AA{size=+7}AA{size=+9}AAAAAAA"
    hide teleport

    scene church
    show melina at left
    show diana at right
    show mann with irisout
    #blinds
    #squares
    man "Huh? Where am I??? Who are you!!"
    man "Don't get close to me!"
    diana "You need to be relax. You're not in danger, and we are no harm to you."
    man "Wh-what. Am i in church?"
    diana "Yes. Yes you are.."
    melina "You are in (x) hero."
    man "A HERO? I'm neighter a hero, nor belong here."
    diana "No. You're belong here. That's why the portal pull you here. It choose you."
    man "Choose for what?"
    melina "Our world is dying. There are monsters, demons, foul creatures everywhere."
    man "Hahahah. Monsters? There is no such thing as a monster, or DEMON. At least in the world."
    diana "No hero. There is. There is at this time."
    man "At this time? Which year are am in rigth now."
    diana "Don't panic but we're in 316bc."
    man "Whaaaaaaaaat??? OMG. I need to wake up. I need to wak.."
    melina "Hero this is NOT a dream."
    melina "And we really need your help. Like we said ou...."
    man "(Who are theese people all i remember is i blacked out at my friends frat and now im middle of nowhere and at the different time. Isn't this a dream.)"
    diana "You accept or not. You're our savior. You can't go to your time until you finish your duty."
    diana "So PLEASE, will you help us?"
    man "Allright, i will help. But what do you want me to do about all of these. A demon? {size=+5}AND ME?" #Size = Changes Size.
    diana "Yes. You are the chosen one. But we still don't your name?"
    $ mcname = renpy.input("What is your name?", length=10)
    $ mcname = mcname.strip() #Player can use its own unique name.
    if not mcname:
        $ mcname = "Me"

    man "My name is [mcname]."
    diana "Nice to meet you [mcname]. I am Diana and sister name is Melina."
    diana "Nice to meet you [mcname]. I know it was fast and you shocked, but we need to talk the importent subjects."
    diana "You right. Actually, we need an army to defeat these threats but before that we need to inform you about all you should do. Than you can understand why YOU has been chosen."
    melina "...and also we can understand."
    
    #Combat explanation.
    scene dusty
    with fade
    "{u}(There are major, minor and rival enemies at this game. You need to defeat them with your army.{/u}" #Underline
    "{u}By doing that you will encounter new girls, both ally,neutral or enemy. You can add girls to your harem by 2 ways.{/u}"
    "{u}You can choose either defeat them in battle and enslave them or be friends with them (friendly or neutral girls)).{/u}"

    label reborn:

    scene church
    with fade
    show melina at left
    show diana at right
    show mann
    melina "Are you relaxed a little [mcname]?"
    man "I'M NOT!"
    man "But i think i have no choice. I need to turn back anyways."
    melina "We can do whatever you want after you saved us. Aren't we sis?"
    diana "Yes. Yes of course. Right now you need to go to (y) castle to meet with the captain? We can assist you to firs place that you can meet your first ally."
    diana "Please try to keep up."
    scene black
    with fade
    "Few moments later..."

    scene arena #Castle
    with fade
    show warrior at left:
        xalign 0.0
        yalign 0.5
    pause(2.0)

    show mann at right
    with moveinright
    casy "Hey soldier! What do you want??"
    show diana with moveinright:
        xalign 0.8
        yalign 1.0
    diana "Hello Casy. Do you remember me?"
    casy "Oh hi Melina."
    diana "I'm diana..."
    casy "I don't assume that this puny with you."
    diana "There's no need to try to humiliate him because he's thehero which portal chooses."
    casy "Hmmm. Really?"
    casy "Ahh nevermind. I was trying to just have some fun."
    casy "Nice to meet you kido."
    mcname "Nice to meet you, too."
    diana "Take care of him Casy."
    casy "Oookay, okay, allright."
    hide diana with moveoutright
    pause(10)
    ""
    ""
    ""
    ""
    casy "So kid? Did you eat your tongue or what?"
    mcname "Ah. Yes, sorry."
    mcname "I was looking for soldiers who are willing to fight and a general that controls them."
    mcname "Soldiers which fight for this world... or kingdom? not only against humans, maybe against demons..."
    mcname "and sister bring me to you."
    casy "You come to right place soldier. Me and my soldiers planning to attack nearby goblin camp."
    casy "Like you sad {color=#ff2626} \"Little Demons\". {/color}" #Color = Changes color of the texts.
    casy "but first you dont look like a war machine, lets turn you into one. Follow me."
    
    scene clothroom #This scene should be equipment room.
    pause(1)
    show mann at center
    with moveinright
    show warrior at right
    with moveinright
    casy "Let's change your clothes first." #Change clothes.
    man "Yes ma'am."
    scene clothroom
    show warrior at right
    
    hide man
    with moveoutleft
    pause(1)
    show warrior2:
        xalign 0.5
        yalign 0.5
    with moveinleft
    casy "Now, you look like normal. (thumbs up)"
    casy "Prepare and come find me in the area for training."
    hide casy
    with moveoutright
    mcname "Lets wear armor and find some weapons." #Pick sword, wear armor.

    menu:
        "Wear armor.":
            menu:
                "Armors(Defance) allows you to reduce some of the attacks you receive. Dodge Chances(DC) allow you to escape from attacks and receive no damage."
                "Light armor. (Def: 1, DC: 1/4)":
                    mcname "I want to move more flexible."
                    $ mc_armor = 1
                    $ mc_dodge = 4
                    $ armor = 1
                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance.)"
                    menu:    
                        "Pick weapon.":
                            menu:
                                "Weapons allows you to attack the enemys. Different weapons has different stats. Atk: Damage, Crt: Critikal Chances."
                                "Dagger: (ATK: 8, CRT: 1/4)": #1/4 Crits doubled damage.
                                    $ mc_atk = 8
                                    $ mc_crit = 4
                                    $ weapon = 1
                                    mcname "Little and sharp. (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                                    jump trainingscene
                                "Shortsword: (ATK: 10, CRT: 1/6)": #1/6
                                    $ mc_atk = 10
                                    $ mc_crit = 6
                                    $ weapon = 2
                                    mcname "Not heavy and balanced. (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                                    jump trainingscene
                                "Longsword: (ATK:12, CRT: 1/8)": #1/8
                                    $ mc_atk = 12
                                    $ mc_crit = 8
                                    $ weapon = 3
                                    mcname "STRONG! (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                                    jump trainingscene                    
                "Medium armor. (Def: 3, DC: 1/6)":
                    mcname "Balanced."
                    $ mc_armor = 3
                    $ mc_dodge = 6
                    $ armor = 2
                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance.)"
                    menu:    
                        "Pick weapon.":
                            menu:
                                "Weapons allows you to attack the enemys. Different weapons has different stats. Atk: Damage, Crt: Critikal Chances."
                                "Dagger: (ATK: 8, CRT: 1/4)": #1/4 Crits doubled damage.
                                    $ mc_atk = 8
                                    $ mc_crit = 4
                                    $ weapon = 1
                                    mcname "Little and sharp. (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                                    jump trainingscene
                                "Shortsword: (ATK: 10, CRT: 1/6)": #1/6
                                    $ mc_atk = 10
                                    $ mc_crit = 6
                                    $ weapon = 2
                                    mcname "Not heavy and balanced. (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                                    jump trainingscene
                                "Longsword: (ATK:12, CRT: 1/8)": #1/8
                                    $ mc_atk = 12
                                    $ mc_crit = 8
                                    $ weapon = 3
                                    mcname "STRONG! (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                                    jump trainingscene                    
                "Heavy armor. (Def: 5, DC: 1/8)":
                    mcname "Tank go brrrr."
                    $ mc_armor = 5
                    $ mc_dodge = 8
                    $ armor = 3
                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance.)"
                    menu:    
                        "Pick weapon.":
                            menu:
                                "Weapons allows you to attack the enemys. Different weapons has different stats. Atk: Damage, Crt: Critikal Chances."
                                "Dagger: (ATK: 8, CRT: 1/4)": #1/4 Crits doubled damage.
                                    $ mc_atk = 8
                                    $ mc_crit = 4
                                    $ weapon = 1
                                    mcname "Little and sharp. (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                                    jump trainingscene
                                "Shortsword: (ATK: 10, CRT: 1/6)": #1/6
                                    $ mc_atk = 10
                                    $ mc_crit = 6
                                    $ weapon = 2
                                    mcname "Not heavy and balanced. (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                                    jump trainingscene
                                "Longsword: (ATK:12, CRT: 1/8)": #1/8
                                    $ mc_atk = 12
                                    $ mc_crit = 8
                                    $ weapon = 3
                                    mcname "STRONG! (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                                    jump trainingscene
        "Pick weapon.":
            menu:
                "Weapons allows you to attack the enemys. Different weapons has different stats. Atk: Damage, Crt: Critikal Chances."
                "Dagger: (ATK: 8, CRT: 1/4)":
                    $ mc_atk += 8
                    $ mc_crit = 4
                    $ weapon = 1
                    mcname "Little and sharp. (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                    menu:
                        "Wear armor.":
                            menu:
                                "Armors(Defance) allows you to reduce some of the attacks you receive. Dodge Chances(DC) allow you to escape from attacks and receive no damage."
                                "Light armor. (Def: 1, DC: 1/4)":
                                    mcname "I want to move more flexible."
                                    $ mc_armor = 1
                                    $ mc_dodge = 4
                                    $ armor = 1
                                "Medium armor. (Def: 3, DC: 1/6)":
                                    mcname "Balanced."
                                    $ mc_armor = 3
                                    $ mc_dodge = 6
                                    $ armor = 2
                                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance.)"
                                "Heavy armor. (Def: 5, DC: 1/8)":
                                    mcname "Tank go brrrr."
                                    $ mc_armor = 5
                                    $ mc_dodge = 8 
                                    $ armor = 3
                                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance."
                            jump trainingscene
                "Shortsword: (ATK: 10, CRT: 1/6)":
                    $ mc_atk += 10
                    $ mc_crit = 6
                    $ weapon = 2
                    mcname "Not heavy and balanced. (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                    menu:
                        "Wear armor.":
                            menu:
                                "Armors(Defance) allows you to reduce some of the attacks you receive. Dodge Chances(DC) allow you to escape from attacks and receive no damage."
                                "Light armor. (Def: 1, DC: 1/4)":
                                    mcname "I want to move more flexible."
                                    $ mc_armor = 1
                                    $ mc_dodge = 4
                                    $ armor = 1
                                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance.)"
                                "Medium armor. (Def: 3, DC: 1/6)":
                                    mcname "Balanced."
                                    $ mc_armor = 3
                                    $ mc_dodge = 6
                                    $ armor = 2
                                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance.)"
                                "Heavy armor. (Def: 5, DC: 1/8)":
                                    mcname "Tank go brrrr."
                                    $ mc_armor = 5
                                    $ mc_dodge = 8
                                    $ armor = 3
                                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance."
                            jump trainingscene
                "Longsword: (ATK:12, CRT: 1/8)": 
                    $ mc_atk += 12
                    $ mc_crit = 8
                    $ weapon = 3
                    mcname "STRONG! (You get [mc_atk] defance and 1/[mc_crit] dodge chance.)"
                    menu:
                        "Wear armor.":
                            menu:
                                "Armors(Defance) allows you to reduce some of the attacks you receive. Dodge Chances(DC) allow you to escape from attacks and receive no damage."
                                "Light armor. (Def: 1, DC: 1/4)":
                                    mcname "I want to move more flexible."
                                    $ mc_armor = 1
                                    $ mc_dodge = 4
                                    $ armor = 1
                                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance.)"
                                "Medium armor. (Def: 3, DC: 1/6)":
                                    mcname "Balanced."
                                    $ mc_armor = 3
                                    $ mc_dodge = 6
                                    $ armor = 2
                                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance.)"
                                "Heavy armor. (Def: 5, DC: 1/8)":
                                    mcname "Tank go brrrr."
                                    $ mc_armor = 5
                                    $ mc_dodge = 8
                                    $ armor = 3
                                    mcname "That's look nice. (You get [mc_armor] defance and 1/[mc_dodge] dodge chance."
                            jump trainingscene

    #TODO Add enemy stats. and friendlys stat as Stats UI Navigation. +4
    label trainingscene:
    scene black
    with fade

    scene arena #TrainingArea
    show warrior at left:
        xalign 0.0
        yalign 0.5
    show mann at right
    casy "Grab that sword soldier and attack me."
    mcname "Okay."

    scene black 
    with fade
    show slash with vpunch: #Slash effect
        xalign 0.5
        yalign 0.5
    "Swish"

    scene arena #TrainingArea
    show warrior at left:
        xalign 0.0
        yalign 0.5
    show mann at right
    casy "Ugh..."
    casy "That was a luck shot. Lets do one more!"

    scene black
    with fade
    show slash with vpunch: #Slash effect
        xalign 0.5
        yalign 0.5
    "Swish"

    scene arena #TrainingArea
    with fade
    show warrior at left:
        xalign 0.0
        yalign 0.5
    show mann at right
    casy "Oh my goodness. Maybe that wasn't luck. You are a real talent. Where did you learn all theese skills."
    mcname "(hmm strange.. as i teleported here, i feel strange.)" 
    mcname "I was a great warrior in my world."
    casy "Hahahah. In what world?"
    mcname "Nevermind. Forget about it. I was just boasting myself, do you want to join me or not?"
    casy "Of course i want to join you. But i need few drinks first."
    casy "You know, our fight exhaust me. How about.."
    casy "we share some good drink at tavern soldier?"
    mcname "How can someone deny that.." 
    # Show mann_winks.

    scene black
    with fade
    "Few moments later..."

    scene tavern
    with fade
    show warrior at left:
        xalign 0.1
        yalign 1.0
    show mann at right
    casy "I waaanaa drink onee moooore"
    mcname "I think you shouldn't captain." 
    casy "Why nooooğt."
    casy "Gigh."
    casy "Waiğt, why you're not drinking anything huhh?"
    casy "Heğyy, bartenderr."
    show bartender: # Bartender's position near the text.
        xalign 0.0
        yalign 1.0
        zoom 0.8
    bartender "Yes ma'am"
    casy "What do you want to drink kid. It's on meğğ"
    bartender "What do you want to drink sir?"
    menu: # Choose menu.
        "Milk":
            mcname "I think i don't need any alcohol today. Can i have some milk?"
            bartender "Girl, pour [mcname] a milk."
        "Beer":
            mcname "Okay, maybe just A beer.."
            bartender "Girl, pour [mcname] a beer."
        "Wine":
            mcname "I want to try wine in this wor... i mean tavern."
            bartender "Girl, pour [mcname] a wine."
    hide bartender
    mcname "Glup"
    mcname "It's already late we need to go back to ho..."
    casy "Huh?"
    mcname "I.. actually i don't have anywehere to stay."
    casy "How about you let me drink one more, just one.., and you came to my place soldier?"
    mcname "Looks like i have no choice here."
    casy "Gooood"

    scene black
    with fade
    "Some time at the road..."

    scene room
    with fade
    show warrior at right:
        xalign 0.5
        yalign 0.9
    show mann at left
    casy "There is a small problem soldier, since i live alone i have a single bed. How about we share it?"
    mcname "(Gulp)"
    casy "Don't be shy little man. You're not the first man share bed with me." #why

    scene room at Transform(matrixcolor = TintMatrix('#3f55b8')) 
    #Changes color of the scene. (IMAGE MANIPULATORS)
    #Same room scene but night
    with fade
    casy "Are you sleeping boy. Come here. Let your captain take care of you before sleep. Like in YOUR world."

    scene room
    with fade
    show warrior at right:
        xalign 0.5
        yalign 0.9
    show mann at left
    "***THAT MORNING***"
    casy "Wake up soldier we have things to do!"
    mcname "(streches)"
    mcname "Good morning captain whats on your mind?"
    casy "We have a small army of well trained soldiers but we need a healer."
    mcname "Maybe we can find one at adventurers guild."
    casy "Odds are really low soldier because of the ongoing war, almost all healers and sorcerers called to empire's army."
    mcname "What should we do then we need a healer and maybe a sorcerer to control and destroy battlefield."
    casy "I know a decent healer but she is captured by goblins few days ago if we rescue her im sure that she will help us."
    mcname "Lets rescue her then..."
    casy "We need to prepare first soldier, you are half naked."
    mcname "(blushes and takes his clothes)"
    casy "hahahaha you are a funny one"
    mcname "Can we take down this goblins?"
    casy "We need to be careful, goblins are weak but the cave they inhabit is a massive hole that include thousands of goblins."
    mcname "How we take them down we are not that strong?"
    casy "We will infiltrate there soldier you and me."
    mcname "(gulps) You and me against a whole army of goblins?"
    casy "I know it sounds like a suicide but this is the only way."
    mcname "Okay but how we take down thousands of them?"
    casy "Listen boy goblins may be thousands but if we take down their queen they will shattered and flee without looking their backs."
    mcname "Don't tell me we need to assassinate the queen."
    casy "(smiles) that is the exact way i thought."
    mcname "You know what, i think you are a bit crazy. How we assassinate a queen covered by hundreds maybe thousands of goblins."
    casy "I said we will assassinate her not fight her. She has her own cave for resting and other things. I heard that the queen holds prisoners in that cave."
    casy "If we have some luck on our side Triss will be there."
    mcname "Sounds like a plan but how we got there without getting noticed by guards."
    casy "The next full moon is starting of a hunt season. That night almost all goblins go for hunting and raiding to nearby towns and villages. Only goblin kids, female goblins and queen's elite guards will stay."
    #(at the cave entrance)
    casy "Allright young one here is the plan, as goblins go outside we sneak in from the small entrance then we crawl into queens cave i heard that some gobbos stay and protect the queen we take them down and rescue our ally understand?"
    mcname "Allright, Now this plan make sense."
    casy "Now its time to prepare ourselves next full moon is tomorrow. Lets go to the jungle and camp close to the goblins camp."
    casy "Also you need this code: BlueRoses. With this, triss will understand. If you forgot open this latter. It's also written in this."
        #Mektup açma sahnesi gelebilir. Hem password girme hem mektuba bakabilme ve sonradan girebilme. BlueRoses.

    scene jungle1 at center:
        zoom 3
    with fade
    pause(1.0)
    show warrior:
        xalign 0.3
        yalign 0.9
    with moveinleft
    casy "Hey. Get up kid. The time has come."
    mcname "Oh sorry. I fell asleep."
    show mann:
        xalign 0.7
        yalign 1.0
    with moveinbottom
    casy "Do you remember the plan?"
    mcname "Yes."
    casy "Nice. Lets go and hide. Hurry!"
    hide mann
    with moveoutleft
    pause(1)
    hide warrior
    with moveoutleft

    scene caveentrance
    with fade
    "grass noises"
    show mann at left
    show warrior:
        xalign 0.2
        yalign 1.0
    with moveinleft
    mcname "Okay. Now we need to wait until last ones leave."
    # (few moments later at the cave)
    goblin1 "hey doo yo thingg raidz gonna be okaay ?"
    goblin2 "of course raidz will be okay you stupid no one can stond against mighty goblin army."
    goblin1 "but whot if a heero comes op an steol our mealzz."
    goblin2 "maybe yo go an kill da hero."
    goblin1 "no no, me stay"
    goblin2 "then wa ar yo sayin stoopid things."
    hobgoblin "hey you two stap whisperin or i will cut yo useless heads and sticc into a swood."

    casy "Looks like they all doesn't going out. I still can see few dozen of them. We can't get pass throuh to gate."
    casy "Okay new plan, (burns a torch), I'm gonna distruct them for u kid. Stay here and be silence."

    casy "Hey f#ckrs. Come heree."
    scene black
    with fade
    show slash at center
    with moveinleft
    "woooshh (Burning sounds)"
    goblin "WRAAAAAAA CATCH HERRRRRR AAAAAAA"
    
    scene caveentrance
    with fade
    show mann at left
    mcname "Okay. Good job Casy."
    hide mann
    with moveoutright
    

    scene caveinside
    with fade
    show mann at center
    mcname "I see lots of goblins rushing out bc of casy's distraction."
    mcname "Now i need the find that casys told me about."
    mcname "Healer i guess."
    mcname "Damn, this cave is so small"
    "Tikirt tikirt"
    mcname "Oh no. This stones."
    goblin "WRAAAAAA ISZ SOMEBODY HUH"
    mcname "Really? More goblins. Why they're still here? I think i saw 3 of them and a big one. Thats BAD!"
    mcname "This 3 stupid will be easy but hobgoblin should be the main guard of the queen he looks tough and stand just ourside of queens cave. Casy mentioned yesterday..."
    
    scene jungle1 at center:
        zoom 3
    with fade
    pause(1.0)
    show warrior:
        xalign 0.3
        yalign 0.9
    show mann:
        xalign 0.7
        yalign 1.0
    "YESTERDAY"
    mcname "Wait? A hobgoblin?? What is that?"
    casy "They're something like goblin but way biggers and strongers like 20 times."
    mcname "Don't say we gonna fight the hobgoblin."
    casy "Do you have invisibility cloak or some sort of incredible weapon to take down that big hobgoblin?"
    mcname "Ii-i don't think i have something like that."
    casy "(looks angry) then why dont you shut up."
    mcname "Sorry captain."
    casy "No need to sorry soldier just stick to me and try no to get killed okay?"
    mcname "Okay captain."
    casy "I will strike first just follow me and dont try to do fancy things."
    mcname "Okay captain lead the way, i follow."
    
    scene caveinside
    with fade
    show mann at center
    mcname "Sorry captain. I think i need to try that fancy thing for Triss. But maybe i can split them."
    "You wait until hobgoblin go away."
    mcname "It's the time."
    mcname "Hey GOBLINS!!!"

    scene caveinside #TODO Stats gonna be change.
    $ mc_maxhp = 30
    $ mc_hp = mc_maxhp
    #$ mc_atk = 10 Based on weapon.
    #$ mc_armor = 3 Based on shield
    $ mc_def = mc_armor
    
    $ goblinwarriorhp = 15 #20
    $ goblinwarrioratk = 4 
    $ hobgoblin_hp = 50
    $ hobgoblin_atk = 9
    $ hobgoblin_def = 5
    $ goblin1_hp = goblinwarriorhp
    $ goblin1_atk = goblinwarrioratk
    $ goblin2_hp = goblinwarriorhp
    $ goblin2_atk = goblinwarrioratk
    $ goblin3_hp = goblinwarriorhp
    $ goblin3_atk = goblinwarrioratk
    $ potionleft = 3
    
    screen mainstatsUI:
        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -30
            yoffset 30
            idle "images/stats_idle.png"
            action ShowMenu("StatsUI")

    screen StatsUI:
        add "images/dusty.jpg"
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 30
            ypadding 30

            hbox:
                spacing 40

                vbox:
                    spacing 10
                    text "HP" size 100
                    text "Attack" size 100
                    text "Armor" size 100
                    text "CritChance" size 100
                    text "DodgeChance" size 100
                
                vbox:
                    spacing 10
                    text "[mc_hp]" size 100
                    text "[mc_atk]" size 100
                    text "[mc_armor]" size 100
                    text "[mc_crit]" size 100
                    text "[mc_dodge]" size 100
            
        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -30
            yoffset 30
            auto "images/return_/s.png"
            action Return()
            
    "YOU ENTERED FIGHT WITH GOBLINS!!!"
    
    scene caveinside
    with fade
    "{u}(When you entered a fight, you face all the enemies at the same time. Now you're in turn based fight. You can choose some choices every turn like;) {/u}"
    "{u}(Attack: You make an attack to opponent based on your attack power, Use Potion: You gain as much health as the potion has.){/u}"
    "{u}(If you use potion, you {color=#ff2626}can't{/color} attack in that turn! Lastly, with using \"Flee\" You can escape the battle and gather your energy for return and fight again.){/u}"
    "Choose your fighter;"
    label goblinsfight:
    show goblin1 at left
    show goblin2 at center
    show goblin3 at right
    show screen mainstatsUI

    call screen choose_route

    menu:
        "Enemy: Goblin (HP=15, ATK=4) X 3"  
        "{color=#ff2626}WARNING! {/color} Captain Casy is in another fight! Can't be useable."
        "YOU: [mcname] (HP=[mc_hp], ATK=[mc_atk], DEF=[mc_def])":

            scene black
                ## show the stats button from screen gameUI (custom_screens.rpy)
            show screen gameUI
            jump show_choices


    label show_choices:
        menu:
            "[mcname] Stats"    
            "Show [mcname]'s attack.":
                "[mc_atk]"
            "Show [mcname]'s defance.":
                "[mc_armor]"
            "Show [mcname]'s health.":
                "[mc_hp]"
            "Show [mcname]'s critical chance.":
                "[mc_crit]"   
            "Show [mcname]'s dodge chance.":
                "[mc_dodge]"                         
            "Return":
                jump goblingsfight
            "Cas'ys Stats"    
        menu:
            "Show Casy's attack.":
                "[casy_atk]"
            "Show Casy's defance.":
                "[casy_armor]"
            "Show Casy's health.":
                "[casy_hp]"
            "Show Casy's critical chance.":
                "[casy_crit]"   
            "Show Casy's dodge chance.":
                "[casy_dodge]" 
            "Return":
                jump goblingsfight
        jump show_choices
    


        jump fight_myself
        #TODO Add enemy stats. and friendlys stat as Stats UI Navigation. +4
    hide screen mainstatsUI
    label fight_myself:
    while mc_hp > 0: # Mc stats will be shown at left corner.
        menu:
            "Attack":
                if goblin1_hp > 0:
                    if weapon == 1:
                        $ hitchance = renpy.random.randint(0, 24)
                        if hitchance > 3:
                            $ goblin1_hp = goblin1_hp - mc_atk
                            "Hit for [mc_atk] damage! First Goblin has [goblin1_hp] hp now!"
                            jump goblin1turn
                        else:
                            $ goblin1_hp -= (mc_atk*2)
                            "CRIT HITT! [mc_atk] x 2"
                            jump goblin1turn
                    elif weapon == 2:
                        $ hitchance = renpy.random.randint(0, 24)
                        if hitchance > 4:
                            $ goblin1_hp = goblin1_hp - mc_atk
                            "Hit for [mc_atk] damage! First Goblin has [goblin1_hp] hp now!"
                            jump goblin1turn
                        else:
                            $ goblin1_hp -= (mc_atk*2)
                            "CRIT HITT! [mc_atk] x 2"
                            jump goblin1turn
                    elif weapon == 3:
                        $ hitchance = renpy.random.randint(0, 24)
                        if hitchance > 6:
                            $ goblin1_hp = goblin1_hp - mc_atk
                            "Hit for [mc_atk] damage! First Goblin has [goblin1_hp] hp now!"
                            jump goblin1turn
                        else:
                            $ goblin1_hp -= (mc_atk*2)
                            "CRIT HITT! [mc_atk] x 2"
                            jump goblin1turn
                            label goblin1turn:
                            if goblin1_hp > 0: #TODO Goblins hps changes simultaneously.    
                                mcname "Okay!"
                                $ mc_hp -= (goblin1_atk - mc_def) #TODO Every position shown as different images like attacking and standing. Discriptions should be better.
                                $ mc_hp -= (goblin2_atk - mc_def)
                                $ mc_hp -= (goblin3_atk - mc_def)
                                "First Goblin attacked = [goblin1_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                                "Second Goblin attacked = [goblin2_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                                "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                                if mc_hp > mc_maxhp:
                                    $ mc_hp = mc_maxhp
                                    "Your HP not reduced and is [mc_hp]."
                                else:
                                    "Your HP is reduced to [mc_hp]."
                            else:
                                "You killed the first one!"
                                $ mc_hp -= (goblin2_atk - mc_def)
                                $ mc_hp -= (goblin3_atk - mc_def)
                                "First Goblin Died"
                                "Second Goblin attacked = [goblin2_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                                "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                                if mc_hp > mc_maxhp:
                                    $ mc_hp = mc_maxhp
                                    "Your HP not reduced and is [mc_hp]."
                                else:
                                    "Your HP is reduced to [mc_hp]."
                elif goblin2_hp > 0:
                    if weapon == 1:
                        $ hitchance = renpy.random.randint(0, 24)
                        if hitchance > 3:
                            $ goblin2_hp = goblin2_hp - mc_atk
                            "Hit for [mc_atk] damage! First Goblin has [goblin2_hp] hp now!"
                            jump goblin2turn
                        else:
                            $ goblin2_hp -= (mc_atk*2)
                            "CRIT HITT! [mc_atk] x 2"
                            jump goblin2turn
                    elif weapon == 2:
                        $ hitchance = renpy.random.randint(0, 24)
                        if hitchance > 4:
                            $ goblin2_hp = goblin2_hp - mc_atk
                            "Hit for [mc_atk] damage! First Goblin has [goblin2_hp] hp now!"
                            jump goblin2turn
                        else:
                            $ goblin2_hp -= (mc_atk*2)
                            "CRIT HITT! [mc_atk] x 2"
                            jump goblin2turn
                    elif weapon == 3:
                        $ hitchance = renpy.random.randint(0, 24)
                        if hitchance > 6:
                            $ goblin2_hp = goblin2_hp - mc_atk
                            "Hit for [mc_atk] damage! First Goblin has [goblin2_hp] hp now!"
                            jump goblin2turn
                        else:
                            $ goblin2_hp -= (mc_atk*2)
                            "CRIT HITT! [mc_atk] x 2"
                            jump goblin2turn
                            label goblin2turn:
                            if goblin2_hp > 0:
                                mcname "What about now?"
                                $ mc_hp -= (goblin2_atk - mc_def)
                                $ mc_hp -= (goblin3_atk - mc_def)
                                "First Goblin Died"
                                "Second Goblin attacked = [goblin2_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                                "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                                if mc_hp > mc_maxhp:
                                    $ mc_hp = mc_maxhp
                                    "Your HP not reduced and is [mc_hp]."
                                else:
                                    "Your HP is reduced to [mc_hp]."
                            else:
                                "You killed the second one!"
                                $ mc_hp -= (goblin3_atk - mc_def)
                                "First Goblin Died"
                                "Second Goblin Died"
                                "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                                if mc_hp > mc_maxhp:
                                    $ mc_hp = mc_maxhp
                                    "Your HP not reduced and is [mc_hp]."
                                else:
                                    "Your HP is reduced to [mc_hp]."
                elif goblin3_hp > 0:
                    if weapon == 1:
                        $ hitchance = renpy.random.randint(0, 24)
                        if hitchance > 3:
                            $ goblin3_hp = goblin3_hp - mc_atk
                            "Hit for [mc_atk] damage! First Goblin has [goblin3_hp] hp now!"
                            jump goblin3turn
                        else:
                            $ goblin3_hp -= (mc_atk*2)
                            "CRIT HITT! [mc_atk] x 2"
                            jump goblin3turn
                    elif weapon == 2:
                        $ hitchance = renpy.random.randint(0, 24)
                        if hitchance > 4:
                            $ goblin3_hp = goblin3_hp - mc_atk
                            "Hit for [mc_atk] damage! First Goblin has [goblin3_hp] hp now!"
                            jump goblin3turn
                        else:
                            $ goblin1_hp -= (mc_atk*2)
                            "CRIT HITT! [mc_atk] x 2"
                            jump goblin3turn
                    elif weapon == 3:
                        $ hitchance = renpy.random.randint(0, 24)
                        if hitchance > 6:
                            $ goblin3_hp = goblin3_hp - mc_atk
                            "Hit for [mc_atk] damage! First Goblin has [goblin3_hp] hp now!"
                            jump goblin3turn
                        else:
                            $ goblin3_hp -= (mc_atk*2)
                            "CRIT HITT! [mc_atk] x 2"
                            jump goblin3turn
                            label goblin3turn:
                            if goblin3_hp > 0:
                                mcname "What about now?"
                                $ mc_hp -= (goblin3_atk - mc_def)
                                "First Goblin Died"
                                "Second Goblin Died"
                                "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                                if mc_hp > mc_maxhp:
                                    $ mc_hp = mc_maxhp
                                    "Your HP not reduced and is [mc_hp]."
                                else:
                                    "Your HP is reduced to [mc_hp]."
                            else:
                                "You killed the third one!"  
                                jump hobgoblinfight
                else:
                    jump hobgoblinfight
            "Use Potion (for 15 HP) You have [potionleft] potion/s!":
                if potionleft > 0:
                    $ potionleft -= 1
                    "It's better.."
                    if (mc_hp + 15) > 30:
                        $ mc_maxhp = 30
                        $ mc_hp = mc_maxhp
                        "You're using potion for 15 hp!"
                        "Your HP is increased to [mc_hp]."
                        if goblin1_hp > 0:
                            $ mc_hp -= (goblin1_atk - mc_def)
                            $ mc_hp -= (goblin2_atk - mc_def)
                            $ mc_hp -= (goblin3_atk - mc_def)
                            "First Goblin attacked = [goblin1_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            "Second Goblin attacked = [goblin2_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            if mc_hp > mc_maxhp:
                                $ mc_hp = mc_maxhp
                                "Your HP not reduced and is [mc_hp]."
                            else:
                                "Your HP is reduced to [mc_hp]."
                        elif goblin2_hp > 0:
                            $ mc_hp -= (goblin2_atk - mc_def)
                            $ mc_hp -= (goblin3_atk - mc_def)
                            "First Goblin Died"
                            "Second Goblin attacked = [goblin2_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            if mc_hp > mc_maxhp:
                                $ mc_hp = mc_maxhp
                                "Your HP not reduced and is [mc_hp]."
                            else:
                                "Your HP is reduced to [mc_hp]."
                        elif goblin3_hp > 0:
                            $ mc_hp -= (goblin3_atk - mc_def)
                            "First Goblin Died"
                            "Second Goblin Died"
                            "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            if mc_hp > mc_maxhp:
                                $ mc_hp = mc_maxhp
                                "Your HP not reduced and is [mc_hp]."
                            else:
                                "Your HP is reduced to [mc_hp]."
                        else:
                            jump hobgoblinfight
                    else:
                        $ mc_hp += 15
                        "You're using potion for 15 hp!"
                        "Your HP is increased to [mc_hp]."
                        if goblin1_hp > 0:
                            $ mc_hp -= (goblin1_atk - mc_def)
                            $ mc_hp -= (goblin2_atk - mc_def)
                            $ mc_hp -= (goblin3_atk - mc_def)
                            "First Goblin attacked = [goblin1_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            "Second Goblin attacked = [goblin2_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            if mc_hp > mc_maxhp:
                                $ mc_hp = mc_maxhp
                                "Your HP not reduced and is [mc_hp]."
                            else:
                                "Your HP is reduced to [mc_hp]."
                        elif goblin2_hp > 0:
                            $ mc_hp -= (goblin2_atk - mc_def)
                            $ mc_hp -= (goblin3_atk - mc_def)
                            "First Goblin Died"
                            "Second Goblin attacked = [goblin2_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            if mc_hp > mc_maxhp:
                                $ mc_hp = mc_maxhp
                                "Your HP not reduced and is [mc_hp]."
                            else:
                                "Your HP is reduced to [mc_hp]."
                        elif goblin3_hp > 0:
                            $ mc_hp -= (goblin3_atk - mc_def)
                            "First Goblin Died"
                            "Second Goblin Died"
                            "Third Goblin attacked = [goblin3_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                            if mc_hp > mc_maxhp:
                                $ mc_hp = mc_maxhp
                                "Your HP not reduced and is [mc_hp]."
                            else:
                                "Your HP is reduced to [mc_hp]."
                        else:
                            jump hobgoblinfight
                else:
                    "You don't have any potions. You couldn't heal yourself."
                    jump fight_myself
            "Flee!":
                jump continue_flee
    "You died..."   

    label hobgoblinfight:
    hide goblin1
    with moveoutleft
    hide goblin2
    with moveoutleft
    hide goblin3
    with moveoutleft
    show hobgoblin at center:
        zoom 3
    hobgoblin "WRAAAAAAAA HOW DARE YOUU!!"
    hobgoblin "COME HERE PUNY THING"
    "YOU ENTERED FIGHT WITH HOBGOBLIN!!!"
    "Choose your fighter;"
    menu:
        "Enemy: Hobgoblin (HP=50, ATK=7)"
        "{color=#ff2626}WARNING! {/color} Characters who exit the battle can continue with their remaining health."
        "YOU: [mcname] (HP=[mc_hp], ATK=[mc_atk], DEF=[mc_def])":
            jump fight_myselff
        #TODO Add enemy stats. and friendlys stat as Stats UI Navigation. +4
    label fight_myselff:
    while mc_hp > 0:
        menu:
            "Attack":
                if weapon == 1:
                    $ hitchance = renpy.random.randint(0, 24)
                    if hitchance > 3:
                        $ hobgoblin_hp -= (mc_atk-hobgoblin_def)
                        "Hit! Hobgoblin has [hobgoblin_hp] hp! It's armor ignored [hobgoblin_def] DMG"
                        mcname "Yes!"
                        if hobgoblin_hp <= 0:
                            "You win this Battle! Congrats."
                            jump choices1
                        else:
                            jump hobgoblinattack
                    else:
                        $ hobgoblin_hp -= (mc_atk*2)-hobgoblin_def
                        "CRIT HITT! [mc_atk] x 2"
                        "Hit! Hobgoblin has [hobgoblin_hp] hp! It's armor ignored [hobgoblin_def] DMG"
                        mcname "Yes!"
                        if hobgoblin_hp <= 0:
                            "You win this Battle! Congrats."
                            jump choices1
                        else:
                            jump hobgoblinattack
                elif weapon == 2:
                    $ hitchance = renpy.random.randint(0, 24)
                    if hitchance > 4:
                        $ hobgoblin_hp -= (mc_atk-hobgoblin_def)
                        "Hit! Hobgoblin has [hobgoblin_hp] hp! It's armor ignored [hobgoblin_def] DMG"
                        mcname "Yes!"
                        if hobgoblin_hp <= 0:
                            "You win this Battle! Congrats."
                            jump choices1
                        else:
                            jump hobgoblinattack
                    else:
                        $ hobgoblin_hp -= (mc_atk*2)-hobgoblin_def
                        "CRIT HITT!"
                        "Hit! Hobgoblin has [hobgoblin_hp] hp! It's armor ignored [hobgoblin_def] DMG"
                        mcname "Yes!"
                        if hobgoblin_hp <= 0:
                            "You win this Battle! Congrats."
                            jump choices1
                        else:
                            jump hobgoblinattack
                elif weapon == 3:
                    $ hitchance = renpy.random.randint(0, 24)
                    if hitchance > 6:
                        $ hobgoblin_hp -= (mc_atk-hobgoblin_def)
                        "Hit! Hobgoblin has [hobgoblin_hp] hp! It's armor ignored [hobgoblin_def] DMG"
                        mcname "Yes!"
                        if hobgoblin_hp <= 0:
                            "You win this Battle! Congrats."
                            jump choices1
                        else:
                            jump hobgoblinattack
                    else:
                        $ hobgoblin_hp -= (mc_atk*2)-hobgoblin_def
                        "CRIT HITT!"
                        "Hit! Hobgoblin has [hobgoblin_hp] hp! It's armor ignored [hobgoblin_def] DMG"
                        mcname "Yes!"
                        if hobgoblin_hp <= 0:
                            "You win this Battle! Congrats."
                            jump choices1
                        else:
                            jump hobgoblinattack
            "Use Potion (for 15 HP) You have [potionleft] potion/s!":
                if potionleft > 0:
                    $ potionleft -= 1
                    "It's better.."
                    if 15 <= mc_hp < mc_maxhp:
                        $ mc_hp = 30
                        "You have [mc_hp] hp."
                    elif 0 < mc_hp < 20:
                        $ mc_hp += 15
                        "You have [mc_hp] hp."
                    else: 
                        $ mc_hp = 30
                        "You have [mc_hp] hp."
                else:
                    "You don't have any potions. You couldn't heal yourself."
                    jump fight_myselff        
            "Flee!":
                jump continue_flee

        label hobgoblinattack:
        if armor == 1: 
            $ mc_dodge = renpy.random.randint(0, 24)
            if mc_dodge > 6:
                $ mc_hp -= (hobgoblin_atk-mc_armor)
                "Hobgoblin attacked = [hobgoblin_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                "Your HP is reduced to [mc_hp]."
                jump fight_myselff
            else:
                "You dodge the attack. Your HP is not reduced and is [mc_hp]."
                jump fight_myselff
        elif armor == 2: 
            $ mc_dodge = renpy.random.randint(0, 24)
            if mc_dodge > 4:
                $ mc_hp -= (hobgoblin_atk-mc_armor)
                "Hobgoblin attacked = [hobgoblin_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                "Your HP is reduced to [mc_hp]."
                jump fight_myselff
            else:
                "You dodge the attack. Your HP is not reduced and is [mc_hp]."
                jump fight_myselff
        elif armor == 3: 
            $ mc_dodge = renpy.random.randint(0, 24)
            if mc_dodge > 3:
                $ mc_hp -= (hobgoblin_atk-mc_armor)
                "Hobgoblin attacked = [hobgoblin_atk] DMG dealt. Armor reduced [mc_armor] DMG."
                "Your HP is reduced to [mc_hp]."
                jump fight_myselff
            else:
                "You dodge the attack. Your HP is not reduced and is [mc_hp]."
                jump fight_myselff
            $ renpy.block_rollback()
    "You died..."
    jump reborn 
    
    $ renpy.block_rollback()
    #After battle scene. 
    label choices1:
        "Do you want to recruit her or kill her?"
    menu:
        "RECRUIT.":
            jump recruit_1
        "KILL!!!":
            jump kill_1
    label recruit_1:
        mcname "I'm not gonna kill you unless you work for me after this time!"
        jump choices1_common
    label kill_1:
        mcname "I don't need someone like you. You magot!"
        mcname "DIE!!!"
        mcname "What a shame."
        jump choices1_common

    $ renpy.block_rollback()
    label choices1_common:
        show melina at left
        melina "You fought well [mcname]."
        jump fightend

    label continue_flee:
        "Oh that was close. Lets get out of here!!"
        #$ mc_hp = mc_maxhp
        "I need to rest and go back again!"
        if 20 <= mc_hp < mc_maxhp:
            $ mc_hp = 30
        elif 0 < mc_hp < 20:
            $ mc_hp += 10
            "You have [mc_hp] hp."
        else: 
            $ mc_hp = 30
            "You have [mc_hp] hp."
        "Your hp increased 10 while resting."
        if goblin3_hp > 0:
            "Let's go and kill this goblins this time!"
            jump goblinsfight
        else:
            "Let's go and kill this hobgoblins this time!"
            jump hobgoblinfight 

    label fightend:
    scene caveinside
    with fade
    show mann at right
    with moveinright
    mcname "I think nobody left here. I need to find that girl who Casy told me about."
    mcname "Hope Casy is okay too. She distruckted them all but can she escape?"
    mcname "Nevermind, lets get back to work."
    triss "Barely hearable slow breathing voice..."
    mcname "Somebody is toward me."
    mcname "F*ck, its so dark here."
    mcname "Psst. Anybody there?"
    triss "OHöhöh"
    show triss at left
    with moveinleft
    mcname "Hey, I find you. Don't worry. I'm here. I came to save you."
    triss "Noo pleasee (Crys)"
    mcname "Hey don't worry. Casy send me. You're okay now."
    mcname "I'm gonna help you. Let me lock those chains. Okay?"
    triss "I don't trust you. If you'Re really with Casy. She told you about something. If you coorect it, i will come with you."
    
    scene caveinside
    call screen input_pw_button
    return 
    label get_password:
        default letter = "Letter"
        show screen letterUI
        "(If you forget the code, you can check the latter which Casy's give you!)"
        $ password = "BlueRoses"
        $ password_input = renpy.input("What's the password?", length = 9)
        if password_input == password:
            hide screen letterUI
            jump correct_password
        else:
            jump wrong_password
        return

    label correct_password:
        "The password is correct and is [password]."
        jump crane
        return

    label wrong_password:
        "Your input is wrong. Please try again."
        call screen input_pw_button
        return

    screen input_pw_button:
        textbutton "Click here to input the password.":
            align (0.5,0.5)
            text_color "#c8ff00"
            action [Jump("get_password"), Return()]
    
    label letterUI:


    label crane:
    scene caveinside
    with fade
    show mann at right
    show triss at left
    triss "O-Okay"
    "Clinks"
    mcname "We're good now. Casy distructing them. We don't have much time."
    triss "Wait! You also look doesn't well. Let me help you too."
    #While healing, screen turns bright.
    mcname "Thank you. That feels so good."
    triss "We can go."
    #Reverse of the entering scenes.
    "Few moments later."

    scene camp1
    with fade
    show triss at right
    show mann at left
    triss "Öhöhö"
    mcname "Ah sorry, i forget you need to rest too. I think we're far enoufh. Let's check your wounds."
    triss "I can heal myself but it takes more time than healing others. I'll be fine."
    mcname "Okay then, let me know if you need anything."
    triss "I need to rest, also it's very dark right now. Can we camp here until morning."
    mcname "Yes, yes of course. Just we did't talk like this with Casy. Hope she's okay. If everything goes well, she will be on the road to castle right now. She'll be waiting us."
    triss "Don't worry. She'll be understand. Just, she's gonna be more aggressive. I can talk to her."
    mcname "Okat, thanks."
    mcname "Thann, I'm going to prepare the camp."
    menu:
        "Light a campfire.":
            mcname "I need some stone, wood and dry leaf."
            jump campfire
        "Hunt for food!":
            mcname "I'm gonna chech around for some food. I'll be right back in 10 min."
            jump camphunt
    label campfire:
        #Show fire.
        menu:
            "Hunt for food!":
                mcname "I'm gonna chech around for some food. I'll be right back in 10 min."
                jump campready
    label camphunt:
        #Show meats
        menu:
            "Light a campfire.":
                mcname "I need some stone, wood and dry leaf."
                jump campready
    
    label campready:
    scene camp1 #Campfire and hunting completed scene
    with fade
    show mann at left
    show triss at right
    mcname "Everything is ready for the dinner. Do you want to join? Are you feeling good?"
    triss "Yes, I'm better now."
    mcname "There's some food, we can eat."
    mcname "Do you want to tell what happened."
    triss "It's more proper if i explain when we're with Casy."
    mcname "Oh-Okay, if you perefer so."
    triss "Thank you for understanding..."
    triss "Instead of, why don't you tell me about yourself my hero."
    mcname "Okayy, why not?"
    # Hero explains story. Triss asks some questions. After true answers, triss returning with a gift to her savior.
    default triss_trueanswers = 0
    label trissquestions:
        triss "What's your favorite body type?"
        menu:
            "Lean":
                $ triss_trueanswers += 1
                mcname "Probably skinny girls."
            "Muscular":
                mcname "I loce strong womans."
            "Chubby":
                mcname "I prefer chubby's."
        triss "What's your favorite hair?"
        menu:
            "Long":
                mcname "I like long hair in girls."
            "Short":
                $ triss_trueanswers += 1
                mcname "I like short hair in womans."
            "Bald":
                mcname "I prefer no hair."
        triss "Oh really, so which type?"
        menu:
            "Wavy.":
                mcname "Wavy hairs are so fascinating."
            "Curly.":
                mcname "Curlys are splendid."
            "Straight.":
                $ triss_trueanswers += 1
                mcname "Everything is beautiful when it's straight."
    label ending_evaluation:
        if triss_trueanswers > 1:
            jump trissgoodending
        else:
            jump trissbadending    
    
    label trissgoodending:
    mcname "It's so late. You can sleep, I'm gonna be lookout."
    triss "Uhh [mcname], a-ac"
    mcname "Yes?"
    triss "Actually I want to give you a present for saving me."
    mcname "Oh, you don't nee-"
    # Their relationship increases.

    label trissbadending:
    triss "It's getting so late. Goodnight."
    mcname "Goodnight..."

#When the morning comes, triss and mc turns a castle and they talk with casy.
return