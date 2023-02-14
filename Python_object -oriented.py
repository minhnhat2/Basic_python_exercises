Link bài tập :https://sites.google.com/view/pythonwithnhat/trang-ch%E1%BB%A7

Bài 1 :Viết hàm đưa vào 2 số nguyên, số nào lớn hơn thì in bảng cửu chương của số đó
  
def print_times_table(num1, num2):
    max_num = max(num1, num2)
    for i in range(1, 11):
        print(f"{max_num} x {i} = {max_num * i}")
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
print_times_table(num1, num2)


Bài 2:Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số nguyên tố hay không
  
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
a = int(input("Nhập một số nguyên: "))
if is_prime(a):
    print(f"{a} là số nguyên tố")
else:
    print(f"{a} không phải là số nguyên tố")

Bài 3:Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số Armstrong hay không
  
def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for char in num_str:
        sum += int(char)**num_len
    return sum == num
a = int(input("Nhập một số nguyên: "))
if is_armstrong(a):
    print(f"{a} là số Armstrong")
else:
    print(f"{a} không phải là số Armstrong")

Bài 4:Viết hàm đưa vào 1 list số nguyên, tìm và trả về vị trí có giá trị lớn nhất trong list
  
def find_max_index(numbers):
    max_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[max_index]:
            max_index = i
    return max_index

numbers = list(map(int, input("Nhập các số nguyên cách nhau bằng dấu cách: ").split()))
max_index = find_max_index(numbers)
print(f"Vị trí có giá trị lớn nhất trong list là {max_index} với giá trị {numbers[max_index]}")

Bài 5:Viết hàm đưa vào một list số nguyên và một số nguyên dương k. Hãy tìm và trả về vị trí của phần tử đầu tiên có giá trị k trong list số nguyên, nếu không có thì trả về -1
def find_first_index(numbers, k):
    for i, value in enumerate(numbers):
        if value == k:
            return i
    return -1
# Cho người dùng nhập dữ liệu vào cho list số nguyên
numbers_input = input("Nhập vào một list số nguyên, các số cách nhau bởi dấu phẩy: ")
numbers = [int(x) for x in numbers_input.split(",")]
# Cho người dùng nhập dữ liệu vào cho số nguyên k
k = int(input("Nhập vào một số nguyên dương: "))
# Gọi hàm với một list số nguyên và một số nguyên
print(find_first_index(numbers, k))

Bài 6:Viết hàm đưa vào 1 list có các phần tử là chuỗi, tìm và trả về chuỗi ngắn nhất trong list

def find_shortest_string(strings):
    shortest_string = strings[0]
    for string in strings[1:]:
        if len(string) < len(shortest_string):
            shortest_string = string
    return shortest_string
strings = input("Nhập các chuỗi cách nhau bằng dấu cách: ").split()
shortest_string = find_shortest_string(strings)
print(f"Chuỗi ngắn nhất trong list là: {shortest_string}")

Bài 7:Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tính và trả về giá trị trung bình của a phần tử đầu tiên trong L
  
def average_of_first_n_elements(numbers, n):
    first_n_elements = numbers[:n]
    total = 0
    for number in first_n_elements:
        total += number
    return total / n

numbers = list(map(int, input("Nhập danh sách số nguyên cách nhau bằng dấu cách: ").split()))
a = int(input("Nhập số nguyên dương a: "))
average = average_of_first_n_elements(numbers, a)
print(f"Giá trị trung bình của {a} phần tử đầu tiên trong danh sách là: {average}")

Bài 8:Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tìm và trả về một list mới có số phần tử là a, giá trị các phần tử là các số nguyên tố tìm được trong list L

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def find_first_n_prime_numbers(numbers, n):
    prime_numbers = []
    count = 0
    for number in numbers:
        if is_prime(number) and count < n:
            prime_numbers.append(number)
            count += 1
    return prime_numbers
numbers = list(map(int, input("Nhập danh sách số nguyên cách nhau bằng dấu cách: ").split()))
a = int(input("Nhập số nguyên dương a: "))
prime_numbers = find_first_n_prime_numbers(numbers, a)
print(f"Danh sách {a} số nguyên tố đầu tiên trong danh sách là: {prime_numbers}")

Bài 9:Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tìm và trả về giá trị lớn thứ a trong list L (nếu a = 1 thì tìm giá trị lớn nhất, a = 2 thì tìm giá trị lớn nhì, a = 3 thì tìm giá trị lớn ba,...)

