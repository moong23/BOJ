#include <stdio.h>
#define MAX_SET 100  // 최대 집합 길이

void add_element(int value, int set[], int* cp);
/*
집합에 원소 추가(배열 끝) 중복 허용 안하므로 없을 경우에만 추가 has_element로 check
*/
void delete_element(int value, int set[], int* cp);
/*
원소 삭제 존재하는 경우에만
만약 삭제하면 나머지 한칸 왼쪽으로
원소 있는지는 has_element로 check
*/
int has_element(int value, int set[], const int* cp);
/*
원소 있는지 확인 있는경우 인덱스 변환 없으면 -1 반환
*/
void print_set(int set[], const int* cp);
/*
출력
*/
int main() {
    int value;         // 추가 또는 삭제할 원소
    int set[MAX_SET];  // 집합
    int cp = 0;        // 원소의 개수를 저장한 변수 => set의 최대 원소 개수로 생각하면 될듯

    char cmd;

    // 명령어 읽고 난 후 while(getchar() != '\n')에 의해 입력 버퍼 비움

    printf("Commands : a 5 ==> adds 5 to the set.\n");
    printf("           d 5 ==> deletes 5 from set.\n");
    printf("           q ==> quit\n");
    printf("======================================\n");

    while (1) {
        printf("Enter commands : ");
        scanf("%c", &cmd);

        switch ((int)cmd) {
            case 'a':
                scanf("%d", &value);
                while (getchar() != '\n')
                    ;
                add_element(value, set, &cp);
                break;
            case 'd':
                scanf("%d", &value);
                while (getchar() != '\n')
                    ;
                delete_element(value, set, &cp);
                break;
            case 'q':
                return 0;
                break;
            default:
                while (getchar() != '\n')
                    ;
                printf("wrong command. try again\n");
                break;
        }
        if (cmd == 'a' || cmd == 'd') {
            print_set(set, &cp);
        }
    }

    return 0;
}

void add_element(int value, int set[], int* cp) {
    // printf("add_element\n%d, %d\n", value, *cp);
    if (*cp == 99) {
        printf("max set range\n");
        return;
    }
    if (has_element(value, set, cp) != -1) {
        printf("%d is already in the set.\n", value);
        return;
    }
    set[*cp] = value;
    *cp += 1;
    // printf("*cp: %d\n", *cp);
    return;
}

void delete_element(int value, int set[], int* cp) {
    // printf("delete_element\n%d, %d\n", value, *cp);
    int tmp = has_element(value, set, cp);
    if (tmp == -1) {
        printf("%d is not in the set.\n", value);
        return;
    }
    for (int i = tmp; i < *cp - 1; i++) {
        set[i] = set[i + 1];
    }
    *cp -= 1;
    return;
}

int has_element(int value, int set[], const int* cp) {
    int idx = -1;
    if (*cp == 0) {
        return -1;
    }
    for (int i = 0; i < *cp; i++) {
        if (value == set[i]) {
            idx = i;
            break;
        }
    }
    return idx;
}

void print_set(int set[], const int* cp) {
    // printf("print_set %d\n", *cp);
    for (int i = 0; i < *cp; i++) {
        printf("%d ", set[i]);
    }
    printf("\n");
    return;
}