# SỰ PHẢN BỘI - VISUAL NOVEL GAME
# Story Script

# ============================================
# CHARACTER TRANSFORMS (Scale & Position)
# ============================================

transform character_base:
    zoom 0.88
    yalign 1.0

# For 2 characters - closer together for better UX
transform left:
    character_base
    xalign 0.25

transform right:
    character_base
    xalign 0.75

transform center:
    character_base
    xalign 0.5

# For 3-4 characters - wider spread
transform left_far:
    character_base
    xalign 0.05

transform right_far:
    character_base
    xalign 0.95

transform left_center:
    character_base
    xalign 0.35

transform right_center:
    character_base
    xalign 0.65

# For 4 characters spread evenly
transform pos1:
    character_base
    xalign 0.05

transform pos2:
    character_base
    xalign 0.35

transform pos3:
    character_base
    xalign 0.65

transform pos4:
    character_base
    xalign 0.95

transform text_shake:
    linear 0.03 xoffset -5
    linear 0.03 xoffset 5
    repeat 4

# ============================================
# GAME INITIALIZATION & VARIABLES
# ============================================

init python:
    # Debug mode for displaying psychological variables
    debug_mode = False  # Set to True to see variables on screen
    
    # Game state variables
    class GameState:
        def __init__(self):
            self.has_fake_evidence_note = False
            self.has_translation_document = False
            self.chose_red_diary = False
            self.group_trust_level = 0
            self.minh_injury = False
            self.tuan_injury = False
            self.lan_injury = False
            self.tuan_confession = ""
            self.mai_confession = ""
            self.lan_confession = ""
            self.minh_confession = ""
            
            # === PSYCHOLOGICAL VARIABLES (HIDDEN) ===
            # These variables affect the game's outcome but are not displayed to the player
            # They create a more realistic psychological experience
            
            # TRUST: Niềm tin của nhóm dành cho Minh (0-10)
            # Increases when: Minh makes selfless choices, stays with group
            # Decreases when: Minh abandons friends, trusts fake evidence too quickly
            # Used in: Scene 5 persuasion checks
            self.trust = 5  # Start neutral
            
            # GUILT: Tội lỗi tích tụ giữa các nhân vật (0-10)
            # Increases when: Someone is hurt protecting others (Mai feels guilty)
            # Used in: Character relationships and emotional impact
            self.guilt = 0  # Start with no guilt
            
            # AUTHORITY: Quyền đạo đức của Minh trong phòng bỏ phiếu (0-10)
            # Increases when: Minh tells truth in confessions
            # Decreases when: Minh forces others to sacrifice, reads emotional bait
            # Used in: Scene 5 persuasion checks - determines if group listens to Minh
            self.authority = 5  # Start neutral

    game_state = GameState()

# ============================================
# DEBUG SCREEN (Press 'D' to toggle)
# ============================================

screen debug_stats():
    if debug_mode:
        frame:
            xalign 0.02
            yalign 0.02
            xsize 300
            ysize 200
            background "#000000aa"
            
            vbox:
                spacing 5
                text "=== DEBUG MODE ===" color "#ffff00" size 18
                text "TRUST: [game_state.trust]/10" color "#00ff00"
                text "GUILT: [game_state.guilt]/10" color "#ff8800"
                text "AUTHORITY: [game_state.authority]/10" color "#00aaff"
                text "GROUP TRUST: [game_state.group_trust_level]" color "#ffffff" size 14
                null height 10
                text "Press 'D' to hide" color "#888888" size 12

# Key to toggle debug mode
screen debug_toggle():
    key "d" action ToggleVariable("debug_mode")
    key "D" action ToggleVariable("debug_mode")

# ============================================
# SCENE 1: THE INVITATION (LỜI MỜI GỌI)
# ============================================

label start:
    # Initialize game state
    $ game_state = GameState()
    
    # Show debug screens
    show screen debug_stats
    show screen debug_toggle
    
    # Play door opening video
    call door_opening_transition
    
    scene bg club night
    with fade
    
    "" "Phòng sinh hoạt CLB Tâm linh - 11:00 PM"
    
    "" "Ánh nến leo lét trong căn phòng tối tăm."
    "" "Mùi hương trầm thoảng qua, hòa lẫn với mùi bụi của những cuốn sách cổ xưa."
    "" "Bốn người bạn ngồi quay quanh một tấm bảng Ouija cũ kỹ."
    
    "" "Căn phòng có một cảm giác kỳ lạ... như thể có ai đó đang quan sát họ."
    
    # TUẤN speaks
    show sora at left
    with dissolve
    "TUẤN" "Tớ vẫn không tin được là chúng ta đang làm chuyện này."
    "TUẤN" "Nhỡ có con gì hiện ra thật thì sao?"
    
    # LAN speaks
    show chie at right
    with dissolve
    "LAN" "Thống kê cho thấy 99%% các nghi thức gọi hồn chỉ là ảo giác nhóm."
    "LAN" "Cứ xem như trải nghiệm tâm lý đi."
    
    show sora frown
    "TUẤN" "Cậu và cái kiểu nói chuyện khoa học đó..."
    "TUẤN" "Không phải mọi thứ đều giải thích được bằng số liệu đâu!"
    
    show chie frown
    "LAN" "Chính xác là mọi thứ ĐỀU có thể giải thích bằng khoa học."
    "LAN" "Chỉ là chúng ta chưa tìm ra cách thôi."
    
    # MAI speaks
    hide sora
    with dissolve
    show nora at left
    with dissolve
    "MAI" "Các cậu ơi... đừng cãi nhau nữa."
    "MAI" "Nhưng... từ lúc vào đây tớ đã thấy lạnh sống lưng rồi."
    
    show nora frown
    "MAI" "Các cậu có thấy không? Cái bóng tối ở góc kia... nó như đang nhìn chúng ta."
    
    hide nora
    hide chie
    with dissolve
    
    "" "Tất cả quay lại nhìn góc phòng tối đó."
    "" "Không có gì cả. Chỉ là bóng tối."
    "" "Hay là... có?"
    
    # MINH speaks
    hide chie
    hide nora
    with dissolve
    show aoto at center
    with dissolve
    "MINH" "Thôi nào các cậu. Đừng dọa nhau nữa."
    "MINH" "Chỉ là đọc vài câu cho vui thôi."
    
    show aoto smile
    "MINH" "Hơn nữa, nếu có ma thật thì chúng ta có bốn người cơ mà!"
    "MINH" "Để tớ đọc câu cuối cùng nhé."
    
    "" "Minh cầm tấm bảng Ouija lên, tay hơi run."
    "" "Dù nói mạnh mồm, nhưng trong thâm tâm anh cũng hơi... lo lắng."
    
    "" "Anh hít một hơi thật sâu..."
    
    play sound "audio/chant.ogg"
    "" "Minh đọc câu niệm chú cuối cùng..."
    
    "" "Giọng anh vang vọng trong căn phòng tĩnh lặng."
    "" "Những ngọn nến bắt đầu lung lay dữ dội."
    
    hide aoto
    with dissolve
    
    scene bg black
    with flash
    
    play sound "audio/candle_out.ogg"
    "" "Tất cả ngọn nến đồng loạt tắt phụt!"
    
    play sound "audio/pain.ogg"
    "" "Một cơn đau buốt nhói lên trong đầu cả bốn người."
    
    # Whispers - each character hears something different
    "" "Những lời thì thầm vang lên từ khắp nơi..."
    "" "Mỗi người nghe thấy một điều khác nhau."
    pause 1.0
    
    play sound "audio/whisper.ogg"
    
    centered "{color=#ff0000}MINH nghe thấy:{/color}\n\"Trong số các ngươi, có một kẻ đã bị chiếm xác.\""
    
    centered "{color=#ff0000}LAN nghe thấy:{/color}\n\"Đừng tin ai cả. Một người trong nhóm không còn là chính mình nữa.\""
    
    centered "{color=#ff0000}TUẤN nghe thấy:{/color}\n\"Là Mai. Nó đang giả vờ yếu đuối. Hãy cẩn thận.\""
    
    centered "{color=#ff0000}MAI nghe thấy:{/color}\n\"Bọn họ đang nghi ngờ ngươi. Ngươi sẽ bị bỏ lại.\""
    
    "" "Bốn người nhìn nhau, hoảng loạn."
    "" "Mỗi người đều có một bí mật mà họ không dám nói ra."
    
    scene bg club_room
    with flash
    
    "" "Khi ánh sáng trở lại, cánh cửa phòng đã biến mất."
    "" "Thay vào đó là một cổng sắt rỉ máu với dòng chữ khắc sâu:"
    
    show text "{size=+20}{color=#ff0000}TRÒ CHƠI BẮT ĐẦU\nTÌM RA KẺ MẠO DANH ĐỂ SỐNG SÓT{/color}{/size}" at truecenter
    with dissolve
    pause 3.0
    hide text
    
    # Door transition to next chapter
    call door_quick_transition
    
    jump scene2_corridor

