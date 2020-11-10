<template>
  <v-form class="singin-form">
    <h1><b>Welcome Back</b></h1>
    <h4>To keep connected with us please login with your personal info.</h4>
    <v-text-field v-model="currentUserData.username" color="#5e60ce" label="Username" prepend-inner-icon="mdi-account">
    </v-text-field>
    <v-text-field v-model="currentUserData.password" color="#5e60ce" class="input-group--focused" 
      prepend-inner-icon="mdi-lock" :append-icon="isPasswordVisible ? 'mdi-eye' : 'mdi-eye-off'"
      :rules="[rules.required]" :type="isPasswordVisible ? 'text' : 'password'"
      name="input-10-2" label="Password" hint="At least 8 characters"
      value="" @click:append="isPasswordVisible = !isPasswordVisible">
    </v-text-field>
    <v-btn color="#5e60ce" class="white--text" @click="trySignIn()">Sign In</v-btn>
    <label class="form__error-text" v-if="isSignInError">Username or password incorrect. Please try again.</label>
  </v-form>
</template>

<script lang="ts">

  import { Component, Vue } from 'vue-property-decorator';
  import { VueRouter } from 'vue-router/types/router';

  import { User } from '../types/model';
  import TripBeAPI from '../third_parties/trip_be_api';

  @Component
  export default class SignInForm extends Vue {
    
    $router: any;
    $auth: any;

    currentUserData: User = { username: '', password: '' };
    isPasswordVisible: boolean = false;
    isSignInError: boolean = false;
    rules = { required: (value:string) => !!value || 'Required.' };

    created() {
      if (this.$auth.$state.loggedIn) {
        this.$router.push('home');
      }
    }

    async trySignIn() {
      try{

        await this.$auth.loginWith('local', { data:this.currentUserData });
        let user = await TripBeAPI.getUser(this.currentUserData.username);
        this.currentUserData = { username:'', password:'' }; //clean sensitive data
        this.$auth.$storage.setCookie('user', user, true);
        this.$router.push('home');
        
      }catch(error){
        this.isSignInError = true;
      }

    }

  }

</script>

<style scoped>

  .form__error-text{
    color: rgb(255, 78, 78);
    padding: 2% 0 0 0;
  }

</style>