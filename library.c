#include <stdio.h>
#include <stdlib.h>


int c_multiply(int x, int y) {
    int result = x * y;
    return result;
}

int c_add(int x, int y) {
    int result = x + y;
    return result;
}

int c_sub(int x, int y) {
    int result = x - y;
    return result;
}

float c_div(int x, int y) {
    float result = x / y;
    return result;
}


int c_loop(int n){
    int i, s;
    for (s = i = 0; i < n  ; i++){
        s += 1;
    }
}

int c_looper(int x, int y, int n){
    int answer = 0;
    for (int i = 0; i < n; i++){
        answer = x + y;
    }
    return answer;
}