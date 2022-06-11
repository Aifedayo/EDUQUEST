<template>
<div class="container">
  <div class="header">
    <div class="hero">
      <div class="hero-text">
        <h1 class="hero-text__main">Never Stop Your <span class="nav-logo__quest">Quest</span> For Knowledge</h1>
        <p class="hero-text__subs"></p>
        <p class="hero-text__subs">This is an enclave to learn and to ask;
            To benefit and to be benefitted; To gain and be of help to people within
            or outside.
        </p>
        <p class="hero-text__subs">
          In a time of turbulence and change, it is more true than ever that <span class="nav-logo__quest">knowledge</span> is power.
          <span class="hero-text__quote"> - John F. Kennedy </span>
        </p>
        <div class="hero-text__div">
          <a class="hero-text__btn" href="categories">Discover</a>
        </div>
      </div>
      <div class="hero-image">
        <img class="hero-image__main" :src="image" alt="Images">
      </div>
    </div>
  </div>
  <main class="main">
    <section class="about">
      <div class="container">
        <div class="about-image">
          <img class="about-image__main" src="../assets/Learning-rafiki.png" alt="Images">
        </div>
        <div class="about-text">
          <h1 class="about-text__main"><span class="nav-logo__quest">Knowledge</span> is power. 
          <span class="nav-logo__quest">Knowledge</span> shared is power multiplied..</h1>
          <p class="about-text__subs">
              Information is liberating. 
              Education is the premise of progress, in every society, in every family.
            </p>
            <p class="about-text__subs">The beautiful thing about learning is nobody can take it away from you.
            The man who asks a question is a fool for a minute, the man who does not 
            ask is a fool for life.
          </p>
        </div>
      </div>
    </section>
    <section class="service">
      <div class="container">
        <div class="card card-1">
          <div class="card-image">
            <img src="../assets/Curious-cuate.png" alt="Images">
          </div>
          <div class="card-text">
            <h2 class="card-text__title">ANYWHERE IN THE WORLD</h2>
            <p class="card-text__subs">The best thing a human being can do is 
                to help another human being know more.
            </p>
          </div>
        </div>
        <div class="card card-2">
          <div class="card-image">
            <img src="../assets/Online-learning-rafiki.png" alt="Images">
          </div>
          <div class="card-text">
            <h2 class="card-text__title">SHARE YOUR <span class="nav-logo__quest">KNOWLEDGE</span></h2>
            <p class="card-text__subs">If you have <span class="nav-logo__quest">knowledge</span>, let others light their candles in it.
            </p>
          </div>
        </div>
        <div class="card card-3">
          <div class="card-image">
            <img src="../assets/Curious-pana.png" alt="Images">
          </div>
          <div class="card-text">
            <h2 class="card-text__title">DEBATE ETHICALLY</h2>
            <p class="card-text__subs"><span class="nav-logo__quest">Knowledge</span> when put to use - 
                only when the use made of it is constructive.
            </p>
          </div>
        </div>
      </div>
    </section>
    <section class="contact">
      <div class="container">
        <div class="contact-image">
          <img src="../assets/Mention-rafiki.png" alt="Images">
        </div>
        <div class="contact-form">
          <h2 class="contact-title">Contact Us Now.</h2>
          <form class="form">
            <div class="form-group group-1">
              <input type="text" name="name" class="form-input" placeholder="Input Your Name">
            </div>
            <div class="form-group group-2">
              <input type="text" name="email" class="form-input" placeholder="Input Your Email">
            </div>
            <div class="form-group group-3">
              <textarea name="message" rows="5" class="form-textarea" placeholder="Input Your Messages"></textarea>
            </div>
            <div class="form-group group-4">
              <input type="submit" class="form-submit" value="Submit">
            </div>
          </form>
        </div>
      </div>
    </section>
  </main>
</div>
</template>

<script>
import image from "../assets/Learning-amico.png"
export default {
  name: "HomeView",

  data() {
    return {
      image: image,
    }
  }
}
</script>

