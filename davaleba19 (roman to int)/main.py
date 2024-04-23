class Roman:
    def roman_to_int(self, rome_num):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(rome_num)):
            if i + 1 < len(rome_num) and roman[rome_num[i]] < roman[rome_num[i + 1]]:
                result -= roman[rome_num[i]]
            else:
                result += roman[rome_num[i]]

        return result


r = Roman()
r_to_num = r.roman_to_int("MMCML")
print(r_to_num)