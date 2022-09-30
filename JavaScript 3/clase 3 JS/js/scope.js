var a = 5
var b = 10
if (a === 5) {
  let a = 4 // El alcance es dentro del bloque if
  var b = 15 // El alcance es global, sobreescribe a 10
  console.log(a)  // 4, por alcance a nivel de bloque
  console.log(b)  // 15, por alcance global
}
console.log(a) // 5, por alcance global
console.log(b) // 15, por alcance global