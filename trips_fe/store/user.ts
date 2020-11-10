/**
 * @file user's session store / ES module
 * @module store/user
 * @author Johan Ballesteros <johan.ballesteros@outlook.com>
 */
import { Module, VuexModule, Mutation, Action } from 'vuex-module-decorators';

import { User, TripAPIError, TourGuide } from '@/types/model';
import TripBeAPI from '~/third_parties/trip_be_api';

@Module({ stateFactory: true, namespaced: true })
export default class UserStore extends VuexModule {

  $auth: any;

  get avatar() {
    return '/avatar-default.png';
  }

  @Action({ rawError: true })
  async signUp(user: User) {
    let userFetched = await TripBeAPI.signUp(user);
    if ((userFetched as TripAPIError).error === undefined) {
      return Promise.resolve();
    } else {
      return Promise.reject((userFetched as TripAPIError).error);
    }
  }

  @Action({ rawError: true })
  async submitGuideInfo(guide: TourGuide) {
    try {
      await TripBeAPI.submitGuide(guide);
      return Promise.resolve();
    }catch(error) {
      return Promise.reject();
    }
  }

};