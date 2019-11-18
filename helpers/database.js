const mysql =  require('mysql2');

const pool = mysql.createPool({
    host: 'localhost',
    user: 'vondd',
    database: 'vondd',
    password: 'EwMx(foo!2bar'
});

module.exports = pool.promise();
