/**
 * @file trips store / ES module
 * @module store/trips
 * @author Johan Ballesteros <johan.ballesteros@outlook.com>
 */
import { Module, VuexModule, Mutation, Action } from 'vuex-module-decorators';

import { Trip, Booking } from '@/types/model';
import TripBeAPI from '~/third_parties/trip_be_api';

@Module({ stateFactory: true, namespaced: true })
export default class TripsStore extends VuexModule {

  trips: Trip[] = [];
  bookings: Booking[] = [];

  get allTrips() {
    return [...this.trips].reverse();
  };

  get lastTripId() {
    let tripsSize = this.trips.length;
    if(tripsSize > 0){
      return this.trips[tripsSize - 1].id;
    }else{
      return 0;
    }
  };

  get allBookings() {
    return this.bookings;
  };

  @Mutation
  addTrip(trip: Trip) {
    this.trips.unshift(trip);
  };

  @Mutation
  updateTrips(trips: Trip[]) {
    this.trips = this.trips.concat(trips);
  };

  @Mutation
  updateBookings(bookings: Booking[]) {
    this.bookings = bookings;
  };

  @Action({ rawError: true })
  async submitTrip(trip:Trip) {
    await TripBeAPI.createTrip(trip);
    this.context.dispatch('fetchTrips');
  };

  @Action({ rawError: true })
  async fetchTrips() {
    let lastTripIndex = this.context.getters['lastTripId'];
    let trips = await TripBeAPI.listTrips(lastTripIndex);
    this.context.commit('updateTrips', trips);
  };

  @Action({ rawError: true })
  async submitBooking(booking: Booking) {
    await TripBeAPI.createBooking(booking);
  };

  @Action({ rawError: true })
  async fetchBookings(){
    let bookings = await TripBeAPI.listBookings();
    this.context.commit('updateBookings', bookings);
  };

  @Action({ rawError: true })
  async incrementLikes(trip_id: number) {
    TripBeAPI.incrementLikes(trip_id);
  };

  @Action({ rawError: true })
  async decrementLikes(trip_id: number) {
    TripBeAPI.decrementLikes(trip_id);
  };

};