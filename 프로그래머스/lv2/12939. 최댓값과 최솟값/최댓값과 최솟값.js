function solution(s) {
    s=s.split(' ').map((x)=>Number(x))
    ans=String(Math.min(...s))+' '+String(Math.max(...s))
    return ans
}