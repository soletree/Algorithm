import Foundation

func countZeroAndOne(_ s: String) -> [Int] {
    var zero: Int = 0
    var one: Int = 0
     
    for char in s {
        switch char {
            case "0": 
                zero += 1
            case "1": 
                one += 1
            default: 
                continue
        }
    }
    return [zero, one]
}

func convertDecimalToBinary(_ decimal: Int) -> String {
    var result: String = ""
    var decimal: Int = decimal 
    while decimal / 2 != 0 {
        result = String(decimal % 2) + result
        decimal = decimal / 2
    }
    
    if decimal % 2 == 1 {
        result = "1" + result
    }

    return result
}

func solution(_ s:String) -> [Int] {
    var convertedBinary: String = s
    var countZero: Int = 0 
    var countConvert: Int = 0
    
    while true {
        // 0 제거 0의 개수, 1의 개수 구함 
        let deleteZero = countZeroAndOne(convertedBinary)
        countZero += deleteZero[0]
        if convertedBinary == "1" {
            break
        }
        
        // 이진 변환
        convertedBinary = convertDecimalToBinary(deleteZero[1])
        countConvert += 1
    }
    
    return [countConvert, countZero]
}