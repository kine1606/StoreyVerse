# SỰ PHẢN BỘI - VISUAL NOVEL GAME
# Story Script

# ============================================
# GAME INITIALIZATION & VARIABLES
# ============================================

init python:
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
    game_state = GameState()

# ============================================
# SCENE 1: THE INVITATION (LỜI MỜI GỌI)
# ============================================

label start:
    # Initialize game state
    $ game_state = GameState()
    
    scene bg club night
    with fade
    
    show text "Phòng sinh hoạt CLB Tâm linh\n11:00 PM" at truecenter
    with dissolve
    pause 2.0
    hide text
    
    "Ánh nến leo lét trong căn phòng tối tăm."
    "Bốn người bạn ngồi quay quanh một tấm bảng Ouija cũ kỹ."
    
    # TUẤN speaks
    "TUẤN" "Tớ vẫn không tin được là chúng ta đang làm chuyện này. Nhỡ có con gì hiện ra thật thì sao?"
    
    # LAN speaks
    "LAN" "Thống kê cho thấy 99%% các nghi thức gọi hồn chỉ là ảo giác nhóm. Cứ xem như trải nghiệm tâm lý đi."
    
    # MAI speaks
    "MAI" "Nhưng... từ lúc vào đây tớ đã thấy lạnh sống lưng rồi."
    
    # MINH speaks
    "MINH" "Thôi nào. Chỉ là đọc vài câu cho vui thôi. Để tớ đọc câu cuối cùng nhé."
    
    play sound "audio/chant.ogg"
    "Minh đọc câu niệm chú cuối cùng..."
    
    scene bg black
    with flash
    
    play sound "audio/candle_out.ogg"
    "Tất cả ngọn nến đồng loạt tắt phụt!"
    
    play sound "audio/pain.ogg"
    "Một cơn đau buốt nhói lên trong đầu cả bốn người."
    
    # Whispers - each character hears something different
    show text "Những lời thì thầm vang lên..." at truecenter
    with dissolve
    pause 2.0
    hide text
    
    play sound "audio/whisper.ogg"
    
    centered "{color=#ff0000}MINH nghe thấy:{/color}\n\"Trong số các ngươi, có một kẻ đã bị chiếm xác.\""
    
    centered "{color=#ff0000}LAN nghe thấy:{/color}\n\"Đừng tin ai cả. Một người trong nhóm không còn là chính mình nữa.\""
    
    centered "{color=#ff0000}TUẤN nghe thấy:{/color}\n\"Là Mai. Nó đang giả vờ yếu đuối. Hãy cẩn thận.\""
    
    centered "{color=#ff0000}MAI nghe thấy:{/color}\n\"Bọn họ đang nghi ngờ ngươi. Ngươi sẽ bị bỏ lại.\""
    
    scene bg club_room
    with flash
    
    "Khi ánh sáng trở lại, cánh cửa phòng đã biến mất."
    "Thay vào đó là một cổng sắt rỉ máu với dòng chữ khắc sâu:"
    
    show text "{size=+20}{color=#ff0000}TRÒ CHƠI BẮT ĐẦU\nTÌM RA KẺ MẠO DANH ĐỂ SỐNG SÓT{/color}{/size}" at truecenter
    with dissolve
    pause 3.0
    hide text
    
    jump scene2_corridor

# ============================================
# SCENE 2: MAZE OF CLUES (MÊ CUNG MANH MỐI)
# ============================================

label scene2_corridor:
    scene bg old_corridor
    with fade
    
    show text "Hành lang trường học cũ nát" at truecenter
    with dissolve
    pause 1.5
    hide text
    
    "Căn hành lang ẩm mốc, vách tường bong tróc."
    "Mùi mốc nồng nặc khiến cả nhóm khó thở."
    
    "LAN" "Chúng ta cần thông tin. Nếu có kẻ mạo danh, phải có manh mối."
    
    "TUẤN" "Chia ra sẽ nhanh hơn. Minh và Lan vào thư viện. Tôi trông Mai ở phòng y tế."
    
    menu:
        "MINH phải quyết định:"
        
        "Chia nhóm hành động (Nguy hiểm)":
            $ game_state.group_trust_level -= 10
            jump scene2_branch_a_library
            
        "Đi cùng nhau (An toàn)":
            $ game_state.group_trust_level += 10
            jump scene2_branch_b_archive

