#include <stdio.h>
#include <string.h>

void vulnerableFunction(char *input) {
    char buffer[8];
    strcpy(buffer, input);
}

int main() {
    char input[16];
    printf("Ingrese su entrada: ");
    gets(input);
    vulnerableFunction(input);
    printf("Fin del programa.\n");
    return 0;
}