# ============================================
# SCENE 2: MAZE OF CLUES (MÊ CUNG MANH MỐI)
# ============================================

label scene2_corridor:
    scene bg old_corridor
    with fade
    
    "" "Hành lang trường học cũ nát"
    
    "" "Căn hành lang ẩm mốc, vách tường bong tróc."
    "" "Mùi mốc nồng nặc khiến cả nhóm khó thở."
    "" "Những bóng đèn huỳnh quang nhấp nháy yếu ớt trên trần nhà."
    
    show nora frown at right
    with dissolve
    "MAI" "Chỗ này... tại sao nó lại giống trường của chúng ta thế?"
    "MAI" "Nhưng mà... cũ hơn. Rất nhiều."
    
    show aoto at left
    with dissolve
    "MINH" "Không chỉ cũ. Nó như thể đã bị bỏ hoang hàng chục năm."
    
    hide nora
    hide aoto
    with dissolve
    
    show chie at right
    with dissolve
    "LAN" "Chúng ta cần thông tin. Nếu có kẻ mạo danh, phải có manh mối."
    "LAN" "Nên tìm kiếm có hệ thống. Chia ra để kiểm tra nhiều nơi hơn."
    
    show sora at left
    with dissolve
    "TUẤN" "Chia ra sẽ nhanh hơn. Minh và Lan vào thư viện. Tôi trông Mai ở phòng y tế."
    
    show chie frown at right
    "LAN" "Sao cậu lại muốn đi với Mai?"
    
    show sora frown at left
    "TUẤN" "Cô ấy yếu nhất. Ai đó phải bảo vệ cô ấy."
    
    show chie closed frown at right 
    "LAN" "Hay là cậu muốn giám sát cô ấy?"
    
    "" "Không khí bỗng trở nên căng thẳng."
    "" "Lời thì thầm về Mai vẫn còn văng vẳng trong đầu Tuấn."
    
    "" "Minh phải đưa ra quyết định..."
    
    menu:
        "Chia nhóm hành động {color=#ff6666}(Nguy hiểm){/color}":
            $ game_state.group_trust_level -= 10
            # Leaving friends behind reduces trust
            jump scene2_branch_a_library
            
        "Đi cùng nhau {color=#66ff66}(An toàn){/color}":
            $ game_state.group_trust_level += 10
            # Staying together maintains trust
            jump scene2_branch_b_archive

# ============================================
# BRANCH A: LIBRARY (THƯ VIỆN)
# ============================================

label scene2_branch_a_library:
    scene bg library
    with fade
    
    show aoto at left
    show chie at right
    with dissolve
    
    "" "Minh và Lan bước vào thư viện tối tăm."
    "" "Ánh đèn pin rọi lên những giá sách bụi mờ."
    
    "" "Không khí lạnh lẽ đến kỳ lạ."
    "" "Những cuốn sách xếp ngăn nắp, như thể ai đó vừa sắp xếp lại."
    
    show chie closed frown
    "LAN" "Kỳ lạ... Nếu nơi này bị bỏ hoang, sao sách vẫn ngăn nắp thế này?"
    
    show aoto frown
    "MINH" "Có lẽ ai đó vẫn... sống ở đây?"
    
    "" "Một cơn gió lạnh thổi qua, khiến cả hai rùng mình."
    
    play sound "audio/book_fall.ogg"
    
    "" "Một cuốn sách rơi xuống đất, trang giở sẵn."
    "" "Không có ai ở gần. Cuốn sách tự rơi."
    
    show chie frown
    "LAN" "Minh, xem này!"
    
    "" "Lan nhặt cuốn sách lên, tay hơi run."
    
    "" "Đó là một trang nhật ký viết nguệch ngoạc:"
    show expression Solid("#0008") as overlay
    show text """{size=+5} {i} {color=#FFF000}
    Mai đang diễn kịch. Tôi biết. 
    Cô ta không yếu đuối như vẻ bề ngoài.{/color}{/i}{/size}""" at truecenter
    with dissolve
    pause 3.0
    hide text
    hide overlay
    show chie open
    "LAN" "Thấy chưa? Đây là bằng chứng!"
    "LAN" "Mai đang lừa dối chúng ta! Đi thôi!"
    
    show aoto closed frown
    "" "{i}Minh cảm thấy có gì đó không đúng...{/i}"
    "" "{i}Tại sao cuốn sách lại tự rơi xuống đúng lúc họ vào?{/i}"
    "" "{i}Quá tiện lợi. Quá... có dựng ý.{/i}"
    
    menu:
        "Tin ngay và rời đi {color=#ff8866}(Vội vàng){/color}":
            $ game_state.group_trust_level -= 20
            $ game_state.trust -= 1  # A1: Believing too quickly reduces trust
            "" "Minh và Lan vội vã rời khỏi thư viện."
            "" "{color=#9966ff}\Họ bỏ lỡ manh mối quan trọng..."
            jump scene2_reunite
            
        "Kiểm tra kỹ hơn {color=#66aaff}(Cẩn thận){/color}":
            $ game_state.group_trust_level += 5
            
            "MINH" "Khoan đã... Trang này trông quá... giả tạo."
            
            "" "Minh lật lại trang nhật ký, phát hiện một mảnh giấy nhỏ kẹp bên trong:"
            
            show expression Solid("#0008") as overlay
            show text "{size=+5}{color=#ffffff}\"Mọi bằng chứng là {color=#e34250}giả. \n{color=#ffffff}Tin tưởng là lối thoát duy nhất.\"{/color}" at truecenter
            with dissolve
            pause 4.0
            hide text
            hide expression overlay
            $ game_state.has_fake_evidence_note = True
            
            play sound "audio/item_get.ogg"
            centered """{color=#ffffff}\Đã nhận: \n {color=#00ff00}\Mảnh giấy 'Bằng chứng giả'{/color}"""
            
            "MINH" "Tớ hiểu rồi... Tất cả chỉ là bẫy để chia rẽ chúng ta."
            
            # Dead End Trap
            "" "Khi chuẩn bị rời đi, một cuốn sách phát sáng màu tím xuất hiện trên giá."
            "" "Nó rung rinh, như thể đang mời gọi..."
            
            scene bg library_aura
            
            show aoto at left
            show chie at pos4
            with dissolve
            
            "" "{color=#9966ff}Ánh sáng huyền bí tỏa ra từ cuốn sách...{/color}"
            
            menu:
                "{color=#9966ff}\"Đợi đã, cuốn sách kia phát sáng!\"{/color}":
                    # play sound "audio/curiosity.ogg" if renpy.loadable("audio/curiosity.ogg") else None
                
                    "" "Minh không cưỡng lại được sự tò mò."
                    "" "Anh chạm tay vào cuốn sách..."
                    
                    play sound "audio/dark_consume.ogg"
                    
                    scene bg library_blackhole
                    with flash
                    
                    "" "Cuốn sách nổ tung thành một hố đen khổng lồ!"
                    "" "Bóng tối cuộn xoáy, hút mọi thứ vào trong!"
                    
                    scene bg black
                    with dissolve
                    
                    "" "Cuốn sách hóa thành khói đen, nuốt chửng Minh!"
                    
                    "LAN" "MINH! KHÔNG!!!"
                    
                    jump bad_end_1_lost
                    
                "{color=#66ff66}\"Đi thôi, tớ có cảm giác không lành.\"{/color}":
                    $ game_state.group_trust_level += 10
                    # S2: Being cautious and avoiding trap
                    
                    "MINH" "Không, có gì đó sai sai. Chúng ta đi thôi."
                    
                    "" "Cả hai nhanh chóng rời khỏi thư viện."
                    
                    jump scene2_reunite

