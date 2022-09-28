function solution(n, computers) {
    let visited=Array.from({length:n},()=>0)
    let answer=0
    
    function dfs(i){
        visited[i]=1
        for(let j=0;j<n;j++){
            if(computers[i][j]==1&&!visited[j]){
                dfs(j)
            }
        }
    }
    
    for(let i=0;i<n;i++){
        if(!visited[i]){
            dfs(i)
            answer++
        }
    }
    return answer
}