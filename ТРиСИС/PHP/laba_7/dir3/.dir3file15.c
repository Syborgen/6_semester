#include <stdio.h>
#include <conio.h>
void main()
{
int I;
int J;
int C;
printf("How many meters? \n");
scanf("%d",&I);
J=100*I;
printf("%d meters contain %d centimeters \n", I,J);
C=getch();
}