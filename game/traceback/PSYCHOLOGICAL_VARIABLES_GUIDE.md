# PSYCHOLOGICAL VARIABLES SYSTEM
## StoreyVerse - Sự Phản Bội

This document explains the three hidden psychological variables that make the game more realistic and immersive.

---

## Overview

The game uses **3 hidden variables** that track the psychological state of the group. These variables are:

1. **TRUST** - Niềm tin của nhóm dành cho Minh
2. **GUILT** - Tội lỗi tích tụ giữa các nhân vật  
3. **AUTHORITY** - Quyền đạo đức của Minh trong phòng bỏ phiếu

These variables are **NOT displayed to the player** by default (unless debug mode is enabled), creating a more realistic experience where players don't know exactly how their choices affect relationships.

---

## 1. TRUST (Niềm Tin)

**Range:** 0-10 | **Starting Value:** 5 (neutral)

### What it represents:
- How much the group trusts Minh's leadership
- Whether friends believe Minh has their best interests at heart

### Increases when:
- ✅ Minh makes selfless choices
- ✅ Minh sacrifices himself (Chemistry Room - "Để tớ làm")
- ✅ Minh stays with the group (choosing "Đi chùng nhau")
- ✅ Minh is cautious and avoids traps (not touching glowing book)

### Decreases when:
- ❌ Minh splits the group (Branch A - Library)
- ❌ Minh trusts fake evidence too quickly (A1 choice)
- ❌ Tuấn feels abandoned after being left behind

### Used in:
- **Scene 5 (Voting Room)** - Persuasion checks
- Required: `trust >= 1` (with evidence) or `trust >= 2` (without evidence)

---

## 2. GUILT (Tội Lỗi)

**Range:** 0-10 | **Starting Value:** 0 (no guilt)

### What it represents:
- Emotional burden characters carry
- Mai's guilt when Minh sacrifices for the group

### Increases when:
- 💔 Minh gets injured protecting everyone (Chemistry Room - self-sacrifice)
- 💔 Mai feels responsible for Minh's pain

### Effects:
- Creates emotional weight in character relationships
- Mai's guilt makes her more vulnerable to manipulation
- Affects the emotional tone of later scenes

### Used in:
- Character dialogue nuances
- Emotional authenticity in relationships

---

## 3. AUTHORITY (Quyền Đạo Đức)

**Range:** 0-10 | **Starting Value:** 5 (neutral)

### What it represents:
- Minh's moral standing to persuade others
- Whether the group respects Minh's judgment in critical moments

### Increases when:
- ⬆️ Minh tells the truth in confessions (Scene 4 - either confession choice)
- ⬆️ Minh shows moral integrity

### Decreases when:
- ⬇️ Minh takes emotional bait (B1 - Red Diary)
- ⬇️ Minh forces others to sacrifice (Chemistry Room - assigning Tuấn/Lan)
- ⬇️ Minh makes decisions that harm others

### Used in:
- **Scene 5 (Voting Room)** - Persuasion checks
- Required: `authority >= 1` (with evidence) or `authority >= 2` (without evidence)

---

## How They Work Together

### Scene 5: Critical Persuasion Check

To successfully persuade the group to trust each other in the voting room:

**Path 1: With Evidence (Fake Evidence Note or Translation Document)**
- Required: `trust >= 1 AND authority >= 1`
- Easier to achieve if Minh made good choices

**Path 2: Without Evidence (Pure Faith)**
- Required: `trust >= 2 AND authority >= 2`  
- Much harder - Minh must have been selfless and honest throughout

### Example Playthrough:

**Good Path to True Ending:**
1. Scene 2: Choose "Kiểm tra kỹ hơn" → Get evidence, avoid trap → `trust +0`
2. Scene 3: Choose "Để tớ làm" → Self-sacrifice → `trust +1, guilt +1`
3. Scene 4: Choose either honest confession → `authority +1`
4. Scene 5: Have evidence + `trust=6, authority=6` → **Success!**

**Bad Path to Normal Ending:**
1. Scene 2: Choose "Chộp lấy Cuốn Nhật Ký Bìa Đỏ" → `authority -1`
2. Scene 3: Choose "Chỉ định Tuấn làm" → `authority -2`
3. Scene 4: No confession bonus
4. Scene 5: `trust=5, authority=2` → **Persuasion fails**

---

## Debug Mode

To see these variables during gameplay:

1. Press **'D'** key during the game
2. A debug panel will appear in the top-left corner showing:
   - TRUST
   - GUILT  
   - AUTHORITY
   - GROUP TRUST (old system, still used)

3. Press **'D'** again to hide

**Note:** This is for testing purposes only. The intended experience is to play without seeing these numbers.

---

## Design Philosophy

### Why Hide These Variables?

1. **Realism**: In real life, you don't know exactly how much people trust you
2. **Immersion**: Players make choices based on morality, not min-maxing numbers
3. **Surprise**: Persuasion success/failure feels more organic and emotional
4. **Replay Value**: Players discover different outcomes through natural play

### Compared to Old System:

**Old System:**
- Only `group_trust_level` (visible to code)
- Simple threshold checks
- Less nuanced

**New System:**
- 3 psychological dimensions
- Tracks both trust AND moral authority
- Emotional consequences (guilt)
- More realistic character dynamics

---

## Variable Changes Summary

| Scene | Choice | TRUST | GUILT | AUTHORITY |
|-------|--------|-------|-------|-----------|
| **Scene 2 - Library** | | | | |
| Split group (A) | - | - | - | - |
| Trust fake evidence (A1) | -1 | - | - | - |
| Examine carefully (A2) | - | - | - | - |
| Avoid trap (S2) | - | - | - | - |
| Reunite (Tuấn upset) | -1 | - | - | - |
| **Scene 2 - Archive** | | | | |
| Red Diary (B1) | - | - | -1 | - |
| Translation Doc (B2) | - | - | - | - |
| **Scene 3 - Chemistry** | | | | |
| Hesitate (A) | - | - | - | DEATH |
| Assign Tuấn (B) | - | - | -2 | - |
| Assign Lan (B) | - | - | -2 | - |
| Self-sacrifice (C) | +1 | +1 | - | - |
| **Scene 4 - Truth Hall** | | | | |
| Honest confession | - | - | +1 | - |

---

## Implementation Notes

### File Location:
`game/story.rpy` - Lines 8-50 (GameState class definition)

### Debug Screens:
- `debug_stats()` - Shows variable panel
- `debug_toggle()` - Keyboard listener for 'D' key

### Integration:
All psychological variables are part of the `game_state` object and are saved with game progress.

---

## Future Enhancements (Optional)

Potential expansions to the system:

1. **PARANOIA** - Tracks how suspicious Minh becomes
2. **COHESION** - Measures overall group unity
3. **DESPERATION** - Increases over time, affects decision-making
4. **Character-specific trust** - Individual trust levels (Lan's trust, Tuấn's trust, Mai's trust)

---

## Conclusion

The psychological variables system creates a more nuanced, realistic experience where:

- **Choices have hidden consequences**
- **Moral integrity matters** (not just gathering evidence)
- **Relationships feel authentic** (guilt, trust, authority)
- **Outcomes emerge organically** (not obviously triggered)

This aligns with the game's theme: **"Kẻ phản bội không phải quỷ, mà là sự hèn nhát của con người"** (The betrayer isn't a demon, but human cowardice).

---

**Made with ❤️ for StoreyVerse**  
*Updated: December 2025*
