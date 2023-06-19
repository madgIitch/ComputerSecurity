Prog1

Se ha depurado el programa original con el fin de saber donde estaban situadas las posiciones de memoria. 
Sabiendo que:

char buffer[8] --> 8 bytes en la pos de memoria 0x4028
int val1 --> 4 bytes en la pos de memoria 0x4030
int val2 --> 4 bytes en la pos de memoria 0x4034

Sabiendo que C no tiene un endianess determinado, sino que se adapta a las características de la máquina en la que se ejecuta, se ha comprobado que en la máquina en la que se ha ejecutado el programa, 
el endianess es little endian. Por lo tanto, buffer será la variable que se escriba primero en memoria, luego val1, siendo val2 la última.

Los comandos que se usan para depurar a través de gdb son:
gcc -g -o mi_programa mi_programa.c 
gdb mi_programa
run

Una vez está corriendo el programa, se puede usar el comando print &variable para saber la posición de memoria de la variable.

Para saber el endianess de la máquina, se puede usar el comando info target. En el caso de la máquina en la que se ha ejecutado el programa, el endianess es little endian.


