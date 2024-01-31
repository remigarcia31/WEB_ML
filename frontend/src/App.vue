<template>
  <v-app>
  <Header @changeComponent="changeComponent"/>
  <v-main>
   <v-container id="componentContainer">
      <SandBoxLayout v-if="currentComponent === 'SandBoxLayout'" />
      <DatasetsLayout v-if="currentComponent === 'DatasetsLayout'" />
      <ModelsLayout v-if="currentComponent === 'ModelsLayout'" />
   </v-container>
  </v-main>
  <Footer />
  </v-app>
</template>

<script>
  import Header from './components/General/Header.vue';
  import SandBoxLayout from './components/SandBox/SandBoxLayout.vue';
  import DatasetsLayout from './components/DatasetsLayout/DatasetsLayout.vue';
  import ModelsLayout from './components/ModelsLayout/ModelsLayout.vue';
  
  export default {
      data() {
        return {
          currentComponent: 'SandBoxLayout',
        }
      },
      methods: {
        changeComponent(component) {
          this.currentComponent = component;
      },
    }
  } 
</script>

<style>
</style>
