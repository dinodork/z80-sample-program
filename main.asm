;===========================================================================
; main.asm
;===========================================================================

    SLDOPT COMMENT WPMEM, LOGPOINT, ASSERTION

NEX:    equ 0   ;  1=Create nex file, 0=create sna file

    IF NEX == 0
        ;DEVICE ZXSPECTRUM128
        DEVICE ZXSPECTRUM48
        ;DEVICE NOSLOT64K
    ELSE
        DEVICE ZXSPECTRUMNEXT
    ENDIF

    ORG 0x4000
    defs 0x6000 - $    ; move after screen area
screen_top: defb    0   ; WPMEMx


;===========================================================================
; Persistent watchpoint.
; Change WPMEMx (remove the 'x' from WPMEMx) below to activate.
; If you do so the program will hit a breakpoint when it tries to
; write to the first byte of the 3rd line.
; When program breaks in the fill_memory sub routine please hover over hl
; to see that it contains 0x5804 or COLOR_SCREEN+64.
;===========================================================================

; WPMEMx 0x5840, 1, w


;===========================================================================
; Include modules
;===========================================================================
    include "utilities.asm"
    include "fill.asm"
    include "clearscreen.asm"
    include "src/demo_sprites.z80"

    ; Normally you would assemble the unit tests in a separate target
    ; in the makefile.
    ; As this is a very short program and for simplicity the
    ; unit tests and the main program are assembled in the same binary.
    include "unit_tests.asm"


;===========================================================================
; main routine - the code execution starts here.
; Sets up the new interrupt routine, the memory
; banks and jumps to the start loop.
;===========================================================================


 defs 0x8000 - $
 ORG $8000

Stack_Top:		EQU 0xFFF0
			LD SP, Stack_Top

main:
jqqw
	DI
	LD SP, Stack_Top
	LD A,38h
	CALL Clear_Screen
	LD IX, Text_Scores
	CALL Print_String
	CALL Initialise_Sprites
	LD HL, Interrupt
	LD IX, 0xFFF0
	LD (IX + 04h), 0xC3	   ; Opcode for JP
	LD (IX + 05h), L
	LD (IX + 06h), H
	LD (IX + 0Fh), 0x18	    ; Opcode for JR; this will do JR to FFF4h
	LD A, 0x39
	LD I, A
	IM 2
	EI

LOOP:
	HALT
	CALL Read_Keyboard
	JR LOOP

;===========================================================================
; Stack.
;===========================================================================


; Stack: this area is reserved for the stack
STACK_SIZE: equ 100    ; in words


; Reserve stack space
    defw 0  ; WPMEM, 2
stack_bottom:
    defs    STACK_SIZE*2, 0
stack_top:
    ;defw 0
    defw 0  ; WPMEM, 2



    IF NEX == 0
        SAVESNA "z80-sample-program.sna", main
    ELSE
        SAVENEX OPEN "z80-sample-program.nex", main, stack_top
        SAVENEX CORE 3, 1, 5
        SAVENEX CFG 7   ; Border color
        SAVENEX AUTO
        SAVENEX CLOSE
    ENDIF
