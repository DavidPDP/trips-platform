<template>
  <v-dialog v-model="syncedDialog" width="500px">
    <v-card class="tour-guide-data">
      <h1>Formulario Para Guía</h1>
      <form class="tour-guide-form">
        <p>Complete la siguiente información con el propósito de generar confianza en sus potenciales clientes.</p>
        <v-textarea style="line-height: 1.3rem" wrap="hard" color="#5e60ce" v-model="guideForm.description" label="Info acerca de ti" rows="2" :placeholder="descriptionPlaceholder"></v-textarea>
        <v-text-field v-model="guideForm.identification" label="Cédula" required placeholder="114419145"></v-text-field>
        <v-text-field v-model="guideForm.email" label="Email" required placeholder="trip@outlook.com"></v-text-field>
        <v-text-field v-model="guideForm.address" label="Dirección" required placeholder="Cra 12 # 67-98, Cali-Colombia"></v-text-field>
        <v-text-field v-model="guideForm.telephone" label="Teléfono" required placeholder="3156997465"></v-text-field>
      </form>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="#5e60ce" text @click="submitGuideInfo()">Post</v-btn>
        <v-btn color="#5e60ce" text @click="syncedDialog = false">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">

  import { Component, Vue, PropSync } from 'vue-property-decorator';
  import { mapGetters } from 'vuex';
  import { TourGuide } from '../types/model';

  @Component
  export default class Home extends Vue {

    $auth: any;

    @PropSync('fillGuideForm', { type: Boolean }) syncedDialog!: boolean;

    guideForm = { description: '', identification: '', email:'', address: '', telephone: '' };
    descriptionPlaceholder = 'Disfruto mucho exponer a todos los implicados a\
    las vistas, los sonidos, los olores y la cultura...'

    submitGuideInfo() {

      let currentUser = this.$auth.$storage.getCookie('user');

      let guideInfo: TourGuide = { 
        user: currentUser.id, 
        description: this.guideForm.description,
        identification: parseInt(this.guideForm.identification),
        email: this.guideForm.email,
        address: this.guideForm.address,
        telephone: parseInt(this.guideForm.telephone) 
      };

      currentUser.tourguide = guideInfo;
      this.$auth.$storage.setCookie('user', currentUser, true);

      this.$store.dispatch('user/submitGuideInfo', guideInfo).then(() => {
        this.$emit("submitSuccessful", "Información Guardada!");
        this.syncedDialog = false;
      });

    }

  }

</script>

<style lang="scss" scoped>

  .tour-guide-data {
    
    @include container;

    h1{
      color: $text-color;
      background-color: $text-background;
      padding: 2% 0 2% 4%;
    }

    p{
      @include text--opaque;
    }

  }

  .tour-guide-form {

    @include small-container;

    .theme--light.v-input {
      @include container;
      font-size: 0.875rem;
    }

  }

</style>