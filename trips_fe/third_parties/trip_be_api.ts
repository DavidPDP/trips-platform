import { NuxtAxiosInstance } from '@nuxtjs/axios';

import { User, TripAPIError, Trip, TourGuide, Booking } from '@/types/model';

class TripBeAPI {
  
  private $axios = <NuxtAxiosInstance>{};
  
  setAxiosClient(axios_client: NuxtAxiosInstance) {
    this.$axios = axios_client;
  };

  signUp(user: User): Promise<User|TripAPIError> {
    return this.$axios.$post('auth/signup', user);
  };

  getUser(username: string): Promise<User> {
    return this.$axios.$get('auth/user?username=' + username);
  }

  submitGuide(guide: TourGuide): Promise<void> {
    return this.$axios.$post('auth/tour_guide', guide);
  }

  createTrip(trip: Trip): Promise<void> {
    return this.$axios.$post('trips/', trip);
  };

  listTrips(lastTrip: number): Promise<Trip[]> {
    return this.$axios.$get('trips/list?last_trip=' + lastTrip);
  };

  createBooking(booking: Booking): Promise<void> {
    return this.$axios.$post('trips/booking', booking);
  };

  listBookings(): Promise<Booking[]> {
    return this.$axios.$get('trips/booking/list');
  };

  incrementLikes(trip_id: number): Promise<void> {
    return this.$axios.$post('trips/likes/increment', {trip_id: trip_id})
  };

  decrementLikes(trip_id: number): Promise<void> {
    return this.$axios.$post('trips/likes/decrement', {trip_id: trip_id})
  };

};

const task_processor = new TripBeAPI();

export default task_processor;