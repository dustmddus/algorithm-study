/*
선행 스킬 순서 skill과 유저들이 만든 스킬 트리 담은 skill_trees가 주어짐
가능한 스킬 트리 개수 리턴하라. 

*/
function solution(skill, skill_trees) {
    let cnt=0
    skill_trees.forEach((item)=>{
        let filterItem=[...item].filter((i)=>
            skill.includes(i)
        )
        let newSkill=skill.slice(0,filterItem.length)
        if(filterItem.join('')===newSkill)cnt++
    })
    return cnt
}