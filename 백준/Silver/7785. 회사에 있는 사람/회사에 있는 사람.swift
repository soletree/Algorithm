import Foundation

let n = Int(readLine()!)!
var histories: Set<String> = []

for _ in (0..<n) {
    let history = readLine()!.split(separator: " ").map{ String($0) }
    let (name, cmd) = (history[0], history[1])
    
    if cmd == "enter" {
        histories.insert(name)
    } else {
        histories.remove(name)
    }
}

histories.sorted{ $0 > $1 }.forEach{ print($0) }