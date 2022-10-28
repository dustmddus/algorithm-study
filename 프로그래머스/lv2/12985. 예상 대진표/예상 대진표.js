/*
n명 참가 게임. 1~n까지 배정. 
각 묶음에서 우승자가 1~n/2 배정
*/
function solution(n,a,b)
{   
    let cnt=0
    while(a!==b){
        a=parseInt((a+1)/2)
        b=parseInt((b+1)/2)
        cnt+=1
    }
    return cnt
}