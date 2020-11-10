<template>
  <v-app dark>
    <nuxt />
    <v-footer :absolute="true" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>