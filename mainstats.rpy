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