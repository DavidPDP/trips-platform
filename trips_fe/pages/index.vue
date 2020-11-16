<template>
  <div class="main-container">
    <section class="auth-sidebar">
      <h1>Adventure is worthwhile Feed your soul.</h1>
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
    navText: string = 'Not a member? ';
    navLinkText: string = 'Sign up now.';

    switchSignForm() {
      if (this.signInVisible) {
        this.navText = 'Already a member? ';
        this.navLinkText = 'Login now.';
        this.signInVisible = false;
      } else {
        this.navText = 'Not a member? ';
        this.navLinkText = 'Sign up now.';
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
    justify-content: center;
    text-align: center;

    h1 {
      color: #f8f8ff;
      padding: 10% 10% 2% 10%;
      font-family: Poppins;
      font-size: 30px;
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
