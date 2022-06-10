<template>
  <div class="home mt-2">
    <div class="container">
        <div v-for="question in questions"
                :key="question.uuid"
        >

            <section class="dark">
                <div class="container py-4">
                    <router-link :to="{ name: 'question', params: {slug: question.slug} }"
                      class="question-link"
                    >
                        <article class="postcard dark blue">
                            <a class="postcard__img_link" href="#">
                                <img class="postcard__img" src="https://picsum.photos/1000/1000" alt="Image Title" />
                            </a>
                            <div class="postcard__text">
                                <h1 class="postcard__title blue"><a href="#"> {{ question.title }}</a></h1>
                                <div class="postcard__subtitle small">
                                    <time datetime="2020-05-25 12:00:00">
                                        <i class="fas fa-calendar-alt mr-2"></i>{{ question.created_at }}
                                    </time>
                                </div>
                                <div class="postcard__bar"></div>
                                <div class="postcard__preview-txt">{{ question.content }}</div>
                                <ul class="postcard__tagbox">
                                    <li class="tag__item"><i class="fas fa-tag mr-2"></i>{{ question.category }}</li>
                                    <li class="tag__item"><i class="fas fa-clock mr-2"></i>55 mins.</li>
                                    <li class="tag__item play blue">
                                        <a href="#"><i class="fas fa-play mr-2"></i>{{ question.updated_at }}</a>
                                    </li>
                                </ul>
                            </div>
                        </article>
                    </router-link>
                </div>
            </section>
        </div>
        <div class="my-4">
            <p v-show="loadingQuestions">...loading...</p>
            <button v-show="next" @click="getQuestions"
                class="btn btn-sm btn-outline-danger"
            >
                Load more questions
            </button>
        </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { axios } from "@/common/api.service.js";
