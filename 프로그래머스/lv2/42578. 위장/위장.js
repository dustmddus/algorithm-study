function solution(clothes) {
    const map={}
    for(let item of clothes){
        if(item[1] in map)map[item[1]]+=1
        else map[item[1]]=1
    }
    let answer=1
    for(let item in map){
        answer*=(map[item]+1)
    }
    return answer-1
}