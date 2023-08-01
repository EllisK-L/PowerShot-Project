<template>
    <div>
        <ImageItem @postUpdate="$emit('postUpdate')" class="image-item" v-for="(item, index) in images" :image="item" :token="token" :username="username" :is_detail="false" @postClick="post_details(item)"/>
        <!-- <PostDetail :image="detail_image" v-if="detail" class="detail"/> -->
        <ImageItem v-if="detail" @postUpdate="$emit('postUpdate')" id="detail" :image="detail_image" :token="token" :username="username" :is_detail="true"/>
    </div>
</template>
<script>
import ImageItem from './ImageItem.vue';
import PostDetail from './PostDetail.vue';
export default {
    components: {
        ImageItem,
        PostDetail
    },
    props:{
        images: Array,
        token: String,
        username: String
    },
    methods: {
        post_details(image){
            if(this.detail){
                this.detail = false
            }
            else{
                this.detail = true
                this.detail_image = image
            }
        }
    },
    data(){
        return {
            detail: false,
            detail_image: null
        }
    }
}
</script>
<style scoped>
.image-item{
    cursor: pointer;
}
#detail{
    position: fixed;
    left: 40px;
    right: 40px;
    margin: auto;
    top: 10%;
    border-radius: 2rem;
}

</style>