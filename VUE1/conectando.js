const { createApp } = Vue

  createApp({
    data() {
      return {
        mensaje: 'Hola Mundo con VUE',
        curso:'Codo a Codo'
      }
    }
  }).mount('#app')

