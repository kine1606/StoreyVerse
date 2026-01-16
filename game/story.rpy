# SỰ PHẢN BỘI - VISUAL NOVEL GAME
# Story Script

# ============================================
# CHARACTER TRANSFORMS (Scale & Position)
# ============================================
transform ghost_base:
    zoom 0.75

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
    xalign 0.6

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
            self.Minh_injury = False
            self.tuan_injury = False
            self.Lan_injury = False
            self.tuan_confession = ""
            self.Mai_confession = ""
            self.Lan_confession = ""
            self.Minh_confession = ""
            
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
    # jump normal_end_b_cracked
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
    
    # Tuấn speaks
    show sora at left
    with dissolve
    "Tuấn" "Tớ vẫn không tin được là chúng ta đang làm chuyện này."
    "Tuấn" "Nhỡ có con gì hiện ra thật thì sao?"
    
    # Lan speaks
    show chie at right
    with dissolve
    "Lan" "Thống kê cho thấy 99%% các nghi thức gọi hồn chỉ là ảo giác nhóm."
    "Lan" "Cứ xem như trải nghiệm tâm lý đi."
    
    show sora frown
    "Tuấn" "Cậu và cái kiểu nói chuyện khoa học đó..."
    "Tuấn" "Không phải mọi thứ đều giải thích được bằng số liệu đâu!"
    
    show chie frown
    "Lan" "Chính xác là mọi thứ ĐỀU có thể giải thích bằng khoa học."
    "Lan" "Chỉ là chúng ta chưa tìm ra cách thôi."
    
    # Mai speaks
    hide sora
    with dissolve
    show nora at left
    with dissolve
    "Mai" "Các cậu ơi... đừng cãi nhau nữa."
    "Mai" "Nhưng... từ lúc vào đây tớ đã thấy lạnh sống lưng rồi."
    
    show nora frown
    "Mai" "Các cậu có thấy không? Cái bóng tối ở góc kia... nó như đang nhìn chúng ta."
    
    hide nora
    hide chie
    with dissolve
    
    "" "Tất cả quay lại nhìn góc phòng tối đó."
    "" "Không có gì cả. Chỉ là bóng tối."
    "" "Hay là... có?"
    
    # Minh speaks
    hide chie
    hide nora
    with dissolve
    show aoto at center
    with dissolve
    "Minh" "Thôi nào các cậu. Đừng dọa nhau nữa."
    "Minh" "Chỉ là đọc vài câu cho vui thôi."
    
    show aoto smile
    "Minh" "Hơn nữa, nếu có ma thật thì chúng ta có bốn người cơ mà!"
    "Minh" "Để tớ đọc câu cuối cùng nhé."
    
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
    
    centered "{color=#ff0000}Minh nghe thấy:{/color}\n\"Trong số các ngươi, có một kẻ đã bị chiếm xác.\""
    
    centered "{color=#ff0000}Lan nghe thấy:{/color}\n\"Đừng tin ai cả. Một người trong nhóm không còn là chính mình nữa.\""
    
    centered "{color=#ff0000}Tuấn nghe thấy:{/color}\n\"Là Mai. Nó đang giả vờ yếu đuối. Hãy cẩn thận.\""
    
    centered "{color=#ff0000}Mai nghe thấy:{/color}\n\"Bọn họ đang nghi ngờ ngươi. Ngươi sẽ bị bỏ lại.\""
    
    "" "Bốn người nhìn nhau, hoảng loạn."
    "" "Mỗi người đều có một bí mật mà họ không dám nói ra."
    
    scene bg club_room
    with flash
    
    "" "Khi ánh sáng trở lại, cánh cửa phòng đã biến mất."
    "" "Thay vào đó là một cổng sắt rỉ máu với dòng chữ khắc sâu:"
    show expression Solid("#0008") as overlay
    show text "{size=+20}{color=#ff0000}TRÒ CHƠI BẮT ĐẦU\nTÌM RA KẺ MẠO DANH ĐỂ SỐNG SÓT{/color}{/size}" at truecenter
    with dissolve
    pause 3.0
    hide text
    hide overlay
    # Door transition to next chapter
    call door_quick_transition
    
    jump scene2_corridor

# ============================================
# SCENE 2: MAZE OF CLUES (MÊ CUNG MANH MỐI)
# ============================================

