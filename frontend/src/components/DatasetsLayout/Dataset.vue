<template>
    <v-container>
        <v-data-table :headers="headers" :items="csvPreview" class="elevation-1" />
    </v-container>
  </template>
  
  <script>
  export default {
    props: {
      selectedCsv: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        csvPreview: [],
        headers: [],
      };
    },
    methods: {
      previewCsv() {
        fetch(`/api/csv-preview/${this.selectedCsv}`)
          .then((res) => res.json())
          .then((data) => {
            this.csvPreview = data;
            if (data.length > 0) {
              this.headers = Object.keys(data[0]).map((key) => ({ text: key, value: key, sortable: true }));
            }
          });
      },
    },
    watch: {
        selectedCsv(newVal, oldVal) {
            if (newVal !== oldVal) {
              this.previewCsv();
            }
        },
    },
  };
  </script>