<script setup>
import FormTrain from "./FormTrain.vue";
</script>

<template>
  <v-container>
    <v-row>
        <v-col>
            <FormTrain @image-url-changed="handleImageUrlChanged" /> 
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
            <v-container class="d-flex justify-center">
                <v-btn>
                    <v-icon>mdi-download</v-icon>
                    Download Model
                </v-btn>
                <v-spacer />
                <a :href="imageUrl" download>
                    <v-btn color="primary">
                        <v-icon>mdi-download</v-icon>
                        Download plot
                    </v-btn>
                </a>
            </v-container>
        </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
    data() {
        return {
            imageUrl: null,
            isLoading: false,
        }
    },
    methods : {
        handleImageUrlChanged(newUrl) {
                this.imageUrl = newUrl;
                this.isLoading = false;
        },
    } 
}
</script>
