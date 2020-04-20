<template>
  <div id="app" class="bg-black">
    <el-container class="over-all">
      <!-- <el-header>
      </el-header>-->
      <!-- <div class="toptitle-container"> -->

      <el-main>
        <el-row>
          <el-col :span="24">
            <div class="grid-content bg-black" id="title-main">FROM NACA TO NASA</div>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24" class="bg-black">
            <div class="grid-content bg-black" id="title-sub">
              Research at The National Advisory Committe for Aeronautics
              that made it the National Aeronautics and Space Administration
            </div>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24" class="bg-black">
            <el-col :span="12">
              <div
                class="grid-content top-description"
              >During World War I aircraft technology was in its infancy and it prompted the United States to establish the National Advisory Committee for Aeronautics (NACA) in 1915. Subsequently great advances were made by scientists and aviators and NACA advanced commercial and military aviation through research and development activities. By the time World War II broke out, NACA was well established as a leading aerospace research institution.</div>
            </el-col>

            <el-col :span="12">
              <div class="grid-content top-description">
                The NACA’s research made it the obvious choice for the US Congress when the space race began in earnest. The NACA agency’s operational research model was ideal for advancing development from aerospace to space and in 1958 the National Aeronautics and Space Administration (NASA) was created, making the NACA the core of NASA.
                <!-- <logo /> -->
              </div>
            </el-col>
          </el-col>
        </el-row>
      </el-main>

      <el-main class="bg-black-blue ">
        <el-row>
          <el-col :span="6" class="selector-blocks">
              <selectorOne />
          </el-col>
          <el-col :span="6" class="selector-blocks">
              <selectorOne />
          </el-col>
              <!-- <selectorOne /> -->
          </el-col>
        </el-row>

        <el-row>
          <el-col :span="24">

              <img id="main-image" src="../assets/test3png.png" />

          </el-col>
        </el-row>
      </el-main>

      <!-- <el-main>
        <div class="demo-container"></div>

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
      </el-main> -->

      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>



<script>
// import 'element-ui/lib/theme-default/myStyles.css';
import akzidenz from "~/assets/Akzidenz-grotesk-roman.ttf"
import akzidenzl from "~/assets/Akzidenz-grotesk-light.ttf"
import Logo from "~/components/Logo.vue";
import selectorOne from "~/components/selectorOne.vue";
import * as d3 from "d3";
import myJson from "~/static/naca_data.json";
console.log(myJson[0]);
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
    d3.csv("testplot.csv", data => {
      // console.log(data)
      this.myArr = data.columns;
    });
  }
};
</script>











<style scoped>

.over-all{
  max-width: 1000px;
  margin: auto;
  /* display: block; */
  /* text-align: center; */
}
.toptitle-container {
  margin: 0 auto;
  /* min-height: 100vh; */
  display: block;
  justify-content: center;
  /* align-items: center; */
  /* text-align: center; */
}

#title-main {
  font-family: "Akzidenz-grotesk-light",;
  text-align: center;
  display: block;
  font-weight: 300;
    font-size: 3.2em;
  color: #ddd;
  letter-spacing: 1px;
}

#title-sub {
  font-family: "Courier";

  font-size: 1.3em;
  font-weight: medium;
  color: rgb(182, 194, 218);
  /* word-spacing: 5px; */
  text-align: center;
  text-justify: inter-word;
  /* padding-top: 10px;
  padding-left: 10px;
  padding-right: 10px; */
  padding: 10px;
}

.top-description {
  font-family: Roboto, sans-serif ;
  text-align: justify;
  opacity: 0.8;
  height: auto;
  padding: 10px;
  font-size: 0.85em;
}

#main-image {
  opacity: 0.9;
  filter: invert(100%); 
  text-align: center;
  display: block;
  width: 100%;
  height: auto;
}

@font-face {
  font-family: Akzidenz-grotesk-light;
  src: akzidenzl;
}

.filters-block{
  padding: 5px;
}
.selector-blocks{
  display: inline-block;
  padding-left: 10px;
  padding-right: 10px;
}

.links {
  padding-top: 15px;
}
</style>
