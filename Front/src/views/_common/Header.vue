<template>
  <div id="header"></div>
</template>

<script></script>

<style scoped>
#header {
  height: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

#header a {
  font-weight: bold;
  color: #2c3e50;
  margin: 2rem;
}

#header a.router-link-exact-active {
  color: #42b983;
}
</style>
