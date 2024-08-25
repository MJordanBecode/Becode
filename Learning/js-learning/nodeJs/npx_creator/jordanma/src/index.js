#!/usr/bin/env node
//index.js
// import boxen from 'boxen';
import {chalk} from 'chalk';

const log = console.log;


log(chalk.blue('Hello') + ' World' + chalk.red('!'));
let urlGithug = "https://github.com/MJordanBecode";
let urlLinkedn = "https://www.linkedin.com/in/jordan-masy/";

// console.log(boxen('unicorn', {padding: 1}));

console.log("Welcome on my Card !");
console.log("My Github : " + urlGithug );
console.log("My Linkdn : " + urlLinkedn);