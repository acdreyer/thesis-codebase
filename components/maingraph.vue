<template>
  <div class="container border">
    <div class="d-flex justify-content-center" id="p5Canvas"></div>
    <div class="message d-flex justify-content-center">
      {{message}}
    </div>
  </div>
</template>


// p5 in nuxt from https://github.com/mitsuyacider/p5VueDemo
<script>
if (process.browser) {
  var sketch = require('@/js/Sketch.js')
}
export default {
  data() {
    return {
      message: ""
    }
  },
  mounted() {
    const P5 = require('p5')
    new P5(sketch.main)
    // NOTE: p5.js Receive a callback from
    sketch.setDelegate(this.callbackOnP5);
  },
  methods: {
    callbackOnP5: function(timeStr) {
      this.message = timeStr;
    }
  }
}
</script>

<style>
.message {
  color: black;
}
</style>