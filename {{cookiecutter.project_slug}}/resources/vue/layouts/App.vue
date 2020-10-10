<template>
  <div class="flex items-center justify-center h-screen">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  created () {
    document.title = this.$route.meta.title
  }
}
</script>

<style>

</style>
