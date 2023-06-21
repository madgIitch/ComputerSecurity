section .data
    message db 'hello world',0x0a  ; Null-terminated message to print

section .text
    global _start

_start:
    ; Preparar los argumentos para la llamada a la función system
    xor eax, eax              ; Limpiar eax
    mov ebx, message          ; Puntero al comando a ejecutar
    xor ecx, ecx              ; Argumento adicional (opcional)
    xor edx, edx              ; Argumento adicional (opcional)

    ; Llamada a la función system
    mov al, 0xb               ; Número de la llamada al sistema para system
    int 0x80                  ; Interrupción para invocar al kernel

    ; Exit program
    xor eax, eax              ; Número de la llamada al sistema para exit
    xor ebx, ebx              ; Código de salida (0)
    inc eax                   ; Ajustar el número de la llamada al sistema para exit
    int 0x80                  ; Interrupción para invocar al kernel
