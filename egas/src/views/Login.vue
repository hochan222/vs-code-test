<template>
  <v-container>
    <v-layout
      align-center
      column
      justify-center
      fill-height
    >
      <v-card class="px-5 deep-purple accent-2">
        <v-layout
           justify-space-around
         >
          <v-avatar size="70" class="mt-4">
            <img
              src="https://cdn.vuetifyjs.com/images/john.jpg"
              alt="John"
            >
          </v-avatar>
        </v-layout>

        <v-layout justify-center column align-center>
          <v-card-title primary-title>
            <div>
              <p class="blue--text text--lighten-3 caption">___ invited you to join</p>
              <h3 class="headline mb-0 mx-5 subheading deep-purple--text text--darken-4">Egas</h3>
            </div>
          </v-card-title>

          <v-card-actions>
            <v-btn outline color="deep-purple darken-4"><router-link :to="'chat'"><span>Join</span></router-link></v-btn>
          </v-card-actions>
        </v-layout>
      </v-card>
    </v-layout>
 </v-container>
</template>


<script>
// import LoginF from '../components/Login-form'

export default {
  components: {
    
  }  
}
</script>

<style>
  a{
    color: #311B92;
    text-decoration: none;
  }
</style>
