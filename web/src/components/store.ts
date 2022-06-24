import { ref, Ref } from "vue"


export function useStore(){
    const leagues = ref([])
    const clubs = ref([])
    const matches = ref([])
    const _ = require('lodash')
    const getLeagues = async() => {
        
        await fetch("/user_api/leagues").then(async(res)=>{
            
            const data = await res.json()
            
            leagues.value = data
        })
        
        
    }

    const getClubs = async(league_id) => {
        
        const response = await fetch("/user_api/clubs?" + new URLSearchParams({league_id: league_id}));
        var data1 = await response.json();
        
        clubs.value = _.orderBy(data1, ["points","name"], ["desc","asc"])
    }

    const getMatchesByDay = async(start_time) => {
        
        const day = start_time.getDate()
        const month = start_time.getMonth() + 1
        const year = start_time.getFullYear()
        const timeToString = year.toString() + '-' + month.toString() + '-' + day.toString()
        
        
        const response = await fetch("/user_api/matches?" + new URLSearchParams({start_time: timeToString}))
        var data1 = await response.json();
        matches.value = data1
       
    }
    
     

return {leagues, clubs, matches, getLeagues, getClubs, getMatchesByDay}
}

    