label scene2_corridor:
    scene bg old_corridor
    with fade
    
    "" "Hành Lang trường học cũ nát"
    
    "" "Căn hành Lang ẩm mốc, vách tường bong tróc."
    "" "Mùi mốc nồng nặc khiến cả nhóm khó thở."
    "" "Những bóng đèn huỳnh quang nhấp nháy yếu ớt trên trần nhà."
    
    show nora frown at right
    with dissolve
    "Mai" "Chỗ này... tại sao nó lại giống trường của chúng ta thế?"
    "Mai" "Nhưng mà... cũ hơn. Rất nhiều."
    
    show aoto at left
    with dissolve
    "Minh" "Không chỉ cũ. Nó như thể đã bị bỏ hoang hàng chục năm."
    
    hide nora
    hide aoto
    with dissolve
    
    show chie at right
    with dissolve
    "Lan" "Chúng ta cần thông tin. Nếu có kẻ mạo danh, phải có manh mối."
    "Lan" "Nên tìm kiếm có hệ thống. Chia ra để kiểm tra nhiều nơi hơn."
    
    show sora at left
    with dissolve
    "Tuấn" "Chia ra sẽ nhanh hơn. Minh và Lan vào thư viện. Tôi trông Mai ở phòng y tế."
    
    show chie frown at right
    "Lan" "Sao cậu lại muốn đi với Mai?"
    
    show sora frown at left
    "Tuấn" "Cô ấy yếu nhất. Ai đó phải bảo vệ cô ấy."
    
    show chie closed frown at right 
    "Lan" "Hay là cậu muốn giám sát cô ấy?"
    
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
            # Staying together Maintains trust
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
    "Lan" "Kỳ lạ... Nếu nơi này bị bỏ hoang, sao sách vẫn ngăn nắp thế này?"
    
    show aoto frown
    "Minh" "Có lẽ ai đó vẫn... sống ở đây?"
    
    "" "Một cơn gió lạnh thổi qua, khiến cả hai rùng mình."
    
    play sound "audio/book_fall.ogg"
    
    "" "Một cuốn sách rơi xuống đất, trang giở sẵn."
    "" "Không có ai ở gần. Cuốn sách tự rơi."
    
    show chie frown
    "Lan" "Minh, xem này!"
    
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
    "Lan" "Thấy chưa? Đây là bằng chứng!"
    "Lan" "Mai đang lừa dối chúng ta! Đi thôi!"
    
    show aoto closed frown
    "" "{i}Minh cảm thấy có gì đó không đúng...{/i}"
    "" "{i}Tại sao cuốn sách lại tự rơi xuống đúng lúc họ vào?{/i}"
    "" "{i}Quá tiện lợi. Quá... có dụng ý.{/i}"
    
    menu:
        "Tin ngay và rời đi {color=#ff8866}(Vội vàng){/color}":
            $ game_state.group_trust_level -= 20
            $ game_state.trust -= 1  # A1: Believing too quickly reduces trust
            "" "Minh và Lan vội vã rời khỏi thư viện."
            "" "{color=#9966ff}\Họ bỏ lỡ manh mối quan trọng..."
            jump scene2_reunite
            
        "Kiểm tra kỹ hơn {color=#66aaff}(Cẩn thận){/color}":
            $ game_state.group_trust_level += 5
            
            "Minh" "Khoan đã... Trang này trông quá... giả tạo."
            
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
            
            "Minh" "Tớ hiểu rồi... Tất cả chỉ là bẫy để chia rẽ chúng ta."
            
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
                    
                    "Lan" "Minh! KHÔNG!!!"
                    
                    jump bad_end_1_lost
                    
                "{color=#66ff66}\"Đi thôi, tớ có cảm giác không lành.\"{/color}":
                    $ game_state.group_trust_level += 10
                    # S2: Being cautious and avoiding trap
                    
                    "Minh" "Không, có gì đó sai sai. Chúng ta đi thôi."
                    
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
    "Mai" "Nơi này... tớ có cảm giác kỳ lạ."
    "Mai" "Như thể có ai đó vừa mới rời đi."
    
    show chie closed frown
    "Lan" "Đừng tưởng tượng. Tập trung tìm manh mối."
    
    show sora frown
    "Tuấn" "Tôi thấy có gì đó trên bàn kia..."
    
    "" "Cả nhóm tiến lại gần chiếc bàn làm việc cũ."
    "" "Bụi bặm dày cộm, nhưng có vài tài liệu trông mới hơn."
    
    play sound "audio/rumble.ogg"
    
    "" "Đột nhiên, căn phòng rung chuyển dữ dội!"
    "" "Trần nhà bắt đầu nứt ra"
    
    show nora closed frown
    "Mai" "AAAAHHH!!!"
    
    show sora open
    "Tuấn" "Cẩn thận!"
    
    "" "Tuấn kéo Mai tránh khỏi một mảng tường lớn đang rơi xuống."

    show expression Solid("#00000f") as overlay
    show text "{size=+10}Căn phòng bỗng mất điện, một giọng nói vang lên" at truecenter as wtf
    pause(1.0)
    hide wtf with dissolve
    
    show ghost_minion at ghost_base
    with dissolve
    
    play sound "audio/evil_laugh.ogg"
    
    "Nữ sinh bí ẩn" "Hahaha... Thật vui!"
    "Nữ sinh bí ẩn" "Chọn nhanh lên! Các ngươi chỉ có 10 giây!"
    "Nữ sinh bí ẩn" "Chận quá... ta sẽ chôn sống các ngươi ở đây!"
    
    hide ghost_minion
    with dissolve
    hide overlay
    "" "Trên bàn làm việc lộn xộn, có hai tài liệu nổi bật:"
    "" "CUỐN NHẬT KÝ BÌA ĐỎ - Đang mở sẵn, nét chữ đầy thù hận"
    "" "TẬP GIẤY GHI CHÚ CŨ NÁT - Toàn công thức dịch thuật khô khan"
    
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
            
            show text "{i}\"Thằng bạn thân nhất đã đâm sau lưng tao... Đừng tin ai...\nTất cả đều muốn mày chết...\"{/i}" at truecenter
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
            
            "" "{color=#901ec9}Quy tắc thứ 13 ghi như sau:"
            "" " \"Ta là người ở vị thế quan sát. Ta sống bằng {color=#901ec9}nỗi sợ.\""
            "" "Nếu các {color=#901ec9}'Vật Hiến Tế'{/color} từ chối giết nhau, sẽ vi phạm giao kèo quỷ dữ và buộc phải hiện nguyên hình"
            "" "{size=+10}ĐÓ LÀ LÚC KẾT THÚC."
            with dissolve
            pause 2.0
            hide text
            
            play sound "audio/revelation.ogg"
            centered "{color=#00ff00}Đã nhận: \nBản dịch Luật chơi gốc{/color}"
            
            "Minh" "Tớ hiểu rồi... Sự đoàn kết không chỉ giúp ta sống sót..."
            "Minh" "...mà còn là vũ khí để tiêu diệt con quỷ!"
            
            jump scene3_chemistry

