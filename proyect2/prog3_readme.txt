{\rtf1\ansi\ansicpg1252\cocoartf2708
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww13180\viewh7420\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 We have first to compile the secript with:\
\
gcc -fno-stack-protector prog3.c -o prog3\
\
then we pen GDB with:\
\
gdb prog3 \
\
and dissassemble main with:\
\
dissas main\
\
and we set a breakpoint before that the program finishes:\
\
break *main+106\
\
and we run it again with a long password and look at the buffer stack with:\
\
x/32wx $rsp\
\
that starts with 0x7fffffffde00\
\
also we look at the rip point with  the command \'93i f\'94 and it is at the point:\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 0x7fffffffde18\
\
so the difference is 24 bytes, so to overflow the buffer it has to be more of 24 bytes inserted.\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \
\
}