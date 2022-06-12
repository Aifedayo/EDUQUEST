<template>
    <div class="container mt-3">
        <div v-if="question" class="container">
        <h1>{{ question.title }}</h1>

        <p> {{ question.content }}</p>
        <p class="mb-0">
            Posted by:
            <span class="author-name">{{ question.author }}</span>
        </p>
        <p>{{ question.created_at }}</p>

        <QuestionActions 
            v-if="isQuestionAuthor"
            :slug="question.slug"
        />

        <div v-if="userHasAnswered">
            <p class="answer-added">You've written an answer!</p>
        </div>
        <div v-else-if="showForm">
            <form @submit.prevent="onSubmit">
                <p>Answer the Question</p>
                <textarea 
                    v-model="newAnswerBody"
                    class="form-control" placeholder="Share your knowledge" 
                    rows="10"
                >
                </textarea>
                <button class="btn btn-outline-success my-3" @click="showForm=true">
                    Send your Answer
                </button>
            </form>
            <p v-if="error" class="error mt-2">{{ error }}</p>
        </div>
        <div v-else>
            <button class="btn btn-outline-danger" @click="showForm=true">
                Answer the Question
            </button>
        </div>
        </div>
        <div v-else>
            <h1 class="error text-center">404 - Question Not Found</h1>
        </div>
        <div v-if="question" class="container">
            <AnswerComponent 
                v-for="answer in answers"
                :key="answer.uuid"
                :answer="answer"
                :requestUser="requestUser"
                @delete-answer="deletAnswer"
            />
        </div>
        <div class="my-4">
            <p v-show="loadingAnswers">...loading...</p>
            <button v-show="next" @click="getQuestionAnswers"
                class="btn btn-sm btn-outline-danger"
            >
            Load more answers
                </button>
            </div>
    </div>
</template>

<script>
import { axios } from '@/common/api.service.js';
import AnswerComponent from '@/components/Answer.vue';
import QuestionActions from '@/components/QuestionActions.vue';

export default {
    name: "QuestionDetail",

    props: {
        slug: {
            type: String,
            required: true,
        }
    },

    components: {
    AnswerComponent,
    QuestionActions,
  },

    data() {
        return {
            question: null,
            answers: [],
            next: null,
            loadingAnswers: false,
            userHasAnswered: false,
            showForm: false,
            newAnswerBody: null,
            newQuestionTitle: null,
            error: null,
            requestUser: null,
        }
    },

    computed: {
        isQuestionAuthor() {
            return this.question.author == this.requestUser;
        }
    },

    methods: {
        setRequestUser() {
            this.requestUser = window.localStorage.getItem("username");
        },

        setPageTitle(title) {
            document.title = title;
        },

        async getQuestionDetail() {
            const endpoint = `/api/v1/question/${this.slug}/`;
            try {
                const response = await axios.get(endpoint);
                this.question = response.data;
                this.userHasAnswered = response.data.user_has_answered;
                this.setPageTitle(response.data.content);
            } catch(error) {
                console.error(error.response);
                const title = '404 - Not Found!';
                this.setPageTitle(title);
            }
        },

        async getQuestionAnswers() {
            let endpoint = `/api/v1/question/${this.slug}/answers/`;
            if (this.next) {
                endpoint = this.next;
            }
            this.loadingAnswers = true;
            try {
                const response = await axios.get(endpoint);
                this.answers.push(...response.data.results);
                this.loadingAnswers = false;
                if (response.data.next) {
                this.next = response.data.next;
                } else {
                this.next = null;
                }
            } catch (error) {
                console.log(error.response);
                alert(error.response.statusText);
            }
        },

        async onSubmit() {
            if (!this.newAnswerBody){
                this.error = "You can't send an empty answer!"
                return
            }
            const endpoint = `/api/v1/question/${this.slug}/answer/`;
            try {
                const response = await axios.post(endpoint, {
                    body: this.newAnswerBody,
                });
                this.answers.unshift(response.data);
                this.newAnswerBody = null;
                this.showForm = false;
                this.userHasAnswered = true;
                if (this.error) {
                    this.error = null;
                }
            } catch (error) {
                console.error(error.response);
                alert(error.response.statusText);
            }
        },

        async deletAnswer(answer) {
            const endpoint = `/api/v1/answers/${answer.uuid}/`;
            try {
                await axios.delete(endpoint);
                this.answers.splice(this.answers.indexOf(answer), 1);
                this.userHasAnswered = false;
            } catch (error) {
                console.error(error);
            }
        }
    },

    created() {
        document.title = "QueAns";
        this.getQuestionDetail();
        this.getQuestionAnswers();
        this.setRequestUser();
    }
}
</script>

<style>
    .author-name {
        font-weight: bold;
          color: #dc3545; 
    }

    .answer-added {
        color: green;
    }
</style>