# ============================================
# BRANCH A: LIBRARY (THƯ VIỆN)
# ============================================

label scene2_branch_a_library:
    scene bg library
    with fade
    
    "Minh và Lan bước vào thư viện tối tăm."
    "Ánh đèn pin rọi lên những giá sách bụi mờ."
    
    play sound "audio/book_fall.ogg"
    
    "Một cuốn sách rơi xuống đất, trang giở sẵn."
    
    "LAN" "Minh, xem này!"
    
    "Đó là một trang nhật ký viết nguệch ngoạc:"
    
    show text "{i}\"Mai đang diễn kịch. Tôi biết. Cô ta không yếu đuối như vẻ bề ngoài.\"{/i}" at truecenter
    with dissolve
    pause 3.0
    hide text
    
    "LAN" "Thấy chưa? Mai đang lừa dối chúng ta! Đi thôi!"
    
    menu:
        "MINH quyết định:"
        
        "Tin ngay và rời đi":
            $ game_state.group_trust_level -= 20
            "Minh và Lan vội vã rời khỏi thư viện."
            "Họ bỏ lỡ manh mối quan trọng..."
            jump scene2_reunite
            
        "Kiểm tra kỹ hơn":
            $ game_state.group_trust_level += 5
            
            "MINH" "Khoan đã... Trang này trông quá... giả tạo."
            
            "Minh lật lại trang nhật ký, phát hiện một mảnh giấy nhỏ kẹp bên trong:"
            
            show text "{color=#00ff00}\"MỌI BẰNG CHỨNG ĐỀU LÀ GIẢ.\nTIN TƯỞNG NHAU LÀ LỐI THOÁT DUY NHẤT.\"{/color}" at truecenter
            with dissolve
            pause 4.0
            hide text
            
            $ game_state.has_fake_evidence_note = True
            
            play sound "audio/item_get.ogg"
            centered "{color=#00ff00}\[Đã nhận: Mảnh giấy 'Bằng chứng giả']{/color}"
            
            "MINH" "Tớ hiểu rồi... Tất cả chỉ là bẫy để chia rẽ chúng ta."
            
            # Dead End Trap
            "Khi chuẩn bị rời đi, một cuốn sách phát sáng màu tím xuất hiện trên giá."
            "Nó rung rinh, như thể đang mời gọi..."
            
            menu:
                "Một cuốn sách lạ đang phát sáng..."
                
                "\"Đợi đã, cuốn sách kia phát sáng!\"":
                    "Minh không cưỡng lại được sự tò mò."
                    "Anh chạm tay vào cuốn sách..."
                    
                    scene bg black
                    with flash
                    
                    play sound "audio/dark_consume.ogg"
                    
                    "Cuốn sách hóa thành khói đen, nuốt chửng Minh!"
                    
                    "LAN" "MINH! KHÔNG!!!"
                    
                    jump bad_end_1_lost
                    
                "\"Đi thôi, tớ có cảm giác không lành.\"":
                    $ game_state.group_trust_level += 10
                    
                    "MINH" "Không, có gì đó sai sai. Chúng ta đi thôi."
                    
                    "Cả hai nhanh chóng rời khỏi thư viện."
                    
                    jump scene2_reunite

# ============================================
# BRANCH B: ARCHIVE ROOM (PHÒNG LƯU TRỮ)
# ============================================

