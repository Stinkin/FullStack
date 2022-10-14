const { createApp } = Vue

  createApp({
    data() {
      return {
        nombre:'Lola',
        apellido:'Mora',
        direccion:'San Juan 100',
        nombreCompleto:'',
        error:''
      }
    },
  
    methods:{
        detalles(){
            return "Soy " + this.nombre + " " + this.apellido + " y vivo " + this.direccion
        },
      
    verificarNombreCompleto(){
      if(this.nombreCompleto.length < 4){
        this.error='El nombre no es valido'
      }else{
             this.error= ' '
      }
    }
    },
  }).mount('#ejemplo')
