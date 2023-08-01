<template>
  <header>
    <!-- <div v-if="token != null">
      <h1>Logged in</h1>
      <button @click="logout()">Logout</button>
      <button @click="kill_token()">kill token</button>
    </div> -->
    <Nav :username="username"/>
  </header>
  <RouterView @loginEvent="refresh_login()" :token="token" :user_data="user_data"/>
</template>

<script>
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';
import Nav from './components/Nav.vue'
export default {
  components: {
    Nav
  },
  methods: {
    logout(){
      localStorage.token = "";
      this.token = null;
    },
    kill_token(){
      localStorage.token = localStorage.token+"a2w323"
      this.token = localStorage.token;
    },
    refresh_login(){
      console.log("refersh_login")
      this.token = localStorage.token
      this.get_user_data();
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
        // Object.assign(this.user_data, data)

      })
      .catch((error) => {
        console.log(`Error getting user info: ${error}`)
      })
    }
  },
  mounted(){
    this.get_user_data()
    // double check token is valid
    if(this.token != null){

      const url = `${this.uri}/api/user/${this.token}`;
      axios.get(url, {
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json;charset=UTF-8",
          Authorization: `Token ${this.token}`
        }
      })
      .then(({data}) => {
        console.log(data);

      })
      .catch((error) => {
        localStorage.token = "";
        this.token = null;
        this.$router.push({name: 'login'});
      })
    }

  },
  data() {
    let token = null;
    if(localStorage.token){
      token = localStorage.token
    }
    return {
      token: token,
      hide_nav: false,
      uri: import.meta.env.VITE_APP_BASE_URI,
      username: "",
      user_data: {}
    }
  }
}
</script>
<style scoped>

</style>
