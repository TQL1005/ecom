var btnCart = document.getElementsByClassName("update-cart");
let x = 0;
for (let index = 0; index < btnCart.length; index++) {
    btnCart[index].addEventListener("click", myFunc);
}
function myFunc(event) {
    var productId = event.target.getAttribute('data-product');
    var action = event.target.getAttribute('data-action');
    console.log("product " + productId + " action " + action);
    let x = 0;
    if (sessionStorage.getItem(productId)){
        x = parseInt(sessionStorage.getItem(productId));
    }else{
        x = 0;
    }
    if (action){
        x = x + 1; 
    }
    sessionStorage.setItem(productId,x);

    if (sessionStorage.clickcount) {
        sessionStorage.clickcount = Number(sessionStorage.clickcount) + 1;
        document.getElementById("cart-total").innerHTML = sessionStorage.clickcount
      } else {
        sessionStorage.clickcount = 1;
      }
}

