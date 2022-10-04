const user = {
    name: "Manz",
    life: 99
  };
  
  const json2 = JSON.stringify(user, null, 2);
  console.log(json2);
  // {
  //   "name": "Manz",
  //   "life": 99
  // }
  
  const json4 = JSON.stringify(user, null, 4);
  console.log(json4);
  // {
  //     "name": "Manz",
  //     "life": 99
  // }
  
  const json1 = JSON.stringify(user, ["name"], 1);
  console.log(json1);
  // {
  //  "name": "Manz"
  // }