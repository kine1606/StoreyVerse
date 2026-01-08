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

# Timed choice screen for scene 3 - Chemistry Room
screen timed_choice_scene3(timeout_seconds):
    zorder 100
    modal True
    
    default time_left = timeout_seconds
    
    # Countdown timer - when reaches 0, set result to None and return
    timer 1.0 repeat True action If(
        time_left > 1,
        SetScreenVariable("time_left", time_left - 1),
        [SetVariable("_timed_choice_result", None), Return()]
    )
    
    # Timer display at top
    frame:
        xalign 0.5
        yalign 0.05
        background "#000000cc"
        padding (20, 10)
        
        hbox:
            spacing 10
            text "⏱" size 40 color "#ffffff"
            text "[time_left]s" size 40:
                if time_left > 5:
                    color "#ffff00"
                else:
                    color "#ff0000"
    
    # Choice buttons in center
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 15
        
        textbutton "{color=#888888}\"Không! Tớ không thể ép ai cả! Tìm cách khác đi!\"{/color}":
            action [SetVariable("_timed_choice_result", "hesitate"), Return()]
            xalign 0.5
            
        textbutton "{color=#ff8866}Chỉ định Tuấn làm{/color}":
            action [SetVariable("_timed_choice_result", "tuan"), Return()]
            xalign 0.5
            
        textbutton "{color=#ff8866}Chỉ định Lan làm{/color}":
            action [SetVariable("_timed_choice_result", "lan"), Return()]
            xalign 0.5
            
        textbutton "{color=#66ff66}\"Để tớ làm.\"{/color}":
            action [SetVariable("_timed_choice_result", "minh"), Return()]
            xalign 0.5

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
