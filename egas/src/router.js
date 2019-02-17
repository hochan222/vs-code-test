import Vue from 'vue'
import Router from 'vue-router'
import Login from './views/Login.vue'
import Chat from './views/Chat.vue'
import Picture from './views/Picture.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/chat',
      name: 'chat',
      component: Chat
    },
    {
      path: '/picture',
      name: 'picture',
      component: Picture
    }
  ]
})