# ============================================
# BRANCH B: ARCHIVE ROOM (PHÒNG LƯU TRỮ)
# ============================================

label scene2_branch_b_archive:
    scene bg archive_room
    with fade
    
    show aoto at left_far
    show chie at left_center
    show sora at right_far
    show nora at right_center
    with dissolve
    
    "" "Cả nhóm cùng nhau bước vào phòng lưu trữ CLB."
    "" "Giá tài liệu xếp chồng lên nhau một cách lộn xộn."
    
    show nora frown
    "MAI" "Nơi này... tớ có cảm giác kỳ lạ."
    "MAI" "Như thể có ai đó vừa mới rời đi."
    
    show chie closed frown
    "LAN" "Đừng tưởng tượng. Tập trung tìm manh mối."
    
    show sora frown
    "TUẤN" "Tôi thấy có gì đó trên bàn kia..."
    
    "" "Cả nhóm tiến lại gần chiếc bàn làm việc cũ."
    "" "Bụi bặm dày cộm, nhưng có vài tài liệu trông mới hơn."
    
    play sound "audio/rumble.ogg"
    
    "" "Đột nhiên, căn phòng rung chuyển dữ dội!"
    "" "Trần nhà bắt đầu nứt ra, mảng tường rơi xuống!"
    
    show nora closed frown
    "MAI" "AAAAHHH!!!"
    
    show sora open
    "TUẤN" "Cẩn thận!"
    
    "" "Tuấn kéo Mai tránh một mảng vữa rơi xuống."
    
    show ghost_minion at center
    with dissolve
    
    play sound "audio/evil_laugh.ogg"
    
    "HỒN MA TAY SAI" "Hahaha... Thật vui!"
    "HỒN MA TAY SAI" "Chọn nhanh lên! Các ngươi chỉ có 10 giây!"
    "HỒN MA TAY SAI" "Chận quá... ta sẽ chôn sống các ngươi ở đây!"
    
    hide ghost_minion
    with dissolve
    
    "" "Trên bàn làm việc lộn xộn, có hai tài liệu nổi bật:"
    "" "1. CUỐN NHẬT KÝ BÌA ĐỎ - Đang mở sẵn, nét chữ đầy thù hận"
    "" "2. TẬP GIẤY GHI CHÚ CŨ NÁT - Toàn công thức dịch thuật khô khan"
    
    "" "Minh chỉ có thể cầm MỘT thứ trước khi chạy!"
    
    "" "{color=#ff4444}{b}Chọn nhanh! Thời gian không còn nhiều!{/b}{/color}"
    
    menu:
        "Chộp lấy {color=#ff6666}Cuốn Nhật Ký Bìa Đỏ{/color}":
            $ game_state.chose_red_diary = True
            $ game_state.group_trust_level -= 15
            $ game_state.authority -= 1  # B1: Taking emotional bait reduces authority
            
            play sound "audio/grab.ogg"
            
            "" "Minh túm lấy cuốn nhật ký và chạy theo nhóm!"
            
            scene bg old_corridor
            with fade
            
            "" "Cả nhóm chạy ra ngoài, thở hổn hển."
            
            "" "Minh mở cuốn nhật ký ra đọc:"
            
            show text "{i}\"Thằng bạn thân nhất đã đâm sau lưng tao...\nĐừng tin ai...\nTất cả đều muốn mày chết...\"{/i}" at truecenter
            with dissolve
            pause 3.0
            hide text
            
            "" "Những dòng chữ hoang tưởng khiến Minh càng thêm nghi ngờ."
            "" "Hạt giống hoài nghi đã được gieo vào tâm trí anh..."
            
            jump scene3_chemistry
            
        "Giật lấy {color=#66ff66}Tập Giấy Ghi Chú{/color}":
            $ game_state.has_translation_document = True
            $ game_state.group_trust_level += 20
            
            play sound "audio/grab.ogg"
            
            "" "Minh chộp lấy tập giấy cũ nát và lao ra ngoài!"
            
            scene bg old_corridor
            with fade
            
            "" "Cả nhóm an toàn. Minh mở tập giấy ra đọc lướt..."
            
            "" "Đây là bản dịch luật chơi gốc!"
            
            show text "{color=#00ff00}Quy tắc thứ 13:\nQuản Trò không phải trọng tài.\nQuản Trò là 'Người Chơi' ở vị thế quan sát.\nHắn sống bằng nỗi sợ.\n\nNếu các 'Vật Hiến Tế' từ chối giết nhau,\nQuản Trò sẽ vi phạm Giao Kèo\nvà buộc phải hiện nguyên hình.\n\nĐÓ LÀ LÚC HẮN CÓ THỂ BỊ GIẾT.{/color}" at truecenter
            with dissolve
            pause 5.0
            hide text
            
            play sound "audio/revelation.ogg"
            centered "{color=#00ff00}Đã nhận: Bản dịch Luật Chơi Gốc{/color}"
            
            "MINH" "Tớ hiểu rồi... Sự đoàn kết không chỉ giúp ta sống sót..."
            "MINH" "...mà còn là vũ khí để tiêu diệt con quỷ!"
            
            jump scene3_chemistry

label scene2_reunite:
    scene bg old_corridor
    with fade
    
    show aoto at left_far
    show chie at left_center
    show sora at right_center
    show nora at right_far
    with dissolve
    
    "" "Minh và Lan gặp lại Tuấn và Mai ở hành lang."
    "" "Cả hai trông có vẻ mệt mỏi và lo lắng."
    
    show nora frown
    "MAI" "Các cậu! Các cậu không sao chứ?"
    "MAI" "Tớ lo quá... tớ cứ nghĩ có chuyện gì xảy ra với các cậu..."
    
    show sora frown
    "TUẤN" "Các cậu tìm được gì không?"
    
    "" "Giọng Tuấn lạnh nhạt hơn bình thường."
    
    # Tuấn is upset about being left behind
    $ game_state.trust -= 1  # "Mày bỏ tụi tao lại" - reduces trust
    
    show sora closed frown
    "TUẤN" "Mày bỏ tụi tao lại."
    "TUẤN" "Nếu có chuyện gì xảy ra với Mai, mày tính sao?"
    
    show aoto frown
    "MINH" "Tuấn, tớ..."
    
    "TUẤN" "Thôi, không cần giải thích. Đã qua rồi."
    
    "" "Nhưng ánh mắt Tuấn cho thấy anh không quên."
    
    if game_state.has_fake_evidence_note:
        "MINH" "Có... nhưng không phải bằng chứng. Là một lời cảnh báo."
    else:
        "MINH" "Không có gì đáng tin cả. Đi tiếp thôi."
    
    # Door transition to next chapter
    call door_quick_transition
    
    jump scene3_chemistry

