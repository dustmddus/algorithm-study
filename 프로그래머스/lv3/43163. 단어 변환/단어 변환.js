function solution(begin, target, words) {
    const visited=[]
    const queue=[]
    let answer=0
    queue.push([begin,answer])
    
    while(queue.length){
        let [v,cnt]=queue.shift()
        if(v===target)return cnt
        visited.push(v)
        words.forEach((item)=>{
            const tmp=[...item].filter((ele,i)=>ele!==v[i])
            if(tmp.length===1&&!visited.includes(item)){
                queue.push([item,++cnt])
                visited.push(item)
            }
        })
    }
    return answer
}