//based on Syntax 2
#include <iostream> 
using namespace std; 
// function to print numbers from 1 to 5
void printNumbers() 
{ 
int n = 1; 
print:
cout << n << " "; 
n++; 
if (n <= 5) 
goto print; 
} 
// main method to test above function 
int main() 
{ 
printNumbers(); 
return 0; 
}