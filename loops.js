// loops

// for
// for in
// for of
// while
// do while
let nombres = ["Luis", "Miguel", "Juan"];

for(let i = 1; i <= 10; i++){
    console.log(i);
}

for(let i = 0; i < nombres.length; i++){
    console.log(nombres[i]);
}

for(let i in nombres){
    console.log(nombres[i])
}

for(let nombre of nombres){
    console.log(nombre);
}
