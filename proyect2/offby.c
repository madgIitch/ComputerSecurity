#include <stdio.h>
#include <string.h>

void save(char* str) {
    char buff[256];
    strncpy(buff, str, strlen(str) + 1);
}

void function(char* str) {
    save(str);
}

int main(int argc, char* argv[]) {
    
    if (strlen(argv[1]) > 256)
        printf("Entrada fuera de tamaño.\n");
    else
        function(argv[1]);

    return 0;
}
