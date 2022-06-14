	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0	sdk_version 12, 1
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	adrp	x8, _a@GOTPAGE
	ldr	x8, [x8, _a@GOTPAGEOFF]
	ldr	w9, [x8, #1828]
	adrp	x8, _k@GOTPAGE
	ldr	x8, [x8, _k@GOTPAGEOFF]
	str	w9, [x8]
	adrp	x9, _d1@GOTPAGE
	ldr	x9, [x9, _d1@GOTPAGEOFF]
	mov	w0, #0
	str	wzr, [x9]
	ldr	w9, [x8]
	adrp	x8, _d2@GOTPAGE
	ldr	x8, [x8, _d2@GOTPAGEOFF]
	str	w9, [x8]
	adrp	x9, _cc@GOTPAGE
	ldr	x9, [x9, _cc@GOTPAGEOFF]
	str	x8, [x9]
	ret
	.cfi_endproc
                                        ; -- End function
	.comm	_a,4000,2                       ; @a
	.comm	_k,4,2                          ; @k
	.comm	_d1,4,2                         ; @d1
	.comm	_d2,4,2                         ; @d2
	.comm	_cc,8,3                         ; @cc
	.comm	_dep,20,2                       ; @dep
.subsections_via_symbols
