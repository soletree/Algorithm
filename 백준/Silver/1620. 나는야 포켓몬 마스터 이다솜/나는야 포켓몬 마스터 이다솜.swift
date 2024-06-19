import Foundation

let input = readLine()!.split(separator: " ").compactMap{ Int($0) }
let (n, m) = (input[0], input[1])
var numberDict: [Int : String] = [:]
var nameDict: [String : Int] = [:]

for i in (1...n) {
    let name = readLine()!
    nameDict[name] = i
    numberDict[i] = name
}

for _ in (0..<m) {
    let searchedText = readLine()!
    if let number = Int(searchedText) {
        print(numberDict[number]!)
    } else {
        print(nameDict[searchedText]!)
    }
}