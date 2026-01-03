# ============================================
# SKIN SHOP SYSTEM
# Base system for character skins/outfits
# ============================================

# ============================================
# PERSISTENT DATA (Saves across game sessions)
# ============================================

default persistent.shop_coins = 500
default persistent.shop_unlocked_skins = ["minh_casual", "lan_casual", "tuan_casual", "mai_casual"]
default persistent.shop_equipped_skins = {}

# ============================================
# SHOP DATA STRUCTURES
# ============================================

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
            self.categories = ["All", "Minh", "Lan", "Tuấn", "Mai"]
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
        # ============================================
        
        skin_shop.add_skin(SkinItem(
            id="minh_casual",
            name="Casual Outfit",
            character="Minh",
            price=0,
            description="Minh's default casual outfit.",
            preview_image=None
        ))
        
        skin_shop.add_skin(SkinItem(
            id="lan_casual",
            name="Casual Outfit", 
            character="Lan",
            price=0,
            description="Lan's default casual outfit.",
            preview_image=None
        ))
        
        skin_shop.add_skin(SkinItem(
            id="tuan_casual",
            name="Casual Outfit",
            character="Tuấn",
            price=0,
            description="Tuấn's default casual outfit.",
            preview_image=None
        ))
        
        skin_shop.add_skin(SkinItem(
            id="mai_casual",
            name="Casual Outfit",
            character="Mai",
            price=0,
            description="Mai's default casual outfit.",
            preview_image=None
        ))
        
        # ============================================
        # PREMIUM SKINS (Purchasable)
        # Add your custom skins here!
        # ============================================
        
        skin_shop.add_skin(SkinItem(
            id="minh_formal",
            name="Formal Suit",
            character="Minh",
            price=100,
            description="A stylish formal suit for Minh.",
            preview_image=None
        ))
        
        skin_shop.add_skin(SkinItem(
            id="lan_summer",
            name="Summer Dress",
            character="Lan",
            price=150,
            description="A beautiful summer dress for Lan.",
            preview_image=None
        ))
        
        skin_shop.add_skin(SkinItem(
            id="tuan_sports",
            name="Sports Outfit",
            character="Tuấn",
            price=120,
            description="Athletic sports wear for Tuấn.",
            preview_image=None
        ))
        
        skin_shop.add_skin(SkinItem(
            id="mai_winter",
            name="Winter Coat",
            character="Mai",
            price=180,
            description="A warm winter coat for Mai.",
            preview_image=None
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
    add Solid("#000000AA")
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 650
        background "#1a1a2e"
        padding (20, 20)
        
        vbox:
            spacing 15
            
            # Header with title and coins
            hbox:
                xfill True
                
                text "🛍️ Skin Shop" size 36 color "#FFFFFF" yalign 0.5
                
                hbox:
                    xalign 1.0
                    spacing 10
                    
                    text "🪙" size 28 yalign 0.5
                    text "[persistent.shop_coins]" size 24 color "#FFD700" yalign 0.5
            
            # Separator line
            add Solid("#444444") xsize 960 ysize 2
            
            # Category tabs
            hbox:
                xalign 0.5
                spacing 15
                
                for cat in ["All", "Minh", "Lan", "Tuấn", "Mai"]:
                    textbutton cat:
                        style "shop_tab_button"
                        action SetVariable("shop_current_category", cat)
                        selected shop_current_category == cat
            
            null height 10
            
            # Skin grid with scrolling
            viewport:
                scrollbars "vertical"
                mousewheel True
                xfill True
                ysize 420
                
                vbox:
                    spacing 15
                    
                    # Create rows of 4 skins each
                    python:
                        current_skins = skin_shop.get_skins_by_category(shop_current_category)
                    
                    hbox:
                        spacing 15
                        xalign 0.5
                        
                        for skin in current_skins:
                            frame:
                                xsize 220
                                ysize 300
                                background "#2d2d44"
                                padding (10, 10)
                                
                                vbox:
                                    spacing 8
                                    
                                    # Preview area
                                    frame:
                                        xsize 200
                                        ysize 150
                                        xalign 0.5
                                        background "#3d3d5c"
                                        
                                        if skin.preview_image:
                                            add skin.preview_image xalign 0.5 yalign 0.5 fit "contain"
                                        else:
                                            vbox:
                                                xalign 0.5
                                                yalign 0.5
                                                text "👤" size 50 xalign 0.5
                                                text "No Preview" size 12 color "#888888" xalign 0.5
                                    
                                    # Skin info
                                    text skin.name size 16 color "#FFFFFF" xalign 0.5
                                    text skin.character size 12 color "#888888" xalign 0.5
                                    
                                    # Action button
                                    if skin.unlocked:
                                        if skin_shop.is_equipped(skin.id):
                                            textbutton "✓ Equipped":
                                                style "shop_equipped_button"
                                                xalign 0.5
                                                action NullAction()
                                        else:
                                            textbutton "Equip":
                                                style "shop_equip_button"
                                                xalign 0.5
                                                action Function(skin_shop.equip_skin, skin.id)
                                    else:
                                        if skin.can_purchase():
                                            textbutton "🪙 [skin.price]":
                                                style "shop_buy_button"
                                                xalign 0.5
                                                action Function(skin.purchase)
                                        else:
                                            textbutton "🪙 [skin.price]":
                                                style "shop_locked_button"
                                                xalign 0.5
                                                action NullAction()
            
            # Footer with back button
            hbox:
                xalign 0.5
                
                textbutton "← Back to Menu":
                    style "shop_back_button"
                    action Return()

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
