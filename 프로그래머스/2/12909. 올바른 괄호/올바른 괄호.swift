import Foundation

func solution(_ s:String) -> Bool {
    var stack: [Character] = []
     
    for bracket in s {
        if bracket == "(" {
            stack.append(bracket)
            continue
        } 
        
        if stack.isEmpty {
            return false
        }
        stack.popLast()
     }

    return stack.isEmpty
}