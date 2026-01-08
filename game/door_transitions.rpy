# Door Opening/Closing Transitions
# Like "Detective Conan" - door gradually opens with white background at the end

# ============================================
# VIDEO PLAYBACK SCREEN
# ============================================

screen play_door_video():
    zorder 100
    modal True
    
    # Try to play video - prefer .webm, fallback to .mov
    add Movie(play="images/OpenDoor.webm", loop=False):
        size (config.screen_width, config.screen_height)
        xalign 0.5
        yalign 0.5
    
    # Auto-dismiss after video duration
    timer 5.0 action Hide("play_door_video")

# ============================================
# DOOR OPENING TRANSITION (Game Start)
# ============================================

label door_opening_transition:
    # Start with black screen
    scene bg black
    
    # Try to play video
    python:
        import os
        video_path_webm = renpy.loader.transfn("images/OpenDoor.webm")
        video_path_mov = renpy.loader.transfn("images/OpenDoor.mov")
        has_video = os.path.exists(video_path_webm) if video_path_webm else (os.path.exists(video_path_mov) if video_path_mov else False)
    
    if has_video:
        # Show the video playback screen
        show screen play_door_video
        
        # Wait for the video to finish
        $ renpy.pause(5.0, hard=True)
        
        # Hide the video screen
        hide screen play_door_video
    else:
        # Fallback: simple fade transition
        scene bg white
        with Dissolve(2.0)
        $ renpy.pause(0.5)
    
    # Fade to white at the end (like the video shows)
    # scene bg white
    # with dissolve
    
    # Brief pause on white
    $ renpy.pause(0.5)
    
    return


# ============================================
# DOOR CLOSING & REOPENING (Chapter Transitions)
# ============================================

label door_chapter_transition:
    # """
    # Call this label between chapters to show:
    # 1. Door closing (reversed video)
    # 2. Brief pause
    # 3. Door opening again (normal video)
    # """
    
    # Fade to black (door is "closed")
    scene bg black
    with fade
    
    # Brief pause
    $ renpy.pause(0.5)
    
    # Show the video playback screen
    show screen play_door_video
    
    # Wait for the video to finish
    $ renpy.pause(5.0, hard=True)
    
    # Hide the video screen
    hide screen play_door_video
    
    # Fade to white
    scene bg white
    with dissolve
    
    # Brief pause
    $ renpy.pause(0.5)
    
    return


# ============================================
# ALTERNATIVE: Quick Door Transition
# ============================================

label door_quick_transition:
    
    # Quick fade to black
    scene bg black
    with Dissolve(0.3)
    
    # Very brief pause
    $ renpy.pause(0.2)
    
    # Quick fade to white
    scene bg white
    with Dissolve(0.3)
    
    # Brief pause
    $ renpy.pause(0.2)
    
    return
