func solution(_ s:String) -> String {    
    var result: String = String(s.first!).uppercased()
    var prev: String = result
    let arrayOfS = Array(s).map{ String($0) }
    
    for char in arrayOfS[1..<arrayOfS.count] {
        if prev == " " {
            result += char.uppercased() 
            prev = char
            continue
        }
        
        result += char.lowercased()
        prev = char
    }
    return result
}