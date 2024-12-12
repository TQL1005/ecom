var btnCart = document.getElementsByClassName("update-cart");
document.addEventListener("DOMContentLoaded", function () {
    // Ensure the function only executes when a button is clicked
    const postButton = document.getElementById("cart-click");

    if (postButton) {
        postButton.addEventListener("click", function () {
            order_itemPost();
        });
    }
});

function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getToken('csrftoken')


for (let index = 0; index < btnCart.length; index++) {
    btnCart[index].addEventListener("click", myFunc);
}
function myFunc(event) {
    var productId = event.target.getAttribute('data-product');
    var action = event.target.getAttribute('data-action');
    console.log("product " + productId + " action " + action);
    let x = 0;
    if (sessionStorage.getItem(productId)) {
        x = parseInt(sessionStorage.getItem(productId));
    } else {
        x = 0;
    }
    if (action) {
        x = x + 1;
    }
    sessionStorage.setItem(productId, x);
   
    
}

clickCount();

function clickCount() {
    // Select all elements with the "update-cart" class
    const cartButtons = document.getElementsByClassName("update-cart");

    // Loop through each button and attach an event listener
    for (let i = 0; i < cartButtons.length; i++) {
        cartButtons[i].addEventListener("click", function () {
            // Increment the click count in sessionStorage
            if (sessionStorage.clickcount) {
                sessionStorage.clickcount = Number(sessionStorage.clickcount) + 1;
            } else {
                sessionStorage.clickcount = 1;
            }

            // Update the cart total display
            var cartTotalElement = document.getElementById("cart-total");
            if (cartTotalElement) {
                cartTotalElement.innerHTML = sessionStorage.clickcount;
            }
        });
    }
    // Update the cart total display
    var cartTotalElement = document.getElementById("cart-total");
    if (typeof sessionStorage.clickcount !== 'undefined') {
        cartTotalElement.innerHTML = sessionStorage.clickcount;
    }else{
        cartTotalElement.innerHTML = "0";
    }
}


function getData() {
    let data = [];
    for (let index = 0; index < sessionStorage.length; index++) {
        let key = sessionStorage.key(index); // Get the key at the current index
        if (key !== 'clickcount') { // Exclude the 'clickcount' key
            let value = parseInt(sessionStorage.getItem(key)); // Get the value using the key
            if (!isNaN(value)) { // Ensure the value is a valid number
                data.push({
                    product: key,
                    quantity: value
                });
            }
        }
    }
    return data;
}


function order_itemPost() {
    var url = '/api/order_item';
    var data = getData();
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data)
    })
}

