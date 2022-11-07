function solution(n, left, right) {
    let answer=[]
   for(let i=left;i<=right;i++){
       let [row,col]=[parseInt(i/n),i%n]
       answer.push(Math.max(row,col)+1)
   }
    return answer
}