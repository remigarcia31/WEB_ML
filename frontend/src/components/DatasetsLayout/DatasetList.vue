<template>
    <v-container>
        <v-form>
            <v-select
                :items="csvFiles"
                label="Selectionner un fichier CSV"
                :value="modelValue"
                @update:model-value="$emit('update:modelValue', $event)"
            />
        </v-form>
    </v-container>
</template>
    
<script>
    export default {
        props: ['modelValue'],
        emits: ['update:modelValue'],
        data() {
            return {
            csvFiles: [],
            selectedCsv: null,
            };
        },
        methods: {
            test(event) {
                console.log(event)
                
            }
        },
        created() {
            fetch('/api/csv-files')
            .then((res) => res.json())
            .then((data) => {
                this.csvFiles = data;
            });
        },
    };
</script>