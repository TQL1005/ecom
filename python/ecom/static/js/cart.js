var btnCart = document.getElementsByClassName("update-cart");

document.addEventListener("DOMContentLoaded", function () {
    // Ensure the function only executes when a button is clicked
    for (var i = 0; i < btnCart.length; i++) {
        if (btnCart[i]) {
            btnCart[i].addEventListener("click", myFunc);
        }
    }
});

function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getToken('csrftoken');

function myFunc(event) {
    var productId = event.target.getAttribute('data-product');
    var action = event.target.getAttribute('data-action');
    console.log("product " + productId + " action " + action);
    let x = sessionStorage.getItem(productId) ? parseInt(sessionStorage.getItem(productId)) : 0;

    if (action) {
        x += 1;
    }
    let total = 0;
    var count = document.getElementById("cart-total");
    total = parseInt(count.innerHTML) + 1; 
    count.innerHTML=total;
    sessionStorage.setItem(productId, x);

    
    fetch_data_order_item_all().then(order_item_all => {
        console.log("Extracted Data:", order_item_all);

        // Iterate through the resolved data
        const productExists = order_item_all.some(item => item.product === parseInt(productId));

        if (productExists) {
            order_itemUpdate();  // Product exists, update it
        } else {
            order_itemPush();  // Product does not exist, push it
        }
    }).catch(error => {
        console.error("Error fetching data:", error);
    });
    
    }

    async function fetch_data_order_item_all() {
        const response = await fetch('/api/order_item');
        const data = await response.json();
        return data['items'];
    }

async function fetch_data_order_item() {
    const response = await fetch('/api/order_item');
    const data = await response.json();
    return data['total_quantity'] || 0;  // Default to 0 if undefined
}

async function updateCartTotal() {
    const total = await fetch_data_order_item();
    const cartTotalElement = document.getElementById("cart-total");
    cartTotalElement.innerHTML = total;
}

document.addEventListener("DOMContentLoaded", updateCartTotal);

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

async function order_itemUpdate() {
    const url = '/api/order_item_update';
    const data = getData();
    const response = await fetch(url, {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data)
    });
    sessionStorage.clear();  // Optional: Clear the session storage after posting
}


async function order_itemPush() {
    const url = '/api/order_item';
    const data = getData();
    const response = await fetch(url, {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data)
    });
    sessionStorage.clear();  // Optional: Clear the session storage after posting
}
