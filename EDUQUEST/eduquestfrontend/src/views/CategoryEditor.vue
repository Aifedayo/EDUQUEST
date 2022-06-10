<template>
    <div class="container mt-4">
        <h4>Add a new Category</h4>
        <form @submit.prevent="onSubmit">
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Title</span>
                <input 
                    v-model="categoryName"
                    type="text" 
                    class="form-control" 
                    placeholder="Category title comes here" 
                    aria-label="Title" 
                    aria-describedby="basic-addon1"
                >
            </div>
            <div class="input-group">
                <span class="input-group-text">Textarea</span>
                <textarea 
                    v-model="categoryContext"
                    class="form-control"
                    rows="5" 
                    aria-label="With textarea">
                </textarea>
            </div>
            <button  class="btn btn-warning mt-3" type="submit">Submit</button>
        </form>
        <p v-if="error" class="nuted mt-2">
            {{ error }}
        </p>
    </div>
</template>

<script>
import { axios } from '@/common/api.service.js';
export default {
    name: "CategoryEditor",

    data() {
        return {
            categoryName: null,
            categoryContext: null,
        }
    },

    methods: {
        async performNetworkRequest() {
            let endpoint = '/api/v1/categories/';
            let method = "POST";

            try {
                const response = await axios({
                    method: method,
                    url: endpoint,
                    data: {
                        name: this.categoryName,
                        context: this.categoryContext,
                    }
                })
                console.log(response);
                this.$router.push({name: 'home'})
            } catch (error) {
                console.error(error.response)
            }
        },

        onSubmit() {
            if (!this.categoryName || !this.categoryContext) {
                this.error = "The question body nor the title cannot be empty"
            } else if (this.categoryContext.length > 255) {
                this.error = "The length of the question should not be greater than 255"
            } else {
                this.performNetworkRequest();
            }
        }
    }
}
</script>

<style>

</style>