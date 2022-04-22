#include <stdio.h>

double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    return a / b;
}

int main() {
    char op;
    double first, second;

    // Get values and operator
    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &op);
    printf("Enter two operants: ");
    scanf("%lf %lf", &first, &second);

    // Switch between possible operations
    switch(op) {
        case '+':
            printf("%.1f + %.1f = %.1f", first, second, add(first, second));
            break;
        case '-':
            printf("%.1f - %.1f = %.1f", first, second, subtract(first, second));
            break;
        case '*':
            printf("%.1f * %.1f = %.1f", first, second, multiply(first, second));
            break;
        case '/':
            printf("%.1f / %.1f = %.1f", first, second, divide(first, second));
            break;
        default:
            printf("ERROR! No such operants.");
    }
    return 0;
}
