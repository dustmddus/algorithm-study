function solution(begin, target, words) {
    let answer=0
    let queue=[]
    const visited=[]
    queue.push([begin,answer])
    while(queue.length){
        let [cur,cnt]=queue.shift()
        if(cur===target)return cnt
        words.forEach((item)=>{
            const tmp=[...item].filter((ele,i)=>ele!==cur[i])
            if(tmp.length===1&&!visited.includes(item)){
                visited.push(item)
                queue.push([item,++cnt])
            }
        })
    }
    return answer
}