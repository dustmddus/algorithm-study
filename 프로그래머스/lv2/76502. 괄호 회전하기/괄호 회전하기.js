function solution(s) {
    let ans=0
    s=[...s]
    let open=['(','[','{']
    let close=[')',']','}']
    
    const isRight=(str)=>{
        let stack=[]
        for(let i of str){
            if(open.includes(i)){
                stack.push(i)
            }else{
                if(stack.length===0)return
                let x=stack.pop()
                let openIdx=open.findIndex((e)=>e===x)
                let closeIdx=close.findIndex((e)=>e===i)
                if(openIdx!==closeIdx)return
            }
        }
        if(stack.length>0)return
        ans++
    }
    isRight(s)
    for(let i=0;i<s.length-1;i++){
        s.push(s.shift())
        isRight(s)
    }
    return ans
}