#include <stdio.h>
#include <unistd.h>  //Header file for sleep function
int value;
void displayMessage()
{
    printf("Enter some value\n");
    scanf("The value is %d\t",&value);
    printf("C Program Running inside a container\n");
}
int main()
{
    for(int i=0; i<100; i++)
    {
        displayMessage();
        sleep(1);
    }
    return 0;
}
