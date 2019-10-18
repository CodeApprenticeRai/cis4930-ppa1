const express = require('express')
const app = express()
const port = 3002

var mongo = require('mongodb');
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";



app.get('/emailverifier', (req, res) => {
  MongoClient.connect(url, function(err, db) {
    if (err){ throw err};


    var cursor = db.db("function_solution_records");
    // cursor.listCollections().toArray( (err, dbs) => { console.log( dbs ) } );
    collection = cursor.collection("records");

    collection.find({}).toArray(  (error, result) => {
        if (error){
          console.log( error );
        }
        res.setHeader('Content-Type', 'application/json');
        res.end( JSON.stringify(result) );
    });

    db.close();
  });
});

app.get('/retirement', (req, res) => {
  MongoClient.connect(url, function(err, db) {
    if (err){ throw err};


    var cursor = db.db("function_solution_records");
    // cursor.listCollections().toArray( (err, dbs) => { console.log( dbs ) } );
    collection = cursor.collection("records");

    collection.find({ "function_name": "Retirement" }).toArray(  (error, result) => {
        if (error){
          throw error;
        }
        res.setHeader('Content-Type', 'application/json');
        res.end( JSON.stringify(result) );
    });

    db.close();
  });
});


app.listen(port, () => console.log(`Example app listening on port ${port}!`))
