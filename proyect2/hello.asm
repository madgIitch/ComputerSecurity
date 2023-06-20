section .text
    global _start

_start:
    ; Imprimir el mensaje "Ingrese su entrada: "
    mov eax, 4
    mov ebx, 1
    mov ecx, mensaje1
    mov edx, mensaje1len
    int 0x80

    ; Leer la entrada del usuario
    mov eax, 3
    mov ebx, 0
    mov ecx, buffer
    mov edx, 32
    int 0x80

    ; Realizar el buffer overflow y sobrescribir el valor de retorno
    lea edi, [esp+0x20]
    add edi, 12
    mov dword [edi], 0x6c6c6568

    ; Imprimir el mensaje "hello world"
    mov eax, 4
    mov ebx, 1
    mov ecx, mensaje2
    mov edx, mensaje2len
    int 0x80

    ; Finalizar el programa
    mov eax, 1
    xor ebx, ebx
    int 0x80

section .data
    mensaje1 db "Ingrese su entrada: ", 0
    mensaje1len equ $ - mensaje1

    mensaje2 db "hello world", 0
    mensaje2len equ $ - mensaje2

section .bss
    buffer resb 32
