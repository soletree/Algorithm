func solution(_ s:String) -> String {
    let arrayOfS = s.split(separator: " ").map { Int($0) ?? 0 }
    let maxOfS = arrayOfS.max()!
    let minOfS = arrayOfS.min()!

    return "\(minOfS) \(maxOfS)"
}