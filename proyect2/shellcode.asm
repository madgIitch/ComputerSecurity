section .text
    global _start

_start:
    ; Prepare arguments for write system call
    xor eax, eax             ; File descriptor (0 = stdin)
    mov ebx, eax             ; Buffer (stdin)
    xor ecx, ecx             ; Message offset
    mov edx, 11              ; Message length (11 characters)
    
    ; Invoke write system call
    mov al, 4                ; System call number for write
    int 0x80                 ; Interrupt to invoke the kernel
    
    ; Exit program
    xor eax, eax             ; System call number for exit
    inc eax                  ; Exit status (1)
    int 0x80                 ; Interrupt to invoke the kernel
