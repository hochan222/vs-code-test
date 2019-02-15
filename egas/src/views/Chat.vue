<template>
  
<v-navigation-drawer
    dark
    permanent
  >
    <v-list>
      <v-list-tile
        v-for="item in items"
        :key="item.title"
        @click=""
      >
        <v-list-tile-action>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-tile-action>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>

</template>

<script>
import Navi from '../components/Navi'

export default {
  components: {
    Navi
  },
  data () {
      return {
        items: [
          { title: 'Dashboard', icon: 'dashboard' },
          { title: 'Account', icon: 'account_box' },
          { title: 'Admin', icon: 'gavel' }
        ]
      }
    }
}
</script>
