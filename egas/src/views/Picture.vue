<template>
 <v-container grid-list-md text-xs-center>
    <Navi />
    <v-textarea
     outline
     v-model="ta"
       ></v-textarea>
    <v-layout row wrap>
      <v-flex class="xs12 sm6 md4" v-for="x in ($vuetify.breakpoint.xs ? 2: 4)" :key="x">
          <v-card>
        <v-img
          src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
          height="200px"
        >
        </v-img>

        <v-card-title primary-title>
          <div>
            <v-chip>{{x}}</v-chip>
            <div class="headline">Top western road trips</div>
            <span class="grey--text">1,000 miles of wonder</span>
          </div>
        </v-card-title>

        <v-card-actions>
          <v-btn flat>Share</v-btn>
          <v-btn flat color="purple">Explore</v-btn>
          <v-spacer></v-spacer>
          <v-btn icon @click="show = !show">
            <v-icon>{{ show ? 'keyboard_arrow_down' : 'keyboard_arrow_up' }}</v-icon>
          </v-btn>
        </v-card-actions>

        <v-slide-y-transition>
          <v-card-text v-show="show">
            I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
          </v-card-text>
        </v-slide-y-transition>
      </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Navi from '../components/Navi'

export default {
    components: {
    Navi
  },
  mounted () {
    const a = {a:1, b:2}
    this.ta = JSON.stringify(this.$vuetify.breakpoint);
    console.log('dd')
  },
  data () {
    return {
      ta:'debug',
      show: false
    }
  }
}
</script>