label scene2_reunite:
    scene bg old_corridor
    with fade
    
    show aoto at left_far
    show chie at left_center
    show sora at right_center
    show nora at right_far
    with dissolve
    
    "" "Minh và Lan gặp lại Tuấn và Mai ở hành Lang."
    "" "Cả hai trông có vẻ mệt mỏi và lo lắng."
    
    show nora frown
    "Mai" "Các cậu! Các cậu không sao chứ?"
    "Mai" "Tớ lo quá... tớ cứ nghĩ có chuyện gì xảy ra với các cậu..."
    
    show sora frown
    "Tuấn" "Các cậu tìm được gì không?"
    
    "" "Giọng Tuấn lạnh nhạt hơn bình thường."
    
    # Tuấn is upset about being left behind
    $ game_state.trust -= 1  # "Mày bỏ tụi tao lại" - reduces trust
    
    show sora closed frown
    "Tuấn" "Mày bỏ tụi tao lại."
    "Tuấn" "Nếu có chuyện gì xảy ra với Mai, mày tính sao?"
    
    show aoto frown
    "Minh" "Tuấn, tớ..."
    
    "Tuấn" "Thôi, không cần giải thích. Đã qua rồi."
    
    "" "Nhưng ánh mắt Tuấn cho thấy anh không quên."
    
    if game_state.has_fake_evidence_note:
        "Minh" "Có... nhưng không phải bằng chứng. Là một lời cảnh báo."
    else:
        "Minh" "Không có gì đáng tin cả. Đi tiếp thôi."
    
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
    "Lan" "Phòng thí nghiệm hóa học... Nhưng trông không giống bình thường."
    
    "" "Những lọ hóa chất xếp ngổn ngang trên kệ."
    "" "Một số đã đổ ra, ăn mòn mặt bàn."
    
    show nora closed frown
    "Mai" "Tớ có cảm giác không hay..."
    
    "" "Giữa phòng có một chiếc hộp kính chứa dung dịch sủi bọt."
    "" "Dung dịch màu xanh lục nhạt, bốc khói."
    "" "Bên trong có rết độc bò lổm ngổm."
    "" "Một chiếc chìa khóa vàng nằm dưới đáy."
    
    show sora frown
    "Tuấn" "Chìa khóa... Chúng ta cần nó để ra ngoài?"
    
    play sound "audio/countdown.ogg"
    
    play music "audio/tension.ogg"
    
    "Giọng nói bí ẩn" "{size=+5}Chọn vật hiến tế để lấy chìa khóa.{/size}"
    "Giọng nói bí ẩn" "{size=+5}Hết giờ, phòng sẽ bơm khí độc.{/size}"
    "Giọng nói bí ẩn" "{size=+5}Thời gian: 30 GIÂY.{/size}"
    
    show sora closed frown
    "Tuấn" "Cái quái gì vậy?! Ai dám thò tay vào đống axit đó?!"
    
    show chie closed frown
    "Lan" "Đ-đừng nhìn tôi! Tôi không làm đâu!"
    "Lan" "Tay tôi... tôi cần chúng để làm thí nghiệm!"
    
    show nora frown
    "Mai" "Chúng ta... chúng ta phải làm sao đây?"
    "Mai" "Nếu không lấy được chìa khóa, tất cả sẽ chết!"
    
    show sora frown
    "Tuấn" "Thế thì sao không cậu làm đi, Mai?"
    "Tuấn" "Cậu yếu nhất... cậu nên cống hiến một chút chứ!"
    
    show nora closed frown
    "Mai" "T-Tuấn?! Cậu nói vậy là sao?!"
    
    show chie frown
    "Lan" "Tuấn, bình tĩnh đi!"
    
    "" "Không khí căng thẳng đến nghẹt thở."
    
    "" "{i}{color=#ffaa00}Thời gian đang cạn kiệt... Minh phải quyết định ngay!{/color}{/i}"
    "" "_____ĐỒNG HỒ BẮT ĐẦU ĐẾM NGƯỢC______"
    # Hide the countdown display timer
    hide screen countdown_timer
    
    # Initialize result variable and show timed choice screen
    $ _timed_choice_result = None
    call screen timed_choice_scene3(30)
    $ result = _timed_choice_result
    
    # If player runs out of time, default to hesitation (death)
    if result is None or result == "hesitate":
        $ game_state.group_trust_level -= 30
        # A: Hesitating leads to death - no variables matter here
        
        "" "Minh do dự, không thể đưa ra quyết định."
        "" "Thời gian trôi qua từng giây..."
        "" "1... 0..."
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
        
        "Minh" "Tuấn... cậu là người mạnh nhất. Cậu phải làm việc này."
        
        "Tuấn" "CÁI GÌ?! Sao lại là tôi?!"
        
        "Minh" "Không còn thời gian! Nhanh lên!"
        
        "" "Tuấn nghiến răng, giận dữ nhìn Minh."
        "" "Anh ta thò tay vào hộp kính..."
        
        play sound "audio/acid_burn.ogg"
        
        "Tuấn" "AAAAAHHHHH!!!"
        
        "" "Bàn tay Tuấn bị bỏng nặng bởi axit!"
        "" "Nhưng anh ta đã lấy được chìa khóa."
        
        hide screen countdown_timer
        
        scene bg black
        with fade
        
        "" "Cửa phòng mở ra. Nhóm thoát ra ngoài."
        
        "" "Tuấn băng bó vết thương, {color=#e03636}ánh mắt căm hận {/color}nhìn Minh."
        "" "{color=#ff0000}Hạt giống thù hận đã được gieo..."
        
        jump scene4_truth_hallway
        
    elif result == "Lan":
        $ game_state.Lan_injury = True
        $ game_state.group_trust_level -= 20
        $ game_state.authority -= 2  # B: Assigning someone else reduces authority
        
        "Minh" "Lan, cậu có bàn tay khéo léo nhất. Cậu làm được."
        
        "Lan" "TẠI SAO?! Sao không phải Mai?!"
        
        "Minh" "Lan, nhanh lên! Chúng ta không còn thời gian!"
        
        "" "Lan run rẩy, nước mắt chảy dài."
        "" "Cô thò tay vào hộp kính..."
        
        play sound "audio/acid_burn.ogg"
        
        "Lan" "AAAHHHH! ĐAU!!!"
        
        "" "Bàn tay Lan bị bỏng, da đỏ bừng."
        "" "Nhưng cô đã lấy được chìa khóa."
        
        hide screen countdown_timer
        
        scene bg black
        with fade
        
        "" "Cửa phòng mở. Nhóm chạy ra ngoài."
        
        "" "Lan khóc nức nở, nhìn Minh với ánh mắt oán hận."
        
        jump scene4_truth_hallway
        
    else:  # result == "Minh"
        $ game_state.Minh_injury = True
        $ game_state.group_trust_level += 30
        $ game_state.trust += 1  # C: Self-sacrifice increases trust
        $ game_state.guilt += 1  # Mai feels guilty
        
        "Minh" "Tớ không thể bắt ai làm điều này. Để tớ."
        
        "Mai" "Minh! Không!"
        
        "Tuấn" "Này, đừng có liều lĩnh!"
        
        "Minh" "Đừng bàn nữa!"
        
        "" "Minh không do dự, thò tay vào hộp kính."
        
        play sound "audio/acid_burn.ogg"
        
        "Minh" "Ghhh...!"
        
        "" "Axit ăn vào da tay, đau như cắt!"
        "" "Nhưng Minh cắn răng chịu đựng, túm lấy chìa khóa!"
        
        hide screen countdown_timer
        
        scene bg black
        with fade
        
        "" "Cửa mở ra. Minh choáng váng, được Tuấn đỡ."
        
        "Tuấn" "Cậu... thật sự điên rồi."
        
        "Lan" "Nhưng... cám ơn cậu."
        
        "Mai" "Minh... Tớ xin lỗi... Tại tớ mà cậu..."
        
        "" "{color=#28b2d1}Niềm tin trong nhóm tăng lên đáng kể."
        
        jump scene4_truth_hallway

