Link bài tập: https://sites.google.com/view/pythonwithnhat/trang-ch%E1%BB%A7

Bài 1: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ (quy định là chuỗi không có ký tự đặc biệt, không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)
string = input("Nhập vào một chuỗi: ")
word_count = len(string.split())
print("Số lượng từ trong chuỗi là:", word_count)
#phương thức split() để tách chuỗi thành các từ, mỗi từ cách nhau bởi khoảng trắng. 

Bài 2: Nhập vào một chuỗi, hãy in từ đầu tiên trong chuỗi
sentence = input("Nhập vào một chuỗi: ")
words = sentence.split()
print("Từ đầu tiên trong chuỗi là:", words[0])

Bài 3: Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy, hãy tính tổng 3 số nguyên đó
VD:
Nhập: 3, 12, 15
Tổng: 30
  
string = input("Nhập vào một chuỗi có dạng 3 số nguyên, mỗi số nguyên cách nhau một dấu phẩy: ")
numbers = string.split(',')
sum = 0
for number in numbers:
    sum += int(number)
print("Tổng của 3 số nguyên là:", sum)

Bài 4: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số

#Hàm isupper() để kiểm tra xem ký tự đang xét có phải là in hoa hay không.  
#hàm islower() để kiểm tra xem ký tự đang xét có phải là in thường hay không
#hàm isdigit() để kiểm tra xem ký tự đang xét có phải là số hay không.
s = input("Nhập vào một chuỗi: ")
upper = 0
lower = 0
digit = 0
for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
print("Số ký tự in hoa: ", upper)
print("Số ký tự in thường: ", lower)
print("Số ký tự số: ", digit)
  
Bài 5: Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số
  # Tương tự bài 4 =))
Bài 6: Nhập vào một chuỗi, hãy tách toàn bộ ký tự số trong chuỗi ra rồi tính tổng của chúng
VD:
Nhập chuỗi: abd45ecf47wde3s1
Tổng: 4 + 5 + 4 + 7 + 3 + 1 = 24
  #hàm isdigit() để kiểm tra xem ký tự đang xét có phải là số hay không.

string = input("Nhập vào một chuỗi: ")
sum = 0
for char in string:
    if char.isdigit():
        sum += int(char)
print("Tổng của các số trong chuỗi là:", sum)  
  
Bài 7: Nhập vào một chuỗi, hãy tách toàn bộ con số trong chuỗi ra rồi tính tổng của chúng
VD:
Nhập chuỗi: abd45ecf47wde3s1
Tổng: 45 + 47 + 3 + 1 = 96
  
string = input("Nhập chuỗi: ")
total = 0
number = ""
for char in string:
    if char.isdigit():
        number += char
    else:
        if len(number) > 0:
            total += int(number)
            number = ""
if len(number) > 0:
    total += int(number)
print("Tổng:", total)

Bài 8: Nhập vào một chuỗi, kiểm tra chuỗi đó có phải là một chuỗi mật khẩu mạnh hay không (một chuỗi mật khẩu mạnh cần có ít nhất 1 ký tự đặc biệt, 1 ký tự in hoa, 1 con số, 1 chữ thường và độ dài phải lớn hơn 6)

password = input("Enter a password: ")
special_char = False
upper_char = False
lower_char = False
digit = False
for char in password:
    if char.isdigit():
        digit = True
    elif char.isupper():
        upper_char = True
    elif char.islower():
        lower_char = True
    elif char in "#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
        special_char = True
if len(password) >= 6 and special_char and upper_char and lower_char and digit:
    print("Password is strong.")
else:
    print("Password is weak.")

  
Bài 9: Nhập vào một số nguyên, hãy chuyển số sang chuỗi, rồi đặt dấu chấm phân tách mỗi 3 chữ số (phân cách phần ngàn) rồi in ra màn hình
VD:
Nhập số: 375469485
Đổi sang chuỗi rồi in ra: 375.469.485
  
number = int(input("Nhập số: "))
number_str = str(number)
result = ''
count = 0
for i in range(len(number_str)-1, -1, -1):
    result = number_str[i] + result
    count += 1
    if count == 3 and i != 0:
        result = '.' + result
        count = 0
print("Đổi sang chuỗi rồi in ra: " + result)

