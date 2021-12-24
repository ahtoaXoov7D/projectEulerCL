let four_m = process.argv.slice(2); 

var fibo = {
    a : 1, b : 1,
    next : function(){let sum = this.a + this.b; this.a = this.b; this.b = sum; return sum;},
    b_is_even : function(){if (this.b %2 == 0) {return true;} 
    else {return false;}},
};

function find_fibo(t_max) {
    let sum = 0; let re = fibo.next();
    while (re < t_max) {if (fibo.b_is_even()) {sum += fibo.b} re = fibo.next()}
    return sum
}

let ret = find_fibo(parseInt(four_m[0])*1000);
console.log(ret);
