function solution(oper) {
    let arr=[]
    for(let item of oper){
        let [op,num]=item.split(' ')
        if(op==='I'){
            arr.push(parseInt(num))
        }
        if(op==='D'&&num==="1"&&arr.length!==0){
            arr.pop()
        }
        if(op==='D'&&num==='-1'&&arr.length!==0){
            arr.shift()
        }
        arr.sort((a,b)=>a-b)
    }
    
    if(arr.length===0)return [0,0]
    let ans=[arr[0],arr[arr.length-1]].sort((a,b)=>b-a)
    return ans
}