function solution(numbers, target) {
    let answer=0
    const dfs=(idx,total)=>{
        if(idx===numbers.length){
            if(target===total){
               answer++
            }
            return
        }
        dfs(idx+1,total+numbers[idx])
        dfs(idx+1,total-numbers[idx])
    }
    dfs(0,0)
    return answer
}