# ============================================
# SCENE 3: CHEMISTRY ROOM (PHÒNG HÓA HỌC)
# ============================================

label scene3_chemistry:
    scene bg chemistry_room
    with fade
    
    # "Phòng Hóa Học"
    
    "" "Cánh cửa duy nhất mở ra dẫn vào phòng Hóa Học."
    "" "Mùi axit nồng nặc làm cả nhóm phải bịt mũi."
    
    show aoto at left_far
    show chie at left_center
    show sora at right_center
    show nora at right_far
    with dissolve
    
    show chie frown
    "LAN" "Phòng thí nghiệm hóa học... Nhưng trông không giống bình thường."
    
    "" "Những lọ hóa chất xếp ngổn ngang trên kệ."
    "" "Một số đã đổ ra, ăn mòn mặt bàn."
    
    show nora closed frown
    "MAI" "Tớ có cảm giác không hay..."
    
    "" "Giữa phòng có một chiếc hộp kính chứa dung dịch sủi bọt."
    "" "Dung dịch màu xanh lục nhạt, bốc khói."
    "" "Bên trong có rết độc bò lổm ngổm."
    "" "Một chiếc chìa khóa vàng nằm dưới đáy."
    
    show sora frown
    "TUẤN" "Chìa khóa... Chúng ta cần nó để ra ngoài?"
    
    play sound "audio/countdown.ogg"
    
    play music "audio/tension.ogg"
    
    $ countdown_time = 30
    show screen countdown_timer(countdown_time)
    
    "Giọng nói bí ẩn" "{size=+5}Chọn vật hiến tế để lấy chìa khóa.{/size}"
    "Giọng nói bí ẩn" "{size=+5}Hết giờ, phòng sẽ bơm khí độc.{/size}"
    "Giọng nói bí ẩn" "{size=+5}Thời gian: 30 GIÂY.{/size}"
    
    show sora closed frown
    "TUẤN" "Cái quái gì vậy?! Ai dám thò tay vào đống axit đó?!"
    
    show chie closed frown
    "LAN" "Đ-đừng nhìn tôi! Tôi không làm đâu!"
    "LAN" "Tay tôi... tôi cần chúng để làm thí nghiệm!"
    
    show nora frown
    "MAI" "Chúng ta... chúng ta phải làm sao đây?"
    "MAI" "Nếu không lấy được chìa khóa, tất cả sẽ chết!"
    
    show sora frown
    "TUẤN" "Thế thì sao không cậu làm đi, Mai?"
    "TUẤN" "Cậu yếu nhất... cậu nên cống hiến một chút chứ!"
    
    show nora closed frown
    "MAI" "T-Tuấn?! Cậu nói vậy là sao?!"
    
    show chie frown
    "LAN" "Tuấn, bình tĩnh đi!"
    
    "" "Đồng hồ đếm ngược. 25 giây... 20 giây..."
    "" "Không khí căng thẳng đến nghẹt thở."
    
    "" "{i}{color=#ffaa00}Thời gian đang cạn kiệt... Minh phải quyết định ngay!{/color}{/i}"
    
    # Hide the countdown display timer
    hide screen countdown_timer
    
    # Initialize result variable and show timed choice screen
    $ _timed_choice_result = None
    call screen timed_choice_scene3(10)
    $ result = _timed_choice_result
    
    # If player runs out of time, default to hesitation (death)
    if result is None or result == "hesitate":
        $ game_state.group_trust_level -= 30
        # A: Hesitating leads to death - no variables matter here
        
        "" "Minh do dự, không thể đưa ra quyết định."
        "" "Thời gian trôi qua từng giây..."
        
        "" "30... 20... 10..."
        
        hide screen countdown_timer
        
        play sound "audio/timer_end.ogg"
        
        "" "{size=+30}{color=#fc2336}KHÔNG!!!"
        pause 1.5

        scene bg black
        with flash
        
        play sound "audio/gas.ogg"
        
        "" "Đồng hồ về 0."
        "" "Cửa phòng khóa chặt."
        "" "Khí gas độc phun ra từ các ống thông gió!"
        
        jump bad_end_2_gas_room
        
    elif result == "tuan":
        $ game_state.tuan_injury = True
        $ game_state.group_trust_level -= 20
        $ game_state.authority -= 2  # B: Assigning someone else reduces authority
        
        "MINH" "Tuấn... cậu là người mạnh nhất. Cậu phải làm việc này."
        
        "TUẤN" "CÁI GÌ?! Sao lại là tôi?!"
        
        "MINH" "Không còn thời gian! Nhanh lên!"
        
        "" "Tuấn nghiến răng, giận dữ nhìn Minh."
        "" "Anh ta thò tay vào hộp kính..."
        
        play sound "audio/acid_burn.ogg"
        
        "TUẤN" "AAAAAHHHHH!!!"
        
        "" "Bàn tay Tuấn bị bỏng nặng bởi axit!"
        "" "Nhưng anh ta đã lấy được chìa khóa."
        
        hide screen countdown_timer
        
        scene bg black
        with fade
        
        "" "Cửa phòng mở ra. Nhóm thoát ra ngoài."
        
        "" "Tuấn băng bó vết thương, ánh mắt căm hận nhìn Minh."
        "" "Hạt giống thù hận đã được gieo..."
        
        jump scene4_truth_hallway
        
    elif result == "lan":
        $ game_state.lan_injury = True
        $ game_state.group_trust_level -= 20
        $ game_state.authority -= 2  # B: Assigning someone else reduces authority
        
        "MINH" "Lan, cậu có bàn tay khéo léo nhất. Cậu làm được."
        
        "LAN" "TẠI SAO?! Sao không phải Mai?!"
        
        "MINH" "Lan, nhanh lên! Chúng ta không còn thời gian!"
        
        "" "Lan run rẩy, nước mắt chảy dài."
        "" "Cô thò tay vào hộp kính..."
        
        play sound "audio/acid_burn.ogg"
        
        "LAN" "AAAHHHH! ĐAU!!!"
        
        "" "Bàn tay Lan bị bỏng, da đỏ bừng."
        "" "Nhưng cô đã lấy được chìa khóa."
        
        hide screen countdown_timer
        
        scene bg black
        with fade
        
        "" "Cửa phòng mở. Nhóm chạy ra ngoài."
        
        "" "Lan khóc nức nở, nhìn Minh với ánh mắt oán hận."
        
        jump scene4_truth_hallway
        
    else:  # result == "minh"
        $ game_state.minh_injury = True
        $ game_state.group_trust_level += 30
        $ game_state.trust += 1  # C: Self-sacrifice increases trust
        $ game_state.guilt += 1  # Mai feels guilty
        
        "MINH" "Tớ không thể bắt ai làm điều này. Để tớ."
        
        "MAI" "Minh! Không!"
        
        "TUẤN" "Này, đừng có liều lĩnh!"
        
        "MINH" "Đừng bàn nữa!"
        
        "" "Minh không do dự, thò tay vào hộp kính."
        
        play sound "audio/acid_burn.ogg"
        
        "MINH" "Ghhh...!"
        
        "" "Axit ăn vào da tay, đau như cắt!"
        "" "Nhưng Minh cắn răng chịu đựng, túm lấy chìa khóa!"
        
        hide screen countdown_timer
        
        scene bg black
        with fade
        
        "" "Cửa mở ra. Minh choáng váng, được Tuấn đỡ."
        
        "TUẤN" "Cậu... thật sự điên rồi."
        
        "LAN" "Nhưng... cám ơn cậu."
        
        "MAI" "Minh... Tớ xin lỗi... Tại tớ mà cậu..."
        
        "" "Niềm tin trong nhóm tăng lên đáng kể."
        
        jump scene4_truth_hallway

