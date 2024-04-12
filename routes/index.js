var express = require('express');
var router = express.Router();
const controller = require ("../controller/controller1")


/* GET home page. */
router.get('/', controller.index)
router.get('/grafica', controller.grafica)

module.exports = router;