label scene2_branch_b_archive:
    scene bg archive_room
    with fade
    
    "Cả nhóm cùng nhau bước vào phòng lưu trữ CLB."
    "Giá tài liệu xếp chồng lên nhau một cách lộn xộn."
    
    play sound "audio/rumble.ogg"
    
    "Đột nhiên, căn phòng rung chuyển dữ dội!"
    "Trần nhà bắt đầu nứt ra, mảng tường rơi xuống!"
    
    show ghost_minion at center
    with dissolve
    
    play sound "audio/evil_laugh.ogg"
    
    "HỒN MA TAY SAI" "Hahaha... Chọn nhanh lên! Các ngươi chỉ có 10 giây!"
    
    hide ghost_minion
    with dissolve
    
    "Trên bàn làm việc lộn xộn, có hai tài liệu nổi bật:"
    "1. CUỐN NHẬT KÝ BÌA ĐỎ - Đang mở sẵn, nét chữ đầy thù hận"
    "2. TẬP GIẤY GHI CHÚ CŨ NÁT - Toàn công thức dịch thuật khô khan"
    
    "Minh chỉ có thể cầm MỘT thứ trước khi chạy!"
    
    menu:
        "Chọn nhanh! Thời gian không còn nhiều!"
        
        "Chộp lấy Cuốn Nhật Ký Bìa Đỏ":
            $ game_state.chose_red_diary = True
            $ game_state.group_trust_level -= 15
            
            play sound "audio/grab.ogg"
            
            "Minh túm lấy cuốn nhật ký và chạy theo nhóm!"
            
            scene bg old_corridor
            with fade
            
            "Cả nhóm chạy ra ngoài, thở hổn hển."
            
            "Minh mở cuốn nhật ký ra đọc:"
            
            show text "{i}\"Thằng bạn thân nhất đã đâm sau lưng tao...\nĐừng tin ai...\nTất cả đều muốn mày chết...\"{/i}" at truecenter
            with dissolve
            pause 3.0
            hide text
            
            "Những dòng chữ hoang tưởng khiến Minh càng thêm nghi ngờ."
            "Hạt giống hoài nghi đã được gieo vào tâm trí anh..."
            
            jump scene3_chemistry
            
        "Giật lấy Tập Giấy Ghi Chú":
            $ game_state.has_translation_document = True
            $ game_state.group_trust_level += 20
            
            play sound "audio/grab.ogg"
            
            "Minh chộp lấy tập giấy cũ nát và lao ra ngoài!"
            
            scene bg old_corridor
            with fade
            
            "Cả nhóm an toàn. Minh mở tập giấy ra đọc lướt..."
            
            "Đây là bản dịch luật chơi gốc!"
            
            show text "{color=#00ff00}Quy tắc thứ 13:\nQuản Trò không phải trọng tài.\nQuản Trò là 'Người Chơi' ở vị thế quan sát.\nHắn sống bằng nỗi sợ.\n\nNếu các 'Vật Hiến Tế' từ chối giết nhau,\nQuản Trò sẽ vi phạm Giao Kèo\nvà buộc phải hiện nguyên hình.\n\nĐÓ LÀ LÚC HẮN CÓ THỂ BỊ GIẾT.{/color}" at truecenter
            with dissolve
            pause 5.0
            hide text
            
            play sound "audio/revelation.ogg"
            centered "{color=#00ff00}[Đã nhận: Bản dịch Luật Chơi Gốc]{/color}"
            
            "MINH" "Tớ hiểu rồi... Sự đoàn kết không chỉ giúp ta sống sót..."
            "MINH" "...mà còn là vũ khí để tiêu diệt con quỷ!"
            
            jump scene3_chemistry

label scene2_reunite:
    scene bg old_corridor
    with fade
    
    "Minh và Lan gặp lại Tuấn và Mai ở hành lang."
    
    "TUẤN" "Các cậu tìm được gì không?"
    
    if game_state.has_fake_evidence_note:
        "MINH" "Có... nhưng không phải bằng chứng. Là một lời cảnh báo."
    else:
        "MINH" "Không có gì đáng tin cả. Đi tiếp thôi."
    
    jump scene3_chemistry

# ============================================
# SCENE 3: CHEMISTRY ROOM (PHÒNG HÓA HỌC)
# ============================================

