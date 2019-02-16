<template>
  <v-app>
    
    <router-view></router-view>
    
    <!-- <v-content></v-content> -->
  </v-app>
</template>

<script>
import Navi from './components/Navi'

export default {
  name: 'App',
  components: {
    Navi
  },
  data () {
    return {
      //
    }
  }
}
</script>
