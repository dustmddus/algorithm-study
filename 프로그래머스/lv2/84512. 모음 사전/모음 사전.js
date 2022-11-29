function calc(idx){
    let sum=0
    for(let i=idx;i>=0;i--){
        sum+=5**i
    }
    return sum
}
function solution(word) {
    let answer=0
    const word_map={'A':0,'E':1,'I':2,'O':3,'U':4}
    let wordArr=[...word]
    wordArr.forEach((w,idx)=>{
        const val=word_map[w]
        answer+=val*calc(4-idx)+1
    })
    return answer
}