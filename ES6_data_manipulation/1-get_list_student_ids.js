export default function getListStudentIDs(array) {
  if (!Array.isArray(array)) {
    return [];
  }
  const id = array.map(array => array.id)
  return id
}