# ============================================
# SCENE 4: HALLWAY OF TRUTH (HÀNH LANG SỰ THẬT)
# ============================================

label scene4_truth_hallway:
    scene bg mirror_hallway
    with fade
    
    # "Hành Lang Gương"
    
    "" "Một hành lang dài đầy gương."
    "" "Hàng trăm chiếc gương xếp dọc hai bên tường."
    "" "Hình ảnh phản chiếu không cử động, chỉ đứng yên cười quỷ dị."
    
    show aoto at left_far
    show chie at left_center
    show sora at right_center
    show nora at right_far
    with dissolve
    
    show nora closed frown
    "MAI" "Sao... sao hình ảnh trong gương lại khác với chúng ta?"
    
    show aoto frown
    "MINH" "Chúng đang cười... Nhưng chúng ta không cười."
    
    "GIỌNG NÓI QUẢN TRÒ" "Muốn đi tiếp, hãy thú nhận bí mật dơ bẩn nhất."
    "GIỌNG NÓI QUẢN TRÒ" "Những gì các ngươi giấu kín trong tâm hồn."
    "GIỌNG NÓI QUẢN TRÒ" "Nói dối, gương sẽ vỡ... và các ngươi sẽ chết."
    
    "" "Căn phòng im lặng đến rợn người."
    
    show chie frown
    "LAN" "Chúng ta... phải làm sao?"
    "LAN" "Nói thật mọi bí mật? Điều đó... có khác gì tự hủy hoại mình."
    
    show sora closed frown
    "TUẤN" "Không có lựa chọn nào khác."
    "TUẤN" "Hoặc chúng ta thật thà, hoặc chúng ta chết."
    
    "" "Một sự im lặng nặng nề bao trùm."
    
    # TUẤN's confession
    "" "Tuấn hít một hơi sâu, bước lên trước."
    "" "Anh nhìn vào gương, đối diện với chính mình."
    
    show sora frown at center
    with move
    "TUẤN" "Tôi... tôi đã hãm hại Lan."
    
    show chie closed frown
    "LAN" "Cái gì?!"
    
    "TUẤN" "Năm ngoái, tôi đã xóa email thông báo học bổng của cậu."
    "TUẤN" "Vì tôi ghen tị. Ghen tị với sự thông minh của cậu."
    "TUẤN" "Cậu luôn giỏi hơn tôi mọi thứ. Tôi ghét điều đó."
    "TUẤN" "Tôi xin lỗi..."
    
    $ game_state.tuan_confession = "sabotaged Lan's scholarship"
    
    show chie frown
    "LAN" "Tuấn... cậu..."
    "LAN" "Tôi đã mất cơ hội du học vì cậu!"
    
    "TUẤN" "Tôi biết. Và tôi hối hận mỗi ngày."
    
    play sound "audio/mirror_accept.ogg"
    
    "" "Gương phát sáng xanh, chấp nhận sự thật."
    "" "Tuấn thở phào nhẹ nhõm, nhưng khuôn mặt vẫn đầy tội lỗi."
    
    show sora at right_center
    with move
    
    # MAI's confession
    "" "Mai run rẩy, chân bước không vững."
    "" "Cô tiến lên trước gương."
    
    show nora frown at center
    with move
    "MAI" "Tớ... tớ có một bí mật."
    "MAI" "Tớ... tớ chỉ lợi dụng Tuấn."
    
    show sora closed frown
    "TUẤN" "...Mai?"
    
    "MAI" "Tớ không thích cậu. Chưa bao giờ."
    "MAI" "Tớ chỉ giả vờ yếu đuối để cậu bảo vệ tớ."
    "MAI" "Để tớ có người che chở. Để tớ không phải đối mặt mọi thứ một mình."
    "MAI" "Tớ... tớ xin lỗi, Tuấn."
    
    "TUẤN" "..."
    
    $ game_state.mai_confession = "used Tuấn for protection"
    
    play sound "audio/mirror_accept.ogg"
    
    "" "Gương lại sáng lên, chấp nhận lời thú tội."
    
    show nora at right
    with move
    
    # LAN's confession
    "" "Lan thở dài, bước ra."
    "" "Cô nhìn thẳng vào gương, mặt lạnh lùng."
    
    show chie closed frown at center
    with move
    "LAN" "Tôi coi tất cả các cậu... như vật thí nghiệm."
    
    show aoto frown
    "MINH" "Lan..."
    
    "LAN" "Tôi nghiên cứu hành vi của các cậu. Ghi chép lại phản ứng của các cậu."
    "LAN" "Tôi khinh thường trí tuệ của mọi người."
    "LAN" "Tôi nghĩ mình thông minh hơn tất cả."
    
    show chie frown
    "LAN" "Nhưng... ở đây, tôi nhận ra..."
    "LAN" "Sự thông minh chẳng có ý nghĩa gì nếu không có ai bên cạnh."
    "LAN" "Tôi... xin lỗi."
    
    $ game_state.lan_confession = "looked down on everyone"
    
    play sound "audio/mirror_accept.ogg"
    
    "" "Gương sáng lên, chấp nhận sự thật của Lan."
    
    show chie at left_center
    with move
    
    # MINH's turn
    "" "Cuối cùng đến lượt Minh."
    "" "Tất cả nhìn anh, chờ đợi."
    "" "Gương trước mặt anh sáng lên nhẹ, như đang sẵn sàng phán xét."
    
    "" "{i}Minh hít một hơi thật sâu. Đã đến lúc phải đối mặt với chính mình...{/i}"
    "" "{i}Anh phải thú nhận điều gì?{/i}"
    
    menu:
        "{color=#ff8866}Sự hèn nhát{/color} - \"Tớ muốn bỏ mặc các cậu\"":
            $ game_state.minh_confession = "wanted to abandon everyone"
            $ game_state.group_trust_level -= 10
            $ game_state.authority += 1  # Being honest increases authority
            
            "MINH" "Tớ... tớ đã nhiều lần nghĩ đến việc bỏ các cậu lại."
            "MINH" "Khi gặp nguy hiểm, tớ chỉ nghĩ đến việc tự cứu mình thôi."
            "MINH" "Tớ là một kẻ hèn nhát. Xin lỗi..."
            
        "{color=#66aaff}Sự đố kỵ{/color} - \"Tớ ghen tị với các cậu\"":
            $ game_state.minh_confession = "jealous of friends"
            $ game_state.group_trust_level -= 5
            $ game_state.authority += 1  # Being honest increases authority
            
            "MINH" "Tớ luôn ghen tị với các cậu."
            "MINH" "Lan thông minh, Tuấn mạnh mẽ, Mai được yêu quý..."
            "MINH" "Còn tớ? Tớ chỉ là người bình thường nhất."
            "MINH" "Tớ ghét điều đó. Xin lỗi..."
    
    play sound "audio/mirror_accept.ogg"
    
    "" "Tất cả các gương sáng lên."
    "" "Một cánh cửa hiện ra ở cuối hành lang."
    
    "" "Cả bốn người im lặng."
    "" "Bí mật xấu xa nhất của họ đã được phơi bày."
    "" "Nhưng họ vẫn đang sống."
    
    "MAI" "Chúng ta... đều không hoàn hảo."
    
    "LAN" "Đúng vậy. Nhưng chúng ta vẫn ở đây, cùng nhau."
    
    if game_state.group_trust_level > 0:
        $ game_state.group_trust_level += 20
        "" "Một cảm giác kỳ lạ lan toa trong nhóm."
        "" "Họ hiểu nhau hơn... và cũng tha thứ hơn."
    
    # Door transition to next chapter
    call door_quick_transition
    
    jump scene5_voting_room

