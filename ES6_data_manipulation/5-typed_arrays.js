import { error } from "console";

export default function createInt8TypedArray(length, position, value) {
  if (position > length) {
    throw error('Position outside range')
  }
  else {
    ArrayBuffer = []
    ArrayBuffer[position] = value
    return ArrayBuffer
  }
}
