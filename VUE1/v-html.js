const { createApp } = Vue
createApp({
    data() {
        return {
            titulo: '<h1>Hola <span class="clase"> mundo</span></h1>',
        }
    }
}).mount('#app')
