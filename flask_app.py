from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')

def index():

    out = "<h1 style='font-size: 70px;'>Web Development - <mark>Flask</mark></h1>"

    out += "<div style='color: lightgreen;font-size: 40px'><a href='/home'>Home</a> | <a href='/about'>About</a> | <a href='/projects'>Projects</a> | <a href='/github'>GitHub</a> | <a href='/contact'>Contact</a> </div>"

    out += "<h3>from flask import Flask</h3>"

    out += "<h3>from flask import render_template</h3>"

    out += "<h3>app = Flask(__name__)</h3>"

    out += "<h3>@app.route('/')</h3>"

    out += "<h3>def index():</h3>"

    out += "<h3>return 'Web App with Python Flask!'</h3>"

    out += "<h3>app.run(host='0.0.0.0', port=81)</h3>"

    out += ""

    return out

@app.route('/github')

def git():

    return "<h1 style='background-color: yellow; font-size: 100px'>http://thinkphp.github.io</h1>"

@app.route('/home')

def home():

    name = 'Adrian'

    return render_template('ironman.html', title='Welcome', username=name)

@app.route('/projects/golden/<int:num>')

def Golden_Ratio(num):

    ret = []

    N = num

    a, b = 0, 1

    ret.append(a)

    for i in range(2, N + 1):

        c = a + b

        ret.append( b / c )

        a, b = b, c

    out = "<h1 style='font-size: 100px'>Golden Ratio</h1><h1 style='background-color: yellow; font-size: 70px'>"

    out += '<br/> '.join(str(i) for i in ret)

    out += '</h1>'

    return out



@app.route('/projects/fib/<int:num>')

def fib(num):

    ret = []

    N = num

    a, b = 0, 1

    ret.append(a)

    i = 2

    while i <= N:

          ret.append(b)

          a, b = b, a + b

          i += 1

    out = "<h1 style='font-size: 100px'>Fibonacci Sequence</h1><h1 style='background-color: yellow; font-size: 70px'>"

    out += ', '.join(str(i) for i in ret)

    out += '</h1>'

    return out


@app.route('/projects')

def projects():

    return "<div style='font-size: 50px; padding: 20px; margin-left: 20px'><h1 style='background-color: yellow'>Algorithms Basics</h1><ol><li><a href='projects/golden/100'>Golden Ratio</a></li> <li><a href='projects/fib/1000'>Fibonacci</a></li><li><a href='projects/gcd/10/3'>Greater Common Divisor</a></li><li> <a href='projects/fta/10'>Fundamental Theorem of Arithmetic</a></li><li><a href='projects/lcm/88/12'>Lower Common Multiple</a></li> <li><a href='/projects/bisect/64'>Bisection Method</a></li><li><a href='projects/eratosthenes/1000'>Sieve of Eratosthenes</li> <li><a href='projects/permutation/3'>Permutation</li> <li><a href='projects/partition/4'>Partitions</li> <li><a href='projects/subsets/3'>Subsets</li> <li><a href='projects/bin/8'>toBin</li> <li><a href='projects/dec/1000'>toDec</li> <li><a href='projects/combinations/4/2'>Combinations</li> <li><a href='projects/arrangements/4/2'>Arrangements</li> <li><a href='projects/partitionNumber/4'>Partitions Number</li>  <li><a href='projects/cartesian/2/3/3'>Cartesian Product A x B x C</li> <li><a href='projects/cartesian/2/3'>Cartesian Product A x B</li>  <li><a href='projects/cartesian/3'>Cartesian Product A x A</li>  <li><a href='projects/goldbach/100'>Goldbach</li> <li><a href='projects/collatz/1234'>Collatz Sequence</li> <li><a href='projects/queens/5'>N Queens Puzzle</li> </ol></div>"

@app.route('/about')

def about():

    return "<h1 style='background-color: yellow;font-size: 90px'>Adrian Statescu - Full Stack Developer</h1>"

@app.route('/contact')

