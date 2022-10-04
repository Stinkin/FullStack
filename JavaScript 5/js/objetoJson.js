//convertir de objeto a JSON

const user = {
    name: "Manz",
    life: 99,
    talk: function () {
      return "Hola!";
    },
  };
  
  JSON.stringify(user);       // '{"name":"Manz","life":99}'

  