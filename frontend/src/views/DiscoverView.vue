<template>
    <main>
        <h1>Posts From Following</h1>
        <ImageList @postUpdate="get_posts()" :images="sorted_posts" :token="token" :username="username" />
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
        if(this.user_data.following != undefined){
          const url = `${this.uri}/api/uploads/`
              axios.get(url)
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
            let sorted_images = this.posts.filter(obj => obj.user.username !== this.user_data.username )
            sorted_images = sorted_images.map(obj => ({
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