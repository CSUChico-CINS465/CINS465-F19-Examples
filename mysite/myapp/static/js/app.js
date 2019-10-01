
//Adapted from https://rustwasm.github.io/docs/wasm-bindgen/examples/without-a-bundler.html
import init, { greet } from '/static/js/my_project.js';

async function run() {
    
    await init();
    greet();
}

run();