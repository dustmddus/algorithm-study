function solution(brown, yellow) {
    brown=parseInt((brown-4)/2)
    for(let i=1;i<brown;i++){
        col=brown-i
        if(i*col===yellow&&col<=i){
            return [i+2,col+2]
        }
    }
}