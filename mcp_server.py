import sys
import json
from client import SurfaceCodeSyndromeDecoder

def handle_call(name, arguments):
    if name == "decode":
        err_q = arguments.get("qubit_error", 1)
        sc = SurfaceCodeSyndromeDecoder()
        sc.inject_x_error(err_q)
        syn = sc.measure_syndrome()
        sc.decode_and_correct(syn)
        return {"corrected": sum(sc.data_qubits) == 0, "syndrome": syn}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
