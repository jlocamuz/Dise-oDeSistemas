const express = require('express')

const router = express.Router();
const controladorProducto = require('../controller/controllerProduct')

router.get('/findAll', controladorProducto.findAll)

router.get('/findById/:id', controladorProducto.findById)

 router.post('/create', controladorProducto.create)

 router.put('/edit/:id', controladorProducto.edit)


 router.delete('/deleteById/:id', controladorProducto.deleteById)


module.exports = router;