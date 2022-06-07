<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
  <div class="container">
    <router-link class="navbar-brand" :to="{name: 'home'}">
      EDUQUEST
    </router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse ml-auto" id="navbarSupportedContent">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item me-3">
          <button class="slide">
            <a href="/accounts/logout/">Logout</a>
          </button>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>

<script>
export default {
  name: "NavbarComponent",

  data() {
    return {
      requestUser: null,
    }
  },

  created() {
    this.setRequestUser();
  },

  methods: {
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
      console.log(this.requestUser);
    },
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Smooch&display=swap');
.my-navbar {
  border-bottom: 1px solid #ddd;
}

.navbar-brand {
  font-weight: bold;
  color: #66c887;
  font-size: 3rem;
  font-family: 'Cormorant Garamond', serif;
}

.navbar-brand:hover {
  color: #66c887 !important;
}


button {
  color: #8fc866;
  transition: 0.25s;
}
button:hover, button:focus {
  border-color: #66c887;
  color: #fff;
}

button {
  background: none;
  border: 2px solid;
  font: inherit;
  line-height: 1;
  margin: 0.5em;
  padding: 1em 2em;
}

h1 { font-weight: 400; }

button a {
  text-decoration: none !important;
  color: #66c887;
}

button a:hover {
  text-decoration: none !important;
  color:white;
  z-index: 1;
}

.slide:hover,
.slide:focus {
  box-shadow: inset 11em 0 0 0 #66c887;
}
</style>