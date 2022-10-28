/*
n명 참가 게임. 1~n까지 배정. 
각 묶음에서 우승자가 1~n/2 배정
*/
function solution(n,a,b)
{
    let x,y
    if(a<b){
        [x,y]=[a,b]
    }
    else{
        [x,y]=[b,a]
    }
    
    let cnt=0
    while(true){
        if(x===y){
            break
        }
        x=parseInt((x+1)/2)
        y=parseInt((y+1)/2)
        cnt+=1
    }
    return cnt
}