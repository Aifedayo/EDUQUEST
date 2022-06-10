<template>
    <div class="container mt-2">
        <h4 class="my-2">Edit your Answer</h4>
        <form @submit.prevent="onSubmit">
            <textarea
                v-model="answerBody"
                class="form-control"
                placeholder="Your answer goes here!"
                cols="30" rows="10"
            >
            </textarea>
            <button class="btn btn-outline-danger mt-4">Publish</button>
        </form>
        <p v-if="error" class="muted mt-2">{{ error }}</p>
    </div>
</template>

<script>
import { axios } from '@/common/api.service.js';
export default {
    name: "AnswerEditor",

    props: {
        uuid: {
            type: String,
            required: true,
        }
    },

    data() {
        return {
            questionSlug: null,
            answerBody: null,
            error: null,
        }
    },

    methods: {
        async onSubmit() {
            if (!this.answerBody) {
                this.error = "You cannot submit an empty answer";
                return;
            }
            const endpoint = `/api/v1/answers/${this.uuid}/`;
            try {
                await axios.put(endpoint, {body: this.answerBody });
                this.$router.push({
                    name: "question",
                    params: { slug: this.questionSlug },
                });
            } catch (error) {
                console.error(error);
                alert(error.response.statusText);
            }
        },
    },

    async beforeRouteEnter(to, from, next) {
        const endpoint = `/api/v1/answers/${to.params.uuid}/`;
        try {
            const response = await axios.get(endpoint);
            return next(
                (vm) => (
                (vm.answerBody = response.data.body),
                (vm.questionSlug = response.data.question_slug)
                )
            );
        } catch (error) {
            console.log(error.response);
            alert(error.response.statusText);
        }
    }
}
</script>