<template>
    <v-container>
        <v-row>
            <v-col>
                <DatasetList @selectedCsv="handleCsvSelected" />
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
            selectedCsv: null
        };
    },
    methods: {
        handleCsvSelected(csv) {
            console.log(csv)
            this.selectedCsv = csv;
        }
    }
};
</script>