package pl.scalania.euler

class Euler01Spec extends AbstractSpec {

  "Euler01 " should {
    "Multiples of 3 and 5 below 10" in {
      val result = Euler01.multipliesSum(3, 5, 10)
      result should be(23)
    }

    "Multiples of 3 and 5 below 1000" in {
      val result = Euler01.multipliesSum(3, 5, 1000)
      result should be(233168)
    }
  }

}
