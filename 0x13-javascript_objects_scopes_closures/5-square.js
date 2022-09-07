#!/usr/bin/node
module.exports = class Square extends require("./0-rectangle"){
    constructor(size){
        super(size, size);
    }
};