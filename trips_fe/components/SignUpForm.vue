<template>
  <v-form class="singup-form">
    <h1><b>Sign Up</b></h1>
    <h4>It's quick and easy.</h4>
    <v-text-field v-model="currentUserData.username" color="#5e60ce" label="Username" prepend-inner-icon="mdi-account"></v-text-field>
    <v-text-field v-model="currentUserData.email" color="#5e60ce" label="Email" prepend-inner-icon="mdi-account"></v-text-field>
    <v-text-field v-model="currentUserData.password" color="#5e60ce" class="input-group--focused" 
      prepend-inner-icon="mdi-lock" :append-icon="isPasswordVisible ? 'mdi-eye' : 'mdi-eye-off'"
      :rules="[rules.required]" :type="isPasswordVisible ? 'text' : 'password'"
      name="input-10-2" label="Password" hint="At least 8 characters"
      value="" @click:append="isPasswordVisible = !isPasswordVisible">
    </v-text-field>
    <v-text-field v-model="passwordRepeat" color="#5e60ce" class="input-group--focused" 
      prepend-inner-icon="mdi-lock" :append-icon="isPasswordVisible ? 'mdi-eye' : 'mdi-eye-off'"
      :rules="[rules.required]" :type="isPasswordVisible ? 'text' : 'password'"
      name="input-10-2" label="Repeat Password" hint="At least 8 characters"
      value="" @click:append="isPasswordVisible = !isPasswordVisible">
    </v-text-field>
    <v-btn @click="trySignUp()" color="#5e60ce" class="white--text">Create Account</v-btn>
    <label class="form__error-text" v-if="isSignInError">{{ signInError }}</label>
  </v-form>
</template>

<script lang="ts">

  import { Component, Vue, PropSync } from 'vue-property-decorator';
  import { VueRouter } from 'vue-router/types/router';

  import { User } from '../types/model';

  @Component
  export default class SignInForm extends Vue {

    @PropSync('signInVisible', { type: Boolean }) signInAlert!: boolean;
    @PropSync('notification', { type: Boolean }) signInNotification!: boolean;

    currentUserData: User = { username: '', password: '', email: '' };
    passwordRepeat: string = '';
    isPasswordVisible: boolean = false;
    isSignInError: boolean = false;
    signInError: string = '';
    rules = {
      required: (value: string) => !!value || 'Required.',
      emailMatch: () => ('The email and password you entered don\'t match'),
    };

    trySignUp() {
      if(this.currentUserData.password !== this.passwordRepeat) {
        this.signInError = 'Passwords do not match. Please verify.';
        this.isSignInError = true;
      } else {
        this.$store.dispatch('user/signUp', this.currentUserData).then(() => {
          this.$emit("signSuccessful", "User created!");
        }).catch((error:string) => {
          this.signInError = error;
          this.isSignInError = true;
        });
      }
    }

  }

</script>