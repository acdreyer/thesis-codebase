<template>
  <div id="app">
    <el-container>
      <el-header>
        <!-- <div class="toptitle-container"> -->
        <el-row>
          <el-col :span="24">
            <div class="grid-content bg-purple-dark" id="title-main">FROM NACA TO NASA</div>
            <div class="grid-content bg-purple-dark" id="title-sub">
              Research at The National Advisory Committe for Aeronautics
              that made it become the National Aeronautics and Space Administration
            </div>
          </el-col>
        </el-row>
      </el-header>

      <el-main>
        <el-row>
          <el-col :span="12">
            <div class="grid-content bg-purple">
              During World War I aircraft technology was in its infancy and it prompted the United States to establish the National Advisory Committee for Aeronautics (NACA) in 1915. Subsequently great advances were made by scientists and aviators and NACA advanced commercial and military aviation through research and development activities. By the time World War II broke out, NACA was well established as a leading aerospace research institution.
              The NACA’s research made it the obvious choice for the US Congress when the space race began in earnest. The NACA agency’s operational research model was ideal for advancing development from aerospace to space and in 1958 the National Aeronautics and Space Administration (NASA) was created, making the NACA the core of NASA.
            </div>
          </el-col>

          <el-col :span="12">
            <div class="grid-content bg-purple-light">
              <logo />
            </div>
          </el-col>
        </el-row>
      </el-main>

      <el-main>
        <el-row>
          <el-col :span="24">
           <selectorOne />
          <!-- <selectorOne /> -->
          </el-col>
        </el-row>
      </el-main>

      <el-main>
        <div class="demo-container"></div>

        <div class="block">
          <el-row>
            <img src="../assets/test2png.png" />
          </el-row>
        </div>

        <el-row>
          <div class="grid-content bg-purple-dark">
            <h1 class="title">antonie-thesis</h1>
            <h2 class="subtitle">Thesis nuxt intro</h2>
            <div class="links">
              <a href="https://nuxtjs.org/" target="_blank" class="button--green">Documentation</a>
              <a href="https://github.com/nuxt/nuxt.js" target="_blank" class="button--grey">GitHub</a>
            </div>
            <logo />
          </div>
        </el-row>
      </el-main>

      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>



<script>
// import 'element-ui/lib/theme-default/myStyles.css';
import Logo from "~/components/Logo.vue";
import selectorOne from "~/components/selectorOne.vue";
import * as d3 from "d3";
import myJson from "~/static/naca_data.json"
console.log(myJson[0])
// d3.select('.demo-container');

export default {
  name: "app",
  components: {
    Logo,
    selectorOne
  },
  data() {
  	return {
      myArr: [],
      myJson
    };
  },
  mounted() {
    d3.csv('testplot.csv', (data) => {
      // console.log(data)
      this.myArr = data.columns;
    })

  }
};
</script>











<style>
.toptitle-container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
