var express = require('express');
var router = express.Router();
var db=require('../database');
// another routes also appear here
// this script to fetch data from MySQL databse table
router.get('/user-list', function(req, res, next) {
    var sql='SELECT * FROM testDB_table';
    db.query(sql, function (err, data, fields) {
    if (err) throw err;
    res.render('table-list', { title: 'Messdata', userData: data});
  });
});
module.exports = router;