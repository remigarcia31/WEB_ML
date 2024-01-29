<script setup>
import FormTrain from "./FormTrain.vue";
</script>

<template>
  <v-container>
    <v-row>
        <v-col>
            <FormTrain /> 
        </v-col>
        <v-col>
            <v-card-title>Graph :</v-card-title>
            <v-container>
                <v-row>
                    <v-progress-circular
                    v-if="isLoading"
                    indeterminate
                    color="primary"
                    />
                    <img v-if="imageUrl" :src="imageUrl" alt="Prediction plot" />
                </v-row>
            </v-container>
            <v-btn>
                <v-icon>mdi-download</v-icon>
                Download Model
            </v-btn>
            <a :href="imageUrl" download>
                <v-btn color="primary">
                    <v-icon>mdi-download</v-icon>
                    Download plot
                </v-btn>
            </a>
        </v-col>
    </v-row>
  </v-container>
</template>

<script>
   
</script>
