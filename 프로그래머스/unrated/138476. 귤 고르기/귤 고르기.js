function solution(k, tang) {
    const fruit={}
    tang.forEach((item)=>{
        if(item in fruit)fruit[item]+=1
        else fruit[item]=1
    })
    let cnt=0
    const sortedFruit=Object.entries(fruit).sort((a,b)=>b[1]-a[1])
    for(let i=0;i<sortedFruit.length;i++){
        let [,value]=sortedFruit[i]
        if(k<=0) return cnt
        k-=value
        cnt+=1
    }
    return cnt
}
