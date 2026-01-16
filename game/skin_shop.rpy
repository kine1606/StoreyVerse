# ============================================
# SKIN SHOP SYSTEM
# Base system for character skins/outfits
# ============================================

# ============================================
# PERSISTENT DATA (Saves across game sessions)
# ============================================

default persistent.shop_coins = 1000
default persistent.shop_unlocked_skins = ["chie_casual", "nora_casual"]
default persistent.shop_equipped_skins = {}

# ============================================
# SHOP DATA STRUCTURES
# ============================================
transform shop_base:
    zoom 0.88
    yalign 1.0
    xpos -50
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
default shop_owner_state = "welcome"  # welcome, success, no_money, equip_success
default shop_preview_character = None  # Character to preview (Chie, Nora, etc.)

init python:
    def shop_try_purchase(skin):
        """Try to purchase a skin and update shop owner state"""
        global shop_owner_state
        if skin.can_purchase():
            skin.purchase()
            store.shop_owner_state = "success"
        else:
            store.shop_owner_state = "no_money"
        renpy.restart_interaction()
    
    def shop_equip_skin(skin_id):
        """Equip a skin and show success message - does NOT close the screen"""
        global shop_owner_state
        if skin_shop.equip_skin(skin_id):
            store.shop_owner_state = "equip_success"
            renpy.notify("Equipped successfully!")
            # Update preview to show the equipped skin
            skin = skin_shop.get_skin(skin_id)
            if skin:
                store.shop_preview_character = skin.character
            renpy.restart_interaction()
        # Return None to prevent screen from closing
        return None
    
    def get_character_preview_image(character):
        """Get the preview image for a character with their equipped skin"""
        if not character or character == "All":
            return None
        
        # Get the equipped skin for this character
        equipped_skin = skin_shop.get_equipped_skin(character)
        
        if equipped_skin and equipped_skin.preview_image:
            return equipped_skin.preview_image
        
        # Default images if no skin equipped
        default_images = {
            "Chie": "images/Casual/chie/chie casual smile.png",
            "Nora": "images/Casual/nora/nora casual smile.png",
            "Aoto": "images/Casual/aoto/aoto casual glasses open blush.png",
            "Sora": "images/Casual/sora/sora casual smile.png"
        }
        
        return default_images.get(character)

# ============================================
# SKIN SHOP SCREEN
# ============================================

screen skin_shop_screen():
    tag menu
    # show bg shop
    # Ensure shop is initialized
    python:
        if skin_shop is None:
            init_skin_shop()
    
    on "show" action SetVariable("shop_owner_state", "welcome")
    
    # Background
    add "images/backgrounds/shop.png" xysize (config.screen_width, config.screen_height)
    
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
        background "#6FBC6E"
        padding (15, 10)
        
        hbox:
            spacing 10
            text "🪙" size 24 yalign 0.5
            text "[persistent.shop_coins]" size 22 color "#FFFFFF" yalign 0.5
            text "+" size 22 color "#FFFFFF" yalign 0.5
    
    # Character preview - center of screen (shows selected character with equipped skin)
    if shop_preview_character and shop_preview_character != "All":
        python:
            preview_img = get_character_preview_image(shop_preview_character)
        
        if preview_img:
            add preview_img:
                zoom 0.88
                yalign 1.0
                xalign 0.5
    
    # Shop owner character - left center with dynamic expression
    if shop_owner_state == "success":
        add "images/Casual/shopper/shopper sus smile.png" at shop_base
    elif shop_owner_state == "no_money":
        add "images/Casual/shopper/shopper angry.png" at shop_base
    elif shop_owner_state == "equip_success":
        add "images/Casual/shopper/shopper sus smile.png" at shop_base
    else:
        add "images/Casual/shopper/shopper normal smile.png" at shop_base
    
    # Shop owner speech bubble using pre-made images
    if shop_owner_state == "success":
        add "images/backgrounds/shop/speech buy success.png"  yalign 0.2 xpos 250 zoom 0.88
    elif shop_owner_state == "no_money":
        add "images/backgrounds/shop/speech buy fail.png" xpos 250 yalign 0.2 zoom 0.88
    elif shop_owner_state == "equip_success":
        frame:
            xpos 250
            yalign 0.2
            background "#FFFFFF"
            padding (20, 15)
            text "Equipped successfully!" size 20 color "#000000"
    else:
        add "images/backgrounds/shop/speech welcome.png" xpos 250 yalign 0.2 zoom 0.88

    # Shop title - top center
    vbox:
        xalign 0.5
        ypos 30
        spacing 15
        
        text "Mystery shop" size 32 color "#EEEEEE" xalign 0.5
        
        # Category tabs
        vbox:
            xpos 250
            ypos 15
            # xalign 0.5
            spacing 8
            
            for cat in ["All", "Aoto", "Sora", "Chie", "Nora"]:
                textbutton cat:
                    style "shop_tab_button"
                    action [SetVariable("shop_current_category", cat), SetVariable("shop_preview_character", cat if cat != "All" else None)]
                    selected shop_current_category == cat
    
    # Items List - right center
    frame:
        xalign 1.0
        yalign 0.8
        xsize 460
        ysize 650
        background "#1a1a2e"
        padding (20, 15)
        
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
                                        background "#FFE693"
                                        padding (10, 10)
                                        
                                        vbox:
                                            spacing 10
                                            xalign 0.5
                                            
                                            # Skin preview (top) - Light pink background, cropped to show body only
                                            frame:
                                                xsize 160
                                                ysize 180
                                                xalign 0.5
                                                background "#FFC6E9"  # Light pink
                                                
                                                fixed:
                                                    xfit True
                                                    yfit True
                                                    
                                                    if skin.preview_image:
                                                        # Crop the image to show only body (cut off head)
                                                        # Crop(x, y, width, height) - start from y=300 to skip head
                                                        add Crop((0, 300, 600, 700), skin.preview_image):
                                                            zoom 0.25
                                                            anchor (0.5, 0.5)
                                                            pos (110, 120)
                                                    else:
                                                        text "👤" size 60 xalign 0.5 yalign 0.5 color "#333333"
                                            
                                            # Skin name (middle)
                                            text skin.name size 16 color "#000000" xalign 0.5 text_align 0.5
                                            
                                            # Price (bottom)
                                            if skin.unlocked:
                                                if skin_shop.is_equipped(skin.id):
                                                    text "✓ Equipped" size 16 color "#6FBC6E" xalign 0.5
                                                else:
                                                    textbutton "Equip":
                                                        style "shop_card_button"
                                                        xalign 0.5
                                                        action [Function(shop_equip_skin, skin.id), NullAction()]
                                            else:
                                                textbutton "🪙[skin.price]":
                                                    style "shop_card_buy_button"
                                                    xalign 0.5
                                                    action [Function(shop_try_purchase, skin), NullAction()]

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
    xminimum 150

style shop_card_buy_button_text:
    size 10
    color "#FFFFFF"
    xalign 0.5

style shop_back_button:
    background Frame("#6FBC6E", 20, 20)
    hover_background Frame("#2fad2d", 20, 20)
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
