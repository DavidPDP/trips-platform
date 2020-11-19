<template>
  <v-app dark>
    <v-app-bar dense fixed app src="/banner.jpg">
      <v-img src="/logo.png" max-height="50" max-width="50"></v-img>
      <p class="menu-bar__title">Stroll App</p>  
      <v-spacer></v-spacer>
      <v-menu left bottom min-width="300px" rounded offset-y>
        <template v-slot:activator="{ on }">
          <v-btn icon x-large v-on="on">
            <v-avatar size="36">
              <img :src="avatar">
            </v-avatar>
          </v-btn>
        </template>
        <v-card>
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center">
              <v-avatar color="brown" size="62">
                <img :src="avatar">
              </v-avatar>
              <p></p>
              <h3>{{currentUser.username}}</h3>
              <p class="caption mt-1">{{currentUser.email}}</p>
              <v-divider class="my-3"></v-divider>
              <v-btn depressed rounded text @click="trips()">Destinos</v-btn>
              <v-divider class="my-3"></v-divider>
              <v-btn depressed rounded text @click="bookings()">Mis Reservas</v-btn>
              <v-divider class="my-3"></v-divider>
              <v-btn depressed rounded text @click="logout()">Cerrar Sesión</v-btn>
            </div>
          </v-list-item-content>
        </v-card>
      </v-menu>
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <v-footer :absolute="true" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script lang="ts">

  import { Component, Vue } from 'vue-property-decorator';
  import { User } from '../types/model';

  @Component
  export default class SignInForm extends Vue {
    
    $auth: any;
    $router: any;
    avatar: string = '';
    currentUser: User = { username: '', email: '' };
    
    mounted(){
      if(process.client) {
        this.avatar = this.$store.getters['user/avatar'];
        this.currentUser = this.$auth.$storage.getCookie('user');
        console.log(this.currentUser);
      }
    }
  
    trips() {
      this.$router.push('/home');
    }

    bookings() {
      this.$router.push('/bookings');
    };

    logout() {
      this.$auth.$storage.setCookie('user', '');
      this.$auth.logout();
      this.$router.push({path:'/'});
    };

  }

</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap');

  .menu-bar__title {
    font-family: 'Dancing Script', cursive;
    color: #f8f8ff;
    font-size: 35px;
    padding: 1% 0 0 1%;
  }
</style>