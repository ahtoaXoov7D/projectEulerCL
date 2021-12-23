enum BigNumSign {
    case Negative
    case Positive
}

struct BigNum : CustomDebugStringConvertible {
    let sign:BigNumSign
    let digits:[Int]

    init(sign:BigNumSign, digits:[Int]) {
        self.sign = sign
        self.digits = digits
    }

    init(i:Int) {
        if i==0 {
            self.init(sign:BigNumSign.Positive, digits:[0])
        } else {
            var tmpI = i
            var tmpDigits = [Int]()

            var sign:BigNumSign

            if i>0 {
                sign = BigNumSign.Positive
            } else {
                sign = BigNumSign.Negative
                tmpI = -i
            }

            while tmpI > 0 {
                let remainder = tmpI % 10
                tmpDigits.append(remainder)
                tmpI = tmpI/10
            }

            self.init(sign:sign, digits:Array(tmpDigits.reverse()))
        }
    }

    init(sign:BigNumSign, digitString:String) {
        var tmpDigits = [Int]()
        for i in 0...digitString.length-1 {
            if let digit = Int(digitString[i]) {
                tmpDigits.append(digit)
            }
        }
        self.init(sign:sign, digits:tmpDigits)
    }

    var debugDescription:String {
        get {
            return (self.sign == BigNumSign.Negative ? "-" : "") + digits.reduce("") { $0 + String($1) }
        }
    }
}

func + (lhs: BigNum, rhs: BigNum) -> BigNum {
    return lhs // TODO: implement this
}

func * (lhs: BigNum, rhs: Int) -> BigNum {
    return lhs // TODO: implement this
}

func * (lhs: BigNum, rhs: BigNum) -> BigNum {
    return lhs // TODO: implement this
}
