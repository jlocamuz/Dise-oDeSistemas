const express = require('express')

const router = express.Router();
router.get('/findAll', (req, res) => res.send('Todos los registros'))

router.get('/findById/:id', (req, res) =>{
    const recibidaId = req.params.id
    res.send('Busco por ID: ' + recibidaId)}
 )

 router.post('/create', (req, res) => res.send('Cree un nuevo registro'))

 router.put('/edit/:id', (req, res) => res.send('Edité un nuevo registro'))


 router.delete('/deleteById/:id', (req, res) =>{
    const recibidaId = req.params.id
    res.send('Elimino por ID: ' + recibidaId)}
 )







module.exports = router;