import Foundation

// Initialize
let n = Int(readLine()!)!
let m = Int(readLine()!)!
var adj: [[Int]] = .init(repeating: .init(), count: n+1)

// Input
for _ in (0..<m) {
    let input = readLine()!.components(separatedBy: " ").map{ Int($0)! }
    let (i, j) = (input[0], input[1])
    
    adj[i].append(j)
    adj[j].append(i)
}

var friends: Set<Int> = [1]

for friend in adj[1] {
    friends.insert(friend)
    for next in adj[friend] {
        friends.insert(next)
    }
}

print(friends.count-1)