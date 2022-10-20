/*
x의 모든 0을 제거한다.
x의 길이를 c라고 하면 x를 c를 2진법으로 표현한 문자열로 바꿈
s가 1이 될 때까지 계속 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서
제거된 모든 0의 개수를 각각 배열에 담아 리턴. 
s가 1이 될 떄까지는 자리수가 한자리가 될 때까지
*/
function solution(s) {
    let zero_cnt=0
    let cnt=0
    while(true){
        s=[...s]
        let len=s.length
        if(len===1){
            return [cnt,zero_cnt]
        }
        s=s.filter(i=>i==='1').join('').length
        zero_cnt+=(len-s)
        s=s.toString(2)
        cnt+=1
    }
   
}