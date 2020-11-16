<template>
  <v-dialog v-model="syncedDialog" width="500px">
    <v-card class="new-offer">
      <h1>New Offer</h1>
      <div class="new-offer__content">
        <div class="new-offer__header">
          <v-avatar>
            <img :src="avatar">
          </v-avatar>
          <b>{{ currentUser.username }}</b>
        </div><br>
        <form class="new-offer_description">
          <v-textarea color="#5e60ce" v-model="tripData.description" autocomplete="email" label="Enter your trip information" rows="2" :placeholder="infoPlaceholder"></v-textarea>
          <v-row>
            <v-col>
              <v-text-field color="#5e60ce" type="number" v-model="tripData.price" label="Price" prefix="$" placeholder="1500000"></v-text-field>
            </v-col>
            <v-col>
              <v-text-field color="#5e60ce" type="number" v-model="tripData.long_days" label="Long" suffix="days" placeholder="5"></v-text-field>
            </v-col>
            <v-col>
              <v-text-field color="#5e60ce" v-model="tripData.location" label="Location" append-icon="mdi-map-marker" placeholder="Perú"></v-text-field>
            </v-col>
          </v-row>
        </form>
      </div>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="#5e60ce" text @click="postTrip()">Post</v-btn>
        <v-btn color="#5e60ce" text @click="syncedDialog = false;">Cancel</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">

  import { Component, Vue, PropSync } from 'vue-property-decorator';
  import { mapGetters } from 'vuex';
  import { Trip } from '../types/model';

  @Component
  export default class Home extends Vue {

    $auth: any;

    @PropSync('newOffer', { type: Boolean }) syncedDialog!: boolean;

    avatar = this.$store.getters['user/avatar'];
    tripData = {
      description: '', price: '', headerDescription: '', 
      long_days: '', location: ''
    };
    infoPlaceholder = 'La idea de viajar a una de las 7 maravillas del\
    mundo hará que la piel se te erice, los viajes a Machu Picchu crean\
    una satisfacción indescriptible...';

    get currentUser() {
      return this.$auth.$storage.getCookie('user');
    }

    postTrip() {

      let trip : Trip = {
        user_id: this.currentUser.id,
        description: this.tripData.description,
        price: parseFloat(this.tripData.price),
        match: Math.trunc(Math.random() * (99 - 70) + 70),
        long_days: parseInt(this.tripData.long_days),
        location: this.tripData.location,
        date: new Date(),
        likes: 0
      };

      this.$store.dispatch('trips/submitTrip', trip);

      this.syncedDialog = false;
      
    }

  };

</script>

<style lang="scss" scoped>

  .new-offer {

    h1{
      color: $text-color;
      background-color: $text-background;
      padding: 2% 0 2% 4%;
    }

    .new-offer__content{
      @include small-container;

      .new-offer__header {
        display: flex;
        flex-direction: row;
        align-items: center;

        b{
          padding: 0 0 0 1%;
        }

      }

      .new-offer_description {
        
        .theme--light.v-input {
          @include container;
          font-size: 0.875rem;
        }

        textarea {
          width: 100%;
          padding: 0 1% 0 1%;
        }

        .new-offer_attrs{
          display: flex;
          flex-direction: row;
        }

      }

      .new-offerr_image-viewer {
        display: flex;
        flex-direction: row;
        padding: 0 1% 0 1%;
        width: 100%;
        flex-flow: row wrap;
        justify-content: center;
      }

    }

  }

</style>
