import Foundation

let input = readLine()!.split(separator: " ").compactMap{ Int($0) }
let (n, m) = (input[0], input[1])
var strSet: Set<String> = []
var ans: Int = 0

for _ in (0..<n) {
    strSet.insert(readLine()!)
}

for _ in (0..<m) {
    let cmpStr = readLine()!
    if strSet.contains(cmpStr) {
        ans += 1
    }
}

print(ans)