/*
week 2 data structure
http://acmicpc.net/problem/1406
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char leftstack[600000], rightstack[600000];
int l_top = -1, r_top = -1;

void toLeft()
{
    //printf("to the left!\n");
    rightstack[++r_top] = leftstack[l_top--];
    leftstack[l_top + 1] = '\0';
}

void toRight()
{
    // printf("to the right!\n");
    leftstack[++l_top] = rightstack[r_top--];
    rightstack[r_top + 1] = '\0';
}

void del_stack()
{
    // printf("deleting the stack!\n");
    leftstack[l_top] = '\0';
    l_top--;
}

void add_stack(char value)
{
    // printf("adding the stack! : %c\n", value);
    leftstack[++l_top] = value;
}

int main()
{
    char cursor, target;
    int num, length;
    scanf("%s", leftstack);

    // printf("%c\n", leftstack[2]);
    l_top = strlen(leftstack) - 1;
    //    printf("l_top: %d\n", l_top);

    scanf("%d", &num);
    while (num--)
    {
        scanf("%s", &cursor);
        //        printf("this is cursor: %c\n", cursor);
        if (cursor == 'L')
        { //cursor move left
            if (l_top != -1)
            {
                toLeft();
            }
        }
        else if (cursor == 'D')
        { //cursor move right
            if (r_top != -1)
            {
                toRight();
            }
        }
        else if (cursor == 'B')
        { //del
            if (l_top != -1)
            {
                del_stack();
            }
        }
        else if (cursor == 'P')
        {
            scanf(" %c", &target);
            add_stack(target);
        }
        //        printf("\nafter doing %c\nleftstack:%s\nrightstack:%s\n\n", cursor, leftstack, rightstack);
    }
    while (r_top != -1)
        toRight();
    printf("%s%s\n", leftstack, rightstack);

    return 0;
}