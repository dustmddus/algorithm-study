function solution(tickets) {
    let start=[]
    start=tickets.filter((item)=>item[0]==='ICN')
    visited=tickets.slice()
    result=[]
    function removeItem(visited,item){
        for(let i=0;i<visited.length;i++){
            if(visited[i]===item){
                visited.splice(i,1)
                break
            }
        }
    }
    function dfs(arr,n){
        if(n===tickets.length){
            if(visited.length===0){
                result.push(arr)    
            }
            return
        }
        for(let i of tickets){
            len=arr.length
            if(visited.includes(i)&&arr[arr.length-1]===i[0]){

                removeItem(visited,i)
                temp_arr=arr.slice()
                temp_arr.push(i[1])
                dfs(temp_arr,n+1)
                visited.push(i)
            }
        }
    }
    for(let i=0;i<start.length;i++){
        removeItem(visited,start[i])
        dfs(start[i],1)
        visited.push(start[i])
    }
    result.sort()
    return result[0]
}