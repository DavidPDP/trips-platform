<template>
  <div class="main-container">
    <section class="auth-sidebar">
      <h1>La aventura vale la pena Alimenta tu alma.</h1>
      <div class="auth-sidebar__logo">
        <v-img style="margin: 0 0 0 10%;" src="/logo.png" max-height="100" max-width="114"></v-img>
        <p>Stroll App</p>
      </div>
      <p></p>
    </section>
    <section class="auth-content">
      <nav>
        <p>{{ navText }}<a href="#" @click.prevent="switchSignForm()">{{ navLinkText }}</a></p>
      </nav>
      <SignInForm v-if="signInVisible" />
      <SignUpForm v-else @signSuccessful="switchNotification"/>
      <v-snackbar v-model="notification" :timeout="2000">
        {{ notificationText }}
        <template v-slot:action="{ attrs }">
          <v-btn color="blue" text v-bind="attrs" @click="notification = false">Close</v-btn>
        </template>
      </v-snackbar>
    </section>
  </div>
</template>

<script lang="ts">
  import { Component, Vue } from 'vue-property-decorator';

  import SignInForm from '../components/SignInForm.vue';
  import SignUpForm from '../components/SignUpForm.vue';

  @Component( { components: { SignInForm, SignUpForm }} )
  export default class Index extends Vue {
    
    auth: boolean = false;
    signInVisible: boolean = true;
    notification: boolean = false;
    notificationText: string = '';
    navText: string = '¿No es un miembro? ';
    navLinkText: string = 'Regístrate ahora.';

    switchSignForm() {
      if (this.signInVisible) {
        this.navText = '¿Ya eres usuario? ';
        this.navLinkText = 'Inicia sesión ahora.';
        this.signInVisible = false;
      } else {
        this.navText = '¿No es un miembro? ';
        this.navLinkText = 'Regístrate ahora.';
        this.signInVisible = true;
      }
    }

    switchNotification(text:string) {
      this.notificationText = text;
      this.notification = true;
      this.switchSignForm();
    }

  };

</script>

<style lang="scss">
  @import url('https://fonts.googleapis.com/css?family=Poppins:300,400,800&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap');

  .main-container {
    display: flex;
    display: -ms-flexbox;
    overflow: hidden;
  }

  @media(min-width: 576px) {
    .main-container {
      flex-direction: row;
      -ms-flex-direction: row;

      .auth-sidebar{
        width: 70%;
        height: 100vh;

        .auth-sidebar__logo {
          align-items: center;
        }

        h1 {
          font-size: 30px;
        }

        p {
          font-size: 60px;
        }
      }

      .auth-content{
        width: 100%;
        height: 70%;
      }

    }
  }

  @media(max-width: 768px) {
    .main-container {
      flex-direction: column;
      -ms-flex-direction: column;
      
      .auth-sidebar{
        width: 100vw;
        height: 30%;

        .auth-sidebar__logo {
          flex-direction: row;
          justify-content: center;
          height: 95px;
        }

        h1 {
          font-size: 20px;
        }

        p {
          font-size: 40px;
          
        }
      }

      .auth-content{
        width: 100vw;
        height: 70%;
      }

    }
  }

  .auth-sidebar {
    background: #6930c3;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;

    .auth-sidebar__logo {
      display: flex; 
      flex-direction: column;
    }

    h1 {
      color: #f8f8ff;
      padding: 10% 10% 2% 10%;
      font-family: 'Poppins';
    }

    p {
      font-family: 'Dancing Script', cursive;
      color: #f8f8ff;
      font-size: 60px;
    }

  }

  .auth-content {
    text-align: center;


    h1 {
      font: bold 32px/38px "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
      color: #5e60ce;
    }

    h4 {
      font-family: 'Metropolis-Regular', "Segoe UI", Helvetica Neue, Helvetica, sans-serif;
      color: #5e60ce;
      font-size: 14px;
      margin: 0 0 3% 0;
    }

    nav {
      text-align: right;
      padding: 4% 4% 0;
    }

    .singin-form {
      display: flex;
      flex-direction: column;
      justify-content: center;
      width: 100%;
      padding: 15% 18% 0 18%;
    }

    .singup-form {
      display: flex;
      flex-direction: column;
      justify-content: center;
      width: 100%;
      padding: 5% 18% 0 18%;
    }

  }

</style>
