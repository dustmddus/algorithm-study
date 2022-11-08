function solution(pro, speeds) {
    let day=pro.map((item,i)=>{
        return Math.ceil((100-item)/speeds[i]) 
    })
    let answer=[0]
    let maxNum=day[0]
    for(let i=0,j=0;i<day.length;i++){
        if(day[i]<=maxNum)answer[j]++
        else{
            answer[++j]=1
            maxNum=day[i]
        }
    }
    return answer
}