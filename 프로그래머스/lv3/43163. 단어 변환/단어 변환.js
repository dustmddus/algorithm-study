function solution(begin, target, words) {
    let answer=0
    const queue=[]
    visited=[]
    queue.push([begin,answer])
    visited.push(begin)
    while(queue.length){
        let [cur,cnt]=queue.shift()
        if(cur===target)return cnt
        words.forEach((item)=>{
            let tmp=[...item].filter((ele,i)=>ele!==cur[i])
            if(tmp.length===1&&!visited.includes(item)){
                queue.push([item,++cnt])
                visited.push(item)
            }
        })
    }
    return answer
}