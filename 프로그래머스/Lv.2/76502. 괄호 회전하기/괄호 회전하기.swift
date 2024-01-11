import Foundation

func isValid(_ s: String) -> Bool {
    var stack: [Character] = []
    for char in s {
        switch char {
            // 열린 괄호
            case "[", "(", "{":
                stack.append(char)
            // 닫힌 괄호
            case "]": 
                guard let popElement = stack.popLast(),
                                popElement == "[" 
                    else { return false }
            case ")":
                guard let popElement = stack.popLast(),
                            popElement == "(" 
                else { return false }
            case "}":
                guard let popElement = stack.popLast(),
                            popElement == "{" 
                else { return false }
            default: 
                continue
        }
    }
    return stack.isEmpty
}

func rotateString(_ s: String) -> String {
    var arrayOfS = Array(s).map{ String($0) }
    let count = arrayOfS.count
    guard count > 1 
    else { return s } 
    
    let removedElement = arrayOfS.removeFirst()
    arrayOfS.append(removedElement)
    return arrayOfS.reduce("", +)
}

func solution(_ s:String) -> Int {
    var result: Int = 0
    var s: String = s

    for _ in (0..<s.count) {
        if isValid(s) {
            result += 1
        }
        s = rotateString(s)
    }
    
    return result
}