# ============================================
# SCENE 5: VOTING ROOM (CĂN PHÒNG BỎ PHIẾU)
# ============================================

label scene5_voting_room:
    scene bg white_room
    with fade
    
    "Căn Phòng Trắng"
    
    "" "Một căn phòng trắng toát."
    "" "Không có cửa sổ, không có bóng tối, không có góc khuất."
    "" "Chỉ có sự trắng tinh tối, bao quát mọi thứ."
    
    show aoto at left_far
    show chie at left_center
    show sora at right_center
    show nora at right_far
    with dissolve
    
    "" "Giữa phòng là một chiếc hòm phiếu đen như mực."
    "" "Nó tương phản kỳ lạ với căn phòng trắng xung quanh."
    
    show nora frown
    "MAI" "Cái hòm đó... trông như quan tài."
    
    show sora frown
    "TUẤN" "Đừng nói xui quẩy!"
    
    "" "Bốn tờ giấy trắng và bốn cây bút đen xuất hiện trước mặt mỗi người."
    "" "Chúng bay lơ lửng trong không khí, chờ đợi."
    
    play sound "audio/gamemaster_voice.ogg"
    
    "GIỌNG NÓI QUẢN TRÒ" "{size=+15}QUY TẮC CUỐI CÙNG:{/size}"
    "GIỌNG NÓI QUẢN TRÒ" "Viết tên KẺ PHẢN BỘI vào giấy."
    "GIỌNG NÓI QUẢN TRÒ" "Nếu cả 4 tờ đều TRẮNG: Tất cả sống."
    "GIỌNG NÓI QUẢN TRÒ" "Nếu có TÊN: Người có nhiều phiếu nhất chết, 3 người còn lại về."
    
    "" "Một sự im lặng nặng nề bao trùm."
    
    scene bg white_room
    
    show aoto frown at left_far
    show chie frown at left_center
    show sora frown at right_center
    show nora frown at right_far
    with dissolve
    
    "" "Không khí căng thẳng đến tột độ."
    "" "Mỗi người nhìn nhau, rồi lại nhìn xuống tờ giấy trước mặt."
    
    show chie closed frown
    "LAN" "Nếu cả bốn tờ đều trắng... tất cả sống."
    "LAN" "Nhưng nếu chỉ một người viết tên..."
    
    show sora closed frown
    "TUẤN" "Thì người bị viết tên sẽ chết."
    "TUẤN" "Và ba người còn lại sẽ thoát."
    
    show nora closed frown
    "MAI" "Các cậu sẽ không viết tên tớ chứ?"
    "MAI" "Chúng ta đã hứa... tin tưởng nhau mà..."
    
    "" "Nhưng những lời thì thầm từ đầu trò chơi vẫn còn văng vẳng."
    "" "Mỗi người đều đã nghe thấy điều gì đó khác nhau."
    "" "Ai là kẻ mạo danh? Hay thực sự chẳng có ai?"
    
    if game_state.tuan_injury or game_state.lan_injury:
        "" "Vết thương từ phòng Hóa Học vẫn còn rát buốt."
        "" "Nỗi oán hận bắt đầu tràn ra."
        
        show sora closed frown
        "TUẤN" "Chúng ta... chúng ta phải hy sinh một người."
        
        show chie closed frown
        "LAN" "Đúng vậy. Nếu không, tất cả sẽ chết."
        
        show nora closed frown
        "MAI" "Nhưng... nhưng ai?"
        
        "Tuấn và Lan nhìn Mai."
        
        "TUẤN" "Mai... cậu là người yếu nhất."
        
        "LAN" "Logic cho thấy... hy sinh Mai là lựa chọn tối ưu."
        
        "MAI" "K-không... Đừng...!"
        
        show aoto open
        "MINH" "Đợi đã!"
    else:
        show chie frown
        "LAN" "Chúng ta nên làm gì?"
        
        show sora closed frown
        "TUẤN" "Tôi... tôi không biết."
        
        show nora frown
        "MAI" "Minh, cậu quyết định đi."
    
    "" "{i}{color=#ffffff}Đây là khoảnh khắc quyết định... Số phận của cả nhóm nằm trong tay Minh.{/color}{/i}"
    
    menu:
        "Đồng ý viết tên Mai {color=#ff4444}(Phản bội){/color}":
            jump normal_end_a_black_ink
            
        "Nộp giấy trắng và thuyết phục mọi người {color=#66ff66}(Tin tưởng){/color}":
            jump persuasion_attempt

label persuasion_attempt:
    "MINH" "KHÔNG! Chúng ta không được làm vậy!"
    
    "TUẤN" "Nhưng chúng ta sẽ chết!"
    
    "MINH" "Không! Tất cả những gì chúng ta thấy, tất cả bằng chứng..."
    
    if game_state.has_fake_evidence_note:
        "MINH" "...đều là GIẢ! Tớ đã tìm thấy mảnh giấy cảnh báo!"
        "MINH" "Tin tưởng nhau là lối thoát duy nhất!"
        
        $ game_state.group_trust_level += 30
        
        "LAN" "Nhưng..."
        
        "MINH" "Lan, cậu là người thông minh. Hãy suy nghĩ!"
        "MINH" "Nếu thực sự có kẻ mạo danh, chúng đã giết chúng ta từ lâu rồi!"
        "MINH" "Đây chỉ là trò chơi tâm lý!"
        
        if game_state.group_trust_level >= 30:
            jump persuasion_success
        else:
            jump persuasion_failure
            
    elif game_state.has_translation_document:
        "MINH" "...đều là bẫy! Tớ đã đọc bản dịch luật chơi!"
        "MINH" "Con quỷ đó cần chúng ta giết nhau để sống!"
        "MINH" "Nếu chúng ta đoàn kết, hắn sẽ thua!"
        
        $ game_state.group_trust_level += 40
        
        jump persuasion_success
        
    else:
        "MINH" "Tớ cảm thấy... chúng ta đang bị lừa!"
        
        $ game_state.group_trust_level += 10
        
        "TUẤN" "Cảm thấy? Cậu đang đùa à?!"
        
        "LAN" "Không có bằng chứng gì cả!"
        
        # Without evidence, requires higher trust/authority
        if game_state.trust >= 2 and game_state.authority >= 2:
            jump persuasion_success
        else:
            jump persuasion_failure

