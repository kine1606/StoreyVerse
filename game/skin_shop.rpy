# ============================================
# SKIN SHOP SYSTEM
# Base system for character skins/outfits
# ============================================

# ============================================
# PERSISTENT DATA (Saves across game sessions)
# ============================================

default persistent.shop_coins = 500
default persistent.shop_unlocked_skins = ["chie_casual", "nora_casual"]
default persistent.shop_equipped_skins = {}

# ============================================
# SHOP DATA STRUCTURES
# ============================================
transform character_base:
    zoom 0.88
    yalign 1.0

init python:
    
    class SkinItem:
        """Represents a single skin/outfit item"""
        def __init__(self, id, name, character, price, description="", preview_image=None):
            self.id = id
            self.name = name
            self.character = character  # Which character this skin is for
            self.price = price
            self.description = description
            self.preview_image = preview_image  # Image path for preview
        
        @property
        def unlocked(self):
            return self.id in persistent.shop_unlocked_skins
        
        def can_purchase(self):
            return persistent.shop_coins >= self.price and not self.unlocked
        
        def purchase(self):
            if self.can_purchase():
                persistent.shop_coins -= self.price
                if self.id not in persistent.shop_unlocked_skins:
                    persistent.shop_unlocked_skins.append(self.id)
                return True
            return False
    
    class SkinShop:
        """Manages the skin shop inventory"""
        def __init__(self):
            self.skins = {}  # id -> SkinItem
            self.categories = ["All", "Chie", "Nora"]
            self.current_category = "All"
        
        def add_skin(self, skin):
            """Add a skin to the shop"""
            self.skins[skin.id] = skin
        
        def get_skin(self, skin_id):
            """Get a skin by ID"""
            return self.skins.get(skin_id)
        
        def get_skins_by_category(self, category):
            """Get all skins for a specific character or all skins"""
            if category == "All":
                return list(self.skins.values())
            return [s for s in self.skins.values() if s.character == category]
        
        def get_unlocked_skins(self, character=None):
            """Get all unlocked skins, optionally filtered by character"""
            if character:
                return [s for s in self.skins.values() if s.unlocked and s.character == character]
            return [s for s in self.skins.values() if s.unlocked]
        
        def purchase_skin(self, skin_id):
            """Purchase a skin if player has enough coins"""
            skin = self.get_skin(skin_id)
            if skin:
                return skin.purchase()
            return False
        
        def equip_skin(self, skin_id):
            """Equip a skin for its character"""
            skin = self.get_skin(skin_id)
            if skin and skin.unlocked:
                persistent.shop_equipped_skins[skin.character] = skin_id
                return True
            return False
        
        def unequip_skin(self, character):
            """Unequip the skin for a character (revert to default)"""
            if character in persistent.shop_equipped_skins:
                del persistent.shop_equipped_skins[character]
        
        def get_equipped_skin(self, character):
            """Get the currently equipped skin for a character"""
            skin_id = persistent.shop_equipped_skins.get(character)
            if skin_id:
                return self.get_skin(skin_id)
            return None
        
        def is_equipped(self, skin_id):
            """Check if a skin is currently equipped"""
            skin = self.get_skin(skin_id)
            if skin:
                return persistent.shop_equipped_skins.get(skin.character) == skin_id
            return False
        
        def get_skin_image_path(self, character, expression):
            """
            Get the image path for a character with current equipped skin.
            character: 'Chie' or 'Nora'
            expression: 'smile', 'frown', 'open', 'closed smile', 'closed frown', 'closed open'
            Returns the full image path string.
            """
            skin_id = persistent.shop_equipped_skins.get(character)
            
            # Mapping of skin_id to folder/prefix
            skin_paths = {
                # Default casual skins
                "chie_casual": ("images/Casual/chie", "chie casual"),
                "nora_casual": ("images/Casual/nora", "nora casual"),
                # Premium skins
                "chie_gym": ("images/skin/chie", "chie gym"),
                "nora_summeruni": ("images/skin/nora", "nora summeruni"),
            }
            
            # Get default skin if none equipped
            if not skin_id:
                if character == "Chie":
                    skin_id = "chie_casual"
                elif character == "Nora":
                    skin_id = "nora_casual"
            
            if skin_id in skin_paths:
                folder, prefix = skin_paths[skin_id]
                return "{}/{} {}.png".format(folder, prefix, expression)
            
            # Fallback to casual
            if character == "Chie":
                return "images/Casual/chie/chie casual {}.png".format(expression)
            elif character == "Nora":
                return "images/Casual/nora/nora casual {}.png".format(expression)
            return None

