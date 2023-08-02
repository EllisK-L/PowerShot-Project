<template>
    <main>
        <h1>Register</h1>
        <nav><router-link to="/login"><h2>Or Login</h2></router-link></nav>
        <form>
            <div class="ps-row">
                <label for="fname">First Name: </label>
                <input type="text" id="fname" name="fname" v-model="fname">
            </div>

            <div class="ps-row">
            <label for="lname">Last Name: </label>
            <input type="text" id="lname" name="lname" v-model="lname">
            </div>

            <div class="ps-row">
            <label for="username">Username: </label>
            <input type="text" id="username" name="username" v-model="username">
            </div>

            <div class="ps-row">
            <label for="email">Email: </label>
            <input type="text" id="email" name="email" v-model="email">
            </div>

            <div class="ps-row">
            <label for="password1">Password: </label>
            <input type="password" id="password1" name="password1" v-model="password1">
            </div>

            <div class="ps-row">
            <label for="password2">Confirm Password: </label>
            <input type="password" id="password2" name="password2" v-model="password2">
            </div>

            <div class="ps-row">
            <label for="phone">Phone Number</label>
            <input type="text" id="phone" name="phone" v-model="phone">
            </div>

            <button type="button" @click="register()">Register</button>
        </form>
    </main>

</template>

<script>
import axios from 'axios';
export default{
    props:{
    },
    methods:{
        register(){
            const url = `${this.uri}/api/register`
            const data= {
                username: this.username,
                password: this.password1,
                password2: this.password2,
                email: this.email,
                first_name: this.fname,
                last_name: this.lname,
                phone: this.phone
            }
            axios.post(url, data)
            .then((response) => {
                console.log(response.data);
                console.log(response.status)
                localStorage.token = response.data.token;

                this.$router.push("/login")
            })
        }
    },
    data() {
        console.log()
        return {
            uri: import.meta.env.VITE_APP_BASE_URI,
            fname: "",
            lname: "",
            username: "",
            email: "",
            password1: "",
            password2: "",
            phone: ""
        }
    }
}
</script>

<style scoped>
a{
    text-decoration: underline;
}

</style>