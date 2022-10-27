function solution(arr) {
    const gcd=(a,b)=>{
        if(b===0)return a
        return gcd(b,a%b)
    }
    return arr.reduce((a,b)=>a*b/gcd(a,b))
}