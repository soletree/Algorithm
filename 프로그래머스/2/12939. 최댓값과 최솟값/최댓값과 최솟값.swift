func solution(_ s:String) -> String {
    var result = ""
    let arrayOfS = s.split(separator: " ").map { Int($0) ?? 0 }
    let maxOfS = arrayOfS.max()!
    let minOfS = arrayOfS.min()!
    result = "\(minOfS) \(maxOfS)"
    return result
}