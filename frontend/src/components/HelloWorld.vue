<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-img height="300" src="@/assets/logo.svg" />

      <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>

      <h1 class="text-h2 font-weight-bold">Vuetify</h1>

      <div class="py-14" />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            href="https://vuetifyjs.com/components/all/"
            min-width="164"
            rel="noopener noreferrer"
            target="_blank"
            variant="text"
          >
            <v-icon
              icon="mdi-view-dashboard"
              size="large"
              start
            />

            Components
          </v-btn>
        </v-col>

        <v-col cols="auto">
          <v-btn
            color="primary"
            @click="tryAPI"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
          >
            <v-icon
              icon="mdi-api"
              size="large"
              start
            />
            try API
          </v-btn>
        </v-col>

        <v-col cols="auto">
          <v-btn
            href="https://vuetifyjs.com/introduction/why-vuetify/#feature-guides"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            target="_blank"
            variant="text"
          >
            <v-icon
              icon="mdi-speedometer"
              size="large"
              start
            />

            Get Started
          </v-btn>
        </v-col>

        <v-col cols="auto">
          <v-btn
            href="https://community.vuetifyjs.com/"
            min-width="164"
            rel="noopener noreferrer"
            target="_blank"
            variant="text"
          >
            <v-icon
              icon="mdi-account-group"
              size="large"
              start
            />

            Community
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="auto">
          <div class="d-flex flex-wrap justify-center ga-2">
            <v-chip v-for="p in packages" prepend-icon="mdi-language-python" label color="green">{{ p }}</v-chip>
          </div>
      </v-col>
      </v-row>
    </v-responsive>
  </v-container>
  <v-snackbar v-model="devmode" :timeout="5000" color="warning" min-width="0">
    your backend is in devmode
    </v-snackbar>
</template>

<script>
  export default {
    data(){
      return {
        packages:[],
        devmode:undefined
      }
    },
    methods:{
      tryAPI(){
        fetch("/api/python_pkg").then(res=>res.json()).then(data=>{
          this.packages = data
        })
      }
    },
    created(){

      fetch("/api/mode").then(res=>res.json()).then(data=>{
          this.devmode = data.devmode
        })
    }
  }
</script>
