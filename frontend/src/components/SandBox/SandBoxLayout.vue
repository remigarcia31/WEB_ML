<script setup>
import FormLoad from "./FormLoad.vue";
import FormTrain from "./FormTrain.vue";
</script>

<template>
  <v-container>
    <v-row>
        <v-col>
            <v-btn @click="currentComponent = currentComponent === 'FormLoad' ? 'FormTrain' : 'FormLoad'">
                Switch Form
            </v-btn>
            <FormLoad v-if="currentComponent === 'FormLoad'" />
            <FormTrain v-if="currentComponent === 'FormTrain'" @image-url-changed="handleImageUrlChanged" /> 
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
                <v-btn @click="dialog = true">
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
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="text-h5">Save Model</span>
        </v-card-title>
        <v-card-text>
          <v-text-field v-model="modelName" label="Model Name" />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="saveModel">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
    data() {
        return {
            imageUrl: null,
            isLoading: false,
            dialog: false,
            modelName: '',
            currentComponent: 'FormLoad',
        }
    },
    methods : {
        saveModel() {
            fetch(`/api/savemodel/${this.modelName}`).then((res) => {
                console.log(res);
                this.dialog = false;
            });
        },
        handleImageUrlChanged(newUrl) {
                this.imageUrl = newUrl;
                this.isLoading = false;
        },
    } 
}
</script>
