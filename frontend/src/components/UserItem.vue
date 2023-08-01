<template>
    <div class="ps-row" v-for="(item, index) in users">
        <nav>
        <router-link :to="`/user/${item.username}`">
            {{ item.username }}
        </router-link>
        </nav>
    </div>
</template>
<script>
export default{
    props:{
        users: Array
    }
}
</script>