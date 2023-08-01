<template>
    <main>
        <div v-if="show_login">
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
        </div>
        <div v-if="!show_login" class="ps-row">
            <div>
                <h3>Enter the code you got on your phone</h3>
                <p v-if="error">Please Try Again</p>
            </div>
            <div>
                <input type="text" v-model="phone_code"/>
                <button type="button" @click="check_code()">submit</button>
            </div>

        </div>
    </main>
</template>

<script>
import axios from 'axios';
export default{
    props:{
        token: String
    },
    methods: {
        check_code(){
            console.log(this.user_data.phone_code)
            console.log(this.phone_code)
            if(this.user_data.phone_code == this.phone_code){
                this.$router.push("/home")
                this.$emit("loginEvent");
            }
            else{
                this.error = true
            }
        },
        get_user_data(){
            const url = `${this.uri}/api/user/${this.token}`;
            axios.get(url, {
                headers: {
                Accept: "application/json",
                "Content-Type": "application/json;charset=UTF-8",
                Authorization: `Token ${this.token}`
                }
            })
            .then(({data}) => {
                this.username = data.username
                this.user_data = data
                if(!this.user_data.phone_valid){
                    this.show_login = false;   
                }
                else{
                    this.$router.push("/")
                    this.$emit("loginEvent");
                }

                

            })
            .catch((error) => {
                console.log(`Error getting user info: ${error}`)
            })
        },
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


                // PHONE STUFF
                this.get_user_data()


                /////uncomment
                // this.$router.push("/")

                // this.$emit("loginEvent");
                /////uncomment
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
            error: '',
            user_data: {},
            show_login: true,
            phone_code: "",
            error: false
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