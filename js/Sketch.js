

// const circleNum = 100;
// const degree = 360 / circleNum;
// const spinNum =  4;


// initalize some variables
var xarr = [],
  yarr = [];
var boundRange, xSel, ySel;
var slidermax = 1000;



let p5;
let delegate;
let radius = 50;
let speed = 2;
const width=800;
const height=800;


// The whole p5 sketch is wrapped in this main function so that it works in nuxt.
// The p5 code is run  in instance mode so that variables don't clash. 
// see both:
// https://github.com/processing/p5.js/wiki/Global-and-instance-mode
// https://github.com/mitsuyacider/p5VueDemo
// https://medium.com/js-dojo/experiment-with-p5-js-on-vue-7ebc05030d33

export function main(_p5) {
  p5 = _p5


  // The p5 setup function; run once at startup
  p5.setup = _ => {
    var canvas = p5.createCanvas(width, height)
    canvas.parent("p5Canvas");
    // p5.background(100);
    // radius = 0;

    // generate random points
    for (let i = 0; i < 13800; i++) {
      let xx = p5.random(1);
      var x = p5.map(xx, 0, 1, 0, width)
      xarr.push(x);
      let yy = p5.random(1);
      var y = p5.map(yy, 0, 1, 0, height);
      yarr.push(y);
    }

    //the filter width
    boundRange = 20;

    //create a filter slider
    // slider = p5.createSlider(0, slidermax, 1000);
    // slider.position(10, 10);
    // slider.style('width', '80px');



  }


  // The p5 draw function that keeps refreshing
  p5.draw = _ => {


    var clr_lvl1 = p5.color(71, 149, 184);
    var clr_lvl2 = p5.color(25, 108, 158);
    var clr_lvl3 = p5.color(134, 191, 204);
    var clr_lvl4 = p5.color(221, 230, 232);
    var clr_lvl5 = p5.color(208, 241, 244);
    var clr_bg = p5.color(2, 73, 124);

    p5.background(clr_bg);
    p5.strokeWeight(1);
    p5.stroke(clr_lvl5);
    p5.line(mouseX, 0, mouseX, height);
    p5.line(0, mouseY, width, mouseY);

    // Add the slidervalue
    // let val = slider.value();
    // x_slider = p5.map(val, 0, slidermax, 0, width);


    // Draw the nodes
    for (let i = 0; i < 13800; i++) {

      // if ((mouseX < (xarr[i] + boundRange / 2)) && (mouseX > (xarr[i] - boundRange / 2)) ||
      //   (mouseY < (yarr[i] + boundRange / 2)) && (mouseY > (yarr[i] - boundRange / 2))) {
      //     p5.stroke(clr_lvl4);
      // } // Change the color}
      // // else if ((x_slider < (xarr[i] + boundRange / 2)) && (x_slider > (xarr[i] - boundRange / 2))) {
      // //   p5.stroke(clr_lvl3);
      // // }
      // else {
      //   p5.stroke(clr_lvl1);
      // }
      
      p5.stroke(clr_lvl1);
      p5.strokeWeight(2);
      p5.point(xarr[i], yarr[i]);
    }



    // p5.push();
    // p5.translate(p5.width / 2, p5.height / 2);
    // p5.noFill();
    // p5.stroke(255);
    // for (var i = 0, step = 0; i < 360 * spinNum; i+=degree, step+=1) {
    //   const angle = p5.radians(i);
    //   var x = (radius + step) * p5.cos(angle);
    //   var y = (radius + step) * p5.sin(angle);
    //   p5.stroke(255);
    // 	p5.rotate(1);
    //   p5.ellipse(x, y, 15, 15);
    //   var r = p5.map(i, 0, 360 * spinNum, 0, 255);
    //   var rand = p5.random(255);
    //   p5.stroke(r, rand, r, r);
    //   p5.line(0, 0, x, y);
    // }
    // p5.pop();
    // radius += speed;

    // if (radius > 360 || radius < -360 * 2 ) {
    // 	speed *= -1;
    // }








    // notifyCurrentTime();
  }
}



// part of callbacks
function notifyCurrentTime() {
  if (delegate !== undefined) {
    const message = p5.hour() + ":" + p5.minute() + ":" + p5.second();

    delegate(message);
  }
}


// part of callbacks
export function setDelegate(_delegate) {
  delegate = _delegate;
}
