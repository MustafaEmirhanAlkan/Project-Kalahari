screen choose_route:
    add "images/opening.png"
    # This button will delete any persistent variable
    button:
        text "Clear Persistence": 
            idle_color "#fff"
            hover_color "#c0c0c0"
        action Function(renpy.game.persistent._clear)

    # horizontal box containing the 5 image buttons
    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 30  
        spacing 20

        imagebutton:
            auto "choices/blue_%s.png"
            action Jump("fight_myself")
        imagebutton:
            auto "choices/red_%s.png"
            action Jump("red_start")
            sensitive persistent.blue == False
        imagebutton:
            auto "choices/yellow_%s.png"
            action Jump("yellow_start")
            sensitive persistent.blue == True and persistent.red == True
        imagebutton:
            auto "choices/silver_%s.png"
            action Jump("silver_start")
            # The imagebutton will be enabled if blue, red and yellow are true and disabled when at least one is false.
            sensitive persistent.blue == True and persistent.red == True and persistent.yellow == True  
        imagebutton:
            auto "choices/gold_%s.png"
            action Jump("gold_start")
            # The imagebutton will be enabled if blue, red, yellow and silver are true and disabled when at least one is false.
            sensitive persistent.blue == True and persistent.red == True and persistent.yellow == True and persistent.silver == True 


    text "Enemy: Goblin (HP=15, ATK=4) X 3":
        xpos 640
        ypos 140
    text "{color=#ff2626}WARNING! {/color} Captain Casy is in another fight! Can't be useable.":
        xpos 440
        ypos 800
    text "YOU: [mcname] (HP=[mc_hp], ATK=[mc_atk], DEF=[mc_def])":
        xpos 20
        ypos 350
