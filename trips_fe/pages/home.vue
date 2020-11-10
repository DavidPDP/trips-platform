<template>
  <div class="home">
    <v-card color="rgb(255, 0, 0, 0)" max-width="700" class="mx-auto new-offer">
      <v-btn color="#5e60ce" class="white--text" @click="checkPermission()" block>Quieres agregar un nuevo destino?</v-btn>
    </v-card>
    <NewOfferDialog v-if="newOffer" :newOffer.sync="newOffer" />
    <TourGuideForm v-if="fillGuideForm" :fillGuideForm.sync="fillGuideForm" @submitSuccessful="switchNotification" />
    <div v-if="dataWaiting.trips && dataWaiting.bookings">
      <div v-for="trip in allTrips" :key="trip.id">
        <OfferItem :tripData="trip" /><br>
      </div>
    </div>
    <div class="update-info">
      <b>Te Encuentras Al Día</b>
      <p>Has visto todos los destinos nuevos.</p>
    </div>
    <v-snackbar v-model="notification" :timeout="2000">
      {{ notificationText }}
      <template v-slot:action="{ attrs }">
        <v-btn color="blue" text v-bind="attrs" @click="notification = false">Close</v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script lang="ts">
  
  import { Component, Vue } from 'vue-property-decorator';
  import { mapGetters } from 'vuex';

  const HomeProps = Vue.extend({
    middleware: [ 'auth' ],
    layout: 'app-tools',
    computed: { ...mapGetters({ allTrips: 'trips/allTrips' }) }
  });

  @Component
  export default class Home extends HomeProps {
    
    $auth: any;

    newOffer: boolean = false;
    fillGuideForm: boolean = false;
    notification: boolean = false;
    notificationText: string = '';
    dataWaiting = { trips: false, bookings: false };
    
    created() {
      this.$store.dispatch('trips/fetchTrips').then(() => {this.dataWaiting.trips = true});
      this.$store.dispatch('trips/fetchBookings').then(() => {this.dataWaiting.bookings = true});
      this.scroll();
    }

    scroll () {
      if(process.client) {
        window.onscroll = () => {
          let bottomOfWindow = Math.max(window.pageYOffset, document.documentElement.scrollTop, document.body.scrollTop) + window.innerHeight === document.documentElement.offsetHeight

          if (bottomOfWindow) {
            this.$store.dispatch('trips/fetchTrips');
            this.$store.dispatch('trips/fetchBookings');
          }

        }
      }
  	}

    async checkPermission(){
      let currentUser = this.$auth.$storage.getCookie('user');
      console.log(currentUser);
      if(currentUser.tourguide){
        this.newOffer = true;
      }else{
        this.fillGuideForm = true;
      }
    }

    switchNotification(text:string) {
      this.notificationText = text;
      this.notification = true;
    }

 
  };

</script>

<style lang="scss" scoped>

  .home {
    padding: 2% 0 0 0;
  }

  .new-offer {
    padding: 0 0 3% 0;
    box-shadow: none !important;
  }

  .update-info {
    @include container;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    b{
      margin-bottom: -0.5%;
      font-size: 150%;
    }
  }

</style>