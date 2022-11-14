/*
중요도가 높은 문서를 먼저 인쇄하는 프린터
1. 인쇄 대기 목록 가장 앞에 있는 문서를 대기 목록에서 꺼낸다. 
2. 나머지 인쇄 대기 목록에서 앞에 있는 문서보다 중요도가 높은 문서가 한개라도 존재하면 j를 가장 마지막에
3. 그렇지 않으면 j 인쇄. 

*/
function solution(pri, location) {
    const newArr=pri.map((item,idx)=>[item,idx])
    pri.sort((a,b)=>b-a)
    let cnt=1
    while(true){
        if(pri[0]===newArr[0][0]){
            if(newArr[0][1]===location)return cnt
            pri.shift()
            newArr.shift()
            cnt+=1
        }
        if(pri[0]!==newArr[0][0]){
            newArr.push(newArr.shift())
        }
        
    }
    
}