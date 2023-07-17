	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0	sdk_version 12, 1
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #128                    ; =128
	stp	x29, x30, [sp, #112]            ; 16-byte Folded Spill
	add	x29, sp, #112                   ; =112
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	wzr, [x29, #-4]
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	mov	x9, sp
	sub	x8, x29, #8                     ; =8
	str	x8, [x9]
	bl	_scanf
LBB0_1:                                 ; =>This Inner Loop Header: Depth=1
	ldur	w8, [x29, #-8]
	subs	w9, w8, #1                      ; =1
	stur	w9, [x29, #-8]
	cbz	w8, LBB0_15
; %bb.2:                                ;   in Loop: Header=BB0_1 Depth=1
	adrp	x0, l_.str.1@PAGE
	add	x0, x0, l_.str.1@PAGEOFF
	mov	x9, sp
	sub	x8, x29, #12                    ; =12
	str	x8, [x9]
	sub	x8, x29, #20                    ; =20
	str	x8, [x9, #8]
	sub	x8, x29, #16                    ; =16
	str	x8, [x9, #16]
	sub	x8, x29, #24                    ; =24
	str	x8, [x9, #24]
	sub	x8, x29, #28                    ; =28
	str	x8, [x9, #32]
	sub	x8, x29, #32                    ; =32
	str	x8, [x9, #40]
	bl	_scanf
	ldur	w8, [x29, #-12]
	ldur	w9, [x29, #-16]
	subs	w8, w8, w9
	scvtf	d0, w8
	fmov	d1, #2.00000000
	str	d1, [sp, #56]                   ; 8-byte Folded Spill
	bl	_pow
	ldr	d1, [sp, #56]                   ; 8-byte Folded Reload
	stur	d0, [x29, #-48]                 ; 8-byte Folded Spill
	ldur	w8, [x29, #-20]
	ldur	w9, [x29, #-24]
	subs	w8, w8, w9
	scvtf	d0, w8
	bl	_pow
	mov.16b	v1, v0
	ldur	d0, [x29, #-48]                 ; 8-byte Folded Reload
	fadd	d0, d0, d1
	fcvt	s0, d0
	stur	s0, [x29, #-36]
	ldur	s0, [x29, #-36]
	fcvt	d0, s0
	fsqrt	d0, d0
	fcvt	s0, d0
	stur	s0, [x29, #-36]
	ldur	w8, [x29, #-28]
                                        ; implicit-def: $x11
	mov	x11, x8
	ldur	w8, [x29, #-32]
                                        ; implicit-def: $x9
	mov	x9, x8
	ldur	w8, [x29, #-28]
	ldur	w10, [x29, #-32]
	add	w10, w8, w10
	ldur	s0, [x29, #-36]
	fcvt	d0, s0
	adrp	x0, l_.str.2@PAGE
	add	x0, x0, l_.str.2@PAGEOFF
	mov	x8, sp
	str	x11, [x8]
	str	x9, [x8, #8]
                                        ; implicit-def: $x9
	mov	x9, x10
	str	x9, [x8, #16]
	str	d0, [x8, #24]
	bl	_printf
	ldur	s0, [x29, #-36]
	fcmp	s0, #0.0
	b.ne	LBB0_5
; %bb.3:                                ;   in Loop: Header=BB0_1 Depth=1
	ldur	w8, [x29, #-28]
	ldur	w9, [x29, #-32]
	subs	w8, w8, w9
	b.ne	LBB0_5
; %bb.4:                                ;   in Loop: Header=BB0_1 Depth=1
	adrp	x0, l_.str.3@PAGE
	add	x0, x0, l_.str.3@PAGEOFF
	bl	_puts
	b	LBB0_14
LBB0_5:                                 ;   in Loop: Header=BB0_1 Depth=1
	ldur	s0, [x29, #-36]
	ldur	w8, [x29, #-28]
	ldur	w9, [x29, #-32]
	add	w8, w8, w9
	scvtf	s1, w8
	fcmp	s0, s1
	b.pl	LBB0_7
; %bb.6:                                ;   in Loop: Header=BB0_1 Depth=1
	adrp	x0, l_.str.4@PAGE
	add	x0, x0, l_.str.4@PAGEOFF
	bl	_puts
	b	LBB0_13
LBB0_7:                                 ;   in Loop: Header=BB0_1 Depth=1
	ldur	s0, [x29, #-36]
	ldur	w8, [x29, #-28]
	ldur	w9, [x29, #-32]
	add	w8, w8, w9
	scvtf	s1, w8
	fcmp	s0, s1
	b.ne	LBB0_9
; %bb.8:                                ;   in Loop: Header=BB0_1 Depth=1
	adrp	x0, l_.str.5@PAGE
	add	x0, x0, l_.str.5@PAGEOFF
	bl	_puts
	b	LBB0_12
LBB0_9:                                 ;   in Loop: Header=BB0_1 Depth=1
	ldur	s0, [x29, #-36]
	ldur	w8, [x29, #-28]
	ldur	w9, [x29, #-32]
	add	w8, w8, w9
	scvtf	s1, w8
	fcmp	s0, s1
	b.le	LBB0_11
; %bb.10:                               ;   in Loop: Header=BB0_1 Depth=1
	adrp	x0, l_.str.6@PAGE
	add	x0, x0, l_.str.6@PAGEOFF
	bl	_puts
LBB0_11:                                ;   in Loop: Header=BB0_1 Depth=1
LBB0_12:                                ;   in Loop: Header=BB0_1 Depth=1
LBB0_13:                                ;   in Loop: Header=BB0_1 Depth=1
LBB0_14:                                ;   in Loop: Header=BB0_1 Depth=1
	b	LBB0_1
LBB0_15:
	mov	w0, #0
	ldp	x29, x30, [sp, #112]            ; 16-byte Folded Reload
	add	sp, sp, #128                    ; =128
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"%d"

l_.str.1:                               ; @.str.1
	.asciz	"%d %d %d %d %d %d"

l_.str.2:                               ; @.str.2
	.asciz	"***%d %d %d %f\n"

l_.str.3:                               ; @.str.3
	.asciz	"-1"

l_.str.4:                               ; @.str.4
	.asciz	"0"

l_.str.5:                               ; @.str.5
	.asciz	"1"

l_.str.6:                               ; @.str.6
	.asciz	"2"

.subsections_via_symbols