def find_a_largest_number(L, a):
    L.sort(reverse=True)
    return L[a-1]
  
Bài 10:Viết hàm đưa vào 1 dictionary có các phần tử có giá trị là số nguyên, tìm và trả về key có giá trị lớn nhất

def find_max_key(d):
    max_key = None
    max_val = float('-inf')
    for key, val in d.items():
        if val > max_val:
            max_val = val
            max_key = key
    return max_key
# Nhập thông tin từ người dùng để tạo dictionary
d = {}
n = int(input("Nhập số phần tử muốn thêm vào dictionary: "))
for i in range(n):
    key = input(f"Nhập key cho phần tử thứ {i+1}: ")
    val = int(input(f"Nhập giá trị cho phần tử thứ {i+1}: "))
    d[key] = val
# Tìm key có giá trị lớn nhất trong dictionary
max_key = find_max_key(d)
# In key có giá trị lớn nhất ra màn hình
if max_key is not None:
    print(f"Key có giá trị lớn nhất trong dictionary là '{max_key}' với giá trị {d[max_key]}.")
else:
    print("Dictionary rỗng.")

Bài 11 :Viết hàm đưa vào 1 dictionary có các phần tử có key là chuỗi, tìm và trả về giá trị của key có độ dài lớn nhất

def find_longest_key(d):
    longest_key = None
    longest_len = 0
    for key in d:
        if len(key) > longest_len:
            longest_len = len(key)
            longest_key = key
    if longest_key is not None:
        return d[longest_key]
    else:
        return None
# Nhập thông tin từ người dùng để tạo dictionary
d = {}
n = int(input("Nhập số phần tử muốn thêm vào dictionary: "))
for i in range(n):
    key = input(f"Nhập key cho phần tử thứ {i+1}: ")
    val = input(f"Nhập giá trị cho phần tử thứ {i+1}: ")
    d[key] = val
# Tìm giá trị của key có độ dài lớn nhất trong dictionary
longest_val = find_longest_key(d)
# In giá trị của key có độ dài lớn nhất ra màn hình
if longest_val is not None:
    print(f"Giá trị của key có độ dài lớn nhất trong dictionary là '{longest_val}'.")
else:
    print("Dictionary rỗng.")

Bài 12:Viết hàm có tham số đầu vào là một list L có các phần tử là chuỗi. Hãy tạo ra một dictionary D mã hóa, với mỗi một phần tử trong L được mã hóa thành một con số (theo thứ tự từ 0 tăng dần lên 1 đơn vị). Sau đó trả về list đã được mã hóa
Ví dụ:
Cho
L = ["đen","vàng","xanh","vàng","xanh","đỏ","hồng"]
Xây dựng dictionary mã hóa:
D = {'đen':0,'vàng':1,'xanh':2,'đỏ':3,'hồng':4}
Trả về List mã hóa:
L_mahoa = [0, 1, 2, 1, 2, 3, 4]

def encode_list(L):
    # Tạo một dictionary mã hóa
    encoding_dict = {}
    for item in L:
        if item not in encoding_dict:
            encoding_dict[item] = len(encoding_dict)
    # Sử dụng list comprehension để mã hóa list
    encoded_list = [encoding_dict[item] for item in L]
    # Trả về list đã được mã hóa
    return encoded_list
# Sử dụng hàm encode_list để mã hóa list L
L = ["đen", "vàng", "xanh", "vàng", "xanh", "đỏ", "hồng"]
L_mahoa = encode_list(L)
# In list đã được mã hóa
print(L_mahoa)

Bài 13:Viết hàm có tham số đầu vào là một dictionary, hãy tạo một dictionary mới hoán đổi giá trị và key của dictionary đầu vào, rồi trả về dicionary mới đó. Nếu sau khi hoán đổi có 2 key trùng nhau (do dictionary đầu vào có 2 giá trị trùng nhau), hàm trả về None

def exchange_dict(d):
    # Tạo một dictionary mới để hoán đổi key và value
    new_dict = {v: k for k, v in d.items()}
    # Kiểm tra xem new_dict có trùng key hay không
    if len(new_dict) != len(d):
        return None
    else:
        return new_dict
