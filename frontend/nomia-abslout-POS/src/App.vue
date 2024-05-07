<template>
  <div class="app" >
    <router-view />
  </div>
</template>

<script>
export default {
  name: "AppView",
  data() {
    return {
      current_user: {
        is_authenticated: true,
      },
    };
  },

}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  align-items: center;
  justify-content: flex-start;
  scrollbar-width: thin;
  scrollbar-color: var(--event-color-btn-h) var(--event-color-bg-total);
  --event-color-bg-total: #00130f;
  --event-color-btn: #336633;
  --event-color-btn-h: #669966;
  --event-color-text-white: #fff;
  --event-color-text-gray: #747579;
  --event-color-text-gray-h: #a5a5a5;
}
body {
  min-height: 100vh;
  background: var(--event-color-bg-total);
}
*::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
*::-webkit-scrollbar-thumb {
    background-color: var(--event-color-btn);
    border-radius: 6px;
}
*::-webkit-scrollbar-thumb:hover {
    background-color: var(--event-color-btn-h);
}
*::-webkit-scrollbar-track {
    background-color: var(--event-color-bg-total);
}

.choices{
  display: block;
  align-items: center;
  justify-content: center
}
.parent {
  display: flex;
  justify-content: left;
  min-height: 100vh;
  flex-direction: column;
  padding: 4rem 2rem;
}
.box {
  min-width: 17rem;
  margin-top: 2.5rem;
  top: 20vh;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  max-width: 23.5rem;
}
.text-block {
  display: block;
  font-size: 0.875rem;
  font-weight: 500;
  line-height: 1.5;
  color: var(--event-color-text-gray-h);
  font-family: "MS Sans Serif", sans-serif;
  flex: 1;
  margin: 1rem;
  text-align: center;
}
.title {
  margin-top: 2.5rem;
  text-align: center;
  font-size: 1.5rem;
  font-weight: bold;
  line-height: 1.25;
  letter-spacing: -0.025em;
  color: var(--event-color-text-white);
  font-family: Arial, sans-serif;
}
.container {
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  max-width: 40rem;
}
</style>
