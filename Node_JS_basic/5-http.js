const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      console.log(`Number of students: ${students.length}`);
      const fields = {};
      students.forEach((line) => {
        const parts = line.split(',');
        const firstname = parts[0];
        const field = parts[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });
      for (const field in fields) {
        if (Object.hasOwn(fields, field)) {
          const list = fields[field];
          console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
        }
      }
      resolve(fields);
    });
  });
}

module.exports = countStudents;

const http = require('http');

const app = http.createServer((req, res) => {
  const { url, method } = req;

  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (method === 'GET' && url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!')
  }  else if (method === 'GET' && url === '/students') {
    res.statusCode = 200;
    res.end('This is the list of our students');
    const database = process.argv[2];
    countStudents(database)
      .then((output) => {
        res.end(output);
      })
      .catch((err) => {
        res.end(err.message)
      });
  } else {
    res.end();
  }
});

const PORT = 1245

app.listen(PORT, 'localhost', () => {
  console.log(`Server running at http://localhost:${PORT}/`);
});

module.exports = app;
