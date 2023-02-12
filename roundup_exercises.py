Bài 1:In 10 lần chữ hello ra màn hình
for i in range(10):
    print("Hello")

Bài 2:In các số lẻ dương bé hơn 100
for i in range(1, 100, 2):
    print(i)

Bài 3:In các số chẵn chia hết cho 3 bé hơn 100
for i in range(2, 100, 2):
    if i % 3 == 0:
        print(i)

Bài 4:Nhập vào số nguyên dương a, in ra bảng cửu chương của a
a = int(input("Nhập số nguyên dương a: "))

for i in range(1, 11):
    if a >= 1:
        print(f"{a} x {i} = {a * i}")
    else:
        break

Bài 5:Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím
Ví dụ: Ta nhập h = 4:

h=int(input("Nhập vào độ cao h: "))
khoangtrangngoai=h-1
khoangtrangtrong=1
for i in range(h):
    if i==0:
        print(" " * khoangtrangngoai + "*")
    elif i<h-1:
        print(" " * khoangtrangngoai + "*" + " " * khoangtrangtrong + "*")
        khoangtrangtrong+=2
    else:
        print("*" * (h*2-1))
    khoangtrangngoai -=1
    
Bài 6:Nhập vào n
Tính S = 1 + 2 + 3 + 4 + … + n
Bài 7:Nhập vào số nguyên dương a, in toàn bộ ước của a
n = int(input("Nhập số n: "))
s = 0

for i in range(1, n + 1):
    s += i

print(f"S = 1 + 2 + 3 + ... + {n} = {s}")

Bài 8:Viết chương trình nhập một số nguyên dương có một chữ số. Sau đó in ra màn hình một hình chữ nhật gồm 4 cột và 5 hàng như sau.
INPUT
Số nguyên dương có một chữ số.
OUTPUT
In ra 5 dòng có định dạng như bên dưới (các bạn nhớ để ý các chuỗi khoảng trắng ở giữa các số nguyên dương có một chữ số).
VÍ DỤ
input:        
4
output:     
4 4 4 4
4     4
4     4
4     4
4 4 4 4

number = int(input("Nhập số nguyên dương có một chữ số: "))
for i in range(5):
    if i == 0 or i == 4:
        print(f"{number} {number} {number} {number}")
    else:
        print(f"{number}     {number}")


Bài 9:Nhập vào số nguyên dương a, đếm số ước của a
a = int(input("Nhập số nguyên dương a: "))
count = 0
for i in range(1, a+1):
    if a % i == 0:
        count += 1
print("Số ước của", a, "là", count)

Bài 10:Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b

# Nhập vào số nguyên dương a và b
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
# Tìm ước chung nhỏ nhất của a và b
min_num = min(a, b)
# Khởi tạo danh sách chứa các ước chung của a và b
uc = []
# Sử dụng vòng lặp để tìm tất cả các ước chung của a và b
for i in range(1, min_num + 1):
    if a % i == 0 and b % i == 0:
        uc.append(i)
# In ra toàn bộ ước chung của a và b
print("Toàn bộ ước chung của", a, "và", b, "là:", uc)

Bài 11:Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(i, end=' ')

Bài 12:Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
# Nếu dùng vòng lập for
a = int(input("Nhập số nguyên dương a: "))
if a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            print(a, "không phải là số nguyên tố")
            break
    else:
        print(a, "là số nguyên tố")
else:
    print(a, "không phải là số nguyên tố")

# Nếu dùng vòng lập while
a = int(input("Nhập số nguyên dương a: "))
if a <= 1:
    print(a, "không phải là số nguyên tố.")
else:
    is_prime = True
    i = 2
    while i <= a ** (0.5):
        if a % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(a, "là số nguyên tố.")
    else:
        print(a, "không phải là số nguyên tố.")

Bài 13:Nhập vào số nguyên dương a, nếu nhập số âm thì yêu cầu nhập lại cho đến khi người dùng nhập đúng số dương
Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng quy tắc”
a = int(input("Nhập vào số nguyên dương: "))
while a < 0:
  print("Vui lòng nhập lại số dương.")
  a = int(input("Nhập vào số nguyên dương: "))
print("Bạn nhập đúng quy tắc.")

Bài 14:Nhập n
Cho S(k) = 1 + 2 + 3 + … + k
Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
n = int(input("Nhập vào số n: "))
k = 1
sum = 0
while sum < n:
    sum = sum + k
    k = k + 1
