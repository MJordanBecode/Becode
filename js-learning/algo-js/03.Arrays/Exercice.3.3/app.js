let arr=[1,2,3,4,5]; arr2=[]; safe=0;

console.log(arr);
for(let i = 0;i<arr.length;i++){
    safe = arr[i];
    arr2=[safe];
    console.log(arr2);
}