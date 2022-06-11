<template>
  <div class="container">
    
    <nav class="nav navbar fixed-top navbar-light bg-light">
      <div class="nav-logo">
          <a href="/" class="nav-logo__link" title="logo">
              <i class="fa fa-cog fa-spin fa-fw"></i>  
              EDU<span class="nav-logo__quest">QUEST</span>
          </a>
      </div>
      <div class="nav-menu">
        <ul class="nav-menu__item">
          <li><a href="#" class="nav-menu__link">Hello {{requestUser}}</a></li>
          <li><a href="#" class="nav-menu__link">About</a></li>
          <li><a href="#" class="nav-menu__link">Service</a></li>
          <li><a href="#" class="nav-menu__link">Contact</a></li>
        </ul>
      </div>
      <div class="nav-menu">
        <ul class="nav-menu__item">
          <li
            v-if="requestUser"
          >
            <a class="hero-text__btn" href="accounts/login/">Take a break</a>
          </li>
          <li v-else>
            <a class="hero-text__btn" href="accounts/logout/">Join Us</a>
          </li>
        </ul>
      </div>
    </nav>
  </div>
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
    },
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@700&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Work+Sans:wght@300&display=swap');
      * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  text-decoration: none;
  list-style: none;
}
body {
  font-family: 'Work Sans', sans-serif;
  font-size: 1rem;
  font-weight: normal;
  line-height: 1.4;
  background: #ffffff;
  color: #333333;
}

.container {
  padding: 0 1rem;
  margin: 0 auto;
  max-width: 80rem;
  width: 100%;
}

.nav {
  display: flex;
  flex-direction: row;
  flex: 1;
  flex-basis: auto;
  justify-content: space-between;
  align-items: center;
  padding: .4rem 0;
  margin:1rem;
}
.nav-logo {
  font-family: 'Quicksand', sans-serif;
  text-decoration: none;
  color: black;
  line-height: inherit;
}
.nav-logo__link {
  font-size: 1.9rem;
  font-weight: 700;
  color: #3a041c;
  text-decoration: none;
}
.nav-logo__quest {
    color: #D90C66;
}

.nav-menu__item {
  display: flex;
  flex-direction: row;
  flex: 1;
  flex-basis: auto;
}
.nav-menu__link {
  margin: 0 2rem 0 0;
  font-family: 'Quicksand', sans-serif;;
  font-size: 1.3rem;
  font-weight: 500;
  color: #43041e;
  text-decoration: none;
}
.nav-menu__link:hover {
  color: #6334ba;
}

.hero-text__btn {
  padding: 1rem 2rem;
  border-radius: 5px;
  font-family: inherit;
  font-size: 1.2rem;
  font-weight: 500;
  text-align: center;
  color: #ffffff;
  background: #D90C66;
  border: none;
  outline: none;
  border-radius: 2px;
  text-decoration: none;
}

.hero-text__btn:hover {
  background: #003049;
  color: #ffffff;
}

</style>