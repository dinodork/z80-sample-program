Player_Left_Loop_End:    EQU 0x00
Player_Left_Loop_Start:  EQU 0x03
Player_Center:           EQU 0x04
Player_Right_Loop_Start: EQU 0x05
Player_Right_Loop_End:   EQU 0x08

; Description of the animation
; The animation proceeds as follows:

;   Loop
;   ___
;  |   v
; +-+-+-+-+-+-+-+-+-+
; |2|1|2|3|4|5|6|7|6|
; +-+-+-+-+-+-+-+-+-+
;              ^   |
;               \--
;              Loop
Player_Frames:
    DW Player_left_2, Player_left_1, Player_left_2, Player_left_3
    DW Player_center_1
    DW Player_right_1, Player_right_2, Player_right_3, Player_right_2
