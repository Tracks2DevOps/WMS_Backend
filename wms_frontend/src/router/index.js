import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'

import WarehouseOrders from '../views/WarehouseOrders.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  {
    path: '/about',
    name: 'about',
    component: AboutView
  },

  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUpView
  },

  {
    path: '/log-in',
    name: 'LogIn',
    component: LogInView
  },

  {
    path: '/warehouseorders',
    name: 'WarehouseOrders',
    component: WarehouseOrders
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
