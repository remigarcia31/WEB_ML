import Vue from 'vue';
import Router from 'vue-router';
import SandBoxLayout from './components/SandBoxLayout.vue';
import DatasetsLayout from './components/DatasetsLayout.vue';
import ModelsLayout from './components/ModelsLayout.vue';

Vue.use(Router);

export default new Router({
  routes: [
    { path: '/sandbox', name: 'sandbox', component: SandBoxLayout },
    { path: '/datasets', name: 'datasets', component: DatasetsLayout },
    { path: '/models', name: 'models', component: ModelsLayout },
  ],
});