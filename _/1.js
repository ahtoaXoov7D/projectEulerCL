//const scriptArgs = process.argv.slice(2);
// console.log(scriptArgs);

// const scriptArgs1 =  scriptArgs[0];

// console.log(scriptArgs1, scriptArgs2);
let i, sum = 0; for (i = 0; i < 1000; i++) {((i % 3 == 0) || (i % 5 == 0)) ? sum += i : " ";}
console.log(sum);