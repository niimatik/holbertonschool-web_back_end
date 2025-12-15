export default function getStudentIdsSum(array) {
  const sumarray = array.reduce((sum, temparray) => sum + temparray.id, 0);
  return sumarray;
}
