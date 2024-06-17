import Foundation

let n = Int(readLine()!)!
var ans: [(num: Int, count: Int)] = .init(repeating: (num: n, count: Int.max),
                            count: n+1)
ans[n] = (n, 0)


for i in stride(from: n, to: 0, by: -1) {
    if i % 2 == 0, i / 2 > 0 {
        if ans[i].count + 1 < ans[i/2].count {
            ans[i/2] = (i, ans[i].count+1)
        }
    }
    
    if i % 3 == 0, i / 3 > 0 {
        if ans[i].count + 1 < ans[i/3].count {
            ans[i/3] = (i, ans[i].count+1)
        }
    }
    
    if i - 1 > 0 {
        if ans[i].count + 1 < ans[i-1].count {
            ans[i-1] = (i, ans[i].count+1)
        }
    }
}

var result: String = ""

var current: Int = 1
var cnt: Int = 0

while true {
    if current == n {
        result = String(current) + " " + result
        break
    }
    cnt += 1
    result = String(current) + " " + result
    current = ans[current].num
}

print(cnt)
print(result)