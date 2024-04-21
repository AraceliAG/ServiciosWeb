var express = require('express');
var router = express.Router();
const controller = require ("../controller/controller1")


/* GET home page. */
router.get('/', controller.index)
router.get('/grafica', controller.grafica)
router.post('/grafica', controller.graficaD)

module.exports = router;
