section .data
    message db 'hola chavales',0

section .text
    global _start

_start:
    ; Escribir la cadena en la salida estándar
    mov eax, 4
    mov ebx, 1
    mov ecx, message
    mov edx, 11
    int 0x80

    ; Salir del programa
    mov eax, 1
    xor ebx, ebx
    int 0x80
