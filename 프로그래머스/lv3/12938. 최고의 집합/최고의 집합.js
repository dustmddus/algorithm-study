function solution(n, s) {
    if(n>s)return [-1]
    if(s%n===0){
        let ans=s/n
        return Array.from({length:n},()=>ans)
    }else{
        let ans=parseInt(s/n)
        let arr=Array.from({length:n},()=>ans)
        for(let i=0;i<s%n;i++){
            arr[i]+=1
        }
        arr.sort()
        return arr
    }
}