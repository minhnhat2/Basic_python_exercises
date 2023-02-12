Link bài tập : https://sites.google.com/view/pythonwithnhat/trang-ch%E1%BB%A7

Bài 1:Nhập 2 số a và b , tính tổng, hiệu, tích và thương 2 số đó biết a bằng 10 và b bằng 5 python
a = 10
b = 5 
# Tính tổng
tong = a + b
print("Tổng của a và b là:", tong)
# Tính hiệu
hieu = a - b
print("Hiệu của a và b là:", hieu)
# Tính tích
tich = a * b
print("Tích của a và b là:", tich)
# Tính thương
thuong = a / b
print("Thương của a và b là:", thuong)

Bài 2:Nhập vào nhiệt độ F, in ra nhiệt độ C
# Nhập vào nhiệt độ F
F = float(input("Nhập vào nhiệt độ F: ")) #float vì dữ liệu đầu vào có thể là phân số hoặc số âm
# Chuyển đổi nhiệt độ F sang độ C
C = (F - 32) * 5/9
# In ra nhiệt độ C
print("Nhiệt độ C tương đương là:", C)

Bài 3:Nhập vào đơn vị tiền Việt Nam , in ra giá trị sau khi quy đổi sang tiền Đô La
# Nhập vào số tiền Việt Nam
vnd = float(input("Nhập vào số tiền Việt Nam: "))
# Tỷ giá hối đoái
ty_gia = 23000
# Quy đổi đồng VND sang đô la
usd = vnd / ty_gia
# In ra giá trị sau khi quy đổi sang đô la
print("Giá trị sau khi quy đổi sang đô la là:", usd)

Bài 4:Nhập vào số n, hãy nhân n lên cho 3, rồi cộng 1 sau đó in kết quả ra màn hình
# Nhập vào số n
n = float(input("Nhập vào số n: "))
# Tính toán
result = n * 3 + 1
# In ra kết quả
print("Kết quả là:", result)

Bài 5:Nhập vào số n, hãy mũ 2 rồi chia cho 3, sau đó in kết quả ra màn hình
# Nhập vào số n
n = float(input("Nhập vào số n: "))
# Tính toán
result = (n ** 2) / 3
# In ra kết quả
print("Kết quả là:", result)

Bài 6.Nhập vào nhiệt độ c, in ra nhiệt độ F
# Nhập vào nhiệt độ C
celsius = float(input("Nhập vào nhiệt độ C: "))
# Tính toán nhiệt độ F
fahrenheit = (celsius * 9 / 5) + 32
# In ra nhiệt độ F
print("Nhiệt độ F là:", fahrenheit)

Bài 7.Nhập vào một số nguyên a, nếu a chia hết cho 2 thì in ra True, ngược lại in ra False
# Nhập vào số nguyên a
a = int(input("Nhập vào số nguyên a: "))
# Kiểm tra a có chia hết cho 2 không
if a % 2 == 0:
    print("True")
else:
    print("False")

Bài 8.Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ 50 - 100 thì in ra True, ngược lại in ra False
# Nhập vào số nguyên a
a = int(input("Nhập vào số nguyên a: "))
# Kiểm tra a có đạt điều kiện chia hết cho 3 và nằm trong khoảng từ 50 - 100 không
if a % 3 == 0 and 50 <= a <= 100:
    print("True")
else:
    print("False")

Bài 9.Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
# Nhập vào số nguyên a
a = int(input("Nhập vào số nguyên a: "))
# Kiểm tra a có đạt điều kiện chia hết cho 5 và KHÔNG nằm trong khoảng từ 20 - 70 không
if a % 5 == 0 and (a < 20 or a > 70):
    print("True")
else:
    print("False")

Bài 10.Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
# Nhập vào nguyên a và b
a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
# Kiểm tra xem có một trong hai số a và b chia hết cho 2 không
if a % 2 == 0 or b % 2 == 0:
    print("True")
else:
    print("False")

Bài 11.Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False
# Nhập vào số thực a
a = float(input("Nhập vào số thực a: "))
# Kiểm tra xem a có phải là số nguyên hay không
if int(a) == a:
    print("True")
else:
    print("False")

Bài 12.Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False
# Nhập vào số nguyên a
a = int(input("Nhập vào số nguyên a: "))
# Kiểm tra xem a có phải là số chính phương hay không
root = int(a**0.5)
if root**2 == a:
    print("True")
else:
    print("False")
    
Bài 13.Nhập vào lương tháng này nhận được, ta phải đưa cho vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại
luong = float(input("Nhập vào lương tháng này: "))
luong_giu_lai = luong * (1 - 0.9)
print("Lương giữ lại:", luong_giu_lai)

Bài 14.Nhập vào số thực a, kiểm tra xem a có phải là số nguyên tố hay không, nếu có thì in ra True, ngược lại in ra False
a = int(input("Nhập vào số thực a: "))
if a > 1:
    for i in range(2, int(a**(1/2)) + 1):
        if (a % i) == 0:
            print("False")
            break
    else:
        print("True")
else:
    print("False")

