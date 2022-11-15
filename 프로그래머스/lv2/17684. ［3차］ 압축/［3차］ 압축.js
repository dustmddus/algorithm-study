function solution(msg) {
    let alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha=[...alpha]
    let map={}
    alpha.forEach((item,idx)=>{
        map[item]=idx+1
    })
    let arr=[...msg]
    let start=0
    let end=start
    let answer=[]
    let result=arr[start]
    while(true){
        if(arr.slice(start,end+1) in map){
            result=arr.slice(start,end+1)
            end+=1
            if(start===arr.length-1){
                answer.push(map[result])
                return answer
            }if(end===arr.length){
                answer.push(map[result])
                return answer
            }
        }else{
            answer.push(map[result])
            map[arr.slice(start,end+1)]=Object.keys(map).length+1
            start=end
            end=start
        }
    }
}