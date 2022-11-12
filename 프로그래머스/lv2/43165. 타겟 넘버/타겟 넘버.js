function solution(numbers, target) {
    let cnt=0
    function dfs(idx,total){
        if(idx===numbers.length){
            if(target===total){
                cnt++
            }
            return 
        }
        dfs(idx+1,total+numbers[idx])
        dfs(idx+1,total-numbers[idx])
    }
    dfs(0,0)
    return cnt
}