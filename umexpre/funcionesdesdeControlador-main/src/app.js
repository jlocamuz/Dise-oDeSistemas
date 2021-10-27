const express = require('express')
const app = express()
const port = 3000
const rutasProducto = require('./routes/routeProduct')

app.use('/productos', rutasProducto);






app.listen(port, () =>
 console.log(`Estamos probando ahora desde el Controller las rutas!`))