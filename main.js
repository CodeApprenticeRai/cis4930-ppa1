const express = require('express')
const app = express()
const port = 3003

var mongo = require('mongodb');
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

app.use(express.json());       // to support JSON-encoded bodies
app.use(express.urlencoded()); // to support URL-encoded bodies

app.get('/emailverifier', (req, res) => {
  MongoClient.connect(url, function(err, db) {
    if (err){ throw err};


    var cursor = db.db("function_solution_records");
    // cursor.listCollections().toArray( (err, dbs) => { console.log( dbs ) } );
    collection = cursor.collection("records");

    collection.find({}).toArray(  (error, result) => {
        if (error){
          db.close();
          console.log( error );
        }
        db.close();
        res.setHeader('Content-Type', 'application/json');
        res.end( JSON.stringify(result) );
    });
  });
});


// let callPythonFunction = new Promise(
//   ( argumentArray ) => {
//     const { spawn } = require('child_process');
//     const pythonProgram = spawn('python', argumentArray );
//
//     pythonProgram.stderr.on('data', (errorData) => {
//       console.log(data);
//     });
//   });


app.post('/emailverifier', (req, res) => {
  email = req.body.email;

  if ( email == undefined ){
    let error_message = {
      "error" : "Your request is missing the required parameter 'email'. Please include it in the request body."
    }

    res.setHeader('Content-Type', 'application/json');
    res.end( JSON.stringify(error_message) );
  }

  var functionArguments = [ './EmailVerifier.py', email ];

  const { spawn } = require('child_process');
  const pythonProgram = spawn('python', functionArguments );

  pythonProgram.stdout.on('data', (data) => {
    response_data = {
      "is_valid_email" : data.toString()
    }

    try {
        res.setHeader('Content-Type', 'application/json');
    } catch(error) {
      // just means the header is already set
    }

    res.end( JSON.stringify(response_data) );

  })

  pythonProgram.stderr.on('data', (errorData) => {
     console.log(errorData);

     let error_message = {
       "error" : "Your request is missing the required parameter 'email'. Please include it in the request body."
     }

     res.setHeader('Content-Type', 'application/json');
     res.end( JSON.stringify(error_message) );
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
          db.close();
          throw error;
        }
        db.close();
        res.setHeader('Content-Type', 'application/json');
        res.end( JSON.stringify(result) );
    });
  });
});

app.post('/retirement', (req, res) => {
  if (
    ( (req.body.starting_age !== undefined) && ( !isNaN(req.body.starting_age) ) ) &&
    ( (req.body.salary !== undefined) && ( !isNaN(req.body.salary) ) ) &&
    ( (req.body.percentage_saved !== undefined) && ( !isNaN(req.body.percentage_saved) ) ) &&
    ( (req.body.savings_goal !== undefined) && ( !isNaN(req.body.savings_goal) ) )
  ){
    var functionArguments = [ './Retirement.py', req.body.starting_age, req.body.salary, req.body.percentage_saved, req.body.savings_goal ];

    const { spawn } = require('child_process');
    const pythonProgram = spawn('python', functionArguments );

    pythonProgram.stdout.on('data', (data) => {
      response_data = {
        "solution" : data.toString()
      }

      try {
          res.setHeader('Content-Type', 'application/json');
      } catch(error) {
        // just means the header is already set
      }

      res.end( JSON.stringify(response_data) );

    })

    pythonProgram.stderr.on('data', (errorData) => {
       console.log(errorData);
       res.status(500).send("An error occured involving exeucution of the request function");
    });

  } else {
    let error_message = {
      "error" : "Your request is either missing required arguments or your arguemnts passed are non numermic. Please include the numeric arguments: [ 'starting_age', 'salary', 'percentage_saved', 'savings_goal' ] in your request."
    }

    console.log(  req.body.starting_age, req.body.salary, req.body.percentage_saved, req.body.savings_goal );

    res.setHeader('Content-Type', 'application/json');
    res.end( JSON.stringify(error_message) );
  }
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`))


module.exports = app;
