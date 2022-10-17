
function solution(numbers, target) {
    cnt=0
    function dfs(i,total){
        if(i===numbers.length){
            if(total===target){
                cnt+=1
            }
            return
        }
        for(let c=0;c<2;c++){
            if(c==0){
                dfs(i+1,total+numbers[i])
            }else{
                dfs(i+1,total-numbers[i])
            }
        }
    }
    dfs(0,0)
    return cnt
}