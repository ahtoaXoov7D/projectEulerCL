let squared_sum = 0, total_sum = 0;
for(let i = 1; i <= 100; i++){squared_sum += i * i; total_sum += i;}
console.log((total_sum * total_sum) - squared_sum);