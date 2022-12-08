function solution(elem) {
    let len=elem.length
    elem=elem.concat(elem)
    let result=new Set()
    for(let i=1;i<=len;i++){
        for(let j=0;j<len;j++){
            if(j+i>=elem.length)continue
            if(j>=len)continue
            let new_arr=elem.slice(j,j+i)
            let sum=new_arr.reduce((acc,i)=>acc+i)
            result.add(sum)
        }
    }
    return result.size
}