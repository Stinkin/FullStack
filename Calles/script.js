function fetchData(y) {
  fetch(y)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      let output = '<h2">Direcciones</h2>';

      if (data.direccionesNormalizadas.length == 0) {
        output = data.errorMessage;
      } else {
        data.direccionesNormalizadas.forEach((item) => {
          output += `
           <ul>
           <li> ${item.direccion}</li>
           <li> ${item.coordenadas.x}</li>
           <li> ${item.coordenadas.y}</li>           
           </ul>
        `;
        });
      }
      document.getElementById("resultados").innerHTML = output;
    })
    .catch((error) => {
      console.log(`Error Fetching data : ${error}`);
      document.getElementById("resultados").innerHTML = "Error de Conexion";
    });
}

function myFunction() {
  var x = document.getElementById("dire").value;
  let y = "http://servicios.usig.buenosaires.gob.ar/normalizar/?direccion=" + x+"&geocodificar=TRUE";
  console.log(y);
  fetchData(y);
}
