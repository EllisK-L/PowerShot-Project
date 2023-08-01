<template>
    <main>
        <h1>Login</h1>
        <p class="error" v-if="error != ''">Login failed - {{ error }}</p>
        <form>
            <div class="ps-row">
                <label for="username">Username: </label>
                <input type="text" id="username" name="username" v-model="username">
            </div>

            <div class="ps-row">
                <label for="password">Password: </label>
                <input type="password" id="password" name="password" v-model="password">
            </div>
            
            <div class="ps-row">
                <a>Login</a>
                <button type="button" @click="login()">Login</button>
            </div>
        </form>
    </main>
</template>

<script>
import axios from 'axios';
export default{
    methods: {
        login(){
            console.log("Login");
            const url = `${this.uri}/login/`;
            const data = {
                username: this.username,
                password: this.password
            }
            axios.post(url, data)
            .then((response) => {
                console.log(response.data);
                console.log(response.status)
                localStorage.token = response.data.token;

                this.$router.push("/")
                // console.log("emit");
                this.$emit("loginEvent");
            })
            // .catch((error) => {
            //     console.log(error)
            //     // this.error = error.response.data
            // })
        }
    },
    data() {
        return {
            username: "",
            password: "",
            uri: import.meta.env.VITE_APP_BASE_URI,
            error: ''
        }
    }
}
</script>
<style scoped>
input{
    width: 50%;
}
button{
    width: 52%;
}
.error{
    color: red;
}
</style>