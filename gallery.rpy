init python:
    gallery = Gallery()
    gallery.transition = fade

    gallery.button("test_gallery")
    gallery.image("gallerymc")
    gallery.unlock_image("gallerymelina")
    gallery.unlock_image("gallerydiana")
    gallery.unlock_image("gallerycasy")
    gallery.button("test_collectables")
    gallery.unlock_image("collectcamp")
    gallery.unlock_image("collectcave")
    gallery.unlock_image("collectjungle")
    gallery.unlock_image("collectchurch")
    gallery.unlock_image("collectarena")

screen gallery():
    tag menu
    add "images/dusty.jpg"
    frame:
        xalign 0.5
        yalign 1.0
        default page = 1
        hbox:
            textbutton "Gallery" action SetScreenVariable("page",1)
            textbutton "Collectables" action SetScreenVariable("page",2)
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        if page == 1:
            text "You are on Gallery."
            grid 1 1:
                spacing 10
                vbox:
                    add gallery.make_button(name = "test_gallery", locked = "images/locked.jpg", unlocked = "images/mann.png")
                    text gallery.get_fraction(name="test_gallery", format = u'{seen}/{total}')
        elif page == 2:
            text "You are on Collactables."
            grid 1 1:
                spacing 10
                vbox:
                    add gallery.make_button(name = "test_collectables", locked = "images/locked.jpg", unlocked = "images/arena.jpg")
                    text gallery.get_fraction(name="test_collectables", format = u'{seen}/{total}')
        else:
            text "You have no item in gallery! Please continue playing to unlock images."
            
    frame:
        xalign 0.0
        yalign 1.0
        xpadding 10
        ypadding 10
        textbutton "Return" action Return()






        
'''
init python:
    collectables = Collectables()
    collectables.transition = fade
    
    collectables.button("test_collactables")
    collectables.image("collectablearena")
    collectables.unlock_image("collectablecamp")
    collectables.unlock_image("collectablecave")
    collectables.unlock_image("collectablejungle")
    collectables.unlock_image("collectablechurch")
    collectables.unlock_image("collectablemc")

screen collectables():
    tag menu
    add "images/dusty.jpg"
    frame:
        xalign 0.5
        yalign 1.0
        default page = 1
        hbox:
            textbutton "Gallery" action SetScreenVariable("page",1)
            textbutton "Collectables" action SetScreenVariable("page",2)
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        if page == 1:
            text "You are on Gallery."
            grid 2 2:
                spacing 10
                vbox:
                    add gallery.make_button(name = "test_gallery", locked = "images/locked.jpg", unlocked = "images/man.jpg")
                    text gallery.get_fraction(name="test_gallery", format = u'{seen}/{total}')
        elif page == 2:
            text "You are on Collactables."
            grid 1 1:
                spacing 10
                vbox:
                    add gallery.make_button(name = "test_collectables", locked = "images/locked.jpg", unlocked = "images/arena.jpg")
                    text gallery.get_fraction(name="test_collectables", format = u'{seen}/{total}')
        else:
            text "You have no item in collectables! Please continue playing to unlock images."

    frame:
        xalign 0.0
        yalign 1.0
        xpadding 10
        ypadding 10
        textbutton "Return" action Return()
'''