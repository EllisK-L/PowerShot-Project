<template>
    <h1>Upload</h1>
    <p v-if="error != ''">{{ error }}</p>
    <form>
        <div class="ps-row">
            <label for="caption">Caption</label>
            <input type="text" id="caption" v-model="caption">
        </div>
        <div class="ps-row">
            <label for="description">Description</label>
            <textarea id="description" v-model="description"></textarea>
        </div>
        <div class="ps-row">
            <label for="image">Upload Image</label>
            <input type="file" id="image" name="image" ref="file">
        </div>
        <div class="ps-row">
            <label for="button">Post!</label>
            <button type="button" id="button" @click="submit()">Post!</button>
        </div>
    </form>
</template>
<script>
import axios from 'axios';
export default{
    props: {
        token: String
    },
    methods: {
        submit() {
            const validImageTypes = ['image/gif', 'image/jpeg', 'image/png', 'image/jpeg'];
            if(validImageTypes.includes(this.$refs.file.files[0].type)){
                console.log(this.$refs.file.files[0])

                const formData = new FormData();
                formData.append("caption",this.caption)
                formData.append("description", this.description)
                formData.append("token", this.token)
                formData.append("image",this.$refs.file.files[0])


                const url = `${this.uri}/api/upload/`
                axios.post(url, formData)
                .then((response) => {
                    console.log(response)
                    if(response.status == 201){
                        this.$router.push({name:"home"})
                    }
                })
            }
            else{
                this.error = "Please submit a gif, jpeg, or png only!"

            }
        }
    },
    data() {
        return {
            uri: import.meta.env.VITE_APP_BASE_URI,
            caption:"",
            description: "",
            image: null,
            error: ""
        }
    }
}
</script>