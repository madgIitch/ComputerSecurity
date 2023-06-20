Prog1

gcc -g -o prog1 prog1.c 
chmod +x prog1.pl     
./prog1.pl


----------------------
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


