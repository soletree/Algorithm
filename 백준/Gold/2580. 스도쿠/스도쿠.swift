import Foundation

// 9*9
var rowMask: [Int] = .init(repeating: 0, count: 9)
var colMask: [Int] = .init(repeating: 0, count: 9)
var blockMask: [[Int]] = .init(repeating: .init(repeating: 0, count: 3), count: 3)
var board: [[Int]] = .init(repeating: .init(), count: 9)
var emptyBlocks: [(x: Int, y: Int)] = []

for i in 0..<9 {
    let row = readLine()!.split(separator: " ").map { Int($0)! }
    for j in 0..<9 {
        let value = row[j]
        board[i].append(value)
        
        if value == 0 {
            emptyBlocks.append((i, j))
        } else {
            let bit = 1 << (value - 1)
            rowMask[i] |= bit
            colMask[j] |= bit
            blockMask[i/3][j/3] |= bit
        }
    }
}

let countOfEmptyBlocks = emptyBlocks.count

func back(cnt: Int) {
    if countOfEmptyBlocks == cnt {
        printMatrix(board)
        exit(0)
    }
    
    let (x, y) = emptyBlocks[cnt]
    
    for next in 1...9 {
        let bit = 1 << (next - 1)
        if rowMask[x] & bit == 0 && colMask[y] & bit == 0 && blockMask[x/3][y/3] & bit == 0 {
            rowMask[x] |= bit
            colMask[y] |= bit
            blockMask[x/3][y/3] |= bit
            board[x][y] = next
            
            back(cnt: cnt + 1)
            
            board[x][y] = 0
            rowMask[x] &= ~bit
            colMask[y] &= ~bit
            blockMask[x/3][y/3] &= ~bit
        }
    }
}

back(cnt: 0)

func printMatrix(_ mat: [[Int]]) {
    for arr in mat {
        for element in arr {
            print(element, terminator: " ")
        }
        print()
    }
}