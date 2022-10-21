function solution(n) {
    var answer = 0;
    let arr=[0,1]
    for(let i=2;i<=n;i++){
        let val=(arr[i-1]+arr[i-2])%1234567
        arr.push(val)
    }
    console.log(arr)
    return arr[n];
}