var assert = require('assert');
const request = require('request');



describe("API Endpoint",
  () => {
    describe("EmailVerifier", () =>{
      it('should return a list', () => {
        request('localhost:3002/emailverifier', { json: true }, (err, res, body) => {
          if (err) { return console.log(err); }
          assert.equal( Array.isArray( body.explanation ), True );
        });
      });
    });

    describe("Retirement", () =>{
      it('should return a list', () => {
        request('localhost:3002/retirement', { json: true }, (err, res, body) => {
          if (err) { return console.log(err); }
          assert.equal( Array.isArray( body.explanation ), True );
        });
      });
    });

  }
});