def contact():

    return "<h1 style='background-color: yellow; font-size: 100px'>Contact: adrian@ironman.com</h1>"

@app.route('/projects/bisect/<int:num>')

def apps(num):

    result = bisection(0, num + 5, num)

    out = '<h1 style="background-color: orange;color: #fff; font-size: 170px">Bisection Method</h1><h1 style="font-size: 150px; color: mediumseagreen">sqrt (%d) = ' % num + '<mark>%f</mark></h1>' % result

    out += '<p>def bisection(lo, hi, a):</p>'

    out += '<p>EPS = 0.00001</p>'

    out += '<p>while not hi - lo <= EPS:</p>'

    out += '<p>m = (lo + hi) / 2.0</p>'

    out += '<p>x = lo * lo - a</p>'

    out += '<p>y = m * m - a</p>'

    out += '<p>if x > 0 and y < 0 or x < 0 and y > 0:</p>'

    out += '<p>hi = m</p>'

    out += '<p>else:</p>'

    out += '<p>lo = m</p>'

    out += '<p>return m</p>'

    out += '<style>p{background-color: mediumseagreen; color: #fff;font-size: 70px}</style>'

    return out

def bisection(lo, hi, a):

    EPS = 0.00001

    while not hi - lo <= EPS:

        m = (lo + hi) / 2.0

        x = lo * lo - a

        y = m * m - a

        if x > 0 and y < 0 or x < 0 and y > 0:

            hi = m

        else:

            lo = m

    return hi

@app.route('/projects/eratosthenes/<int:num>')

def primes(num):

    ret = eratosthenes(num)

    res = '<h1 style="color: white; background-color: mediumseagreen; font-size: 150px">Sieve of Eratosthenes</h1>'

    res += '<h2 style="font-size: 100; background-color: yellow">'

    res += ', '.join(str(i) for i in ret)

    res += '</h2>'

    return res;


def eratosthenes( n ):

    sieve = [True for i in range(0, n + 1)]

    i = 2

    while i * i <= n:

         if sieve[ i ] is True:

             j = 2

             while i * j <= n:

                   multiply = i * j

                   sieve[ multiply ] = False

                   j += 1
         i += 1

    list = []

    for i in range(2, n + 1):

        if sieve[ i ] is True:

           list.append(i)

    return list

@app.route('/projects/partition/<int:num>')

def partition(num):

    global stack, ret, n

    n = num

    stack = [0] * (n + 1)

    ret = []

    _bk()

    out = '<h2 style="font-size: 100px; color: blue; font-family: Verdana">Partitions of a set</h2><h1 style="background-color: mediumseagreen; font-size: 80px;color: yellow">'

    out += '<br/>'.join(str(i) for i in ret)

    out += '<h1>'

    return out


@app.route('/projects/permutation/<int:num>')

def permutation(num):

    global stack, ret, n

    n = num

    stack = [0] * (n + 1)

    ret = []

    bk()

    out = '<h2 style="font-size: 100px; color: blue; font-family: Verdana">Permutation of a set</h2><h1 style="background-color: yellow; font-size: 80px">'

    out += '<br/>'.join(str(i) for i in ret)

    out += '<h1>'

    return out

def init():

    global stack, level

    stack[ level ] = 0

def succ():

    global level, stack, n

    if stack[level] < n:

       stack[level] += 1
       return True

    return False

def _succ():

    global level, stack, n

    if stack[level] < stack[level - 1] + 1:

       stack[level] += 1
       return True

    return False


def _valid():

    return True

def valid():

    global level, stack, n

    for i in range(1, level):

        if stack[i] == stack[level]:

           return False

    return True

def sol():

    global level, n

    return level == n

def _printf():

    global stack, n, ret

    out = ''

    mx = max(stack)

    for i in range(1, mx + 1):

        out += '{'

        for j in range(1, n + 1):

            if stack[j] == i:

                out += str(j) + ','

        out = out[:-1]
        out += '}'

    ret.append(out)

