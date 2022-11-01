/*
성능 측정 수행
캐시 크기를 얼마로 해야 효율적인지 몰라 난감
캐시 크기에 따른 실행시간 측정 프로그램
*/
function solution(cacheSize, cities) {
    cities=cities.map((item)=>item.toLowerCase())
    let visited=[]
    let total=0
    for(let item of cities){
        if(cacheSize===0){
            total+=5
            continue
        }
        if(visited.includes(item)){
            total++
            visited=visited.filter((ele)=>ele!=item)
        }else{
            if(visited.length===cacheSize){
                visited.shift()
            }
            total+=5
        }
        visited.push(item)
    }
    return total
}