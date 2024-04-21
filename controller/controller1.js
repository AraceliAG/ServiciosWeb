
module.exports={
    

    index:function (req, res){
        res.render('index');
    },

    
    grafica:function (req, res){

        res.render('grafica');
    },
    graficaD: function(req, res) {
  
        const anio = req.body.anioSeleccionado
        const mes = req.body.mesSeleccionado
        console.log('mes', mes)
        console.log('anio', anio)
        res.render('grafica');
    }
}