Bài 15.Nhập vào số thực a, kiểm tra xem a có phải là số nguyên tố chẵn hay không, nếu có thì in ra True, ngược lại in ra False
a = int(input("Nhập vào một số nguyên a: "))
if a > 2:
  for i in range(2, int(a**(1/2))+1):
    if a % i == 0:
      print("False")
      break
  else:
    if a % 2 == 0:
      print("True")
    else:
      print("False")
else:
  print("False")

Bài 16.Nhập vào số nguyên dương a, nếu a lớn hơn 10 thì ta in ra đây là số lớn hơn 10
a = int(input("Nhập vào số nguyên dương a: "))
if a > 10:
    print("Đây là số lớn hơn 10")

Bài 17.Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ
a = int(input("Nhập vào số nguyên dương a: "))
if a % 2 == 0:
  print("Đây là số chẵn")
else:
  print("Đây là số lẻ")

Bài 18.Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
a = float(input("Nhập vào số thực a: "))
b = float(input("Nhập vào số thực b: "))
c = float(input("Nhập vào số thực c: "))
if (a + b > c) and (b + c > a) and (c + a > b):
    print("a, b, c cấu thành độ dài của 1 tam giác")
else:
    print("a, b, c không cấu thành độ dài của 1 tam giác")

Bài 19.Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, kiểm tra xem đó là tam giác gì (tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường)
a = float(input("Nhập số thực dương a: "))
b = float(input("Nhập số thực dương b: "))
c = float(input("Nhập số thực dương c: "))
if a + b > c and a + c > b and b + c > a:
    print("Đây là tam giác")
    if a == b == c:
        print("Đây là tam giác đều")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông")
    elif a == b or a == c or b == c:
        if a**2 + b**2 > c**2 and b**2 + c**2 > a**2 and a**2 + c**2 > b**2:
            print("Đây là tam giác cân")
        else:
            print("Đây là tam giác thường")
    else:
        print("Đây là tam giác thường")
else:
    print("Đây không phải là tam giác")

Bài 20.Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
numbers = [a, b, c]
numbers.sort()
print("Thứ tự tăng dần của a, b, c là: ", numbers)

Bài 21.Giải và biện luận phương trình ax + b = 0
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
    print("Nghiệm của phương trình là:", x)

Bài 22.Giải và biện luận phương trình ax^2 + bx + c = 0
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    x = -b / (2 * a)
    print("Phương trình có nghiệm kép x =", x)
else:
    sqrt_delta = delta**0.5
    x1 = (-b + sqrt_delta) / (2 * a)
    x2 = (-b - sqrt_delta) / (2 * a)
    print("Phương trình có 2 nghiệm phân biệt: x1 =", x1, "và x2 =", x2)

Bài 23.Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    num_of_days = 31
elif month in (4, 6, 9, 11):
    num_of_days = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        num_of_days = 29
    else:
        num_of_days = 28
print("Tháng %d năm %d có %d ngày." % (month, year, num_of_days))

Bài 24.Ngày vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày (giả sư năm đó không phải là năm nhuận)
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    num_of_days = 31
elif month in (4, 6, 9, 11):
    num_of_days = 30
else:
    num_of_days = 28
days_from_start = 0
for i in range(1, month):
    if i in (1, 3, 5, 7, 8, 10, 12):
        days_from_start += 31
    elif i in (4, 6, 9, 11):
        days_from_start += 30
    else:
        days_from_start += 28
days_from_start += day
print("Ngày nhập vào cách ngày đầu năm %d ngày." % days_from_start)

Bài 25.Nhập điểm toán, văn, anh.
Nếu điểm đúng quy tắc (trong khoảng từ 0 - 10), ta tính điểm trung bình rồi tiến hành xét:
Nếu điểm trung bình lớn hơn hoặc bằng 8, toán hoặc văn lớn hơn hoặc bằng 8 và không có điểm nào dưới 6.5 thì in ra “Học sinh giỏi”
Nếu không đủ điều kiện học sinh giỏi ta xét nếu điểm trung bình lớn hơn hoặc bằng 6.5, toán hoặc văn lớn hơn hoặc bằng 6.5 và không có điểm nào dưới 5 thì in ra “Học sinh khá”
Nếu không đủ điều kiện học sinh khá ta xét nếu điểm trung bình lớn hơn hoặc bằng 5, toán hoặc văn lớn hơn hoặc bằng 5 và không có điểm nào dưới 3.5 thì in ra “Học sinh trung bình”
Nếu không đủ điều kiện học sinh trung bình ta xét nếu điểm trung bình lớn hơn hoặc bằng 3.5, toán hoặc văn lớn hơn hoặc bằng 3.5 và không có điểm nào dưới 2 thì in ra “Học sinh yếu”
Nếu không đủ điều kiện học sinh yếu ta in ra “Học sinh kém”

