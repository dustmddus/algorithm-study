function solution(n) {
    let cnt=0
    for(let i=1;i<=n;i++){
        let total=0
        for(let j=i;j<=n;j++){
            total+=j
            if(total>=n){
                if(total===n)cnt+=1
                break
            }
        }
    }
    return cnt
}