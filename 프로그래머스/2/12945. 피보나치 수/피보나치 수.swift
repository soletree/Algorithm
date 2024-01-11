import Foundation

func solution(_ n:Int) -> Int {
    var first: Int = 0 // f(0)
    var second: Int = 1 // f(1)
    var result: Int = 0 // output
    
    for input in (2...n) {
        result = (first + second) % 1234567
        first = second 
        second = result
    }
    
    return result % 1234567
}