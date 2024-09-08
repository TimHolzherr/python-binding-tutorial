#include <stdio.h>
#include <unistd.h>  // for sleep

int add(int a, int b) {
    sleep(5);  // Sleep for 5 secondss
    return a + b;
}
