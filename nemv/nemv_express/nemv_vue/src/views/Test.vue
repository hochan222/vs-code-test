<template>
  <div>
    <h1>{{title}}</h1>
    <v-btn @click="test" :color="btnColor">test</v-btn>
    <v-chip close v-for="chip in chips" :key="chip.name" :color="chip.color">{{chip.name}}</v-chip>
  </div>
</template>

<script>
  export default {
    name: 'test',
    data () {
      return {
        title: 'Vuetify.js',
        btnColor: 'success',
        chips: [
          {
            color: 'primary',
            name: 'aaaa'
          },
          {
            color: 'success',
            name: 'bbbb'
          },
          {
            color: 'secondary',
            name: 'cccc'
          },
        ]
      }
    },
    methods: {
      test() {
        this.title = 'nnnnnn',
        this.btnColor = 'warning'
      }
    }
  }
</script>
