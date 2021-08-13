def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        pop_list = []
        z = 1
        for i in range(len(s)):
            if len(s) > 1:
                if s[i] == 'I' and s[z] == 'V':
                    value += 4
                    pop_list.append('IV')
                elif s[i] == 'I' and s[z] == 'X':
                    value += 9
                    pop_list.append('IX')
                elif s[i] == 'X' and s[z] == 'L':
                    value += 40
                    pop_list.append('XL')
                elif s[i] == 'X' and s[z] == 'C':
                    value += 90
                    pop_list.append('XC')
                elif s[i] == 'C' and s[z] == 'D':
                    value += 400
                    pop_list.append('CD')
                elif s[i] == 'C' and s[z] == 'M':
                    value += 900
                    pop_list.append('CM')
                z += 1
                if z == len(s):
                    break
            # rem_valueszero = pop_list
            # rem_valuesone = value
            # print(rem_valuesone)

        import re
        z = 1
        new_str_final = s
        for i in range(len(s)):
                if len(s) > 1:
                    total = s[i] + s[z]
                    for item in pop_list:
                        if total == item:
                            new_str_final = re.sub(item,"",new_str_final)
                            break
                    z += 1
                    if z == len(s):
                        break
        new_value = 0
        for i in new_str_final:
            if i == 'M':
                new_value += 1000
            if i == 'D':
                new_value += 500
            if i == 'C':
                new_value += 100
            if i == 'L':
                new_value += 50
            if i == 'X':
                new_value += 10
            if i == 'V':
                new_value += 5
            if i == 'I':
                new_value += 1
        val = new_value + value
        return val