# Sử dụng hàm exchange_dict để hoán đổi key và value của dictionary
d = {'a': 1, 'b': 2, 'c': 3}
new_dict = exchange_dict(d)
# In dictionary mới hoán đổi key và value
print(new_dict)

Bài 14:Một nhà hàng có các món ăn: Gà rán, hamburger, cocacola
Giá của gà rán là: 30.000đ
Giá của hamburger là: 25.000đ
Giá của cocacola là: 10.000đ
Yêu cầu người dùng nhập vào số lượng từng món ăn.
Sau đó in ra hóa đơn theo dạng như sau:
Chào mừng các bạn đến với nhà hàng thức ăn nhanh!
Mời bạn nhập số lượng từng món ăn:Gà rán: 2
Hamburger: 3
Cocacola: 5Hóa đơn:
Gà rán30.000đ x 2
Hamburger25.000đ x 3
Cocacola10.000đ x 5Tổng:
Gà rán60.000đ
Hamburger75.000đ
Cocacola50.000đ
Tổng trước thuế185.000đ
Thuế(5%)9.250đ
Tổng sau thuế194.250đ
Phần bên trái có số ký tự là 20 ký tự

def print_bill():
    # Giá của từng món ăn
    menu = {'Gà rán': 30000, 'Hamburger': 25000, 'Cocacola': 10000}

    # Yêu cầu người dùng nhập số lượng từng món ăn
    order = {}
    for item in menu:
        quantity = int(input(f'Mời bạn nhập số lượng {item}: '))
        order[item] = quantity
    # In ra hóa đơn
    print('Chào mừng các bạn đến với nhà hàng thức ăn nhanh!')
    print('Mời bạn nhập số lượng từng món ăn:')
    for item, price in menu.items():
        qty = order[item]
        subtotal = price * qty
        print(f'{item: <20}{price: >10,}đ x {qty: <5}{subtotal: >20,}đ')
    # Tính tổng tiền
    total = sum(menu[item] * order[item] for item in menu)
    # In tổng tiền
    print('Tổng:')
    for item, price in menu.items():
        qty = order[item]
        subtotal = price * qty
        print(f'{item: <20}{subtotal: >20,}đ')
    print(f'Tổng trước thuế:{total: >16,}đ')
    tax = total * 0.05
    print(f'Thế (5%):{tax: >28,.0f}đ')
    total_after_tax = total + tax
    print(f'Tổng sau thuế:{total_after_tax: >23,}đ')
# Gọi hàm in hóa đơn
print_bill()

Bài 15:Viết hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên dương k. Hãy tạo và trả về một list L_kq có các phần tử là giá trị của phần tử xuất hiện nhiều hơn k lần trong list L theo thứ tự tăng dần

def find_elements_appear_more_than_k_times(L, k):
    counts = {}
    for x in L:
        counts[x] = counts.get(x, 0) + 1
    L_kq = []
    for x in sorted(counts.keys()):
        if counts[x] > k:
            L_kq.append(x)
    return L_kq
# Nhập dữ liệu
L = []
while True:
    x = input("Nhập số nguyên dương (nhập q để dừng): ")
    if x == "q":
        break
    else:
        L.append(int(x))
k = int(input("Nhập giá trị k: "))
# Tìm các phần tử xuất hiện nhiều hơn k lần
L_kq = find_elements_appear_more_than_k_times(L, k)
# In kết quả
print("Các phần tử xuất hiện nhiều hơn", k, "lần trong list là:", L_kq)

Bài 16:Viết hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên dương k. Tìm và trả về đoạn list dài nhất trong L có giá trị trung bình là k

def longest_sublist_with_average_k(L, k):
    # Tính các đoạn liên tiếp trong L có giá trị trung bình bằng k
    sublists = []
    for i in range(len(L)):
        for j in range(i+1, len(L)+1):
            sublist = L[i:j]
            if sum(sublist) / len(sublist) == k:
                sublists.append(sublist)
    # Tìm đoạn dài nhất
    longest_sublist = []
    for sublist in sublists:
        if len(sublist) > len(longest_sublist):
            longest_sublist = sublist
    return longest_sublist
# Nhập giá trị đầu vào
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
# Tìm đoạn dài nhất có giá trị trung bình bằng k
longest_sublist = longest_sublist_with_average_k(L, k)
# In kết quả
print("Đoạn dài nhất có giá trị trung bình bằng", k, "là", longest_sublist)