toan = float(input("Nhập điểm toán: "))
van = float(input("Nhập điểm văn: "))
anh = float(input("Nhập điểm anh: "))
if 0 <= toan <= 10 and 0 <= van <= 10 and 0 <= anh <= 10:
    diem_trung_binh = (toan + van + anh) / 3
    if diem_trung_binh >= 8 and toan >= 8 and van >= 8 and anh >= 8 and toan >= 6.5 and van >= 6.5 and anh >= 6.5:
        print("Học sinh giỏi")
    elif diem_trung_binh >= 6.5 and (toan >= 6.5 or van >= 6.5 or anh >= 6.5) and toan >= 5 and van >= 5 and anh >= 5:
        print("Học sinh khá")
    elif diem_trung_binh >= 5 and (toan >= 5 or van >= 5 or anh >= 5) and toan >= 3.5 and van >= 3.5 and anh >= 3.5:
        print("Học sinh trung bình")
    elif diem_trung_binh >= 3.5 and (toan >= 3.5 or van >= 3.5 or anh >= 3.5) and toan >= 2 and van >= 2 and anh >= 2:
        print("Học sinh yếu")
    else:
        print("Học sinh kém")
else:
    print("Nhập sai điểm")

Bài 26 : Viết chương trình trò chơi kéo búa bao (2 player)
print("Trò chơi Kéo-Búa-Bao")

while True:
    player1 = input("Người chơi 1: Chọn Kéo (K), Búa (B) hoặc Bao (O): ")
    player2 = input("Người chơi 2: Chọn Kéo (K), Búa (B) hoặc Bao (O): ")

    if player1 == player2:
        print("Hòa!")
    elif player1 == "K" and player2 == "B":
        print("Người chơi 1 thắng!")
    elif player1 == "B" and player2 == "O":
        print("Người chơi 1 thắng!")
    elif player1 == "O" and player2 == "K":
        print("Người chơi 1 thắng!")
    else:
        print("Người chơi 2 thắng!")
    play_again = input("Bạn muốn chơi lại không (C/K): ")
    if play_again == "K":
        break

Bài 27: giống bài 26 nhưng 1 người chơi 
print("Trò chơi Kéo-Búa-Bao")
print("1. Kéo")
print("2. Búa")
print("3. Bao")
player_choice = int(input("Mời bạn chọn (1/2/3): "))
import random
computer_choice = random.randint(1,3)
if (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 3) or (player_choice == 3 and computer_choice == 1):
    print("Bạn thắng!")
elif player_choice == computer_choice:
    print("Hòa!")
else:
    print("Bạn thua!")


Bài 28: Một set tennis sẽ kết thúc khi có người đạt tới 6 điểm trước. Tuy nhiên nếu cả hai đang hòa nhau 5-5 trong một set thì set phải đánh tới điểm thứ 7 mới kết thúc. Bạn hãy viết chương trình xét xem hai số tự nhiên có phải tỷ số của một set tennis hay không
INPUT
Hai số tự nhiên
OUTPUT
Số 1 nếu đó là tỷ số của một set tennis. Ngược lại output số 0.
VÍ DỤ
input:5 6
output:0
input:6 4
output:1

score1 = int(input("Nhập số điểm cho người chơi 1: "))
score2 = int(input("Nhập số điểm cho người chơi 2: "))
if ((score1 >= 6 or score2 >= 6) and abs(score1 - score2) >= 2):
    print(1)
elif ((score1 == 6 or score2 == 6) and abs(score1 - score2) == 1):
    print(1)
else:
    print(0)

Bài 29:Các bạn hãy viết chương trình nhập một năm bất kỳ cho biết năm đó năm con gì.
INPUT
Một con số nguyên khác 0 có trị tuyệt đối không quá 1 tỷ. Đây là năm cần xét, năm trước công nguyên được quy ước ghi bằng số âm và năm sau công nguyên quy ước ghi bằng số dương.
OUTPUT
Cho biết năm đó là năm con gì, ghi chữ hoa toàn bộ, không dấu. Biết rằng 12 con giáp có các con:
TY'
SUU
DAN
MEO
THIN
TY.
NGO
MUI
THAN
DAU
TUAT
HOI
(Chú ý dấu nháy đơn sau con Tý và dấu chấm câu sau con Tỵ)
VÍ DỤ
input:2015
output:MÙI
input:1968
output:THAN
input:40
output:TY'
input:-208
output:TY.
input:1985
output:SỬU

animals = ['TY\'', 'SUU', 'DAN', 'MEO', 'THIN', 'TY.', 'NGO', 'MUI', 'THAN', 'DAU', 'TUAT', 'HOI']
year = int(input("Nhập vào năm: "))
print(animals[(year - 4) % 12])


Bài 30: Nhập ngày/tháng/năm của ngày sinh và hiện tại, tính tổng số ngày từ ngày sinh đến hiện tại 
import time
birthday = input("Nhập ngày sinh (dd/mm/yyyy): ")
current_date = input("Nhập ngày hiện tại (dd/mm/yyyy): ")
birthday = time.strptime(birthday, '%d/%m/%Y')
current_date = time.strptime(current_date, '%d/%m/%Y')
birthday_timestamp = int(time.mktime(birthday))
current_timestamp = int(time.mktime(current_date))
days = (current_timestamp - birthday_timestamp) / (24 * 60 * 60)
print("Tổng số ngày từ ngày sinh đến hiện tại:", int(days))