# ============================================
# INITIALIZE SHOP
# ============================================

init python:
    skin_shop = None
    
    def init_skin_shop():
        """Initialize the skin shop with all available skins"""
        global skin_shop
        skin_shop = SkinShop()
        
        # ============================================
        # DEFAULT SKINS (Free/Unlocked by default)
        # Located in: images/Casual/{character}/
        # ============================================
        
        skin_shop.add_skin(SkinItem(
            id="chie_casual",
            name="Casual Outfit",
            character="Chie",
            price=0,
            description="Chie's default casual outfit.",
            preview_image="images/Casual/chie/chie casual smile.png"
        ))
        
        skin_shop.add_skin(SkinItem(
            id="nora_casual",
            name="Casual Outfit", 
            character="Nora",
            price=0,
            description="Nora's default casual outfit.",
            preview_image="images/Casual/nora/nora casual smile.png"
        ))
        
        # ============================================
        # PREMIUM SKINS (Purchasable)
        # Located in: images/skin/{character}/
        # ============================================
        
        skin_shop.add_skin(SkinItem(
            id="chie_gym",
            name="Gym Outfit",
            character="Chie",
            price=150,
            description="Athletic gym wear for Chie.",
            preview_image="images/skin/chie/chie gym smile.png"
        ))
        
        skin_shop.add_skin(SkinItem(
            id="nora_summeruni",
            name="Summer Uniform",
            character="Nora",
            price=180,
            description="A summer school uniform for Nora.",
            preview_image="images/skin/nora/nora summeruni smile.png"
        ))
    
    # Initialize shop at game start
    init_skin_shop()

# ============================================
# COIN REWARD FUNCTIONS
# ============================================

init python:
    def reward_coins(amount, reason=""):
        """Give coins to player - call this after completing scenes/endings"""
        persistent.shop_coins += amount
        if reason:
            renpy.notify("+{} coins: {}".format(amount, reason))
        else:
            renpy.notify("+{} coins!".format(amount))
    
    def get_coins():
        """Get current coin balance"""
        return persistent.shop_coins

# ============================================
# SHOP SCREEN VARIABLES
# ============================================

default shop_current_category = "All"
default shop_selected_skin = None

# ============================================
# SKIN SHOP SCREEN
# ============================================

