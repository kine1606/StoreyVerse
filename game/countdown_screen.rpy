# Countdown Timer Screen

screen countdown_timer(start_time):
    zorder 100
    
    default time_left = start_time
    
    # Timer that counts down every second
    timer 1.0 repeat True action SetScreenVariable("time_left", max(0, time_left - 1))
    
    # Timer display at the top center
    frame:
        xalign 0.5
        yalign 0.05
        background "#000000cc"
        padding (20, 10)
        
        hbox:
            spacing 10
            
            # Clock icon (optional decoration)
            text "⏱" size 40 color "#ffffff"
            
            # The actual countdown display
            text "[time_left]s" size 40:
                if time_left > 30:
                    color "#00ff00"  # Green when > 30 seconds
                elif time_left > 10:
                    color "#ffff00"  # Yellow when > 10 seconds
                else:
                    color "#ff0000"  # Red when <= 10 seconds

# Alternative animated countdown timer with better visuals
screen countdown_timer_fancy(start_time):
    zorder 100
    
    default time_left = start_time
    
    timer 1.0 repeat True action SetScreenVariable("time_left", max(0, time_left - 1))
    
    # Background bar
    frame:
        xalign 0.5
        yalign 0.05
        xsize 400
        ysize 80
        background Solid("#000000dd")
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            
            # Timer text
            text "{size=45}{b}[time_left]{/b}{/size}" xalign 0.5:
                if time_left > 30:
                    color "#00ff00"
                elif time_left > 10:
                    color "#ffaa00"
                else:
                    color "#ff0000"
            
            # Progress bar
            bar:
                value time_left
                range start_time
                xsize 360
                ysize 15
                xalign 0.5
                
                if time_left > 30:
                    left_bar Solid("#00ff00")
                elif time_left > 10:
                    left_bar Solid("#ffaa00")
                else:
                    left_bar Solid("#ff0000")
                    
                right_bar Solid("#333333")
