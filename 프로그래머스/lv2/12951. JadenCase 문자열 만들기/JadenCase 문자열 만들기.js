function solution(s) {
    let ans=''
    for(let i=0;i<s.length;i++){
        if(i===0||s[i-1]===' ')ans+=s[i].toUpperCase()
        else ans+=s[i].toLowerCase()
    }
    return ans
}