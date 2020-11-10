<template>
  <div class="like-btn">
    <div :class="['heart', { 'is-active': toggled }]" @click="like()"></div>
    <b>{{likesFacade}} personas lo desean.</b>
  </div>
</template>

<script lang="ts">
  
  import { Component, Vue, Prop } from 'vue-property-decorator';

  @Component
  export default class LikeButton extends Vue {

    @Prop(Number) readonly likes!: number;
    @Prop(Number) readonly tripId!: number;

    likesFacade = this.likes;
    toggled = false;

    like() {
      this.toggled = !this.toggled;
      if (this.toggled) {
        this.incrementLikes();
      }else{
        this.decrementLikes();
      }
    }

    incrementLikes() {
      this.likesFacade ++;
      this.$store.dispatch('trips/incrementLikes', this.tripId);
    }

    decrementLikes() {
      this.likesFacade --;
      this.$store.dispatch('trips/decrementLikes', this.tripId);
    }

  }

</script>

<style lang="scss" scoped>
  
  .like-btn {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .heart {
    width: 100px;
    height: 100px;
    margin: -15% -10% -15% -8%;
    background: url("https://cssanimation.rocks/images/posts/steps/heart.png") no-repeat;
    background-position: 0 0;
    cursor: pointer;
    transition: background-position 1s steps(28);
    transition-duration: 0s;
    
    &.is-active {
      transition-duration: 1s;
      background-position: -2800px 0;
    }
  }

</style>
