<template>
    <v-container>
        <v-row>
            <v-col>
                <DatasetList v-model="selectedCsv"/>
            </v-col>
            <v-col>
                <Datasets v-bind:selectedCsv="selectedCsv" />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import DatasetList from "./DatasetList.vue";
import Datasets from "./Dataset.vue";

export default {
    components: {
        DatasetList,
        Datasets
    },
    data() {
        return {
            selectedCsv: ''
        };
    },
    methods: {
    },
    watch : {
        selectedCsv(csv) {
            this.selectedCsv = csv.split(".")[0];
        }
    }
};
</script>