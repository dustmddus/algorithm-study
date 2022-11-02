function solution(arr1, arr2) {
    let row1=arr1.length
    let col1=arr1[0].length
    let row2=arr2.length
    let col2=arr2[0].length
    const result=Array.from(Array(row1),()=>Array(col2).fill(0))
    for(let i=0;i<row1;i++){
        for(let j=0;j<col2;j++){
            let num=0
            for(let k=0;k<row2;k++){
                num+=arr1[i][k]*arr2[k][j]
                
            }
            result[i][j]=num
        }
    }
    return result
}