var express = require('express');
var router = express.Router();
const controlador = require("../controller/controlador");


/* GET home page. */

router.get('/',controlador.mostrarGrafico);
// router.get('/', function(req, res, next) {
//   res.render('index', { title: 'Express' });
// });

module.exports = router;
