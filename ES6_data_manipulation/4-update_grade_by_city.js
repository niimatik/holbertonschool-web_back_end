export default function updateStudentGradeByCity(studentlist, city, newgrades) {
  const locationarray = studentlist.filter(element => element.location === city);
  const updatearray = locationarray.map(element => {
    const gradefound = newgrades.find(item => item.studentID === element.id)
    let grade
    if (gradefound) {
      grade = gradefound.grade
    }
    else {
      grade = "N/A"
    };
    return {
      ...element,
      grade: grade
    }
  });
  return updatearray
}
