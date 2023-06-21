hello

nasm -f elf32 hello.asm -o hello.o
ld -m elf_i386 hello.o -o hello.bin
ld -m elf_i386 -o hello hello.o
./hello

gcc -g -o hello hello.c

./hello

readelf -a hello.bin | grep "Entry point address"



----------------------
carga util --> \x00\x90\x04\x08


--------------------------------

hello segunda vuelta

nasm -f elf32 -o helloShellcode.o helloShellcode.asm
ld -m elf_i386 -o helloShellcode helloShellcode.o

gcc -m32 -z execstack -fno-stack-protector -o hello hello.c

./helloShellcode | ./hello

----------------------

sudo -bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'

gcc -fno-stack-protector hello.c -o hello

gdb hello

rip located at 0x7fffffffde18 and our buffer at 0x7fffffffde08 --> 16 bytes of difference.

gcc -o 

-----------------------------------

nasm -f elf32 shellcode.asm -o shellcode.o
ld -m elf_i386 shellcode.o -o shellcode

gcc -m32 -fno-stack-protector -z execstack hello.c -o hello

gdb hello
break vulnerableFunction
run <<< $(python -c 'print("A" * 20)')
