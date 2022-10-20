/*
두 수를 곱한 값을 누적하여 더한다. 누적된 값이 최소가 되도록 만드는 것이 목표
*/
function solution(A,B){
    A.sort((a,b)=>b-a)
    B.sort((a,b)=>a-b)
    result=0
    for(let i=0;i<A.length;i++){
        result+=A[i]*B[i]
    }
    return result
}