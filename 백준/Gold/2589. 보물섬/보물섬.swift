import Foundation

// start point (i, j)
func solve(i: Int, j: Int) -> Int {
    guard board[i][j] == "L"
    else { return 0 }
    
    let dx: [Int] = [0, 0, 1, -1]
    let dy: [Int] = [1, -1, 0, 0]
    
    var result: Int = 0
    var visited: [[Int]] = Array(repeating: 
                                    Array(repeating: Int.max,
                                          count: w),
                                 count: l)
    
    
    var queue: Queue<(Int, Int)> = .init()
    queue.push((i, j))
    visited[i][j] = 0
    
    while !queue.isEmpty() {
        let (x, y) = queue.popLeft()!
        
        for index in (0..<4) {
            let nx = x + dx[index]
            let ny = y + dy[index]
            
            guard nx >= 0, nx < l, ny >= 0, ny < w,
                  board[nx][ny] == "L"
            else { continue }
            
            if visited[nx][ny] == Int.max {
                queue.push((nx, ny))
            }
            
            visited[nx][ny] = min(visited[nx][ny], visited[x][y] + 1)
            result = max(visited[nx][ny], result)
        }
    }
    
    return result
}


let arr: [Int] = readLine()!.split(separator: " ").map({Int($0)!})
let (l, w) = (arr[0], arr[1])
var board: [[String]] = []

(1...l).forEach { _ in
    board.append(readLine()!.map({String($0)}))
}



var ans: Int = 0

for i in (0..<l) {
    for j in (0..<w) {
        ans = max(ans, solve(i: i, j: j))
    }
}

print(ans)


struct Queue<T> {
    // index
    var left: Int = 0
    var right: Int = 1
    var body: [T] = []
    // body에 있는 개수
    var count: Int = 0
    
    mutating func push(_ newElement: T) {
        self.body.append(newElement)
        self.right += 1
        self.count += 1
    }
    
    mutating func popLeft() -> T? {
        guard self.count > 0
        else { return nil }
        self.left += 1
        self.count -= 1
        return self.body[self.left-1]
    }
    
    func isEmpty() -> Bool {
        return self.count == 0
    }
}