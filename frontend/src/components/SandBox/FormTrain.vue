<template>
  <v-card-title>Training model : </v-card-title>
  <form method="post">
    <v-card-text>Enter the CSV you want :</v-card-text>
    <v-file-input
      v-model="file"
      accept=".csv"
      label="File input"
      name="csvFile"
      @change="parseCSV"
    />
    <v-select
      v-if="file"
      v-model="predictionModel"
      label="Select"
      :items="['XGBoost', 'AdaBoost']"
    />
    <v-radio-group v-model="selectLearningTask" v-if="predictionModel">
      <v-radio label="Classification" value="classification" />
      <v-radio label="Regression" value="regression" />
    </v-radio-group>
    <v-card-text v-if="selectLearningTask"
      >Select the split value :</v-card-text
    >
    <v-slider
      v-if="selectLearningTask"
      v-model="splitValue"
      :min="0"
      :max="1"
      :step="0.2"
      thumb-label
    />
    <v-select
      v-if="selectLearningTask"
      label="Select"
      :items="columns"
      v-model="target"
    />
    <v-btn v-if="splitValue" @click="launchPredict" :loading="isLoading">Predict</v-btn>
  </form>
</template>

<script>
import Papa from "papaparse";
export default {
  data() {
    return {
      file: null,
      splitValue: null,
      csvFile: null,
      selectLearningTask: null,
      predictionModel: null,
      target: null,
      imageUrl: null,
      isLoading: false,
      columns: [],
    };
  },
  methods: {
    parseCSV(event) {
      const file = event.target.files[0];
      this.csvFile = file;
      Papa.parse(file, {
        header: true,
        complete: (results) => {
          this.columns = results.meta.fields;
        },
      });
    },
    launchPredict() {
      this.isLoading = true;
      this.imageUrl = null;
      const formData = new FormData();
      formData.append("csvFile", this.csvFile);
      fetch("/api/upload", { method: "POST", body: formData }).catch(
        (error) => {
          console.error("Error:", error);
        }
      );
      fetch(
        `/api/predict/${this.csvFile.name}/${this.predictionModel}/${
          this.selectLearningTask
        }/${this.target}/${this.splitValue * 10}`
      ).then((res) => {
        this.$emit('image-url-changed', res.url);
        //console.log(res.url)
        //console.log("Done")
        this.$emit('loading', false);
        this.isLoading = false;
      });
    },
  }
};
</script>
