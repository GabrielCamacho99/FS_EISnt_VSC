/* 
Método Sincrono

fetch("https://jsonplaceholder.typicode.com/users/")
    .then(res => res.json())
    .then(data => {
        console.log(data.name);
        console.log(data.address.city);

    }); */

    // Método Assincrono

    async function getUser() {
        const res = await fetch("https://jsonplaceholder.typicode.com/users/1")
        const data = await res.json();

        console.log(data.name);
    }

    getUser();