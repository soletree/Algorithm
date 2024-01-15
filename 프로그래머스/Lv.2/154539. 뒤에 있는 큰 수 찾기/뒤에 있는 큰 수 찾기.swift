import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var result: [Int] = Array(repeating: -1, count: numbers.count)
    var stack: [(index: Int, number: Int)] = []
    
    for (index, number) in numbers.enumerated() {
        guard !stack.isEmpty 
        else { 
            stack.append((index, number))
            continue
        }
        
        while true {
            guard !stack.isEmpty 
            else { 
                stack.append((index, number))
                break
            }
            
            guard let last = stack.last 
            else { break }
            if last.number >= number {
                stack.append((index, number))
                break
            }
            
            result[last.index] = number
            stack.popLast()
        }
    }
    return result
}