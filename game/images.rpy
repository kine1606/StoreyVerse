# Image definitions for Sự Phản Bội game

# Background images for scenes
# Scene 1: Club room at night (supernatural ritual setting)
image bg club night = "images/backgrounds/bg club night .png"
image bg club_room = "images/Noraneko_Backgrounds_Pack_2/bg bedroom night dark.png"

# Scene 2: Haunted school corridors and rooms
image bg old_corridor = "images/Noraneko_Backgrounds_Pack_2/bg school hallway day.png"
image bg library = "images/Noraneko_Backgrounds_Old/bg old school.png"
image bg archive_room = "images/Noraneko_Backgrounds_Pack_2/bg classroom day.png"

# Scene 3: Chemistry room (dark, ominous)
image bg chemistry_room = "images/Noraneko_Backgrounds_Pack_2/bg livingroom dark.png"

# Scene 4: Mirror hallway (eerie, reflective)
image bg mirror_hallway = "images/Noraneko_Backgrounds_Pack_3/bg backstreet spring night.png"

# Scene 5: Voting room (stark white room)
image bg white_room = "images/Noraneko_Backgrounds_Pack_2/bg bedroom day.png"

# Scene 6 & Ending: Dawn/bright sky
image bg dawn_sky = "images/Noraneko_Backgrounds_Pack_2/bg street summer stars.png"

# Utility backgrounds
image bg black = "#000000"
image bg white = "#ffffff"

# Character sprite placeholders
# (You'll add actual character sprites later)
# image minh = "character/minh.png"
# image lan = "character/lan.png"
# image tuan = "character/tuan.png"
# image mai = "character/mai.png"

# Character sprites - MINH (aoto)
image aoto = "images/Casual/aoto/aoto casual glasses smile.png"
image aoto smile = "images/Casual/aoto/aoto casual glasses smile.png"
image aoto open = "images/Casual/aoto/aoto casual glasses open.png"
image aoto frown = "images/Casual/aoto/aoto casual glasses frown.png"
image aoto closed smile = "images/Casual/aoto/aoto casual glasses closed smile.png"
image aoto closed open = "images/Casual/aoto/aoto casual glasses closed open.png"
image aoto closed frown = "images/Casual/aoto/aoto casual glasses closed frown.png"

# Character sprites - LAN (chie) - Dynamic based on equipped skin
init python:
    def get_chie_image(expression="smile"):
        """Get Chie's image path based on equipped skin"""
        skin_id = persistent.shop_equipped_skins.get("Chie")
        if skin_id == "chie_gym":
            return "images/skin/chie/chie gym {}.png".format(expression)
        return "images/Casual/chie/chie casual {}.png".format(expression)
    
    def get_nora_image(expression="smile"):
        """Get Nora's image path based on equipped skin"""
        skin_id = persistent.shop_equipped_skins.get("Nora")
        if skin_id == "nora_summeruni":
            return "images/skin/nora/nora summeruni {}.png".format(expression)
        return "images/Casual/nora/nora casual {}.png".format(expression)

# Dynamic character images for Chie (uses equipped skin)
image chie = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Chie') == 'chie_gym'", "images/skin/chie/chie gym smile.png",
    "True", "images/Casual/chie/chie casual smile.png"
)
image chie smile = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Chie') == 'chie_gym'", "images/skin/chie/chie gym smile.png",
    "True", "images/Casual/chie/chie casual smile.png"
)
image chie open = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Chie') == 'chie_gym'", "images/skin/chie/chie gym open.png",
    "True", "images/Casual/chie/chie casual open.png"
)
image chie frown = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Chie') == 'chie_gym'", "images/skin/chie/chie gym frown.png",
    "True", "images/Casual/chie/chie casual frown.png"
)
image chie closed smile = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Chie') == 'chie_gym'", "images/skin/chie/chie gym closed smile.png",
    "True", "images/Casual/chie/chie casual closed smile.png"
)
image chie closed open = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Chie') == 'chie_gym'", "images/skin/chie/chie gym closed open.png",
    "True", "images/Casual/chie/chie casual closed open.png"
)
image chie closed frown = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Chie') == 'chie_gym'", "images/skin/chie/chie gym closed frown.png",
    "True", "images/Casual/chie/chie casual closed frown.png"
)

# Character sprites - TUAN (sora)
image sora = "images/Casual/sora/sora casual smile.png"
image sora smile = "images/Casual/sora/sora casual smile.png"
image sora open = "images/Casual/sora/sora casual open.png"
image sora frown = "images/Casual/sora/sora casual frown.png"
image sora closed smile = "images/Casual/sora/sora casual closed smile.png"
image sora closed open = "images/Casual/sora/sora casual closed open.png"
image sora closed frown = "images/Casual/sora/sora casual closed frown.png"

# Dynamic character images for Nora (uses equipped skin)
image nora = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Nora') == 'nora_summeruni'", "images/skin/nora/nora summeruni smile.png",
    "True", "images/Casual/nora/nora casual smile.png"
)
image nora smile = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Nora') == 'nora_summeruni'", "images/skin/nora/nora summeruni smile.png",
    "True", "images/Casual/nora/nora casual smile.png"
)
image nora open = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Nora') == 'nora_summeruni'", "images/skin/nora/nora summeruni open.png",
    "True", "images/Casual/nora/nora casual open.png"
)
image nora frown = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Nora') == 'nora_summeruni'", "images/skin/nora/nora summeruni frown.png",
    "True", "images/Casual/nora/nora casual frown.png"
)
image nora closed smile = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Nora') == 'nora_summeruni'", "images/skin/nora/nora summeruni closed smile.png",
    "True", "images/Casual/nora/nora casual closed smile.png"
)
image nora closed open = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Nora') == 'nora_summeruni'", "images/skin/nora/nora summeruni closed open.png",
    "True", "images/Casual/nora/nora casual closed open.png"
)
image nora closed frown = ConditionSwitch(
    "persistent.shop_equipped_skins.get('Nora') == 'nora_summeruni'", "images/skin/nora/nora summeruni closed frown.png",
    "True", "images/Casual/nora/nora casual closed frown.png"
)

# Special effects
image gamemaster = "#ff0000"  # Placeholder for gamemaster sprite
image ghost_minion = "#660000"  # Placeholder for ghost sprite

# Timer display
image timer = Text("00:60", size=40, color="#ff0000")
