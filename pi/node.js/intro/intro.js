const http = require ('http');
const url = require ('url');

const echo = require ('./echo');

const host = "127.0.0.1";
const port = 3000;

const myEcho = new echo;


const server = http.createServer((req, res) =>
{
    var str = "Nothing to see here."

    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    const parsedUrl = url.parse(req.url, true);

    if (parsedUrl.pathname == "/echo" && req.method === "GET")
    {
        str = "Echo: " + myEcho.getString();
    }
    else if(parsedUrl.pathname="/echo" && req.method === "POST")
    {
        if (!parsedUrl.query.str) {
            res.statusCode = 400;
            str = "Need str";
        } else {
            myEcho.setString(parsedUrl.query.str);
            str = "echo set";
        }
    }

    res.end(`-${str}-`);
});

server.listen(port, host, () => {
    console.log('Web server runningat http://%s:%s/echo', host, port);
});