
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
        console.log('anio', anio)
        console.log('mes', mes)
        
        res.render('grafica');
    }
}
