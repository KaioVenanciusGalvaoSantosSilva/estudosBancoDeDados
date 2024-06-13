const products = [
    { id: 1, name: "Produto 1", price: 10.00, image: "https://via.placeholder.com/150" },
    { id: 2, name: "Produto 2", price: 20.00, image: "https://via.placeholder.com/150" },
    { id: 3, name: "Produto 3", price: 30.00, image: "https://via.placeholder.com/150" }
];

let cart = [];

function displayProducts() {
    const productList = document.getElementById('product-list');
    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('product');
        productDiv.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <div class="product-details">
                <h3>${product.name}</h3>
                <p>R$ ${product.price.toFixed(2)}</p>
                <button onclick="addToCart(${product.id})">Adicionar ao Carrinho</button>
            </div>
        `;
        productList.appendChild(productDiv);
    });
}

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    cart.push(product);
    updateCartCount();
    updateCartItems();
}

function updateCartCount() {
    const cartCount = document.getElementById('cart-count');
    cartCount.textContent = cart.length;
}

function updateCartItems() {
    const cartList = document.getElementById('cart-list');
    cartList.innerHTML = '';
    cart.forEach(item => {
        const listItem = document.createElement('li');
        listItem.textContent = `${item.name} - R$ ${item.price.toFixed(2)}`;
        cartList.appendChild(listItem);
    });
}

function toggleCart() {
    const cartItems = document.getElementById('cart-items');
    cartItems.classList.toggle('hidden');
}

function deleteAccount() {

    if (confirm("Tem certeza de que deseja excluir sua conta permanentemente? Esta ação não pode ser desfeita.")) {
        fetch('delete_account.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao excluir conta.');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert("Conta excluída com sucesso.");
                window.location.href = 'login.html';
            } else {
                alert("Erro ao excluir a conta.");
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert("Ocorreu um erro ao processar sua solicitação. Tente novamente mais tarde.");
        });
    }
}



function checkout() {
    alert('Compra finalizada com sucesso!');
    cart = [];
    updateCartCount();
    updateCartItems();
}

function toggleAccount() {
    const accountOptions = document.getElementById('account-options');
    accountOptions.classList.toggle('hidden');
}

window.onload = () => {
    displayProducts();
};

