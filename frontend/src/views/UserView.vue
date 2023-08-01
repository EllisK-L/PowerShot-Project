<template>
    <main>
        <h1>
            {{ username }}
        </h1>
        <div><button @click="follow()" :disabled="user_data.username == username">{{ follow_text }}</button></div>
        <ImageList @postUpdate="update_images()" :images="images" :token="token" :username="username"/>    
    </main>
</template>
<script>
import ImageList from '../components/ImageList.vue';
import axios from 'axios';
export default {
    components: {
        ImageList
    },
    props: {
        token: String,
        user_data: Object
    },
    methods: {
        follow(){
            const url = `${this.uri}/api/follow/`
            const data = {
                follow_username:this.username,
                token: this.token 
            }
            axios.post(url,data, {
                headers: {
                Accept: "application/json",
                "Content-Type": "application/json;charset=UTF-8",
                Authorization: `Token ${this.token}`
                }
            })
            .then(({data}) => {
                console.log(data)
                this.$emit("loginEvent")
            })
        },  
        update_images(){
            const url = `${this.uri}/api/uploads/`
            axios.get(url, {
                params: {
                    username: this.username
                }
            })
            .then((data) => {
                console.log(data);
                this.images = data.data;
            })
            .catch((error) =>{
                console.log("error fetching uploads"+error)
            })
        }
    },  
    mounted(){
        this.$nextTick(() =>{
            for(let i=0; i<this.user_data.following.length; i++){
                    if(this.user_data.following[i].username == this.username){
                        this.follow_text = "Following";
                    }
                }
        })
        this.update_images()
    },
    data() {
        return {
            uri: import.meta.env.VITE_APP_BASE_URI,
            username: this.$route.params.username,
            images: [],
            follow_text: "Follow"
        }
    },
    watch: {
        user_data: {
            handler(newValue, oldValue){
                console.log("WATCHER")
                this.follow_text = "Follow";
                for(let i=0; i<this.user_data.following.length; i++){
                    if(this.user_data.following[i].username == this.username){
                        this.follow_text = "Following";
                    }
                }
            },
            deep: true
        },
        $route(to, form){
            this.username = to.params.username
            this.update_images()
        }
    }
}
</script>
<style scoped>
h1{
    margin-bottom: 0;
    font-size: 5rem;
}
p{
    cursor: pointer;
    padding: .2rem;
    /* width: 3rem; */
    margin-left: 1rem;
    margin-top: 1rem;
    margin-bottom: 1rem;
    outline-width: 1px;
    outline-style: solid;
    border-radius: 3px;
}
</style>