Bài 17:Một người dùng số tiền là U đô-la và V Euro để mua một loại nguyên liệu sản xuất.
Có N công ty nước ngoài bán nguyên liệu trên được đánh số từ 1 đến N. Công ty thứ i có giá bán Ai đô la/1 kg nguyên liệu và Bi Euro/1 kg nguyên liệu.
Tuy nhiên, tại mỗi công ty chỉ bán nguyên liệu cho một khách hàng hoặc theo đô-la, hoặc theo Euro.
Hãy giúp người đó tìm cách chọn ra 2 công ty để mua hàng sao cho số lượng nguyên liệu sản xuất có thể mua được là nhiều nhất.
Nhập vào: U, V và List A và List B
In ra: Số lượng nguyên liệu S (kg) người đó mua được với 2 chữ số thập phân.

# Hàm tính số lượng nguyên liệu tối đa có thể mua được với U đô-la và V Euro
def max_quantity(U, V, A, B):
    max_q = 0  # Số lượng nguyên liệu tối đa có thể mua được
    n = len(A)  # Số lượng công ty bán nguyên liệu
    for i in range(n):
        for j in range(i + 1, n):
            # Nếu hai công ty bán khác loại tiền tệ
            if (A[i] >= U and B[i] < V) or (A[i] < U and B[i] >= V):
                if (A[j] >= U and B[j] < V) or (A[j] < U and B[j] >= V):
                    # Tính số lượng nguyên liệu tối đa mua được ở hai công ty
                    q = min(U / A[i], V / B[i]) + min(U / A[j], V / B[j])
                    if q > max_q:
                        max_q = q
    return '{:.2f}'.format(max_q)
# Nhập giá trị đầu vào
U = float(input("Nhập số tiền đô-la của bạn: "))
V = float(input("Nhập số tiền Euro của bạn: "))
n = int(input("Nhập số lượng công ty bán nguyên liệu: "))
A = []
B = []
for i in range(n):
    ai, bi = input("Nhập giá bán của công ty {}: ".format(i+1)).split()
    A.append(float(ai))
    B.append(float(bi))
# Tính và in ra số lượng nguyên liệu tối đa có thể mua được
max_quantity = max_quantity(U, V, A, B)
print("Số lượng nguyên liệu tối đa có thể mua được là:", max_quantity, "kg")

Bài 18:Phỏng đoán COLLATZ
Giả sử ta có một số n
Phỏng đoán COLLATZ hoạt động như sau:
Nếu n là số chẵn, thì ta chia n cho 2 (n/2)
Nếu n là số lẻ, thì ta nhân n cho 3 rồi + 1 (3n + 1)
Phỏng đoán hoạt động cho đến khi nào n = 1
Yêu cầu:
Nhập vào số nguyên dương m, hãy in ra dãy phỏng đoán COLLATZ từ 1 đến m (mỗi một phỏng đoán ta in trên 1 dòng, mỗi một số cách nhau một dấu phẩy)
Ví dụ:
Nhập: m = 6
In ra:
1
2,1
3,10,5,16,8,4,2,1
4,2,1
5,16,8,4,2,1
6,3,10,5,16,8,4,2,1

def collatz(n):
    seq = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq
def collatz_sequence(m):
    for i in range(1, m + 1):
        seq = collatz(i)
        print(','.join(str(x) for x in seq))
m = int(input("Nhap vao so nguyen duong m: "))
collatz_sequence(m)

Bài 19:Một khách sạn có N phòng đôi được đánh số từ 1 đến N và M đoàn khách.
Với mỗi đoàn khách, ta xếp mỗi cặp khách của đoàn vào một phòng trống theo thứ tự phòng tăng dần.
Nếu đoàn khách có số người lẻ thì người khách cuối cùng được xếp vào một phòng trống tiếp theo.
Nếu đã hết phòng còn trống thì ta sẽ xếp khách vào những phòng mới chỉ có 1 khách theo thứ tự phòng tăng dần.
In ra số khách của mỗi phòng sau khi xếp.
Giả sử không có 2 đoàn khách nào đến cùng một lúc.
Ví dụ 1:
N = 7, M = 3
doankhach = [3,7,3]
Ta in: 2, 2, 2, 2, 2, 1, 2
Ví dụ 2:
N = 5, M = 3
doankhach = [2,3,2]
Ta in: 2, 2, 1, 2, 0

