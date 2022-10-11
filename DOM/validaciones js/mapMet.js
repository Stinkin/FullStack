const persona=[{
    id:0,
    nombre:"Lola",
    apellido:"Mora",
    edad:25
},
{
    id:1,
    nombre:"Juan",
    apellido:"Perez",
    edad:45
},
{
    id:2,
    nombre:"Mara",
    apellido:"Lopez",
    edad:33
},
{
    id:3,
    nombre:"Lucas",
    apellido:"Ramos",
    edad:55
},
]





persona.map(elemento=> {
    //renderiza codigo html 
    document.body.innerHTML +=
    `<ul>
    <li>
    Id:${elemento.id} <br>

    Nombre:${elemento.nombre}<br>
    Apellido:${elemento.apellido}<br>
    Edad:${elemento.edad}<br>
    </li>
    </ul>
    `
})