import Foundation

func pronounce(_ word: String) -> Bool {
    let twoChar = ["ye", "ma"]
    let threeChar = ["aya", "woo"]
    
    var temp = ""
    var prev = ""
    
    for char in word {
        temp += String(char)
        
        guard temp.count > 1 
        else { continue }
        
        if temp.count == 2 {
            if temp == prev {
                return false 
            }
            
            if twoChar.contains(temp) {
                prev = temp
                temp = ""
            } 
            
            continue
        }
        
        if temp.count == 3 {
            if temp == prev {
                return false
            }
            
            if threeChar.contains(temp) {
                prev = temp
                temp = ""
            } 
        }
    }
    return temp.count == 0
}

func solution(_ babblings:[String]) -> Int {
    var count = 0
    for babbling in babblings {
        if pronounce(babbling) {
            count += 1
        }
    }
    return count
}