import Foundation

func findFactor(_ n: Int) -> [Int] {
    var result: Set<Int> = []
    if n == 0 {
        return [0]
    }
    
    for i in (1...Int(sqrt(Double(n)))) {
        if n % i == 0 {
            result.insert(i)
            result.insert(n / i)
        }
    }
    return Array(result)
}

func solution(_ n:Int) -> Int {
    return findFactor(n).reduce(0, +)
}