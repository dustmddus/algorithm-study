function solution(k, dung) {
    let visited=Array.from({length:dung.length},()=>false)
    let result=[]
    function dfs(cnt,tmp_k){
        result.push(cnt)
        for(let i=0;i<dung.length;i++){
            if(!visited[i]&&dung[i][0]<=tmp_k){
                visited[i]=true
                dfs(cnt+1,tmp_k-dung[i][1])
                visited[i]=false
            }
        }
    }
    dfs(0,k)
    return Math.max(...result)
}