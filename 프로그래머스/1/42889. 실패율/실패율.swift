import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var clears: [Int] = Array(repeating: 0, count: N)
    var fails: [Double]  = []
    var result: [Int] = Array(1...N)
    
    for stage in stages {
        guard stage != N+1 
        else { continue }
        clears[stage-1] += 1
    }
    
    var deno: Int = stages.count
    for stage in (1...N) {
        let mole = clears[stage-1]
        fails.append(Double(Double(mole)/Double(deno)))
        deno -= mole
    }
    
    result.sort { 
        if fails[$0-1] > fails[$1-1] {
            return true
        } else if fails[$0-1] == fails[$1-1] {
            if $0 < $1 {
                return true
            }
        } 
        return false
    }

    return result
}