def printf():

    global stack, n, ret

    output = []

    for i in range(1, n + 1):

        output.append(stack[i])

    ret.append(output)


def bk():

    global level

    level = 1

    init()

    while level > 0:

        hs = True
        iv = False

        while hs is True and iv is False:

            hs = succ()

            if hs is True:

               iv = valid()

        if hs is True:

            if sol() is True:

               printf()

            else:

               level += 1
               init()

        else:

            level -= 1


def _bk():

    global level

    level = 1

    init()

    while level > 0:

        hs = True
        iv = False

        while hs is True and iv is False:

            hs = _succ()

            if hs is True:

               iv = _valid()

        if hs is True:

            if sol() is True:

               _printf()

            else:

               level += 1
               init()

        else:

            level -= 1

@app.route('/projects/subsets/<int:n>')

def subsets( n ):

    vec = [0] * ( n + 1 )

    s = 0

    sol = []

    sol.append('<h1 style="font-size: 100px;background-color: lightgreen">Subsets of a Set</h1><pre style="background-color: yellow;font-size: 80px">')

    while not s == n:

        vec[ n - 1 ] += 1

        for i in range(n - 1, -1, -1):

            if vec[ i ] > 1:

               vec[ i ] -= 2

               vec[ i - 1 ] += 1

        out = ''

        s = 0

        for i in range(0, n):

            if vec[ i ] == 1:

               s += 1

               out += str(i + 1) + ' '

        sol.append(out)

    sol.append('</pre>')

    return '<br/>'.join(str(i) for i in sol)

@app.route('/projects/bin/<int:n>')

def bin( n ):

    out = ['<h2 style="font-size: 140px;background-color: yellow">Decimal to Binary</h2><h1 style="font-size: 100px; color: mediumseagreen">']

    num = '%d (10) = ' % n

    out.append( num )

    for i in range(15, -1, -1):

        out.append((n>>i)&1)

    out.append('(2)</h1>')

    return ''.join(str(i) for i in out)

def _pow(a, b):
    p = 1
    for i in range(1, b + 1):
        p *= a
    return p

@app.route('/projects/dec/<int:n>')

def dec( n ):

    out = ['<h2 style="font-size: 140px;background-color: yellow">Binary to Decimal</h2><h1 style="font-size: 100px; color: mediumseagreen">']

    num = '%d (2) = ' % n

    out.append( num )

    base = 0

    dec = 0

    while n > 0:

        dec += n % 10 * _pow(2, base)

        base += 1

        n //= 10

    out.append( dec )

    out.append('(10)</h1>')

    return ''.join(str(i) for i in out)

def i():
    global s, l
    s[l] = s[l-1]

def su():
    global s, n, k, l
    if s[l] < n - k + l:
       s[l] += 1
       return True
    return False
def s_l():
    global l, k
    return l == k
def v():
    return True
def p():
    global s, l, r
    out = ''
    for i in range(1, l + 1):
        out += str(s[i]) + ' '
    r.append(out)
def b():
    global l
    l = 1
    i()
    while not l == 0:
        hs = True
        iv = False
        while hs is True and iv is False:
              hs = su()
              if hs is True:
                 iv = v()
        if hs is True:
            if s_l():
               p()
            else:
               l += 1
               i()
        else:
            l -= 1



@app.route('/projects/combinations/<int:N>/<int:K>')

def combinations( N, K ):
    global s, n, k, r
    n = N
    k = K
    r = []
    r1 = '<span style="background-color: yellow; font-size: 100px">Comb(%d, ' % n
    r2 = '%d)</span>' % k
    r3 = r1 + r2
    r.append(r3)
    r.append('<h1 style="background-color: lightgreen;font-size: 80px">')
    s = [0] * (k + 1)
    b()
    r.append('</h1>')
    return '<br/>'.join(str(i) for i in r)

# next Arrangements

def _i():
    global s, l
    s[l] = 0

def _su():
    global s, n, k, l
    if s[l] < n:
       s[l] += 1
       return True
    return False