N, M = map(int, input().split())
doankhach = list(map(int, input().split()))
rooms = [0] * N
for i in range(M):
    p = doankhach[i]
    for j in range(N):
        if p == 0:
            break
        if rooms[j] == 0:
            rooms[j] = 2
            p -= 2
        elif rooms[j] == 1:
            rooms[j] += 1
            p -= 1
for i in range(N):
    if rooms[i] == 0:
        print(0)
    else:
        print(rooms[i])

Bài 20:Cho số tự nhiên n được nhập vào từ bàn phím, bạn hãy viết hàm kiểm tra xem n có phải là số nguyên tố không, nếu có trả về True, ngược lại trả về False.
Số nguyên tố là các số tự nhiên mà chỉ có 2 ước là 1 và chính nó. Ví dụ: 2, 3, 5, 7, 11, 13, 17,... là các số nguyên tố.
Ví dụ:
Nếu bạn nhập n = 9 thì màn hình sẽ hiển thị ra False
Nếu bạn nhập n = 3 thì màn hình sẽ hiển thị ra True

def is_prime(n):
    a=0 
    for i in range(1,n+1):
      if n%i==0:
        a+=1
    if a==2:
      return True
    return False
n = int(input())
print(is_prime(n))

Bài 21 :Cho trước list res là list chứa các phần tử integer được nhập từ bàn phím. Viết chương trình Python để tìm ra các phần tử chẵn trong list đó. Kế tiếp, in kết quả là một list các số chẵn ra màn hình.
Ví dụ: 
với res = [1,2,3,4,5,6,7,8,9] thì hiển thị là [2,4,6,8]
với res = [10, 22, 33, 45, 79, 81] thì hiển thị là [10,22]
Đầu vào: res là số nguyên được nhập từ bàn phím
Đầu ra: Hiển thị ra màn hình theo yêu cầu của đề
ví dụ :
input: [1,2,3]
output : [2]

res = []
lengths = int(input())
for i in range(lengths):
    n = int(input())
    res.append(n)
def evenNum(res):
    return[x for x in res if x % 2 ==0]
print(evenNum(res))

Bài 22:Cho 3 số nguyên a, b và c là 3 cạnh của một tam giác. Viết chương trình để kiểm tra xem tam giác đó là tam giác đều, tam giác cân hay tam giác thường và in ra màn hình kết quả  "Equilateral triangle", "Isosceles triangle" hoặc "Scalene triangle" tương ứng.
Ví dụ:
Với a = 20, b = 20, c = 20 thì kết quả hiển thị là "Equilateral triangle"
Với a = 33, b = 20, c = 15 thì kết quả hiển thị là "Scalene triangle"
Đầu vào: 3 số nguyên được nhập từ bàn phím
Đầu ra: Hiển thị ra màn hình theo yêu cầu đề bài
Gợi ý
Hoàn thành bài tập này bằng cách dùng câu lệnh điều kiện if else đơn giản
Note:
+ Một tam giác được gọi là tam giác đều khi tam giác đó có 3 cạnh bằng nhau
+ Một tam giác được gọi là tam giác cân khi tam giác đó có ít nhất hai cạnh bằng nhau
+ Một tam giác được gọi là tam giác thường khi tam giác có 3 cạnh cấu thành thoả điều kiện là tam giác 

a = int(input())
b = int(input())
c = int(input())
typesOfTriangle = ['Scalene triangle', 'Isosceles triangle', 'Equilateral triangle']
typeTriangle = typesOfTriangle[0]
lst = []
Equal = 0
lst.append(a)
lst.append(b)
lst.append(c)
for i in range(len(lst)):
    if lst.count(a) > 1:
        Equal += 1
    if Equal == 1:
        typeTriangle = typesOfTriangle[1]
    elif Equal == 2:
        typeTriangle = typesOfTriangle[2]
print(typeTriangle)