label scene3_chemistry:
    scene bg chemistry_room
    with fade
    
    show text "Phòng Hóa Học" at truecenter
    with dissolve
    pause 1.5
    hide text
    
    "Cánh cửa duy nhất mở ra dẫn vào phòng Hóa Học."
    "Mùi axit nồng nặc làm cả nhóm phải bịt mũi."
    
    "Giữa phòng có một chiếc hộp kính chứa dung dịch sủi bọt."
    "Bên trong có rết độc bò lổm ngổm."
    "Một chiếc chìa khóa vàng nằm dưới đáy."
    
    play sound "audio/countdown.ogg"
    
    play music "audio/tension.ogg"
    
    $ countdown_time = 60
    show screen countdown_timer(countdown_time)
    
    "GIỌNG NÓI QUẢN TRÒ" "{size=+10}/Chọn vật hiến tế để lấy chìa khóa.{/size}"
    "GIỌNG NÓI QUẢN TRÒ" "{size=+10}/Hết giờ, phòng sẽ bơm khí độc.{/size}"
    
    "TUẤN" "Cái quái gì vậy?! Ai dám thò tay vào đống axit đó?!"
    
    "LAN" "Đ-đừng nhìn tôi! Tôi không làm đâu!"
    
    "MAI" "Chúng ta... chúng ta phải làm sao đây?"
    
    "Đồng hồ đếm ngược. 45 giây... 40 giây..."
    
    menu:
        "MINH phải quyết định ngay!"
        
        "\"Không! Tớ không thể ép ai cả! Tìm cách khác đi!\"":
            $ game_state.group_trust_level -= 30
            
            "Minh do dự, không thể đưa ra quyết định."
            "Thời gian trôi qua từng giây..."
            
            "30... 20... 10..."
            
            hide screen countdown_timer
            
            play sound "audio/timer_end.ogg"
            
            "KHÔNG!!!"
            
            scene bg black
            with flash
            
            play sound "audio/gas.ogg"
            
            "Đồng hồ về 0."
            "Cửa phòng khóa chặt."
            "Khí gas độc phun ra từ các ống thông gió!"
            
            jump bad_end_2_gas_room
            
        "Chỉ định Tuấn làm":
            $ game_state.tuan_injury = True
            $ game_state.group_trust_level -= 20
            
            "MINH" "Tuấn... cậu là người mạnh nhất. Cậu phải làm việc này."
            
            "TUẤN" "CÁI GÌ?! Sao lại là tôi?!"
            
            "MINH" "Không còn thời gian! Nhanh lên!"
            
            "Tuấn nghiến răng, giận dữ nhìn Minh."
            "Anh ta thò tay vào hộp kính..."
            
            play sound "audio/acid_burn.ogg"
            
            "TUẤN" "AAAAAHHHHH!!!"
            
            "Bàn tay Tuấn bị bỏng nặng bởi axit!"
            "Nhưng anh ta đã lấy được chìa khóa."
            
            hide screen countdown_timer
            
            scene bg black
            with fade
            
            "Cửa phòng mở ra. Nhóm thoát ra ngoài."
            
            "Tuấn băng bó vết thương, ánh mắt căm hận nhìn Minh."
            "Hạt giống thù hận đã được gieo..."
            
            jump scene4_truth_hallway
            
        "Chỉ định Lan làm":
            $ game_state.lan_injury = True
            $ game_state.group_trust_level -= 20
            
            "MINH" "Lan, cậu có bàn tay khéo léo nhất. Cậu làm được."
            
            "LAN" "TẠI SAO?! Sao không phải Mai?!"
            
            "MINH" "Lan, nhanh lên! Chúng ta không còn thời gian!"
            
            "Lan run rẩy, nước mắt chảy dài."
            "Cô thò tay vào hộp kính..."
            
            play sound "audio/acid_burn.ogg"
            
            "LAN" "AAAHHHH! ĐAU!!!"
            
            "Bàn tay Lan bị bỏng, da đỏ bừng."
            "Nhưng cô đã lấy được chìa khóa."
            
            hide screen countdown_timer
            
            scene bg black
            with fade
            
            "Cửa phòng mở. Nhóm chạy ra ngoài."
            
            "Lan khóc nức nở, nhìn Minh với ánh mắt oán hận."
            
            jump scene4_truth_hallway
            
        "\"Để tớ làm.\"":
            $ game_state.minh_injury = True
            $ game_state.group_trust_level += 30
            
            "MINH" "Tớ không thể bắt ai làm điều này. Để tớ."
            
            "MAI" "Minh! Không!"
            
            "TUẤN" "Này, đừng có liều lĩnh!"
            
            "MINH" "Đừng bàn nữa!"
            
            "Minh không do dự, thò tay vào hộp kính."
            
            play sound "audio/acid_burn.ogg"
            
            "MINH" "Ghhh...!"
            
            "Axit ăn vào da tay, đau như cắt!"
            "Nhưng Minh cắn răng chịu đựng, túm lấy chìa khóa!"
            
            hide screen countdown_timer
            
            scene bg black
            with fade
            
            "Cửa mở ra. Minh choáng váng, được Tuấn đỡ."
            
            "TUẤN" "Cậu... thật sự điên rồi."
            
            "LAN" "Nhưng... cám ơn cậu."
            
            "MAI" "Minh... Tớ xin lỗi... Tại tớ mà cậu..."
            
            "Niềm tin trong nhóm tăng lên đáng kể."
            
            jump scene4_truth_hallway

