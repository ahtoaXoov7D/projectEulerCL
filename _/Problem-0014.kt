package euler.problem0014

import euler.multipleOf
import euler.plus

import java.util.Collection
import java.util.List

fun main(args : Array<String>) {
  val limit = 1000000

  // average execution time of 590.8156 milliseconds over 10 iterations
  val result = (1..limit).map { (n: Int) -> #(n, lengthOfSequence(n.toLong())) }.max()

  val chain = sequence(result._1.toLong())
  println("the longest chain below $limit starts with ${result._1} and has ${chain.size()} elements:\n$chain")
}

inline fun lengthOfSequence(n: Long, length: Int = 0): Int {
  return if (n == 1.toLong()) length + 1 else lengthOfSequence(if (n multipleOf 2) (n / 2) else (3 * n + 1), length + 1)
}

inline fun List<#(Int, Int)>.max() = fold(#(0, 0)) { (a, b) -> if (a._2 > b._2) a else b }

inline fun sequence(n: Long): List<Long> {
  if (n == 1.toLong()) return arrayList(n)
  return if (n multipleOf 2) n + sequence(n / 2) else n + sequence(3 * n + 1)
}
