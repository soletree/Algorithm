import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int {
    var ans = 0
    let sortedA = A.sorted(by: <)
    let sortedB = B.sorted(by: >)
    
    for (index, a) in sortedA.enumerated() {
        ans += a * sortedB[index]
    }

    return ans
}