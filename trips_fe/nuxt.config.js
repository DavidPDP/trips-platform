import colors from 'vuetify/es5/util/colors'

export default {
  
  head: {
    titleTemplate: '%s - trips-fe',
    title: 'trips-fe',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  css: [],

  plugins: ['~/plugins/axios_port.ts'],

  components: true,

  buildModules: [
    '@nuxt/typescript-build',
    '@nuxtjs/vuetify',
  ],

  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next'
  ],

  axios: { baseURL: 'http://localhost:8000' },

  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
    },
  },

  auth: {
    localStorage: false,
    redirect: {
      login: '/',
      logout: '/',
      callback: '/',
      home: '/home',
    },
    strategies: {
      local: {
        scheme: 'refresh',
        token: { property: 'access', maxAge: 300 },
        refreshToken: { property: 'refresh', data: 'refresh', maxAge: 60 * 60 * 24 },
        endpoints: {
          login: { url: '/auth/signin', method: 'post' },
          refresh: { url: '/auth/refresh', method: 'post' },
          user: false,
          logout: false
        }
      }
    }
  },

  build: {}

}