# ============================================
# SCENE 4: HALLWAY OF TRUTH (HÀNH LANG SỰ THẬT)
# ============================================

label scene4_truth_hallway:
    scene bg mirror_hallway
    with fade
    
    show text "Hành Lang Gương" at truecenter
    with dissolve
    pause 1.5
    hide text
    
    "Một hành lang dài đầy gương."
    "Hình ảnh phản chiếu không cử động, chỉ đứng yên cười quỷ dị."
    
    "GIỌNG NÓI QUẢN TRÒ" "Muốn đi tiếp, hãy thú nhận bí mật dơ bẩn nhất."
    "GIỌNG NÓI QUẢN TRÒ" "Nói dối, gương sẽ vỡ... và các ngươi sẽ chết."
    
    "LAN" "Chúng ta... phải làm sao?"
    
    "TUẤN" "Không có lựa chọn nào khác."
    
    # TUẤN's confession
    "Tuấn bước lên trước, nhìn vào gương."
    
    "TUẤN" "Tôi... tôi đã hãm hại Lan."
    
    "LAN" "Cái gì?!"
    
    "TUẤN" "Năm ngoái, tôi đã xóa email thông báo học bổng của cậu."
    "TUẤN" "Vì tôi ghen tị. Ghen tị với sự thông minh của cậu."
    "TUẤN" "Tôi xin lỗi..."
    
    $ game_state.tuan_confession = "sabotaged Lan's scholarship"
    
    play sound "audio/mirror_accept.ogg"
    
    "Gương phát sáng xanh, chấp nhận sự thật."
    
    # MAI's confession
    "Mai run rẩy bước tới."
    
    "MAI" "Tớ... tớ chỉ lợi dụng Tuấn."
    
    "TUẤN" "...Mai?"
    
    "MAI" "Tớ không thích cậu. Tớ chỉ giả vờ yếu đuối để cậu bảo vệ tớ."
    "MAI" "Tớ... tớ xin lỗi, Tuấn."
    
    $ game_state.mai_confession = "used Tuấn for protection"
    
    play sound "audio/mirror_accept.ogg"
    
    "Gương lại sáng lên."
    
    # LAN's confession
    "Lan thở dài, bước ra."
    
    "LAN" "Tôi coi tất cả các cậu... như vật thí nghiệm."
    
    "MINH" "Lan..."
    
    "LAN" "Tôi nghiên cứu hành vi của các cậu. Tôi khinh thường trí tuệ của mọi người."
    "LAN" "Tôi nghĩ mình thông minh hơn tất cả. Tôi... xin lỗi."
    
    $ game_state.lan_confession = "looked down on everyone"
    
    play sound "audio/mirror_accept.ogg"
    
    # MINH's turn
    "Cuối cùng đến lượt Minh."
    "Tất cả nhìn anh."
    
    menu:
        "Minh phải thú nhận..."
        
        "Sự hèn nhát - \"Tớ muốn bỏ mặc các cậu\"":
            $ game_state.minh_confession = "wanted to abandon everyone"
            $ game_state.group_trust_level -= 10
            
            "MINH" "Tớ... tớ đã nhiều lần nghĩ đến việc bỏ các cậu lại."
            "MINH" "Khi gặp nguy hiểm, tớ chỉ nghĩ đến việc tự cứu mình thôi."
            "MINH" "Tớ là một kẻ hèn nhát. Xin lỗi..."
            
        "Sự đố kỵ - \"Tớ ghen tị với các cậu\"":
            $ game_state.minh_confession = "jealous of friends"
            $ game_state.group_trust_level -= 5
            
            "MINH" "Tớ luôn ghen tị với các cậu."
            "MINH" "Lan thông minh, Tuấn mạnh mẽ, Mai được yêu quý..."
            "MINH" "Còn tớ? Tớ chỉ là người bình thường nhất."
            "MINH" "Tớ ghét điều đó. Xin lỗi..."
    
    play sound "audio/mirror_accept.ogg"
    
    "Tất cả các gương sáng lên."
    "Một cánh cửa hiện ra ở cuối hành lang."
    
    "Cả bốn người im lặng."
    "Bí mật xấu xa nhất của họ đã được phơi bày."
    "Nhưng họ vẫn đang sống."
    
    "MAI" "Chúng ta... đều không hoàn hảo."
    
    "LAN" "Đúng vậy. Nhưng chúng ta vẫn ở đây, cùng nhau."
    
    if game_state.group_trust_level > 0:
        $ game_state.group_trust_level += 20
        "Một cảm giác kỳ lạ lan toa trong nhóm."
        "Họ hiểu nhau hơn... và cũng tha thứ hơn."
    
    jump scene5_voting_room

