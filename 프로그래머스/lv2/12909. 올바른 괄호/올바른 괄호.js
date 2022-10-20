function solution(s){
    stack=[]
    let flag=true
    for(let i of s){
        if(i==='('){
            stack.push(i)
        }
        else{
            if(stack.length===0||stack[s.length-1]===')'){
                flag=false
                break
            }
            if(stack.pop()==='('){
                flag=true
            }
        }
    }
    if(stack.length!==0)flag=false
    return flag?true:false
}