function solution(array, commands) {
    answer=[]
    for(let [i,j,k] of commands){
        let temp=array.slice(i-1,j).sort((a,b)=>a-b)
        answer.push(temp[k-1])
    }
    return answer
}