<template>
  <div>
      <nav class ="navbar" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
        <div class="navbar-brand">
          <a class="navbar-item is-size-4" href="/">LVIC</a>
        </div>

        <div id="navbar-item" class="navbar-menu">
          <div class="navbar-start">
            <a href="/" class="navbar-item">Home</a>
            <a href="/about" class="navbar-item">About</a>
          </div>

          <div class="navbar-end">
            <div class="navbar-item">
              <div class="buttons">
                <a href="/sign-up" class="button is-primary"><strong>Sign Up</strong></a>
                <a href="/log-in" class="button is-light">Log in</a>
              </div>
            </div>
          </div>
        </div>
      </nav>

    <router-view/>

    <footer class="footer">
      <p class="has-text-centered">Created by Travis Jackson</p>
      <p class="has-text-centered">@2023 Technologent</p>
      <p class="has-text-centered">770 E Pilot Road, Ste G, Las Vegas, NV 89119 | 702-575-6916</p>
    </footer>
  </div>
</template>

<style lang="scss">
@import '/Users/travis.jackson/PycharmProjects/WMS_Backend/node_modules/bulma';

</style>
<script setup>

</script>
