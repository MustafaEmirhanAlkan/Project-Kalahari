screen letterUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "images/letter.png"
        action ShowMenu("Letter")

screen Letter:
    add "images/bg dusty.jpg"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "BlueRoses" size 100
            
            vbox:
                spacing 10
                text "[blueRoses]" size 100
        
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "images/letter.png"
        action Return()