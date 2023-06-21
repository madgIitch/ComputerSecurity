section .text
    global _start

_start:
    ; Escribir "Hello, World!" en la salida estándar
    mov eax, 4         ; Número de la llamada al sistema 'write'
    mov ebx, 1         ; Descriptor de archivo para la salida estándar (stdout)
    mov ecx, message   ; Dirección del mensaje
    mov edx, 13        ; Longitud del mensaje
    int 0x80           ; Llamar al sistema

    ; Salir del programa
    mov eax, 1         ; Número de la llamada al sistema 'exit'
    xor ebx, ebx       ; Código de salida 0
    int 0x80           ; Llamar al sistema

section .data
    message db "Hello, World!", 0x0a  ; Mensaje a imprimir
