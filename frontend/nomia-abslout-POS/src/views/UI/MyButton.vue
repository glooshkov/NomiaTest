<template>
  <button class="btn" :disabled="isDisabled" :style="styleString">
    <slot></slot>
  </button>
</template>

<script>
export default {
  props: {
    isDisabled: Boolean,
    styleString: String,
  },

}
</script>

<style scoped>
.btn {
  display: flex;
  width: 100%;
  justify-content: center;
  border-radius: 0.375rem;
  background-color: var(--event-color-btn);
  padding: 0.7rem 0.75rem;
  font-size: 0.875rem;
  font-weight: 500;
  line-height: 1.5;
  letter-spacing: 0.07em;
  color: var(--event-color-text-white);
  font-family: Arial, sans-serif;
  outline: none;
  outline-offset: 2px;
  border: none;
}
.btn:hover {
    background-color: var(--event-color-btn-h);
}
.btn:focus-visible {
    outline-offset: 2px;
}
</style>


