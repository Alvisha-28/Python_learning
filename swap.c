#swapping two numbers using a temporary variable using functions
#include <stdio.h>
void swap(int *a, int *b) {
    int temp; // temporary variable to hold the value during swapping
    temp = *a; // store the value at address a in temp
    *a = *b;   // assign the value at address b to address a
    *b = temp; // assign the value stored in temp to address b
}
int main() {
    int num1, num2;
    
    // Input two numbers from the user
    printf("Enter two numbers to swap: ");
    scanf("%d %d", &num1, &num2);
    
    // Display the numbers before swapping
    printf("Before swapping: num1 = %d, num2 = %d\n", num1, num2);
    
    // Call the swap function
    swap(&num1, &num2);
    
    // Display the numbers after swapping
    printf("After swapping: num1 = %d, num2 = %d\n", num1, num2);
    
    return 0;
}