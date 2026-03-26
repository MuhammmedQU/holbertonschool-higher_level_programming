#!/usr/bin/node

const num = parseInt(process.argv[2]);

if(isNaN(num)) {
    console.log("Not anumber.");
}
else {
    console.log('My number: ' + num);
}
