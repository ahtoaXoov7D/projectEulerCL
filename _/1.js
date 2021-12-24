const skriptArgs = process.argv.slice(2);

let skriptprocess=skriptArgs.toString().split("");

function sum_of_all_multiples_of_x(x, t_max) {
    var i = 0; var ret = 0; 
    for (i = 1; i < t_max; i += 1) 
    {if (i % x === 0) {ret += i;}} 
    return ret;
}

console.log(
    sum_of_all_multiples_of_x(parseInt(skriptprocess[0].charCodeAt(0)), 1000),
    sum_of_all_multiples_of_x(parseInt(skriptprocess[1].charCodeAt(0)), 1000),
    sum_of_all_multiples_of_x(parseInt(skriptprocess[2].charCodeAt(0)), 1000),
    sum_of_all_multiples_of_x(parseInt(skriptprocess[3].charCodeAt(0)), 1000),
    sum_of_all_multiples_of_x(parseInt(skriptprocess[4].charCodeAt(0)), 1000),
    sum_of_all_multiples_of_x(parseInt(skriptprocess[5].charCodeAt(0)), 1000),
    sum_of_all_multiples_of_x(parseInt(skriptprocess[6].charCodeAt(0)), 1000),
    sum_of_all_multiples_of_x(parseInt(skriptprocess[7].charCodeAt(0)), 1000),
    sum_of_all_multiples_of_x(parseInt(skriptprocess[8].charCodeAt(0)), 1000),
    sum_of_all_multiples_of_x(parseInt(skriptprocess[9].charCodeAt(0)), 1000),
);
