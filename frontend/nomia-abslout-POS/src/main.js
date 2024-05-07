import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router/index'
import { apolloProvider } from "@/apollo-config";


createApp(App).use(createPinia()).use(router).use(apolloProvider).mount("#app");