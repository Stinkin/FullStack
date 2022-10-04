const user = {
    name: "Manz",
    life: 99,
    power: 10,
  };
  
  JSON.stringify(user, ["life"])              // '{"life":99}'
  JSON.stringify(user, ["name", "power"])     // '{"name":"Manz","power":10}'
  JSON.stringify(user, [])                    // '{}' (filtra todo)
  JSON.stringify(user, null)                  // '{"name":"Manz","life":99,"power":10}' (no filtra nada)