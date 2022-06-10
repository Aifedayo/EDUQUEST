<template>
        <!--

Design: https://dribbble.com/shots/13206178-Pokedex-404-Page

--> 
    <div>
        <div class="wrapper">

            <h3 class="sorry">sorry</h3>

            <div class="not-found">

                <span>4</span>

                <div class="pokeball-wrapper">
                <div class="pokeball-red"></div>
                <div class="pokeball-ball__center"></div>
                <div class="pokeball-shadow"></div>
                </div>

                <span>4</span>

                <div class="not-found__shadow"></div>

            </div>

            <h3 style="font-weight: 500;letter-spacing: 4px;">{{ message }}</h3>
        </div>
    </div>
</template>

<script>
export default {
    name: "NotFound",

    data() {
        return {
            message: "Not Found!"
        }
    },

    created() {
        document.title = this.message;
    }
}
</script>

<style>
         :root {
  --not-found-size: 8rem;
  --color-red: #e53935;
}


.wrapper {
  font-family: "Roboto", sans-serif;
  text-transform: uppercase;
  background: #f0f2f5;
  color: #273446;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.sorry {
  color: var(--color-red);
  letter-spacing: 4px;
}

.not-found {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  font-size: var(--not-found-size);
}

.pokeball-wrapper {
  background: white;
  margin: 0 0.5rem;
  border: 4px solid currentColor;
  width: calc(var(--not-found-size) - 3rem);
  height: calc(var(--not-found-size) - 3rem);
  border-radius: 50%;
  overflow: hidden;
  position: relative;
}

.pokeball-red {
  background: #e53935;
  width: 200%;
  transform: translate3d(-25%, 0, 0);
  height: calc(50% + 4px);
  border-bottom: 4px solid;
  border-radius: 50%;
}

.pokeball-ball__center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate3d(-50%, -50%, 0);
  border: 4px solid;
  width: 50%;
  height: 50%;
  border-radius: 50%;
  background: #455a64;
}

.pokeball-ball__center:after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate3d(-50%, -50%, 0);
  background: white;
  width: 50%;
  height: 50%;
  border: 4px solid;
  border-radius: 50%;
}

.pokeball-shadow {
  position: absolute;
  top: 0;
  left: 0;
  width: 110%;
  height: 110%;
  border-radius: 50%;
  transform: translate3d(-15%, -20%, 0);
  box-shadow: 10px 10px rgba(0, 0, 0, 0.1);
}

.not-found__shadow {
  min-width: 120%;
  height: 25px;
  background: #d6e1e6;
  border-radius: 50%;
  margin-bottom: 2rem;
  margin-top: -1rem;
}

.btn-link {
  display: block;
  margin-top: 2rem;
  text-align: center;
  color: white;
  background: var(--color-red);
  border-radius: 4px;
  padding: 5px;
  font-size: 0.8rem;
  text-decoration: none;

}

.btn-link:hover{
    text-decoration: none;
}
</style>