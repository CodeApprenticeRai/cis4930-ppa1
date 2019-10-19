process.env.NODE_ENV = 'test';

let chai = require('chai');
let chaiHttp = require('chai-http');
let server = require('../main');
let should = chai.should();

chai.use(chaiHttp);

describe('/GET emailverifier', () => {
    it('should successfully return an array', (done) => {
      chai.request(server)
          .get('/emailverifier')
          .end((err, res) => {
                res.should.have.status(200);
                res.body.should.be.a('array');
            done();
          });
    });
});

describe('/POST emailverifier', () => {
    it('should return an error message if required argument \'email\' is missing', (done) => {
      let request_data = {
        "irrelevant": "information"
      };

      chai.request(server)
          .post('/emailverifier')
          .send(request_data)
          .end((err, res) => {
                res.should.have.status(200);
                res.body.should.contain.key('error');
            done();
          });
    });

    it('should return a solution if email argument present', (done) => {
      let request_data = {
        "email": "jamesbond@gmail.com"
      };

      chai.request(server)
        .post('/emailverifier')
        .send(request_data)
        .end((err, res) => {
              res.should.have.status(200);
              res.body.should.contain.key( "is_valid_email");
          done();
        });
    });
});


describe('/GET retirement', () => {
    it('should successfully return an array', (done) => {
      chai.request(server)
          .get('/retirement')
          .end((err, res) => {
                res.should.have.status(200);
                res.body.should.be.a('array');
            done();
          });
    });
});

describe('/POST retirement', () => {
    it('should return an error message if required arguments are  missing', (done) => {
      let request_data = {
        "irrelevant": "information",
        "required_arguments": "missing"
      };

      chai.request(server)
          .post('/retirement')
          .send(request_data)
          .end((err, res) => {
                res.should.have.status(200);
                res.body.should.contain.key('error');
            done();
          });
    });

    it('should return a solution if all required arguments present', (done) => {
      let request_data = {
              "starting_age": 10,
              "salary": 1000000,
              "percentage_saved": 0.75,
              "savings_goal": 10000000
          };

      chai.request(server)
        .post('/retirement')
        .send(request_data)
        .end((err, res) => {
              res.should.have.status(200);
              res.body.should.contain.key( "solution");
          done();
        });
    });
});
