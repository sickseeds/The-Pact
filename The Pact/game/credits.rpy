transform credits_scroll:
    yoffset 1200
    linear 25.0 ypos -4000

screen credits():

    add Solid("#000")
    
    timer 25.0 action Return()

    frame:
        background None
        xalign 0.5
        at credits_scroll

        vbox:
            spacing 40
            xalign 0.5

            text "{size=80}{b}CREDITS{/b}{/size}" xalign 0.5

            null height 100

            text "{size=50}{b}Creators{/b}{/size}" xalign 0.5
            text "Dove & Eta" xalign 0.5

            null height 80

            text "{size=50}{b}Writing{/b}{/size}" xalign 0.5
            text "Dove & Eta" xalign 0.5

            null height 80

            text "{size=50}{b}Programming{/b}{/size}" xalign 0.5
            text "Dove" xalign 0.5

            null height 80

            text "{size=50}{b}Character Art{/b}{/size}" xalign 0.5
            text "Dove & Eta" xalign 0.5

            null height 80

            text "{size=50}{b}Background Art{/b}{/size}" xalign 0.5
            text "Pixabay, edited using SAI2 and CSP" xalign 0.5

            null height 80

            text "{size=50}{b}Music{/b}{/size}" xalign 0.5
            text "Pixabay" xalign 0.5
            text "Arthur Vyncke" xalign 0.5

            null height 80

            text "{size=50}{b}Sound Effects{/b}{/size}" xalign 0.5
            text "Pixabay" xalign 0.5

            null height 120

            text "{size=55}{b}Special Thanks{/b}{/size}" xalign 0.5
            text "My friends, testers, and supporters." xalign 0.5
            text "This was my first ever VN, and I joined late, so I crammed it into a week LOL, hope you enjoyed it!" xalign 0.5

            null height 150

            text "{size=70}{b}Made for{/b}{/size}" xalign 0.5
            text "{size=55}Toxic Yuri VN Game Jam 2{/size}" xalign 0.5

            null height 200

            text "{size=80}Thank you for playing.{/size}" xalign 0.5

            null height 100

            text "{size=40}The End?{/size}" xalign 0.5