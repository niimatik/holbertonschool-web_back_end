export default function getStudentsByLocation(list, city) {
  const array = list.filter(element => element.location === city);
  return array;
}
