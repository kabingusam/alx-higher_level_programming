#!/usr/bin/node
module.exports = class Rectangle {
    constructor(w, h){
        if(w > 0 && h > 0){ [this.width, this.heigth] = [w, h]; }
    }
    print(){
        for( i = 0; i < this.heigth; i ++) console.log('X'.repeat(this.width));
    }
};