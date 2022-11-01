function solution(cita) {
    cita.sort((a,b)=>b-a)
    for(let i=0;i<cita.length;i++){
        if(i>=cita[i])return i
    }
    return cita.length
}