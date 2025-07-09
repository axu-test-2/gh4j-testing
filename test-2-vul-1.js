const http = require('http');
const url = require('url');

http.createServer(function (req, res) {
    const queryObject = url.parse(req.url, true).query;
    const userCode = queryObject.code;

    // 🚨 Vulnerability: eval with unsanitized user input
    eval(userCode); // CodeQL will flag this

    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Code executed');
}).listen(8080);
