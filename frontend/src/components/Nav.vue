<template>
    <nav>
        <div id="buttons">
        <router-link :class="{active: active == 'home'}" to="/home" class="nav-button">Home</router-link>
        <router-link :class="{active: active == 'discover'}" to="/discover" class="nav-button">Discover</router-link>
        <router-link :class="{active: active == 'search'}" to="/search" class="nav-button">Search</router-link>
        <router-link :class="{active: active == 'upload'}" to="/upload" class="nav-button">Upload</router-link>
        <router-link :class="{active: active == 'profile'}" :to="'/user/'+username" class="nav-button">Profile</router-link>
        </div>
        <hr id="nav-line">
    </nav>
</template>
<script>
export default {
    props: {
        username: String
    },
    methods: {
        get_active(new_route){
            let active = ""
            if(new_route.includes("home")){
                active = "home"
            }
            else if(new_route.includes("discover")){
                active = "discover"
            }
            else if(new_route.includes("search")){
                active = "search"
            }
            else if(new_route.includes("upload")){
                active = "upload"
            }
            else if(new_route.includes("user/"+this.username)){
                active = "profile"
            }
            console.log("Changed active to"+active)
            this.active = active
        }
    },
    watch: {
        $route(to, from){
            this.route = to.path
            this.get_active(to.path)
        }
    },
    mounted(){
        this.get_active(this.route)
    },
    data() {
        return{
            route: this.$route.path,
            active: "",
            colors: {
                home: "lightblue",
                discover: "green",
                search: "yellow",
                upload: "orange",
                profile: "purple"
            }
        }
    }
}
</script>

<style scoped>
.nav-button{
    margin-right: .5rem;
    background-color: #828788;
    padding-top: .4rem;
    padding-bottom: .4rem;
    padding-right: .6rem;
    padding-left: .6rem;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 0px;
    border-bottom-right-radius: 0px;
}

#buttons{
    margin-left: .6rem;
}

#nav-line{
    /* color: #828788; */
    color: v-bind(colors[active]);
    margin-top: 6px;
    border-width: 5px;
    border-radius: 2px;
    border-style: solid;
}
.active{
    background-color: v-bind(colors[active]);
}

</style>