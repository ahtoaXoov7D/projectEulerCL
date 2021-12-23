//
//  main.swift
//  SwiftEulerProblems
//
//  Created by Gabriel Ruiz on 2/11/18.
//  Copyright © 2018 Gabriel Ruiz. All rights reserved.
//

import Foundation

func euler1() -> Int {
    return Array((1..<1000)).filter({(num: Int) -> Bool in return (num % 3 == 0 || num % 5 == 0) }).reduce(0, +)
}

func euler2() -> Int {
    var matrix = fibonacciMultiplication(times: 33) // i have a paper proving why this is, sorta
    return (matrix[0][0] - 1)/2
}

func euler7() -> Int {
    return primeSieve(n: 10001)
}

var problemMap = [Int: ()->Int]()
problemMap = [
    1: euler1,
    2: euler2,
    7: euler7
]

func eulerRun(num: Int) -> Int {
    return problemMap[num]!()
}

print(eulerRun(num: 7))

