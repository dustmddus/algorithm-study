/*
유사도 검사 
A, B 사이의 유사도는 J(A,B)
두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
두 집합이 모두 공집합일 경우엔 1

- 문자열 모두 소문자로 변환
- 두 글자씩 끊어서 다중집합 만들기 -> 영어 이외의 다른 문자는 모두 제외

*/
function solution(str1, str2) {
    str1=str1.toLowerCase().split('')
    str2=str2.toLowerCase().split('')
    let arr1=[]
    let arr2=[]
    const isAlpha=(a,b)=>{
        let ascA=a.charCodeAt()
        let ascB=b.charCodeAt()
        if(ascA<97||ascA>122||ascB<97||ascB>122)return true
        return false
    }
    
    for(let i=0;i<str1.length-1;i++){
        if(isAlpha(str1[i],str1[i+1]))continue
        arr1.push(str1[i]+str1[i+1])
    }
    for(let i=0;i<str2.length-1;i++){
        if(isAlpha(str2[i],str2[i+1]))continue
        arr2.push(str2[i]+str2[i+1])
        
    }
    if(arr1.length===0 &&arr2.length===0)return 65536
    let inter=0
    //교집합 구하기
    for(let i of arr1){
        if(arr2.includes(i)){
            let idx=arr2.indexOf(i) 
            delete arr2[idx]
            inter++
        }
    }
    //합집합 구하기
    let y=arr1.length-inter+arr2.length
    return parseInt((inter/y)*65536)
    
}