# ============================================
# SCENE 5: VOTING ROOM (CĂN PHÒNG BỎ PHIẾU)
# ============================================

label scene5_voting_room:
    scene bg white_room
    with fade
    
    show text "Căn Phòng Trắng" at truecenter
    with dissolve
    pause 1.5
    hide text
    
    "Một căn phòng trắng toát."
    "Giữa phòng là một chiếc hòm phiếu đen như mực."
    
    "Bốn tờ giấy trắng và bốn cây bút đen xuất hiện trước mặt mỗi người."
    
    play sound "audio/gamemaster_voice.ogg"
    
    "GIỌNG NÓI QUẢN TRÒ" "{size=+15}QUY TẮC CUỐI CÙNG:{/size}"
    "GIỌNG NÓI QUẢN TRÒ" "Viết tên KẺ PHẢN BỘI vào giấy."
    "GIỌNG NÓI QUẢN TRÒ" "Nếu cả 4 tờ đều TRẮNG: Tất cả sống."
    "GIỌNG NÓI QUẢN TRÒ" "Nếu có TÊN: Người có nhiều phiếu nhất chết, 3 người còn lại về."
    
    scene bg white_room
    
    "Không khí căng thẳng đến tột độ."
    
    if game_state.tuan_injury or game_state.lan_injury:
        "TUẤN" "Chúng ta... chúng ta phải hy sinh một người."
        
        "LAN" "Đúng vậy. Nếu không, tất cả sẽ chết."
        
        "MAI" "Nhưng... nhưng ai?"
        
        "Tuấn và Lan nhìn Mai."
        
        "TUẤN" "Mai... cậu là người yếu nhất."
        
        "LAN" "Logic cho thấy... hy sinh Mai là lựa chọn tối ưu."
        
        "MAI" "K-không... Đừng...!"
        
        "MINH" "Đợi đã!"
    else:
        "LAN" "Chúng ta nên làm gì?"
        
        "TUẤN" "Tôi... tôi không biết."
        
        "MAI" "Minh, cậu quyết định đi."
    
    menu:
        "MINH phải đưa ra quyết định cuối cùng:"
        
        "Đồng ý viết tên Mai (Phản bội)":
            jump normal_end_a_black_ink
            
        "Nộp giấy trắng và thuyết phục mọi người (Tin tưởng)":
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
        
        if game_state.group_trust_level >= 40:
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
    
    jump scene6_confrontation

