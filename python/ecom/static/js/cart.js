var btnCart = document.getElementsByClassName("update-cart");
for (let index = 0; index < btnCart.length; index++) {
    btnCart[index].addEventListener("click", myFunc);
}
function myFunc(event) {
    var productId = event.target.getAttribute('data-product');
    var action = event.target.getAttribute('data-action');
    console.log("product " + productId + " action " + action);
}