Bài 10: Nhập vào chuỗi a và chuỗi b
Hãy xóa chuỗi b trong chuỗi a rồi in lại chuỗi a ra màn hình (không dùng hàm replace)
Ví dụ:
Chuỗi a: "Xin chào mọi người!"
Chuỗi b: "Xin chào"
Sau khi xóa, chuỗi a: " mọi người!"
  
a = input("Nhập chuỗi a: ")
b = input("Nhập chuỗi b: ")
i = 0
while i < len(a):
    if a[i:i+len(b)] == b:
        a = a[:i] + a[i+len(b):]
    else:
        i += 1
print("Sau khi xóa, chuỗi a:", a)

Bài 11: Nhập vào một list số nguyên L, tìm và in ra giá trị lớn nhất trong L
 
L = list(map(int, input("Nhập vào list số nguyên: ").split()))
max_value = L[0]
for num in L:
    if num > max_value:
        max_value = num
print("Giá trị lớn nhất trong list là:", max_value)

Bài 12: Nhập vào một list số nguyên L, nhập vào 2 số nguyên dương a và b (a < b < len(L))
Tìm và in ra số nhỏ nhất trong list từ vị trí a đến vị trí b

L = list(map(int, input("Nhập list số nguyên L: ").split()))
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
min_value = L[a]
for i in range(a + 1, b + 1):
    if L[i] < min_value:
        min_value = L[i]
print("Số nhỏ nhất trong list từ vị trí a đến vị trí b là:", min_value)

Bài 13: Nhập vào một list số nguyên L, hãy kiểm tra xem tất cả các phần tử trong mảng có bằng nhau hay không, nếu có thì in True, không có thì in False
 
L = list(map(int, input("Nhập vào list số nguyên L (các phần tử cách nhau bằng dấu cách): ").split()))
check = True
for i in range(1, len(L)):
    if L[i] != L[i-1]:
        check = False
        break
if check:
    print(True)
else:
    print(False)

Bài 14: Nhập vào một list số nguyên L, tìm và in ra giá trị dương đầu tiên của list, nếu không có giá trị dương, ta in ra -1

L = [int(x) for x in input("Nhập vào một list số nguyên L: ").split()]
for i in L:
    if i > 0:
        print(i)
        break
else:
    print(-1)

Bài 15: Nhập vào một list L, hãy tìm và in ra giá trị âm lớn nhất trong L, nếu L không có giá trị âm thì ta in 0
 
L = [int(x) for x in input("Nhập vào list L: ").split()]
max_negative = 0
for num in L:
    if num < 0:
        if num > max_negative:
            max_negative = num
print("Giá trị âm lớn nhất trong L là:", max_negative)

Bài 16: Nhập vào một list số nguyên L, nhập vào số nguyên x, tìm giá trị trong list xa x nhất
  
L = list(map(int, input("Nhập vào list L: ").split()))
x = int(input("Nhập vào số nguyên x: "))
max_distance = 0
result = 0
for num in L:
    distance = abs(num - x)
    if distance > max_distance:
        max_distance = distance
        result = num
print("Giá trị trong list xa x nhất:", result)
  
