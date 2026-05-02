console.log("Ola monguitos");
//print ("Ola monguitos") --- IGNORE ---

// VARIAVEIS JS

let idade = 25; //VARIAVEL MUTAVEL
const pi = 3.14; // VARIAVEL IMUTAVEL

//CONDIÇOES E LOOPS

let idade2 = 18;

if (idade2 >= 18) {
    console.log("Adulto");
} else {
    console.log("Menor");
}

for (let i = 0; i < 5; i++) {
    console.log
}

// OBJECTOS

let user = {
    nome: "Bruno",
    idade: 30
};

console.log(user.nome);


// js com APIs

//Método Sincrono
fetch("https://jsonplaceholder.typicode.com/users/")
    .then(res => res.json())
    .then(data => {
        console.log(data.name);
        console.log(data.address.city);

    });

// Método Assincrono

async function getUser() {
    const res = await fetch("https://jsonplaceholder.typicode.com/users/1")
    const data = await res.json();

    console.log(data.name);
}

getUser();

//CONSTRUÇAO API EM PY

res = requests.get(url)
dados = res.json()

//CONSTRUÇAO API em JS

const res = await fetch(url);
const dados = await res.json();

/*
escolher cada um de acordo com o que se está a trabalhar

Python:
    dados
    automação
    ficheiros


JavaScript:
    web 
    APIs
    integração frontend/backend

Combinar ambos também é possível

*/