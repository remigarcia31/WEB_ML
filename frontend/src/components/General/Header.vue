<template>
    <v-app-bar>
        <v-app-bar-nav-icon>
            <img src="https://static.thenounproject.com/png/2300300-200.png" alt="Icone" style="width: 100%;"/>
        </v-app-bar-nav-icon>
        <v-app-bar-title class="white--text">Machine learning Tools</v-app-bar-title>
        <v-spacer />
        <v-app-bar-items>
            <v-btn flat @click="setComponent('SandBoxLayout')">SandBox</v-btn>
            <v-btn flat @click="setComponent('DatasetsLayout')">Datasets</v-btn>
            <v-btn flat @click="setComponent('ModelsLayout')">Models</v-btn>
        </v-app-bar-items>
    </v-app-bar>
</template>

<script>
export default {
  methods: {
    setComponent(component) {
      this.$emit('change-component', component);
    },
  },
};
</script>