<template>
  <div class="flex-center position-ref full-height">
    <div class="content">
      <div class="title m-b-md">
        <img
          src="https://res.cloudinary.com/yunior-dev/image/upload/v1619387919/Django-Cookie/django-cookie_cczfau.png"
          alt="Django-Cookie"
          width="889"
          height="108"
        />
      </div>

      <div class="links">
        <a href="https://docs.djangoproject.com/en/3.2/" target="_blank">Django</a>
        <a href="https://vuejs.org" target="_blank">Vue.js</a>
        <a href="https://github.com/yunior-dev/django-cookie" target="_blank">GitHub</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Welcome',
};
</script>

<style>
html,
body {
  background-color: #fffbeb;
  color: #78350f;
  font-family: 'Nunito', sans-serif;
  font-weight: 200;
  height: 100vh;
  margin: 0;
}

.full-height {
  height: 100vh;
}

.flex-center {
  align-items: center;
  display: flex;
  justify-content: center;
}

.position-ref {
  position: relative;
}

.top-right {
  position: absolute;
  right: 10px;
  top: 18px;
}

.content {
  text-align: center;
}

.title {
  font-size: 84px;
  font-weight: 600;
}

.links > a {
  color: #78350f;
  padding: 0 25px;
  font-weight: 800;
  font-size: 16px;
  letter-spacing: 0.1rem;
  text-decoration: none;
  text-transform: uppercase;
}

.m-b-md {
  margin-bottom: 30px;
}
</style>