label persuasion_failure:
    "TUẤN" "KHÔNG! Tôi không chấp nhận rủi ro!"
    
    "LAN" "Tôi cũng vậy!"
    
    play sound "audio/paper_write.ogg"
    
    "Tuấn và Lan viết tên Mai."
    
    "MAI" "Không... KHÔNG!!!"
    
    menu:
        "Minh còn cơ hội cuối cùng..."
        
        "Viết tên Mai (Cứu bản thân)":
            jump normal_end_a_black_ink
            
        "Vẫn nộp giấy trắng (Giữ nguyên tắc)":
            jump normal_end_b_cracked

# ============================================
# SCENE 6: CONFRONTING THE EVIL (ĐỐI MẶT ÁC QUỶ)
# ============================================

label scene6_confrontation:
    scene bg white_room
    
    play sound "audio/ballot_open.ogg"
    
    "Hòm phiếu từ từ mở ra."
    "Bốn tờ giấy trắng bay lên."
    
    "TUẤN" "Chúng ta... thắng rồi?"
    
    play sound "audio/rumble.ogg"
    
    "Nhưng thay vì cánh cửa mở ra..."
    "Căn phòng rung chuyển dữ dội!"
    
    scene bg black
    with flash
    
    play sound "audio/blood_drip.ogg"
    
    "Máu chảy từ trần nhà xuống!"
    
    show gamemaster at center
    with dissolve
    
    play music "audio/boss_theme.ogg"
    
    "QUẢN TRÒ" "{size=+20}{color=#ff0000}LŨ NGU NGỐC!{/color}{/size}"
    "QUẢN TRÒ" "Giấy trắng nghĩa là KHÔNG TÌM RA AI!"
    "QUẢN TRÒ" "TẤT CẢ PHẠM LUẬT! CHẾT ĐI!!!"
    
    "Bóng tối bắt đầu bao trùm..."
    
    # Check for key items
    if game_state.has_fake_evidence_note:
        jump true_end_path_1
    elif game_state.has_translation_document:
        jump true_end_path_2
    else:
        jump bad_end_chaos

label true_end_path_1:
    "MINH" "KHOAN!"
    
    "Bóng tối dừng lại."
    
    "MINH" "Trong chúng tôi không ai là kẻ mạo danh!"
    
    "QUẢN TRÒ" "Vậy thì sao?!"
    
    "MINH" "Vậy thì chỉ còn một đáp án..."
    
    "Minh rút mảnh giấy cảnh báo ra."
    
    "MINH" "{size=+15}NGƯƠI MỚI LÀ KẺ MẠO DANH, QUẢN TRÒ!{/size}"
    
    "QUẢN TRÒ" "...!!!"
    
    "LAN" "Đúng rồi! Ngươi là người chơi thứ 5!"
    
    "TUẤN" "Ngươi giả làm trọng tài để lừa chúng tôi giết nhau!"
    
    play sound "audio/paper_write.ogg"
    
    "Minh viết 'QUẢN TRÒ' lên tờ giấy và ném vào hòm phiếu."
    
    jump true_ending_dawn

