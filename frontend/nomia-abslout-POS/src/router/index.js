import { createRouter, createWebHistory } from 'vue-router'
import OnboardingView from '../views/user/OnboardingView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/onboarding',
      name: 'Onboarding',
      component: OnboardingView
    },
  ]
})

export default router
