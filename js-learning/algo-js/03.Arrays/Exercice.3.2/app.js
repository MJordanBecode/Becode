let arr=[1, 2, 3, 4, 5], arr2=[100, 101, 102]; sum=0; sum2=0;

for(let i=0;i<arr.length;i++){
    sum += arr[i];
    console.log(sum);
}
sum = sum / arr.length;
console.log(sum);

for(let i=0;i<arr2.length;i++){
    sum2 += arr2[i];
    console.log(sum2);
}
sum2 = sum2 / arr2.length;
console.log(sum2);