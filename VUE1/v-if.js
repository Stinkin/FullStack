const { createApp } = Vue
createApp({
    data() {
        return {
            frutas: [
                {nombre:"naranja", cantidad: 10},
                {nombre:"banana", cantidad: 0},
                {nombre:"durazno", cantidad: 3},
                {nombre:"pera", cantidad: 0}
            ]
        }
    }
}).mount('#app')