export default {
  name: "HomeView",


    props: {
        slug: {
            type: String,
            required: true,
        }
    },

    data() {
        return {
        questions: [],
        next: null,
        loadingQuestions: false,
        }
    },

  created() {
    this.getQuestions();
  },

  methods: {
    async getQuestions() {
      let endpoint = `/api/v1/categories/${this.slug}/questions/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      try {
        const response = await axios.get(endpoint);
        this.questions.push(...response.data.results);
        this.loadingQuestions = false;
        if (response.data.next){
          this.next = response.data.next;
        } else {
          this.next = null;
        }
      } catch (error) {
        console.error(error.response);
        alert(error.response.statusText);
      }
    }
  }
}
</script>

<style scoped>

  .question-author {
    font-weight: bold;
    color: rgb(244, 103, 103);
  }

  .question-link {
    text-decoration: none;
    color: black;
    font-weight: 400;
  }

  .question-link:hover {
    text-decoration: none;
    color: rgb(63, 61, 61);
    font-weight: 400;
  }

  @import url("https://fonts.googleapis.com/css2?family=Baloo+2&display=swap");
/* This pen */
body {
  font-family: "Baloo 2", cursive;
  font-size: 16px;
  color: #ffffff;
  text-rendering: optimizeLegibility;
  font-weight: initial;
}


a, a:hover {
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

#pageHeaderTitle {
  margin: 2rem 0;
  text-transform: uppercase;
  text-align: center;
  font-size: 2.5rem;
}

/* Cards */
.postcard {
  flex-wrap: wrap;
  display: flex;
  box-shadow: 0 4px 21px -12px rgba(0, 0, 0, 0.66);
  border-radius: 10px;
  margin: 0 0 2rem 0;
  overflow: hidden;
  position: relative;
  color: #ffffff;
}
.postcard.dark {
  background-color: #18151f;
}
.postcard.light {
  background-color: #e1e5ea;
}
.postcard .t-dark {
  color: #18151f;
}
.postcard a {
  color: inherit;
}
.postcard h1, .postcard .h1 {
  margin-bottom: 0.5rem;
  font-weight: 500;
  line-height: 1.2;
}
.postcard .small {
  font-size: 80%;
}
.postcard .postcard__title {
  font-size: 1.75rem;
}
.postcard .postcard__img {
  max-height: 180px;
  width: 100%;
  object-fit: cover;
  position: relative;
}
.postcard .postcard__img_link {
  display: contents;
}
.postcard .postcard__bar {
  width: 50px;
  height: 10px;
  margin: 10px 0;
  border-radius: 5px;
  background-color: #424242;
  transition: width 0.2s ease;
}
.postcard .postcard__text {
  padding: 1.5rem;
  position: relative;
  display: flex;
  flex-direction: column;
}
.postcard .postcard__preview-txt {
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: justify;
  height: 100%;
}
.postcard .postcard__tagbox {
  display: flex;
  flex-flow: row wrap;
  font-size: 14px;
  margin: 20px 0 0 0;
  padding: 0;
  justify-content: center;
}
.postcard .postcard__tagbox .tag__item {
  display: inline-block;
  background: rgba(83, 83, 83, 0.4);
  border-radius: 3px;
  padding: 2.5px 10px;
  margin: 0 5px 5px 0;
  cursor: default;
  user-select: none;
  transition: background-color 0.3s;
}
.postcard .postcard__tagbox .tag__item:hover {
  background: rgba(83, 83, 83, 0.8);
}
.postcard:before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-image: linear-gradient(-70deg, #424242, transparent 50%);
  opacity: 1;
  border-radius: 10px;
}
.postcard:hover .postcard__bar {
  width: 100px;
}

@media screen and (min-width: 769px) {
  .postcard {
    flex-wrap: inherit;
  }
  .postcard .postcard__title {
    font-size: 2rem;
  }
  .postcard .postcard__tagbox {
    justify-content: start;
  }
  .postcard .postcard__img {
    max-width: 300px;
    max-height: 100%;
    transition: transform 0.3s ease;
  }
  .postcard .postcard__text {
    padding: 3rem;
    width: 100%;
  }
  .postcard .media.postcard__text:before {
    content: "";
    position: absolute;
    display: block;
    background: #18151f;
    top: -20%;
    height: 130%;
    width: 55px;
  }
  .postcard:hover .postcard__img {
    transform: scale(1.1);
  }
  .postcard:nth-child(2n+1) {
    flex-direction: row;
  }
  .postcard:nth-child(2n+0) {
    flex-direction: row-reverse;
  }
  .postcard:nth-child(2n+1) .postcard__text::before {
    left: -12px !important;
    transform: rotate(4deg);
  }
  .postcard:nth-child(2n+0) .postcard__text::before {
    right: -12px !important;
    transform: rotate(-4deg);
  }
}
@media screen and (min-width: 1024px) {
  .postcard__text {
    padding: 2rem 3.5rem;
  }

  .postcard__text:before {
    content: "";
    position: absolute;
    display: block;
    top: -20%;
    height: 130%;
    width: 55px;
  }

  .postcard.dark .postcard__text:before {
    background: #18151f;
  }

  .postcard.light .postcard__text:before {
    background: #e1e5ea;
  }
}
/* COLORS */

.postcard .postcard__tagbox .blue.play:hover {
  background: #0076bd;
}

.blue .postcard__title:hover {
  color: #0076bd;
}

.blue .postcard__bar {
  background-color: #0076bd;
}

.blue::before {
  background-image: linear-gradient(-30deg, rgba(0, 118, 189, 0.1), transparent 50%);
}

.blue:nth-child(2n)::before {
  background-image: linear-gradient(30deg, rgba(0, 118, 189, 0.1), transparent 50%);
}

@media screen and (min-width: 769px) {

  .blue::before {
    background-image: linear-gradient(-80deg, rgba(0, 118, 189, 0.1), transparent 50%);
  }

  .blue:nth-child(2n)::before {
    background-image: linear-gradient(80deg, rgba(0, 118, 189, 0.1), transparent 50%);
  }
}


</style>