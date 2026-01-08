# 🎭 StoreyVerse - Sự Phản Bội (The Betrayal)

A psychological horror visual novel built with Ren'Py 8.5.0

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Ren'Py](https://img.shields.io/badge/Ren'Py-8.5.0-red.svg)
![Language](https://img.shields.io/badge/language-Vietnamese-green.svg)

## 📖 Story

Four friends gather in their school's Paranormal Activities Club room late at night to perform an Ouija board ritual. What starts as a harmless game quickly spirals into a deadly nightmare when they become trapped in a twisted version of their school.

A mysterious Game Master forces them to complete dangerous challenges, and whispers suggest that one of them has been possessed. Trust erodes as secrets are revealed, and the group must decide: will they turn on each other, or unite against the true enemy?

**Can you guide Minh through the darkness and uncover the truth before it's too late?**

## ✨ Features

### 🎮 Gameplay Mechanics
- **Branching Narrative**: Multiple story paths based on player choices
- **Hidden Psychological System**: Secret variables (Trust, Guilt, Authority) affect outcomes
- **Timed Decisions**: Critical moments with countdown timers that force quick thinking
- **Multiple Endings**: 
  - 1 True Ending (Dawn)
  - 2 Normal Endings (Black Ink, Cracked)
  - 3+ Bad Endings (Lost, Gas Room, Chaos)

### 🎨 Visual Features
- **Dynamic Character Sprites**: Multiple expressions and emotions for each character
- **Costume System**: Unlock and equip different outfits in the Mystery Shop
- **Cinematic Transitions**: Detective Conan-style door opening/closing animations
- **Atmospheric Backgrounds**: Hand-crafted scenes for each location

### 🛍️ Mystery Shop
- Purchase character skins using coins earned through gameplay
- Interactive shopkeeper with dynamic responses
- Unlockable premium outfits for customization

### 🧠 Psychological Horror Elements
- Confession scenes that reveal dark secrets
- Trust-breaking moments that affect character relationships
- Moral dilemmas with no clear right answers
- Paranoia-inducing gameplay that questions everyone's motives

## 🎯 Characters

- **Minh (MINH)** - The protagonist. A regular student who becomes the de facto leader
- **Lan (LAN)** - The intelligent researcher who values logic above emotion
- **Tuấn (TUẤN)** - The strong, protective friend with a hidden jealous side
- **Mai (MAI)** - The seemingly weak member who may be hiding something

## 🎬 Key Scenes

1. **The Invitation** - The ritual that starts everything
2. **Maze of Clues** - Exploring the corrupted school
3. **Chemistry Room** - A deadly sacrifice must be made
4. **Hallway of Truth** - Confessing darkest secrets
5. **Voting Room** - The final judgment
6. **Confrontation** - Face the true enemy

## 🎲 How to Play

### Installation
1. Ensure you have Ren'Py 8.5.0 or later installed
2. Clone or download this repository
3. Launch the project through Ren'Py Launcher
4. Click "Launch Project"

### Controls
- **Left Click / Space**: Advance dialogue
- **Right Click / Esc**: Open game menu
- **D Key**: Toggle debug mode (shows psychological variables)
- **Mouse Wheel**: Scroll through backlog

### Tips for Best Experience
- Read carefully - small details matter
- Your choices have consequences beyond what's immediately visible
- Try different paths to discover all endings
- Enable debug mode to understand the hidden mechanics

## 🏆 Endings Guide

### True Ending: Dawn ☀️
**Requirements:**
- Find either the "Fake Evidence Note" or "Translation Document"
- Maintain high group trust (convince everyone to submit blank ballots)
- Successfully identify the Game Master as the impostor

### Normal Ending A: Black Ink 🖤
- Vote for Mai when prompted
- Sacrifice her to escape

### Normal Ending B: Cracked 💔
- Submit a blank ballot while others vote for Mai
- Maintain personal principles but lose friendship

### Bad Endings ☠️
Multiple failure states including:
- Hesitating too long in timed choices
- Making consistently poor decisions
- Failing to find key items

## 🛠️ Technical Details

### Built With
- **Engine**: Ren'Py 8.5.0.25111603
- **Language**: Python (Ren'Py Script)
- **Platform**: Windows, macOS, Linux (via Ren'Py)

### Project Structure
```
StoreyVerse/
├── game/
│   ├── audio/              # Sound effects and music
│   ├── images/
│   │   ├── backgrounds/    # Scene backgrounds
│   │   ├── Casual/        # Character sprites
│   │   └── skin/          # Premium character outfits
│   ├── script.rpy         # Main game script
│   ├── story.rpy          # Story scenes and dialogue
│   ├── skin_shop.rpy      # Shop system
│   ├── countdown_screen.rpy  # Timer UI
│   └── door_transitions.rpy  # Video transitions
└── README.md
```

### Key Systems

#### Psychological Variables (Hidden)
```python
class GameState:
    trust: int       # 0-10, affects persuasion in voting room
    guilt: int       # 0-10, impacts character relationships
    authority: int   # 0-10, determines leadership influence
```

#### Timed Choice System
- Countdown timer displays remaining seconds
- Hover effects on choice buttons
- Automatic bad ending if time expires

#### Skin Shop System
- Persistent coin storage across game sessions
- Dynamic character preview with body cropping
- Category filtering (All, Chie, Nora)
- Shopkeeper reactions based on purchase outcome

## 🎨 Asset Requirements

### Required Image Assets
- Character sprites (multiple expressions per character)
- Background scenes (10+ locations)
- Door transition video (OpenDoor.mov or .webm)
- Shop speech bubbles
- UI elements

### Audio Assets
- Background music (tension, boss theme, peaceful)
- Sound effects (countdown, acid burn, mirror accept, etc.)
- Voice clips (optional)

## 🐛 Debug Mode

Press **D** during gameplay to toggle debug statistics:
- Current Trust level
- Current Guilt level
- Current Authority level
- Group Trust Level
- Current equipped skins

## 📝 Development Notes

### Known Issues
- Door transition video (.mov format) may not play on all systems - consider converting to .webm
- Font file for scary text needs to be added to `game/fonts/`

### Future Improvements
- Add more character skins
- Implement achievement system
- Add voice acting
- Create animated CGs for key scenes
- Multiple language support

## 👥 Credits

**Course**: SE215 - Human-Computer Interaction  
**University**: OndaUni  
**Engine**: Ren'Py Visual Novel Engine  

### Development Team
- Game Design & Story
- Programming & Systems
- Art & Visual Design
- Audio & Sound Design

## 📄 License

This project is created for educational purposes as part of the SE215 course.

## 🙏 Acknowledgments

- Ren'Py community for documentation and support
- Detective Conan for door transition inspiration
- Beta testers for feedback

---

**Enjoy your descent into psychological horror!** 🎭👻

*Remember: Trust is fragile. Betrayal is eternal.*
