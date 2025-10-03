"""
FelipedelosH
2025

Encryptor
"""
class Enigma:
    def __init__(self, base_path="config/.env"):
        self.alphabet = ""
        self.rotations = [0, 0, 0]
        self.actuatorBar = [0, 0, 0]
        self.rotorA = []
        self.rotorB = []
        self.rotorC = []
        self.initMachine(base_path)

    def initMachine(self, base_path):
        try:
            _keys = ""
            with open(base_path, "r", encoding="UTF-8") as f:
                _keys = f.read()

            self.alphabet = _keys.split("\n")[0].split("=")[-1]
            secret = _keys.split("\n")[1].split("=")[-1]
            self._buildRotorsWithSecret(secret)
        except:
            print("Error fatal... NO KEY detected.")

    def _buildRotorsWithSecret(self, secret):
        _total_chars = len(self.alphabet)
        s = str(secret).lower()
        vals = []
        first_seen = {}
        next_id = 1
        for ch in s:
            if ch not in first_seen:
                first_seen[ch] = next_id
                next_id += 1
            vals.append(first_seen[ch])

        if vals:
            rotations_a = sum(vals)
            rotations_a = sum([v for i, v in enumerate(vals) if i % 2 == 0])
            self.rotations[0] = rotations_a

            rotations_b = sum([v for i, v in enumerate(vals) if i % 3 == 0])
            rotations_b = rotations_b%_total_chars
            self.rotations[1] = rotations_b

            rotations_c = sum([v for i, v in enumerate(vals) if i % 5 == 0])
            rotations_c = rotations_c%_total_chars
            self.rotations[2] = rotations_c

        self._buildRotorsWithPositions()

    def _buildRotorsWithPositions(self):
        self.rotorA = []
        self.rotorB = []
        self.rotorC = []
        _total_chars = len(self.alphabet)
        for i in range(_total_chars):
            # RotorA
            idx_a_in  = i
            idx_a_out = (i + self.rotations[0] + self.actuatorBar[0]) % _total_chars
            self.rotorA.append(f"{self.alphabet[idx_a_in]}:{self.alphabet[idx_a_out]}")

            # RotorB
            idx_b_in  = (i + self.rotations[0] + self.actuatorBar[0]) % _total_chars
            idx_b_out = (i + self.rotations[1] + self.actuatorBar[1]) % _total_chars
            self.rotorB.append(f"{self.alphabet[idx_b_in]}:{self.alphabet[idx_b_out]}")

            # RotorC
            idx_c_in  = (i + self.rotations[1] + self.actuatorBar[1]) % _total_chars
            idx_c_out = (i + self.rotations[2] + self.actuatorBar[2]) % _total_chars
            self.rotorC.append(f"{self.alphabet[idx_c_in]}:{self.alphabet[idx_c_out]}")

    def processEncryptText(self, text):
        txt = ""
        self.actuatorBar = [0, 0, 0]
        for i in text:
            self._buildRotorsWithPositions()
            chr = str(i)
            isUpper = str(chr).isupper()

            if isUpper:
                chr = str(chr).lower()

            if chr not in self.alphabet:
                txt = txt + i
                continue
            
            if isUpper:
                txt = txt + str(self._processEncryptChr(chr)).upper()
            else:
                txt = txt + str(self._processEncryptChr(chr))
            self._actionActuatorBar()
 
        return txt 
    
    def _processEncryptChr(self, chr):
        _chr_pos = 0
        for itterChrA in self.rotorA:
            if f"{chr}:" in itterChrA:
                break
            _chr_pos = _chr_pos + 1

        temp = self.rotorA[_chr_pos]
        temp = str(temp).split(":")[-1]

        _chr_pos = 0
        for itterChrB in self.rotorB:
            if f"{temp}:" in itterChrB:
                break
            _chr_pos = _chr_pos + 1

        temp = self.rotorB[_chr_pos]
        temp = str(temp).split(":")[-1]

        _chr_pos = 0
        for itterChrC in self.rotorC:
            if f"{temp}:" in itterChrC:
                break
            _chr_pos = _chr_pos + 1

        temp = self.rotorC[_chr_pos]
        temp = str(temp).split(":")[-1]

        return temp

    def processDecryptText(self, text):
        txt = ""
        self.actuatorBar = [0, 0, 0]
        for i in text:
            self._buildRotorsWithPositions()
            chr = str(i)
            isUpper = str(chr).isupper()

            if isUpper:
                chr = str(chr).lower()

            if chr not in self.alphabet:
                txt = txt + i
                continue
            
            if isUpper:
                txt = txt + str(self._processDecryptChr(chr)).upper()
            else:
                txt = txt + str(self._processDecryptChr(chr))
            self._actionActuatorBar()

        return txt 

    def _processDecryptChr(self, chr):
        _chr_pos = 0
        for itterChrC in self.rotorC:
            if f":{chr}" in itterChrC:
                break
            _chr_pos = _chr_pos + 1

        temp = self.rotorC[_chr_pos]
        temp = str(temp).split(":")[0]

        _chr_pos = 0
        for itterChrB in self.rotorB:
            if f":{temp}" in itterChrB:
                break
            _chr_pos = _chr_pos + 1

        temp = self.rotorB[_chr_pos]
        temp = str(temp).split(":")[0]

        _chr_pos = 0
        for itterChrA in self.rotorA:
            if f":{temp}" in itterChrA:
                break
            _chr_pos = _chr_pos + 1

        temp = self.rotorA[_chr_pos]
        temp = str(temp).split(":")[0]

        return temp

    def _actionActuatorBar(self):
        self.actuatorBar[2] = self.actuatorBar[2] + 1
        if self.actuatorBar[2] >= len(self.alphabet):
            self.actuatorBar[2] = 0
            self.actuatorBar[1] = self.actuatorBar[1] + 1

        if self.actuatorBar[1] >= len(self.alphabet):
            self.actuatorBar[1] = 0
            self.actuatorBar[0] = self.actuatorBar[0] + 1

        if self.actuatorBar[0] >= len(self.alphabet):
            self.actuatorBar[0] = 0