k = k - 1
print("k sao cho S(k) lớn nhất nhưng nhỏ hơn n là: ", k)

Bài 15:Nhập vào A, tìm n nhỏ nhất sao cho
1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
n = 1
sum = 0
A = float(input("Nhập vào A: "))
while sum <= A:
    sum += 1/n
    n += 1
print("Kết quả:", n-1)

Bài 16:Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.
Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập
number = int(input("Nhập số: "))
max_number = number
min_number = number
while number != -1:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
    number = int(input("Nhập số: "))

print("Số lớn nhất:", max_number)
print("Số nhỏ nhất:", min_number)

Bài 17:Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số
n = int(input("Nhập vào số nguyên dương n: "))
print("Số chữ số của n là:", len(str(n)))

Bài 18:Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
n = int(input("Nhập số nguyên dương n: "))
so_chu_so_chan = 0
so_chu_so_le = 0
while n > 0:
    chu_so = n % 10
    if chu_so % 2 == 0:
        so_chu_so_chan += 1
    else:
        so_chu_so_le += 1
    n = n // 10

print("Số chữ số chẵn:", so_chu_so_chan)
print("Số chữ số lẻ:", so_chu_so_le)

Bài 19:Nhập vào số nguyên dương n, tính tổng các chữ số của n
n = int(input("Nhập vào số nguyên dương n: "))
sum_of_digits = 0
while n > 0:
    digit = n % 10
    sum_of_digits += digit
    n //= 10
print("Tổng các chữ số của số n là:", sum_of_digits)

Bài 20:Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 2^k hay không
n = int(input("Nhập số nguyên dương n: "))
# Kiểm tra n có phải là số dạng 2^k hay không
is_power_of_two = True
while n > 1:
    if n % 2 != 0:
        is_power_of_two = False
        break
    n = n // 2
# In kết quả
if is_power_of_two:
    print("n là số dạng 2^k")
else:
    print("n không phải là số dạng 2^k")

Bài 21:Dãy số fibonacci là dãy số được định nghĩa như sau: 1, 1, 2, 3, 5, 8, 13,... với số kế tiếp sẽ bằng tổng hai số trước đó
Nhập vào A, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá A
a, b = 1, 1
A = int(input("Nhập A: "))
while b <= A:
    print(b)
    a, b = b, a + b

Bài 22:in bảng cửu chương rút gọn
Bảng cửu chương rút gọn là bảng có hàng là kết quả của phép nhân một số với các giá trị từ 1 tới 10. Chúng ta sẽ in 9 hàng tương ứng với các số từ 2 tới 10.
Bài 23: Viết chương trình quản lý điểm học sinh bao gồm 5 môn : Toán , lý , hóa, văn, anh , mỗi môn gồm 6 cột  là cột điểm "miệng", cột điểm "15 phút",cột điểm "1 tiết" , cột điểm "thi" ,  cột điểm "trung bình mônmôn" ( cột điểm trung bình môn được tính như sau : "miệng" cộng "15 phút" cộng "1 tiết" nhân 2 cộng "thi" nhân 3 , sau đó lấy tổng chia cho 7 sẽ ra điểm trung bình ) và cột " xếp loại" ( Đây là cột xếp theo thứ tự điểm trung bình , nếu trong danh sách có 10 học sinh thì thì cột này sẽ xếp học sinh có điểm ttrung bình cao nhất là 1, người cao thứ 2 là 2 , người cao thứ 3 là 3, ... người thấp nhất là 10)
Bài 24:In danh sách 24 chữ cái tiếng anh 
Bài 25:Tạo trò chơi “Cows and Bulls” với cách thức hoạt động như sau:
Tạo ngẫu nhiên một con số có 4 chữ số. Yêu cầu người chơi đoán con số đó.
Khi người chơi đoán đúng một chữ số nào đó ở đúng vị trí, họ sẽ có một “Cow”. Với mỗi chữ số sai, họ sẽ có một “Bull”. 
Mỗi khi người dùng đưa ra phỏng đoán, hãy cho họ biết họ có bao nhiêu “Cows” và “Bulls”. Khi người dùng đoán đúng số, trò chơi kết thúc. Theo dõi số lần đoán mà người dùng thực hiện trong suốt trò chơi và họ biết khi kết thúc.
Giả sử, máy tính tạo ra một con số là 1038. Một tương tác sẽ diễn ra như sau:
Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
