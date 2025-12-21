# SỰ PHẢN BỘI - GAME SETUP GUIDE

## GAME STRUCTURE

Your visual novel game is now complete! Here's what has been created:

### Main Files:
1. **story.rpy** - Complete game script with all 6 scenes and all endings
2. **config.rpy** - Game configuration and character definitions
3. **images.rpy** - Image placeholder definitions
4. **audio_placeholders.rpy** - Audio placeholder definitions

### Game Features:
✅ 6 Complete Scenes (Cảnh 1-6)
✅ Multiple Choice System with Consequences
✅ Trust Level Tracking System
✅ Branching Paths (Branch A & B in Scene 2)
✅ 6 Different Endings:
   - BAD END 1: Kẻ Lạc Lối
   - BAD END 2: Căn Phòng Hơi Ngạt
   - NORMAL END A: Giọt Mực Đen
   - NORMAL END B: Rạn Nứt
   - BAD END: Sự Hỗn Loạn
   - TRUE END: Bình Minh

✅ Key Item System (Mảnh giấy, Bản dịch)
✅ Character Injury Tracking
✅ Confession System
✅ Dynamic Dialogue Based on Choices

## WHAT YOU NEED TO ADD:

### 1. Character Sprites
Add character images to: `game/images/characters/`
- MINH (protagonist)
- LAN (smart girl)
- TUẤN (protective guy)
- MAI (sensitive girl)

### 2. Background Images (Optional but recommended)
Add backgrounds to: `game/images/backgrounds/`
See: `game/images/backgrounds/_PLACEHOLDER_INFO.txt` for the list

Currently using colored placeholders:
- Club room (#2b1810 - dark brown)
- Old corridor (#3a3a2e - dark gray)
- Library (#1a1a1a - very dark)
- Archive room (#2e2e2e - dark gray)
- Chemistry room (#1e2e1e - dark green tint)
- Mirror hallway (#1a1a2e - dark blue)
- White room (#ffffff)
- Dawn sky (#ff9966 - orange)

### 3. Audio Files (Optional)
Add audio to: `game/audio/`
See: `game/audio/_PLACEHOLDER_INFO.txt` for the complete list
Currently using silent placeholders - game will run fine without audio

## HOW TO RUN:

1. Open the game folder in Ren'Py Launcher
2. Click "Launch Project"
3. The game will start from `story.rpy` label `start`

## TESTING DIFFERENT PATHS:

### To reach TRUE ENDING:
1. Scene 2: Choose "Đi cùng nhau" → Take "Tập Giấy Ghi Chú"
2. Scene 3: Choose "Để tớ làm" (builds trust)
3. Scene 4: Make any confession
4. Scene 5: Choose "Nộp giấy trắng và thuyết phục"
5. Scene 6: Will unlock automatically with key item

### To test BAD ENDS:
- BAD END 1: Choose "Chia nhóm" → "Tin ngay" → "Đợi đã, cuốn sách kia phát sáng!"
- BAD END 2: In Scene 3, choose "Không! Tớ không thể ép ai cả!"

## GAME VARIABLES:

The game tracks:
- `game_state.has_fake_evidence_note` - Key item from library
- `game_state.has_translation_document` - Key item from archive
- `game_state.group_trust_level` - Determines persuasion success
- `game_state.minh_injury` - If Minh sacrificed in chemistry room
- `game_state.tuan_injury` - If Tuấn was chosen
- `game_state.lan_injury` - If Lan was chosen
- Various confession variables

## NOTES:

- The old demo code in `script.rpy` is preserved but not used
- Game entry point is now in `story.rpy`
- All placeholder systems allow the game to run immediately
- You can add real assets (images, audio) gradually

## CUSTOMIZATION:

To modify game settings, edit:
- `config.rpy` - Character colors, game title, save directory
- `gui.rpy` - UI appearance
- `options.rpy` - Game options

Good luck with your visual novel! 🎮
