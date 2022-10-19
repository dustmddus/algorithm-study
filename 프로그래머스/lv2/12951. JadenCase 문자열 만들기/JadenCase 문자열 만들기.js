function solution(s) {
    s=s.toLowerCase()
    ans=''
    flag=true
    for(let i of s){
         if(flag&&i!==' '){
            ans+=i.toUpperCase()
            flag=false
            continue
        }
        else if(i==' '){
            flag=true
        }
        ans+=i 
    }
    return ans
}