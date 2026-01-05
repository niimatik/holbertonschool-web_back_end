const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const line = data.split('\n').filter((line) => line.trim() !== '');
    const student = line.slice(1);
    console.log(`Number of students: ${student.length}`);
    const fields = {};
    student.forEach((lines) => {
      const part = lines.split(',');
      const firstname = part[0];
      const field = part[3];
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
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
