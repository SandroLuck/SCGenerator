//This script return the contracts event data
//String(process.argv[2] is the location of the contract generated
var web3 = require('web3');
const fs = require("fs");
const solc = require('solc')
web3 = new web3(new web3.providers.HttpProvider("http://localhost:8545"));
var source = fs.readFileSync(String(process.argv[2]), 'utf8');
var compiledContract = solc.compile(source, 1);
var bytecode = compiledContract.bytecode;
var gasEstimate = web3.eth.estimateGas({data: bytecode});
console.log(String(gasEstimate))