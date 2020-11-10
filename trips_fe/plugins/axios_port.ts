import '@nuxtjs/axios';
import { Plugin } from '@nuxt/types';

import TripBeAPI from '../third_parties/trip_be_api';

const axios_port: Plugin = (context) => {
  if(!context.$axios) {
    console.error( 'Please make sure $axios module is added' );
  }else{
    TripBeAPI.setAxiosClient(context.$axios);
  }
};

export default axios_port;