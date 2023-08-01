<template>
    <div class="container">
        <div class="ps-row">
                <div>{{ username }}</div>
                <form>
                    <input type="text" v-model="comment">
                    <button type="button" @click="post_comment()">Post</button>
                </form>
        </div>
        <div class="ps-row" v-for="(item, index) in comments">
            <nav> <router-link :to="'/user/'+item.commenter.username">{{ item.commenter.username }}</router-link></nav>
            <div>{{ item.text }}</div>
        </div>
    </div>
</template>
<script>
import axios from 'axios';
export default{
    props:{
        upload_id: Number,
        username: String,
        token: String
    },
    methods:{
        post_comment(){
            const url = `${this.uri}/api/create_comment/`;
            const data = {
                text:this.comment,
                upload_id:this.upload_id,
                token:this.token
            }
            axios.post(url, data, {
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json;charset=UTF-8",
                Authorization: `Token ${this.token}`
            }
            })
            .then(({data}) =>{
                console.log(data)
                this.comment = ""
                this.get_comments()
            })
        },  
        get_comments(){
            const url = `${this.uri}/api/comments/`;
            axios.get(url, {
                params:{
                    upload_id:this.upload_id
                }
            })
            .then(({data}) =>{
                console.log(data)
                this.comments = data
            })
        }
    },
    mounted() {
        this.get_comments()
    },
    data(){
        return {
            uri: import.meta.env.VITE_APP_BASE_URI,
            comments: [],
            comment: ""
        }
    }
}
</script>
<style scoped>
.container{
    max-height: 20rem;
    overflow: scroll;
}
</style>