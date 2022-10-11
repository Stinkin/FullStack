//DOM

console.log(document.body)

let caja=document.createElement('div');
let caja2=document.createElement('div');

caja.style.width="200px";
caja.style.height="200px";
caja.style.background="green";


caja2.style.width="100px";
caja2.style.height="100px";
caja2.style.background="red";


document.body.append(caja,caja2)
