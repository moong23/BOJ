#include <stdio.h>

void add_element(int value, int set[], int* cp);
void delete_element(int value, int set[], int* cp);
int has_element(int value, int set[], const int* cp);
void print_set(int set[], const int* cp);

int main(void) {
    char alphabet;
    int arr[1][20], num = 0, temp;

    printf("Commands : a 5 ==> adds 5 to the set.\n");
    printf("           d 5 ==> deletes 5 from set.\n");
    printf("           q ==> quit\n");
    printf("======================================\n");

    while (1) {
        int i, j, cp;
        printf("Enter commands : ");
        scanf("%c", &alphabet);

        for (i = 0; i < 20; i++) {
            temp = has_element(num, arr[0][i], &cp);
        }

        i = 0;

        // if (alphabet == 'a') {
        // 	add_element(temp, arr[i], &temp);
        // 	arr[0][i] = num;
        // 	i++;
        // }
        // else if (arr[0][0] = 'd') {
        // 	for (i++;arr[0][i] == j;j++) {

        // 	}
        // }
        switch ((int)alphabet) {
            case 'a':
                printf("a input\n");
                scanf("%d", &num);
                add_element(temp, arr[i], &temp);
                arr[0][i] = num;
                i++;
                break;
            case 'd':
                printf("d input\n");
                scanf("%d", &num);
                //
                break;
            case 'q':
                printf("q input\n");
                return 0;
            default:
                printf("%c input\n", alphabet);
                printf("wrong command. try again.\n");
                break;
        }
    }
}

void add_element(int value, int set[], int* cp) {
    set[*cp] = value;
    *cp++;
}

void delete_element(int value, int set[], int* cp) {
}

int has_element(int value, int set[], const int* cp) {
    int i;
    for (i = 0; i < *cp; i++) {
        if (set[i] == 0) {
            return set[i];
        }

        else {
            return -1;
        }
    }
}

void print_set(int set[], const int* cp) {
    int i;
    for (i = 0; i < *cp; i++) {
        printf("%d ", set[i]);
    }
}
