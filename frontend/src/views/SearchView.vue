<template>
<main>
    <h1>Search</h1>
    <div class="ps-row">
        <div>
            Search for some usernames
        </div>
        <div>
            <input type="text" @input="get_users()" v-model="user_input">
        </div>
    </div>
    <UserItem :users="users" />
</main>
</template>
<script>
import debounce from 'lodash.debounce'
import axios from 'axios';
import UserItem from '../components/UserItem.vue'
export default{
    components: {
        UserItem
    },
    props:{
        token: String
    },
    methods: {
        get_users: debounce(function(){
            console.log(this)
            const url = `${this.uri}/api/users`
            axios.get(url, {
                params: {
                    search: this.user_input
                }
            })
            .then(({data}) => {
                console.log(data);
                this.users = data
            })
        }, 500)
    },
    data(){
        return{
            uri: import.meta.env.VITE_APP_BASE_URI,
            user_input: "",
            users: []
        }
    }
}
</script>