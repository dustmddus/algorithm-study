/*
0은 벽, 1은 벽없음. 
*/
function solution(maps) {
    let row=maps.length
    let col=maps[0].length
    let visited=Array.from({length:row},()=>Array(col).fill(0))
    let queue=[]
    queue.push([0,0])
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    visited[0][0]=1
    while(queue.length!==0){
        let [x,y]=queue.shift()
        for(let i=0;i<4;i++){
            let nx=x+dx[i]
            let ny=y+dy[i]
            if(0>nx||0>ny||nx>=row||ny>=col)continue
            if(visited[nx][ny]!==0||maps[nx][ny]===0)continue
            queue.push([nx,ny])
            visited[nx][ny]=visited[x][y]+1
        }
    }
    return visited[row-1][col-1]===0?-1:visited[row-1][col-1]
}