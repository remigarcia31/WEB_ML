<template>
    <v-card-title>Loading model : </v-card-title>
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
            :items="models"
        />
        <v-card-text v-if="models">Select the split value :</v-card-text>
        <v-slider
        v-if="models"
            v-model="splitValue"
            :min="0"
            :max="1"
            :step="0.2"
            thumb-label
        />
        <v-select
            v-if="models"
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
            models: [],
            columns: [],
            predictionModel: null,
            modelOptions: [],
            splitValue: null,
            target: null,
        };
    },
    methods: {
        parseCSV() {
            const file = event.target.files[0];
            this.csvFile = file;
            Papa.parse(file, {
                header: true,
                complete: (results) => {
                    this.columns = results.meta.fields;
                },
            });
        },
        fetchModels() {
            fetch('/api/models')
            .then((res) => res.json())
            .then((data) => {
                this.models = data;
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
            console.log(this.predictionModel)
            fetch(
                `/api/predict/${this.csvFile.name}/${this.predictionModel.name}/${this.target}/${this.splitValue * 10}`
            ).then((res) => {
                this.$emit('image-url-changed', res.url);
                //console.log(res.url)
                //console.log("Done")
                this.$emit('loading', false);
                this.isLoading = false;
            });
        },
    },
    created() {
        this.fetchModels();
    },
};
</script>
