

let controllerProduct = {

    findAll: (req, res) => res.send('Todos los registros desde el controller'),
  
    findById: (req, res) => {
        const recibidaId = req.params.id
        res.send('Busco por ID, desde el controller: ' + recibidaId)
    },

    create: (req, res) => res.send('Cree un nuevo registro desde el controller'),

    edit : (req, res) => res.send('Edité un nuevo registro'),

    deleteById : (req, res) =>{
        const recibidaId = req.params.id
        res.send('Elimino por ID: ' + recibidaId)}
     
    
}

module.exports = controllerProduct