label persuasion_success:
    $ game_state.group_trust_level += 20
    
    "LAN" "...Cậu nói đúng."
    
    "TUẤN" "Cái gì?"
    
    "LAN" "Minh nói đúng. Tất cả những manh mối đều quá... hoàn hảo."
    "LAN" "Như thể có ai đó cố tình sắp đặt."
    
    "MAI" "Vậy... chúng ta làm gì?"
    
    "MINH" "Chúng ta cùng nộp giấy trắng. Tin tưởng nhau."
    
    if game_state.minh_injury:
        "TUẤN" "Cậu đã hy sinh vì chúng tôi. Tôi tin cậu."
    
    "LAN" "...Được rồi. Tôi tin."
    
    "MAI" "Tớ cũng vậy!"
    
    play sound "audio/paper_write.ogg"
    
    "Cả bốn người cùng nộp tờ giấy trắng vào hòm phiếu."
    
    # Door transition to final chapter
    call door_quick_transition
    
    jump scene6_confrontation

label persuasion_failure:
    "TUẤN" "KHÔNG! Tôi không chấp nhận rủi ro!"
    
    "LAN" "Tôi cũng vậy!"
    
    play sound "audio/paper_write.ogg"
    
    "Tuấn và Lan viết tên Mai."
    
    "MAI" "Không... KHÔNG!!!"
    
    "" "{i}{color=#ffcc00}Đây là cơ hội cuối cùng của Minh...{/color}{/i}"
    
    menu:
        "Viết tên Mai {color=#ff4444}(Cứu bản thân){/color}":
            jump normal_end_a_black_ink
            
        "Vẫn nộp giấy trắng {color=#66ff66}(Giữ nguyên tắc){/color}":
            jump normal_end_b_cracked

# ============================================
# SCENE 6: CONFRONTING THE EVIL (ĐỐI MẶT ÁC QUỶ)
# ============================================

label scene6_confrontation:
    scene bg white_room
    
    show aoto at left_far
    show chie at left_center
    show sora at right_center
    show nora at right_far
    with dissolve
    
    play sound "audio/ballot_open.ogg"
    
    "" "Hòm phiếu từ từ mở ra."
    "" "Bốn tờ giấy trắng bay lên."
    
    show sora open
    "TUẤN" "Chúng ta... thắng rồi?"
    
    play sound "audio/rumble.ogg"
    
    "" "Nhưng thay vì cánh cửa mở ra..."
    "" "Căn phòng rung chuyển dữ dội!"
    
    hide aoto
    hide chie
    hide sora
    hide nora
    with dissolve
    
    scene bg black
    with flash
    
    play sound "audio/blood_drip.ogg"
    
    "Máu chảy từ trần nhà xuống!"
    
    show gamemaster at center
    with dissolve
    
    play music "audio/boss_theme.ogg"
    
    "" "Một bóng đen khổng lồ hiện ra từ hư không."
    "" "Khuôn mặt không rõ ràng, chỉ có nụ cười rộng đến tai."
    
    "QUẢN TRÒ" "{size=+20}{color=#ff0000}LŨ NGU NGỐC!{/color}{/size}"
    "QUẢN TRÒ" "Ta đã cho các ngươi cơ hội tìm ra kẻ mạo danh!"
    "QUẢN TRÒ" "Nhưng các ngươi lại chọn... tin tưởng nhau?"
    
    "" "Tiếng cười vang vọng khắp căn phòng."
    
    "QUẢN TRÒ" "Giấy trắng nghĩa là KHÔNG TÌM RA AI!"
    "QUẢN TRÒ" "TẤT CẢ PHẠM LUẬT! CHẾT ĐI!!!"
    
    "" "Bóng tối bắt đầu bò ra từ góc phòng."
    "" "Nó cuộn lại, sẵn sàng nuốt chửng cả nhóm."
    
    # Check for key items
    if game_state.has_fake_evidence_note:
        jump true_end_path_1
    elif game_state.has_translation_document:
        jump true_end_path_2
    else:
        jump bad_end_chaos

label true_end_path_1:
    show aoto at left_far
    show chie at left_center
    show sora at right_center
    show nora at right_far
    with dissolve
    
    "" "Bóng tối đang tiến lại gần."
    "" "Mọi người lùi lại, sợ hãi."
    
    "" "Nhưng Minh bước lên phía trước."
    
    show aoto open
    "MINH" "KHOAN!"
    
    "" "Giọng anh vang lên mạnh mẽ, đầy quyết tâm."
    "" "Bóng tối dừng lại, như thể đang ngạc nhiên."
    
    "QUẢN TRÒ" "Hmm? Ngươi còn muốn nói gì?"
    
    "MINH" "Trong chúng tôi không ai là kẻ mạo danh!"
    "MINH" "Tất cả bằng chứng đều là giả!"
    
    "QUẢN TRÒ" "Vậy thì sao?! Các ngươi vẫn phạm luật!"
    
    "MINH" "Không!"
    "MINH" "Vậy thì chỉ còn một đáp án..."
    
    "" "Minh rút mảnh giấy cảnh báo ra."
    "" "Mảnh giấy mà anh đã tìm được trong thư viện."
    "" "Nó phát ra ánh sáng nhẹ trong tay anh."
    
    "MINH" "{size=+15}NGƯƠI MỚI LÀ KẺ MẠO DANH, QUẢN TRÒ!{/size}"
    
    "QUẢN TRÒ" "...!!!"
    
    show chie open
    "LAN" "Đúng rồi! Ngươi là người chơi thứ 5!"
    
    show sora open
    "TUẤN" "Ngươi giả làm trọng tài để lừa chúng tôi giết nhau!"
    
    play sound "audio/paper_write.ogg"
    
    "Minh viết 'QUẢN TRÒ' lên tờ giấy và ném vào hòm phiếu."
    
    jump true_ending_dawn

label true_end_path_2:
    show aoto at left_far
    show chie at left_center
    show sora at right_center
    show nora at right_far
    with dissolve
    
    "" "Bóng tối đang tiến lại gần, sẵn sàng nuốt chửng mọi người."
    "" "Nhưng Minh không hề sợ hãi."
    
    show aoto open
    "MINH" "Mày định dọa ai?"
    
    "" "Minh giơ tập giấy ghi chú cũ nát lên."
    "" "Nó phát ra ánh sáng vàng nhạt, đẩy lùi bóng tối."
    
    "MINH" "Tao đã đọc bản dịch GỐC của nghi thức này rồi!"
    
    "QUẢN TRÒ" "Cái gì...?! Làm sao ngươi có được...?!"
    
    "MINH" "Mày nói bọn tao phạm luật? SAI!"
    "MINH" "Luật nói: 'Kẻ thua cuộc phải chết'."
    "MINH" "Nhưng khi cả 4 tờ đều trắng, KHÔNG AI THUA!"
    
    "" "Quản Trò lùi lại, vẻ mặt bắt đầu hoảng loạn."
    
    show chie open
    "LAN" "Đợi đã... Tôi hiểu rồi!"
    "LAN" "Nếu không có người chơi nào thua..."
    "LAN" "...thì kẻ duy nhất thất bại trong việc duy trì trò chơi..."
    "LAN" "...là MÀY - QUẢN TRÒ!"
    
    show nora open
    "MAI" "Hắn là người chơi thứ 5! Giả làm trọng tài!"
    
    show aoto smile
    "MINH" "Quy tắc thứ 13: Khi Quản Trò thất bại, hắn sẽ mất quyền năng!"
    "MINH" "Mày không phải thần thánh. Mày chỉ là KÝ SINH TRÙNG!"
    "MINH" "Sống dựa vào nỗi sợ của chúng tao!"
    
    show sora smile
    "TUẤN" "Và giờ bọn tao sẽ nghiền nát mày!"
    
    "" "Cả bốn người cùng đứng lên, đối mặt với Quản Trò."
    "" "Sự đoàn kết của họ tạo thành một bức tường vô hình."
    
    play sound "audio/paper_write.ogg"
    
    "Minh viết 'QUẢN TRÒ' vào phiếu và ném vào hòm."
    
    jump true_ending_dawn