Bài 17: Nhập vào một list số nguyên L, tính giá trị trung bình của list L
Bài 18: Nhập vào một list số nguyên L, hãy kiểm tra xem L có được sắp xếp từ bé đến lớn hay không, nếu có thì in True, không có thì in False
Bài 19: Nhập vào một list số nguyên L, hãy sắp xếp list L theo thứ tự từ bé đến lớn
Bài 20: Nhập vào một list số nguyên L, hãy kiểm tra xem L có phải là một cấp số cộng hay không? Nếu có thì tìm và in ra công sai, nếu không có thì in ra None
Bài 21: Nhập vào một list số nguyên L, Hãy tìm và in ra một vị trí trong L thỏa hai điều kiện: có hai giá trị lân cận và giá trị tại vị trí đó bằng tích hai giá trị lân cận. Nếu L không tồn tại giá trị như vậy thì in ra - 1
Bài 22: Người ta định nghĩa một list số nguyên là list chẵn lẻ, nếu như tổng 2 phần tử bất kỳ bên trong list đều là số lẻ
Nhập vào một list số nguyên L và kiểm tra xem L có phải là list chẵn lẻ hay không
Bài 23: Người ta định nghĩa một list số nguyên được gọi là “dạng sóng” khi tất cả các phần tử đều lớn hơn hoặc nhỏ hơn hai phần tử xung quanh nó.
Nhập vào một list số nguyên L và kiểm tra xem L có phải là list “dạng sóng” hay không, nếu có thì ta in ra True, không có thì ta in False
Bài 24: Nhập vào một list số nguyên L, hãy đếm số lượng giá trị trong list thỏa tính chất: “lớn hơn tất cả các giá trị đứng đằng trước nó”
Bài 25: Nhập vào một list số nguyên L, hãy đưa các số chẵn trong list về đầu list, số lẻ về cuối list và các phần tử 0 nằm ở giữa
Bài 26: Nhập vào một list số nguyên L, hãy biến đổi L bằng cách thay đổi vị trí giữa giá trị nhỏ nhất và lớn nhất
Bài 27: Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy tìm và in ra chuỗi có độ dài lớn nhất và số nguyên có giá trị nhỏ nhất
Bài 28: Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy kiểm tra các phần tử trong L có phải là chuỗi và số xen kẽ nhau không, nếu có thì ta tiến hành tạo một list K mới có các phần tử như sau:
K[i/2] = L[i]*L[i+1] (với i chẵn) 
Bài 29: Nhập vào một list L có các phần tử là chuỗi (các chuỗi này không có ký tự đặc biệt, dấu câu, ký tự số, chỉ có ký tự chữ cái và khoảng trắng)
Hãy tìm ra vị trí của chuỗi có nhiều từ nhất
Bài 30: Nhập vào một list L có các phần tử là chuỗi.
Hãy tìm ra chuỗi có vị trí ký tự in hoa lớn nhất
Bài 31:Đề bài: Lấy một list, ví dụ như sau:
a = [1, 1, 2, 3, 5, 9, 12, 23, 35, 56, 88]
Viết một chương trình in ra tất cả các phần tử có giá trị nhỏ hơn 5. Ngoài ra, bạn có thể làm thêm các yêu cầu sau:
Thay vì in từng phần tử một, hãy in ra một list mới có tất cả các phần tử nhỏ hơn 5 từ list a ban đầu.
Khi hỏi thêm người dùng một con số khác (số X), chương trình có thể trả lại một list mới có chứa các phần tử nhỏ hơn X từ list a ban đầu.
Bài 32:Đề bài: Lấy hai lists, ví dụ như sau:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Viết chương trình cho ra một list chỉ chứa những phần tử chung giữa các list đã cho (không được trùng nhau). Đảm bảo rằng chương trình có thể hoạt động trên hai lists có kích thước khác nhau. Bạn cần sử dụng ít nhất một List Comprehension (List Comprehension là cách viết code ngắn gọn để tạo một danh sách phức tạp).
Bài 33:Đề bài: Viết một chương trình (sử dụng các hàm) yêu cầu người dùng cung cấp một chuỗi dài chứa nhiều từ. In lại cho người dùng một chuỗi mới với thứ tự từ ngữ được đảo ngược lại với list ban đầu. Ví dụ, khi người dùng nhập chuỗi:
My name is Got It-ian
thì họ sẽ nhận lại được một kết quả như sau:
Got It-ian is name My
Bài 34:Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái , chữ số, chữ hoa, chữ thường  trong câu đó. Giả sử đầu vào sau được cấp cho chương trình: Hello World! 123
Thì đầu ra sẽ là:
Số chữ cái là: 10
Số chữ hoa là : 2
Số chữ thường là : 8
Số chữ số là: 3
Bài 35:Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển.
Định dạng nhật ký được hiển thị như sau:
D 100
W 200
(D là tiền gửi, W là tiền rút ra).
Giả sử đầu vào được cung cấp là:
D 300
D 300
W 200
D 100
Thì đầu ra sẽ là:
500
Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
Bài 36:Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là string, age và height là number. Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp là:
Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là tên > tuổi > điểm.
Nếu đầu vào là:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Thì đầu ra sẽ là:
[(‘John’, ’20’, ’90’), (‘Jony’, ’17’, ’91’), (‘Jony’, ’17’, ’93’), (‘Json’, ’21’, ’85’), (‘Tom’, ’19’, ’80’)]
Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
Sử dụng itemgetter để chấp nhận nhiều key sắp xếp.
