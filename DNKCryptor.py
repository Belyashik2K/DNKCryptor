class DNKCryptor:
    """
    Cryptor/decryptor for DNK string
    """
    def __init__(self) -> None:
        self.__DNK: str = ""
        self.__temp_len = 1
        self.__new_DNK: list = []

    def crypt_DNK(self, DNK: str) -> str:
        """
        Crypt DNK string
        
        Args:
            DNK (str): DNK string
            
        Returns:
            str: crypted DNK string
            
        Examples:
            >>> DC = DNKCryptor()
            >>> crypt_dnk = DC.crypt_DNK('AAAAAAATTTTTTTGGGGGGCCCCC')
            >>> print(crypt_dnk)
            A7T7G6C5
        """
        self.__clear_cache()
        self.__DNK = DNK
        for letter_i in range(len(self.__DNK) - 1):
            if self.__DNK[letter_i] == self.__DNK[letter_i + 1]:
                self.__temp_len += 1
            else:
                self.__new_DNK.append(self.__DNK[letter_i] + str(self.__temp_len))
                self.__temp_len = 1
        self.__new_DNK.append(self.__DNK[-1] + str(self.__temp_len))
        return "".join(self.__new_DNK)

    def decrypt_DNK(self, DNK: str) -> str:
        """
        Decrypt DNK string
        
        Args:
            DNK (str): DNK string
        
        Returns:
            str: decrypted DNK string
            
        Examples:
            >>> DC = DNKCryptor()
            >>> decrypt_dnk = DC.decrypt_DNK('A7T7G6C5')
            >>> print(decrypt_dnk)
            AAAAAAATTTTTTTGGGGGGCCCCC
        """
        self.__clear_cache()
        self.__DNK = DNK
        for letter_i in range(0, len(self.__DNK), 2):
            self.__new_DNK.append(self.__DNK[letter_i] * int(self.__DNK[letter_i + 1]))
        return "".join(self.__new_DNK)

    def __clear_cache(self) -> None:
        """
        Clear cache
        """
        self.__DNK = ''
        self.__temp_len = 1
        self.__new_DNK = []

def main():
    DC = DNKCryptor()
    crypt_dnk = DC.crypt_DNK('AAAAAAATTTTTTTGGGGGGCCCCC')
    print(crypt_dnk)
    decrypt_dnk = DC.decrypt_DNK('A7T7G6C5')
    print(decrypt_dnk)

if __name__ == "__main__":
    main()