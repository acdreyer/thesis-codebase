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
              <selectorTwo />
          </el-col :span="12">
              <selectorThree />
          </el-col>
        </el-row>
<el-row>
            <el-col :span="24" class="selector-blocks" id="xaxis" style="margin:0px;padding:0px;">
              <br>
              <br>
              <br>
              <table style="width:100%;  margin:0px;padding:5px;">
                <td>
                  <th style="width:10%," title="Aerodynamics, is the study of motion of air, 
particularly as interaction with a solid object, 
such as an airplane wing.">Aerodynamics</th>
                  <th style="width:10%" title="The branch of science concerned with forces 
acting on or exerted by fluids (especially liquids).">Hydrodynamics</th>
                  <th style="width:10%" title="A propulsion system consists of a 
source of mechanical power.">Propulsion</th>
                  <th style="width:10%">Structures</th>
                  <th style="width:10%">Operating problems</th>
                  <th style="width:10%">Instruments</th>
                  <th style="width:10%">Research equipment</th>
                  <th style="width:10%">Indexes</th>
                  <th style="width:10%">Technical summaries</th>
                </td>
                </table>
          </el-col>
</el-row>
        <el-row>
          <el-col :span="24">





              <div class="parent">

              <img class="image1" src="../assets/scatter46_CB_2.png" />

<svg width="100%" height="160px" viewBox="0 0 500 200" class="svgover">
  <g transform:translate(500px,500px)>
                <!-- d="M 0 80 C 0 20, 160 20, 160 80 C 160 140, 0,140 0,80" -->
    <path id="curve" fill="transparent" stroke="transparent"
                d="M 25.0,100.0 A 75.0,75.0 0.0 1,1 175.0,100.0 A 75.0,75.0 0.0 1,1 25.0,100.0"
                style="transform:rotate(45);">
      
    </path>
    <text width="100%" style="transform:translate3d(0,0,0);" fill=white font-family=sans-serif id="titlerotate" >
        <textPath  alignment-baseline="top" startOffset="40" xlink:href="#curve">Flight Investigation of Boundary-Layer and Profile-Drag Characteristics of Smooth Wing Sections of a P-47D Airplane</textPath>
    </text>
    <circle class="marker" r="4" fill="white"></circle>
    <circle class="marker2" r="2" fill="white" startOffset="40"></circle>
    <circle class="marker3" r="6" fill="white" startOffset="80"></circle>
      </g>
</svg>




              <img class="image3" src="../assets/scatter117_RB.png" />
              <img class="image3" src="../assets/scatter258_ACR.png" />
              <img class="image3" src="../assets/scatter341_MR.png" />
              <img class="image2" src="../assets/scatter525_ARR.png" />
              <img class="image3" src="../assets/scatter1264_WR.png" />
              <img class="image3" src="../assets/scatter1444_TR.png" />
              <img class="image3" src="../assets/scatter4125_TN.png" />
              <img class="image3" src="../assets/scatter5164_RM.png" />

              <!--tooltip text-->
              <!-- <maingraph/> -->



              </div>
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
import selectorTwo from "~/components/selectorTwo.vue";
import selectorThree from "~/components/selectorThree.vue";
import maingraph from "~/components/maingraph.vue"
// import p5js from "~/static/p5.min.js";
// import p5dom from "~/static/p5.dom.min.js";
// import Vue from 'vue'; 
//https://github.com/Kinrany/vue-p5
//https://www.npmjs.com/package/vue-p5
// import VueP5 from 'vue-p5';
// import VueSession from 'vue-session';
// Vue.use(VueSession);
// Vue.use(VueP5);

import * as d3 from "d3";
import myJson from "~/static/naca_data.json";
console.log(myJson[0]);
// d3.select('.demo-container');

export default {
  name: "app",
  components: {
    Logo,
    selectorOne,
    selectorTwo,
    selectorThree,
    maingraph
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
  font-family:  "Akzidenz-grotesk-roman",sans-serif,'Cochin', Times, 'Times New Roman', serif ;
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

.main-image {
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

.parent {
  /* position: absolute; */
  top: 0;
  left: 0;
}
.image1 {
  position: relative;
  top: 0;
  left: 0;
    opacity: 1;
  filter: invert(100%); 
    text-align: center;
  display: block;
  width: 100%;
  height: auto;
}
.image2 {
  position: absolute;
  top: 0;
  left: 0;
    opacity: 0.6;
  filter: invert(100%); 
    text-align: center;
  display: block;
  width: 100%;
  height: auto;
  /* border: 1px green solid; */
}
.image3 {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
    opacity: 0.1;
  filter: invert(100%); 
    text-align: center;
  display: block;
  width: 100%;
  height: auto;
  /* border: 1px green solid; */
}
.svgover {
  position: absolute;
  top: 29.9%;
  left: 51.25%;
    text-align: center;
  display: block;
  width: 30%;
  height: auto;
  /* border: 1px green solid; */
}







.tooltiptext{
  fill: white;
  stroke: white;
  font-family: sans-serif;
}
  .marker {
  /*motion-path: path('M 5 5 m -4, 0 a 4,4 0 1,0 8,0 a 4,4 0 1,0 -8,0');*/
  /*offset-path: path('M 5 5 m -4, 0 a 4,4 0 1,0 8,0 a 4,4 0 1,0 -8,0');*/
  motion-path: path("M 100, 100 m -75, 0 a 75,75 0 1,0 150,0 a 75,75 0 1,0 -150,0");
  offset-path: path("M 100, 100 m -75, 0 a 75,75 0 1,0 150,0 a 75,75 0 1,0 -150,0");
  animation: move 3s linear infinite;
}
  .marker2 {
  /*motion-path: path('M 5 5 m -4, 0 a 4,4 0 1,0 8,0 a 4,4 0 1,0 -8,0');*/
  /*offset-path: path('M 5 5 m -4, 0 a 4,4 0 1,0 8,0 a 4,4 0 1,0 -8,0');*/
  motion-path: path("M 100, 100 m -75, 0 a 75,75 0 1,0 150,0 a 75,75 0 1,0 -150,0");
  offset-path: path("M 100, 100 m -75, 0 a 75,75 0 1,0 150,0 a 75,75 0 1,0 -150,0");
  animation: move 2s linear infinite;
}
  .marker3 {
  /*motion-path: path('M 5 5 m -4, 0 a 4,4 0 1,0 8,0 a 4,4 0 1,0 -8,0');*/
  /*offset-path: path('M 5 5 m -4, 0 a 4,4 0 1,0 8,0 a 4,4 0 1,0 -8,0');*/
  motion-path: path("M 25.0,100.0 A 75.0,75.0 0.0 1,1 175.0,100.0 A 75.0,75.0 0.0 1,1 25.0,100.0");
  offset-path: path("M 25.0,100.0 A 75.0,75.0 0.0 1,1 175.0,100.0 A 75.0,75.0 0.0 1,1 25.0,100.0");
  animation: move 4s linear infinite;
}


@keyframes move {
  100% { 
    motion-offset: 100%;
    offset-distance: 100%;
  }
}


#xaxis{
  font-family: "Arial" sans-serif;
  font-weight: normal;
  font-size: 0.7em;
}



/* #titlerotate{
    animation-name: ckw;
    /* animation-duration: 1s; */
    /* Things added */
    animation-iteration-count: infinite;
    transform-origin: 50% 50% ;
    /* display: inline-block; */
    /* <--- */
/* }
@keyframes ckw {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}  */



</style>
