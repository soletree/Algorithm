import Foundation

func bfs(_ i: Int, _ j: Int) -> Int {
    let dx: [Int] = [0, 0, 1, -1]
    let dy: [Int] = [1, -1, 0, 0]
    
    var cnt: Int = 0
    var q: Queue<(Int, Int)> = .init()
    
    if board[i][j] == 1 {
        cnt = 1
        q.push((i, j))
        board[i][j] = -1
    }
    
    while !q.isEmpty {
        let (x, y) = q.popLeft()!
        
        for i in (0..<4) {
            let nx = x + dx[i]
            let ny = y + dy[i]
            
            guard nx >= 0, nx < n, ny >= 0, ny < n,
                  board[nx][ny] == 1
            else { continue }
            
            // visited
            board[nx][ny] = -1
            q.push((nx, ny))
            cnt += 1
        }
    }
    return cnt
}

let n = Int(readLine()!)!
var board: [[Int]] = []
var ans: [Int] = []

(1...n).forEach { _ in
    board.append(readLine()!.map({Int(String($0))!}))
}

for i in (0..<n) {
    for j in (0..<n) {
        let result = bfs(i, j)
        if result > 0 {
            ans.append(result)
        }
    }
}

print(ans.count)
ans.sorted().forEach({ print($0) })

struct Queue<T> {
    var body: [T] = []
    
    var count: Int = 0
    var left: Int = 0
    var right: Int = 1
    var isEmpty: Bool {
        return self.count == 0
    }
    
    mutating func popLeft() -> T? {
        guard self.count > 0
        else { return nil }
        self.count -= 1
        self.left += 1
        return body[left-1]
    }
    
    mutating func push(_ newElement: T) {
        self.right += 1
        self.count += 1
        self.body.append(newElement)
    }
}