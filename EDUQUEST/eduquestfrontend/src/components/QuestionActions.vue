<template>
    <div class="container mt-3">
        <router-link 
            class="btn btn-sm btn-warning"
            :to="{ name: 'question-editor', params: {slug: slug}}"
        >
            Edit
        </router-link>
        <button class="btn btn-sm btn-danger mx-3" @click="showDeleteModal = !showDeleteModal">Delete</button>
        
        <button v-show="showDeleteModal" 
            class="btn btn-sm btn-outline-danger"
            @click="deleteQuestion"    
        >
            Yes, delete the Question
        </button>
        <hr>
    </div>
</template>

<script>
import { axios } from '@/common/api.service.js'
export default {
    name: "QuestionActions",

    props: {
        slug: {
            type: String,
            required: true,
        }
    },

    data() {
        return {
            showDeleteModal: false,
        }
    },

    methods: {
        async deleteQuestion() {
            const endpoint = `/api/v1/questions/${this.slug}/`
            try {
                await axios.delete(endpoint);
                this.$router.push({
                    name: 'home'
                })
            } catch (error) {
                console.log(error.response);
                alert(error.response.statusText);
            }
        }
    }
}
</script>