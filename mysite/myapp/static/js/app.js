
//Adapted from https://rustwasm.github.io/docs/wasm-bindgen/examples/without-a-bundler.html
import init, { greet } from '/static/js/my_project.js';

async function run() {
    
    await init();
    var t1 = performance.now();
    greet();
    var t2 = performance.now();
    console.log(t2-t1);
    var t1 = performance.now();
    alert("HI");
    var t2 = performance.now();
    console.log(t2-t1);
}

run();