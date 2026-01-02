# GAME CONFIGURATION FOR SỰ PHẢN BỘI

# Game title and version
define config.name = "Sự Phản Bội"
define config.version = "1.0"

# Game window settings
define config.window_title = "Sự Phản Bội - The Betrayal"

# Save directory name
define config.save_directory = "SuPhanBoi"

# Character definitions
define narrator = Character(None, kind=nvl)
define MINH = Character("MINH", color="#4169e1", who_bold=True, image="aoto")
define LAN = Character("LAN", color="#9370db", who_bold=True, image="chie")
define TUAN = Character("TUẤN", color="#ff6347", who_bold=True, image="sora")
define MAI = Character("MAI", color="#ffb6c1", who_bold=True, image="nora")

# Special characters
define GAMEMASTER = Character("???", color="#ff0000", who_bold=True, what_italic=True)

# Game settings
define config.has_autosave = True
define config.autosave_frequency = 200

# Transitions
define dissolve = Dissolve(1.0)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# Default text speed
default preferences.text_cps = 50
