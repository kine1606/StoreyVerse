
define character.main = Character("Main", image = "aoto", what_prefix = '(', what_suffix = ')',)
# label start:
#     show sora
#     "Hello"
#     define point = 0
#     define unlock_ending = False
#     scene bg old cafe
#     "haha"
#     jump shop

#     return

label shop:
    scene bg old encorekitchena
    
    if point >= 50:
        $unlock_ending = True

    call screen options

screen options:
    # text "point = [point]"

    imagebutton:
        xpos 550
        idle "images/Glasses/aoto casual glasses closed frown blush.png"
        action Jump("shopInside")
    
    imagebutton:
        xpos 950
        idle "images/Glasses/aoto casual glasses smile.png"
        action Jump("workForMoney")

    imagebutton:
        idle "images/Glasses/aoto casual glasses smile.png"
        action Jump("ending")

label shopInside:
    "wtf"
    jump shop
    
label workForMoney:
    $point +=10
    "you work! point = [point]"

    jump shop

label ending:
    if unlock_ending:
        scene bg old templeday 
        "You won!"
    else:
        "not enough point"
        jump shop