screen skin_shop_screen():
    tag menu
    
    # Ensure shop is initialized
    python:
        if skin_shop is None:
            init_skin_shop()
    
    # Background
    add "gui/main_menu_background.png"
    
    # Dark overlay
    add Solid("#000000CC")
    
    # Back button - Top Left
    textbutton "← Back":
        style "shop_back_button"
        xpos 20
        ypos 20
        action Return()
    
    # Coins display - Top Right
    frame:
        xalign 1.0
        ypos 20
        xoffset -20
        background "#2d2d44"
        padding (15, 10)
        
        hbox:
            spacing 10
            text "🪙" size 24 yalign 0.5
            text "[persistent.shop_coins]" size 22 color "#FFD700" yalign 0.5
    
    # Shop owner character - left center
    add "images/Casual/shopper/shopper normal smile.png" at character_base xalign 0.2
    
    # Shop title - top center
    vbox:
        xalign 0.5
        ypos 30
        spacing 15
        
        text "🛍️ Skin Shop" size 32 color "#FFFFFF" xalign 0.5
        
        # Category tabs
        hbox:
            xalign 0.5
            spacing 8
            
            for cat in ["All", "Chie", "Nora"]:
                textbutton cat:
                    style "shop_tab_button"
                    action SetVariable("shop_current_category", cat)
                    selected shop_current_category == cat
    
    # Items List - right center
    frame:
        xalign 0.7
        yalign 0.55
        xsize 500
        ysize 600
        background "#1a1a2e"
        padding (20, 20)
        
        vbox:
            spacing 15
            
            # Title
            text "Available Items" size 24 color "#FFFFFF" xalign 0.5
            
            # Separator
            add Solid("#444444") xsize 460 ysize 2 xalign 0.5
            
            null height 5
            
            # Items list with scrollbar - 2 skins per row
            viewport:
                scrollbars "vertical"
                mousewheel True
                xfill True
                ysize 510
                
                vbox:
                    spacing 15
                    xalign 0.5
                    
                    python:
                        current_skins = skin_shop.get_skins_by_category(shop_current_category)
                        # Split into rows of 2
                        skin_rows = [current_skins[i:i+2] for i in range(0, len(current_skins), 2)]
                    
                    for row in skin_rows:
                            hbox:
                                spacing 20
                                xalign 0.5
                                
                                for skin in row:
                                    # Vertical card for each item - larger size
                                    frame:
                                        xsize 180
                                        ysize 280
                                        xalign 0.5
                                        background "#2d2d44"
                                        padding (10, 10)
                                        
                                        vbox:
                                            spacing 10
                                            xalign 0.5
                                            
                                            # Skin preview (top) - Light pink background, cropped to show body only
                                            frame:
                                                xsize 160
                                                ysize 180
                                                xalign 0.5
                                                background "#FFB6C1"  # Light pink
                                                
                                                if skin.preview_image:
                                                    # Crop the image to show only body (cut off head)
                                                    # Crop(x, y, width, height) - start from y=300 to skip head
                                                    add Crop((0, 300, 600, 700), skin.preview_image) xalign 0.5 yalign 0.5 zoom 0.25
                                                else:
                                                    text "👤" size 60 xalign 0.5 yalign 0.5 color "#333333"
                                            
                                            # Skin name (middle)
                                            text skin.name size 16 color "#FFFFFF" xalign 0.5 text_align 0.5
                                            
                                            # Price (bottom)
                                            if skin.unlocked:
                                                if skin_shop.is_equipped(skin.id):
                                                    text "✓ Equipped" size 16 color "#22c55e" xalign 0.5
                                                else:
                                                    textbutton "Equip":
                                                        style "shop_card_button"
                                                        xalign 0.5
                                                        action Function(skin_shop.equip_skin, skin.id)
                                            else:
                                                if skin.can_purchase():
                                                    textbutton "🪙[skin.price]":
                                                        style "shop_card_buy_button"
                                                        xalign 0.5
                                                        action Function(skin.purchase)
                                                else:
                                                    text "🪙[skin.price]" size 14 color "#9ca3af" xalign 0.5

# ============================================
# SHOP STYLES
# ============================================

style shop_tab_button:
    background "#3d3d5c"
    hover_background "#4d4d6c"
    selected_background "#6366f1"
    padding (20, 10)
    xminimum 80

style shop_tab_button_text:
    size 16
    color "#CCCCCC"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"

style shop_buy_button:
    background "#22c55e"
    hover_background "#16a34a"
    padding (25, 8)
    xminimum 100

style shop_buy_button_text:
    size 14
    color "#FFFFFF"
    xalign 0.5

style shop_equip_button:
    background "#3b82f6"
    hover_background "#2563eb"
    padding (25, 8)
    xminimum 100

style shop_equip_button_text:
    size 14
    color "#FFFFFF"
    xalign 0.5

style shop_equipped_button:
    background "#6b7280"
    padding (25, 8)
    xminimum 100

style shop_equipped_button_text:
    size 14
    color "#D1D5DB"
    xalign 0.5

style shop_locked_button:
    background "#4b5563"
    padding (25, 8)
    xminimum 100

style shop_locked_button_text:
    size 14
    color "#9ca3af"
    xalign 0.5

style shop_card_button:
    background "#3b82f6"
    hover_background "#2563eb"
    padding (8, 4)
    xminimum 60

style shop_card_button_text:
    size 10
    color "#FFFFFF"
    xalign 0.5

style shop_card_buy_button:
    background "#22c55e"
    hover_background "#16a34a"
    padding (8, 4)
    xminimum 60

style shop_card_buy_button_text:
    size 10
    color "#FFFFFF"
    xalign 0.5

style shop_back_button:
    background "#4b5563"
    hover_background "#6b7280"
    padding (30, 12)

style shop_back_button_text:
    size 18
    color "#FFFFFF"

# ============================================
# HELPER LABEL TO OPEN SHOP
# ============================================

label open_skin_shop:
    call screen skin_shop_screen
    return
