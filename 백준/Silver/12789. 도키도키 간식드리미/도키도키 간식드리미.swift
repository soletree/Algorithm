import Foundation

let n = Int(readLine()!)!
var waiting: [Int] = []
var currentOrder: Int = 1

let students = readLine()!.components(separatedBy: " ").compactMap{ Int($0) }

func simulate() -> Bool {
    for student in students {
        if currentOrder == student {
            currentOrder += 1
            continue
        }
        
        while !waiting.isEmpty {
            if waiting[waiting.endIndex-1] == currentOrder {
                _ = waiting.popLast()
                currentOrder += 1
            } else { break }
        }
        
        if !waiting.isEmpty,
           waiting[waiting.endIndex-1] < student {
            return false
        }
        
        waiting.append(student)
    }
    
    return true
}

print(simulate() ? "Nice" : "Sad")