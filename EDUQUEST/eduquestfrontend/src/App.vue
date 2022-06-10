<template>
  <div id="nav">
    <NavbarComponent />
  </div>  
  <router-view/>
</template>

<script>
import { axios } from '@/common/api.service.js';
import NavbarComponent from '@/components/Navbar.vue';
export default {
  name: "App",
  components: {
    NavbarComponent,
  },

  methods: {
    async setUserInfo() {
      try {
        const endpoint = '/auth/users/me/';
        if (endpoint) {
          const response = await axios.get(endpoint);
          const requestUser = response.data['username']
          window.localStorage.setItem("username", requestUser);
        } else {
          console.log('AnonUser');
        }
      } catch (error) {
        console.error(error.response);
        alert(error.response.statusText);
      }
    },
  },

  created() {
    this.setUserInfo();
  }
}
</script>

<style>
  body {
        font-family: "Noto Sans JP", sans-serif;
        font-weight: 400;
        background: linear-gradient(to bottom right, #f9f7f9, #f4f4f4);;
      }
      
</style>
