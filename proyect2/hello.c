#include <stdio.h>
#include <string.h>

void vulnerableFunction(char* input) {
    char buffer[8];
    strcpy(buffer, input);
    printf("Buffer content: %s\n", buffer);
}

int main() {
    char input[16];
    printf("Enter your input: ");
    scanf("%s", input);
    vulnerableFunction(input);
    return 0;
}
