<template>
    
</template>

<script>
export default {
  methods: {
    setComponent(component) {
      this.$emit('change-component', component);
    },
  },
};
</script>