def _v():
    global s, l
    for i in range(1, l):
        if s[i] == s[l]:
           return False
    return True
def _b():
    global l
    l = 1
    _i()
    while not l == 0:
        hs = True
        iv = False
        while hs is True and iv is False:
              hs = _su()
              if hs is True:
                 iv = _v()
        if hs is True:
            if s_l():
               p()
            else:
               l += 1
               _i()
        else:
            l -= 1

# Generate all arrangements
@app.route('/projects/arrangements/<int:N>/<int:K>')

def arrangements( N, K ):

    global s, n, k, r
    n = N
    k = K
    r = []
    r1 = '<span style="background-color: yellow; font-size: 100px">Arrange(%d, ' % n
    r2 = '%d)</span>' % k
    r3 = r1 + r2
    r.append(r3)
    r.append('<h1 style="background-color: lightgreen;font-size: 80px">')
    s = [0] * (k + 1)
    _b()
    r.append('</h1>')
    return '<br/>'.join(str(i) for i in r)

# Greatest Common Divisor using Euclid's Algorithm
@app.route('/projects/gcd/<int:a>/<int:b>')

def euclid(a, b):
    def _euclid(a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a
    ret = _euclid(a, b)
    ret1 = "<h1 style='color: #888; background-color: orange;font-size: 90px'>Greatest Common Divisor(%d ," % a
    ret2 = "%d) = " % b
    return ret1 + ret2 + str(ret) + "</h1>"

# Lowest Common Multiple using loop
@app.route('/projects/lcm/<int:a>/<int:b>')

def lcm(a, b):

    def euclid(a,b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def _lcm(a, b):
        mx = max(a,b)
        lcm = mx
        while True:
            if lcm % a == 0 and lcm % b == 0:
                break
            lcm += 1

        return lcm

    #for debug
    #ret = (a * b) // euclid(a, b)
    ret = _lcm(a, b)
    ret1 = "<h1 style='color: #888; background-color: orange;font-size: 90px'>Lowest Common Multiple(%d, " % a
    ret2 = "%d) = " % b
    return ret1 + ret2 + str(ret) + "</h1>"


# generates all unique partitions of an integer.
# https://leetcode.com/discuss/interview-question/414064/google-count-integer-partitions
@app.route('/projects/partitionNumber/<int:number>')

def partitionsOfNumber( number ):

    global level, N, stack, sum, ret
    ret = []
    N = number
    sum = 0
    stack = [0] * (N + 1)

    def init():
        global stack, level

        if level == 1:
            stack[level] = 0
        else:
            stack[level] = stack[level-1] - 1

    def succ():
        global stack, level, N, sum

        if stack[level] < N - sum:
            stack[level] += 1
            return True
        else:
            sum -= stack[level-1]
            return False


    def valid():

        global stack, level, N, sum
        if stack[level] <= N - sum:
           sum += stack[level]
           return True
        else:
           return False

    def printf():
        global stack, level, ret, sum
        out = ""
        for i in range(1, level + 1):
            out += str(stack[i]) + " + "
        sum -= stack[level]
        out = out[:-2]
        ret.append(out)

    def sol():
        global sum, N
        return sum == N

    def bk():
        global level
        level = 1
        init()
        while not level == 0:

            hs = True
            iv = False

            while hs is True and iv is False:

                hs = succ()

                if hs is True:
                    iv = valid()

            if hs is True:
                if sol() is True:
                    printf()
                else:
                    level += 1
                    init()
            else:
                level -= 1

    bk()
    out = "<p style='font-size: 50px'>Count Integer Partitions. Given a positive integer n, find out how many ways of writing n as a sum of positive integers (Google Interview).</p><h1 style='font-size: 100px'>"
    out += '<br/>'.join(str(i) for i in ret)
    out += "</h1><p>created with Passion by <a href='http://adrianstatescu.ch'>Adrian Statescu</a></p>"
    return out

# Fundamental Theorem of Arithmetic
@app.route('/projects/fta/<int:number>')

def fta( number ):

    i = 2

    N = number

    res = []

    res.append("<h1 style='font-size: 90px; background-color: cyan'>Fundamental Theorem of Arithmetic</h1><h1 style='font-size: 80px; background-color: yellow'>")

    num = "%d = " % number

    res.append(num)

    while not N == 1:

          fm = 0

          out = ""

          while N % i == 0:

                fm += 1

                N //= i

          if fm != 0:

             out += str(i) + "^" + str(fm) + " * "

          if N == 1:
                out = out[:-2]

          res.append(out)

          i += 1

    res.append("</h1>")

    res.append("<p>Created with PASSION by <a href='http://adrianstatescu.ch'>Adrian Statescu</a></p>")

    return ''.join(str(i) for i in res)

# Collatz Sequence
@app.route('/projects/collatz/<int:number>')

def collatz( number ):

    N = number

    out = []

    first_out = "<h2 style='font-size: 100px; color: mediumseagreen; background-color: yellow'>Collatz Sequence</h2><h1 style='font-size: 120px'>%d" % number

    out.append(first_out)


    while not N == 1:

        if N & 1 != 0:

            N = 3 * N + 1

        else:

            N //= 2

        out.append(N)

    out.append("<p>Created with PASSION by <a href='http://adrianstatescu.ch'>Adrian Statescu</a></p>")

    ret = ', '.join(str(i) for i in out)

    return ret

# Goldbach's conjecture
@app.route('/projects/goldbach/<int:number>')

def goldbach( number ):

    def isPrime(n):

        prime = True

        i = 2

        while i * i <= n and prime is True:

              prime = n % i != 0

              i +=1

        return prime

    middle = number // 2

    out = "<h1 style='font-size: 120px; color: mediumseagreen; background-color: yellow'>Goldbach's conjecture</h1><h2 style='font-size: 100px'>"

    for i in range(2, middle + 1):

        if isPrime(i) is True and isPrime(number - i) is True:

           out += str(i) + ' + ' + str(number-i) +' </br> '

    out += "</h1><p>Created with PASSION by <a href='http://adrianstatescu.ch'>Adrian Statescu</a></p>"

    return out

# Cartesian
@app.route('/projects/cartesian/<int:A>/<int:B>/<int:C>')

def cartesian( A, B, C ):

    global N, vec, stack, ret

    vec = [0,A,B,C]
    N = 3
    stack = [0] * (N + 1)
    ret = ["<h2 style='font-size: 100px; background-color: yellow;color: mediumseagreen'>Cartesian Product N Sets A x B x C</h2><h1 style='font-size: 80px'> {"]

    def init():
        global stack, level
        stack[level] = 0

    def succ():
        global stack, level, vec
        if stack[level] < vec[level]:
           stack[level] +=1
           return True
        else:
           return False

    def valid():
        return True

    def sol():
        global N, level
        return N == level

    def printf():
        global stack, level, ret
        out = "("
        for i in range(1, level + 1):
            out += str(stack[i]) + ","
        out = out[:-1]
        out += ")"
        ret.append(out)

    def bk():
        global level

        level = 1
        init()

        while not level == 0:
            hs = True
            iv = False
            while hs is True and iv is False:
                  hs = succ()
                  if hs is True:
                     iv = valid()

            if hs is True:
                if sol() is True:
                   printf()
                else:
                   level += 1
                   init()
            else:
                level -= 1

    bk()
    ret.append("}")
    return ''.join(str(i) for i in ret)


@app.route('/projects/cartesian/<int:A>/<int:B>')

def productcartesian( A, B ):

    global N, vec, stack, ret

    vec = [0,A,B]
    N = 2
    stack = [0] * (N + 1)
    ret = ["<h2 style='font-size: 100px; background-color: yellow;color: mediumseagreen'>Cartesian Product A x B</h2><h1 style='font-size: 80px'> {"]

    def init():
        global stack, level
        stack[level] = 0

    def succ():
        global stack, level, vec
        if stack[level] < vec[level]:
           stack[level] +=1
           return True
        else:
           return False

    def valid():
        return True

    def sol():
        global N, level
        return N == level

    def printf():
        global stack, level, ret
        out = "("
        for i in range(1, level + 1):
            out += str(stack[i]) + ","
        out = out[:-1]
        out += ")"
        ret.append(out)

    def bk():
        global level

        level = 1
        init()

        while not level == 0:
            hs = True
            iv = False
            while hs is True and iv is False:
                  hs = succ()
                  if hs is True:
                     iv = valid()

            if hs is True:
                if sol() is True:
                   printf()
                else:
                   level += 1
                   init()
            else:
                level -= 1

    bk()
    ret.append("}")
    return ''.join(str(i) for i in ret)

@app.route('/projects/cartesian/<int:A>')

def product_cartesian( A ):

    global N, vec, stack, ret

    vec = [0,A,A]
    N = 2
    stack = [0] * (N + 1)
    ret = ["<h2 style='font-size: 100px; background-color: yellow;color: mediumseagreen'>Cartesian Product A x A</h2><h1 style='font-size: 80px'> {"]

    def init():
        global stack, level
        stack[level] = 0

    def succ():
        global stack, level, vec
        if stack[level] < vec[level]:
           stack[level] +=1
           return True
        else:
           return False

    def valid():
        return True

    def sol():
        global N, level
        return N == level

    def printf():
        global stack, level, ret
        out = "("
        for i in range(1, level + 1):
            out += str(stack[i]) + ","
        out = out[:-1]
        out += ")"
        ret.append(out)

    def bk():
        global level

        level = 1
        init()

        while not level == 0:
            hs = True
            iv = False
            while hs is True and iv is False:
                  hs = succ()
                  if hs is True:
                     iv = valid()

            if hs is True:
                if sol() is True:
                   printf()
                else:
                   level += 1
                   init()
            else:
                level -= 1

    bk()
    ret.append("}")
    return ''.join(str(i) for i in ret)

@app.route('/projects/queens/<int:N>')

def queens( N ):

    global Q, mat, stack

    Q = N

    mat = []

    stack = [0] * (Q + 1)

    for i in range(0, Q + 1):

        arr = []

        for j in range(0, Q + 1):

            arr.append(0)

        mat.append(arr)

    for i in range(0, Q + 1):

        mat[0][i] = i

    for j in range(0, Q + 1):

        mat[j][0] = j

    def succ():
        global level, stack, Q
        if stack[level] < Q:
           stack[level] += 1
           return True
        return False

    def init():

        global stack, level
        stack[level] = 0

    def valid():
        global stack, level
        for i in range(1, level):
            if stack[i] == stack[level] or abs(stack[i]-stack[level]) == abs(i - level):
                return False
        return True

    def sol():
        global level, Q
        return level == Q

    def printf():
        global stack, Q, mat
        for i in range(1, Q + 1):
            mat[i][stack[i]] = '<div style="background-color: yellow">1</div>'

    def bk():
        global level

        level = 1
        init()

        while not level == 0:

            hs = True
            iv = False

            while hs is True and iv is False:
                    hs = succ()
                    if hs is True:
                       iv = valid()
            if hs is True:
                if sol() is True:
                   printf()
                   break
                else:
                   level += 1
                   init()
            else:
                level -= 1




    bk()

    out = "<h1 style='font-size: 90px; background-color: yellow; color: mediumseagreen'>N Queens Puzzle</h1><table style='font-size: 100px;width: 100%; background-color: mediumseagreen;color: cyan'>"

    for i in range(0, Q + 1):

        out += "<tr>"

        out += ''.join('<td>' + str(j) + '</td>' for j in mat[i])

        out += "</tr>"

    out += "</table><style>tr, td {border: 3px solid cyan;text-align: center}p {font-size: 18px; color: green}</style>"

    out += "<p>Created with PASSION by <a href='http://adrianstatescu.ch'>Adrian Statescu</a></p>"

    return out
