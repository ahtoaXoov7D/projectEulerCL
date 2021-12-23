;; Euler #1
;; Answer: 233168
;;
;; If we list all the natural numbers below 10 that are multiples of 3 or 5,
;; we get 3, 5, 6 and 9. The sum of these multiples is 23.
;;
;; Find the sum of all the multiples of 3 or 5 below 1000.

(define (e1-accumulate n max acc)
    (if (>= n max)
        acc
        (e1-accumulate (+ n 1) max (if (or (= 0 (modulo n 3))
                                           (= 0 (modulo n 5)))
                                       (+ acc n)
                                       acc))))

(define (euler1)
    (e1-accumulate 1 1000 0))


;; Euler #2
;; Answer: 4613732
;;
;; Each new term in the Fibonacci sequence is generated by adding the previous
;; two terms. By starting with 1 and 2, the first 10 terms will be:
;;
;; 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
;;
;; Find the sum of all the even-valued terms in the sequence which do not
;; exceed four million.

(define (e2-accumulate a b acc)
    (if (>= b 4000000)
        acc
        (let ((c (+ a b)))
            (e2-accumulate b c (if (even? c)
                                   (+ acc c)
                                   acc)))))

(define (euler2)
    (e2-accumulate 1 2 2))


;; Euler #3:
;; Answer: 6857
;;
;; The prime factors of 13195 are 5, 7, 13 and 29.
;;
;; What is the largest prime factor of the number 600851475143 ?

(define (prime?-acc n x)
    (if (or (< x 2) (= n 2))
        #t
        (if (= 0 (modulo n x))
            #f
            (prime?-acc n (- x 1)))))

(define (prime? n)
    (prime?-acc n (inexact->exact (ceiling (sqrt n)))))

(define (euler3-accumulate f n)
    (if (and (= 0 (modulo n f)) (prime? f))
        f
        (euler3-accumulate (- f 1) n)))

(define (euler3)
    (let ((x 600851475143))
        (euler3-accumulate (inexact->exact (ceiling (sqrt x))) x)))


;; Problem #4
;; Answer: 906609
;;
;; A palindromic number reads the same both ways. The largest
;; palindrome made from the product of two 2-digit numbers is 9009 =
;; 91 99.
;;
;; Find the largest palindrome made from the product of two 3-digit
;; numbers.

;; This is supposed to be in the language but I can't find it / figure out
;; how to import the right namespace / whatever, so...
(define (reverse-string s)
    (list->string (reverse (string->list s))))

(define (palindromic-number? n)
    (let ((s (number->string n)))
        (string=? s (reverse-string s))))

(define (euler4-accumulate x y acc)
    (if (> y 999)
        acc
        (if (> x 999)
            (euler4-accumulate 100 (+ 1 y) acc)
            (let ((p (* x y)))
                (euler4-accumulate (+ 1 x) y (if (and (> p acc) (palindromic-number? p))
                                                  p
                                                  acc))))))

(define (euler4)
    (euler4-accumulate 100 100 0))


;; Problem #5
;; Answer: 232792560
;;
;; 2520 is the smallest number that can be divided by each of the
;; numbers from 1 to 10 without any remainder.
;;
;; What is the smallest number that is evenly divisible by all of the
;; numbers from 1 to 20?

(define (divisible-by-all? n xs)
    (if (>= 0 (length xs))
        #t
        (if (not (= 0 (modulo n (car xs))))
            #f
            (divisible-by-all? n (cdr xs)))))

(define (euler5-accumulate n)
    (if (divisible-by-all? n '(20 19 18 17 16 15 14 13 12 11))
        n
        (euler5-accumulate (+ n 1))))

(define (euler5)
    (euler5-accumulate 2520))


;; Problem #6
;; Answer: 25164150
;;
;; The sum of the squares of the first ten natural numbers is,
;;     1² + 2² + ... + 10² = 385
;; The square of the sum of the first ten natural numbers is,
;;     (1 + 2 + ... + 10)² = 55² = 3025
;; Hence the difference between the sum of the squares of the first
;; ten natural numbers and the square of the sum is 3025 - 385 = 2640.
;;
;; Find the difference between the sum of the squares of the first one
;; hundred natural numbers and the square of the sum.

(define (square n)
    (* n n))

(define (sum-from-to-acc from to acc)
    (if (> from to)
        (sum-from-to-acc to from acc)
        (if (= from to)
            (+ to acc)
            (sum-from-to-acc (+ 1 from) to (+ from acc)))))

(define (sum-from-to from to)
    (sum-from-to-acc from to 0))

(define (sum-of-squares-acc from to acc)
    (if (> from to)
        (sum-of-squares-acc to from acc)
        (if (= from to)
            (+ (square to) acc)
            (sum-of-squares-acc (+ 1 from) to (+ (square from) acc)))))

(define (sum-of-squares from to)
    (sum-of-squares-acc from to 0))

(define (square-of-sum from to)
    (square (sum-from-to from to)))

(define (euler6)
    (- (square-of-sum 1 100) (sum-of-squares 1 100)))


;; Problem #7
;; Answer: 104743
;; NOTE: Way too slow, but got the right answer.
;;
;; By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
;; we can see that the 6th prime is 13.
;;
;; What is the 10001st prime number?

(define (divisible-by-any? n xs)
  (if (>= 0 (length xs))
      #f
      (if (= 0 (modulo n (car xs)))
          #t
          (divisible-by-any? n (cdr xs)))))

(define (next-prime-acc primes n)
  (if (divisible-by-any? n primes)
      (next-prime-acc primes (+ n 1))
      n))

(define (next-prime primes)
  (next-prime-acc primes (+ 1 (car primes))))

(define (find-nth-prime-acc n primes)
  (if (< n (length primes))
      (find-nth-prime-acc n (cdr primes))
      (if (= n (length primes))
          (car primes)
          (find-nth-prime-acc n (cons (next-prime primes) primes)))))

(define (find-nth-prime n)
  (find-nth-prime-acc n '(2)))

(define (euler7)
    (find-nth-prime 10001))
