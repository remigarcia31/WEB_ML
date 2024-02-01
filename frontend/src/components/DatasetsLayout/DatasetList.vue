<template>
    <v-container>
        <v-form>
            <v-select
                :items="csvFiles"
                label="Select a CSV file"
                v-model="selectedCsv"
                @change="$emit('selectedCsv', selectedCsv)"
            />
        </v-form>
    </v-container>
</template>
    
<script>
    export default {
        data() {
            return {
            csvFiles: [],
            selectedCsv: null,
            };
        },
        created() {
            fetch('/api/csv-files')
            .then((res) => res.json())
            .then((data) => {
                this.csvFiles = data;
                //console.log(data)
            });
        },
    };
</script>