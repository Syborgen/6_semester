#define SIZE 16
#include <stdio.h>
main()
{
char c='A';
#ifdef SIZE
int x=123;
printf("x=%d\n",x);
#else
char (x[SIZE])="computer";
printf("x=%s\n",x);
#endif
printf("%c\n",c);
}