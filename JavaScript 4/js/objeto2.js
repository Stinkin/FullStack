//objeto literal

let persona = {
    //clave/valor separado por coma
    //nombre[0]='Lola', nombre[1]='Mora'
    //arreglo de 2 elementos
    nombre: ['Lola' , 'Mora'],
    edad: 52,
    genero: 'Femenino',
    intereses: ['música' , 'voley'],

    //metodos del objeto
    bio: function () {            
      alert(this.nombre[0] + '' + this.nombre[1] + ' tiene ' + this.edad + ' años. Le gusta ' + this.intereses[0] + ' y ' + this.intereses[1] + '.');
    },
    saludo: function() {
      alert('Hola, Soy '+ this.nombre[0] + '. ');
    }
  };

persona.nombre 
persona.nombre[0]
persona.edad
persona.intereses[1]
persona.bio()
persona.saludo()

//crear nuevos miembros
persona['ojos'] = 'avellana';
persona.despedida = function() { alert("¡Adiós a todos!"); }

persona['ojos']
persona.despedida()