# ============================================
# SCENE 4: HALLWAY OF TRUTH (HÀNH LanG SỰ THẬT)
# ============================================

label scene4_truth_hallway:
    scene bg mirror_hallway
    with fade
    "" "Cả nhóm rời phòng hóa, tiếp tục bám theo lối cũ"
    # "Hành Lang Gương"
    
    "" "Hành Lang cũ nát bây giờ đầy gương."
    "" "Hàng trăm chiếc gương xếp dọc hai bên tường."
    "" "Hình ảnh phản chiếu không cử động, chỉ đứng yên cười quỷ dị."
    
    show aoto at left_far
    show chie at left_center
    show sora at right_center
    show nora at right_far
    with dissolve
    
    show nora closed frown
    "Mai" "Sao... sao hình ảnh trong gương lại khác với chúng ta?"
    
    show aoto frown
    "Minh" "Chúng đang cười... Nhưng chúng ta không cười."
    
    "Giọng nói bí ẩn" "Muốn đi tiếp, hãy thú nhận bí mật dơ bẩn nhất."
    "Giọng nói bí ẩn" "Những gì các ngươi giấu kín trong tâm hồn."
    "Giọng nói bí ẩn"  "Nói dối, gương sẽ vỡ... và các ngươi sẽ chết."
    
    "" "Căn phòng im lặng đến rợn người."
    
    show chie frown
    "Lan" "Chúng ta... phải làm sao?"
    "Lan" "Nói thật mọi bí mật? Điều đó... có khác gì tự hủy hoại mình."
    
    show sora closed frown
    "Tuấn" "Không có lựa chọn nào khác."
    "Tuấn" "Hoặc chúng ta thật thà, hoặc chúng ta chết."
    
    "" "Một sự im lặng nặng nề bao trùm."
    
    # Tuấn's confession
    "" "Tuấn hít một hơi sâu, bước lên trước."
    "" "Anh nhìn vào gương, đối diện với chính mình."
    
    show sora frown at pos3
    with move
    "Tuấn" "Tôi... tôi đã hãm hại Lan."
    
    show chie closed frown
    "Lan" "Cái gì?!"
    
    "Tuấn" "Năm ngoái, tôi đã xóa eMail thông báo học bổng của cậu."
    "Tuấn" "Vì tôi ghen tị. Ghen tị với sự thông Minh của cậu."
    "Tuấn" "Cậu luôn giỏi hơn tôi mọi thứ. Tôi ghét điều đó."
    "Tuấn" "Tôi xin lỗi..."
    
    $ game_state.tuan_confession = "sabotaged Lan's scholarship"
    
    show chie frown
    "Lan" "Tuấn... cậu..."
    "Lan" "Tôi đã mất cơ hội du học vì cậu!"
    
    "Tuấn" "Tôi biết. Và tôi hối hận mỗi ngày."
    
    play sound "audio/mirror_accept.ogg"
    
    "" "Gương phát sáng xanh, chấp nhận sự thật."
    "" "Tuấn thở phào nhẹ nhõm, nhưng khuôn mặt vẫn đầy tội lỗi."
    
    show sora at right_center
    with move
    
    # Mai's confession
    "" "Mai run rẩy, chân bước không vững."
    "" "Cô tiến lên trước gương."
    
    show sora at right_far
    with move
    show nora frown at pos3
    with move
    "Mai" "Tớ... tớ có một bí mật."
    "Mai" "Tớ... tớ chỉ lợi dụng Tuấn."
    
    show sora closed frown
    "Tuấn" "...Mai?"
    
    "Mai" "Tớ không thích cậu. Chưa bao giờ."
    "Mai" "Tớ chỉ giả vờ yếu đuối để cậu bảo vệ tớ."
    "Mai" "Để tớ có người che chở. Để tớ không phải đối mặt mọi thứ một mình."
    "Mai" "Tớ... tớ xin lỗi, Tuấn."
    
    "Tuấn" "..."
    
    $ game_state.Mai_confession = "used Tuấn for protection"
    
    play sound "audio/mirror_accept.ogg"
    
    "" "Gương lại sáng lên, chấp nhận lời thú tội."
    
    show nora at right
    with move
    
    # Lan's confession
    "" "Lan thở dài, bước ra."
    "" "Cô nhìn thẳng vào gương, mặt lạnh lùng."
    
    show chie closed frown at center
    with move
    "Lan" "Tôi coi tất cả các cậu... như vật thí nghiệm."
    
    show aoto frown
    "Minh" "Lan..."
    
    "Lan" "Tôi nghiên cứu hành vi của các cậu. Ghi chép lại phản ứng của các cậu."
    "Lan" "Tôi khinh thường trí tuệ của mọi người."
    "Lan" "Tôi nghĩ mình thông Minh hơn tất cả."
    
    show chie frown
    "Lan" "Nhưng... ở đây, tôi nhận ra..."
    "Lan" "Sự thông Minh chẳng có ý nghĩa gì nếu không có ai bên cạnh."
    "Lan" "Tôi... xin lỗi."
    
    $ game_state.Lan_confession = "looked down on everyone"
    
    play sound "audio/mirror_accept.ogg"
    
    "" "Gương sáng lên, chấp nhận sự thật của Lan."
    
    show chie at left_center
    with move
    
    # Minh's turn
    "" "Cuối cùng đến lượt Minh."
    "" "Tất cả nhìn anh, chờ đợi."
    "" "Gương trước mặt anh sáng lên nhẹ, như đang sẵn sàng phán xét."
    
    "" "{i}Minh hít một hơi thật sâu. Đã đến lúc phải đối mặt với chính mình...{/i}"
    "" "{i}Anh phải thú nhận điều gì?{/i}"
    
    show chie at left_far
    with move
    show aoto at left_center
    with move

    menu:
        "{color=#ff8866}Sự hèn nhát{/color} - \"Tớ muốn bỏ mặc các cậu\"":
            $ game_state.Minh_confession = "wanted to abandon everyone"
            $ game_state.group_trust_level -= 10
            $ game_state.authority += 1  # Being honest increases authority
            
            "Minh" "Tớ... tớ đã nhiều lần nghĩ đến việc bỏ các cậu lại."
            "Minh" "Khi gặp nguy hiểm, tớ chỉ nghĩ đến việc tự cứu mình thôi."
            "Minh" "Tớ là một kẻ hèn nhát. Xin lỗi..."
            
        "{color=#66aaff}Sự đố kỵ{/color} - \"Tớ ghen tị với các cậu\"":
            $ game_state.Minh_confession = "jealous of friends"
            $ game_state.group_trust_level -= 5
            $ game_state.authority += 1  # Being honest increases authority
            
            "Minh" "Tớ luôn ghen tị với các cậu."
            "Minh" "Lan thông Minh, Tuấn mạnh mẽ, Mai được yêu quý..."
            "Minh" "Còn tớ? Tớ chỉ là người bình thường nhất."
            "Minh" "Tớ ghét điều đó. Xin lỗi..."
    
    play sound "audio/mirror_accept.ogg"
    
    "" "Tất cả các gương sáng lên."
    "" "Một cánh cửa hiện ra ở cuối hành Lang."
    
    "" "Cả bốn người im lặng."
    "" "Bí mật xấu xa nhất của họ đã được phơi bày."
    "" "Nhưng họ vẫn đang sống."
    
    "Mai" "Chúng ta... đều không hoàn hảo."
    
    "Lan" "Đúng vậy. Nhưng chúng ta vẫn ở đây, cùng nhau."
    
    if game_state.group_trust_level > 0:
        $ game_state.group_trust_level += 20
        "" "Một cảm giác kỳ lạ Lan toa trong nhóm."
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
    
    "" "Cả nhóm đi đến căn phòng cuối hành Lang"
    "" "Trước mắt là căn phòng trắng với một chiếc hộp trắng"
    
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
    "Mai" "Cái hòm đó... trông như quan tài."
    
    show sora frown
    "Tuấn" "Đừng nói xui quẩy!"
    
    "" "Bốn tờ giấy trắng và bốn cây bút đen xuất hiện trước mặt mỗi người."
    "" "Chúng bay lơ lửng trong không khí, chờ đợi."
    
    play sound "audio/gamemaster_voice.ogg"
    
    "Giọng nói bí ẩn" "{size=+15}{b}QUY TẮC CUỐI CÙNG{/size}"
    "Giọng nói bí ẩn" "Viết tên {size=+5}{color=#eb2f64}{b}KẺ PHẢN BỘI{/b}{/color}{/size} vào giấy."
    "Giọng nói bí ẩn" "Ai có nhiều phiếu bầu nhất sẽ ở lại đây mãi mãi."
    
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
    "Lan" "Nếu cả bốn tờ đều trắng... tất cả sống."
    "Lan" "Nhưng nếu chỉ một người viết tên..."
    
    show sora closed frown
    "Tuấn" "Thì người bị viết tên sẽ chết."
    "Tuấn" "Và ba người còn lại sẽ thoát."
    
    show nora closed frown
    "Mai" "Các cậu sẽ không viết tên tớ chứ?"
    "Mai" "Chúng ta đã hứa... tin tưởng nhau mà..."
    
    "" "Nhưng những lời thì thầm từ đầu trò chơi vẫn còn văng vẳng."
    "" "Mỗi người đều đã nghe thấy điều gì đó khác nhau."
    "" "Ai là kẻ mạo danh? Hay thực sự chẳng có ai?"
    
    if game_state.tuan_injury or game_state.Lan_injury:
        "" "Vết thương từ phòng Hóa Học vẫn còn rát buốt."
        "" "Nỗi oán hận bắt đầu tràn ra."
        
        show sora closed frown
        "Tuấn" "Chúng ta... chúng ta phải hy sinh một người."
        
        show chie closed frown
        "Lan" "Đúng vậy. Nếu không, tất cả sẽ chết."
        
        show nora closed frown
        "Mai" "Nhưng... nhưng ai?"
        
        "" "{i}Tuấn và Lan nhìn Mai."
        
        "Tuấn" "Mai... cậu là người yếu nhất."
        
        "Lan" "Logic cho thấy... hy sinh Mai là lựa chọn tối ưu."
        
        "Mai" "K-không... Đừng...!"
        
        show aoto open
        "Minh" "Đợi đã!"
    else:
        show chie frown
        "Lan" "Chúng ta nên làm gì?"
        
        show sora closed frown
        "Tuấn" "Tôi... tôi không biết."
        
        show nora frown
        "Mai" "Minh, cậu quyết định đi."
    
    "" "{i}{color=#ffffff}Đây là khoảnh khắc quyết định... Số phận của cả nhóm nằm trong tay Minh.{/color}{/i}"
    
    menu:
        "Đồng ý viết tên Mai":
            jump normal_end_a_black_ink
            
        "Nộp giấy trắng":
            jump persuasion_attempt

