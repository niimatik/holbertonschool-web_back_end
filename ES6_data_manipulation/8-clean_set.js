export default function cleanSet(set, startString) {
  if (startString === "" || typeof(startString) !== String) {
    return "";
  };
  const result = [];
  for (const i of set) {
    if (i.startWith(startString) && typeof i === "string") {
      const cleanvalue = i.slice(startString.length);
      result.push(cleanvalue);
    };
  };
  return result.join('-');
}
