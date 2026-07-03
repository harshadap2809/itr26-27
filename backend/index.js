//console.log("hello world");
//here all the backend import lies
const express = require("express");

const server = express();
server.get("/", (req, res) => {
    res.send("hello world");
});

server.get("/test",(request,response)=>{
    response.json({message:"hello world"});
});

server.post("/test",(request,response)=>{
    const{name,age}=request.body;
    response.json({message:`hello ${name} your age is ${age}`});
});

server.listen(3000,() =>{
    console.log("server is running on port 3000");
})