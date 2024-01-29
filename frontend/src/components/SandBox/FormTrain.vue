<template>
  <form method="post">
    <v-card-text>Enter the CSV you want :</v-card-text>
    <v-file-input
      v-model="file"
      accept="*.csv"
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
    <v-btn v-if="splitValue" @click="launchPredict">Predict</v-btn>
  </form>
</template>

<script>
export default {
  data() {
    return {
      file: null,
      splitValue: null,
      csvFile: null,
      selectLearningTask: null,
      predictionModel: null,
      target: null,
      columns: [],
    };
  },
};
</script>
