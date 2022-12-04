/*
땅은 총 n행 4열로 이루어짐. 
모든 칸에는 점수 쓰여 있음. 
같은 열을 연속해서 밟을 수는 없음. 
마지막 행까지 모두 내려왔을 때 얻을 수 있는 점수의 최댓값

최댓값 d[n-1][0], d[n-1][1],d[n-1][2], d[n-1][3] 최댓값
d[n][0]=land[n][0]+max(d[n-1][1],d[n-1][2],d[n-1][3])
d[n][1]=land[n][1]+max(d[n-1][0],d[n-1][2],d[n-1][3])
d[n][2]=land[n][2]+max(d[n-1][0],d[n-1][1],d[n-1][3])
d[n][3]=land[n][3]+max(d[n-1][0],d[n-1][1],d[n-1][2])
*/
function solution(land) {
    let n=land.length
    const d=Array.from(Array(n),()=>new Array(4))
    d[0][0]=land[0][0]
    d[0][1]=land[0][1]
    d[0][2]=land[0][2]
    d[0][3]=land[0][3]
    for(let i=1;i<n;i++){
        d[i][0]=land[i][0]+Math.max(d[i-1][1],d[i-1][2],d[i-1][3])
        d[i][1]=land[i][1]+Math.max(d[i-1][0],d[i-1][2],d[i-1][3])
        d[i][2]=land[i][2]+Math.max(d[i-1][0],d[i-1][1],d[i-1][3])
        d[i][3]=land[i][3]+Math.max(d[i-1][0],d[i-1][1],d[i-1][2])
    }
    return (Math.max(d[n-1][0],d[n-1][1],d[n-1][2],d[n-1][3]))  
}