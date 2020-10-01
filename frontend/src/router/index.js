import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home_axios.vue'
import Car from '../views/Car_axios.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/:id',
    name: 'Car',
    component: Car,
    props: true,
  },
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
