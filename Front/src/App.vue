<template>
  <div id="app">
    <Header></Header>
    <div id="main">
      <router-view />
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "@/views/_common/Header.vue";
import Footer from "@/views/_common/Footer.vue";

export default {
  name: "App",
  components: {
    Header,
    Footer,
  },
};
</script>

<style>
body {
  padding: 0;
  margin: 0;
}
#app {
  height: 100vh;
  display: flex;
  flex-direction: column;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#main {
  flex: 1;
}
</style>
