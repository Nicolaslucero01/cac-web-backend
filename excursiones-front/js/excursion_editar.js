console.log(location.search)     // lee los argumentos pasados a este formulario
var id=location.search.substr(4)  // excursion_update.html?id=1
console.log(id)
const { createApp } = Vue
  createApp({
    data() {
      return {
        id:0,
        nombre:"",
        descripcion:"",
        duracion:0,
        dificultad:"",
        cupos:0,
        precio:0,
        imagen:"",
        url:'https://natsanabria.pythonanywhere.com/excursiones/'+id,
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
                    this.descripcion=data.descripcion;
                    this.duracion=data.duracion;
                    this.dificultad=data.dificultad;
                    this.cupos=data.cupos;
                    this.precio=data.precio;
                    this.imagen=data.imagen;                    
                })
                .catch(err => {
                    console.error(err);
                    this.error=true              
                })
        },
        modificar() {
            let excursion = {
                nombre:this.nombre,
                descripcion: this.descripcion,
                duracion: this.duracion,
                dificultad: this.dificultad,
                cupos: this.cupos,
                precio: this.precio,
                imagen:this.imagen,
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
                    window.location.href = "./excursiones.html"; // navega a productos.html          
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
