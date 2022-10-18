function solution(begin, target, words) {
    begin=[...begin]
    words=words.map((i)=>[...i])
    visited={[begin]:0}
    needVisit=[]
    needVisit.push(begin)
    while(needVisit.length!==0){
        const node=needVisit.shift()
        if(node.join('')===target){
            break
        }
        for(let i=0;i<words.length;i++){
            if(!visited[words[i]]&&check(words[i],node)){
                visited[words[i]]=visited[node]+1
                needVisit.push(words[i])
            }
        }
    }
    return visited[[...target]]? visited[[...target]]: 0
}

const check=(words,node)=>{
    let cnt=0
    let len=node.length
    for(let i=0;i<len;i++){
        if(words[i]!==node[i]) cnt++
    }
    return cnt===1?true:false
}
