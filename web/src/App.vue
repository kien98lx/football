<template>
  <v-app>
    <v-main>
      <UserPage/>
    </v-main>
   
  </v-app>
</template>

<script>

import UserPage from './components/UserPage.vue'
export default {
  name: 'App',

  components: {
    UserPage
  },

  data: () => ({
    //
  }),
}
</script>
