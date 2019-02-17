<template>
  <v-app>
    <v-toolbar>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>
    </v-toolbar>
    
    <Navigation />

    <v-content>
       <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Navigation from './components/Navigation'

export default {
  name: 'App',
  components: {
    Navigation
  },
  data () {
    return {
      //
    }
  }
}
</script>
