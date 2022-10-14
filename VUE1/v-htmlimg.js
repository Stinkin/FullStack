const { createApp } = Vue
createApp({
    data() {
        return {
           contenidoHtml: '<div><h2>Imagen de una rosa</h2></div>',
           imgsrc:"/css/img/rosa.jpg",
           imgalt:"Imagen de una Rosa"
        }
    }
}).mount('#ejemploimagen')
