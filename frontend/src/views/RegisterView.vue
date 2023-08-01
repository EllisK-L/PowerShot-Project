<template>
    <main>
        <h1>Register</h1>

        <form>
            <label for="fname">First Name: </label>
            <input type="text" id="fname" name="fname">

            <br>
            <label for="lname">Last Name: </label>
            <input type="text" id="lname" name="lname">

            <br>
            <label for="username">Username: </label>
            <input type="text" id="username" name="username">

            <br>
            <label for="email">Email: </label>
            <input type="text" id="email" name="email">

            <br>
            <label for="password1">Password: </label>
            <input type="text" id="password1" name="password1">

            <br>
            <label for="password2">Confirm Password: </label>
            <input type="text" id="password2" name="password2">

            <br>
            <br>
            <input type="submit" value="Register">
        </form>
    </main>

</template>

<script>
export default{
    data() {
        console.log(import.meta.env.VITE_APP_BASE_URI)
        return "oof"
    }
}
</script>