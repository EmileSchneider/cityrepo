import Vue from 'vue'
import Router from 'vue-router'
import LandingPage from '@/components/LandingPage'
import Portfolio from '@/components/Portfolio'
import CV from '@/components/CV'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: LandingPage
    },
    {
      path: '/portfolio',
      name: 'portfolio',
      component: Portfolio
    },
      { path: '/cv',
	name: 'CV',
	component: CV
      }
  ]
})
