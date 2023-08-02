<template>
  <main>
      <h1>Posts From Following</h1>
      <ImageList @postUpdate="get_posts()" :images="sorted_posts" :token="token" :username="username" />
      <h2 v-if="sorted_posts.length == 0">Not following anyone</h2>
  </main>
</template>
<script>
import ImageList from '../components/ImageList.vue';
import axios from 'axios';
export default{
  components: {
    ImageList
  },
  props:{
    user_data: Object,
    token: String,
    username: String,
  },
  methods: {
    get_posts(){
      let first_update = true
      if(this.user_data.following != undefined){
        const url = `${this.uri}/api/uploads/`
        this.user_data.following.forEach(element => {
          console.log(element.username)
            axios.get(url, {
                params: {
                    username: element.username
                }
            })
            .then((data) => {
                console.log(data);

                data.data.forEach((element) => {
                  let found = false;
                  for(let i=0; i < this.posts.length; i++){
                    if(element.id == this.posts[i].id){
                      this.posts[i] = element;
                      found = true;
                      break;
                    }
                  }
                  if(!found){
                    this.posts.push(element)
                  }
                })
            })
        });
      }
      else{
        console.log("UNDEFINED")
      }
    }
  },
  mounted(){
    this.get_posts()
  },
  computed: {
        sorted_posts(){
            let sorted_images = this.posts.map(obj => ({
              ...obj,
              date: new Date(obj.date)
            }))
            sorted_images.sort((a, b) => a.date - b.date)
            return sorted_images
        }
    },
  data(){
    return{
      uri: import.meta.env.VITE_APP_BASE_URI,
      posts: []
    }
  },
  watch:{
    user_data: {
            handler(newValue, oldValue){
                this.get_posts()
            },
            deep: true
        },
  }
}
</script>