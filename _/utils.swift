//
//  utils.swift
//  SwiftEulerProblems
//
//  Created by Gabriel Ruiz on 2/12/18.
//  Copyright © 2018 Gabriel Ruiz. All rights reserved.
//

import Foundation

// greatest common divisor algorithm
internal func gcd(a: Int, b: Int) -> Int {
    if (b == 0) {
        return a
    }
    else {
        return gcd(a: b, b: a % b)
    }
}

// matrix multiplication: internal
internal func matrixMultiply (first: [[Int]], second: [[Int]]) -> [[Int]] {
    var finalMatrix = Array(repeating: [Int]() , count: first.count)
    for i in 0..<first.count {
        for j in 0..<second[0].count {
            var sum = 0
            for k in 0..<first[0].count {
                sum = sum + first[i][k] * second[k][j]
            }
            finalMatrix[i].append(sum)
        }
    }
    return finalMatrix
}

// matrix exponentiation for fibonacci numbers
public func fibonacciMultiplication (times: Int) -> [[Int]] {
    let multiplier = [
        [1,1],
        [1,0]
    ]
    
    var changedMatrix = [
        [1,1],
        [1,0]
    ]
    
    var i = 0
    repeat {
        changedMatrix = matrixMultiply(first: changedMatrix, second: multiplier)
        i += 1
    } while (i < times)
    
    return changedMatrix
}

// function to detect the nth prime number
public func primeSieve(n: Int) -> Int {
    let estimatePrime = Int(2.0 * Double(n) * log2(Double(n)))
    var sieve = Array(repeating: true, count: estimatePrime)
    var count = 0
    for i in 2..<estimatePrime {
        if (sieve[i]) {
            count += 1
            if (count == n) {
                return i
            }
            for j in stride(from: 2*i, to: estimatePrime, by: i) {
                sieve[j] = false
            }
        }
    }
    return 2
}

