import Foundation

// 보드의 크기
let n = Int(readLine()!)!
// 사과의 개수
let k = Int(readLine()!)!
// 보드
var board: [[Int]] = (0..<n).map{ _ in [Int](repeating: 0, count: n) }

// 입력
// 사과 위치
for _ in (0..<k) {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }
    board[input[0]-1][input[1]-1] = 2
}
// 뱀의 방향 정보
let l = Int(readLine()!)!
var moves: Queue<(time: Int, direct: String)> = .init()
for _ in (0..<l) {
    let move = readLine()!.split(separator: " ")
    moves.push((Int(move[0])!, String(move[1])))
}

func simulate() -> Int {
    var time: Int = 0
    var direct: GlobalDirect = .right
    var snake: [(x: Int, y: Int)] = [(0, 0)]
    board[0][0] = 1
    
    while true {
        time += 1
        let (x, y) = snake[0]
        let (dx, dy) = direct.findDxDy()
        let (nx, ny) = (x+dx, y+dy)
        
        // 보드 범위 밖이면 게임 종료
        if nx < 0 || nx > n-1 || ny < 0 || ny > n-1 {
            break
        }
        // 몸과 만나면 게임 종료
        if board[nx][ny] == 1 {
            break
        }
        
        // 사과가 있으면
        if board[nx][ny] == 2 {
            board[nx][ny] = 1
            snake = [(nx, ny)] + snake
        } else {
            board[nx][ny] = 1
            snake = [(nx, ny)] + snake
            // 몸 크기 줄이기
            if let tail = snake.popLast() {
                board[tail.x][tail.y] = 0
            }
        }
        
        // 방향 전환해야 하는 시간이면
        if !moves.isEmpty &&
           moves.body[moves.left].time == time {
            if let (_, turn) = moves.popLeft() {
                direct = convertDirect(current: direct,
                                       direct: TurnDirect(rawValue: turn)!)
            }
        }
    }
    return time
}

print(simulate())


struct Queue<T> {
    var left: Int = 0
    var body: [T] = []
    
    var count: Int {
        return self.body.count - self.left
    }
    
    var isEmpty: Bool {
        self.count == 0
    }
    
    mutating func push(_ element: T) {
        self.body.append(element)
    }
    
    mutating func popLeft() -> T? {
        guard !self.isEmpty else { return nil }
        self.left += 1
        return self.body[left-1]
    }
}


// direction: left or right
enum GlobalDirect {
    case top
    case bottom
    case left
    case right
    
    func findDxDy() -> (dx: Int, dy: Int) {
        switch self {
        case .top:
            return (-1, 0)
        case .bottom:
            return (1, 0)
        case .left:
            return (0, -1)
        case .right:
            return (0, 1)
        }
    }
}

enum TurnDirect: String {
    case left = "L"
    case right = "D"
}

func convertDirect(current: GlobalDirect,
                   direct: TurnDirect) -> GlobalDirect {
    switch current {
    case .top:
        if direct == .left { return .left }
        else { return .right }
    case .bottom:
        if direct == .left { return .right }
        else { return .left }
    case .left:
        if direct == .left { return .bottom }
        else { return .top }
    case .right:
        if direct == .left { return .top }
        else { return .bottom }
    }
}