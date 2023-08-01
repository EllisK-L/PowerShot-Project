<template>
<div class="ps-row">
    <div>
            <h1>{{ image.caption }}</h1>
            <h3>{{ image.description }}</h3>
            <small>{{ image.date }}</small>
        </div>
        <img class=post_image :src="image.image"/>
</div>
</template>
<script>
export default {
    props: {
        image: Object
    }
}
</script>
<style scoped>
.post_image{
    width: 100%;
}
.ps-row{
    box-shadow: 0 0 0 max(100vh, 100vw) rgba(0, 0, 0, .5);
}
</style>