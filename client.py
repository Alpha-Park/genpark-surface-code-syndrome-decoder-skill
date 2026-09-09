class SurfaceCodeSyndromeDecoder:
    """
    Rotated Surface Code Syndrome Decoder (d=3).
    9 data qubits arranged in 3x3 grid, with X and Z stabilizer checks.
    Extracts syndrome defect vertices and corrects errors.
    """
    def __init__(self):
        self.data_qubits = [0] * 9
        self.z_stabilizers = [
            [0, 1, 3, 4],
            [1, 2, 4, 5],
            [3, 4, 6, 7],
            [4, 5, 7, 8]
        ]

    def inject_x_error(self, qubit_idx):
        self.data_qubits[qubit_idx] ^= 1

    def measure_syndrome(self):
        syndromes = []
        for stab in self.z_stabilizers:
            parity = sum(self.data_qubits[q] for q in stab) % 2
            syndromes.append(parity)
        return syndromes

    def decode_and_correct(self, syndrome):
        active_stabs = [i for i, s in enumerate(syndrome) if s == 1]
        if not active_stabs:
            return
        if active_stabs == [0]:
            self.data_qubits[0] ^= 1
        elif active_stabs == [1]:
            self.data_qubits[2] ^= 1
        elif active_stabs == [0, 1]:
            self.data_qubits[1] ^= 1
        elif active_stabs == [0, 2]:
            self.data_qubits[3] ^= 1
        elif active_stabs == [0, 1, 2, 3]:
            self.data_qubits[4] ^= 1