Bài 23:Cho trước chuỗi str được nhập từ bàn phím. Viết chương trình Python để tìm ra từ có độ dài lớn hơn 3. Sau đó, in kết quả là mội list các chuỗi thoả mãn điều kiện đó ra màn hình
Ví dụ:
Với str = "You are an awesome man", thì hiển thị là ['awesome']
Với str = "CodeLearn helps you reach your goal", thì hiển thị là ['CodeLearn', 'helps', 'reach', 'your', 'goal']
Đầu vào: str là chuỗi được nhập từ bàn phím
Đầu ra: Hiển thị ra màn hình theo yêu cầu đề bài
Ví dụ:
input:"The quick brown fox jumps over the lazy dog"
output: "['quick', 'brown', 'jumps', 'over', 'lazy']"
Gợi ý
Hoàn thành bài tập này bằng cách viết hàm để kiểm tra các từ trong chuỗi đã cho có độ dài lớn hơn 3. Có thể dùng thêm hàm split() để loại bỏ các khoảng trắng trong chuỗi.

str = str(input())
ans = []
def a(str):
    b = str.split(" ")
    for i in b:
        if len(i) > 3:
            ans.append(i)
    return ans
print(a(str))

Bài 24:Cho trước nlà số nguyên được nhập từ bàn phím. Viết chương trình Python để kiểm tra số đó có phải là số abundant hay là không. Sau đó, in kết quả True hoặc False ra màn hình
Ví dụ:
Với n = 55 thì hiển thị là False
Với n = 66 thì hiển thị là True
Với n = 10 thì hiển thị là False
Đầu vào: n là số tự nhiên được nhập từ bàn phím
Đầu ra: Hiển thị ra màn hình True hoăc False theo yêu cầu đề bài
Gợi ý
Hoàn thành bài tập này bằng cách dùng vòng lặp for
Lưu ý: Trong lĩnh vực lý thuyết số, một số tự nhiên n được gọi là số abundant khi mà tổng các ước số của n (không tính n) lớn hơn n. Ví dụ số 12 có các ước số là 1, 2, 3, 4, 6 có tổng là 1 + 2 + 3 + 4 + 6 = 16 > 12

n = int(input())
def is_abundant(n):
    total = 0
    for i in range(1, n):
        if n%i==0:
            total+=i
    if (total > n):
        print(True)
    else:
        print(False)
is_abundant(n)

Bài 25: Viết chương trình bằng python tính chu vi & diệntích các hình (abstract)
Viết chương trình tính chu vi và điện tích của một số hình như sau:
Hình tròn
Hình chữ nhật
Hình tam giác


Bài 26: Viết chương trình quản lý sinh viên trong Python. Mỗi đối tượng sinh viên có các thuộc tính sau: "id", "tên", "giới tính"," tuổi", "điểm toán", "điểm lý", "điểm hóa","điểm văn" ,  "điểm anh" , "điểm trung bình môn"và "học lực "
Id là mã sinh viên tự động tăng.
Trong các thuộc tính "điểm toán" , "điểm lý" , "điểm hóa", "điểm văn" , "điểm anh" có các cột điểm như "điểm quá trình " , "điểm thực hành" , điểm thi cuối khóa"  và "điểm trung bình" và "đánh giá"
"điểm trung bình" là các được tính như sau :" điểm quá trình" nhân 20% cộng "điểm thực hành " nhân 30% cộng "điểm thi cuối khóa" nhân 50 % 
"điểm trung bình môn " là giá trị trung bình của 5 cột "điểm trung bình" của 5 môn "điểm toán", "điểm lý" , "điểm hóa", "điểm văn" , "điểm anh"  .
" đánh giá" là cột có 2 giá trị là "qua môn" và "rớt môn",  nếu cột "điểm trung bình" của một môn thấp hơn 5 thì sẽ là "rớt môn", còn nếu từ 5 trở lên thì sẽ là "qua môn"
Học lực được tính như sau:
Giỏi: nếu điểm "trung bình môn "lớn hơn hoặc bằng 8.
Khá: nếu điểm "trung bình môn" nhỏ hơn 8 và lớn hơn hoặc bằng 6.5.
Trung Bình: nếu điểm "trung bình môn " nhỏ hơn 6.5 và lớn hơn hoặc bằng 5.
Yếu: nếu điểm "trung bình môn " nhỏ hơn 5.
Yêu cầu: tạo ra một menu với các chức năng sau:
1. Thêm sinh viên.
2. Cập nhật thông tin sinh viên bởi ID.
3. Xóa sinh viên bởi ID.
4. Tìm kiếm sinh viên theo tên.
5. Sắp xếp sinh viên theo điểm trung bình (GPA).
6. Sắp xếp sinh viên theo tên.
6. Sắp xếp sinh viên theo ID.
8. Hiển thị danh sách sinh viên.
