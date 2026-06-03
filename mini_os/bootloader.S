.code16
.global _start

_start:
    cli
    xorw %ax, %ax
    movw %ax, %ds
    movw %ax, %es
    movw %ax, %ss
    movw $0x7c00, %sp

    movw $0x1000, %bx
    movb $0x02, %ah
    movb $1, %al
    movb $0, %ch
    movb $2, %cl
    movb $0, %dh
    int $0x13
    jc disk_error

    movb $0x0e, %ah
    movb $'R', %al
    int $0x10

    lgdt gdt_descriptor

    movl %cr0, %eax
    orl $1, %eax
    movl %eax, %cr0

    ljmpl $0x08, $protected_mode
disk_error:
    movb $0x0e, %ah
    movb $'E', %al
    int $0x10

hang16:
    jmp hang16

gdt_start:
    .quad 0x0000000000000000
    .quad 0x00cf9a000000ffff
    .quad 0x00cf92000000ffff
gdt_end:

gdt_descriptor:
    .word gdt_end - gdt_start - 1
    .long gdt_start

.code32
protected_mode:
    movw $0x10, %ax
    movw %ax, %ds
    movw %ax, %es
    movw %ax, %fs
    movw %ax, %gs
    movw %ax, %ss

    movl $0x90000, %esp

    movb $'P', 0xb8000
    movb $0x07, 0xb8001

    movl $0x1000, %eax
    call *%eax
hang32:
    jmp hang32

.org 510
.word 0xaa55
