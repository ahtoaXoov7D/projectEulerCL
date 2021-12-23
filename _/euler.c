#include <stdio.h>
#include <math.h>
#include <string.h>


/* Euler #1
 * Answer: 233168
 *
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */
int euler1() {
    int i=1, n=0;
    for (;i<1000; i++) {
        if ((i % 3 == 0) || (i % 5 ==0)) {
            n += i;
        }
    }
    return n;
}

/* Euler #2
 * Answer: 
 *
 * Each new term in the Fibonacci sequence is generated by adding the
 * previous two terms. By starting with 1 and 2, the first 10 terms will be:
 *
 * 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 *
 * Find the sum of all the even-valued terms in the sequence which do not
 * exceed four million.
 */
int euler2() {
    int n = 2, a = 1, b = 2;
    while (1) {
        int c = a + b;
        if (4000000 <= c) {
            break;
        }
        if (0 == c % 2) {
            n += c;
        }
        a = b;
        b = c;
    }
    return n;
}

int is_prime(n) {
    int i = ceil(sqrt(n));
    for (;i > 2; i--) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

/* Euler #3:
 * Answer: 6857
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
 */
int euler3() {
    unsigned long target = 600851475143;
    int i;
    double s = sqrtl(target);
    double c = (long double)ceill(s);
    for (i = c; i > 0; i--) {
        if ((target % i == 0) && (is_prime(i))) {
            return i;
        }
    }
    return -1;
}


/* Euler #4
 * Answer: 906609
 *
 * A palindromic number reads the same both ways. The largest
 * palindrome made from the product of two 2-digit numbers is 9009 =
 * 91 99.
 *
 * Find the largest palindrome made from the product of two 3-digit
 * numbers.
 */
int same_both_ways(char *s) {
    int i = 0,
        len = strlen(s),
        mid = len/2;

    for (;i<mid; i++) {
        int j = (len - i) - 1;
        if (s[i] != s[j]) {
            return 0;
        }
    }

    return 1;
}

int euler4() {
    int result = 0, a, b, c;
    char *s;
    for (a=100; a<1000; a++) {
        for (b=100; b<1000; b++) {
            c = a * b;
            if (c > result) {
                asprintf(&s, "%d", c);
                if (same_both_ways(s)) {
                    result = c;
                }
                free(s);
            }
        }
    }
    return result;
}


/* Euler #5
 * Answer: 232792560
 *
 * 2520 is the smallest number that can be divided by each of the numbers
 * from 1 to 10 without any remainder. What is the smallest number that
 * is evenly divisible by all of the numbers from 1 to 20?
 */

int lcm(int a, int b)
{
    int n;
    for (n=1;; n++) {
        if(n % a == 0 && n % b == 0) {
            return n;
        }
    }
}

int euler5() {
    int i, result = lcm(1,2);

    for (i=2; i<20; i++) {
        result = lcm(result, i);
    }
    return result;
}


/* Problem #6
 * Answer: 25164150
 *
 * The sum of the squares of the first ten natural numbers is,
 *     1² + 2² + ... + 10² = 385
 * The square of the sum of the first ten natural numbers is,
 *     (1 + 2 + ... + 10)² = 55² = 3025
 * Hence the difference between the sum of the squares of the first
 * ten natural numbers and the square of the sum is 3025 - 385 = 2640.
 *
 * Find the difference between the sum of the squares of the first one
 * hundred natural numbers and the square of the sum.
 */
int euler6() {
    int i, sum = 0, sum_of_squares = 0;
    for (i=0; i<=100; i++) {
        sum_of_squares += i*i;
        sum += i;
    }
    return (sum * sum) - sum_of_squares;
}


/* An array of the euler functions to make main easy.
 * I wonder if there's a way to eval e.g. ("euler%d", index) instead.
 */
int (*EULERS[])() = {
    euler1,
    euler2,
    euler3,
    euler4,
    euler5,
    euler6,
    NULL
};

/* main entry point.
 * If problem numbers are provided, print the solutions for each of those
 * problems, otherwise print all solutions.
 */
int main(int argc, char **argv, char **envp) 
{
    if (argc > 1) {
        int i = 1;
        for (i; i<argc; i++) {
            int n = atoi(argv[i]);
            printf("#%d: %d\n", n, EULERS[(n-1)]());
        }
    } else {
        int i = 0;
        for (; EULERS[i] != NULL; i++) {
            printf("#%d: %d\n", (i+1), EULERS[i]());
        }
    }
    return 0;
}
