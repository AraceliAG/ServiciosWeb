
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
        
        //res.redirect('grafica');
        // Enviar datos mediante redirección con parámetros de consulta
        res.redirect(`/grafica?anio=${anio}&mes=${mes}`);

    }
}
