# class Poly:
    # def __init__(self, *coefficients):
        # self.coeffs = list(coefficients)

    # def __add__(self, other):
        # len_self = len(self.coeffs)
        # len_other = len(other.coeffs)
        # if len_self < len_other:
            # padded_self = [0] * (len_other - len_self) + self.coeffs
            # padded_other = other.coeffs[:]
        # else:
            # padded_self = self.coeffs[:]
            # padded_other = [0] * (len_self - len_other) + other.coeffs
        # result_coeffs = [a + b for a, b in zip(padded_self, padded_other)]
        # return Poly(*result_coeffs)

    # def __repr__(self):
        # return 

# """"
# a = Poly(1,2,3)  #an, ...., a0 
# b = Poly(1,0,1,1,2,3)
# c = a+b 
# print(c) #Poly ( 1,0,1, 2,4,6)"""


import os
import datetime

class File:
    def __init__(self, directory):
        self.directory = directory

    def getMaxSizeFile(self, n):
        files = [
            (f, os.path.getsize(os.path.join(self.directory, f)))
            for f in os.listdir(self.directory)
            if os.path.isfile(os.path.join(self.directory, f))
        ]
        # Sort by size in descending order
        files.sort(key=lambda x: x[1], reverse=True)
        # Return top 'n' filenames
        return [f[0] for f in files[:n]]

    def getLatestFiles(self, since_date):
        result = []
        for f in os.listdir(self.directory):
            full_path = os.path.join(self.directory, f)
            if os.path.isfile(full_path):
                modified_time = datetime.date.fromtimestamp(os.path.getmtime(full_path))
                if modified_time > since_date:
                    result.append(f)
        return result
