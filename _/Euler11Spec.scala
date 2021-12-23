package pl.scalania.euler

import scala.io.Source

class Euler11Spec extends AbstractSpec {

  val grid = Source.fromInputStream(getClass.getClassLoader.getResourceAsStream("grid.txt")).getLines().map { line => line.split("\\s+").map(_.toInt) }.toArray

  "Largest product in a grid " should {
    "be for 4 numbers" in {
      val result = Euler11.largestProductInGrid(grid, 4)
      result should be(70600674)
    }

    "be for 1 number" in {
      val result = Euler11.largestProductInGrid(grid, 1)
      result should be(99)
    }
  }

}
