var express = require('express');
var router = express.Router();
const controller = require ("../controller/controller1")


/* GET home page. */
router.get('/', controller.index)
router.get('/grafica', controller.grafica)
router.post('/grafica', controller.graficaD)
router.get('/graficaP', controller.graficaP)
router.post('/graficaP', controller.graficaDP)

module.exports = router;
