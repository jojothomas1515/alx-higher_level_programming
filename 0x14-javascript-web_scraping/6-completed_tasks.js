#!/usr/bin/node

// get the number of completed task for all users
const process = require('process');
const argv = process.argv;
const argLen = argv.length;
const request = require('request');

if (argLen !== 3) { process.exit(-1); }

const uri = argv[2];

function completedTasks (err, res, body) {
  const result = {};
  if (err) { console.log(err); } else {
    const tasks = JSON.parse(body);
    const completed = tasks.filter((data) => {
      return data.completed === true;
    });
    completed.forEach(task => {
      const id = task.userId;
      result[`${id}`] = result[`${id}`] ? result[`${id}`] + 1 : 1;
    });
    console.log(result);
  }
}

request(uri, completedTasks);
