<template>
  <v-card outlined elevation="2" max-width="700" class="mx-auto">
    <div class="offer-item__header">
      <v-avatar>
        <img :src="avatar">
      </v-avatar>
      <div class="offer-item__header__info">
        <b>{{ tripData.user.username }}</b>
        <p>{{ tripData.match }}% de afinidad | {{ tripData.date }} | {{ tripData.long_days }} día(s)</p>
      </div>
    </div>
    <div>
      <div class="offer-item__multimedia">
        <div class="offer-item__price">
          <v-icon medium color="#6930c3" class="mr-2"> mdi-currency-usd </v-icon>
          <label>{{ tripData.price }} COP</label>
        </div>
        <div>
          <v-icon medium color="#6930c3" class="mr-2" @click="switchInfoPanel('guide-data')"> mdi-information-outline </v-icon>
          <v-icon medium color="#6930c3" class="mr-2" @click="switchInfoPanel('location-data')"> mdi-google-maps </v-icon>
          <v-icon medium color="#6930c3" class="mr-2" @click="switchInfoPanel('pictures')"> mdi-camera </v-icon>
        </div>
      </div>
      <div v-if="infoPanel === 'guide-data'" class="offer-item__info-panel">
        <div>
          <h2>Acerca del guía</h2>
          <p>{{ tripData.user.tourguide.description }}</p>
        </div>
        <h2>Datos</h2>
        <div class="offer-item__info-panel__data">
          <p><b>Cédula: </b>{{ tripData.user.tourguide.identification }}</p>
          <p><b>Email: </b>{{ tripData.user.tourguide.email }}</p>
          <p><b>Dirección: </b>{{ tripData.user.tourguide.address }}</p>
          <p><b>Teléfono: </b>{{ tripData.user.tourguide.telephone }}</p>
        </div>
      </div>
      <div v-else-if="infoPanel === 'location-data'" class="offer-item__location">
        <h1>{{ tripData.location }}</h1>
      </div>
      <v-carousel v-else-if="infoPanel === 'pictures'" hide-delimiters height="250">
        <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src"></v-carousel-item>
      </v-carousel>
    </div>
    <div class="offer-item__actions">
      <LikeBtn :likes="tripData.likes" :tripId="tripData.id" />
      <v-btn color="#5e60ce" class="white--text" :disabled="isBooking" @click="booking()">{{ bookingText }}</v-btn>
    </div>
    <v-card-text style="text-align: justify; text-justify: inter-word;">
      <b>Info:</b>
      {{ tripData.description }}
    </v-card-text>
  </v-card>
</template>

<script lang="ts">

  import { Component, Vue, PropSync, Prop } from 'vue-property-decorator';

  import { Trip, Booking } from '../types/model';

  @Component
  export default class Home extends Vue {
    
    $auth: any;

    @Prop(Object) readonly tripData!: Trip;

    avatar = this.$store.getters['user/avatar'];
    infoPanel = 'pictures';
    bookingText = 'Reservar';
    isBooking = false;
    items = [ {src: '/trip-default-picture.jpg'} ];

    mounted() {
      this.checkBooking();
    };

    checkBooking() {

      let currentUser = this.$auth.$storage.getCookie('user');
      let searchedBooking = {trip_id: this.tripData.id, user: currentUser.id};

      let bookings = this.$store.getters['trips/allBookings'];

      if(bookings.filter((booking: Booking) => {

          if (booking.trip) {
            return Number(booking.trip.id) === Number(searchedBooking.trip_id) &&
              Number(booking.user) === Number(searchedBooking.user);
          }

      }).length > 0){
        this.bookingText = 'Reservado';
        this.isBooking = true;
      } else {
        this.bookingText = 'Reservar';
        this.isBooking = false;
      }

    }

    switchInfoPanel(panel: string) {
      this.infoPanel = panel;
    };

    booking() {

      let currentUser = this.$auth.$storage.getCookie('user');

      let booking: Booking = {
        trip_id: this.tripData.id,
        user: currentUser.id
      };

      this.$store.dispatch('trips/submitBooking', booking);
      this.bookingText = 'Reservado';
      this.isBooking = true;

    };

  }

</script>

<style lang="scss" scoped>

  .offer-item__header {
    display: flex;
    flex-direction: row;
    padding: 2% 2% 0 2%;

    p{
      @include text--opaque;
    }

    .offer-item__header__info {
      display: flex;
      flex-direction: column;
      padding: 0 0 0 2%
    }

  }

  .offer-item__actions {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 2% 2% 0 0;
    align-items: center;
  }

  .offer-item__multimedia {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0 0 1% 0;

    label {
      @include text--opaque;
    }

    .offer-item__price {
      padding: 0 0 0 2%;
      
      label {
        margin: 0 0 0 -10%;
      }
    }

  }

  .offer-item__info-panel {
    background-color: #0077b6;
    height: 250px;
    color: $text-color;
    @include small-container;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    font-size: 0.875rem;
    overflow-x:none; 
    overflow-y:auto;

    .offer-item__info-panel__data {
      line-height: 1rem;
    }

  }

  .offer-item__location {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 250px;
    width: auto;
    background-color: #0077b6;
    color: $text-color;
  }

</style>