label persuasion_attempt:
    "Minh" "KHÔNG! Chúng ta không được làm vậy!"
    
    "Tuấn" "Nhưng chúng ta sẽ chết!"
    
    "Minh" "Không! Tất cả những gì chúng ta thấy, tất cả bằng chứng..."
    
    if game_state.has_fake_evidence_note:
        "Minh" "...đều là GIẢ! Tớ đã tìm thấy mảnh giấy cảnh báo!"
        "Minh" "Tin tưởng nhau là lối thoát duy nhất!"
        
        $ game_state.group_trust_level += 30
        
        "Lan" "Nhưng..."
        
        "Minh" "Lan, cậu là người thông Minh. Hãy suy nghĩ!"
        "Minh" "Nếu thực sự có kẻ mạo danh, chúng đã giết chúng ta từ lâu rồi!"
        "Minh" "Đây chỉ là trò chơi tâm lý!"
        
        if game_state.group_trust_level >= 30:
            jump persuasion_success
        else:
            jump persuasion_failure
            
    elif game_state.has_translation_document:
        "Minh" "...đều là bẫy! Tớ đã đọc bản dịch luật chơi!"
        "Minh" "Con quỷ đó cần chúng ta giết nhau để sống!"
        "Minh" "Nếu chúng ta đoàn kết, hắn sẽ thua!"
        
        $ game_state.group_trust_level += 40
        
        jump persuasion_success
        
    else:
        "Minh" "Tớ cảm thấy... chúng ta đang bị lừa!"
        
        $ game_state.group_trust_level += 10
        
        "Tuấn" "Cảm thấy? Cậu đang đùa à?!"
        
        "Lan" "Không có bằng chứng gì cả!"
        
        # Without evidence, requires higher trust/authority
        if game_state.trust >= 2 and game_state.authority >= 2:
            jump persuasion_success
        else:
            jump persuasion_failure

