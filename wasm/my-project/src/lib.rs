extern crate reqwest;

mod utils;

use wasm_bindgen::prelude::*;
use web_sys::{Document, Element, HtmlElement, Window, console};

    


// When the `wee_alloc` feature is enabled, use `wee_alloc` as the global
// allocator.
#[cfg(feature = "wee_alloc")]
#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

#[wasm_bindgen]
extern {
    fn alert(s: &str);
}

#[wasm_bindgen]
pub fn greet() {
    alert("Hello, my-project!");
    let body = reqwest::get("/suggestions/")
        .await?
        .text()
        .await?;
    console::log_1(&body.into());


}

// #[wasm_bindgen(start)]
// pub fn run(){
//     let window = web_sys::window().expect("should have a window in this context");
//     let document = window.document().expect("window should have a document");
// }