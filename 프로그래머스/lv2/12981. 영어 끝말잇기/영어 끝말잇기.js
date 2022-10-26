function solution(n, words) {
    words=words.map((i)=>[...i])
    let visited=[words[0].join('')]
    for(let i=0;i<words.length-1;i++){
        if(words[i][words[i].length-1]!==words[i+1][0] || visited.includes(words[i+1].join(''))){
            let num=(i+1)%n+1
            let cnt=parseInt((i+1)/n)+1
            return [num,cnt]
        }
        visited.push(words[i+1].join(''))
    }
    return [0,0]
}