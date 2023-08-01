<template>
    <div>
    <div class="ps-row" :class="{detail: is_detail}">
        <div @click="$emit('postClick')">
            <nav>
                <router-link :to="`/user/${image.user.username }`">
                    <h3 class="username">{{ image.user.username }}</h3>
                </router-link>
            </nav>
            <h1>{{ image.caption }}</h1>
            <h3>{{ image.description }}</h3>
            <small>{{ image.date }}</small>
        </div>
        <img @click="$emit('postClick')" class=post_image :src="image.image"/>
        <div @click="like()">
            <span class="material-symbols-outlined liked">
                favorite
            </span>
            Liked by {{ image.likes.length }}
        </div>
        <div v-if="!is_detail" @click="$emit('postClick')">
            ↓ Comments ↓
        </div>
    </div>
    <div v-if="is_detail">
            <Comments :upload_id="image.id" :username="username" :token="token"/>
    </div>
    </div>
</template>
<script>
import axios from 'axios';
import Comments from './Comments.vue';
export default {
    components: {
        Comments
    },
    props: {
        token: String,
        image: Object,
        username: String,
        is_detail: Boolean
    },
    methods: {
        like(){
            const url = `${this.uri}/api/like/`;
            const data = {
                token: this.token,
                post_id: this.image.id,
                username: this.username
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
        this.$emit("postUpdate")

      })
      .catch((error) => {
        console.log(error)
      })
        }
    },
    data() {
        return {
            uri: import.meta.env.VITE_APP_BASE_URI,
        }
    }
}
</script>
<style scoped>
 .post_image{
    /* width: 100%; */
    max-height: 300px;
 }
 a {
  color: inherit;
  text-decoration: none;
  background: none;
  border: none;
  padding: 0;
  margin: 0;
}
h1 {
    margin-top: 0;
}
h3 {
    margin-left: 1rem;
}
small{
    font-size: smaller;
}
.liked{
    color: red;
}
.detail{
    box-shadow: 0 0 0 max(100vh, 100vw) rgba(0, 0, 0, .5);
}
.username{
    margin: 0;
}
</style>