# ============================================
# ENDINGS
# ============================================

# BAD END 1: LOST IN LIBRARY
label bad_end_1_lost:
    scene bg black
    
    play music "audio/sad_theme.ogg"
    
    centered "{size=+20}{color=#ff0000}BAD ENDING 1{/color}{/size}"
    centered "{size=+10}KẺ LẠC LỐI{/size}"
    
    pause 2.0
    
    centered "Minh đã biến mất trong bóng tối."
    centered "Lan gào thét tìm kiếm nhưng không thấy dấu vết."
    centered "Cả nhóm không bao giờ thoát ra được..."
    
    pause 3.0
    
    return

# BAD END 2: GAS ROOM
label bad_end_2_gas_room:
    scene bg black
    
    play music "audio/sad_theme.ogg"
    
    centered "{size=+20}{color=#ff0000}BAD ENDING 2{/color}{/size}"
    centered "{size=+10}CĂN PHÒNG HƠI NGẠT{/size}"
    
    pause 2.0
    
    centered "Sự do dự đã giết chết cả nhóm."
    centered "Họ ngã xuống một cách vô vọng trong khói độc."
    centered "Không ai sống sót."
    
    pause 3.0
    
    return

# NORMAL END A: BLACK INK
label normal_end_a_black_ink:
    scene bg white_room
    
    play sound "audio/paper_write.ogg"
    
    "" "Minh run rẩy viết tên 'Mai' vào giấy."
    
    "MAI" "Minh...? Cậu... cậu làm gì vậy?"
    
    "" "Cả bốn người nộp phiếu."
    
    play sound "audio/ballot_open.ogg"
    
    "" "Hòm phiếu mở ra: 3 phiếu 'Mai'. 1 phiếu trắng."
    
    "MAI" "Không... các cậu..."
    
    scene bg black
    with flash
    
    play sound "audio/scream.ogg"
    
    "" "Mai biến mất trong tiếng thét."
    
    scene bg club_room
    with fade
    
    "" "Ba người còn lại tỉnh lại trong phòng CLB."
    "" "Họ sống sót."
    "" "Nhưng Mai không còn đó."
    
    play music "audio/melancholic.ogg"
    
    centered "{size=+20}{color=#ffaa00}NORMAL ENDING A{/color}{/size}"
    centered "{size=+10}GIỌT MỰC ĐEN{/size}"
    
    pause 2.0
    
    "" "Cả ba người không bao giờ nói chuyện với nhau nữa."
    "" "Họ sống trong day dứt suốt đời."
    "" "Giọt mực đen đó... không bao giờ tẩy sạch."
    
    pause 3.0
    
    return

# NORMAL END B: CRACKED
label normal_end_b_cracked:
    scene bg white_room
    
    play sound "audio/paper_write.ogg"
    
    "" "Minh nộp giấy trắng."
    "" "Nhưng Tuấn và Lan đã viết 'Mai'."
    
    play sound "audio/ballot_open.ogg"
    
    "" "Hòm mở: 2 phiếu 'Mai'. 2 phiếu trắng."
    
    "" "Mai có số phiếu cao nhất."
    
    scene bg black
    with flash
    
    play sound "audio/scream.ogg"
    
    "MAI" "MINH! CỨU TỚ!!!"
    
    "Nhưng đã quá muộn. Mai biến mất."
    
    scene bg club_room
    with fade
    
    play music "audio/melancholic.ogg"
    
    centered "{size=+20}{color=#ffaa00}NORMAL ENDING B{/color}{/size}"
    centered "{size=+10}RẠN NỨT{/size}"
    
    pause 2.0
    
    "" "Ba người tỉnh lại."
    "" "Minh nhìn Tuấn và Lan với ánh mắt căm phẫn."
    
    "MINH" "Các cậu... đã giết Mai."
    
    "" "Tình bạn tan vỡ hoàn toàn."
    "" "Họ không bao giờ gặp lại nhau nữa."
    
    pause 3.0
    
    return

# BAD END: CHAOS
label bad_end_chaos:
    scene bg black
    with flash
    
    play sound "audio/darkness.ogg"
    
    "Không có manh mối, Minh không biết phải làm gì."
    "Bóng tối nuốt chửng cả nhóm."
    
    play music "audio/sad_theme.ogg"
    
    centered "{size=+20}{color=#ff0000}BAD ENDING{/color}{/size}"
    centered "{size=+10}SỰ HỖN LOẠN{/size}"
    
    pause 2.0
    
    centered "Họ không tìm ra lối thoát."
    centered "Tất cả đều biến mất trong bóng tối."
    
    pause 3.0
    
    return

# TRUE ENDING: DAWN
label true_ending_dawn:
    scene bg white_room
    
    play sound "audio/fire_burn.ogg"
    
    "" "Hòm phiếu bốc cháy dữ dội!"
    
    show gamemaster at center
    
    "QUẢN TRÒ" "{size=+20}KHÔNG! CÁC NGƯƠI... AAAAAHHHHH!!!{/size}"
    
    hide gamemaster
    with dissolve
    
    play sound "audio/explosion.ogg"
    
    scene bg white
    with flash
    
    "" "Ánh sáng chói lọi!"
    
    scene bg club_room
    with fade
    
    show aoto at left_far
    show chie at left_center
    show sora at right_center
    show nora at right_far
    with dissolve
    
    play music "audio/peaceful.ogg"
    
    "" "Cả bốn người từ từ tỉnh lại."
    "" "Họ đang nằm trong phòng CLB."
    
    "" "Đồng hồ treo tường chỉ 11:05 PM."
    "" "Chỉ mới 5 phút kể từ khi bắt đầu nghi thức."
    
    show sora open
    "TUẤN" "Chúng ta... sống sót?"
    
    show chie smile
    "LAN" "Có vẻ vậy."
    
    show nora smile
    "MAI" "Minh... cám ơn cậu."
    
    show aoto smile
    "MINH" "Không. Cám ơn tất cả các cậu."
    "MINH" "Chúng ta đã tin tưởng nhau."
    
    "" "Họ ngồi im lặng một lúc."
    "" "Những bí mật đã được phơi bày."
    "" "Những vết thương đã được tạo ra."
    
    show chie frown
    "LAN" "Chúng ta... vẫn là bạn chứ?"
    
    show sora closed smile
    "TUẤN" "Tôi muốn vậy. Nếu các cậu tha thứ cho tôi."
    
    show nora closed smile
    "MAI" "Tớ cũng xin lỗi. Xin lỗi tất cả."
    
    show aoto smile
    "MINH" "Chúng ta không hoàn hảo. Nhưng chúng ta vẫn ở đây."
    "MINH" "Và đó là điều quan trọng nhất."
    
    hide aoto
    hide chie
    hide sora
    hide nora
    with dissolve
    
    scene bg dawn_sky
    with fade
    
    "" "Bên ngoài cửa sổ, bình minh đang dần ló rạng."
    
    centered "{size=+30}{color=#ffff00}TRUE ENDING{/color}{/size}"
    centered "{size=+20}BÌNH MINH{/size}"
    
    pause 3.0
    
    centered "Họ chấp nhận quá khứ xấu xí của nhau."
    centered "Họ chọn tha thứ."
    centered "Họ chọn tin tưởng."
    
    pause 2.0
    
    centered "Và họ bước vào một ngày mới."
    centered "Cùng nhau."
    
    pause 3.0
    
    return