<style scoped>
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
.header .nav-menu__item {
  display: flex;
  flex-direction: row;
  flex: 1;
  flex-basis: auto;
}
.header .nav-menu__link {
  margin: 0 2rem 0 0;
  font-family: 'Quicksand', sans-serif;
  font-size: 1.3rem;
  font-weight: 500;
  color: #333333;
  text-decoration: none;
}
.header .nav-menu__link:hover {
  color: #6334ba;
}
.header .hero {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 2rem;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.header .hero-text__main {
  font-family: 'Quicksand', sans-serif;
  font-size: 3em;
  font-weight: 800;
  line-height: 1em;
  text-transform: uppercase;
  color: rgb(59, 59, 59);
}
.header .hero-text__subs {
  font-family: inherit;
  font-size: 1.2em;
  font-weight: 300;
  text-transform: capitalize;
  color: #333333;
}

.header .hero-text__quote {
    color: #D90C66;
    font-weight: 600;
}

.header .hero-text__div{
    margin: 2em 0;
}

.header .hero-text__btn {
  padding: 1rem 2rem;
  
  font-family: inherit;
  font-size: 1.2rem;
  font-weight: 500;
  text-align: center;
  color: #ffffff;
  background: #003049;
  border: none;
  outline: none;
  border-radius: 2px;
  text-decoration: none;
}
.header .hero-image__main {
  width: 100%;
  height: auto;
}

.main .about {
  background: #fafafa;
  margin-top: 0rem;
}
.main .about .container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 3rem;
  justify-content: space-between;
  align-items: center;
  padding: 2.5rem;
}
.main .about-image__main {
  width: 80%;
  height: auto;
}
.main .about-text__main {
  font-family: 'Quicksand', sans-serif;
  font-size: 2rem;
  font-weight: 700;
  line-height: inherit;
  text-transform: uppercase;
  color: #003049;
}
.main .about-text__subs {
  font-family: 'Work Sans', sans-serif;;
  font-size: 1.1rem;
  font-weight: 400;
  text-transform: capitalize;
  color: #003049;
  margin: 1rem 0 0 0;
}
.main .service {
  margin-top: 2rem;
}
.main .service .container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 3rem;
  justify-content: center;
  align-items: center;
  padding: 2.5rem 0;
}
.main .service .card {
  padding: 2rem;
  background: #ffffff;
  color: #003049;
  border-radius: 2px;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}

.main .service .card-1,
.main .service .card-2,
.main .service .card-3 {
  border-radius: 20px;
}


.main .service .card:hover {
  background: #D90C66;
  color: white;
  border-radius: 20px;
}

.main .service .card-image {
  display: flex;
  flex-direction: column;
  flex: 1;
  flex-basis: auto;
  justify-content: center;
  align-items: center;
}
.main .service .card-image img {
  max-height: 10rem;
  height: 100%;
  width: auto;
}
.main .service .card-text {
  margin-top: 1.5rem;
  font-family: 'Work Sans', sans-serif;
}

.main .service .card-text__title {
  font-family: 'Courier New', Courier, monospace;
  font-size: 1.4rem;
  font-weight: 600;
  line-height: inherit;
  text-transform: uppercase;
  margin-bottom: 1rem;
}

.main .contact {
  background: #fafafa;
  margin-top: 2rem;
}
.main .contact .container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 2rem;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
}
.main .contact-image img {
  width: 80%;
  height: auto;
}
.main .contact-form .contact-title {
  font-family: inherit;
  font-size: 1.5rem;
  font-weight: 700;
  line-height: inherit;
  text-transform: uppercase;
  color: #D90C66;
  margin-bottom: 1rem;
}
.main .contact-form .form {
  display: flex;
  flex-direction: column;
  flex: 1;
  flex-basis: auto;
  width: 100%;
  height: auto;
}
.main .contact-form .form-group {
  width: 100%;
  height: auto;
}
.main .contact-form .form-group:not(:last-child) {
  margin-bottom: 1rem;
}
.main .contact-form .form-input {
  padding: 1rem 0.75rem;
  width: 100%;
  height: auto;
  font-family: inherit;
  font-size: inherit;
  outline: none;
  border: none;
  border-radius: 2px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
}
.main .contact-form .form-textarea {
  padding: 1rem 0.75rem;
  width: 100%;
  height: auto;
  font-family: inherit;
  font-size: inherit;
  outline: none;
  border: none;
  border-radius: 2px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
}
.main .contact-form .form-submit {
  padding: 0.75rem 1.5rem;
  font-family: inherit;
  font-size: inherit;
  outline: none;
  border: none;
  color: #ffffff;
  background: #7e073d;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
}

.footer {
  padding: 2rem 0;
  background: #333333;
  color: #ffffff;
}
.footer .container {
  display: flex;
  flex-direction: row;
  flex: 1;
  flex-basis: auto;
  justify-content: space-between;
  align-items: center;
}
.footer-menu__item {
  display: flex;
  flex-direction: row;
  flex: 1;
  flex-basis: auto;
}
.footer-menu__link {
  margin: 0 2rem 0 0;
  font-family: inherit;
  font-size: 1rem;
  color: #ffffff;
}

@media only screen and (max-width: 600px) {
  .header .nav {
    flex-direction: column;
    justify-content: center;
  }
  .header .hero {
    grid-template-columns: 1fr;
    justify-content: center;
    margin-top: 5rem;
  }
  .header .hero-text {
    order: 2;
    font-size: 1.2rem;
  }

  .main .about .container {
    grid-template-columns: 1fr;
    justify-content: center;
  }
  .main .about-image img {
    width: 100%;
    height: auto;
  }
  .main .service .container {
    grid-template-columns: 1fr;
    justify-content: center;
  }
  .main .contact .container {
    grid-template-columns: 1fr;
    justify-content: center;
    margin-bottom: 2rem;
  }
  .main .contact-image img {
    width: 100%;
    height: auto;
  }

  .footer .container {
    flex-direction: column;
    justify-content: center;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  .footer-menu__item {
    display: flex;
    flex-direction: row;
    flex: 1;
    flex-basis: auto;
    margin-bottom: 2rem;
  }
  .footer-menu__link {
    margin: 0 1rem 0 1rem;
    font-family: inherit;
    font-size: 1rem;
    color: #ffffff;
  }
  
}

</style>