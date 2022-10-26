/*
n명의 사람이 영어 끝말잇기. 
사람 수 n, 순서대로 말한 words. 
가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째에서 탈락하는지 구하라. 
*/
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
        console.log(visited)
    }
    return [0,0]
}