const skriptArgs = process.argv.slice(2);

function sum_of_all_multiples_of_x(x, t_max) {
    var i = 0; var ret = 0;
    for (i = 1; i < t_max; i += 1) {if (i % x === 0) {ret += i;}}
    return ret;
}

console.log(sum_of_all_multiples_of_x(parseInt(skriptArgs[0]), 1000),
            sum_of_all_multiples_of_x(parseInt(skriptArgs[1]), 1000),
            sum_of_all_multiples_of_x(parseInt(skriptArgs[2]), 1000),
            sum_of_all_multiples_of_x(parseInt(skriptArgs[3]), 1000),
            sum_of_all_multiples_of_x(parseInt(skriptArgs[4]), 1000),
            sum_of_all_multiples_of_x(parseInt(skriptArgs[5]), 1000),
            sum_of_all_multiples_of_x(parseInt(skriptArgs[6]), 1000),
            sum_of_all_multiples_of_x(parseInt(skriptArgs[7]), 1000),
            sum_of_all_multiples_of_x(parseInt(skriptArgs[8]), 1000),
            sum_of_all_multiples_of_x(parseInt(skriptArgs[9]), 1000));
