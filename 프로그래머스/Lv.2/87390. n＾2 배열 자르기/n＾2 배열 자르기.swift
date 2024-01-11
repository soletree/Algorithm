import Foundation

func solution(_ n: Int,
              _ left: Int64,
              _ right: Int64) -> [Int] {
    var nByN: [[Int]] = []
    var result: [Int] = []
    
    for index in (Int(left)...Int(right)) {
        let row = index / n 
        let col = index % n
        result.append(max(row+1, col+1))
    }
    
    return result
}