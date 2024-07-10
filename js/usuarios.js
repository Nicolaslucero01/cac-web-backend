const { createApp } = Vue
createApp({
    data() {
        return {
            usuarios: [],
            url: 'https://natsanabria.pythonanywhere.com/usuarios', 
            // si el backend esta corriendo local usar localhost 5000 (si no lo subieron a pythonanywhere)
            // url: 'http://mcerda.pythonanywhere.com/productos',   // si ya lo subieron a pythonanywhere
            error: false,
            cargando: true,
            /* atributos para el guardar los valores del formulario */
            id: 0,
            nombre: "", 
            clave: "",
            nivel: ""       
        }  
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.usuarios = data;
                    this.cargando = false;
                })
                .catch(err => {
                    console.error(err);
                    this.error = true;
                });
        },
        eliminar(id) {
            const url = this.url + '/' + id;
            var options = {
                method: 'DELETE',
            };
            fetch(url, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
                    alert('Registro Eliminado');
                    location.reload(); // recarga el json luego de eliminado el registro
                })
                .catch(error => {
                    // Manejar cualquier error que ocurra durante la solicitud
                    console.error('Error al eliminar el registro:', error);
                    alert('Ocurrió un error al eliminar el registro.');
                }); // <- Aquí falta una llave de cierre '}' y paréntesis de cierre ')'
        },
        grabar() {
            let usuario = {
                nombre: this.nombre,
                clave: this.clave,
                nivel: this.nivel
            };
            var options = {
                body: JSON.stringify(usuario),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            };
            fetch(this.url, options)
                .then(() => {
                    alert("Registro grabado");
                    window.location.href = "./usuarios.html";  // recarga productos.html
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar");  // puedo mostrar el error tambien
                });
        }
    },
    created() {
        this.fetchData(this.url);
    },
}).mount('#app');