import itertools
from random import randint
import numpy as np

function getTrace(arr, K) {
    var tv = "IMPOSSIBLE"
    var diagonal = []
    // for i in set(itertools.permutations(arr)) {
    for i in arr {
        if (sum(i) == K) {
            var diagonal = i
            var tv = "POSSIBLE"
            break
}    return [tv, diagonal]
}
function draw_mat(diagonal, N) {
    if (diagonal == []) {
        return []
}    var arr = []
    for i in range(N) {
        var j = []
        for k in range(N) {
            var m = 1
            while m<N {
                if (m not in j) {
                    break
}                m += 1
}            j.append(m)
}        arr.append(j)
}    for i in range(N) {
        var arr[i][i] = diagonal[i]
}    return arr
}

for x in range(1, int(input())+1) {
    var a = input().split(" ")
    var N = int(a[0])
    var K = int(a[1])
    del a
    var det = getTrace( [ [i for j in range(1, N+1)] for i in range(1, N+1)] , K)
    console.log("Case //%s: %s" % (x, det[0]))
    for i in draw_mat(det[1], N) {
        if (det[0] == 'IMPOSSIBLE') {
            continue
}        var r = ""
        for j in i {
            var r = "%s %s" % (r, j)
}        console.log(r)
}