label persuasion_success:
    $ game_state.group_trust_level += 20
    
    "Lan" "...Cậu nói đúng."
    
    "Tuấn" "Cái gì?"
    
    "Lan" "Minh nói đúng. Tất cả những manh mối đều quá... hoàn hảo."
    "Lan" "Như thể có ai đó cố tình sắp đặt."
    
    "Mai" "Vậy... chúng ta làm gì?"
    
    "Minh" "Chúng ta cùng nộp giấy trắng. Tin tưởng nhau."
    
    if game_state.Minh_injury:
        "Tuấn" "Cậu đã hy sinh vì chúng tôi. Tôi tin cậu."
    
    "Lan" "...Được rồi. Tôi tin."
    
    "Mai" "Tớ cũng vậy!"
    
    play sound "audio/paper_write.ogg"
    
    "" "Cả bốn người cùng nộp tờ giấy trắng vào hòm phiếu."
    
    # Door transition to final chapter
    call door_quick_transition
    
    jump scene6_confrontation

label persuasion_failure:
    "Tuấn" "KHÔNG! Tôi không chấp nhận rủi ro!"
    
    "Lan" "Tôi cũng vậy!"
    
    play sound "audio/paper_write.ogg"
    
    "Tuấn và Lan viết tên Mai."
    
    "Mai" "Không... KHÔNG!!!"
    
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
    "Tuấn" "Chúng ta... thắng rồi?"
    
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
    
    "" "Máu chảy từ trần nhà xuống!"
    
    show gamemaster at center
    with dissolve
    
    play music "audio/boss_theme.ogg"
    
    "" "Một bóng đen khổng lồ hiện ra từ hư không."
    "" "Khuôn mặt không rõ ràng, chỉ có nụ cười rộng đến tai."
    
    "Giọng nói bí ẩn" "{size=+20}{color=#ff0000}LŨ NGU NGỐC!{/color}{/size}"
    "Giọng nói bí ẩn" "Ta đã cho các ngươi cơ hội tìm ra kẻ mạo danh!"
    "Giọng nói bí ẩn" "Nhưng các ngươi lại chọn... tin tưởng nhau?"
    
    "" "Tiếng cười vang vọng khắp căn phòng."
    
    "Giọng nói bí ẩn" "Giấy trắng nghĩa là KHÔNG TÌM RA AI!"
    "Giọng nói bí ẩn" "TẤT CẢ PHẠM LUẬT! CHẾT ĐI!!!"
    
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
    "Minh" "KHOAN!"
    
    "" "Giọng anh vang lên mạnh mẽ, đầy quyết tâm."
    "" "Bóng tối dừng lại, như thể đang ngạc nhiên."
    
    "QUẢN TRÒ" "Hmm? Ngươi còn muốn nói gì?"
    
    "Minh" "Trong chúng tôi không ai là kẻ mạo danh!"
    "Minh" "Tất cả bằng chứng đều là giả!"
    
    "QUẢN TRÒ" "Vậy thì sao?! Các ngươi vẫn phạm luật!"
    
    "Minh" "Không!"
    "Minh" "Vậy thì chỉ còn một đáp án..."
    
    "" "Minh rút mảnh giấy cảnh báo ra."
    "" "Mảnh giấy mà anh đã tìm được trong thư viện."
    "" "Nó phát ra ánh sáng nhẹ trong tay anh."
    
    "Minh" "{size=+15}NGƯƠI MỚI LÀ KẺ MẠO DANH, QUẢN TRÒ!{/size}"
    
    "QUẢN TRÒ" "...!!!"
    
    show chie open
    "Lan" "Đúng rồi! Ngươi là người chơi thứ 5!"
    
    show sora open
    "Tuấn" "Ngươi giả làm trọng tài để lừa chúng tôi giết nhau!"
    
    play sound "audio/paper_write.ogg"
    
    "" "Minh viết 'Quản trò' vào tờ giấy và ném vào hòm phiếu."
    
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
    "Minh" "Mày định dọa ai?"
    
    "" "Minh giơ tập giấy ghi chú cũ nát lên."
    "" "Nó phát ra ánh sáng vàng nhạt, đẩy lùi bóng tối."
    
    "Minh" "Tao đã đọc bản dịch GỐC của nghi thức này rồi!"
    
    "Giọng nói bí ẩn" "Cái gì...?! Làm sao ngươi có được...?!"
    
    "Minh" "Mày nói bọn tao phạm luật? SAI!"
    "Minh" "Luật nói: 'Kẻ thua cuộc phải chết'."
    "Minh" "Nhưng khi cả 4 tờ đều trắng, KHÔNG AI THUA!"
    
    "" "Quản Trò lùi lại, vẻ mặt bắt đầu hoảng loạn."
    
    show chie open
    "Lan" "Đợi đã... Tôi hiểu rồi!"
    "Lan" "Nếu không có người chơi nào thua..."
    "Lan" "...thì kẻ duy nhất thất bại trong việc duy trì trò chơi..."
    "Lan" "...là MÀY - QUẢN TRÒ!"
    
    show nora open
    "Mai" "Hắn là người chơi thứ 5! Giả làm trọng tài!"
    
    show aoto smile
    "Minh" "Quy tắc thứ 13: Khi Quản Trò thất bại, hắn sẽ mất quyền năng!"
    "Minh" "Mày không phải thần thánh. Mày chỉ là KÝ SINH TRÙNG!"
    "Minh" "Sống dựa vào nỗi sợ của chúng tao!"
    
    show sora smile
    "Tuấn" "Và giờ bọn tao sẽ nghiền nát mày!"
    
    "" "Cả bốn người cùng đứng lên, đối mặt với Quản Trò."
    "" "Sự đoàn kết của họ tạo thành một bức tường vô hình."
    
    play sound "audio/paper_write.ogg"
    
    "Minh viết 'Quản trò' vào phiếu và ném vào hòm."
    
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
    
    centered "{size=+10}NGẠT...{/size}"
    
    pause 2.0
    
    centered "Sự do dự đã giết chết cả nhóm."
    centered "Họ ngã xuống một cách vô vọng trong khói độc."
    centered "Không ai sống sót."
    centered "{size=+20}{color=#ff0000}BAD ENDING 2{/color}{/size}"
    
    pause 3.0
    
    return