label true_end_path_2:
    "MINH" "Mày định dọa ai?"
    
    "Minh giơ tập giấy ghi chú cũ nát lên."
    
    "MINH" "Tao đã đọc bản dịch GỐC của nghi thức này rồi!"
    
    "QUẢN TRÒ" "Cái gì...?!"
    
    "MINH" "Mày nói bọn tao phạm luật? SAI!"
    "MINH" "Luật nói: 'Kẻ thua cuộc phải chết'."
    "MINH" "Nhưng khi cả 4 tờ đều trắng, KHÔNG AI THUA!"
    
    "LAN" "Nếu không có người chơi nào thua..."
    "LAN" "...thì kẻ duy nhất thất bại trong việc duy trì trò chơi..."
    "LAN" "...là MÀY - QUẢN TRÒ!"
    
    "MINH" "Quy tắc thứ 13: Khi Quản Trò thất bại, hắn sẽ mất quyền năng!"
    "MINH" "Mày không phải thần thánh. Mày chỉ là KÝ SINH TRÙNG!"
    
    "TUẤN" "Và giờ bọn tao sẽ nghiền nát mày!"
    
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
    
    "Minh run rẩy viết tên 'Mai' vào giấy."
    
    "MAI" "Minh...? Cậu... cậu làm gì vậy?"
    
    "Cả bốn người nộp phiếu."
    
    play sound "audio/ballot_open.ogg"
    
    "Hòm phiếu mở ra: 3 phiếu 'Mai'. 1 phiếu trắng."
    
    "MAI" "Không... các cậu..."
    
    scene bg black
    with flash
    
    play sound "audio/scream.ogg"
    
    "Mai biến mất trong tiếng thét."
    
    scene bg club_room
    with fade
    
    "Ba người còn lại tỉnh lại trong phòng CLB."
    "Họ sống sót."
    "Nhưng Mai không còn đó."
    
    play music "audio/melancholic.ogg"
    
    centered "{size=+20}{color=#ffaa00}NORMAL ENDING A{/color}{/size}"
    centered "{size=+10}GIỌT MỰC ĐEN{/size}"
    
    pause 2.0
    
    "Cả ba người không bao giờ nói chuyện với nhau nữa."
    "Họ sống trong day dứt suốt đời."
    "Giọt mực đen đó... không bao giờ tẩy sạch."
    
    pause 3.0
    
    return

# NORMAL END B: CRACKED
label normal_end_b_cracked:
    scene bg white_room
    
    play sound "audio/paper_write.ogg"
    
    "Minh nộp giấy trắng."
    "Nhưng Tuấn và Lan đã viết 'Mai'."
    
    play sound "audio/ballot_open.ogg"
    
    "Hòm mở: 2 phiếu 'Mai'. 2 phiếu trắng."
    
    "Mai có số phiếu cao nhất."
    
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
    
    "Ba người tỉnh lại."
    "Minh nhìn Tuấn và Lan với ánh mắt căm phẫn."
    
    "MINH" "Các cậu... đã giết Mai."
    
    "Tình bạn tan vỡ hoàn toàn."
    "Họ không bao giờ gặp lại nhau nữa."
    
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
    
    "Hòm phiếu bốc cháy dữ dội!"
    
    show gamemaster at center
    
    "QUẢN TRÒ" "{size=+20}KHÔNG! CÁC NGƯƠI... AAAAAHHHHH!!!{/size}"
    
    hide gamemaster
    with dissolve
    
    play sound "audio/explosion.ogg"
    
    scene bg white
    with flash
    
    "Ánh sáng chói lọi!"
    
    scene bg club_room
    with fade
    
    play music "audio/peaceful.ogg"
    
    "Cả bốn người từ từ tỉnh lại."
    "Họ đang nằm trong phòng CLB."
    
    "Đồng hồ treo tường chỉ 11:05 PM."
    "Chỉ mới 5 phút kể từ khi bắt đầu nghi thức."
    
    "TUẤN" "Chúng ta... sống sót?"
    
    "LAN" "Có vẻ vậy."
    
    "MAI" "Minh... cám ơn cậu."
    
    "MINH" "Không. Cám ơn tất cả các cậu."
    "MINH" "Chúng ta đã tin tưởng nhau."
    
    "Họ ngồi im lặng một lúc."
    "Những bí mật đã được phơi bày."
    "Những vết thương đã được tạo ra."
    
    "LAN" "Chúng ta... vẫn là bạn chứ?"
    
    "TUẤN" "Tôi muốn vậy. Nếu các cậu tha thứ cho tôi."
    
    "MAI" "Tớ cũng xin lỗi. Xin lỗi tất cả."
    
    "MINH" "Chúng ta không hoàn hảo. Nhưng chúng ta vẫn ở đây."
    "MINH" "Và đó là điều quan trọng nhất."
    
    scene bg dawn_sky
    with fade
    
    "Bên ngoài cửa sổ, bình minh đang dần ló rạng."
    
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
