section .text
    global _start

_start:
    ; Colocar aquí el shellcode

    ; Llamada a la función save
    ; Puedes cambiar el tamaño del búfer si lo deseas
    ; Recuerda que debes ajustar los offsets en consecuencia
    mov ebx, esp
    add ebx, 512
    push ebx
    call save

    ; Salir del programa
    mov eax, 1
    xor ebx, ebx
    int 0x80

; Definición de la función save
save:
    ; Reservar espacio en el stack para la variable buff
    sub esp, 256

    ; Copiar el contenido de la cadena proporcionada por el usuario al buffer
    mov ecx, esp
    mov edi, [esp+4]
    mov esi, edi
    mov edx, edi
    xor eax, eax
    mov al, byte [edi-1]
    add edx, eax
    shr edx, 0x2
    mov eax, edi
    and eax, 0x3
    sub edx, eax
    mov eax, edx
    sub ecx, eax
    shr edx, 0x2
    and eax, 0x3
    rep movsd
    mov ecx, edx
    rep movsb

    ; Retornar
    ret
