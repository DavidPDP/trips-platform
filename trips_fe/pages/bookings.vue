<template>
  <div class="home">
    <v-card color="rgb(255, 0, 0, 0)" max-width="700" class="mx-auto bookings">
      <v-btn color="#5e60ce" class="white--text" block>Mis Reservas</v-btn>
    </v-card>
    <div v-for="booking in allBookings" :key="booking.id">
      <OfferItem :tripData="booking.trip" /><br>
    </div>
  </div>
</template>

<script lang="ts">
  
  import { Component, Vue } from 'vue-property-decorator';
  import { mapGetters } from 'vuex';

  const HomeProps = Vue.extend({
    middleware: [ 'auth' ],
    layout: 'app-tools',
    computed: { ...mapGetters({ allBookings: 'trips/allBookings' }) }
  });

  @Component
  export default class Home extends HomeProps {
    
    $auth: any;

    newOffer: boolean = false;
    fillGuideForm: boolean = false;
    notification: boolean = false;
    notificationText: string = '';
    
    mounted() {
      this.$store.dispatch('trips/fetchBookings');
    }
 
  };

</script>

<style lang="scss" scoped>

  .home {
    padding: 2% 0 0 0;
  }

  .bookings {
    padding: 0 0 3% 0;
    box-shadow: none !important;
    pointer-events: none;
  }

</style>