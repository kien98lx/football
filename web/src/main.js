import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import {createRouter, createWebHashHistory} from 'vue-router'
import UserPage from "@/components/UserPage.vue"
import MatchesDetail from "@/components/AdminPage/Matches/Detail.vue"
import MatchesList from "@/components/AdminPage/Matches/List.vue"

loadFonts()


const routes = [
  { path: '/', component: UserPage},
  { path: '/admin-matches-detail', component: MatchesDetail},
  { path: '/admin-matches-list' , component: MatchesList}  
]

const router = createRouter({

  history: createWebHashHistory(),
  routes,
})

const app = createApp(App)
app.use(vuetify)
          
app.use(router)
app.mount('#app')
