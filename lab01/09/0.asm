	.file	"main.cpp"
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
.LFB2036:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$48, %rsp
	.seh_stackalloc	48
	.seh_endprologue
	call	__main
	movl	$0, -4(%rbp)                    -4(%rbp)=s      ;   s=0
	leaq	-12(%rbp), %rax                 -12(%rbp)=x     ;|
	movq	.refptr._ZSt3cin(%rip), %rcx                    ;|
	movq	%rax, %rdx                                      ;|  cin >> x
	call	_ZNSirsERi                                      ;|
	movl	$0, -8(%rbp)                    -8(%rbp)=i      ;   i=0
	jmp	.L2
.L3:
	movl	-12(%rbp), %eax                                 ;   eax = x
	addl	%eax, -4(%rbp)                                  ;   s += eax
	addl	$1, -8(%rbp)                                    ;   i += 1
.L2:
	cmpl	$122, -8(%rbp)                                  ;   сравнить i и 122
	jle	.L3                                                 ;   если i>122 то перейти на L3
	movl	-4(%rbp), %edx                                  ;|
	movq	.refptr._ZSt4cout(%rip), %rax                   ;|
	movq	%rax, %rcx                                      ;|  cout << s
	call	_ZNSolsEi                                       ;|
	movl	$0, %eax
	addq	$48, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.ident	"GCC: (x86_64-win32-seh-rev0, Built by MinGW-Builds project) 15.2.0"
	.def	_ZNSirsERi;	.scl	2;	.type	32;	.endef
	.def	_ZNSolsEi;	.scl	2;	.type	32;	.endef
	.section	.rdata$.refptr._ZSt4cout, "dr"
	.p2align	3, 0
	.globl	.refptr._ZSt4cout
	.linkonce	discard
.refptr._ZSt4cout:
	.quad	_ZSt4cout
	.section	.rdata$.refptr._ZSt3cin, "dr"
	.p2align	3, 0
	.globl	.refptr._ZSt3cin
	.linkonce	discard
.refptr._ZSt3cin:
	.quad	_ZSt3cin
