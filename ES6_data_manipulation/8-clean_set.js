export default function cleanSet(set, startString) {
  if (startString.length === 0 || typeof startString !== String) {
    return "";
  };
  const result = [];
  for (const i of set) {
    if (i.startsWith(startString) && typeof i === "string") {
      const cleanvalue = i.slice(startString.length);
      result.push(cleanvalue);
    };
  };
  return result.join("-");
}