# NORMAL END A: BLACK INK
label normal_end_a_black_ink:
    scene bg white_room
    
    play sound "audio/paper_write.ogg"
    
    "" "Minh run rẩy viết tên 'Mai' vào giấy."
    
    "Mai" "Minh...? Cậu... cậu làm gì vậy?"
    
    "" "Cả bốn người nộp phiếu."
    
    play sound "audio/ballot_open.ogg"
    
    "" "Hòm phiếu mở ra: 3 phiếu 'Mai'. 1 phiếu trắng."
    
    "Mai" "Không... các cậu..."
    
    scene bg black
    with flash
    
    play sound "audio/scream.ogg"
    
    "" "Mai biến mất trong tiếng thét."
    
    scene bg club_room
    with fade
    
    show expression Solid("#000000") as overlay
    centered "{size=+10}GIỌT MỰC ĐEN{/size}"
    "" "Ba người còn lại tỉnh lại trong phòng CLB."
    "" "Họ sống sót."
    "" "Nhưng Mai không còn đó."
    
    play music "audio/meLancholic.ogg"

    
    pause 2.0
    
    "" "Cả ba người không bao giờ nói chuyện với nhau nữa."
    "" "Họ sống trong day dứt suốt đời."
    "" "Giọt mực đen đó... không bao giờ tẩy sạch."
    
    centered "{size=+20}{color=#ffaa00}NORMAL ENDING A{/color}{/size}"
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
    
    "Mai" "Minh! CỨU TỚ!!!"
    
    show text "{i}{color=#fa4c34}Nhưng đã quá muộn. Mai biến mất." at truecenter
    pause(1.5)
    show expression Solid("#000000") as overlay
    centered "{size=+10}RẠN NỨT{/size}"
    
    pause 2.0
    "" "Ba người tỉnh lại."
    "" "Minh nhìn Tuấn và Lan với ánh mắt căm phẫn."
    
    "Minh" "Các cậu... đã giết Mai."
    
    "" "Tình bạn tan vỡ hoàn toàn."
    "" "Họ không bao giờ gặp lại nhau nữa."
    
    centered "{size=+20}{color=#ffaa00}NORMAL ENDING B{/color}{/size}"
    pause 3.0
    
    return

