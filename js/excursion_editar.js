console.log(location.search)     // lee los argumentos pasados a este formulario
var id=location.search.substr(4)  // producto_update.html?id=1
console.log(id)
const { createApp } = Vue
  createApp({
    data() {
      return {
        id:0,
        nombre:"",
        duracion:"",
        descripcion:"",
        dificultad:"",
        imagen:"",
        cupos:0,
        precio:0,
        url:'http://127.0.0.1:5000/excursiones/'+id,
       }  
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.id=data.id;
                    this.nombre = data.nombre;
                    this.duracion=data.duracion;
                    this.descripcion=data.descripcion;
                    this.dificultad=data.dificultad;
                    this.imagen=data.imagen;
                    this.cupos=data.cupos;
                    this.precio=data.precio                         
                })
                .catch(err => {
                    console.error(err);
                    this.error=true              
                })
        },
        modificar() {
            let excursion = {
                nombre:this.nombre,
                duracion: this.duracion,
                descripcion: this.descripcion,
                dificultad: this.dificultad,
                imagen: this.imagen,
                cupos: this.cupos,
                precio: this.precio
            }
            var options = {
                body: JSON.stringify(excursion),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
                    alert("Registro modificado")
                    window.location.href = "./excursiones.html"; // navega a excursiones.html          
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar")
                })      
        }
    },
    created() {
        this.fetchData(this.url)
    },
  }).mount('#app')

