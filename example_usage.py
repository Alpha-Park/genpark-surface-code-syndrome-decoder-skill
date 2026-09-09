from client import SurfaceCodeSyndromeDecoder

def main():
    print("=== Testing Rotated Surface Code Syndrome Decoder ===")
    sc = SurfaceCodeSyndromeDecoder()
    sc.inject_x_error(1)
    syn = sc.measure_syndrome()
    print("Measured stabilizer syndrome:", syn)
    assert syn == [1, 1, 0, 0]

    sc.decode_and_correct(syn)
    assert sum(sc.data_qubits) == 0
    print("Data qubits after error correction:", sc.data_qubits)
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
