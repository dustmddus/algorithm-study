function solution(pro, speed) {
    const day=pro.map((item,i)=>{
        const result=Math.ceil((100-item)/speed[i])
        return result
    })
    let standard=day[0]
    let cnt=0
    let result=[]
    for(let i of day){
        if(standard>=i)cnt++
        else{
            result.push(cnt)
            standard=i
            cnt=1
        }
    }
    result.push(cnt)
    return result
}