# BAD END: CHAOS
label bad_end_chaos:
    scene bg black
    with flash
    
    play sound "audio/darkness.ogg"
    
    show expression Solid("#000000") as overlay
    "Không có manh mối, Minh không biết phải làm gì."
    "Bóng tối nuốt chửng cả nhóm."
    
    play music "audio/sad_theme.ogg"
    centered "{size=+10}SỰ HỖN LOẠN{/size}"
    
    pause 2.0
    
    centered "Họ không tìm ra lối thoát."
    centered "Tất cả đều biến mất trong bóng tối."
    
    centered "{size=+20}{color=#ff0000}BAD ENDING{/color}{/size}"
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
    "Tuấn" "Chúng ta... sống sót?"
    
    show chie smile
    "Lan" "Có vẻ vậy."
    
    show nora smile
    "Mai" "Minh... cám ơn cậu."
    
    show aoto smile
    "Minh" "Không. Cám ơn tất cả các cậu."
    "Minh" "Chúng ta đã tin tưởng nhau."
    
    "" "Họ ngồi im lặng một lúc."
    "" "Những bí mật đã được phơi bày."
    "" "Những vết thương đã được tạo ra."
    
    show chie frown
    "Lan" "Chúng ta... vẫn là bạn chứ?"
    
    show sora closed smile
    "Tuấn" "Tôi muốn vậy. Nếu các cậu tha thứ cho tôi."
    
    show nora closed smile
    "Mai" "Tớ cũng xin lỗi. Xin lỗi tất cả."
    
    show aoto smile
    "Minh" "Chúng ta không hoàn hảo. Nhưng chúng ta vẫn ở đây."
    "Minh" "Và đó là điều quan trọng nhất."
    
    hide aoto
    hide chie
    hide sora
    hide nora
    with dissolve
    
    scene bg dawn_sky
    with fade
    
    "" "Bên ngoài cửa sổ, bình Minh đang dần ló rạng."
    
    show expression Solid("#000000") as overlay
    centered "{size=+20}Bình Minh{/size}"
    
    pause 3.0
    
    centered "Họ chấp nhận quá khứ xấu xí của nhau."
    centered "Họ chọn tha thứ."
    centered "Họ chọn tin tưởng."
    
    pause 2.0
    
    centered "Và họ bước vào một ngày mới."
    centered "Cùng nhau."
    centered "{size=+30}{color=#00ff5e}TRUE ENDING{/color}{/size}"
    
    pause 3.0
    
    return
