#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *str;
    str = malloc(1024 * sizeof(char));
    printf("Enter a sentence: ");
    scanf("%[^\n]", str);
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == ' ') {
            printf("\n");
        } else {
            printf("%c", str[i]);
        }
        
    }
 return 0;
}   
