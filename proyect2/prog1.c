#include <stdio.h>
#include <string.h>

char buffer[8]; // 8 bytes en la pos de memoria 0x4028
int val1 = 0; // 4 bytes en la pos de memoria 0x4030
int val2 = 0; // 4 bytes en la pos de memoria 0x4034

int main(int argc, char **argv){

    strcpy(buffer,argv[1]);
    printf("val1 = %d, val2 = %d\n", val1, val2);
    
    return 0;
}

