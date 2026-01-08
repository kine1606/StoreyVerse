# Door Transition Implementation Summary

## Overview
I've implemented a "Detective Conan" style door opening/closing transition system for your StoreyVerse visual novel using the OpenDoor.mov video.

## What Was Added

### 1. **Door Video Definition** ([images.rpy](game/images.rpy))
- Added `image door_opening` that plays the OpenDoor.mov video
- Video is set to display at 1920x1080 resolution

### 2. **Door Transition Labels** ([door_transitions.rpy](game/door_transitions.rpy))
New file created with three transition types:

- **`door_opening_transition`**: Used at game start
  - Starts with black screen
  - Plays door opening video
  - Fades to white background
  
- **`door_chapter_transition`**: Used between chapters
  - Fades to black (door "closes")
  - Brief pause
  - Plays door opening video again
  - Fades to white background
  
- **`door_quick_transition`**: Alternative faster version
  - Quick black → white transition without video
  - For more frequent scene changes if needed

### 3. **Integration into Story** ([story.rpy](game/story.rpy))
Door transitions are now called at these points:

1. **Game Start** → Door opens when player clicks "Start"
2. **Scene 1 → Scene 2** → Door closes and reopens
3. **Scene 2 → Scene 3** → Door closes and reopens
4. **Scene 3 → Scene 4** → Door closes and reopens
5. **Scene 4 → Scene 5** → Door closes and reopens
6. **Scene 5 → Scene 6** → Door closes and reopens

## How It Works

### Game Start Flow:
```
Main Menu → Click "Start" 
    ↓
Black screen
    ↓
OpenDoor.mov plays (door gradually opens)
    ↓
White background
    ↓
Scene 1 begins (Club room)
```

### Chapter Transition Flow:
```
End of Chapter X
    ↓
Fade to black (door "closes")
    ↓
Brief pause
    ↓
OpenDoor.mov plays again (door reopens)
    ↓
White background
    ↓
Next Chapter begins
```

## Customization Options

### Adjust Video Timing
If the video pause is too long/short, edit the pause duration in [door_transitions.rpy](game/door_transitions.rpy):
```renpy
$ renpy.pause(0.5)  # Change 0.5 to your preferred seconds
```

### Skip Certain Transitions
If you want to skip the door transition for specific scenes, simply remove the `call door_chapter_transition` line before that scene's jump statement.

### Use Quick Transitions
For less important scene changes, replace:
```renpy
call door_chapter_transition
```
with:
```renpy
call door_quick_transition
```

## Video Requirements
- File: `images/OpenDoor.mov`
- The video should show a door gradually opening
- Should end with a white/bright background
- Video will play at full size (1920x1080)

## Testing
To test the transitions:
1. Run your Ren'Py game
2. Click "Start" on the main menu
3. Watch the door opening animation
4. Play through each chapter to see transitions between scenes

The door will close (fade to black) and reopen (play video) between each major chapter, just like in Detective Conan!
